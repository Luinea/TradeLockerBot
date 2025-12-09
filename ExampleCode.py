# Bots on TradeLocker are implemented in Python using the Backtrader framework.
# You can find more examples and the complete documentation at https://www.backtrader.com/

# This bot is an example that shows how to implement a basic Mean Reversion Strategy:
import backtrader as bt


class MeanReversionStrategy(bt.Strategy):
    params = {"sma_period": 25, "lots_per_trade": 0.02}

    # Define the indicators and initialize the strategy
    def __init__(self) -> None:
        self.order = None
        self.close_price = self.datas[0].close
        self.sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.sma_period)

    # Define the trading logic that is executed on each candle
    def next(self) -> None:
        candle_num = len(self.datas[0])
        self.log(f"User log: next() method started | candle number: {candle_num}")
        if self.position.size <= 0:
            if self.close_price[0] < self.sma[0]:
                self.order = self.buy(size=self.params.lots_per_trade)
        else:  # in the market
            if self.close_price[0] > self.sma[0]:
                self.order = self.sell(size=self.params.lots_per_trade)
        self.log(f"User log: next() method finished | candle number: {candle_num}")

    # ====================================================================================
    # params_metadata is optional -- it is used to configure the "Run Backtest/Bot" modal.
    params_metadata = {
        "sma_period": {
            "label": "SMA period",
            "helper_text": "Period for the Simple Moving Average indicator",
            "value_type": "int",
        },
        "lots_per_trade": {
            "label": "Lots per trade",
            "helper_text": "All trades will use this amount of lots",
            "value_type": "float",
        },
    }
