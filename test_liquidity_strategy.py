import backtrader as bt
import pandas as pd
import datetime
from LiquidityStrategy import LiquidityStrategy

def generate_consolidation_breakout_data(scenario='upward_fake'):
    """
    Generate synthetic price data for testing liquidity strategy.
    
    Args:
        scenario: Type of test scenario
            'upward_fake': Consolidation → breaks high → reverses down (SHORT profit)
            'downward_fake': Consolidation → breaks low → reverses up (LONG profit)
            'equal_highs': Multiple highs at same level → break → reversal
            'equal_lows': Multiple lows at same level → break → reversal
            'trending': Strong trend (should NOT trade)
    
    Returns:
        pd.DataFrame: OHLCV data
    """
    data_list = []
    base_price = 2000.0
    start_date = datetime.datetime(2024, 1, 1)
    
    if scenario == 'upward_fake':
        # Day 0-20: Consolidation at 2000-2010
        for day in range(20):
            current_dt = start_date + datetime.timedelta(days=day)
            noise = (day % 3) - 1
            price = 2005 + noise * 2
            
            data_list.append({
                'datetime': current_dt,
                'open': price,
                'high': price + 3,
                'low': price - 3,
                'close': price + 1,
                'volume': 1000
            })
        
        # Day 20-22: Fake breakout UP (triggers SHORT)
        for day in range(20, 23):
            current_dt = start_date + datetime.timedelta(days=day)
            breakout_move = (day - 19) * 5
            price = 2010 + breakout_move
            
            data_list.append({
                'datetime': current_dt,
                'open': price - 2,
                'high': price + 2,
                'low': price - 3,
                'close': price,  # Close above range
                'volume': 1500
            })
        
        # Day 23-30: Reversal DOWN to range low (SHORT profit)
        for day in range(23, 31):
            current_dt = start_date + datetime.timedelta(days=day)
            reversal_move = (day - 22) * -3
            price = 2020 + reversal_move
            
            data_list.append({
                'datetime': current_dt,
                'open': price + 2,
                'high': price + 3,
                'low': price - 2,
                'close': price,
                'volume': 1200
            })
    
    elif scenario == 'downward_fake':
        # Day 0-20: Consolidation at 2000-2010
        for day in range(20):
            current_dt = start_date + datetime.timedelta(days=day)
            noise = (day % 3) - 1
            price = 2005 + noise * 2
            
            data_list.append({
                'datetime': current_dt,
                'open': price,
                'high': price + 3,
                'low': price - 3,
                'close': price - 1,
                'volume': 1000
            })
        
        # Day 20-22: Fake breakout DOWN (triggers LONG)
        for day in range(20, 23):
            current_dt = start_date + datetime.timedelta(days=day)
            breakout_move = (day - 19) * -5
            price = 2000 + breakout_move
            
            data_list.append({
                'datetime': current_dt,
                'open': price + 2,
                'high': price + 3,
                'low': price - 2,
                'close': price,  # Close below range
                'volume': 1500
            })
        
        # Day 23-30: Reversal UP to range high (LONG profit)
        for day in range(23, 31):
            current_dt = start_date + datetime.timedelta(days=day)
            reversal_move = (day - 22) * 3
            price = 1990 + reversal_move
            
            data_list.append({
                'datetime': current_dt,
                'open': price - 2,
                'high': price + 2,
                'low': price - 3,
                'close': price,
                'volume': 1200
            })
    
    elif scenario == 'equal_highs':
        # Create multiple highs at approximately 2010 (liquidity cluster)
        for day in range(30):
            current_dt = start_date + datetime.timedelta(days=day)
            
            # Create swing highs at same level every 5 days
            if day % 5 == 0 and day > 0:
                # Swing high at 2010
                data_list.append({
                    'datetime': current_dt,
                    'open': 2005,
                    'high': 2010,  # Equal high
                    'low': 2003,
                    'close': 2006,
                    'volume': 1000
                })
            else:
                # Lower bars
                price = 2000 + (day % 4)
                data_list.append({
                    'datetime': current_dt,
                    'open': price,
                    'high': price + 2,
                    'low': price - 1,
                    'close': price + 1,
                    'volume': 1000
                })
        
        # Breakout above equal highs
        for day in range(30, 33):
            current_dt = start_date + datetime.timedelta(days=day)
            price = 2010 + (day - 29) * 3
            data_list.append({
                'datetime': current_dt,
                'open': price - 1,
                'high': price + 2,
                'low': price - 2,
                'close': price,
                'volume': 1500
            })
        
        # Reversal down
        for day in range(33, 40):
            current_dt = start_date + datetime.timedelta(days=day)
            price = 2016 - (day - 32) * 2
            data_list.append({
                'datetime': current_dt,
                'open': price + 1,
                'high': price + 2,
                'low': price - 1,
                'close': price,
                'volume': 1200
            })
    
    elif scenario == 'trending':
        # Strong uptrend - should NOT trigger trades
        for day in range(30):
            current_dt = start_date + datetime.timedelta(days=day)
            price = 2000 + day * 5  # Strong trend
            
            data_list.append({
                'datetime': current_dt,
                'open': price - 1,
                'high': price + 3,
                'low': price - 2,
                'close': price + 2,
                'volume': 1000
            })
    
    df = pd.DataFrame(data_list)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    return df

def run_liquidity_backtest(scenario='upward_fake', verbose=True):
    """
    Run backtest for specified scenario.
    
    Args:
        scenario: Test scenario name
        verbose: Print detailed logs
        
    Returns:
        dict: Backtest results
    """
    cerebro = bt.Cerebro()
    
    # Add strategy
    cerebro.addstrategy(LiquidityStrategy)
    
    # Generate and add data
    df = generate_consolidation_breakout_data(scenario)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    
    # Set broker
    initial_cash = 10000.0
    cerebro.broker.setcash(initial_cash)
    cerebro.broker.setcommission(commission=0.0)
    
    if verbose:
        print('=' * 80)
        print(f'LIQUIDITY STRATEGY BACKTEST - Scenario: {scenario.upper()}')
        print('=' * 80)
        print(f'Starting Portfolio Value: ${cerebro.broker.getvalue():.2f}')
        print(f'Data Points: {len(df)}')
        print('=' * 80)
    
    # Run backtest
    strategies = cerebro.run()
    strat = strategies[0]
    
    final_value = cerebro.broker.getvalue()
    pnl = final_value - initial_cash
    returns = (pnl / initial_cash) * 100
    
    if verbose:
        print('=' * 80)
        print(f'Final Portfolio Value: ${final_value:.2f}')
        print(f'PnL: ${pnl:.2f}')
        print(f'Return: {returns:.2f}%')
        print(f'Total Trades: {strat.daily_trades}')
        print('=' * 80)
    
    return {
        'scenario': scenario,
        'initial_value': initial_cash,
        'final_value': final_value,
        'pnl': pnl,
        'return_pct': returns,
        'trades': strat.daily_trades
    }

def run_all_tests():
    """Run all test scenarios and summarize results"""
    scenarios = [
        'upward_fake',
        'downward_fake',
        'equal_highs',
        'trending'
    ]
    
    print('\n' + '=' * 80)
    print('LIQUIDITY STRATEGY - COMPREHENSIVE BACKTEST SUITE')
    print('=' * 80)
    print()
    
    results = []
    for scenario in scenarios:
        result = run_liquidity_backtest(scenario, verbose=True)
        results.append(result)
        print()
    
    # Summary
    print('=' * 80)
    print('SUMMARY OF ALL SCENARIOS')
    print('=' * 80)
    print(f"{'Scenario':<20} {'PnL':<12} {'Return':<12} {'Trades':<10}")
    print('-' * 80)
    
    for result in results:
        print(f"{result['scenario']:<20} ${result['pnl']:>10.2f} {result['return_pct']:>10.2f}% {result['trades']:>8}")
    
    print('=' * 80)
    
    # Expected outcomes
    print()
    print('EXPECTED OUTCOMES:')
    print('- upward_fake: Should enter SHORT on upward break, profit on reversal')
    print('- downward_fake: Should enter LONG on downward break, profit on reversal')
    print('- equal_highs: Should enter SHORT when equal highs are broken')
    print('- trending: Should NOT trade (no consolidation detected)')
    print('=' * 80)

if __name__ == '__main__':
    # Run comprehensive test suite
    run_all_tests()
    
    # Optional: Run individual scenario for detailed analysis
    # run_liquidity_backtest('upward_fake', verbose=True)
