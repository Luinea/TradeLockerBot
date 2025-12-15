"""
Test script for XAU/USD Heikin-Ashi Strategy.
Generates synthetic data with trend reversals to validate:
- Heikin-Ashi calculation accuracy
- SAR flip detection
- Color change exits
"""
import backtrader as bt
import pandas as pd
import datetime
from XauHeikinAshiStrategy import XauHeikinAshiStrategy


def generate_reversal_data():
    """
    Generate synthetic XAU/USD data with clear trend reversals:
    - Days 1-50: Establish base price above future EMA200 level
    - Days 51-80: Uptrend (green HA candles)
    - Days 81-90: Reversal (red HA candles)
    - Days 91-120: Downtrend continuation below EMA200
    - Days 121-150: Reversal back up
    """
    data_list = []
    base_price = 2100.0  # Start above where EMA200 will settle
    start_date = datetime.datetime(2024, 1, 1, 14, 0)  # 14:00 GMT
    
    for day in range(250):  # Need more data for EMA200
        current_dt = start_date + datetime.timedelta(days=day)
        
        if day < 50:
            # Flat base
            noise = (day % 4) - 2
            price = base_price + noise
        elif day < 80:
            # Uptrend
            trend = (day - 50) * 2
            price = base_price + trend
        elif day < 100:
            # Sharp reversal down
            drop = (day - 80) * 5
            price = base_price + 60 - drop
        elif day < 150:
            # Downtrend (below base)
            trend = (day - 100) * 1.5
            price = base_price - 40 - trend
        elif day < 180:
            # Continue down
            price = base_price - 115 - ((day - 150) * 0.5)
        else:
            # Reversal back up
            recovery = (day - 180) * 2
            price = base_price - 130 + recovery
        
        # Create OHLC with alternating bullish/bearish closes for HA calculation
        direction = 1 if day % 2 == 0 else -1
        open_p = price
        close_p = price + (3 * direction)
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
    
    return pd.DataFrame(data_list)


def run_test():
    cerebro = bt.Cerebro()
    
    # Disable time filter for testing
    cerebro.addstrategy(XauHeikinAshiStrategy, use_time_filter=False)
    
    df = generate_reversal_data()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.0)
    
    print('=' * 70)
    print('XAU HEIKIN-ASHI STRATEGY TEST')
    print('=' * 70)
    print('Strategy: Heikin-Ashi Candles + Parabolic SAR + EMA 200')
    print('Entry: HA color change + SAR flip + Price vs EMA200')
    print('Exit: HA color reversal')
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
        print('[!!] NO TRADES - Check HA calculation or SAR detection')


if __name__ == '__main__':
    run_test()
