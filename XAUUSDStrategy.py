# XAUUSD Mean Reversion Strategy for TradeLocker
# v6.0 - Simple mean reversion with strict limits

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        # Account
        "account_size": 2500,
        "max_trades_per_day": 2,
        
        # Position Size
        "fixed_lots": 0.03,
        
        # Indicators
        "sma_period": 20,
        "rsi_period": 14,
        "rsi_oversold": 30,
        "rsi_overbought": 70,
        "atr_period": 14,
        
        # Exits
        "sl_atr_mult": 2.0,
        "tp_atr_mult": 1.5,            # Smaller TP for faster wins
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
        
        self.sma = bt.indicators.SMA(self.datas[0], period=self.params.sma_period)
        self.rsi = bt.indicators.RSI(self.datas[0], period=self.params.rsi_period)
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)

    def next(self) -> None:
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_trades = 0
        
        if self.order:
            return
        
        if len(self.datas[0]) < 30:
            return
        
        if self.daily_trades >= self.params.max_trades_per_day:
            return
        
        close = self.close_price[0]
        high = self.high_price[0]
        low = self.low_price[0]
        sma = self.sma[0]
        rsi = self.rsi[0]
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
        
        sl_dist = atr * self.params.sl_atr_mult
        tp_dist = atr * self.params.tp_atr_mult
        
        # LONG: Price below SMA + RSI oversold (mean reversion setup)
        if close < sma and rsi < self.params.rsi_oversold:
            self.stop_loss = close - sl_dist
            self.take_profit = close + tp_dist
            self.order = self.buy(size=self.params.fixed_lots)
            self.daily_trades += 1
            self.log(f"LONG {close:.2f} RSI:{rsi:.1f}")
        
        # SHORT: Price above SMA + RSI overbought
        elif close > sma and rsi > self.params.rsi_overbought:
            self.stop_loss = close + sl_dist
            self.take_profit = close - tp_dist
            self.order = self.sell(size=self.params.fixed_lots)
            self.daily_trades += 1
            self.log(f"SHORT {close:.2f} RSI:{rsi:.1f}")

    def notify_order(self, order):
        if order.status == order.Completed:
            self.log(f"EXEC {order.executed.price:.2f}")
        self.order = None

    def notify_trade(self, trade):
        if trade.isclosed:
            pnl = trade.pnl
            self.total_pnl += pnl
            if pnl > 0:
                self.wins += 1
            else:
                self.losses += 1
            self.log(f"PnL: ${pnl:.2f}")
            self.stop_loss = None
            self.take_profit = None

    def stop(self):
        total = self.wins + self.losses
        wr = (self.wins / total * 100) if total > 0 else 0
        self.log(f"=== ${self.total_pnl:.2f} | {wr:.0f}% WR ({self.wins}W/{self.losses}L) ===")

    params_metadata = {
        "rsi_oversold": {"label": "RSI Oversold", "value_type": "int"},
        "rsi_overbought": {"label": "RSI Overbought", "value_type": "int"},
        "sl_atr_mult": {"label": "SL (ATR x)", "value_type": "float"},
        "tp_atr_mult": {"label": "TP (ATR x)", "value_type": "float"},
    }
