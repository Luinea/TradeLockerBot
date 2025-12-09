# TradeLocker XAUUSD Simple Strategy
# Designed for FundedHero $2.5K Challenge
# SIMPLIFIED VERSION - Guaranteed to generate trades

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    """
    Simplified XAUUSD strategy for TradeLocker backtesting.
    Uses EMA crossover with RSI filter for easy signal generation.
    """
    
    params = {
        # Account & Risk Parameters
        "account_size": 2500,
        "risk_percent": 1.0,          # 1% per trade = $25
        "max_daily_loss": 75,         # 3% self-imposed daily stop
        "max_trades_per_day": 3,
        
        # Lot Size Limits (for consistency rule)
        "min_lots": 0.03,
        "max_lots": 0.12,
        
        # Indicator Parameters
        "ema_fast": 9,
        "ema_slow": 21,
        "rsi_period": 14,
        "rsi_long_threshold": 45,     # Buy when RSI < 45 and EMA cross up
        "rsi_short_threshold": 55,    # Sell when RSI > 55 and EMA cross down
        "atr_period": 14,
        "sl_atr_mult": 1.5,           # Stop loss = 1.5 x ATR
        "tp_atr_mult": 2.0,           # Take profit = 2.0 x ATR (for 1.33 R:R)
        
        # Gold-specific
        "point_value": 100,           # $1 move per 1 lot = $100
    }
    
    # TradeLocker params_metadata for UI
    params_metadata = {
        "account_size": {
            "label": "Account Size ($)",
            "helper_text": "Starting account balance",
            "value_type": "float",
        },
        "risk_percent": {
            "label": "Risk per Trade (%)",
            "helper_text": "Percentage of account to risk per trade (0.5-1.0)",
            "value_type": "float",
        },
        "ema_fast": {
            "label": "Fast EMA Period",
            "helper_text": "Period for fast EMA (default: 9)",
            "value_type": "int",
        },
        "ema_slow": {
            "label": "Slow EMA Period",
            "helper_text": "Period for slow EMA (default: 21)",
            "value_type": "int",
        },
    }
    
    def __init__(self):
        """Initialize indicators"""
        self.order = None
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        
        # Daily tracking
        self.current_date = None
        self.daily_pnl = 0.0
        self.daily_trades = 0
        
        # Performance tracking
        self.total_profit = 0.0
        self.best_day_profit = 0.0
        self.wins = 0
        self.losses = 0
        
        # Price data
        self.close = self.datas[0].close
        self.high = self.datas[0].high
        self.low = self.datas[0].low
        
        # Indicators
        self.ema_fast = bt.indicators.EMA(
            self.datas[0], 
            period=self.params.ema_fast
        )
        self.ema_slow = bt.indicators.EMA(
            self.datas[0], 
            period=self.params.ema_slow
        )
        self.rsi = bt.indicators.RSI(
            self.datas[0], 
            period=self.params.rsi_period
        )
        self.atr = bt.indicators.ATR(
            self.datas[0], 
            period=self.params.atr_period
        )
        
        # EMA Crossover signal
        self.ema_cross = bt.indicators.CrossOver(self.ema_fast, self.ema_slow)
    
    def log(self, txt, dt=None):
        """Logging function"""
        dt = dt or self.datas[0].datetime.datetime(0)
        print(f"{dt.isoformat()} | {txt}")
    
    def calculate_lot_size(self, sl_distance):
        """Calculate position size based on risk"""
        risk_amount = self.params.account_size * (self.params.risk_percent / 100)
        
        if sl_distance <= 0:
            return self.params.min_lots
        
        lot_size = risk_amount / (sl_distance * self.params.point_value)
        lot_size = max(self.params.min_lots, min(self.params.max_lots, lot_size))
        
        return round(lot_size, 2)
    
    def check_daily_limits(self):
        """Check if trading is allowed"""
        if self.daily_pnl <= -self.params.max_daily_loss:
            return False
        if self.daily_trades >= self.params.max_trades_per_day:
            return False
        return True
    
    def next(self):
        """Main trading logic"""
        # Update daily tracking
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_pnl = 0.0
            self.daily_trades = 0
        
        # Skip if order pending
        if self.order:
            return
        
        # Skip if not enough bars
        if len(self.datas[0]) < max(self.params.ema_slow, self.params.atr_period) + 5:
            return
        
        # Manage existing position
        if self.position:
            # Check stop loss
            if self.position.size > 0:  # Long
                if self.low[0] <= self.stop_loss:
                    self.order = self.close()
                    self.log(f"Long SL hit at {self.stop_loss:.2f}")
                elif self.high[0] >= self.take_profit:
                    self.order = self.close()
                    self.log(f"Long TP hit at {self.take_profit:.2f}")
            elif self.position.size < 0:  # Short
                if self.high[0] >= self.stop_loss:
                    self.order = self.close()
                    self.log(f"Short SL hit at {self.stop_loss:.2f}")
                elif self.low[0] <= self.take_profit:
                    self.order = self.close()
                    self.log(f"Short TP hit at {self.take_profit:.2f}")
            return
        
        # Check daily limits
        if not self.check_daily_limits():
            return
        
        price = self.close[0]
        atr = self.atr[0]
        rsi = self.rsi[0]
        
        # Entry signals
        # LONG: EMA cross up + RSI not overbought
        if self.ema_cross[0] > 0 and rsi < self.params.rsi_long_threshold:
            sl_distance = atr * self.params.sl_atr_mult
            lot_size = self.calculate_lot_size(sl_distance)
            
            self.entry_price = price
            self.stop_loss = price - sl_distance
            self.take_profit = price + (atr * self.params.tp_atr_mult)
            
            self.order = self.buy(size=lot_size)
            self.daily_trades += 1
            
            self.log(f"LONG Entry: {price:.2f} | SL: {self.stop_loss:.2f} | "
                    f"TP: {self.take_profit:.2f} | Size: {lot_size}")
        
        # SHORT: EMA cross down + RSI not oversold
        elif self.ema_cross[0] < 0 and rsi > self.params.rsi_short_threshold:
            sl_distance = atr * self.params.sl_atr_mult
            lot_size = self.calculate_lot_size(sl_distance)
            
            self.entry_price = price
            self.stop_loss = price + sl_distance
            self.take_profit = price - (atr * self.params.tp_atr_mult)
            
            self.order = self.sell(size=lot_size)
            self.daily_trades += 1
            
            self.log(f"SHORT Entry: {price:.2f} | SL: {self.stop_loss:.2f} | "
                    f"TP: {self.take_profit:.2f} | Size: {lot_size}")
    
    def notify_order(self, order):
        """Handle order notifications"""
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status == order.Completed:
            if order.isbuy():
                self.log(f"BUY EXECUTED: {order.executed.price:.2f}")
            else:
                self.log(f"SELL EXECUTED: {order.executed.price:.2f}")
        
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f"Order Failed: {order.status}")
        
        self.order = None
    
    def notify_trade(self, trade):
        """Handle trade notifications"""
        if not trade.isclosed:
            return
        
        pnl = trade.pnl
        self.daily_pnl += pnl
        self.total_profit += pnl
        
        if pnl > 0:
            self.wins += 1
        else:
            self.losses += 1
        
        self.log(f"TRADE CLOSED: PnL=${pnl:.2f} | Total=${self.total_profit:.2f}")
        
        # Reset position tracking
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
    
    def stop(self):
        """Backtest summary"""
        self.log("=" * 50)
        self.log("BACKTEST SUMMARY")
        self.log("=" * 50)
        self.log(f"Final Value: ${self.broker.getvalue():.2f}")
        self.log(f"Total Profit: ${self.total_profit:.2f}")
        self.log(f"Return: {(self.total_profit / self.params.account_size) * 100:.2f}%")
        
        total_trades = self.wins + self.losses
        if total_trades > 0:
            win_rate = (self.wins / total_trades) * 100
            self.log(f"Win Rate: {win_rate:.1f}% ({self.wins}W / {self.losses}L)")
        else:
            self.log("No trades executed")
        
        # Phase targets
        phase1_target = self.params.account_size * 0.08
        if self.total_profit >= phase1_target:
            self.log(f"[PASSED] Phase 1 Target (${phase1_target:.2f})")
        else:
            self.log(f"[NOT MET] Phase 1 Target (need ${phase1_target:.2f})")
        
        self.log("=" * 50)
