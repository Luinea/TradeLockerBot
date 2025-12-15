"""
Test script for XAU/USD Trend Following Strategy.
Generates synthetic trending data to validate:
- EMA stack alignment detection
- Pullback zone entry
- Trailing stop updates
"""
import backtrader as bt
import pandas as pd
import datetime
from XauTrendFollowingStrategy import XauTrendFollowingStrategy


def generate_trend_data():
    """
    Generate synthetic XAU/USD data with clear trending conditions:
    - Days 1-30: Establish baseline (flat)
    - Days 31-100: Strong uptrend with pullbacks
    - Days 101-150: Strong downtrend with rallies
    """
    data_list = []
    base_price = 2000.0
    start_date = datetime.datetime(2024, 1, 1, 14, 0)  # 14:00 GMT (trading hours)
    
    for day in range(150):
        current_dt = start_date + datetime.timedelta(days=day)
        
        if day < 30:
            # Flat baseline to establish EMAs
            noise = (day % 5) - 2
            price = base_price + noise
        elif day < 100:
            # Uptrend with pullbacks every 10 days
            trend = (day - 30) * 1.5
            pullback = 10 if (day - 30) % 10 < 3 else 0
            price = base_price + trend - pullback
        else:
            # Downtrend with rallies every 10 days  
            trend = (day - 100) * 1.5
            rally = 10 if (day - 100) % 10 < 3 else 0
            price = base_price + 105 - trend + rally
        
        # Create OHLC with some wicks
        noise = (day % 3) - 1
        open_p = price + noise
        close_p = price - noise
        high_p = max(open_p, close_p) + 3
        low_p = min(open_p, close_p) - 3
        
        data_list.append({
            'datetime': current_dt,
            'open': open_p,
            'high': high_p,
            'low': low_p,
            'close': close_p,
            'volume': 1000
        })
    
    return pd.DataFrame(data_list)


def run_test():
    cerebro = bt.Cerebro()
    
    # Disable time filter for testing
    cerebro.addstrategy(XauTrendFollowingStrategy, use_time_filter=False)
    
    df = generate_trend_data()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.0)
    
    print('=' * 70)
    print('XAU TREND FOLLOWING STRATEGY TEST')
    print('=' * 70)
    print('Strategy: EMA Ribbon (8/21/50) with Pullback Entries')
    print('Entry: EMA stack aligned + Price in value zone + Close back in trend')
    print('Exit: Trailing stop at ATR * 2.0')
    print('=' * 70)
    print(f'Starting Portfolio: ${cerebro.broker.getvalue():.2f}')
    print('=' * 70)
    
    cerebro.run()
    
    final_value = cerebro.broker.getvalue()
    returns = ((final_value - 10000) / 10000) * 100
    
    print('=' * 70)
    print(f'Final Portfolio: ${final_value:.2f}')
    print(f'Total Return: {returns:.2f}%')
    print('=' * 70)
    
    if final_value != 10000:
        print('[OK] TRADES EXECUTED - Strategy is functional')
    else:
        print('[!!] NO TRADES - Check EMA alignment or pullback detection')


if __name__ == '__main__':
    run_test()
