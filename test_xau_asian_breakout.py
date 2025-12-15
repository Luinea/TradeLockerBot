"""
Test script for XAU/USD Asian Range Breakout Strategy.
Generates synthetic data with range and breakout patterns.
"""
import backtrader as bt
import pandas as pd
import datetime
from XauAsianBreakoutStrategy import XauAsianBreakoutStrategy


def generate_breakout_data():
    """
    Generate data simulating Asian range + London breakout patterns.
    - 01:00-08:00: Low volatility (range formation)
    - 08:00-17:00: Breakouts and trends
    """
    data_list = []
    base_price = 2300.0
    
    # Simulate 30 days of 5-minute data
    for day in range(30):
        day_start = datetime.datetime(2024, 4, 1, 0, 0) + datetime.timedelta(days=day)
        
        # Daily trend direction (alternates)
        bullish_day = day % 3 != 2  # 2 bullish, 1 bearish pattern
        
        # Generate hourly candles (simplified)
        for hour in range(24):
            current_dt = day_start + datetime.timedelta(hours=hour)
            
            if 1 <= hour < 8:
                # Asian session: tight range
                noise = 3 * ((hour % 4) - 2)
                price = base_price + noise
                volatility = 2
            elif 8 <= hour < 17:
                # London/NY: breakout
                if bullish_day:
                    price = base_price + 10 + (hour - 8) * 3
                else:
                    price = base_price - 10 - (hour - 8) * 2.5
                volatility = 8
            else:
                # Off hours
                price = base_price + (5 if bullish_day else -5)
                volatility = 3
            
            # Create OHLC
            open_p = price
            close_p = price + (2 if bullish_day else -2)
            high_p = max(open_p, close_p) + volatility
            low_p = min(open_p, close_p) - volatility
            
            data_list.append({
                'datetime': current_dt,
                'open': open_p,
                'high': high_p,
                'low': low_p,
                'close': close_p,
                'volume': 1000
            })
        
        # Adjust base price for next day
        if bullish_day:
            base_price += 15
        else:
            base_price -= 10
    
    return pd.DataFrame(data_list)


def run_test():
    cerebro = bt.Cerebro()
    
    cerebro.addstrategy(XauAsianBreakoutStrategy)
    
    df = generate_breakout_data()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.0)
    
    print('=' * 70)
    print('XAU ASIAN BREAKOUT STRATEGY TEST')
    print('=' * 70)
    print('Logic:')
    print('  1. Measure Asian Range (01:00-08:00 GMT)')
    print('  2. Trade Breakouts (08:00-17:00 GMT)')
    print('  3. EMA 50 Trend Filter')
    print('  4. Risk:Reward = 1:3')
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
        print('[OK] TRADES EXECUTED - Asian Breakout strategy is functional')
    else:
        print('[!!] NO TRADES - Check range detection or breakout logic')


if __name__ == '__main__':
    run_test()
