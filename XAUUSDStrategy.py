# XAUUSD EMA Crossover Strategy for TradeLocker
# v4.0 - Ultra-Conservative for FundedHero Challenge (max 12% DD)

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        # Ultra-Conservative Risk Management
        "account_size": 2500,
        "risk_percent": 0.15,          # Only 0.15% per trade ($3.75)
        "max_trades_per_day": 2,       # Reduced from 3
        "max_daily_loss": 25,          # Stop if down $25/day (1%)
        
        # Fixed Small Position Size
        "fixed_lots": 0.03,            # Fixed 0.03 lots (smallest allowed)
        "point_value": 100,
        
        # Indicators (slower for fewer signals)
        "ema_fast": 12,
        "ema_slow": 26,
        "atr_period": 14,
        
        # Wide Exits (reduce whipsaws)
        "sl_atr_mult": 3.0,            # 3x ATR stop
        "tp_atr_mult": 5.0,            # 5x ATR target (1.67:1 R:R)
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
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)

    def next(self) -> None:
        # Daily reset
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_trades = 0
            self.daily_pnl = 0.0
        
        if self.order:
            return
        
        if len(self.datas[0]) < 30:
            return
        
        # Daily loss limit
        if self.daily_pnl <= -self.params.max_daily_loss:
            return
        
        if self.daily_trades >= self.params.max_trades_per_day:
            return
        
        close = self.close_price[0]
        high = self.high_price[0]
        low = self.low_price[0]
        atr = self.atr[0]
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
        
        sl_dist = atr * self.params.sl_atr_mult
        lots = self.params.fixed_lots
        
        # LONG on bullish crossover
        if cross > 0:
            self.stop_loss = close - sl_dist
            self.take_profit = close + (atr * self.params.tp_atr_mult)
            self.order = self.buy(size=lots)
            self.daily_trades += 1
            self.log(f"LONG {close:.2f} SL:{self.stop_loss:.2f} TP:{self.take_profit:.2f}")
        
        # SHORT on bearish crossover
        elif cross < 0:
            self.stop_loss = close + sl_dist
            self.take_profit = close - (atr * self.params.tp_atr_mult)
            self.order = self.sell(size=lots)
            self.daily_trades += 1
            self.log(f"SHORT {close:.2f} SL:{self.stop_loss:.2f} TP:{self.take_profit:.2f}")

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
            self.log(f"PnL: ${pnl:.2f} Total: ${self.total_pnl:.2f}")
            self.stop_loss = None
            self.take_profit = None

    def stop(self):
        self.log(f"=== Final: ${self.total_pnl:.2f} | {self.wins}W/{self.losses}L ===")

    params_metadata = {
        "fixed_lots": {"label": "Lot Size", "helper_text": "Fixed lots per trade", "value_type": "float"},
        "max_daily_loss": {"label": "Max Daily Loss", "helper_text": "Stop trading if hit", "value_type": "float"},
        "sl_atr_mult": {"label": "SL (ATR x)", "value_type": "float"},
        "tp_atr_mult": {"label": "TP (ATR x)", "value_type": "float"},
    }
