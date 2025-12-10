import backtrader as bt
import pandas as pd
import datetime
import math
from LondonBreakoutStrategy import LondonBreakoutStrategy  # Changed import

def run_backtest():
    cerebro = bt.Cerebro()

    # Add our strategy
    cerebro.addstrategy(LondonBreakoutStrategy)

    # --- GENERATE SYNTHETIC DATA FOR LONDON BREAKOUT ---
    # We need hourly data to easily test 00:00-08:00 range
    
    data_list = []
    base_price = 2000.0
    
    start_date = datetime.datetime(2024, 1, 1)
    
    # Generate 10 days of data (Hourly candles)
    for day in range(10): 
        current_day = start_date + datetime.timedelta(days=day)
        
        # Scenario: 
        # Day 0-4:  Asian Range (2000-2005), breakout UP at 09:00 (+20), Profit.
        # Day 5-9:  Asian Range (2000-2005), breakout DOWN at 09:00 (-20), Profit.
        
        day_trend = 1 if day < 5 else -1
        
        for hour in range(24): # 24 hourly candles per day
            current_dt = current_day + datetime.timedelta(hours=hour)
            
            open_p, high_p, low_p, close_p = 0,0,0,0
            
            # ASIAN SESSION (00-08): Tight Range
            if hour < 8:
                # Flat random noise: 2000 +/- 2
                noise = (hour % 3) - 1 # -1, 0, 1
                open_p = base_price + noise
                close_p = base_price + noise + 0.5
                high_p = max(open_p, close_p) + 1
                low_p = min(open_p, close_p) - 1
            
            # LONDON OPEN (08-12): Breakout!
            elif hour >= 8 and hour < 12:
                # Big move in `day_trend` direction
                move = 10 * day_trend # +10 or -10 per hour
                open_p = base_price
                close_p = base_price + move
                high_p = max(open_p, close_p) + 2
                low_p = min(open_p, close_p) - 2
                base_price = close_p # Update base for next candle
                
            # REST OF DAY (12-23): Drift
            else:
                open_p = base_price
                close_p = base_price
                high_p = base_price + 1
                low_p = base_price - 1

            data_list.append({
                'datetime': current_dt,
                'open': open_p,
                'high': high_p,
                'low': low_p,
                'close': close_p,
                'volume': 1000
            })

    df = pd.DataFrame(data_list)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)

    # Need to verify if Backtrader can handle DataFrame directly without a file safely in this env
    # Using PandasDirectData is standard.
    
    data = bt.feeds.PandasData(dataname=df, timeframe=bt.TimeFrame.Minutes, compression=60) # Hourly
    cerebro.adddata(data)

    cerebro.broker.setcash(2500.0)
    cerebro.broker.setcommission(commission=0.0) 

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

if __name__ == '__main__':
    run_backtest()
