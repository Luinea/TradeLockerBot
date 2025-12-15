import backtrader as bt
import math


class XauTrendFollowingStrategy(bt.Strategy):
    """
    EMA Ribbon Trend Following Strategy for XAU/USD.
    
    Strategy Logic:
    - EMA Ribbon: Fast (8), Medium (21), Slow (50) for trend visualization
    - Pullback entries: Wait for price to retrace to "value zone" (between EMA 8 and 21)
    - Trend continuation: Enter when price closes back in trend direction
    
    Entry Rules:
    - LONG: EMA 8 > EMA 21 > EMA 50 (bullish stack) + Price pulls to 8-21 zone + Closes above EMA 8
    - SHORT: EMA 8 < EMA 21 < EMA 50 (bearish stack) + Price rallies to 8-21 zone + Closes below EMA 8
    
    Exit Rules:
    - Stop Loss: Below EMA 50 (invalidates trend)
    - Trailing Stop: ATR * 2.0 dynamic trail
    
    Based on Strat.md Section 5: Momentum Trend Following (EMA Ribbons)
    """
    
    params = (
        # EMA Ribbon
        ("ema_fast", 8),
        ("ema_medium", 21),
        ("ema_slow", 50),
        
        # ATR for stops
        ("atr_period", 14),
        ("atr_trail_multiplier", 2.0),
        
        # Time Filter (London/NY Overlap in GMT)
        ("trade_start_hour", 13),
        ("trade_end_hour", 17),
        ("use_time_filter", True),
        
        # Trailing Stop
        ("use_trailing_stop", True),
        ("trailing_activation_pct", 0.3),  # Activate after 30% of TP reached
        
        # Risk Limits (FundedHero Compliance)
        ("risk_per_trade_percent", 0.01),
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06),
        ("max_lots", 0.5),
        ("contract_size", 100),
        ("tp_risk_reward", 2.0),  # 2:1 RR for trend following
    )

    def __init__(self):
        # EMA Ribbon
        self.ema_fast = bt.indicators.EMA(self.data.close, period=self.params.ema_fast)
        self.ema_medium = bt.indicators.EMA(self.data.close, period=self.params.ema_medium)
        self.ema_slow = bt.indicators.EMA(self.data.close, period=self.params.ema_slow)
        
        self.atr = bt.indicators.ATR(self.data, period=self.params.atr_period)
        
        # State tracking
        self.order = None
        self.stop_order = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.peak_equity = 0.0
        
        # Pullback tracking
        self.in_pullback_zone = False
        self.pullback_direction = None  # 'LONG' or 'SHORT'
        
        # Trailing stop tracking
        self.entry_price = None
        self.initial_sl_distance = None
        self.highest_since_entry = None
        self.lowest_since_entry = None
        self.trailing_active = False
        self.position_direction = None

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
        self.log("XAU Trend Following Strategy Started")
        self.peak_equity = self.broker.getvalue()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.exectype == order.Market:
                if order.isbuy() and self.entry_price is None:
                    self.entry_price = order.executed.price
                    self.position_direction = 'LONG'
                    self.highest_since_entry = order.executed.price
                    self.trailing_active = False
                    self.log(f'LONG Entry @ {self.entry_price:.2f}')
                elif order.issell() and self.entry_price is None:
                    self.entry_price = order.executed.price
                    self.position_direction = 'SHORT'
                    self.lowest_since_entry = order.executed.price
                    self.trailing_active = False
                    self.log(f'SHORT Entry @ {self.entry_price:.2f}')
            
            if order.exectype == order.Stop:
                self.stop_order = order

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
        
        # Reset trailing tracking
        self.entry_price = None
        self.initial_sl_distance = None
        self.highest_since_entry = None
        self.lowest_since_entry = None
        self.trailing_active = False
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

    def check_ema_stack(self):
        """Check EMA alignment for trend direction"""
        fast = self.ema_fast[0]
        medium = self.ema_medium[0]
        slow = self.ema_slow[0]
        
        bullish = fast > medium > slow
        bearish = fast < medium < slow
        
        return 'BULLISH' if bullish else ('BEARISH' if bearish else None)

    def in_value_zone(self, direction):
        """Check if price is in the pullback value zone (between EMA 8 and 21)"""
        price_low = self.data.low[0]
        price_high = self.data.high[0]
        fast = self.ema_fast[0]
        medium = self.ema_medium[0]
        
        if direction == 'BULLISH':
            # Price low touches or dips into zone between EMA 8 and 21
            return price_low <= fast and price_low >= medium
        elif direction == 'BEARISH':
            # Price high touches or rallies into zone between EMA 8 and 21
            return price_high >= fast and price_high <= medium
        
        return False

    def next(self):
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
            return

        if self.daily_trades >= self.params.max_daily_trades:
            return

        # --- TRAILING STOP LOGIC ---
        if self.params.use_trailing_stop and self.position and self.entry_price and self.initial_sl_distance:
            current_price = self.data.close[0]
            
            if self.position_direction == 'LONG':
                if current_price > self.highest_since_entry:
                    self.highest_since_entry = current_price
                
                profit = current_price - self.entry_price
                activation = self.initial_sl_distance * self.params.trailing_activation_pct
                
                if not self.trailing_active and profit >= activation:
                    self.trailing_active = True
                    self.log(f'Trailing ACTIVATED @ profit={profit:.2f}')
                
                if self.trailing_active and self.stop_order:
                    trail_dist = self.atr[0] * self.params.atr_trail_multiplier
                    new_sl = self.highest_since_entry - trail_dist
                    current_sl = self.stop_order.created.price if hasattr(self.stop_order, 'created') else 0
                    
                    if new_sl > current_sl:
                        self.broker.cancel(self.stop_order)
                        self.stop_order = self.sell(exectype=bt.Order.Stop, price=new_sl, size=abs(self.position.size))
                        self.log(f'Trail SL: {current_sl:.2f} -> {new_sl:.2f}')
            
            elif self.position_direction == 'SHORT':
                if current_price < self.lowest_since_entry:
                    self.lowest_since_entry = current_price
                
                profit = self.entry_price - current_price
                activation = self.initial_sl_distance * self.params.trailing_activation_pct
                
                if not self.trailing_active and profit >= activation:
                    self.trailing_active = True
                    self.log(f'Trailing ACTIVATED @ profit={profit:.2f}')
                
                if self.trailing_active and self.stop_order:
                    trail_dist = self.atr[0] * self.params.atr_trail_multiplier
                    new_sl = self.lowest_since_entry + trail_dist
                    current_sl = self.stop_order.created.price if hasattr(self.stop_order, 'created') else 99999
                    
                    if new_sl < current_sl:
                        self.broker.cancel(self.stop_order)
                        self.stop_order = self.buy(exectype=bt.Order.Stop, price=new_sl, size=abs(self.position.size))
                        self.log(f'Trail SL: {current_sl:.2f} -> {new_sl:.2f}')

        # Skip if pending order or in position
        if self.order or self.position:
            return

        # --- TIME FILTER ---
        if not self.is_trading_hours():
            return

        # --- ENTRY LOGIC: EMA Ribbon Pullback ---
        
        trend = self.check_ema_stack()
        if trend is None:
            self.in_pullback_zone = False
            return
        
        price = self.data.close[0]
        atr_val = self.atr[0]
        
        # Check for pullback entry
        if self.in_value_zone(trend):
            self.in_pullback_zone = True
            self.pullback_direction = trend
        
        # Calculate position sizing
        sl_distance = atr_val * self.params.atr_trail_multiplier
        if sl_distance <= 0:
            return
            
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        raw_size = risk_amount / (sl_distance * self.params.contract_size)
        size = round(raw_size, 2)
        
        if size > self.params.max_lots:
            size = self.params.max_lots
        if size <= 0:
            return
        
        # LONG Entry: Was in pullback zone + Now closes above EMA fast
        if self.in_pullback_zone and self.pullback_direction == 'BULLISH':
            if price > self.ema_fast[0]:
                entry_price = price
                sl_price = self.ema_slow[0]  # SL below EMA 50
                tp_price = entry_price + (sl_distance * self.params.tp_risk_reward)
                
                self.log(f'TREND LONG: Pullback complete, price {price:.2f} > EMA8 {self.ema_fast[0]:.2f}')
                self.log(f'  Stack: EMA8={self.ema_fast[0]:.2f} > EMA21={self.ema_medium[0]:.2f} > EMA50={self.ema_slow[0]:.2f}')
                
                self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.initial_sl_distance = entry_price - sl_price
                self.daily_trades += 1
                self.in_pullback_zone = False
        
        # SHORT Entry: Was in pullback zone + Now closes below EMA fast
        elif self.in_pullback_zone and self.pullback_direction == 'BEARISH':
            if price < self.ema_fast[0]:
                entry_price = price
                sl_price = self.ema_slow[0]  # SL above EMA 50
                tp_price = entry_price - (sl_distance * self.params.tp_risk_reward)
                
                self.log(f'TREND SHORT: Pullback complete, price {price:.2f} < EMA8 {self.ema_fast[0]:.2f}')
                self.log(f'  Stack: EMA8={self.ema_fast[0]:.2f} < EMA21={self.ema_medium[0]:.2f} < EMA50={self.ema_slow[0]:.2f}')
                
                self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                self.initial_sl_distance = sl_price - entry_price
                self.daily_trades += 1
                self.in_pullback_zone = False

    # TradeLocker metadata
    params_metadata = {
        "ema_fast": {
            "label": "EMA Fast Period",
            "helper_text": "Fast EMA for immediate momentum (default: 8)",
            "value_type": "int",
        },
        "ema_medium": {
            "label": "EMA Medium Period",
            "helper_text": "Medium EMA for pullback zone (default: 21)",
            "value_type": "int",
        },
        "ema_slow": {
            "label": "EMA Slow Period",
            "helper_text": "Slow EMA for trend baseline (default: 50)",
            "value_type": "int",
        },
        "use_trailing_stop": {
            "label": "Use Trailing Stop",
            "helper_text": "Enable ATR-based trailing stops",
            "value_type": "bool",
        },
        "risk_per_trade_percent": {
            "label": "Risk Per Trade (%)",
            "helper_text": "Percentage of equity to risk (default: 0.01 = 1%)",
            "value_type": "float",
        },
    }
