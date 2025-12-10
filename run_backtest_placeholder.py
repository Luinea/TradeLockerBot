import backtrader as bt
import datetime
from MacdStrategy import MacdStrategy

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    
    # Add our strategy
    cerebro.addstrategy(MacdStrategy)
    
    # Create valid generic data
    data = bt.feeds.GenericCSVData(
        dataname='c:/Users/Isaac/git/FundedHero/TradeLockerBot/ExampleCode.py', # Using any file just to trigger the "no data" error or I can generate data?
        # Actually, let's just make a simple mock data generator or use Yahoo finance if internet is allowed, 
        # but better to avoid external deps if possible.
        # Let's simple create a list of data
    )
    
    # Wait, backtrader needs real data format. 
    # Let's use Yahoo Finance data for XAUUSD or similar if possible, or just generate random data.
    # Since I cannot easily access external APIs without potentially hitting limits or auth 
    # (though yahoo is usually open), I will generate a comprehensive CSV file first.
    
    print("Please use the generated CSV for testing.")
