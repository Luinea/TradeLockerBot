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
        ("atr_sl_multiplier", 1.5),
        ("tp_risk_reward", 2.0),
        
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
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.daily_peak_equity = 0.0
        self.current_regime = None
        self.locked_regime = None  # Hysteresis: remembers last confirmed regime
        self.last_trade_time = None  # Cooldown: time of last trade close

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
        """Calculate position size based on risk."""
        if sl_distance <= 0:
            return 0
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        size = round(risk_amount / (sl_distance * self.params.contract_size), 2)
        return min(size, self.params.max_lots)

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
                
                # Long entry - price returns above EMA8 after pullback
                if self.in_pullback_zone and self.pullback_direction == 'BULLISH':
                    if price > self.ema_fast[0]:
                        if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                            signal = 'LONG'
                            entry_reason = f"TREND PULLBACK: Price > EMA8={self.ema_fast[0]:.2f}"
                            self.in_pullback_zone = False
                
                # Short entry - price returns below EMA8 after pullback
                elif self.in_pullback_zone and self.pullback_direction == 'BEARISH':
                    if price < self.ema_fast[0]:
                        if not self.params.use_ha_filter or self.ha_color == 'RED':
                            signal = 'SHORT'
                            entry_reason = f"TREND PULLBACK: Price < EMA8={self.ema_fast[0]:.2f}"
                            self.in_pullback_zone = False
        
        # =====================================================
        # RANGING REGIME: Use Asian Range Breakout Strategy
        # This is the "choppy market" solution
        # =====================================================
        elif self.current_regime == 'RANGING' and self.asian_range_formed and not self.traded_breakout_today:
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
            
            if signal == 'LONG':
                sl_price = price - sl_distance
                tp_price = price + (sl_distance * self.params.tp_risk_reward)
                self.log(f'{entry_reason} | ADX={self.adx.adx[0]:.1f} | Regime={self.current_regime}')
                self.log(f'  LONG: Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}')
                self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.daily_trades += 1
                
            elif signal == 'SHORT':
                sl_price = price + sl_distance
                tp_price = price - (sl_distance * self.params.tp_risk_reward)
                self.log(f'{entry_reason} | ADX={self.adx.adx[0]:.1f} | Regime={self.current_regime}')
                self.log(f'  SHORT: Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}')
                self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.daily_trades += 1

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
