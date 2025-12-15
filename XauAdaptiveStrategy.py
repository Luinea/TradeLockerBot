import backtrader as bt
import math


class XauAdaptiveStrategy(bt.Strategy):
    """
    Hybrid Regime-Aware XAU/USD Strategy.
    
    Combines TWO approaches based on market regime:
    
    1. TRENDING REGIME (ADX > 25 + aligned EMAs):
       - Uses EMA Ribbon pullback entries
       - Ignores Asian range completely
       - Best for strong directional moves (Jul-Sep 2025 type)
    
    2. RANGING REGIME (ADX < 25 or EMAs not aligned):
       - Uses Asian Range Breakout logic
       - Waits for clean break of Asian session box
       - Best for choppy sideways markets
    
    This solves the problem where:
    - Asian breakout failed in trending markets (-40%)
    - Simple EMA pullback missed opportunities in choppy markets
    
    The strategy automatically detects which regime we're in and applies
    the appropriate entry logic.
    """
    
    params = (
        # === REGIME DETECTION WITH HYSTERESIS ===
        ("adx_period", 14),
        ("adx_trend_enter", 30),   # ADX must exceed 30 to ENTER trending mode
        ("adx_trend_exit", 20),    # ADX must fall below 20 to EXIT trending mode
        # Dead Zone: ADX 20-30 = No new trades (prevents whipsaw)
        ("adx_min_threshold", 12), # Don't trade AT ALL if ADX < 12 (market is dead)
        ("atr_min_pips", 3.0),     # Don't trade if ATR < 3 pips (range too tight for scalping)
        ("require_rising_adx", True), # NEW: Only enter when ADX is rising (momentum building)
        ("bb_period", 20),
        ("bb_dev", 2.0),
        
        # === TREND FOLLOWING (EMA Ribbon) ===
        ("ema_fast", 8),
        ("ema_medium", 21),
        ("ema_slow", 50),
        
        # === MEAN REVERSION (BB+RSI+Stoch) - for ranging ===
        ("rsi_period", 14),
        ("rsi_oversold", 30),
        ("rsi_overbought", 70),
        ("stoch_k", 5),
        ("stoch_d", 3),
        ("stoch_slow", 3),
        ("stoch_oversold", 25),
        ("stoch_overbought", 75),
        
        # === ASIAN RANGE BREAKOUT (for ranging regime) ===
        ("asian_start_hour", 1),   # 01:00 GMT - Range starts
        ("asian_end_hour", 8),     # 08:00 GMT - Range ends
        ("trade_start_hour", 8),   # 08:00 GMT - Trading begins
        ("trade_end_hour", 17),    # 17:00 GMT - No new entries
        ("breakout_buffer", 0.5),  # Pips buffer for breakout
        
        # === HEIKIN-ASHI FILTER ===
        ("use_ha_filter", True),  # Require HA color alignment
        
        # === ATR & RISK ===
        ("atr_period", 14),
        ("atr_sl_multiplier", 2.0),  # WIDENED from 1.5 to give trades more room
        ("tp_risk_reward", 1.0),    # 1:1 R:R for scalping (faster wins)
        ("max_hold_minutes", 60),   # Time-based exit: cut trade if no TP/SL in 60 mins
        
        # === RISK MANAGEMENT ===
        ("risk_per_trade_percent", 0.01),
        ("max_daily_trades", 2),  # Reduced from 3 to be more selective
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06),
        ("max_lots", 0.5),
        ("contract_size", 100),
        ("cooldown_minutes", 30),  # Wait 30 mins between trades to let market reset
        
        # === TREND DIRECTION FILTER ===
        ("ema_macro", 200),  # EMA 200 for macro trend
        ("trade_with_trend_only", True),  # Only long above EMA200, short below
        
        # === MOMENTUM BREAKOUT (RANGING REGIME) ===
        ("use_mean_reversion", False),  # DISABLED: Too many false breakouts in Apr-Jun 2024
        
        # === CHOPPY MARKET IMPROVEMENTS (Dec 2024) ===
        # Multi-bar confirmation - requires price to stay above/below EMA for multiple bars
        ("pullback_confirm_bars", 2),   # Require 2 bars of confirmation before entry
        
        # RSI alignment filter - ensures momentum aligns with trade direction
        ("trend_rsi_long_min", 45),     # RSI must be > 45 for long entries (not oversold = momentum up)
        ("trend_rsi_short_max", 55),    # RSI must be < 55 for short entries (not overbought = momentum down)
        
        # ATR expansion filter - don't enter when volatility is spiking (not a true pullback)
        ("atr_expansion_limit", 1.2),   # Skip if ATR expanded > 20% from previous bar
        
        # Extended hold time for trend trades (trends need time to develop)
        ("trend_hold_minutes", 120),    # 2 hours for trend trades vs 60 mins for ranging
        
        # Stronger trend requirement for pullback entries
        ("adx_strong_trend", 35),       # ADX must exceed 35 for Trend Pullback entry
        
        # Trailing stop - move to breakeven after profit
        ("use_trailing_stop", True),    # Enable breakeven + trailing stop
        ("breakeven_atr_mult", 1.0),    # Move SL to breakeven after 1x ATR profit
        ("trail_atr_mult", 0.5),        # Trail stop by 0.5x ATR after breakeven
    )

    def __init__(self):
        # === REGIME DETECTION INDICATORS ===
        self.adx = bt.indicators.ADX(self.data, period=self.params.adx_period)
        self.bb = bt.indicators.BollingerBands(
            self.data.close, period=self.params.bb_period, devfactor=self.params.bb_dev
        )
        
        # === TREND FOLLOWING INDICATORS ===
        self.ema_fast = bt.indicators.EMA(self.data.close, period=self.params.ema_fast)
        self.ema_medium = bt.indicators.EMA(self.data.close, period=self.params.ema_medium)
        self.ema_slow = bt.indicators.EMA(self.data.close, period=self.params.ema_slow)
        
        # === MEAN REVERSION INDICATORS ===
        self.rsi = bt.indicators.RSI(self.data.close, period=self.params.rsi_period)
        self.stoch = bt.indicators.Stochastic(
            self.data, period=self.params.stoch_k,
            period_dfast=self.params.stoch_d, period_dslow=self.params.stoch_slow
        )
        
        # === ATR ===
        self.atr = bt.indicators.ATR(self.data, period=self.params.atr_period)
        
        # === MACRO TREND FILTER ===
        self.ema_macro = bt.indicators.EMA(self.data.close, period=self.params.ema_macro)
        
        # === HEIKIN-ASHI STATE ===
        self.ha_open = None
        self.ha_close = None
        self.prev_ha_open = None
        self.prev_ha_close = None
        self.ha_color = None  # 'GREEN' or 'RED'
        
        # === PULLBACK TRACKING (for trending regime) ===
        self.in_pullback_zone = False
        self.pullback_direction = None
        
        # === ASIAN RANGE TRACKING (for ranging regime) ===
        self.asian_range_high = None
        self.asian_range_low = None
        self.asian_range_formed = False
        self.traded_breakout_today = False  # Only one breakout per day
        
        # === STATE ===
        self.order = None
        self.bracket_orders = []  # Store bracket orders so we can cancel them on time exit
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.daily_peak_equity = 0.0
        self.current_regime = None
        self.locked_regime = None  # Hysteresis: remembers last confirmed regime
        self.last_trade_time = None  # Cooldown: time of last trade close
        self.entry_time = None  # Time-based exit: when current trade was opened
        self.is_mean_reversion_trade = False  # Flag to use middle BB as TP
        
        # === TRAILING STOP STATE (Dec 2024) ===
        self.entry_price = None          # Price at entry for breakeven calculation
        self.entry_atr = None            # ATR at entry for trailing stop distance
        self.entry_regime = None         # Regime at entry (for hold time logic)
        self.is_breakeven = False        # Has SL been moved to breakeven?
        self.trailing_stop_price = None  # Current trailing stop level

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
        self.log("XAU Hybrid Adaptive Strategy Started")
        self.daily_peak_equity = self.broker.getvalue()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status == order.Completed:
            action = 'BUY' if order.isbuy() else 'SELL'
            self.log(f'{action} EXECUTED @ {order.executed.price:.2f}, Size: {order.executed.size:.2f}')
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log(f'TRADE PROFIT: ${trade.pnlcomm:.2f} [Regime: {self.current_regime}]')
        
        # Record time of trade close for cooldown
        self.last_trade_time = self.datas[0].datetime.datetime(0)
        
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date == current_date:
            self.daily_pnl += trade.pnlcomm
        else:
            self.daily_pnl = trade.pnlcomm
            self.last_trade_date = current_date
            self.daily_trades = 0
        
        # Reset entry time (trade is now closed)
        self.entry_time = None
        self.bracket_orders = []  # Clear bracket orders - trade completed normally

    def calculate_heikin_ashi(self):
        """Calculate Heikin-Ashi candle and determine color."""
        o, h, l, c = self.data.open[0], self.data.high[0], self.data.low[0], self.data.close[0]
        
        self.ha_close = (o + h + l + c) / 4.0
        
        if self.prev_ha_open is None or self.prev_ha_close is None:
            self.ha_open = (o + c) / 2.0
        else:
            self.ha_open = (self.prev_ha_open + self.prev_ha_close) / 2.0
        
        self.ha_color = 'GREEN' if self.ha_close > self.ha_open else 'RED'
        
        self.prev_ha_open = self.ha_open
        self.prev_ha_close = self.ha_close

    def detect_regime(self):
        """
        Detect market regime with HYSTERESIS to prevent whipsaw.
        
        - ADX > 30 AND EMAs aligned = Enter TRENDING mode
        - ADX < 20 = Exit TRENDING, enter RANGING mode
        - ADX 20-30 = DEAD ZONE (keep previous regime, take no new trades)
        
        Hysteresis prevents constant switching when ADX oscillates around threshold.
        """
        adx_val = self.adx.adx[0]
        ema_aligned = self.check_ema_stack() is not None
        
        # === HYSTERESIS LOGIC ===
        # If we're in TRENDING and ADX drops below exit threshold, switch to RANGING
        if self.locked_regime == 'TRENDING':
            if adx_val < self.params.adx_trend_exit:
                self.locked_regime = 'RANGING'
                self.log(f"REGIME CHANGE: TRENDING -> RANGING (ADX={adx_val:.1f} < {self.params.adx_trend_exit})")
            elif not ema_aligned:
                # EMAs no longer aligned, enter dead zone
                return 'DEAD_ZONE'
            else:
                return 'TRENDING'
        
        # If we're in RANGING and ADX rises above enter threshold with EMAs aligned
        elif self.locked_regime == 'RANGING':
            if adx_val > self.params.adx_trend_enter and ema_aligned:
                self.locked_regime = 'TRENDING'
                self.log(f"REGIME CHANGE: RANGING -> TRENDING (ADX={adx_val:.1f} > {self.params.adx_trend_enter})")
                return 'TRENDING'
            else:
                return 'RANGING'
        
        # First time - initialize regime
        else:
            if adx_val > self.params.adx_trend_enter and ema_aligned:
                self.locked_regime = 'TRENDING'
                return 'TRENDING'
            elif adx_val < self.params.adx_trend_exit:
                self.locked_regime = 'RANGING'
                return 'RANGING'
            else:
                # In the dead zone on startup - default to RANGING (safer)
                self.locked_regime = 'RANGING'
                return 'DEAD_ZONE'
        
        return self.locked_regime

    def check_ema_stack(self):
        """Check EMA alignment for trend direction."""
        fast, medium, slow = self.ema_fast[0], self.ema_medium[0], self.ema_slow[0]
        if fast > medium > slow:
            return 'BULLISH'
        elif fast < medium < slow:
            return 'BEARISH'
        return None

    def in_pullback_zone_check(self, direction):
        """Check if price is in the pullback value zone."""
        price_low, price_high = self.data.low[0], self.data.high[0]
        fast, medium = self.ema_fast[0], self.ema_medium[0]
        
        if direction == 'BULLISH':
            return price_low <= fast and price_low >= medium
        elif direction == 'BEARISH':
            return price_high >= fast and price_high <= medium
        return False

    def get_current_hour(self):
        """Get current hour from data."""
        try:
            return self.datas[0].datetime.datetime(0).hour
        except:
            return 0

    def is_trading_hours(self):
        """Check if we're in trading hours (08:00-17:00 GMT)."""
        hour = self.get_current_hour()
        return self.params.trade_start_hour <= hour < self.params.trade_end_hour

    def is_asian_session(self):
        """Check if we're in Asian session for range tracking."""
        hour = self.get_current_hour()
        return self.params.asian_start_hour <= hour < self.params.asian_end_hour

    def calculate_position_size(self, sl_distance):
        """Calculate position size based on risk, reduced in low-ADX environments."""
        if sl_distance <= 0:
            return 0
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        size = round(risk_amount / (sl_distance * self.params.contract_size), 2)
        size = min(size, self.params.max_lots)
        
        # OPTION C: Reduce position size 50% in ranging/uncertain markets
        if self.current_regime == 'RANGING':
            size = round(size * 0.5, 2)
            self.log(f"REDUCED SIZE: ADX={self.adx.adx[0]:.1f} < 20, sizing halved to {size}")
        
        return size

    def next(self):
        # Calculate Heikin-Ashi
        self.calculate_heikin_ashi()
        
        # === DAILY RESET ===
        current_date = self.datas[0].datetime.date(0)
        current_equity = self.broker.getvalue()
        
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date
            self.daily_peak_equity = current_equity
            # Reset Asian range for new day
            self.asian_range_high = None
            self.asian_range_low = None
            self.asian_range_formed = False
            self.traded_breakout_today = False
            self.in_pullback_zone = False
            self.pullback_direction = None
        
        # === ASIAN RANGE TRACKING (01:00-08:00 GMT) ===
        # Always track the Asian range, even if we're in trending mode
        # This gives us a fallback for when regime changes
        if self.is_asian_session():
            if self.asian_range_high is None:
                self.asian_range_high = self.data.high[0]
                self.asian_range_low = self.data.low[0]
            else:
                self.asian_range_high = max(self.asian_range_high, self.data.high[0])
                self.asian_range_low = min(self.asian_range_low, self.data.low[0])
            return  # No trading during Asian session
        
        # Mark Asian range as formed when session ends
        if not self.asian_range_formed and self.asian_range_high is not None:
            self.asian_range_formed = True
            range_size = self.asian_range_high - self.asian_range_low
            self.log(f"ASIAN RANGE: High={self.asian_range_high:.2f}, Low={self.asian_range_low:.2f}, Size={range_size:.2f}")
        
        # === RISK MANAGEMENT ===
        if current_equity > self.daily_peak_equity:
            self.daily_peak_equity = current_equity
        
        drawdown_pct = (self.daily_peak_equity - current_equity) / self.daily_peak_equity
        if drawdown_pct > self.params.max_drawdown_percent:
            self.log(f"!!! DAILY DRAWDOWN {drawdown_pct*100:.2f}% - Halting for today !!!")
            if self.position:
                self.close()
            return

        if self.daily_pnl <= -self.params.max_daily_loss:
            return
        if self.daily_trades >= self.params.max_daily_trades:
            return
        
        # === TIME-BASED EXIT (SCALPING OPTIMIZATION) ===
        # Close position if held longer than max_hold_minutes without hitting TP/SL
        # TREND trades get more time (trend_hold_minutes), RANGING trades use standard time
        if self.position and self.entry_time is not None:
            from datetime import timedelta
            current_time = self.datas[0].datetime.datetime(0)
            
            # Use longer hold time for trend trades (they need time to develop)
            if self.entry_regime == 'TRENDING':
                max_hold = self.params.trend_hold_minutes
            else:
                max_hold = self.params.max_hold_minutes
            
            hold_delta = timedelta(minutes=max_hold)
            if current_time >= self.entry_time + hold_delta:
                self.log(f"TIME EXIT: Position held > {max_hold} mins ({self.entry_regime}) - closing at market")
                # CRITICAL: Cancel pending bracket orders first to prevent orphan orders
                for o in self.bracket_orders:
                    if o and o.alive():
                        self.cancel(o)
                self.bracket_orders = []
                self.close()
                self.entry_time = None
                self.entry_regime = None
                return
        
        # === TRAILING STOP LOGIC (Dec 2024) ===
        # Moves SL to breakeven after 1x ATR profit, then trails behind price
        if self.position and self.params.use_trailing_stop and self.entry_price and self.entry_atr:
            current_price = self.data.close[0]
            breakeven_dist = self.entry_atr * self.params.breakeven_atr_mult
            
            # Long position trailing stop
            if self.position.size > 0:
                profit = current_price - self.entry_price
                
                # Move to breakeven after 1x ATR profit
                if not self.is_breakeven and profit >= breakeven_dist:
                    self.is_breakeven = True
                    self.trailing_stop_price = self.entry_price + 0.10  # Tiny buffer above entry
                    self.log(f"BREAKEVEN: Moved SL to {self.trailing_stop_price:.2f} (entry was {self.entry_price:.2f})")
                
                # Trail stop behind price after breakeven
                if self.is_breakeven and self.trailing_stop_price:
                    trail_dist = self.entry_atr * self.params.trail_atr_mult
                    new_trail = current_price - trail_dist
                    if new_trail > self.trailing_stop_price:
                        self.trailing_stop_price = new_trail
                        # Check if we should exit
                        if current_price <= self.trailing_stop_price:
                            self.log(f"TRAILING STOP: Exiting LONG at {current_price:.2f} (trail={self.trailing_stop_price:.2f})")
                            for o in self.bracket_orders:
                                if o and o.alive():
                                    self.cancel(o)
                            self.bracket_orders = []
                            self.close()
                            return
            
            # Short position trailing stop
            elif self.position.size < 0:
                profit = self.entry_price - current_price
                
                # Move to breakeven after 1x ATR profit
                if not self.is_breakeven and profit >= breakeven_dist:
                    self.is_breakeven = True
                    self.trailing_stop_price = self.entry_price - 0.10  # Tiny buffer below entry
                    self.log(f"BREAKEVEN: Moved SL to {self.trailing_stop_price:.2f} (entry was {self.entry_price:.2f})")
                
                # Trail stop behind price after breakeven
                if self.is_breakeven and self.trailing_stop_price:
                    trail_dist = self.entry_atr * self.params.trail_atr_mult
                    new_trail = current_price + trail_dist
                    if new_trail < self.trailing_stop_price:
                        self.trailing_stop_price = new_trail
                        # Check if we should exit
                        if current_price >= self.trailing_stop_price:
                            self.log(f"TRAILING STOP: Exiting SHORT at {current_price:.2f} (trail={self.trailing_stop_price:.2f})")
                            for o in self.bracket_orders:
                                if o and o.alive():
                                    self.cancel(o)
                            self.bracket_orders = []
                            self.close()
                            return
        
        if self.order or self.position:
            return
        if not self.is_trading_hours():
            return
        
        # === COOLDOWN CHECK ===
        # Wait at least X minutes after last trade before entering new one
        if self.last_trade_time is not None:
            from datetime import timedelta
            current_time = self.datas[0].datetime.datetime(0)
            cooldown_delta = timedelta(minutes=self.params.cooldown_minutes)
            if current_time < self.last_trade_time + cooldown_delta:
                return  # Still in cooldown period

        # === DETECT REGIME ===
        self.current_regime = self.detect_regime()
        
        # === DEAD ZONE: No trades when regime is uncertain ===
        if self.current_regime == 'DEAD_ZONE':
            # Don't trade during regime transitions - wait for clarity
            return
        
        # === LOW VOLATILITY FILTER ===
        # Don't trade when market is "dead" - ADX too low or ATR too tight
        adx_val = self.adx.adx[0]
        atr_val = self.atr[0]
        if adx_val < self.params.adx_min_threshold:
            # Market has no direction at all - skip trading
            return
        if atr_val < self.params.atr_min_pips:
            # Range too tight for scalping - likely to get stopped out
            return
        
        price = self.data.close[0]
        
        signal = None
        entry_reason = ""
        
        # === ADX RISING CHECK (RANGING ONLY) ===
        # Only needed in ranging - in trending, momentum is already confirmed
        if self.params.require_rising_adx and self.current_regime == 'RANGING':
            if len(self.adx.adx) > 1 and adx_val < self.adx.adx[-1]:
                # ADX is falling - momentum is fading, skip entry
                return
        
        # =====================================================
        # TRENDING REGIME: Use EMA Ribbon Pullback Strategy
        # This is the "simple version" that works in trends
        # =====================================================
        if self.current_regime == 'TRENDING':
            trend = self.check_ema_stack()
            if trend:
                if self.in_pullback_zone_check(trend):
                    self.in_pullback_zone = True
                    self.pullback_direction = trend
                
                # === CHOPPY MARKET FILTERS (Dec 2024) ===
                # Filter 1: Stronger trend requirement (ADX > 35 for entry)
                adx_strong_enough = adx_val >= self.params.adx_strong_trend
                
                # Filter 2: ATR not expanding (true pullback, not volatility spike)
                atr_stable = True
                if len(self.atr) > 1 and self.atr[-1] > 0:
                    atr_stable = self.atr[0] <= self.atr[-1] * self.params.atr_expansion_limit
                
                # Filter 3: RSI alignment (momentum confirms direction)
                rsi_val = self.rsi[0]
                
                # Long entry - price returns above EMA8 after pullback
                if self.in_pullback_zone and self.pullback_direction == 'BULLISH':
                    # Multi-bar confirmation: price above EMA8 for N bars
                    bars_above = 0
                    for i in range(self.params.pullback_confirm_bars):
                        if len(self.data.close) > i and len(self.ema_fast) > i:
                            if self.data.close[-i] > self.ema_fast[-i]:
                                bars_above += 1
                    confirmed = bars_above >= self.params.pullback_confirm_bars
                    
                    # RSI filter: must show bullish momentum (RSI > 45)
                    rsi_aligned = rsi_val >= self.params.trend_rsi_long_min
                    
                    if price > self.ema_fast[0] and confirmed and adx_strong_enough and atr_stable and rsi_aligned:
                        if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                            signal = 'LONG'
                            entry_reason = f"TREND PULLBACK: Price > EMA8={self.ema_fast[0]:.2f} | ADX={adx_val:.1f} | RSI={rsi_val:.1f}"
                            self.in_pullback_zone = False
                
                # Short entry - price returns below EMA8 after pullback
                elif self.in_pullback_zone and self.pullback_direction == 'BEARISH':
                    # Multi-bar confirmation: price below EMA8 for N bars
                    bars_below = 0
                    for i in range(self.params.pullback_confirm_bars):
                        if len(self.data.close) > i and len(self.ema_fast) > i:
                            if self.data.close[-i] < self.ema_fast[-i]:
                                bars_below += 1
                    confirmed = bars_below >= self.params.pullback_confirm_bars
                    
                    # RSI filter: must show bearish momentum (RSI < 55)
                    rsi_aligned = rsi_val <= self.params.trend_rsi_short_max
                    
                    if price < self.ema_fast[0] and confirmed and adx_strong_enough and atr_stable and rsi_aligned:
                        if not self.params.use_ha_filter or self.ha_color == 'RED':
                            signal = 'SHORT'
                            entry_reason = f"TREND PULLBACK: Price < EMA8={self.ema_fast[0]:.2f} | ADX={adx_val:.1f} | RSI={rsi_val:.1f}"
                            self.in_pullback_zone = False
        
        # =====================================================
        # RANGING REGIME: Use Asian Range Breakout Strategy
        # OR Mean Reversion (BB + RSI) if enabled
        # =====================================================
        elif self.current_regime == 'RANGING':
            # Try Asian Breakout first (if conditions met)
            if self.asian_range_formed and not self.traded_breakout_today:
                buffer = self.params.breakout_buffer
                
                # Long breakout - price breaks above Asian high
                if price > (self.asian_range_high + buffer):
                    if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                        # Check macro trend alignment
                        if not self.params.trade_with_trend_only or price > self.ema_macro[0]:
                            signal = 'LONG'
                            entry_reason = f"ASIAN BREAKOUT UP: Price={price:.2f} > Range High={self.asian_range_high:.2f}"
                            self.traded_breakout_today = True
                
                # Short breakout - price breaks below Asian low
                elif price < (self.asian_range_low - buffer):
                    if not self.params.use_ha_filter or self.ha_color == 'RED':
                        # Check macro trend alignment
                        if not self.params.trade_with_trend_only or price < self.ema_macro[0]:
                            signal = 'SHORT'
                            entry_reason = f"ASIAN BREAKOUT DOWN: Price={price:.2f} < Range Low={self.asian_range_low:.2f}"
                            self.traded_breakout_today = True
            
            # OPTION B: MOMENTUM BREAKOUT (replaces mean reversion)
            # Instead of fading BB extremes, TRADE WITH THEM when momentum confirms
            # This catches breakouts like March 2024 instead of fighting them
            if signal is None and self.params.use_mean_reversion:
                lower_bb = self.bb.lines.bot[0]
                upper_bb = self.bb.lines.top[0]
                mid_bb = self.bb.lines.mid[0]
                rsi_val = self.rsi[0]
                
                # Check for consecutive closes above/below BB (confirmation)
                # Look back 2 bars for confirmation
                prev_close1 = self.data.close[-1] if len(self.data.close) > 1 else price
                prev_close2 = self.data.close[-2] if len(self.data.close) > 2 else price
                prev_upper_bb = self.bb.lines.top[-1] if len(self.bb.lines.top) > 1 else upper_bb
                prev_lower_bb = self.bb.lines.bot[-1] if len(self.bb.lines.bot) > 1 else lower_bb
                
                # Debug logging
                if not hasattr(self, '_mr_debug_date') or self._mr_debug_date != self.datas[0].datetime.date(0):
                    self._mr_debug_date = self.datas[0].datetime.date(0)
                    self.log(f"BREAKOUT DEBUG: Price={price:.2f}, UpperBB={upper_bb:.2f}, LowerBB={lower_bb:.2f}, RSI={rsi_val:.1f}")
                
                # LONG BREAKOUT: Price above upper BB for 2+ bars + RSI rising/bullish (>50)
                if price > upper_bb and prev_close1 > prev_upper_bb and rsi_val > 50:
                    signal = 'LONG'
                    entry_reason = f"MOMENTUM BREAKOUT UP: Price={price:.2f} > UpperBB={upper_bb:.2f}, RSI={rsi_val:.1f}"
                    self.is_mean_reversion_trade = True  # Use mid BB as TP (target the extension)
                
                # SHORT BREAKOUT: Price below lower BB for 2+ bars + RSI falling/bearish (<50)
                elif price < lower_bb and prev_close1 < prev_lower_bb and rsi_val < 50:
                    signal = 'SHORT'
                    entry_reason = f"MOMENTUM BREAKOUT DOWN: Price={price:.2f} < LowerBB={lower_bb:.2f}, RSI={rsi_val:.1f}"
                    self.is_mean_reversion_trade = True
        
        # === MACRO TREND FILTER (for trending regime) ===
        if signal and self.current_regime == 'TRENDING' and self.params.trade_with_trend_only:
            macro_trend_bullish = price > self.ema_macro[0]
            
            if signal == 'LONG' and not macro_trend_bullish:
                self.log(f'BLOCKED: LONG but price {price:.2f} < EMA200 {self.ema_macro[0]:.2f}')
                signal = None
            elif signal == 'SHORT' and macro_trend_bullish:
                self.log(f'BLOCKED: SHORT but price {price:.2f} > EMA200 {self.ema_macro[0]:.2f}')
                signal = None
        
        # === EXECUTE SIGNAL ===
        if signal:
            sl_distance = atr_val * self.params.atr_sl_multiplier
            size = self.calculate_position_size(sl_distance)
            
            if size <= 0:
                return
            
            # For momentum breakout trades, target ATR extension (continuation)
            # For trend pullback trades, use R:R ratio
            
            if signal == 'LONG':
                sl_price = price - sl_distance
                if self.is_mean_reversion_trade:
                    # Momentum breakout: target 1.5x ATR extension (continuation move)
                    tp_price = price + (sl_distance * 1.5)
                else:
                    tp_price = price + (sl_distance * self.params.tp_risk_reward)
                self.log(f'{entry_reason} | ADX={self.adx.adx[0]:.1f} | Regime={self.current_regime}')
                self.log(f'  LONG: Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}')
                self.bracket_orders = self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.entry_time = self.datas[0].datetime.datetime(0)  # For time-based exit
                self.entry_price = price  # For trailing stop
                self.entry_atr = atr_val  # For trailing stop distance
                self.entry_regime = self.current_regime  # For regime-aware hold time
                self.is_breakeven = False  # Reset trailing stop state
                self.trailing_stop_price = None
                self.daily_trades += 1
                self.is_mean_reversion_trade = False  # Reset flag
                
            elif signal == 'SHORT':
                sl_price = price + sl_distance
                if self.is_mean_reversion_trade:
                    # Momentum breakout: target 1.5x ATR extension (continuation move)
                    tp_price = price - (sl_distance * 1.5)
                else:
                    tp_price = price - (sl_distance * self.params.tp_risk_reward)
                self.log(f'{entry_reason} | ADX={self.adx.adx[0]:.1f} | Regime={self.current_regime}')
                self.log(f'  SHORT: Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}')
                self.bracket_orders = self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.entry_time = self.datas[0].datetime.datetime(0)  # For time-based exit
                self.entry_price = price  # For trailing stop
                self.entry_atr = atr_val  # For trailing stop distance
                self.entry_regime = self.current_regime  # For regime-aware hold time
                self.is_breakeven = False  # Reset trailing stop state
                self.trailing_stop_price = None
                self.daily_trades += 1
                self.is_mean_reversion_trade = False  # Reset flag

    # TradeLocker UI metadata
    params_metadata = {
        "adx_trend_threshold": {
            "label": "ADX Trend Threshold",
            "helper_text": "ADX above this + aligned EMAs = TRENDING, else RANGING (default: 25)",
            "value_type": "int",
        },
        "use_ha_filter": {
            "label": "Use Heikin-Ashi Filter",
            "helper_text": "Require HA color confirmation for entries",
            "value_type": "bool",
        },
        "risk_per_trade_percent": {
            "label": "Risk Per Trade (%)",
            "helper_text": "Percentage of equity to risk (default: 0.01 = 1%)",
            "value_type": "float",
        },
        "trade_with_trend_only": {
            "label": "Trade With Trend Only",
            "helper_text": "Block counter-trend trades using EMA200",
            "value_type": "bool",
        },
        "breakout_buffer": {
            "label": "Breakout Buffer (pips)",
            "helper_text": "Minimum distance above/below Asian range for valid breakout",
            "value_type": "float",
        },
    }
