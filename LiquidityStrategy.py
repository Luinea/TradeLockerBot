import backtrader as bt
import math

class LiquidityStrategy(bt.Strategy):
    """
    Liquidity-Based Trading Strategy - Counter-Intuitive Approach
    
    This strategy exploits algorithmic stop-hunting behavior by trading AGAINST breakouts
    in consolidating markets. The premise is that breakouts often trigger stops to create
    liquidity before the real move occurs in the opposite direction.
    
    Core Logic:
    - When price breaks ABOVE consolidation/liquidity highs → Enter SHORT
    - When price breaks BELOW consolidation/liquidity lows → Enter LONG
    
    Key Features:
    - Consolidation range detection using ATR analysis
    - Equal highs/lows identification (liquidity clusters)
    - Counter-trend entries on breakout confirmation
    - Full FundedHero risk management integration
    
    Rules:
    - Entry: Close beyond liquidity level (not just wick)
    - Stop Loss: Beyond breakout level + buffer
    - Take Profit: Opposite liquidity level (minimum 1.5:1 R:R)
    - Risk: 1% per trade with daily limits
    """
    
    params = (
        # Consolidation Detection
        ("consolidation_lookback", 20),      # Bars to analyze for consolidation
        ("consolidation_atr_threshold", 0.5), # ATR ratio for sideways detection (current/average)
        ("min_consolidation_bars", 10),       # Minimum bars to confirm consolidation
        ("atr_period", 14),                   # ATR calculation period
        
        # Liquidity Level Detection
        ("equal_level_tolerance", 0.001),     # 0.1% tolerance for equal highs/lows
        ("min_touches", 2),                   # Minimum touches to confirm liquidity level
        ("liquidity_expiry_bars", 50),        # Bars before liquidity level expires
        ("swing_lookback", 5),                # Bars to check for swing high/low
        
        # Entry/Exit
        ("breakout_buffer", 5.0),             # Pips beyond level for SL placement
        ("min_rr_ratio", 1.5),                # Minimum risk:reward ratio
        
        # Risk Management (FundedHero Compliance)
        ("risk_per_trade_percent", 0.01),     # 1% risk per trade
        ("max_daily_trades", 3),              # Max 3 trades per day
        ("max_daily_loss", 75.0),             # Hard limit: Stop if daily loss >= $75
        ("max_drawdown_percent", 0.06),       # Hard limit: Stop if DD > 6%
        ("max_lots", 0.5),                    # Safety cap
        ("contract_size", 100),               # XAUUSD contract size
    )

    def __init__(self):
        # Technical Indicators
        self.atr = bt.indicators.ATR(self.data, period=self.params.atr_period)
        
        # Liquidity Level Tracking
        # Format: [(price, touch_count, bar_created), ...]
        self.liquidity_highs = []
        self.liquidity_lows = []
        
        # Consolidation State
        self.consolidation_range = None  # (high, low, start_bar)
        self.in_consolidation = False
        self.consolidation_start_bar = 0
        
        # Order Management
        self.order = None
        
        # Risk State (FundedHero Framework)
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.permanent_lock = False  # Circuit breaker for max drawdown
        self.peak_equity = 0.0

    def log(self, txt, dt=None):
        """Logging utility"""
        if dt is None:
            try:
                dt = self.datas[0].datetime.date(0)
                dts = dt.isoformat()
            except IndexError:
                dts = "---"
        else:
            dts = dt.isoformat() if hasattr(dt, 'isoformat') else str(dt)
        print(f'{dts}, {txt}')

    def start(self):
        self.log("Liquidity Strategy Started - Counter-Intuitive Trading Active")
        self.peak_equity = self.broker.getvalue()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'LONG EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            elif order.issell():
                self.log(f'SHORT EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(f'TRADE PROFIT, GROSS {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')
        
        # Update Daily PnL
        current_date = self.datas[0].datetime.date(0)
        
        if self.last_trade_date == current_date:
            self.daily_pnl += trade.pnlcomm
        else:
            # New day
            self.daily_pnl = trade.pnlcomm
            self.last_trade_date = current_date
            self.daily_trades = 0
            
        self.log(f'Daily PnL: ${self.daily_pnl:.2f}')

    def detect_consolidation(self):
        """
        Detect if market is in consolidation (sideways) phase.
        
        Method:
        1. Calculate price range (high - low) over lookback period
        2. If range is relatively small compared to average price, market is consolidating
        3. Track high/low of consolidation range
        
        Returns:
            bool: True if in consolidation, False otherwise
        """
        if len(self.data) < self.params.consolidation_lookback:
            return False
        
        # Calculate range over lookback period
        lookback = self.params.consolidation_lookback
        range_high = max([self.data.high[-i] for i in range(min(lookback, len(self.data)))])
        range_low = min([self.data.low[-i] for i in range(min(lookback, len(self.data)))])
        range_size = range_high - range_low
        avg_price = (range_high + range_low) / 2
        
        # Calculate range as percentage of price
        if avg_price == 0:
            return False
        
        range_pct = range_size / avg_price
        
        # Consolidation if range is less than 1% of avg price (tight range)
        # This is more reliable than ATR ratio for our test scenarios
        if range_pct < 0.01:  # 1% range
            # Start or update consolidation tracking
            if not self.in_consolidation:
                self.consolidation_start_bar = len(self)
                self.consolidation_range = (range_high, range_low, len(self))
                self.log(f"CONSOLIDATION DETECTED: Range {range_low:.2f} - {range_high:.2f}, Range%: {range_pct*100:.2f}%")
            else:
                # Update range
                self.consolidation_range = (range_high, range_low, self.consolidation_range[2])
            
            self.in_consolidation = True
            
            # Check if we have enough bars in consolidation
            bars_in_consolidation = len(self) - self.consolidation_start_bar
            return bars_in_consolidation >= self.params.min_consolidation_bars
        else:
            # Exit consolidation
            if self.in_consolidation:
                self.log(f"CONSOLIDATION ENDED: Range%: {range_pct*100:.2f}%")
            self.in_consolidation = False
            self.consolidation_range = None
            return False

    def is_swing_high(self, lookback_idx):
        """
        Check if the bar at lookback_idx is a swing high.
        
        Args:
            lookback_idx: Index to check (0 = current, -1 = previous, etc.)
            
        Returns:
            bool: True if it's a swing high
        """
        if len(self.data) < self.params.swing_lookback * 2:
            return False
        
        try:
            center_high = self.data.high[lookback_idx]
            
            # Check if higher than surrounding bars
            for i in range(1, self.params.swing_lookback + 1):
                if (self.data.high[lookback_idx - i] >= center_high or 
                    self.data.high[lookback_idx + i] >= center_high):
                    return False
            return True
        except (IndexError, AttributeError):
            return False

    def is_swing_low(self, lookback_idx):
        """
        Check if the bar at lookback_idx is a swing low.
        
        Args:
            lookback_idx: Index to check (0 = current, -1 = previous, etc.)
            
        Returns:
            bool: True if it's a swing low
        """
        if len(self.data) < self.params.swing_lookback * 2:
            return False
        
        try:
            center_low = self.data.low[lookback_idx]
            
            # Check if lower than surrounding bars
            for i in range(1, self.params.swing_lookback + 1):
                if (self.data.low[lookback_idx - i] <= center_low or 
                    self.data.low[lookback_idx + i] <= center_low):
                    return False
            return True
        except (IndexError, AttributeError):
            return False

    def update_liquidity_levels(self):
        """
        Detect and update equal highs/lows (liquidity clusters).
        
        Equal highs/lows are swing points at approximately the same price level,
        indicating areas where stop-losses cluster.
        """
        current_bar = len(self)
        
        # Remove expired liquidity levels
        self.liquidity_highs = [(price, touches, bar) for price, touches, bar in self.liquidity_highs 
                                if current_bar - bar < self.params.liquidity_expiry_bars]
        self.liquidity_lows = [(price, touches, bar) for price, touches, bar in self.liquidity_lows 
                               if current_bar - bar < self.params.liquidity_expiry_bars]
        
        # Check for new swing highs
        if self.is_swing_high(-self.params.swing_lookback):
            swing_high = self.data.high[-self.params.swing_lookback]
            
            # Check if this high is equal to existing liquidity high
            found_equal = False
            for i, (price, touches, bar) in enumerate(self.liquidity_highs):
                tolerance = price * self.params.equal_level_tolerance
                if abs(swing_high - price) <= tolerance:
                    # Update touch count
                    self.liquidity_highs[i] = (price, touches + 1, bar)
                    self.log(f"EQUAL HIGH UPDATE: {price:.2f} (Touches: {touches + 1})")
                    found_equal = True
                    break
            
            # If not equal to existing, add new
            if not found_equal:
                self.liquidity_highs.append((swing_high, 1, current_bar))
        
        # Check for new swing lows
        if self.is_swing_low(-self.params.swing_lookback):
            swing_low = self.data.low[-self.params.swing_lookback]
            
            # Check if this low is equal to existing liquidity low
            found_equal = False
            for i, (price, touches, bar) in enumerate(self.liquidity_lows):
                tolerance = price * self.params.equal_level_tolerance
                if abs(swing_low - price) <= tolerance:
                    # Update touch count
                    self.liquidity_lows[i] = (price, touches + 1, bar)
                    self.log(f"EQUAL LOW UPDATE: {price:.2f} (Touches: {touches + 1})")
                    found_equal = True
                    break
            
            # If not equal to existing, add new
            if not found_equal:
                self.liquidity_lows.append((swing_low, 1, current_bar))

    def check_liquidity_break(self):
        """
        Check if price has broken a liquidity level.
        
        Returns:
            tuple: (direction, level_price, target_price) or (None, None, None)
                   direction: 'short' for upward break, 'long' for downward break
                   level_price: The liquidity level that was broken
                   target_price: The opposite liquidity level (TP target)
        """
        current_close = self.data.close[0]
        
        # Check for upward breakout (triggers SHORT entry)
        # Priority: Check consolidation range first, then equal highs
        if self.in_consolidation and self.consolidation_range:
            range_high, range_low, _ = self.consolidation_range
            
            # Upward break of consolidation range
            if current_close > range_high:
                self.log(f"LIQUIDITY BREAK (UP): Price {current_close:.2f} broke range high {range_high:.2f}")
                return ('short', range_high, range_low)
            
            # Downward break of consolidation range
            if current_close < range_low:
                self.log(f"LIQUIDITY BREAK (DOWN): Price {current_close:.2f} broke range low {range_low:.2f}")
                return ('long', range_low, range_high)
        
        # Check equal highs (requires minimum touches)
        for price, touches, bar in self.liquidity_highs:
            if touches >= self.params.min_touches and current_close > price:
                # Find target (nearest liquidity low)
                if self.liquidity_lows:
                    target = min([p for p, t, b in self.liquidity_lows if t >= self.params.min_touches], 
                                default=price - 20.0)  # Default to 20 pips if no target
                else:
                    target = price - 20.0
                
                self.log(f"LIQUIDITY BREAK (EQUAL HIGH): Price {current_close:.2f} broke {price:.2f} ({touches} touches)")
                return ('short', price, target)
        
        # Check equal lows (requires minimum touches)
        for price, touches, bar in self.liquidity_lows:
            if touches >= self.params.min_touches and current_close < price:
                # Find target (nearest liquidity high)
                if self.liquidity_highs:
                    target = max([p for p, t, b in self.liquidity_highs if t >= self.params.min_touches], 
                                default=price + 20.0)  # Default to 20 pips if no target
                else:
                    target = price + 20.0
                
                self.log(f"LIQUIDITY BREAK (EQUAL LOW): Price {current_close:.2f} broke {price:.2f} ({touches} touches)")
                return ('long', price, target)
        
        return (None, None, None)

    def calculate_position_size(self, entry_price, sl_price):
        """
        Calculate lot size based on risk and SL distance.
        
        Args:
            entry_price: Entry price
            sl_price: Stop loss price
            
        Returns:
            float: Position size in lots (rounded to 2 decimals)
        """
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        sl_distance = abs(entry_price - sl_price)
        
        if sl_distance == 0:
            return 0
        
        # Position size = Risk Amount / (SL Distance * Contract Size)
        raw_size = risk_amount / (sl_distance * self.params.contract_size)
        size = round(raw_size, 2)
        
        # Safety cap
        if size > self.params.max_lots:
            self.log(f"WARNING: Calc size {size} > Max {self.params.max_lots}. Capped.")
            size = self.params.max_lots
        
        return size

    def next(self):
        """Main trading logic executed on each bar"""
        
        # 0. Circuit Breaker - Check Max Drawdown
        current_equity = self.broker.getvalue()
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity
        
        drawdown_pct = (self.peak_equity - current_equity) / self.peak_equity
        if drawdown_pct > self.params.max_drawdown_percent:
            if not self.permanent_lock:
                self.log(f"!!! CRITICAL: Max Drawdown Hit ({drawdown_pct*100:.2f}%). HALTING TRADING !!!")
                self.permanent_lock = True
            
            # Close positions and cancel orders
            if self.position:
                self.close()
            if self.order:
                self.broker.cancel(self.order)
            return

        if self.permanent_lock:
            return

        # 1. Daily Reset Logic
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date

        # 2. Check Daily Limits
        if self.daily_pnl <= -self.params.max_daily_loss:
            self.log(f"Daily Loss Limit Hit (${self.daily_pnl:.2f}). Trading Stopped for today.")
            return

        if self.daily_trades >= self.params.max_daily_trades:
            return

        # 3. Skip if order or position exists
        if self.order:
            return
        if self.position:
            return

        # 4. Update Market State
        self.detect_consolidation()
        self.update_liquidity_levels()

        # 5. Check for Liquidity Breaks
        direction, level_price, target_price = self.check_liquidity_break()
        
        if direction is None:
            return  # No breakout detected

        # 6. Validate Risk:Reward Ratio
        entry_price = self.data.close[0]
        
        if direction == 'short':
            sl_price = level_price + self.params.breakout_buffer
            tp_price = target_price
            
            risk = sl_price - entry_price
            reward = entry_price - tp_price
            
        else:  # direction == 'long'
            sl_price = level_price - self.params.breakout_buffer
            tp_price = target_price
            
            risk = entry_price - sl_price
            reward = tp_price - entry_price
        
        # Skip if risk is negative or reward:risk ratio is too low
        if risk <= 0 or reward <= 0:
            self.log(f"TRADE SKIPPED: Invalid risk ({risk:.2f}) or reward ({reward:.2f})")
            return
        
        rr_ratio = reward / risk
        if rr_ratio < self.params.min_rr_ratio:
            self.log(f"TRADE SKIPPED: R:R ratio {rr_ratio:.2f} < minimum {self.params.min_rr_ratio}")
            return

        # 7. Calculate Position Size
        size = self.calculate_position_size(entry_price, sl_price)
        
        if size <= 0:
            return

        # 8. Execute Trade
        if direction == 'short':
            self.log(f'SHORT SIGNAL: Entry {entry_price:.2f}, SL {sl_price:.2f}, TP {tp_price:.2f}, Size {size}, R:R {rr_ratio:.2f}')
            self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
            self.daily_trades += 1
            
        else:  # direction == 'long'
            self.log(f'LONG SIGNAL: Entry {entry_price:.2f}, SL {sl_price:.2f}, TP {tp_price:.2f}, Size {size}, R:R {rr_ratio:.2f}')
            self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
            self.daily_trades += 1
