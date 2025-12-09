# XAUUSD Trend Following Strategy for TradeLocker
# Designed for FundedHero $2.5K Challenge
# v2.0 - Improved with trend confirmation and wider stops

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        # Account Settings
        "account_size": 2500,
        "risk_percent": 0.75,          # Reduced to 0.75% per trade
        "max_daily_loss": 75,
        "max_trades_per_day": 3,
        
        # Position Sizing
        "min_lots": 0.03,
        "max_lots": 0.10,
        "point_value": 100,
        
        # Indicators
        "ema_fast": 9,
        "ema_slow": 21,
        "ema_trend": 50,              # Trend filter
        "rsi_period": 14,
        "atr_period": 14,
        
        # Entry Thresholds (more extreme for higher quality)
        "rsi_oversold": 30,           # Only buy at true oversold
        "rsi_overbought": 70,         # Only sell at true overbought
        
        # Exit Settings (wider stops for gold volatility)
        "sl_atr_mult": 2.5,           # Wider stop = 2.5 x ATR
        "tp_atr_mult": 3.5,           # Bigger target = 3.5 x ATR (1.4:1 R:R)
    }

    def __init__(self) -> None:
        self.order = None
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        
        # Tracking
        self.current_date = None
        self.daily_pnl = 0.0
        self.daily_trades = 0
        self.total_pnl = 0.0
        self.wins = 0
        self.losses = 0
        
        # Data
        self.close_price = self.datas[0].close
        self.high_price = self.datas[0].high
        self.low_price = self.datas[0].low
        
        # Trend EMAs
        self.ema_fast = bt.indicators.EMA(
            self.datas[0], period=self.params.ema_fast
        )
        self.ema_slow = bt.indicators.EMA(
            self.datas[0], period=self.params.ema_slow
        )
        self.ema_trend = bt.indicators.EMA(
            self.datas[0], period=self.params.ema_trend
        )
        
        # EMA crossover for entries
        self.ema_cross = bt.indicators.CrossOver(self.ema_fast, self.ema_slow)
        
        # RSI
        self.rsi = bt.indicators.RSI(
            self.datas[0], period=self.params.rsi_period
        )
        
        # ATR for volatility
        self.atr = bt.indicators.ATR(
            self.datas[0], period=self.params.atr_period
        )

    def calculate_lot_size(self, sl_distance):
        """Calculate lot size based on risk"""
        risk_amount = self.params.account_size * (self.params.risk_percent / 100)
        if sl_distance <= 0:
            return self.params.min_lots
        lot_size = risk_amount / (sl_distance * self.params.point_value)
        lot_size = max(self.params.min_lots, min(self.params.max_lots, lot_size))
        return round(lot_size, 2)

    def next(self) -> None:
        # Daily reset
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_pnl = 0.0
            self.daily_trades = 0
        
        if self.order:
            return
        
        # Warmup
        if len(self.datas[0]) < self.params.ema_trend + 10:
            return
        
        # Daily limits
        if self.daily_pnl <= -self.params.max_daily_loss:
            return
        if self.daily_trades >= self.params.max_trades_per_day:
            return
        
        close = self.close_price[0]
        high = self.high_price[0]
        low = self.low_price[0]
        rsi = self.rsi[0]
        atr = self.atr[0]
        ema_trend = self.ema_trend[0]
        
        # Manage positions
        if self.position:
            if self.position.size > 0:  # Long
                if low <= self.stop_loss:
                    self.order = self.close()
                    return
                if high >= self.take_profit:
                    self.order = self.close()
                    return
            elif self.position.size < 0:  # Short
                if high >= self.stop_loss:
                    self.order = self.close()
                    return
                if low <= self.take_profit:
                    self.order = self.close()
                    return
            return
        
        sl_distance = atr * self.params.sl_atr_mult
        lot_size = self.calculate_lot_size(sl_distance)
        
        # LONG: EMA cross up + price above trend EMA + RSI oversold bounce
        if self.ema_cross[0] > 0:
            if close > ema_trend and rsi < 50:  # Trend aligned + not overbought
                self.entry_price = close
                self.stop_loss = close - sl_distance
                self.take_profit = close + (atr * self.params.tp_atr_mult)
                self.order = self.buy(size=lot_size)
                self.daily_trades += 1
                self.log(f"LONG: {close:.2f} | SL: {self.stop_loss:.2f} | TP: {self.take_profit:.2f}")
        
        # SHORT: EMA cross down + price below trend EMA + RSI overbought drop
        elif self.ema_cross[0] < 0:
            if close < ema_trend and rsi > 50:  # Trend aligned + not oversold
                self.entry_price = close
                self.stop_loss = close + sl_distance
                self.take_profit = close - (atr * self.params.tp_atr_mult)
                self.order = self.sell(size=lot_size)
                self.daily_trades += 1
                self.log(f"SHORT: {close:.2f} | SL: {self.stop_loss:.2f} | TP: {self.take_profit:.2f}")

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status == order.Completed:
            self.log(f"EXECUTED at {order.executed.price:.2f}")
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        pnl = trade.pnl
        self.daily_pnl += pnl
        self.total_pnl += pnl
        if pnl > 0:
            self.wins += 1
        else:
            self.losses += 1
        self.log(f"CLOSED: ${pnl:.2f} | Total: ${self.total_pnl:.2f}")
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None

    def stop(self):
        self.log("=" * 50)
        self.log(f"Total PnL: ${self.total_pnl:.2f}")
        total = self.wins + self.losses
        if total > 0:
            self.log(f"Win Rate: {(self.wins/total)*100:.1f}% ({self.wins}W/{self.losses}L)")
        self.log("=" * 50)

    params_metadata = {
        "risk_percent": {
            "label": "Risk %",
            "helper_text": "Risk per trade as % of account",
            "value_type": "float",
        },
        "sl_atr_mult": {
            "label": "SL ATR Mult",
            "helper_text": "Stop loss = ATR x this",
            "value_type": "float",
        },
        "tp_atr_mult": {
            "label": "TP ATR Mult",
            "helper_text": "Take profit = ATR x this",
            "value_type": "float",
        },
    }
