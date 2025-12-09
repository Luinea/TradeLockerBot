# XAUUSD Strategy for TradeLocker
# Based on TradeLocker's example structure

import backtrader as bt


class XAUUSDStrategy(bt.Strategy):
    params = {
        "sma_period": 20,
        "rsi_period": 14,
        "lots_per_trade": 0.05,
        "rsi_buy_level": 45,
        "rsi_sell_level": 55,
    }

    def __init__(self) -> None:
        self.order = None
        self.close_price = self.datas[0].close
        self.sma = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=self.params.sma_period
        )
        self.rsi = bt.indicators.RSI(
            self.datas[0], period=self.params.rsi_period
        )

    def next(self) -> None:
        candle_num = len(self.datas[0])
        self.log(f"Candle {candle_num} | Close: {self.close_price[0]:.2f} | SMA: {self.sma[0]:.2f} | RSI: {self.rsi[0]:.1f}")
        
        # Skip if order pending
        if self.order:
            return
        
        # Entry/Exit Logic
        if self.position.size <= 0:
            # Not in position - look for entry
            # BUY: Price below SMA (mean reversion) + RSI not overbought
            if self.close_price[0] < self.sma[0] and self.rsi[0] < self.params.rsi_buy_level:
                self.order = self.buy(size=self.params.lots_per_trade)
                self.log(f"BUY SIGNAL: Price {self.close_price[0]:.2f} < SMA {self.sma[0]:.2f}")
        else:
            # In position - look for exit
            # SELL: Price above SMA (take profit) + RSI overbought
            if self.close_price[0] > self.sma[0] and self.rsi[0] > self.params.rsi_sell_level:
                self.order = self.sell(size=self.params.lots_per_trade)
                self.log(f"SELL SIGNAL: Price {self.close_price[0]:.2f} > SMA {self.sma[0]:.2f}")

    params_metadata = {
        "sma_period": {
            "label": "SMA Period",
            "helper_text": "Period for Simple Moving Average",
            "value_type": "int",
        },
        "rsi_period": {
            "label": "RSI Period",
            "helper_text": "Period for RSI indicator",
            "value_type": "int",
        },
        "lots_per_trade": {
            "label": "Lots per Trade",
            "helper_text": "Position size for each trade",
            "value_type": "float",
        },
        "rsi_buy_level": {
            "label": "RSI Buy Level",
            "helper_text": "Buy when RSI below this level",
            "value_type": "int",
        },
        "rsi_sell_level": {
            "label": "RSI Sell Level",
            "helper_text": "Sell when RSI above this level",
            "value_type": "int",
        },
    }
