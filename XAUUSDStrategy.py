# TradeLocker XAUUSD Simple Strategy
# Designed for FundedHero $2.5K Challenge
# ULTRA-SIMPLIFIED VERSION - Uses EMA position, not crossover

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    """
    Ultra-simple XAUUSD strategy for TradeLocker.
    Trades based on EMA position and RSI levels.
    """
    
    params = {
        # Account & Risk Parameters
        "account_size": 2500,
        "risk_percent": 1.0,
        "max_trades_per_day": 3,
        
        # Lot Size
        "lots_per_trade": 0.05,
        
        # Indicator Parameters
        "ema_period": 20,
        "rsi_period": 14,
        "rsi_buy": 40,      # Buy when RSI < 40 and price > EMA
        "rsi_sell": 60,     # Sell when RSI > 60 and price < EMA
        "atr_period": 14,
    }
    
    params_metadata = {
        "lots_per_trade": {
            "label": "Lots per Trade",
            "helper_text": "Fixed lot size per trade",
            "value_type": "float",
        },
        "ema_period": {
            "label": "EMA Period",
            "helper_text": "Trend filter EMA period",
            "value_type": "int",
        },
        "rsi_buy": {
            "label": "RSI Buy Level",
            "helper_text": "Buy when RSI drops below this",
            "value_type": "int",
        },
        "rsi_sell": {
            "label": "RSI Sell Level",
            "helper_text": "Sell when RSI rises above this",
            "value_type": "int",
        },
    }
    
    def __init__(self):
        self.order = None
        self.trade_count = 0
        self.current_date = None
        self.daily_trades = 0
        
        # Indicators
        self.ema = bt.indicators.EMA(self.datas[0], period=self.params.ema_period)
        self.rsi = bt.indicators.RSI(self.datas[0], period=self.params.rsi_period)
        self.atr = bt.indicators.ATR(self.datas[0], period=self.params.atr_period)
    
    def log(self, txt):
        dt = self.datas[0].datetime.datetime(0)
        print(f"{dt.isoformat()} | {txt}")
    
    def next(self):
        # Reset daily counter
        current_dt = self.datas[0].datetime.date(0)
        if self.current_date != current_dt:
            self.current_date = current_dt
            self.daily_trades = 0
        
        # Skip if order pending or max trades reached
        if self.order or self.daily_trades >= self.params.max_trades_per_day:
            return
        
        # Skip warmup
        if len(self.datas[0]) < self.params.ema_period + 5:
            return
        
        close = self.datas[0].close[0]
        ema = self.ema[0]
        rsi = self.rsi[0]
        atr = self.atr[0]
        
        # If in position, manage it
        if self.position:
            # Simple exit: reverse signal or 2 ATR move
            if self.position.size > 0:  # Long position
                # Exit on bearish signal
                if close < ema and rsi > self.params.rsi_sell:
                    self.order = self.close()
                    self.log(f"EXIT LONG at {close:.2f}")
            else:  # Short position
                # Exit on bullish signal
                if close > ema and rsi < self.params.rsi_buy:
                    self.order = self.close()
                    self.log(f"EXIT SHORT at {close:.2f}")
            return
        
        # Entry signals
        # LONG: Price above EMA + RSI oversold (pullback in uptrend)
        if close > ema and rsi < self.params.rsi_buy:
            self.order = self.buy(size=self.params.lots_per_trade)
            self.daily_trades += 1
            self.trade_count += 1
            self.log(f"LONG #{self.trade_count}: {close:.2f} | EMA: {ema:.2f} | RSI: {rsi:.1f}")
        
        # SHORT: Price below EMA + RSI overbought (rally in downtrend)
        elif close < ema and rsi > self.params.rsi_sell:
            self.order = self.sell(size=self.params.lots_per_trade)
            self.daily_trades += 1
            self.trade_count += 1
            self.log(f"SHORT #{self.trade_count}: {close:.2f} | EMA: {ema:.2f} | RSI: {rsi:.1f}")
    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status == order.Completed:
            if order.isbuy():
                self.log(f"BUY EXECUTED at {order.executed.price:.2f}")
            else:
                self.log(f"SELL EXECUTED at {order.executed.price:.2f}")
        
        self.order = None
    
    def notify_trade(self, trade):
        if trade.isclosed:
            self.log(f"TRADE PROFIT: ${trade.pnl:.2f}")
    
    def stop(self):
        self.log("=" * 40)
        self.log(f"Total Trades: {self.trade_count}")
        self.log(f"Final Value: ${self.broker.getvalue():.2f}")
        self.log("=" * 40)
