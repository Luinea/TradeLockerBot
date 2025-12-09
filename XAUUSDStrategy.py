# XAUUSD Scalping Strategy for TradeLocker
# v8.0 - Ultra-selective with ADX trend filter

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        # Position Size
        "fixed_lots": 0.03,
        
        # Indicators
        "ema_fast": 8,
        "ema_slow": 21,
        "rsi_period": 7,
        "adx_period": 14,
        "adx_threshold": 20,           # Only trade when ADX > 20
        "atr_period": 14,
        
        # Quick Exits
        "sl_atr_mult": 1.0,
        "tp_atr_mult": 0.8,
        
        # Ultra-selective
        "max_trades_per_day": 1,       # Down from 2
    }

    def __init__(self) -> None:
        self.order = None
        self.stop_loss = None
        self.take_profit = None
        self.current_date = None
        self.daily_trades = 0
        self.total_pnl = 0.0
        self.wins = 0
        self.losses = 0
        
        self.close_price = self.datas[0].close
        self.high_price = self.datas[0].high
        self.low_price = self.datas[0].low
        
        self.ema_fast = bt.indicators.EMA(self.datas[0], period=self.params.ema_fast)
        self.ema_slow = bt.indicators.EMA(self.datas[0], period=self.params.ema_slow)
        self.rsi = bt.indicators.RSI(self.datas[0], period=self.params.rsi_period)
        self.adx = bt.indicators.ADX(self.datas[0], period=self.params.adx_period)
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)

    def next(self) -> None:
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_trades = 0
        
        if self.order:
            return
        
        if len(self.datas[0]) < 25:
            return
        
        if self.daily_trades >= self.params.max_trades_per_day:
            return
        
        close = self.close_price[0]
        high = self.high_price[0]
        low = self.low_price[0]
        ema_fast = self.ema_fast[0]
        ema_slow = self.ema_slow[0]
        rsi = self.rsi[0]
        adx = self.adx[0]
        atr = self.atr[0]
        
        # Manage position
        if self.position:
            if self.position.size > 0:
                if low <= self.stop_loss or high >= self.take_profit:
                    self.order = self.close()
            elif self.position.size < 0:
                if high >= self.stop_loss or low <= self.take_profit:
                    self.order = self.close()
            return
        
        # ADX filter - only trade in trending markets
        if adx < self.params.adx_threshold:
            return
        
        sl_dist = atr * self.params.sl_atr_mult
        tp_dist = atr * self.params.tp_atr_mult
        
        # LONG: EMA aligned bullish + RSI not overbought
        if ema_fast > ema_slow and rsi < 45:
            self.stop_loss = close - sl_dist
            self.take_profit = close + tp_dist
            self.order = self.buy(size=self.params.fixed_lots)
            self.daily_trades += 1
        
        # SHORT: EMA aligned bearish + RSI not oversold
        elif ema_fast < ema_slow and rsi > 55:
            self.stop_loss = close + sl_dist
            self.take_profit = close - tp_dist
            self.order = self.sell(size=self.params.fixed_lots)
            self.daily_trades += 1

    def notify_order(self, order):
        self.order = None

    def notify_trade(self, trade):
        if trade.isclosed:
            self.total_pnl += trade.pnl
            if trade.pnl > 0:
                self.wins += 1
            else:
                self.losses += 1
            self.stop_loss = None
            self.take_profit = None

    def stop(self):
        total = self.wins + self.losses
        wr = (self.wins / total * 100) if total > 0 else 0
        self.log(f"=== ${self.total_pnl:.2f} | {wr:.0f}% WR ({self.wins}W/{self.losses}L) ===")

    params_metadata = {
        "adx_threshold": {"label": "ADX Threshold", "value_type": "float"},
        "max_trades_per_day": {"label": "Max Trades/Day", "value_type": "int"},
    }
