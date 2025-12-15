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
        # === REGIME DETECTION ===
        ("adx_period", 14),
        ("adx_trend_threshold", 25),  # ADX > 25 = trending market
        ("bb_period", 20),
        ("bb_dev", 2.0),
        
        # === TREND FOLLOWING (EMA Ribbon) ===
        ("ema_fast", 8),
        ("ema_medium", 21),
        ("ema_slow", 50),
        
        # === MEAN REVERSION (BB+RSI+Stoch) ===
        ("rsi_period", 14),
        ("rsi_oversold", 30),
        ("rsi_overbought", 70),
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
        
        # === TIME FILTER ===
        ("trade_start_hour", 13),
        ("trade_end_hour", 17),
        ("use_time_filter", True),
        
        # === RISK MANAGEMENT ===
        ("risk_per_trade_percent", 0.01),
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06),
        ("max_lots", 0.5),
        ("contract_size", 100),
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

    def detect_regime(self):
        """Detect market regime based on ADX."""
        adx_val = self.adx.adx[0]
        
        if adx_val > self.params.adx_trend_threshold:
            return 'TRENDING'
        else:
            return 'RANGING'

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

    def is_trading_hours(self):
        if not self.params.use_time_filter:
            return True
        try:
            hour = self.datas[0].datetime.datetime(0).hour
            return self.params.trade_start_hour <= hour < self.params.trade_end_hour
        except:
            return False

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

        # === DETECT REGIME ===
        self.current_regime = self.detect_regime()
        
        price = self.data.close[0]
        atr_val = self.atr[0]
        
        signal = None
        entry_reason = ""
        
        # === TRENDING REGIME: EMA Ribbon Pullback ===
        if self.current_regime == 'TRENDING':
            trend = self.check_ema_stack()
            if trend:
                if self.in_pullback_zone_check(trend):
                    self.in_pullback_zone = True
                    self.pullback_direction = trend
                
                # Long entry
                if self.in_pullback_zone and self.pullback_direction == 'BULLISH':
                    if price > self.ema_fast[0]:
                        # HA filter
                        if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                            signal = 'LONG'
                            entry_reason = f"TREND: Pullback complete, EMA8={self.ema_fast[0]:.2f}"
                            self.in_pullback_zone = False
                
                # Short entry
                elif self.in_pullback_zone and self.pullback_direction == 'BEARISH':
                    if price < self.ema_fast[0]:
                        if not self.params.use_ha_filter or self.ha_color == 'RED':
                            signal = 'SHORT'
                            entry_reason = f"TREND: Pullback complete, EMA8={self.ema_fast[0]:.2f}"
                            self.in_pullback_zone = False
        
        # === RANGING REGIME: Mean Reversion ===
        elif self.current_regime == 'RANGING':
            lower_bb, upper_bb = self.bb.lines.bot[0], self.bb.lines.top[0]
            rsi_val = self.rsi[0]
            stoch_k = self.stoch.percK[0]
            
            # Long: Price below BB + RSI oversold + Stoch oversold
            if price < lower_bb and rsi_val < self.params.rsi_oversold:
                if stoch_k < self.params.stoch_oversold:
                    if not self.params.use_ha_filter or self.ha_color == 'GREEN':
                        signal = 'LONG'
                        entry_reason = f"RANGE: BB breach, RSI={rsi_val:.1f}"
            
            # Short: Price above BB + RSI overbought + Stoch overbought
            elif price > upper_bb and rsi_val > self.params.rsi_overbought:
                if stoch_k > self.params.stoch_overbought:
                    if not self.params.use_ha_filter or self.ha_color == 'RED':
                        signal = 'SHORT'
                        entry_reason = f"RANGE: BB breach, RSI={rsi_val:.1f}"
        
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
    }
