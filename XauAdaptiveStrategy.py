import backtrader as bt
import math


class XauAdaptiveStrategy(bt.Strategy):
    """
    Adaptive Multi-Strategy XAU/USD Scalper.
    
    Automatically switches between strategies based on market regime:
    - TRENDING: Uses EMA Ribbon pullback entries (Trend Following)
    - RANGING: Uses Bollinger+RSI mean reversion entries
    - Heikin-Ashi confirmation filter enhances both modes
    
    Regime Detection:
    - ADX > threshold = TRENDING
    - ADX < threshold = RANGING
    - Bollinger Band Width for volatility confirmation
    
    Based on Strat.md combined strategies approach.
    """
    
    params = (
        # === REGIME DETECTION (with Hysteresis) ===
        ("adx_period", 14),
        ("adx_trend_threshold", 20),  # Lowered from 30 to catch trends early
        ("adx_range_threshold", 15),  # Only range if ADX very low
        # ADX 15-20 = "Dead Zone" - NO TRADES
        ("bb_period", 20),
        ("bb_dev", 2.0),
        
        # === EMA SLOPE FILTER ===
        ("ema_slope_lookback", 5),  # Bars to measure slope
        ("min_ema_slope", 0.5),  # Minimum slope for trend confirmation (price units)
        ("use_slope_filter", True),  # Enable slope filter
        
        # === CHOPPINESS INDEX ===
        ("chop_period", 14),
        ("chop_threshold", 61.8),  # Chop > 61.8 = choppy/ranging market
        ("use_chop_filter", True),  # Enable Choppiness Index filter
        
        # === BOLLINGER SQUEEZE FILTER (NEW) ===
        ("min_bb_width", 0.002),  # 0.2% - if lower, it's a SQUEEZE (danger!)
        ("use_squeeze_filter", True),  # Block mean reversion during squeeze
        ("bb_slope_threshold", 1.5),  # If SMA20 moves >$1.50 in 3 bars, bands are trending
        
        # === TREND FOLLOWING (EMA Ribbon) ===
        ("ema_fast", 8),
        ("ema_medium", 21),
        ("ema_slow", 50),
        
        # === MEAN REVERSION (BB+RSI+Stoch) ===
        ("rsi_period", 14),
        ("rsi_oversold", 35),  # Relaxed for Gold (30 often missed)
        ("rsi_overbought", 65),  # Relaxed for Gold (70 often missed)
        ("stoch_k", 5),
        ("stoch_d", 3),
        ("stoch_slow", 3),
        ("stoch_oversold", 25),
        ("stoch_overbought", 75),
        
        # === HEIKIN-ASHI FILTER ===
        ("use_ha_filter", True),  # Require HA color alignment
        
        # === ATR & RISK ===
        ("atr_period", 14),
        ("atr_sl_multiplier", 1.5),
        ("tp_risk_reward", 2.0),
        
        # === TIME-SEGMENTED SESSIONS ===
        # Session-based strategy: Mean Reversion ONLY in Asian, Trend ONLY in NY
        ("asian_start_hour", 1),   # 01:00 GMT
        ("asian_end_hour", 9),     # 09:00 GMT (Range trading only)
        ("ny_start_hour", 13),     # 13:00 GMT
        ("ny_end_hour", 17),       # 17:00 GMT (Trend trading only)
        ("use_session_filter", True),  # Enable time-based strategy switching
        
        # === RISK MANAGEMENT ===
        ("risk_per_trade_percent", 0.01),
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06),
        ("max_lots", 0.5),
        ("contract_size", 100),
        
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
        
        # === DIRECTIONAL INDICATORS (for faster trend confirmation) ===
        self.plus_di = bt.indicators.PlusDI(self.data, period=self.params.adx_period)
        self.minus_di = bt.indicators.MinusDI(self.data, period=self.params.adx_period)
        
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
        
        # === CHOPPINESS INDEX (Manual Calculation) ===
        # Chop = 100 * LOG10(SUM(ATR, n) / (Highest(n) - Lowest(n))) / LOG10(n)
        # High values (>61.8) = choppy/consolidating, Low (<38.2) = trending
        self.highest = bt.indicators.Highest(self.data.high, period=self.params.chop_period)
        self.lowest = bt.indicators.Lowest(self.data.low, period=self.params.chop_period)
        self.tr = bt.indicators.TrueRange(self.data)
        self.tr_sum = bt.indicators.SumN(self.tr, period=self.params.chop_period)
        
        # === HEIKIN-ASHI STATE ===
        self.ha_open = None
        self.ha_close = None
        self.prev_ha_open = None
        self.prev_ha_close = None
        self.ha_color = None  # 'GREEN' or 'RED'
        
        # === PULLBACK TRACKING ===
        self.in_pullback_zone = False
        self.pullback_direction = None
        
        # === STATE ===
        self.order = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.daily_peak_equity = 0.0  # Resets each trading day
        self.current_regime = None

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
        self.log("XAU Adaptive Strategy Started")
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

    def calculate_choppiness_index(self):
        """Calculate Choppiness Index: 100 * LOG10(SUM(TR, n) / (High - Low)) / LOG10(n)"""
        import math
        try:
            high_low_range = self.highest[0] - self.lowest[0]
            if high_low_range <= 0:
                return 50.0  # Neutral if no range
            tr_sum = self.tr_sum[0]
            chop = 100.0 * math.log10(tr_sum / high_low_range) / math.log10(self.params.chop_period)
            return max(0, min(100, chop))  # Clamp to 0-100
        except:
            return 50.0

    def calculate_ema_slope(self):
        """Calculate slope of EMA50 over lookback period."""
        try:
            lookback = self.params.ema_slope_lookback
            if len(self.ema_slow) > lookback:
                slope = self.ema_slow[0] - self.ema_slow[-lookback]
                return slope
            return 0
        except:
            return 0

    def calculate_bb_width(self):
        """
        Calculate Bollinger Bandwidth as percentage of price.
        Width = (UpperBand - LowerBand) / MiddleBand
        Low width (<0.15%) = SQUEEZE (breakout imminent, dangerous for mean reversion)
        """
        try:
            top = self.bb.lines.top[0]
            bot = self.bb.lines.bot[0]
            mid = self.bb.lines.mid[0]
            if mid == 0:
                return 1.0  # Avoid division by zero, assume wide
            return (top - bot) / mid
        except:
            return 1.0  # Default to wide (safe)

    def detect_regime(self):
        """
        Detect market regime with anti-whipsaw and anti-squeeze filters:
        1. BB Squeeze: Tight bands = breakout imminent, no mean reversion
        2. ADX Hysteresis: >30 = Trend, <20 = Range, 20-30 = Dead Zone
        3. EMA Slope Filter: EMA50 must be moving, not flat
        4. Choppiness Index: >61.8 = Choppy (no trend trades)
        """
        adx_val = self.adx.adx[0]
        
        # === FILTER 0: BB SQUEEZE CHECK (NEW) ===
        # If bands are too tight, breakout is imminent - DON'T FADE!
        if self.params.use_squeeze_filter:
            bb_width = self.calculate_bb_width()
            if bb_width < self.params.min_bb_width:
                self.log(f'SQUEEZE DETECTED: Width={bb_width:.4f} < {self.params.min_bb_width} - DEAD_ZONE')
                return 'DEAD_ZONE'
        
        # === FILTER 1: ADX Hysteresis ===
        if adx_val >= self.params.adx_trend_threshold:  # ADX > 30
            regime = 'TRENDING'
        elif adx_val <= self.params.adx_range_threshold:  # ADX < 20
            regime = 'RANGING'
        else:
            # Dead Zone (ADX 20-30) - NO TRADES
            return 'DEAD_ZONE'
        
        # === FILTER 2: Choppiness Index ===
        if self.params.use_chop_filter and regime == 'TRENDING':
            chop = self.calculate_choppiness_index()
            if chop > self.params.chop_threshold:  # >61.8 = choppy
                self.log(f'CHOP FILTER: Chop={chop:.1f} > {self.params.chop_threshold} - Forcing DEAD_ZONE')
                return 'DEAD_ZONE'
        
        # === FILTER 3: EMA Slope (for TRENDING only) ===
        if self.params.use_slope_filter and regime == 'TRENDING':
            slope = self.calculate_ema_slope()
            if abs(slope) < self.params.min_ema_slope:  # EMA50 is flat
                self.log(f'SLOPE FILTER: EMA50 slope={slope:.2f} < {self.params.min_ema_slope} - Forcing DEAD_ZONE')
                return 'DEAD_ZONE'
        
        return regime

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

    def get_current_session(self):
        """
        Determine current trading session for time-segmented strategy.
        Returns: 'ASIAN', 'NY', or 'OFF_HOURS'
        
        Asian Session (01:00-09:00 GMT): Mean Reversion Only
        NY Session (13:00-17:00 GMT): Trend Following Only
        """
        if not self.params.use_session_filter:
            return 'ANY'  # Allow any strategy
        try:
            hour = self.datas[0].datetime.datetime(0).hour
            
            # Asian Session: Range trading only
            if self.params.asian_start_hour <= hour < self.params.asian_end_hour:
                return 'ASIAN'
            
            # NY Session: Trend trading only
            elif self.params.ny_start_hour <= hour < self.params.ny_end_hour:
                return 'NY'
            
            return 'OFF_HOURS'
        except:
            return 'OFF_HOURS'
    
    def is_trading_hours(self):
        """Check if we're in any valid trading session."""
        session = self.get_current_session()
        return session in ['ASIAN', 'NY', 'ANY']

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
        
        # === RISK MANAGEMENT ===
        current_equity = self.broker.getvalue()
        
        # Daily reset - MUST happen before drawdown check
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date
            # Reset daily peak equity to allow recovery each day
            self.daily_peak_equity = current_equity
        
        # Track daily peak (only increase, never decrease within the day)
        if current_equity > self.daily_peak_equity:
            self.daily_peak_equity = current_equity
        
        # Check daily drawdown
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

        # === DETECT SESSION AND REGIME ===
        session = self.get_current_session()
        self.current_regime = self.detect_regime()
        
        # === SESSION-STRATEGY ENFORCEMENT ===
        # Asian Session: ONLY allow RANGING strategies
        # NY Session: ONLY allow TRENDING strategies
        if session == 'ASIAN' and self.current_regime == 'TRENDING':
            self.current_regime = 'DEAD_ZONE'  # Block trends in Asian
        elif session == 'NY' and self.current_regime == 'RANGING':
            self.current_regime = 'DEAD_ZONE'  # Block ranges in NY
        
        price = self.data.close[0]
        atr_val = self.atr[0]
        
        signal = None
        entry_reason = ""
        
        # === TRENDING REGIME: EMA Ribbon Pullback + DI Confirmation ===
        # Only active in NY Session (or ANY if session filter disabled)
        if self.current_regime == 'TRENDING':
            trend = self.check_ema_stack()
            
            # DI Confirmation: DI+ > DI- for bullish, DI- > DI+ for bearish
            di_bullish = self.plus_di[0] > self.minus_di[0]
            di_bearish = self.minus_di[0] > self.plus_di[0]
            
            if trend:
                if self.in_pullback_zone_check(trend):
                    self.in_pullback_zone = True
                    self.pullback_direction = trend
                
                # Long entry - require DI+ > DI- for confirmation
                if self.in_pullback_zone and self.pullback_direction == 'BULLISH':
                    if price > self.ema_fast[0] and di_bullish:
                        # HA filter
                        if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                            signal = 'LONG'
                            entry_reason = f"NY TREND: Pullback + DI+>DI-, EMA8={self.ema_fast[0]:.2f}"
                            self.in_pullback_zone = False
                
                # Short entry - require DI- > DI+ for confirmation
                elif self.in_pullback_zone and self.pullback_direction == 'BEARISH':
                    if price < self.ema_fast[0] and di_bearish:
                        if not self.params.use_ha_filter or self.ha_color == 'RED':
                            signal = 'SHORT'
                            entry_reason = f"NY TREND: Pullback + DI->DI+, EMA8={self.ema_fast[0]:.2f}"
                            self.in_pullback_zone = False
        
        # === RANGING REGIME: Mean Reversion with Wick Rejection ===
        # ONLY ACTIVE IN ASIAN SESSION (01:00-09:00 GMT)
        # Uses wick rejection pattern: price dips outside BB but closes back inside
        elif self.current_regime == 'RANGING':
            lower_bb = self.bb.lines.bot[0]
            upper_bb = self.bb.lines.top[0]
            mid_bb = self.bb.lines.mid[0]
            
            rsi_val = self.rsi[0]
            stoch_k = self.stoch.percK[0]
            stoch_d = self.stoch.percD[0]
            
            # === BB SLOPE CHECK ===
            # If middle band (SMA20) is trending sharply, this isn't a range
            try:
                bb_slope = abs(mid_bb - self.bb.lines.mid[-3])
            except:
                bb_slope = 0
            is_flat_bands = bb_slope < self.params.bb_slope_threshold
            
            if is_flat_bands:
                # === LONG: WICK REJECTION PATTERN ===
                # 1. Candle's LOW dipped below Lower BB (tested the level)
                # 2. Candle's CLOSE is back above Lower BB (buyers rejected the move)
                # 3. RSI < 35 + Stoch crossing UP
                if self.data.low[0] < lower_bb and self.data.close[0] > lower_bb:
                    if rsi_val < self.params.rsi_oversold and stoch_k > stoch_d:
                        if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                            signal = 'LONG'
                            entry_reason = f"ASIA RANGE: Wick Rejection (Low<BB, Close>BB), RSI={rsi_val:.1f}"
                
                # === SHORT: WICK REJECTION PATTERN ===
                # 1. Candle's HIGH poked above Upper BB
                # 2. Candle's CLOSE is back below Upper BB (sellers rejected the move)
                elif self.data.high[0] > upper_bb and self.data.close[0] < upper_bb:
                    if rsi_val > self.params.rsi_overbought and stoch_k < stoch_d:
                        if not self.params.use_ha_filter or self.ha_color == 'RED':
                            signal = 'SHORT'
                            entry_reason = f"ASIA RANGE: Wick Rejection (High>BB, Close<BB), RSI={rsi_val:.1f}"
            else:
                # Bands are trending - skip mean reversion
                pass
        
        # === MACRO TREND FILTER ===
        # Block counter-trend trades when trade_with_trend_only is enabled
        if signal and self.params.trade_with_trend_only:
            macro_trend_bullish = price > self.ema_macro[0]
            
            if signal == 'LONG' and not macro_trend_bullish:
                self.log(f'BLOCKED: LONG signal but price {price:.2f} < EMA200 {self.ema_macro[0]:.2f}')
                signal = None
            elif signal == 'SHORT' and macro_trend_bullish:
                self.log(f'BLOCKED: SHORT signal but price {price:.2f} > EMA200 {self.ema_macro[0]:.2f}')
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
                self.log(f'{entry_reason} | ADX={self.adx.adx[0]:.1f}')
                self.log(f'  LONG: Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}')
                self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.daily_trades += 1
                
            elif signal == 'SHORT':
                sl_price = price + sl_distance
                tp_price = price - (sl_distance * self.params.tp_risk_reward)
                self.log(f'{entry_reason} | ADX={self.adx.adx[0]:.1f}')
                self.log(f'  SHORT: Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}')
                self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.daily_trades += 1

    # TradeLocker UI metadata
    params_metadata = {
        "adx_trend_threshold": {
            "label": "ADX Trend Threshold",
            "helper_text": "ADX value above this = TRENDING, below = RANGING (default: 25)",
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
        "use_time_filter": {
            "label": "Use Time Filter",
            "helper_text": "Only trade during London/NY Overlap (13:00-17:00 GMT)",
            "value_type": "bool",
        },
        "trade_with_trend_only": {
            "label": "Trade With Trend Only",
            "helper_text": "Block counter-trend trades using EMA200 (LONG above, SHORT below)",
            "value_type": "bool",
        },
    }
