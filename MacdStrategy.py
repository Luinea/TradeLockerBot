import backtrader as bt
import math

class MacdStrategy(bt.Strategy):
    """
    Enhanced MACD Strategy based on TradingLab methodology.
    
    Optimizations (2025-12-10):
    - min_sl_distance: 20 pips (increased from 10) for XAUUSD volatility
    - ema_sl_multiplier: 1.5x (increased from 1.0) for trend breathing room
    
    Rules:
    - LONG: MACD crosses above signal BELOW zero line + price above 200 EMA + near support
    - SHORT: MACD crosses below signal ABOVE zero line + price below 200 EMA + near resistance
    - Stop Loss: Max of (EMA distance * multiplier, min distance)
    - Take Profit: 1.5x risk/reward ratio
    - Support/Resistance: Detected via swing high/low analysis
    """
    
    params = (
        ("macd_fast", 12),
        ("macd_slow", 26),
        ("macd_signal", 9),
        ("ema_period", 200),
        
        # Risk Limits
        ("risk_per_trade_percent", 0.01),  # 1% risk
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),     # Hard limit: Stop if daily loss >= $75
        ("max_drawdown_percent", 0.06), # Hard limit: Stop usage if DD > 6% (Buffer for 12% limit)
        ("max_lots", 0.5),            # Safety cap to prevent fat-finger/math errors
        
        # Symbol specifics
        ("contract_size", 100),
        
        # TradingLab Enhanced Parameters
        ("min_sl_distance", 20.0),     # Min SL: 20 pips for XAUUSD volatility (optimized from 10.0)
        ("ema_sl_multiplier", 1.5),    # EMA SL multiplier: 1.5x for breathing room (optimized from 1.0)
        ("tp_risk_reward", 1.5),       # R:R ratio: 1.5:1 per TradingLab
        
        # Support/Resistance Detection
        ("sr_lookback", 20),           # Bars to look back for swing highs/lows
        ("sr_threshold", 5.0),         # Price must be within this distance to S/R
        ("use_sr_filter", True),       # Toggle S/R filtering
    )

    def __init__(self):
        self.macd = bt.indicators.MACD(
            self.data.close,
            period_me1=self.params.macd_fast,
            period_me2=self.params.macd_slow,
            period_signal=self.params.macd_signal
        )
        self.ema = bt.indicators.ExponentialMovingAverage(
            self.data.close,
            period=self.params.ema_period
        )
        self.crossover = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
        
        self.order = None
        
        # Risk State
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.permanent_lock = False # Liquidation prevention
        self.peak_equity = 0.0
        
        # Support/Resistance Tracking
        self.support_levels = []
        self.resistance_levels = []

    def log(self, txt, dt=None):
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
        self.log("Strategy Started with Risk Hardening")
        self.peak_equity = self.broker.getvalue()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(f'TRADE PROFIT, GROSS {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')
        
        # Update Daily PnL
        # Note: Backtrader triggers notify_trade on current date, but trade might have opened previous day.
        # Ideally we track PnL realized TODAY.
        current_date = self.datas[0].datetime.date(0)
        
        # If trade closed today, add to daily PnL
        if self.last_trade_date == current_date:
            self.daily_pnl += trade.pnlcomm
        else:
            # If we somehow closed a trade on a new day before next() ran (unlikely but possible with stops)
            # Reset daily PnL first if date mismatch
            self.daily_pnl = trade.pnlcomm
            self.last_trade_date = current_date
            self.daily_trades = 0 # It's a new day effectively
            
        self.log(f'Daily PnL: ${self.daily_pnl:.2f}')
    
    def detect_sr_levels(self):
        """
        Detect support and resistance levels using swing highs/lows.
        Support: Swing lows where price bounced up
        Resistance: Swing highs where price bounced down
        """
        if len(self.data) < self.params.sr_lookback + 2:
            return
        
        lookback = self.params.sr_lookback
        support_candidates = []
        resistance_candidates = []
        
        # Find swing lows (potential support)
        for i in range(2, lookback):
            if i >= len(self.data):
                break
            # Check if it's a swing low (lower than both neighbors)
            try:
                if (self.data.low[-i] < self.data.low[-i-1] and 
                    self.data.low[-i] < self.data.low[-i+1]):
                    support_candidates.append(self.data.low[-i])
            except (IndexError, AttributeError):
                break
        
        # Find swing highs (potential resistance)
        for i in range(2, lookback):
            if i >= len(self.data):
                break
            # Check if it's a swing high (higher than both neighbors)
            try:
                if (self.data.high[-i] > self.data.high[-i-1] and 
                    self.data.high[-i] > self.data.high[-i+1]):
                    resistance_candidates.append(self.data.high[-i])
            except (IndexError, AttributeError):
                break
        
        # Keep only the 5 most recent levels to prevent list growth
        self.support_levels = support_candidates[-5:] if support_candidates else []
        self.resistance_levels = resistance_candidates[-5:] if resistance_candidates else []
    
    def near_support(self):
        """
        Check if current price is near a support level.
        Returns True if price is within sr_threshold of any support.
        """
        if not self.support_levels:
            return False
        
        current_price = self.data.close[0]
        for support in self.support_levels:
            if abs(current_price - support) <= self.params.sr_threshold:
                return True
        return False
    
    def near_resistance(self):
        """
        Check if current price is near a resistance level.
        Returns True if price is within sr_threshold of any resistance.
        """
        if not self.resistance_levels:
            return False
        
        current_price = self.data.close[0]
        for resistance in self.resistance_levels:
            if abs(current_price - resistance) <= self.params.sr_threshold:
                return True
        return False

    def next(self):
        # 0. Check Permanent Lock (Circuit Breaker)
        current_equity = self.broker.getvalue()
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity
            
        drawdown_pct = (self.peak_equity - current_equity) / self.peak_equity
        if drawdown_pct > self.params.max_drawdown_percent:
            if not self.permanent_lock:
                self.log(f"!!! CRITICAL: Max Drawdown Hit ({drawdown_pct*100:.2f}%). HALTING TRADING & LIQUIDATING !!!")
                self.permanent_lock = True
                
            # Close any open positions immediately
            if self.position:
                self.close()
            # Cancel any pending orders
            if self.order:
                self.broker.cancel(self.order)
            return

        if self.permanent_lock:
            return

        # 1. Date & Daily Reset
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date
            # self.log(f"New Day: {current_date}")

        # 2. Check Daily Limits
        if self.daily_pnl <= -self.params.max_daily_loss:
            self.log(f"Daily Loss Limit Hit (${self.daily_pnl:.2f}). Trading Stopped for today.")
            return

        if self.daily_trades >= self.params.max_daily_trades:
            return
            
        # 3. Existing Orders/Positions
        if self.order: return
        if self.position: return
        
        # 4. Detect Support/Resistance Levels (if enabled)
        if self.params.use_sr_filter:
            self.detect_sr_levels()

        # 5. Entry Logic with TradingLab Rules
        # LONG Entry Conditions:
        # 1. MACD crosses above signal BELOW zero line
        # 2. Price is above 200 EMA
        # 3. Price is near support (if S/R filter enabled)
        long_condition = (
            self.crossover > 0 and                    # MACD bullish crossover
            self.macd.macd[-1] < 0 and               # MACD was below zero before cross
            self.macd.signal[-1] < 0 and             # Signal was below zero before cross
            self.data.close[0] > self.ema[0] and     # Price above 200 EMA
            (not self.params.use_sr_filter or self.near_support())  # Near support if filter enabled
        )
        
        # SHORT Entry Conditions:
        # 1. MACD crosses below signal ABOVE zero line
        # 2. Price is below 200 EMA
        # 3. Price is near resistance (if S/R filter enabled)
        short_condition = (
            self.crossover < 0 and                    # MACD bearish crossover
            self.macd.macd[-1] > 0 and               # MACD was above zero before cross
            self.macd.signal[-1] > 0 and             # Signal was above zero before cross
            self.data.close[0] < self.ema[0] and     # Price below 200 EMA
            (not self.params.use_sr_filter or self.near_resistance())  # Near resistance if filter enabled
        )
        
        # Calculate risk amount
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        
        # LONG Entry Execution
        if long_condition:
            entry_price = self.data.close[0]
            
            # Calculate SL based on distance to 200 EMA
            ema_distance = abs(entry_price - self.ema[0])
            sl_dist = max(ema_distance * self.params.ema_sl_multiplier, self.params.min_sl_distance)
            
            # Calculate position size based on risk and SL distance
            raw_size = risk_amount / (sl_dist * self.params.contract_size)
            size = round(raw_size, 2)
            
            # Safety cap
            if size > self.params.max_lots:
                self.log(f"WARNING: Calc size {size} > Max {self.params.max_lots}. Capped.")
                size = self.params.max_lots
            
            if size <= 0:
                return
            
            sl_price = entry_price - sl_dist
            tp_price = entry_price + (sl_dist * self.params.tp_risk_reward)
            
            self.log(f'BUY CREATE {size} lots, Entry: {entry_price:.2f}, SL: {sl_price:.2f} (dist: {sl_dist:.2f}), TP: {tp_price:.2f}')
            self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
            self.daily_trades += 1
            
        # SHORT Entry Execution
        elif short_condition:
            entry_price = self.data.close[0]
            
            # Calculate SL based on distance to 200 EMA
            ema_distance = abs(entry_price - self.ema[0])
            sl_dist = max(ema_distance * self.params.ema_sl_multiplier, self.params.min_sl_distance)
            
            # Calculate position size based on risk and SL distance
            raw_size = risk_amount / (sl_dist * self.params.contract_size)
            size = round(raw_size, 2)
            
            # Safety cap
            if size > self.params.max_lots:
                self.log(f"WARNING: Calc size {size} > Max {self.params.max_lots}. Capped.")
                size = self.params.max_lots
            
            if size <= 0:
                return
            
            sl_price = entry_price + sl_dist
            tp_price = entry_price - (sl_dist * self.params.tp_risk_reward)
            
            self.log(f'SELL CREATE {size} lots, Entry: {entry_price:.2f}, SL: {sl_price:.2f} (dist: {sl_dist:.2f}), TP: {tp_price:.2f}')
            self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
            self.daily_trades += 1
