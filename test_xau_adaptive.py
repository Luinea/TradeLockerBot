"""
Test script for XAU/USD Adaptive Strategy.
Generates synthetic data with alternating trending and ranging conditions.
"""
import backtrader as bt
import pandas as pd
import datetime
from XauAdaptiveStrategy import XauAdaptiveStrategy


def generate_adaptive_data():
    """
    Generate data with alternating regimes:
    - Days 1-50: Flat/ranging (low ADX)
    - Days 51-100: Strong uptrend (high ADX)
    - Days 101-150: Ranging with extremes (mean reversion setups)
    - Days 151-200: Strong downtrend (high ADX)
    """
    data_list = []
    base_price = 2000.0
    start_date = datetime.datetime(2024, 1, 1, 14, 0)
    
    for day in range(200):
        current_dt = start_date + datetime.timedelta(days=day)
        
        if day < 50:
            # Ranging: small oscillations
            noise = 5 * ((day % 8) - 4)
            price = base_price + noise
        elif day < 100:
            # Uptrend with pullbacks
            trend = (day - 50) * 2
            pullback = 8 if (day - 50) % 12 < 4 else 0
            price = base_price + trend - pullback
        elif day < 150:
            # Ranging with extreme swings (mean reversion)
            cycle = (day - 100) % 20
            if cycle < 5:
                price = base_price + 100 - (cycle * 10)  # Drop
            elif cycle < 10:
                price = base_price + 50 + ((cycle - 5) * 10)  # Rally
            elif cycle < 15:
                price = base_price + 100 + ((cycle - 10) * 8)  # Spike up
            else:
                price = base_price + 140 - ((cycle - 15) * 10)  # Drop back
        else:
            # Downtrend
            trend = (day - 150) * 1.8
            rally = 6 if (day - 150) % 10 < 3 else 0
            price = base_price + 100 - trend + rally
        
        # Create OHLC
        direction = 1 if day % 2 == 0 else -1
        open_p = price
        close_p = price + (2 * direction)
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
    
    # Disable session filter and HA filter for synthetic data
    cerebro.addstrategy(XauAdaptiveStrategy, use_session_filter=False, use_ha_filter=False)
    
    df = generate_adaptive_data()
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.0)
    
    print('=' * 70)
    print('XAU ADAPTIVE STRATEGY TEST')
    print('=' * 70)
    print('Regime Detection: ADX > 25 = TRENDING, ADX < 25 = RANGING')
    print('TRENDING: EMA Ribbon Pullback entries')
    print('RANGING: Bollinger + RSI mean reversion entries')
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
        print('[OK] TRADES EXECUTED - Adaptive strategy is functional')
    else:
        print('[!!] NO TRADES - Check regime detection or signal logic')


if __name__ == '__main__':
    run_test()
