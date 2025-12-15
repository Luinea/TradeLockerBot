import backtrader as bt
import math


class XauHeikinAshiStrategy(bt.Strategy):
    """
    Heikin-Ashi Price Action Strategy for XAU/USD.
    
    Strategy Logic:
    - Heikin-Ashi candles: Smoothed price action for clear trend visualization
    - Parabolic SAR: Trend reversal confirmation (dots flip)
    - EMA 200: Macro trend filter
    
    Entry Rules:
    - LONG: Price > EMA 200 + HA color Red→Green + SAR flips below price
    - SHORT: Price < EMA 200 + HA color Green→Red + SAR flips above price
    
    Exit Rules:
    - Close immediately when HA color reverses
    
    Based on Strat.md Section 6: Heikin-Ashi Price Action
    """
    
    params = (
        # EMA Filter
        ("ema_period", 200),
        
        # Parabolic SAR
        ("sar_acceleration", 0.02),
        ("sar_max", 0.2),
        
        # ATR for sizing
        ("atr_period", 14),
        
        # Time Filter
        ("trade_start_hour", 13),
        ("trade_end_hour", 17),
        ("use_time_filter", True),
        
        # Risk Limits (FundedHero Compliance)
        ("risk_per_trade_percent", 0.01),
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06),
        ("max_lots", 0.5),
        ("contract_size", 100),
        ("sl_atr_multiplier", 1.5),
        ("tp_atr_multiplier", 2.0),
    )

    def __init__(self):
        # EMA 200 trend filter
        self.ema = bt.indicators.EMA(self.data.close, period=self.params.ema_period)
        
        # Parabolic SAR
        self.sar = bt.indicators.ParabolicSAR(
            self.data,
            period=2,  # Backtrader uses period for initial calculation
            af=self.params.sar_acceleration,
            afmax=self.params.sar_max
        )
        
        self.atr = bt.indicators.ATR(self.data, period=self.params.atr_period)
        
        # Heikin-Ashi tracking
        self.ha_close = None
        self.ha_open = None
        self.prev_ha_close = None
        self.prev_ha_open = None
        self.prev_ha_color = None  # 'GREEN' or 'RED'
        self.current_ha_color = None
        
        # State tracking
        self.order = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.peak_equity = 0.0
        self.position_direction = None
        
        # SAR flip tracking
        self.prev_sar_below = None

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
        self.log("XAU Heikin-Ashi Strategy Started")
        self.peak_equity = self.broker.getvalue()

    def calculate_heikin_ashi(self):
        """
        Calculate Heikin-Ashi candle values.
        HA_Close = (Open + High + Low + Close) / 4
        HA_Open = (Previous HA_Open + Previous HA_Close) / 2
        HA_High = Max(High, HA_Open, HA_Close)
        HA_Low = Min(Low, HA_Open, HA_Close)
        """
        open_p = self.data.open[0]
        high_p = self.data.high[0]
        low_p = self.data.low[0]
        close_p = self.data.close[0]
        
        # HA Close
        self.ha_close = (open_p + high_p + low_p + close_p) / 4.0
        
        # HA Open (first bar uses regular open)
        if self.prev_ha_open is None or self.prev_ha_close is None:
            self.ha_open = (open_p + close_p) / 2.0
        else:
            self.ha_open = (self.prev_ha_open + self.prev_ha_close) / 2.0
        
        # Determine color
        self.prev_ha_color = self.current_ha_color
        if self.ha_close > self.ha_open:
            self.current_ha_color = 'GREEN'  # Bullish
        else:
            self.current_ha_color = 'RED'  # Bearish
        
        # Store for next bar
        self.prev_ha_open = self.ha_open
        self.prev_ha_close = self.ha_close

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED @ {order.executed.price:.2f}, Size: {order.executed.size:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED @ {order.executed.price:.2f}, Size: {order.executed.size:.2f}')

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(f'TRADE PROFIT, GROSS {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')
        
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date == current_date:
            self.daily_pnl += trade.pnlcomm
        else:
            self.daily_pnl = trade.pnlcomm
            self.last_trade_date = current_date
            self.daily_trades = 0
        
        self.position_direction = None

    def is_trading_hours(self):
        if not self.params.use_time_filter:
            return True
        try:
            dt = self.datas[0].datetime.datetime(0)
            hour = dt.hour
            return self.params.trade_start_hour <= hour < self.params.trade_end_hour
        except (IndexError, AttributeError):
            return False

    def next(self):
        # Calculate Heikin-Ashi for this bar
        self.calculate_heikin_ashi()
        
        # Track SAR position relative to price
        sar_val = self.sar[0]
        price = self.data.close[0]
        current_sar_below = sar_val < price
        
        # --- RISK MANAGEMENT ---
        current_equity = self.broker.getvalue()
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity
            
        drawdown_pct = (self.peak_equity - current_equity) / self.peak_equity
        if drawdown_pct > self.params.max_drawdown_percent:
            self.log(f"!!! MAX DRAWDOWN {drawdown_pct*100:.2f}% - HALTING !!!")
            if self.position:
                self.close()
            return

        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date

        if self.daily_pnl <= -self.params.max_daily_loss:
            self.prev_sar_below = current_sar_below
            return

        if self.daily_trades >= self.params.max_daily_trades:
            self.prev_sar_below = current_sar_below
            return

        # --- EXIT LOGIC: Close on HA color reversal ---
        if self.position and self.order is None:
            if self.position_direction == 'LONG' and self.current_ha_color == 'RED':
                self.log(f'HA EXIT: Color changed to RED, closing LONG')
                self.close()
                self.prev_sar_below = current_sar_below
                return
            elif self.position_direction == 'SHORT' and self.current_ha_color == 'GREEN':
                self.log(f'HA EXIT: Color changed to GREEN, closing SHORT')
                self.close()
                self.prev_sar_below = current_sar_below
                return

        # Skip if pending order or in position
        if self.order or self.position:
            self.prev_sar_below = current_sar_below
            return

        # --- TIME FILTER ---
        if not self.is_trading_hours():
            self.prev_sar_below = current_sar_below
            return

        # Need previous values to detect transitions
        if self.prev_ha_color is None or self.prev_sar_below is None:
            self.prev_sar_below = current_sar_below
            return

        # --- ENTRY LOGIC: Heikin-Ashi + SAR ---
        
        ema_val = self.ema[0]
        atr_val = self.atr[0]
        
        # Detect color change
        color_to_green = self.prev_ha_color == 'RED' and self.current_ha_color == 'GREEN'
        color_to_red = self.prev_ha_color == 'GREEN' and self.current_ha_color == 'RED'
        
        # Detect SAR flip
        sar_flipped_below = not self.prev_sar_below and current_sar_below  # Was above, now below
        sar_flipped_above = self.prev_sar_below and not current_sar_below  # Was below, now above
        
        # Calculate position sizing
        sl_distance = atr_val * self.params.sl_atr_multiplier
        if sl_distance <= 0:
            self.prev_sar_below = current_sar_below
            return
            
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        raw_size = risk_amount / (sl_distance * self.params.contract_size)
        size = round(raw_size, 2)
        
        if size > self.params.max_lots:
            size = self.params.max_lots
        if size <= 0:
            self.prev_sar_below = current_sar_below
            return
        
        # LONG: Price > EMA 200 + HA Red→Green + SAR flips below
        long_signal = (
            price > ema_val and
            color_to_green and
            (sar_flipped_below or current_sar_below)  # SAR flipped or already below
        )
        
        # SHORT: Price < EMA 200 + HA Green→Red + SAR flips above
        short_signal = (
            price < ema_val and
            color_to_red and
            (sar_flipped_above or not current_sar_below)  # SAR flipped or already above
        )
        
        if long_signal:
            entry_price = price
            sl_price = entry_price - sl_distance
            tp_price = entry_price + (atr_val * self.params.tp_atr_multiplier)
            
            self.log(f'HEIKIN-ASHI LONG: Color Red→Green, Price {price:.2f} > EMA200 {ema_val:.2f}')
            self.log(f'  SAR: {sar_val:.2f} (below), Entry: {entry_price:.2f}, SL: {sl_price:.2f}, TP: {tp_price:.2f}')
            
            self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
            self.position_direction = 'LONG'
            self.daily_trades += 1
            
        elif short_signal:
            entry_price = price
            sl_price = entry_price + sl_distance
            tp_price = entry_price - (atr_val * self.params.tp_atr_multiplier)
            
            self.log(f'HEIKIN-ASHI SHORT: Color Green→Red, Price {price:.2f} < EMA200 {ema_val:.2f}')
            self.log(f'  SAR: {sar_val:.2f} (above), Entry: {entry_price:.2f}, SL: {sl_price:.2f}, TP: {tp_price:.2f}')
            
            self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
            self.position_direction = 'SHORT'
            self.daily_trades += 1
        
        # Update SAR tracking for next bar
        self.prev_sar_below = current_sar_below

    # TradeLocker metadata
    params_metadata = {
        "ema_period": {
            "label": "EMA Period",
            "helper_text": "EMA period for trend filter (default: 200)",
            "value_type": "int",
        },
        "sar_acceleration": {
            "label": "SAR Acceleration",
            "helper_text": "Parabolic SAR acceleration factor (default: 0.02)",
            "value_type": "float",
        },
        "sar_max": {
            "label": "SAR Max",
            "helper_text": "Parabolic SAR maximum factor (default: 0.2)",
            "value_type": "float",
        },
        "risk_per_trade_percent": {
            "label": "Risk Per Trade (%)",
            "helper_text": "Percentage of equity to risk (default: 0.01 = 1%)",
            "value_type": "float",
        },
        "use_time_filter": {
            "label": "Use Time Filter",
            "helper_text": "Only trade during London/NY Overlap",
            "value_type": "bool",
        },
    }
