import backtrader as bt
import pandas as pd
import datetime
from MacdStrategy import MacdStrategy

def run_macd_backtest():
    """Test the updated MACD strategy with synthetic trending data"""
    cerebro = bt.Cerebro()

    # Add MACD strategy (disable S/R filter for initial test)
    cerebro.addstrategy(MacdStrategy, use_sr_filter=False)

    # Generate synthetic data that should trigger MACD signals
    data_list = []
    base_price = 2000.0
    start_date = datetime.datetime(2024, 1, 1)
    
    # Generate 200 days of data with trending movements
    for day in range(200):
        current_dt = start_date + datetime.timedelta(days=day)
        
        # Create uptrend for first 100 days, downtrend for next 100
        if day < 100:
            # Gradual uptrend with some noise
            trend = day * 2.0  # 2 points per day
            noise = (day % 5) - 2  # -2 to +2
            price = base_price + trend + noise
        else:
            # Gradual downtrend
            trend = (day - 100) * -1.5
            noise = (day % 5) - 2
            price = base_price + 200 + trend + noise
        
        # Create OHLC bar
        open_p = price
        close_p = price + ((day % 3) - 1)  # Small daily movement
        high_p = max(open_p, close_p) + 2
        low_p = min(open_p, close_p) - 2
        
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

    # Add data to cerebro
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    # Set broker parameters
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.0)

    print('MACD Strategy Backtest')
    print('=' * 60)
    print(f'Starting Portfolio Value: ${cerebro.broker.getvalue():.2f}')
    print('Strategy Parameters:')
    print('  - MACD Fast: 12, Slow: 26, Signal: 9')
    print('  - 200 EMA for trend filter')
    print('  - Zero-line crossover filter: ENABLED')
    print('  - Support/Resistance filter: DISABLED (testing)')
    print('  - Stop Loss: Based on distance to 200 EMA')
    print('  - Risk/Reward: 1.5:1')
    print('=' * 60)
    
    # Run backtest
    cerebro.run()
    
    final_value = cerebro.broker.getvalue()
    returns = ((final_value - 10000) / 10000) * 100
    
    print('=' * 60)
    print(f'Final Portfolio Value: ${final_value:.2f}')
    print(f'Total Return: {returns:.2f}%')
    print('=' * 60)

if __name__ == '__main__':
    run_macd_backtest()
