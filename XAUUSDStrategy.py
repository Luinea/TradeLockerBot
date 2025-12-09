# XAUUSD EMA Crossover Strategy for TradeLocker
# v5.0 - Trend-Filtered for FundedHero Challenge (target <12% DD)

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        # Risk Management
        "account_size": 2500,
        "max_trades_per_day": 1,       # Only 1 trade per day
        "max_daily_loss": 20,          # $20 daily limit (0.8%)
        
        # Position Size
        "fixed_lots": 0.03,
        "point_value": 100,
        
        # Indicators
        "ema_fast": 12,
        "ema_slow": 26,
        "adx_period": 14,
        "adx_threshold": 25,           # Only trade when ADX > 25
        "atr_period": 14,
        
        # Exits
        "sl_atr_mult": 3.0,
        "tp_atr_mult": 4.5,            # 1.5:1 R:R
    }

    def __init__(self) -> None:
        self.order = None
        self.stop_loss = None
        self.take_profit = None
        self.current_date = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.total_pnl = 0.0
        self.wins = 0
        self.losses = 0
        
        self.close_price = self.datas[0].close
        self.high_price = self.datas[0].high
        self.low_price = self.datas[0].low
        
        self.ema_fast = bt.indicators.EMA(self.datas[0], period=self.params.ema_fast)
        self.ema_slow = bt.indicators.EMA(self.datas[0], period=self.params.ema_slow)
        self.ema_cross = bt.indicators.CrossOver(self.ema_fast, self.ema_slow)
        self.adx = bt.indicators.ADX(self.datas[0], period=self.params.adx_period)
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)

    def next(self) -> None:
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_trades = 0
            self.daily_pnl = 0.0
        
        if self.order:
            return
        
        if len(self.datas[0]) < 30:
            return
        
        if self.daily_pnl <= -self.params.max_daily_loss:
            return
        
        if self.daily_trades >= self.params.max_trades_per_day:
            return
        
        close = self.close_price[0]
        high = self.high_price[0]
        low = self.low_price[0]
        atr = self.atr[0]
        adx = self.adx[0]
        cross = self.ema_cross[0]
        
        # Manage position
        if self.position:
            if self.position.size > 0:
                if low <= self.stop_loss or high >= self.take_profit:
                    self.order = self.close()
            elif self.position.size < 0:
                if high >= self.stop_loss or low <= self.take_profit:
                    self.order = self.close()
            return
        
        # TREND FILTER: Only trade when ADX > threshold
        if adx < self.params.adx_threshold:
            return
        
        sl_dist = atr * self.params.sl_atr_mult
        lots = self.params.fixed_lots
        
        if cross > 0:
            self.stop_loss = close - sl_dist
            self.take_profit = close + (atr * self.params.tp_atr_mult)
            self.order = self.buy(size=lots)
            self.daily_trades += 1
            self.log(f"LONG {close:.2f} ADX:{adx:.1f}")
        
        elif cross < 0:
            self.stop_loss = close + sl_dist
            self.take_profit = close - (atr * self.params.tp_atr_mult)
            self.order = self.sell(size=lots)
            self.daily_trades += 1
            self.log(f"SHORT {close:.2f} ADX:{adx:.1f}")

    def notify_order(self, order):
        if order.status == order.Completed:
            self.log(f"EXEC {order.executed.price:.2f}")
        self.order = None

    def notify_trade(self, trade):
        if trade.isclosed:
            pnl = trade.pnl
            self.daily_pnl += pnl
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
        "adx_threshold": {"label": "ADX Threshold", "helper_text": "Min ADX for trend", "value_type": "float"},
        "max_trades_per_day": {"label": "Max Trades/Day", "value_type": "int"},
        "sl_atr_mult": {"label": "SL (ATR x)", "value_type": "float"},
    }
