========== Starting to setup a Backtest:
Using configuration: symbolName='XAUUSD.PRO' symbolId=781 resolution='15m' commission=0.0 startDate=datetime.datetime(2025, 2, 1, 0, 0, tzinfo=TzInfo(UTC)) endDate=datetime.datetime(2025, 3, 1, 0, 0, tzinfo=TzInfo(UTC)) leverage=100.0 margin=2500.0 strategyParamsInput={'macd_fast': 12, 'macd_slow': 26, 'macd_signal': 9, 'ema_period': 200, 'risk_per_trade_percent': 0.01, 'max_daily_trades': 3, 'max_daily_loss': 75, 'max_drawdown_percent': 0.06, 'max_lots': 0.5, 'contract_size': 100, 'min_sl_distance': 10, 'ema_sl_multiplier': 1, 'tp_risk_reward': 1.5, 'sr_lookback': 20, 'sr_threshold': 5, 'use_sr_filter': True}
---- [INFO 2025-12-10 14:00:17 +0800 strategy_utils.add_sizer_to_cerebro:297]: Using default sizer 'TLLotSizer'
========== Setup finished. Backtest is running...
---, Strategy Started with Risk Hardening
2025-02-05, BUY CREATE 0.01 lots, Entry: 2866.55, SL: 2842.96 (dist: 23.59), TP: 2901.94
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2842.957621820205 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2842.957621820205 to 2842.95.
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2901.9385672696926 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2901.9385672696926 to 2901.93.
2025-02-06 07:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2866.55, ref_id: 1
2025-02-06 07:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2842.95, ref_id: 2
2025-02-06 07:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2901.93, ref_id: 3
2025-02-06 07:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2866.55, ref_id: 1
2025-02-06 07:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2842.95, ref_id: 2
2025-02-06 07:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2901.93, ref_id: 3
2025-02-05, BUY EXECUTED, Price: 2866.53, Cost: 2866.53, Comm: 0.00
2025-02-06 07:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2866.53, ref_id: 1
2025-02-06, SELL EXECUTED, Price: 2842.95, Cost: 2866.53, Comm: 0.00
2025-02-06 23:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2842.95, ref_id: 2
2025-02-06, Order Failed: Canceled
2025-02-06 23:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2901.93, ref_id: 3
2025-02-06, TRADE PROFIT, GROSS -23.58, NET -23.58
2025-02-06, Daily PnL: $-23.58
2025-02-07, BUY CREATE 0.02 lots, Entry: 2862.55, SL: 2852.55 (dist: 10.00), TP: 2877.55
2025-02-08 05:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2862.55, ref_id: 4
2025-02-08 05:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2852.55, ref_id: 5
2025-02-08 05:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2877.55, ref_id: 6
2025-02-08 05:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2862.55, ref_id: 4
2025-02-08 05:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2852.55, ref_id: 5
2025-02-08 05:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2877.55, ref_id: 6
2025-02-07, BUY EXECUTED, Price: 2862.48, Cost: 5724.96, Comm: 0.00
2025-02-08 05:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2862.48, ref_id: 4
2025-02-10, SELL EXECUTED, Price: 2877.55, Cost: 5724.96, Comm: 0.00
2025-02-10 12:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.02, executed_price: 2877.55, ref_id: 6
2025-02-10, Order Failed: Canceled
2025-02-10 12:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.02, price: 2852.55, ref_id: 5
2025-02-10, TRADE PROFIT, GROSS 30.14, NET 30.14
2025-02-10, Daily PnL: $30.14
2025-02-11, BUY CREATE 0.03 lots, Entry: 2898.44, SL: 2888.44 (dist: 10.00), TP: 2913.44
2025-02-11 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2898.44, ref_id: 7
2025-02-11 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2888.44, ref_id: 8
2025-02-11 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2913.44, ref_id: 9
2025-02-11 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2898.44, ref_id: 7
2025-02-11 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2888.44, ref_id: 8
2025-02-11 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2913.44, ref_id: 9
2025-02-11, BUY EXECUTED, Price: 2898.36, Cost: 8695.08, Comm: 0.00
2025-02-11 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2898.36, ref_id: 7
2025-02-12, SELL EXECUTED, Price: 2888.44, Cost: 8695.08, Comm: 0.00
2025-02-12 09:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2888.44, ref_id: 8
2025-02-12, Order Failed: Canceled
2025-02-12 09:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2913.44, ref_id: 9
2025-02-12, TRADE PROFIT, GROSS -29.76, NET -29.76
2025-02-12, Daily PnL: $-29.76
2025-02-13, BUY CREATE 0.02 lots, Entry: 2916.25, SL: 2903.92 (dist: 12.33), TP: 2934.75
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2903.916624759869 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2903.916624759869 to 2903.91.
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2934.7500628601965 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2934.7500628601965 to 2934.75.
2025-02-13 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2916.25, ref_id: 10
2025-02-13 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2903.91, ref_id: 11
2025-02-13 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2934.75, ref_id: 12
2025-02-13 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2916.25, ref_id: 10
2025-02-13 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2903.91, ref_id: 11
2025-02-13 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2934.75, ref_id: 12
2025-02-13, BUY EXECUTED, Price: 2916.13, Cost: 5832.26, Comm: 0.00
2025-02-13 23:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2916.13, ref_id: 10
2025-02-14, SELL EXECUTED, Price: 2934.75, Cost: 5832.26, Comm: 0.00
2025-02-14 14:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.02, executed_price: 2934.75, ref_id: 12
2025-02-14, Order Failed: Canceled
2025-02-14 14:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.02, price: 2903.91, ref_id: 11
2025-02-14, TRADE PROFIT, GROSS 37.24, NET 37.24
2025-02-14, Daily PnL: $37.24
2025-02-17, SELL CREATE 0.02 lots, Entry: 2895.95, SL: 2907.34 (dist: 11.39), TP: 2878.87
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2907.3392680045313 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2907.3392680045313 to 2907.33.
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2878.866097993203 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2878.866097993203 to 2878.86.
2025-02-17 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2895.95, ref_id: 13
2025-02-17 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2907.33, ref_id: 14
2025-02-17 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2878.86, ref_id: 15
2025-02-17 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2895.95, ref_id: 13
2025-02-17 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2907.33, ref_id: 14
2025-02-17 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2878.86, ref_id: 15
2025-02-17, SELL EXECUTED, Price: 2895.89, Cost: 5791.78, Comm: 0.00
2025-02-17 14:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2895.89, ref_id: 13
2025-02-18, BUY EXECUTED, Price: 2907.33, Cost: 5791.78, Comm: 0.00
2025-02-18 11:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.02, executed_price: 2907.33, ref_id: 14
2025-02-18, Order Failed: Canceled
2025-02-18 11:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2878.86, ref_id: 15
2025-02-18, TRADE PROFIT, GROSS -22.88, NET -22.88
2025-02-18, Daily PnL: $-22.88
2025-02-19, BUY CREATE 0.02 lots, Entry: 2932.79, SL: 2917.63 (dist: 15.16), TP: 2955.52
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2917.634415509644 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2917.634415509644 to 2917.63.
---- [WARNING 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2955.523376735534 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2955.523376735534 to 2955.52.
2025-02-19 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2932.79, ref_id: 16
2025-02-19 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2917.63, ref_id: 17
2025-02-19 14:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2955.52, ref_id: 18
2025-02-19 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2932.79, ref_id: 16
2025-02-19 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2917.63, ref_id: 17
2025-02-19 14:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2955.52, ref_id: 18
2025-02-19, BUY EXECUTED, Price: 2932.74, Cost: 5865.48, Comm: 0.00
2025-02-19 14:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2932.74, ref_id: 16
2025-02-21, SELL EXECUTED, Price: 2917.63, Cost: 5865.48, Comm: 0.00
2025-02-21 16:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.02, executed_price: 2917.63, ref_id: 17
2025-02-21, Order Failed: Canceled
2025-02-21 16:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2955.52, ref_id: 18
2025-02-21, TRADE PROFIT, GROSS -30.22, NET -30.22
2025-02-21, Daily PnL: $-30.22
2025-02-24, BUY CREATE 0.02 lots, Entry: 2944.00, SL: 2934.00 (dist: 10.00), TP: 2959.00
2025-02-25 01:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2944.0, ref_id: 19
2025-02-25 01:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2934.0, ref_id: 20
2025-02-25 01:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2959.0, ref_id: 21
2025-02-25 01:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2944.0, ref_id: 19
2025-02-25 01:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2934.0, ref_id: 20
2025-02-25 01:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2959.0, ref_id: 21
2025-02-24, BUY EXECUTED, Price: 2944.03, Cost: 5888.06, Comm: 0.00
2025-02-25 01:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2944.03, ref_id: 19
2025-02-25, SELL EXECUTED, Price: 2934.00, Cost: 5888.06, Comm: 0.00
2025-02-25 15:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.02, executed_price: 2934.0, ref_id: 20
2025-02-25, Order Failed: Canceled
2025-02-25 15:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2959.0, ref_id: 21
2025-02-25, TRADE PROFIT, GROSS -20.06, NET -20.06
2025-02-25, Daily PnL: $-20.06
2025-02-25, BUY CREATE 0.02 lots, Entry: 2940.83, SL: 2930.83 (dist: 10.00), TP: 2955.83
2025-02-25 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2940.83, ref_id: 22
2025-02-25 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2930.83, ref_id: 23
2025-02-25 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2955.83, ref_id: 24
2025-02-25 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2940.83, ref_id: 22
2025-02-25 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2930.83, ref_id: 23
2025-02-25 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2955.83, ref_id: 24
2025-02-25, BUY EXECUTED, Price: 2940.89, Cost: 5881.78, Comm: 0.00
2025-02-25 17:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2940.89, ref_id: 22
2025-02-25, SELL EXECUTED, Price: 2930.83, Cost: 5881.78, Comm: 0.00
2025-02-25 20:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.02, executed_price: 2930.83, ref_id: 23
2025-02-25, Order Failed: Canceled
2025-02-25 20:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2955.83, ref_id: 24
2025-02-25, TRADE PROFIT, GROSS -20.12, NET -20.12
2025-02-25, Daily PnL: $-40.18
2025-02-25, BUY CREATE 0.02 lots, Entry: 2939.77, SL: 2929.77 (dist: 10.00), TP: 2954.77
2025-02-25 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2939.77, ref_id: 25
2025-02-25 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2929.77, ref_id: 26
2025-02-25 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2954.77, ref_id: 27
2025-02-25 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2939.77, ref_id: 25
2025-02-25 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2929.77, ref_id: 26
2025-02-25 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2954.77, ref_id: 27
2025-02-25, BUY EXECUTED, Price: 2939.86, Cost: 5879.72, Comm: 0.00
2025-02-25 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2939.86, ref_id: 25
2025-02-25, SELL EXECUTED, Price: 2929.77, Cost: 5879.72, Comm: 0.00
2025-02-25 23:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.02, executed_price: 2929.77, ref_id: 26
2025-02-25, Order Failed: Canceled
2025-02-25 23:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2954.77, ref_id: 27
2025-02-25, TRADE PROFIT, GROSS -20.18, NET -20.18
2025-02-25, Daily PnL: $-60.36
2025-02-26, SELL CREATE 0.02 lots, Entry: 2918.36, SL: 2930.54 (dist: 12.18), TP: 2900.09
---- [WARNING 2025-12-10 14:00:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2930.5401591100176 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2930.5401591100176 to 2930.54.
---- [WARNING 2025-12-10 14:00:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2900.089761334974 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:00:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2900.089761334974 to 2900.08.
2025-02-26 10:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2918.36, ref_id: 28
2025-02-26 10:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2930.54, ref_id: 29
2025-02-26 10:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2900.08, ref_id: 30
2025-02-26 10:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2918.36, ref_id: 28
2025-02-26 10:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2930.54, ref_id: 29
2025-02-26 10:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2900.08, ref_id: 30
2025-02-26, SELL EXECUTED, Price: 2918.91, Cost: 5837.82, Comm: 0.00
2025-02-26 10:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2918.91, ref_id: 28
2025-02-26, BUY EXECUTED, Price: 2900.08, Cost: 5837.82, Comm: 0.00
2025-02-26 22:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.02, executed_price: 2900.08, ref_id: 30
2025-02-26, Order Failed: Canceled
2025-02-26 22:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2930.54, ref_id: 29
2025-02-26, TRADE PROFIT, GROSS 37.66, NET 37.66
2025-02-26, Daily PnL: $37.66
2025-02-26, SELL CREATE 0.02 lots, Entry: 2912.81, SL: 2922.81 (dist: 10.00), TP: 2897.81
2025-02-27 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2912.81, ref_id: 31
2025-02-27 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2922.81, ref_id: 32
2025-02-27 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2897.81, ref_id: 33
2025-02-27 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2912.81, ref_id: 31
2025-02-27 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2922.81, ref_id: 32
2025-02-27 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2897.81, ref_id: 33
2025-02-26, SELL EXECUTED, Price: 2913.02, Cost: 5826.04, Comm: 0.00
2025-02-27 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2913.02, ref_id: 31
2025-02-27, BUY EXECUTED, Price: 2897.81, Cost: 5826.04, Comm: 0.00
2025-02-27 13:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.02, executed_price: 2897.81, ref_id: 33
2025-02-27, Order Failed: Canceled
2025-02-27 13:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2922.81, ref_id: 32
2025-02-27, TRADE PROFIT, GROSS 30.42, NET 30.42
2025-02-27, Daily PnL: $30.42
