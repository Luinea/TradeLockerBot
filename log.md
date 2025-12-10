========== Starting to setup a Backtest:
Using configuration: symbolName='XAUUSD.PRO' symbolId=781 resolution='15m' commission=0.0 startDate=datetime.datetime(2025, 2, 1, 0, 0, tzinfo=TzInfo(UTC)) endDate=datetime.datetime(2025, 3, 1, 0, 0, tzinfo=TzInfo(UTC)) leverage=100.0 margin=2500.0 strategyParamsInput={'macd_fast': 12, 'macd_slow': 26, 'macd_signal': 9, 'ema_period': 200, 'risk_per_trade_percent': 0.01, 'max_daily_trades': 3, 'max_daily_loss': 75, 'max_drawdown_percent': 0.06, 'max_lots': 0.5, 'contract_size': 100, 'min_sl_distance': 20, 'ema_sl_multiplier': 1.5, 'tp_risk_reward': 1.5, 'sr_lookback': 20, 'sr_threshold': 5, 'use_sr_filter': False}
---- [INFO 2025-12-10 14:16:08 +0800 strategy_utils.add_sizer_to_cerebro:297]: Using default sizer 'TLLotSizer'
========== Setup finished. Backtest is running...
---, Strategy Started with Risk Hardening
2025-02-05, BUY CREATE 0.01 lots, Entry: 2866.55, SL: 2831.16 (dist: 35.39), TP: 2919.63
---- [WARNING 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2831.1614327303078 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2831.1614327303078 to 2831.16.
---- [WARNING 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2919.6328509045393 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2919.6328509045393 to 2919.63.
2025-02-06 07:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2866.55, ref_id: 1
2025-02-06 07:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2831.16, ref_id: 2
2025-02-06 07:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2919.63, ref_id: 3
2025-02-06 07:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2866.55, ref_id: 1
2025-02-06 07:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2831.16, ref_id: 2
2025-02-06 07:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2919.63, ref_id: 3
2025-02-05, BUY EXECUTED, Price: 2866.53, Cost: 2866.53, Comm: 0.00
2025-02-06 07:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2866.53, ref_id: 1
2025-02-10, SELL EXECUTED, Price: 2919.63, Cost: 2866.53, Comm: 0.00
2025-02-11 07:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2919.63, ref_id: 3
2025-02-10, Order Failed: Canceled
2025-02-11 07:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2831.16, ref_id: 2
2025-02-10, TRADE PROFIT, GROSS 53.10, NET 53.10
2025-02-10, Daily PnL: $53.10
2025-02-11, BUY CREATE 0.01 lots, Entry: 2898.44, SL: 2878.44 (dist: 20.00), TP: 2928.44
2025-02-11 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2898.44, ref_id: 4
2025-02-11 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2878.44, ref_id: 5
2025-02-11 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2928.44, ref_id: 6
2025-02-11 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2898.44, ref_id: 4
2025-02-11 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2878.44, ref_id: 5
2025-02-11 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2928.44, ref_id: 6
2025-02-11, BUY EXECUTED, Price: 2898.36, Cost: 2898.36, Comm: 0.00
2025-02-11 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2898.36, ref_id: 4
2025-02-12, SELL EXECUTED, Price: 2878.44, Cost: 2898.36, Comm: 0.00
2025-02-12 21:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2878.44, ref_id: 5
2025-02-12, Order Failed: Canceled
2025-02-12 21:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2928.44, ref_id: 6
2025-02-12, TRADE PROFIT, GROSS -19.92, NET -19.92
2025-02-12, Daily PnL: $-19.92
2025-02-12, BUY CREATE 0.01 lots, Entry: 2893.80, SL: 2873.80 (dist: 20.00), TP: 2923.80
2025-02-12 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2893.8, ref_id: 7
2025-02-12 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2873.8, ref_id: 8
2025-02-12 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2923.8, ref_id: 9
2025-02-12 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2893.8, ref_id: 7
2025-02-12 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2873.8, ref_id: 8
2025-02-12 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2923.8, ref_id: 9
2025-02-12, BUY EXECUTED, Price: 2893.85, Cost: 2893.85, Comm: 0.00
2025-02-12 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2893.85, ref_id: 7
2025-02-13, SELL EXECUTED, Price: 2923.80, Cost: 2893.85, Comm: 0.00
2025-02-14 03:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2923.8, ref_id: 9
2025-02-13, Order Failed: Canceled
2025-02-14 03:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2873.8, ref_id: 8
2025-02-13, TRADE PROFIT, GROSS 29.95, NET 29.95
2025-02-13, Daily PnL: $29.95
2025-02-17, SELL CREATE 0.01 lots, Entry: 2895.95, SL: 2915.95 (dist: 20.00), TP: 2865.95
2025-02-17 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2895.95, ref_id: 10
2025-02-17 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2915.95, ref_id: 11
2025-02-17 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2865.95, ref_id: 12
2025-02-17 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2895.95, ref_id: 10
2025-02-17 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2915.95, ref_id: 11
2025-02-17 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2865.95, ref_id: 12
2025-02-17, SELL EXECUTED, Price: 2895.89, Cost: 2895.89, Comm: 0.00
2025-02-17 14:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2895.89, ref_id: 10
2025-02-18, BUY EXECUTED, Price: 2915.95, Cost: 2895.89, Comm: 0.00
2025-02-18 20:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.01, executed_price: 2915.95, ref_id: 11
2025-02-18, Order Failed: Canceled
2025-02-18 20:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2865.95, ref_id: 12
2025-02-18, TRADE PROFIT, GROSS -20.06, NET -20.06
2025-02-18, Daily PnL: $-20.06
2025-02-19, BUY CREATE 0.01 lots, Entry: 2932.79, SL: 2910.06 (dist: 22.73), TP: 2966.89
---- [WARNING 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2910.056623264466 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2910.056623264466 to 2910.05.
---- [WARNING 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2966.890065103301 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:16:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2966.890065103301 to 2966.89.
2025-02-19 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2932.79, ref_id: 13
2025-02-19 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2910.05, ref_id: 14
2025-02-19 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2966.89, ref_id: 15
2025-02-19 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2932.79, ref_id: 13
2025-02-19 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2910.05, ref_id: 14
2025-02-19 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2966.89, ref_id: 15
2025-02-19, BUY EXECUTED, Price: 2932.74, Cost: 2932.74, Comm: 0.00
2025-02-19 14:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2932.74, ref_id: 13
2025-02-25, SELL EXECUTED, Price: 2910.05, Cost: 2932.74, Comm: 0.00
2025-02-25 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2910.05, ref_id: 14
2025-02-25, Order Failed: Canceled
2025-02-25 23:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2966.89, ref_id: 15
2025-02-25, TRADE PROFIT, GROSS -22.69, NET -22.69
2025-02-25, Daily PnL: $-22.69
2025-02-26, SELL CREATE 0.01 lots, Entry: 2918.36, SL: 2938.36 (dist: 20.00), TP: 2888.36
2025-02-26 10:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2918.36, ref_id: 16
2025-02-26 10:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2938.36, ref_id: 17
2025-02-26 10:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2888.36, ref_id: 18
2025-02-26 10:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2918.36, ref_id: 16
2025-02-26 10:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2938.36, ref_id: 17
2025-02-26 10:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2888.36, ref_id: 18
2025-02-26, SELL EXECUTED, Price: 2918.91, Cost: 2918.91, Comm: 0.00
2025-02-26 10:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2918.91, ref_id: 16
2025-02-27, BUY EXECUTED, Price: 2888.36, Cost: 2918.91, Comm: 0.00
2025-02-27 15:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.01, executed_price: 2888.36, ref_id: 18
2025-02-27, Order Failed: Canceled
2025-02-27 15:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2938.36, ref_id: 17
2025-02-27, TRADE PROFIT, GROSS 30.55, NET 30.55
2025-02-27, Daily PnL: $30.55

=== BACKTEST RESULTS ===
--------- Returns ---------
{
    "rtot": 0.00020371999999999835,
    "ravg": 1.112369922201194e-05,
    "rnorm": 0.0030879194398460165,
    "rnorm100": 130.87919439846016,
    "rtot_new": 1.0203719999999998,
    "rnorm_new": 1.3087919439846016
}
===========================
---- [INFO 2025-12-10 14:16:09 +0800 strategy_utils.extract_suggest_improvements_and_plot_run_results:348]: ==== Full analyzers output: =========
"{'returns': OrderedDict({'rtot': 0.00020371999999999835, 'ravg': 1.112369922201194e-05, 'rnorm': 0.0030879194398460165, 'rnorm100': 130.87919439846016, 'rtot_new': 1.0203719999999998, 'rnorm_new': 1.3087919439846016}), 'drawdown': AutoOrderedDict({'len': 882, 'drawdown': 0.717028761715507, 'moneydown': 18.42300000000023, 'max': AutoOrderedDict({'len': 882, 'drawdown': 1.9872862934754334, 'moneydown': 51.060399999999845})}), 'vwr': OrderedDict({'vwr': 0.0007664097560838536}), 'tradeanalyzer': AutoOrderedDict({'total': AutoOrderedDict({'total': 6, 'open': 0, 'closed': 6}), 'streak': AutoOrderedDict({'won': AutoOrderedDict({'current': 1, 'longest': 1}), 'lost': AutoOrderedDict({'current': 0, 'longest': 2})}), 'pnl': AutoOrderedDict({'gross': AutoOrderedDict({'total': 50.92999999999999, 'average': 8.488333333333332}), 'net': AutoOrderedDict({'total': 50.92999999999999, 'average': 8.488333333333332})}), 'won': AutoOrderedDict({'total': 3, 'pnl': AutoOrderedDict({'total': 113.6, 'average': 3"
========== Backtest finished after 0:00:02.072779!
