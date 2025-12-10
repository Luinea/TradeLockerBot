========== Starting to setup a Backtest:
Using configuration: symbolName='XAUUSD.PRO' symbolId=781 resolution='30m' commission=0.0 startDate=datetime.datetime(2025, 2, 1, 0, 0, tzinfo=TzInfo(UTC)) endDate=datetime.datetime(2025, 12, 10, 0, 0, tzinfo=TzInfo(UTC)) leverage=100.0 margin=2500.0 strategyParamsInput={'asian_start_hour': 0, 'asian_end_hour': 8, 'trade_end_hour': 20, 'risk_per_trade_percent': 0.01, 'max_daily_trades': 3, 'max_daily_loss': 75, 'max_drawdown_percent': 0.06, 'max_lots': 0.5, 'contract_size': 100, 'tp_risk_reward': 1.5}
---- [INFO 2025-12-10 14:54:47 +0800 strategy_utils.add_sizer_to_cerebro:297]: Using default sizer 'TLLotSizer'
========== Setup finished. Backtest is running...
---, London Breakout Strategy Started
2025-02-03, BREAKOUT BUY: Price 2797.82 > Asian High 2793.80
---- [WARNING 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2784.1000000000004 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2784.1000000000004 to 2784.1.
---- [WARNING 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2818.3999999999996 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2818.3999999999996 to 2818.4.
2025-02-03 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2797.82, ref_id: 1
2025-02-03 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2784.1, ref_id: 2
2025-02-03 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2818.4, ref_id: 3
2025-02-03 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2797.82, ref_id: 1
2025-02-03 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2784.1, ref_id: 2
2025-02-03 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2818.4, ref_id: 3
2025-02-03 17:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2797.73, ref_id: 1
2025-02-03 23:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.02, executed_price: 2818.4, ref_id: 3
2025-02-03 23:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.02, price: 2784.1, ref_id: 2
2025-02-03, TRADE PROFIT, GROSS 41.34, NET 41.34
2025-02-03, Daily PnL: $41.34
2025-02-03, BREAKOUT BUY: Price 2828.67 > Asian High 2793.80
---- [WARNING 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2784.1000000000004 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2784.1000000000004 to 2784.1.
---- [WARNING 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2895.5249999999996 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2895.5249999999996 to 2895.52.
2025-02-03 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2828.67, ref_id: 4
2025-02-03 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2784.1, ref_id: 5
2025-02-03 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2895.52, ref_id: 6
2025-02-03 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2828.67, ref_id: 4
2025-02-03 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2784.1, ref_id: 5
2025-02-03 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2895.52, ref_id: 6
2025-02-03 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2828.92, ref_id: 4
2025-02-03, End of Day - Closing Positions
2025-02-04 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2818.31, ref_id: 7
2025-02-04 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2818.31, ref_id: 7
2025-02-04 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2818.3, ref_id: 7
2025-02-03, TRADE PROFIT, GROSS -10.62, NET -10.62
2025-02-03, Daily PnL: $30.72
2025-02-04, BREAKOUT BUY: Price 2834.92 > Asian High 2823.34
---- [WARNING 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2864.1400000000003 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2864.1400000000003 to 2864.14.
2025-02-04 22:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2834.92, ref_id: 8
2025-02-04 22:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2815.44, ref_id: 9
2025-02-04 22:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2864.14, ref_id: 10
2025-02-04 22:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2834.92, ref_id: 8
2025-02-04 22:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2815.44, ref_id: 9
2025-02-04 22:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2864.14, ref_id: 10
2025-02-04 22:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2834.94, ref_id: 8
2025-02-04, End of Day - Closing Positions
2025-02-05 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2843.01, ref_id: 11
2025-02-05 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2843.01, ref_id: 11
2025-02-05 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2843.1, ref_id: 11
2025-02-04, TRADE PROFIT, GROSS 8.16, NET 8.16
2025-02-04, Daily PnL: $8.16
2025-02-05 16:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2864.14, ref_id: 10
2025-02-05 16:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2815.44, ref_id: 9
2025-02-05, End of Day - Closing Positions
2025-02-06 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2863.53, ref_id: 12
2025-02-06 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2863.53, ref_id: 12
2025-02-06 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2863.71, ref_id: 12
2025-02-05, TRADE PROFIT, GROSS 0.43, NET 0.43
2025-02-05, Daily PnL: $0.43
2025-02-06, BREAKOUT SELL: Price 2855.87 < Asian Low 2859.05
2025-02-06 16:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2855.87, ref_id: 13
2025-02-06 16:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 14
2025-02-06 16:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2841.68, ref_id: 15
2025-02-06 16:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2855.87, ref_id: 13
2025-02-06 16:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 14
2025-02-06 16:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2841.68, ref_id: 15
2025-02-06 16:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2855.84, ref_id: 13
2025-02-06 20:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.03, executed_price: 2865.33, ref_id: 14
2025-02-06 20:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2841.68, ref_id: 15
2025-02-06, TRADE PROFIT, GROSS -28.47, NET -28.47
2025-02-06, Daily PnL: $-28.47
2025-02-06, BREAKOUT SELL: Price 2856.73 < Asian Low 2859.05
2025-02-06 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2856.73, ref_id: 16
2025-02-06 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 17
2025-02-06 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2843.83, ref_id: 18
2025-02-06 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2856.73, ref_id: 16
2025-02-06 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 17
2025-02-06 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2843.83, ref_id: 18
2025-02-06 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2856.69, ref_id: 16
2025-02-06 23:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.03, executed_price: 2843.83, ref_id: 18
2025-02-06 23:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 17
2025-02-06, TRADE PROFIT, GROSS 38.58, NET 38.58
2025-02-06, Daily PnL: $10.11
2025-02-06, BREAKOUT SELL: Price 2842.00 < Asian Low 2859.05
---- [WARNING 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2807.005 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:47 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2807.005 to 2807.0.
2025-02-06 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2842.0, ref_id: 19
2025-02-06 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2865.33, ref_id: 20
2025-02-06 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2807.0, ref_id: 21
2025-02-06 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2842.0, ref_id: 19
2025-02-06 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2865.33, ref_id: 20
2025-02-06 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2807.0, ref_id: 21
2025-02-06 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2841.9, ref_id: 19
2025-02-06, End of Day - Closing Positions
2025-02-07 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2853.76, ref_id: 22
2025-02-07 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2853.76, ref_id: 22
2025-02-07 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2853.79, ref_id: 22
2025-02-06, TRADE PROFIT, GROSS -11.89, NET -11.89
2025-02-06, Daily PnL: $-1.78
2025-02-07 10:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.01, executed_price: 2865.33, ref_id: 20
2025-02-07 10:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2807.0, ref_id: 21
2025-02-07, End of Day - Closing Positions
2025-02-08 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2859.74, ref_id: 23
2025-02-08 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2859.74, ref_id: 23
2025-02-08 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2859.69, ref_id: 23
2025-02-07, TRADE PROFIT, GROSS -5.64, NET -5.64
2025-02-07, Daily PnL: $-5.64
2025-02-10 16:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2895.52, ref_id: 6
2025-02-10 16:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2784.1, ref_id: 5
2025-02-10, End of Day - Closing Positions
2025-02-11 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2904.34, ref_id: 24
2025-02-11 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2904.34, ref_id: 24
2025-02-11 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2904.18, ref_id: 24
2025-02-10, TRADE PROFIT, GROSS -8.66, NET -8.66
2025-02-10, Daily PnL: $-8.66
2025-02-11, BREAKOUT SELL: Price 2907.44 < Asian Low 2911.07
---- [WARNING 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2925.465 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2925.465 to 2925.46.
---- [WARNING 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2880.4025 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2880.4025 to 2880.4.
2025-02-11 17:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2907.44, ref_id: 25
2025-02-11 17:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2925.46, ref_id: 26
2025-02-11 17:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2880.4, ref_id: 27
2025-02-11 17:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2907.44, ref_id: 25
2025-02-11 17:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2925.46, ref_id: 26
2025-02-11 17:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2880.4, ref_id: 27
2025-02-11 17:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2907.2, ref_id: 25
2025-02-11, End of Day - Closing Positions
2025-02-12 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2899.99, ref_id: 28
2025-02-12 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2899.99, ref_id: 28
2025-02-12 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2899.99, ref_id: 28
2025-02-11, TRADE PROFIT, GROSS 7.21, NET 7.21
2025-02-11, Daily PnL: $7.21
2025-02-12 19:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.01, executed_price: 2880.4, ref_id: 27
2025-02-12 19:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2925.46, ref_id: 26
2025-02-12, End of Day - Closing Positions
2025-02-13 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2897.96, ref_id: 29
2025-02-13 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2897.96, ref_id: 29
2025-02-13 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2897.95, ref_id: 29
2025-02-12, TRADE PROFIT, GROSS 17.55, NET 17.55
2025-02-12, Daily PnL: $17.55
2025-02-13, BREAKOUT BUY: Price 2924.09 > Asian High 2922.39
---- [WARNING 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2912.435 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2912.435 to 2912.43.
---- [WARNING 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2941.5725 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2941.5725 to 2941.57.
2025-02-14 03:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2924.09, ref_id: 30
2025-02-14 03:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2912.43, ref_id: 31
2025-02-14 03:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2941.57, ref_id: 32
2025-02-14 03:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2924.09, ref_id: 30
2025-02-14 03:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2912.43, ref_id: 31
2025-02-14 03:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2941.57, ref_id: 32
2025-02-14 03:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2923.93, ref_id: 30
2025-02-13, End of Day - Closing Positions
2025-02-14 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2926.86, ref_id: 33
2025-02-14 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2926.86, ref_id: 33
2025-02-14 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2926.83, ref_id: 33
2025-02-13, TRADE PROFIT, GROSS 5.80, NET 5.80
2025-02-13, Daily PnL: $5.80
2025-02-14, BREAKOUT BUY: Price 2936.61 > Asian High 2934.21
2025-02-14 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2936.61, ref_id: 34
2025-02-14 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2929.21, ref_id: 35
2025-02-14 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2947.71, ref_id: 36
2025-02-14 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2936.61, ref_id: 34
2025-02-14 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2929.21, ref_id: 35
2025-02-14 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2947.71, ref_id: 36
2025-02-14 17:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2936.59, ref_id: 34
2025-02-14 21:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2929.21, ref_id: 35
2025-02-14 21:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2947.71, ref_id: 36
2025-02-14, TRADE PROFIT, GROSS -22.14, NET -22.14
2025-02-14, Daily PnL: $-22.14
2025-02-14, BREAKOUT SELL: Price 2920.50 < Asian Low 2924.21
---- [WARNING 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2907.435 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2907.435 to 2907.43.
2025-02-14 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2920.5, ref_id: 37
2025-02-14 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2929.21, ref_id: 38
2025-02-14 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2907.43, ref_id: 39
2025-02-14 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2920.5, ref_id: 37
2025-02-14 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2929.21, ref_id: 38
2025-02-14 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2907.43, ref_id: 39
2025-02-14 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2920.52, ref_id: 37
2025-02-14 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.02, executed_price: 2912.43, ref_id: 31
2025-02-14 23:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2941.57, ref_id: 32
2025-02-14 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.03, executed_price: 2907.43, ref_id: 39
2025-02-14 23:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2929.21, ref_id: 38
2025-02-14, End of Day - Closing Positions
---- [WARNING 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:291]: Order size 0.020000000000000004 is not a multiple of the lot step 0.01.
---- [INFO 2025-12-10 14:54:48 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order size from 0.020000000000000004 to 0.02.
2025-02-15 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2880.56, ref_id: 40
2025-02-15 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2880.56, ref_id: 40
2025-02-15 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2880.5, ref_id: 40

=== BACKTEST RESULTS ===
--------- Returns ---------
{
    "rtot": 0.0005391199999999951,
    "ravg": 5.358056650251378e-06,
    "rnorm": 0.0006695740719372511,
    "rnorm100": 106.69574071937251,
    "rtot_new": 1.0539119999999995,
    "rnorm_new": 1.0669574071937251
}
===========================
---- [INFO 2025-12-10 14:54:51 +0800 strategy_utils.extract_suggest_improvements_and_plot_run_results:348]: ==== Full analyzers output: =========
"{'returns': OrderedDict({'rtot': 0.0005391199999999951, 'ravg': 5.358056650251378e-06, 'rnorm': 0.0006695740719372511, 'rnorm100': 106.69574071937251, 'rtot_new': 1.0539119999999995, 'rnorm_new': 1.0669574071937251}), 'drawdown': AutoOrderedDict({'len': 0, 'drawdown': 0.0, 'moneydown': 0.0, 'max': AutoOrderedDict({'len': 141, 'drawdown': 1.8792284866468631, 'moneydown': 48.130799999999454})}), 'vwr': OrderedDict({'vwr': 0.0003350136866185979}), 'tradeanalyzer': AutoOrderedDict({'total': AutoOrderedDict({'total': 14, 'open': 1, 'closed': 13}), 'streak': AutoOrderedDict({'won': AutoOrderedDict({'current': 0, 'longest': 3}), 'lost': AutoOrderedDict({'current': 1, 'longest': 3})}), 'pnl': AutoOrderedDict({'gross': AutoOrderedDict({'total': 31.650000000001008, 'average': 2.434615384615462}), 'net': AutoOrderedDict({'total': 31.650000000001008, 'average': 2.434615384615462})}), 'won': AutoOrderedDict({'total': 7, 'pnl': AutoOrderedDict({'total': 119.06999999999998, 'average': 17.009999999999"
========== Backtest finished after 0:00:03.978755!
