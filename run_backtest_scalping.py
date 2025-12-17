"""
Backtest Runner for Scalping Strategy

Run comprehensive backtests for the 6-pattern scalping strategy on XAUUSD 1m data.

Usage:
    python run_backtest_scalping.py
    python run_backtest_scalping.py --pattern power_candle
    python run_backtest_scalping.py --data data/XAUUSD_1m.csv
"""

import backtrader as bt
import pandas as pd
import datetime
import argparse
import os
from ScalpingStrategy import ScalpingStrategy


def generate_synthetic_xauusd_data(days=5):
    """
    Generate synthetic XAUUSD 1-minute data for backtesting.
    
    Creates realistic price action with various patterns embedded.
    """
    data_list = []
    base_price = 2000.0
    start_date = datetime.datetime(2024, 1, 15, 0, 0)
    
    minute = 0
    for day in range(days):
        
        # Asian session (00:00-08:00): Low volatility ranging
        for hour in range(8):
            for m in range(60):
                current_dt = start_date + datetime.timedelta(minutes=minute)
                noise = ((minute % 17) - 8) * 0.3
                volatility = 0.5
                
                price = base_price + noise
                data_list.append({
                    'datetime': current_dt,
                    'open': price,
                    'high': price + volatility,
                    'low': price - volatility,
                    'close': price + ((minute % 3) - 1) * 0.2,
                    'volume': 800 + (minute % 200)
                })
                minute += 1
        
        # London session (08:00-14:00): Higher volatility, trends
        for hour in range(6):
            trend = 1 if day % 2 == 0 else -1
            for m in range(60):
                current_dt = start_date + datetime.timedelta(minutes=minute)
                
                # Add trend
                price = base_price + trend * (hour * 2 + m / 30)
                volatility = 1.5 + (m % 10) * 0.1
                
                # Occasionally create patterns
                if m == 30 and hour == 2:  # Pin bar
                    wick = 5 * trend
                    data_list.append({
                        'datetime': current_dt,
                        'open': price,
                        'high': price + 1 if trend > 0 else price - wick,
                        'low': price - wick if trend > 0 else price - 1,
                        'close': price + 0.5 * trend,
                        'volume': 2000
                    })
                else:
                    data_list.append({
                        'datetime': current_dt,
                        'open': price - 0.3 * trend,
                        'high': price + volatility,
                        'low': price - volatility,
                        'close': price + 0.3 * trend,
                        'volume': 1200 + (minute % 300)
                    })
                minute += 1
            
            base_price += trend * 2  # Trend movement
        
        # NY session (14:00-20:00): High volatility
        for hour in range(6):
            for m in range(60):
                current_dt = start_date + datetime.timedelta(minutes=minute)
                noise = ((minute % 23) - 11) * 0.5
                volatility = 2.0
                
                price = base_price + noise
                
                # Power candle at key times
                if m == 0 and hour == 1:
                    move = 8 * (1 if day % 3 == 0 else -1)
                    data_list.append({
                        'datetime': current_dt,
                        'open': price,
                        'high': price + move if move > 0 else price + 1,
                        'low': price - 1 if move > 0 else price + move,
                        'close': price + move * 0.9,
                        'volume': 4000
                    })
                    base_price += move * 0.5
                else:
                    data_list.append({
                        'datetime': current_dt,
                        'open': price - 0.2,
                        'high': price + volatility,
                        'low': price - volatility,
                        'close': price + 0.2,
                        'volume': 1500 + (minute % 400)
                    })
                minute += 1
        
        # Off-hours (20:00-00:00): Low activity
        for hour in range(4):
            for m in range(60):
                current_dt = start_date + datetime.timedelta(minutes=minute)
                noise = ((minute % 11) - 5) * 0.2
                
                price = base_price + noise
                data_list.append({
                    'datetime': current_dt,
                    'open': price,
                    'high': price + 0.5,
                    'low': price - 0.5,
                    'close': price + 0.1,
                    'volume': 500
                })
                minute += 1
    
    df = pd.DataFrame(data_list)
    df['datetime'] = pd.to_datetime(df['datetime'])
    df.set_index('datetime', inplace=True)
    return df


def run_backtest(data_path=None, days=5, verbose=True, **pattern_flags):
    """
    Run scalping strategy backtest.
    
    Args:
        data_path: Path to CSV data file (optional, uses synthetic if None)
        days: Number of days for synthetic data
        verbose: Enable verbose logging
        **pattern_flags: Enable/disable individual patterns
            pattern_pinbar_inside, pattern_vwap_rejection, etc.
    """
    cerebro = bt.Cerebro()
    
    # Strategy parameters
    params = {'verbose': verbose}
    params.update(pattern_flags)
    
    cerebro.addstrategy(ScalpingStrategy, **params)
    
    # Load data
    if data_path and os.path.exists(data_path):
        print(f'Loading data from: {data_path}')
        df = pd.read_csv(data_path, parse_dates=['datetime'], index_col='datetime')
    else:
        print(f'Generating {days} days of synthetic XAUUSD 1m data...')
        df = generate_synthetic_xauusd_data(days)
    
    data = bt.feeds.PandasData(dataname=df, timeframe=bt.TimeFrame.Minutes, compression=1)
    cerebro.adddata(data)
    
    # Broker settings (FundedHero challenge)
    initial_cash = 10000.0
    cerebro.broker.setcash(initial_cash)
    cerebro.broker.setcommission(commission=0.0)
    
    print('=' * 80)
    print('SCALPING STRATEGY BACKTEST - XAUUSD 1M')
    print('=' * 80)
    print(f'Initial Capital: ${initial_cash:.2f}')
    print(f'Data Points: {len(df):,} (1-minute bars)')
    print(f'Date Range: {df.index[0]} to {df.index[-1]}')
    print()
    print('Active Patterns:')
    print(f'  - Pin Bar + Inside Bar: {params.get("pattern_pinbar_inside", True)}')
    print(f'  - VWAP Rejection: {params.get("pattern_vwap_rejection", True)}')
    print(f'  - Liquidity Fakeout: {params.get("pattern_liquidity_fakeout", True)}')
    print(f'  - Momentum Fading: {params.get("pattern_momentum_fade", True)}')
    print(f'  - Power Candles: {params.get("pattern_power_candle", True)}')
    print(f'  - Tower Patterns: {params.get("pattern_tower", True)}')
    print('=' * 80)
    
    # Run
    strategies = cerebro.run()
    strat = strategies[0]
    
    # Results
    final_value = cerebro.broker.getvalue()
    pnl = final_value - initial_cash
    returns = (pnl / initial_cash) * 100
    
    print()
    print('=' * 80)
    print('BACKTEST RESULTS')
    print('=' * 80)
    print(f'Final Portfolio Value: ${final_value:,.2f}')
    print(f'Total PnL: ${pnl:,.2f}')
    print(f'Return: {returns:.2f}%')
    print(f'Total Trades: {strat.daily_trades}')
    print(f'Final Consecutive Losses: {strat.consecutive_losses}')
    print(f'Permanent Lock: {strat.permanent_lock}')
    print('=' * 80)
    
    return {
        'final_value': final_value,
        'pnl': pnl,
        'return_pct': returns,
        'trades': strat.daily_trades,
        'locked': strat.permanent_lock
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Scalping Strategy Backtest')
    parser.add_argument('--data', type=str, help='Path to OHLCV CSV data file')
    parser.add_argument('--days', type=int, default=5, help='Days of synthetic data to generate')
    parser.add_argument('--quiet', action='store_true', help='Disable verbose logging')
    
    # Pattern toggles
    parser.add_argument('--no-pinbar', action='store_true', help='Disable Pin Bar + Inside Bar')
    parser.add_argument('--no-vwap', action='store_true', help='Disable VWAP Rejection')
    parser.add_argument('--no-fakeout', action='store_true', help='Disable Liquidity Fakeout')
    parser.add_argument('--no-momentum', action='store_true', help='Disable Momentum Fading')
    parser.add_argument('--no-power', action='store_true', help='Disable Power Candles')
    parser.add_argument('--no-tower', action='store_true', help='Disable Tower Patterns')
    
    args = parser.parse_args()
    
    pattern_flags = {
        'pattern_pinbar_inside': not args.no_pinbar,
        'pattern_vwap_rejection': not args.no_vwap,
        'pattern_liquidity_fakeout': not args.no_fakeout,
        'pattern_momentum_fade': not args.no_momentum,
        'pattern_power_candle': not args.no_power,
        'pattern_tower': not args.no_tower,
    }
    
    run_backtest(
        data_path=args.data,
        days=args.days,
        verbose=not args.quiet,
        **pattern_flags
    )
