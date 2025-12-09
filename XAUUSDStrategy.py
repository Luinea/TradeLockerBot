# XAUUSD Strategy for TradeLocker with Full Risk Management
# Designed for FundedHero $2.5K Challenge

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        # Account Settings
        "account_size": 2500,
        "risk_percent": 1.0,           # Risk 1% per trade = $25
        "max_daily_loss": 75,          # Stop trading if daily loss > $75
        "max_trades_per_day": 3,
        
        # Position Sizing
        "min_lots": 0.03,
        "max_lots": 0.12,
        "point_value": 100,            # $1 move = $100 per lot for gold
        
        # Indicators
        "sma_period": 20,
        "rsi_period": 14,
        "atr_period": 14,
        
        # Entry Thresholds
        "rsi_buy_level": 45,
        "rsi_sell_level": 55,
        
        # Exit Settings
        "sl_atr_mult": 1.5,            # Stop loss = 1.5 x ATR
        "tp_atr_mult": 2.0,            # Take profit = 2.0 x ATR
    }

    def __init__(self) -> None:
        self.order = None
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        
        # Daily tracking
        self.current_date = None
        self.daily_pnl = 0.0
        self.daily_trades = 0
        
        # Performance stats
        self.total_pnl = 0.0
        self.wins = 0
        self.losses = 0
        
        # Data references
        self.close_price = self.datas[0].close
        self.high_price = self.datas[0].high
        self.low_price = self.datas[0].low
        
        # Indicators
        self.sma = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=self.params.sma_period
        )
        self.rsi = bt.indicators.RSI(
            self.datas[0], period=self.params.rsi_period
        )
        self.atr = bt.indicators.ATR(
            self.datas[0], period=self.params.atr_period
        )

    def calculate_lot_size(self, sl_distance):
        """Calculate lot size based on risk per trade"""
        risk_amount = self.params.account_size * (self.params.risk_percent / 100)
        
        if sl_distance <= 0:
            return self.params.min_lots
        
        # Lots = Risk Amount / (SL Distance in $ × Point Value)
        lot_size = risk_amount / (sl_distance * self.params.point_value)
        lot_size = max(self.params.min_lots, min(self.params.max_lots, lot_size))
        
        return round(lot_size, 2)

    def next(self) -> None:
        # Reset daily counters on new day
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            if self.current_date is not None:
                self.log(f"Daily PnL: ${self.daily_pnl:.2f}")
            self.current_date = current_dt
            self.daily_pnl = 0.0
            self.daily_trades = 0
        
        # Skip if order pending
        if self.order:
            return
        
        # Skip warmup period
        if len(self.datas[0]) < max(self.params.sma_period, self.params.atr_period) + 5:
            return
        
        # Check daily loss limit
        if self.daily_pnl <= -self.params.max_daily_loss:
            return
        
        # Check max trades per day
        if self.daily_trades >= self.params.max_trades_per_day:
            return
        
        close = self.close_price[0]
        high = self.high_price[0]
        low = self.low_price[0]
        sma = self.sma[0]
        rsi = self.rsi[0]
        atr = self.atr[0]
        
        # Manage existing position
        if self.position:
            if self.position.size > 0:  # Long
                # Check stop loss
                if low <= self.stop_loss:
                    self.order = self.close()
                    self.log(f"LONG SL HIT at {self.stop_loss:.2f}")
                    return
                # Check take profit
                if high >= self.take_profit:
                    self.order = self.close()
                    self.log(f"LONG TP HIT at {self.take_profit:.2f}")
                    return
                    
            elif self.position.size < 0:  # Short
                # Check stop loss
                if high >= self.stop_loss:
                    self.order = self.close()
                    self.log(f"SHORT SL HIT at {self.stop_loss:.2f}")
                    return
                # Check take profit
                if low <= self.take_profit:
                    self.order = self.close()
                    self.log(f"SHORT TP HIT at {self.take_profit:.2f}")
                    return
            return
        
        # Entry signals
        sl_distance = atr * self.params.sl_atr_mult
        lot_size = self.calculate_lot_size(sl_distance)
        
        # LONG: Price below SMA (pullback) + RSI oversold
        if close < sma and rsi < self.params.rsi_buy_level:
            self.entry_price = close
            self.stop_loss = close - sl_distance
            self.take_profit = close + (atr * self.params.tp_atr_mult)
            
            self.order = self.buy(size=lot_size)
            self.daily_trades += 1
            self.log(f"LONG: {close:.2f} | SL: {self.stop_loss:.2f} | TP: {self.take_profit:.2f} | Size: {lot_size}")
        
        # SHORT: Price above SMA (rally) + RSI overbought
        elif close > sma and rsi > self.params.rsi_sell_level:
            self.entry_price = close
            self.stop_loss = close + sl_distance
            self.take_profit = close - (atr * self.params.tp_atr_mult)
            
            self.order = self.sell(size=lot_size)
            self.daily_trades += 1
            self.log(f"SHORT: {close:.2f} | SL: {self.stop_loss:.2f} | TP: {self.take_profit:.2f} | Size: {lot_size}")

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status == order.Completed:
            self.log(f"ORDER EXECUTED at {order.executed.price:.2f}")
        
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
        
        self.log(f"CLOSED: PnL=${pnl:.2f} | Total=${self.total_pnl:.2f}")
        
        # Reset SL/TP
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None

    def stop(self):
        self.log("=" * 50)
        self.log("BACKTEST SUMMARY")
        self.log("=" * 50)
        self.log(f"Final Value: ${self.broker.getvalue():.2f}")
        self.log(f"Total PnL: ${self.total_pnl:.2f}")
        self.log(f"Return: {(self.total_pnl / self.params.account_size) * 100:.2f}%")
        
        total = self.wins + self.losses
        if total > 0:
            wr = (self.wins / total) * 100
            self.log(f"Win Rate: {wr:.1f}% ({self.wins}W / {self.losses}L)")
        
        # Challenge targets
        phase1 = self.params.account_size * 0.08
        if self.total_pnl >= phase1:
            self.log(f"[PASSED] Phase 1 (${phase1:.0f})")
        else:
            self.log(f"[NOT MET] Phase 1 (need ${phase1:.0f})")
        
        self.log("=" * 50)

    params_metadata = {
        "account_size": {
            "label": "Account Size ($)",
            "helper_text": "Starting account balance",
            "value_type": "float",
        },
        "risk_percent": {
            "label": "Risk per Trade (%)",
            "helper_text": "Percentage of account to risk per trade",
            "value_type": "float",
        },
        "max_daily_loss": {
            "label": "Max Daily Loss ($)",
            "helper_text": "Stop trading if daily loss exceeds this",
            "value_type": "float",
        },
        "sl_atr_mult": {
            "label": "SL ATR Multiplier",
            "helper_text": "Stop loss = ATR x this value",
            "value_type": "float",
        },
        "tp_atr_mult": {
            "label": "TP ATR Multiplier",
            "helper_text": "Take profit = ATR x this value",
            "value_type": "float",
        },
    }
