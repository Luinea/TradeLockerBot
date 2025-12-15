========== Starting to setup a Backtest:
Using configuration: symbolName='XAUUSD.PRO' symbolId=781 resolution='5m' commission=0.0 startDate=datetime.datetime(2025, 3, 1, 0, 0, tzinfo=TzInfo(UTC)) endDate=datetime.datetime(2025, 3, 30, 0, 0, tzinfo=TzInfo(UTC)) leverage=100.0 margin=2000.0 strategyParamsInput={'adx_period': 14, 'adx_trend_threshold': 25, 'bb_period': 20, 'bb_dev': 2, 'ema_fast': 8, 'ema_medium': 21, 'ema_slow': 50, 'rsi_period': 14, 'rsi_oversold': 30, 'rsi_overbought': 70, 'stoch_k': 5, 'stoch_d': 3, 'stoch_slow': 3, 'stoch_oversold': 25, 'stoch_overbought': 75, 'use_ha_filter': True, 'atr_period': 14, 'atr_sl_multiplier': 1.5, 'tp_risk_reward': 2, 'trade_start_hour': 13, 'trade_end_hour': 17, 'use_time_filter': True, 'risk_per_trade_percent': 0.01, 'max_daily_trades': 3, 'max_daily_loss': 75, 'max_drawdown_percent': 0.06, 'max_lots': 0.5, 'contract_size': 100}
---- [INFO 2025-12-15 16:13:08 +0800 strategy_utils.add_sizer_to_cerebro:297]: Using default sizer 'TLLotSizer'
========== Setup finished. Backtest is running...
---, XAU Adaptive Strategy Started
2025-03-03, TREND: Pullback complete, EMA8=2873.53 | ADX=27.5
2025-03-03,   LONG: Entry=2874.25, SL=2871.13, TP=2880.48, Size=0.06
---- [WARNING 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2871.133764327231 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2871.133764327231 to 2871.13.
---- [WARNING 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2880.4824713455378 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2880.4824713455378 to 2880.48.
2025-03-03 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.06, price: 2874.25, ref_id: 1
2025-03-03 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.06, price: 2871.13, ref_id: 2
2025-03-03 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.06, price: 2880.48, ref_id: 3
2025-03-03 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.06, price: 2874.25, ref_id: 1
2025-03-03 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.06, price: 2871.13, ref_id: 2
2025-03-03 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.06, price: 2880.48, ref_id: 3
2025-03-03, BUY EXECUTED @ 2874.13, Size: 0.06
2025-03-03 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.06, executed_price: 2874.13, ref_id: 1
2025-03-03, SELL EXECUTED @ 2880.48, Size: -0.06
2025-03-03 22:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.06, executed_price: 2880.48, ref_id: 3
2025-03-03, Order Failed: Canceled
2025-03-03 22:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.06, price: 2871.13, ref_id: 2
2025-03-03, TRADE PROFIT: $38.10 [Regime: TRENDING]
2025-03-04, TREND: Pullback complete, EMA8=2923.45 | ADX=27.3
2025-03-04,   LONG: Entry=2925.97, SL=2922.74, TP=2932.43, Size=0.06
---- [WARNING 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2922.7375563011055 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2922.7375563011055 to 2922.73.
---- [WARNING 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2932.434887397788 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2932.434887397788 to 2932.43.
2025-03-04 21:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.06, price: 2925.97, ref_id: 4
2025-03-04 21:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.06, price: 2922.73, ref_id: 5
2025-03-04 21:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.06, price: 2932.43, ref_id: 6
2025-03-04 21:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.06, price: 2925.97, ref_id: 4
2025-03-04 21:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.06, price: 2922.73, ref_id: 5
2025-03-04 21:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.06, price: 2932.43, ref_id: 6
2025-03-04, BUY EXECUTED @ 2925.96, Size: 0.06
2025-03-04 21:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.06, executed_price: 2925.96, ref_id: 4
2025-03-04, SELL EXECUTED @ 2922.73, Size: -0.06
2025-03-04 21:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.06, executed_price: 2922.73, ref_id: 5
2025-03-04, Order Failed: Canceled
2025-03-04 21:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.06, price: 2932.43, ref_id: 6
2025-03-04, TRADE PROFIT: $-19.38 [Regime: TRENDING]
2025-03-04, TREND: Pullback complete, EMA8=2909.42 | ADX=42.7
2025-03-04,   SHORT: Entry=2905.59, SL=2911.85, TP=2893.07, Size=0.03
---- [WARNING 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2911.850147392859 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2911.850147392859 to 2911.85.
---- [WARNING 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2893.0697052142823 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:08 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2893.0697052142823 to 2893.06.
2025-03-04 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2905.59, ref_id: 7
2025-03-04 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2911.85, ref_id: 8
2025-03-04 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2893.06, ref_id: 9
2025-03-04 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2905.59, ref_id: 7
2025-03-04 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2911.85, ref_id: 8
2025-03-04 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2893.06, ref_id: 9
2025-03-04, SELL EXECUTED @ 2905.59, Size: -0.03
2025-03-04 23:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2905.59, ref_id: 7
2025-03-04, BUY EXECUTED @ 2911.85, Size: 0.03
2025-03-05 00:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.03, executed_price: 2911.85, ref_id: 8
2025-03-04, Order Failed: Canceled
2025-03-05 00:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2893.06, ref_id: 9
2025-03-04, TRADE PROFIT: $-18.78 [Regime: TRENDING]
2025-03-05, TREND: Pullback complete, EMA8=2902.79 | ADX=31.4
2025-03-05,   SHORT: Entry=2901.72, SL=2907.91, TP=2889.35, Size=0.03
---- [WARNING 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2907.905295160956 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2907.905295160956 to 2907.9.
---- [WARNING 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2889.3494096780873 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2889.3494096780873 to 2889.34.
2025-03-05 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2901.72, ref_id: 10
2025-03-05 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2907.9, ref_id: 11
2025-03-05 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2889.34, ref_id: 12
2025-03-05 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2901.72, ref_id: 10
2025-03-05 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2907.9, ref_id: 11
2025-03-05 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2889.34, ref_id: 12
2025-03-05, SELL EXECUTED @ 2901.71, Size: -0.03
2025-03-05 22:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2901.71, ref_id: 10
2025-03-05, BUY EXECUTED @ 2907.90, Size: 0.03
2025-03-05 22:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.03, executed_price: 2907.9, ref_id: 11
2025-03-05, Order Failed: Canceled
2025-03-05 22:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2889.34, ref_id: 12
2025-03-05, TRADE PROFIT: $-18.57 [Regime: TRENDING]
2025-03-06, TREND: Pullback complete, EMA8=2915.90 | ADX=25.2
2025-03-06,   LONG: Entry=2916.93, SL=2911.18, TP=2928.43, Size=0.03
---- [WARNING 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2911.1820625711057 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2911.1820625711057 to 2911.18.
---- [WARNING 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2928.4258748577886 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:09 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2928.4258748577886 to 2928.42.
2025-03-06 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2916.93, ref_id: 13
2025-03-06 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2911.18, ref_id: 14
2025-03-06 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2928.42, ref_id: 15
2025-03-06 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2916.93, ref_id: 13
2025-03-06 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2911.18, ref_id: 14
2025-03-06 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2928.42, ref_id: 15
2025-03-06, BUY EXECUTED @ 2916.83, Size: 0.03
2025-03-06 23:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2916.83, ref_id: 13
2025-03-06, SELL EXECUTED @ 2911.18, Size: -0.03
2025-03-06 23:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2911.18, ref_id: 14
2025-03-06, Order Failed: Canceled
2025-03-06 23:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2928.42, ref_id: 15
2025-03-06, TRADE PROFIT: $-16.95 [Regime: TRENDING]
2025-03-07, TREND: Pullback complete, EMA8=2916.61 | ADX=27.0
2025-03-07,   SHORT: Entry=2915.33, SL=2921.37, TP=2903.25, Size=0.03
---- [WARNING 2025-12-15 16:13:10 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2921.367959403067 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:10 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2921.367959403067 to 2921.36.
---- [WARNING 2025-12-15 16:13:10 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2903.254081193866 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:10 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2903.254081193866 to 2903.25.
2025-03-08 00:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2915.33, ref_id: 16
2025-03-08 00:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2921.36, ref_id: 17
2025-03-08 00:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2903.25, ref_id: 18
2025-03-08 00:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2915.33, ref_id: 16
2025-03-08 00:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2921.36, ref_id: 17
2025-03-08 00:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2903.25, ref_id: 18
2025-03-07, SELL EXECUTED @ 2915.33, Size: -0.03
2025-03-08 00:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2915.33, ref_id: 16
2025-03-07, BUY EXECUTED @ 2903.25, Size: 0.03
2025-03-08 02:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.03, executed_price: 2903.25, ref_id: 18
2025-03-07, Order Failed: Canceled
2025-03-08 02:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2921.36, ref_id: 17
2025-03-07, TRADE PROFIT: $36.24 [Regime: TRENDING]
2025-03-12, TREND: Pullback complete, EMA8=2924.17 | ADX=28.6
2025-03-12,   LONG: Entry=2925.83, SL=2921.67, TP=2934.15, Size=0.05
---- [WARNING 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2921.671049437945 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2921.671049437945 to 2921.67.
---- [WARNING 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2934.14790112411 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2934.14790112411 to 2934.14.
2025-03-12 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.05, price: 2925.83, ref_id: 19
2025-03-12 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.05, price: 2921.67, ref_id: 20
2025-03-12 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.05, price: 2934.14, ref_id: 21
2025-03-12 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.05, price: 2925.83, ref_id: 19
2025-03-12 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.05, price: 2921.67, ref_id: 20
2025-03-12 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.05, price: 2934.14, ref_id: 21
2025-03-12, BUY EXECUTED @ 2925.84, Size: 0.05
2025-03-12 23:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.05, executed_price: 2925.84, ref_id: 19
2025-03-12, SELL EXECUTED @ 2934.14, Size: -0.05
2025-03-13 00:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.05, executed_price: 2934.14, ref_id: 21
2025-03-12, Order Failed: Canceled
2025-03-13 00:10:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.05, price: 2921.67, ref_id: 20
2025-03-12, TRADE PROFIT: $41.50 [Regime: TRENDING]
2025-03-12, TREND: Pullback complete, EMA8=2928.98 | ADX=38.5
2025-03-12,   LONG: Entry=2935.41, SL=2931.20, TP=2943.82, Size=0.05
---- [WARNING 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2931.204834368182 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2931.204834368182 to 2931.2.
---- [WARNING 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2943.820331263635 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2943.820331263635 to 2943.82.
2025-03-13 00:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.05, price: 2935.41, ref_id: 22
2025-03-13 00:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.05, price: 2931.2, ref_id: 23
2025-03-13 00:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.05, price: 2943.82, ref_id: 24
2025-03-13 00:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.05, price: 2935.41, ref_id: 22
2025-03-13 00:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.05, price: 2931.2, ref_id: 23
2025-03-13 00:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.05, price: 2943.82, ref_id: 24
2025-03-12, BUY EXECUTED @ 2935.43, Size: 0.05
2025-03-13 00:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.05, executed_price: 2935.43, ref_id: 22
2025-03-12, SELL EXECUTED @ 2931.20, Size: -0.05
2025-03-13 04:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.05, executed_price: 2931.2, ref_id: 23
2025-03-12, Order Failed: Canceled
2025-03-13 04:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.05, price: 2943.82, ref_id: 24
2025-03-12, TRADE PROFIT: $-21.15 [Regime: TRENDING]
2025-03-13, TREND: Pullback complete, EMA8=2973.53 | ADX=51.0
2025-03-13,   LONG: Entry=2976.71, SL=2970.71, TP=2988.71, Size=0.03
---- [WARNING 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2970.708582479263 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2970.708582479263 to 2970.7.
---- [WARNING 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2988.7128350414746 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2988.7128350414746 to 2988.71.
2025-03-14 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2976.71, ref_id: 25
2025-03-14 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2970.7, ref_id: 26
2025-03-14 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2988.71, ref_id: 27
2025-03-14 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2976.71, ref_id: 25
2025-03-14 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2970.7, ref_id: 26
2025-03-14 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2988.71, ref_id: 27
2025-03-13, BUY EXECUTED @ 2976.47, Size: 0.03
2025-03-14 00:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2976.47, ref_id: 25
2025-03-13, SELL EXECUTED @ 2988.71, Size: -0.03
2025-03-14 05:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.03, executed_price: 2988.71, ref_id: 27
2025-03-13, Order Failed: Canceled
2025-03-14 05:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.03, price: 2970.7, ref_id: 26
2025-03-13, TRADE PROFIT: $36.72 [Regime: TRENDING]
2025-03-14, TREND: Pullback complete, EMA8=2989.73 | ADX=29.9
2025-03-14,   SHORT: Entry=2985.54, SL=2990.73, TP=2975.15, Size=0.04
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2990.734610961572 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2990.734610961572 to 2990.73.
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2975.1507780768566 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2975.1507780768566 to 2975.15.
2025-03-14 22:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.04, price: 2985.54, ref_id: 28
2025-03-14 22:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.04, price: 2990.73, ref_id: 29
2025-03-14 22:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2975.15, ref_id: 30
2025-03-14 22:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.04, price: 2985.54, ref_id: 28
2025-03-14 22:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.04, price: 2990.73, ref_id: 29
2025-03-14 22:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2975.15, ref_id: 30
2025-03-14, SELL EXECUTED @ 2985.57, Size: -0.04
2025-03-14 22:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.04, executed_price: 2985.57, ref_id: 28
2025-03-14, BUY EXECUTED @ 2990.73, Size: 0.04
2025-03-14 22:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.04, executed_price: 2990.73, ref_id: 29
2025-03-14, Order Failed: Canceled
2025-03-14 22:10:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.04, price: 2975.15, ref_id: 30
2025-03-14, TRADE PROFIT: $-20.64 [Regime: TRENDING]
2025-03-14, TREND: Pullback complete, EMA8=2989.71 | ADX=29.7
2025-03-14,   SHORT: Entry=2989.02, SL=2994.32, TP=2978.43, Size=0.04
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2994.317412959918 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2994.317412959918 to 2994.31.
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2978.425174080164 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2978.425174080164 to 2978.42.
2025-03-14 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.04, price: 2989.02, ref_id: 31
2025-03-14 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.04, price: 2994.31, ref_id: 32
2025-03-14 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2978.42, ref_id: 33
2025-03-14 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.04, price: 2989.02, ref_id: 31
2025-03-14 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.04, price: 2994.31, ref_id: 32
2025-03-14 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2978.42, ref_id: 33
2025-03-14, SELL EXECUTED @ 2988.93, Size: -0.04
2025-03-14 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.04, executed_price: 2988.93, ref_id: 31
2025-03-17, BUY EXECUTED @ 2994.31, Size: 0.04
2025-03-17 17:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.04, executed_price: 2994.31, ref_id: 32
2025-03-17, Order Failed: Canceled
2025-03-17 17:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.04, price: 2978.42, ref_id: 33
2025-03-17, TRADE PROFIT: $-21.52 [Regime: TRENDING]
2025-03-17, TREND: Pullback complete, EMA8=2988.95 | ADX=34.6
2025-03-17,   SHORT: Entry=2988.72, SL=2993.30, TP=2979.55, Size=0.04
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2993.3029782087183 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2993.3029782087183 to 2993.3.
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2979.554043582563 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2979.554043582563 to 2979.55.
2025-03-17 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.04, price: 2988.72, ref_id: 34
2025-03-17 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.04, price: 2993.3, ref_id: 35
2025-03-17 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2979.55, ref_id: 36
2025-03-17 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.04, price: 2988.72, ref_id: 34
2025-03-17 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.04, price: 2993.3, ref_id: 35
2025-03-17 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2979.55, ref_id: 36
2025-03-17, SELL EXECUTED @ 2988.81, Size: -0.04
2025-03-17 21:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.04, executed_price: 2988.81, ref_id: 34
2025-03-17, BUY EXECUTED @ 2993.30, Size: 0.04
2025-03-17 22:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.04, executed_price: 2993.3, ref_id: 35
2025-03-17, Order Failed: Canceled
2025-03-17 22:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.04, price: 2979.55, ref_id: 36
2025-03-17, TRADE PROFIT: $-17.96 [Regime: TRENDING]
2025-03-18, TREND: Pullback complete, EMA8=3033.57 | ADX=25.3
2025-03-18,   LONG: Entry=3034.84, SL=3031.25, TP=3042.03, Size=0.06
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3031.247038180969 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3031.247038180969 to 3031.24.
---- [WARNING 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3042.025923638062 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3042.025923638062 to 3042.02.
2025-03-18 21:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.06, price: 3034.84, ref_id: 37
2025-03-18 21:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.06, price: 3031.24, ref_id: 38
2025-03-18 21:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.06, price: 3042.02, ref_id: 39
2025-03-18 21:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.06, price: 3034.84, ref_id: 37
2025-03-18 21:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.06, price: 3031.24, ref_id: 38
2025-03-18 21:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.06, price: 3042.02, ref_id: 39
2025-03-18, BUY EXECUTED @ 3034.81, Size: 0.06
2025-03-18 21:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.06, executed_price: 3034.81, ref_id: 37
2025-03-18, SELL EXECUTED @ 3031.24, Size: -0.06
2025-03-18 21:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.06, executed_price: 3031.24, ref_id: 38
2025-03-18, Order Failed: Canceled
2025-03-18 21:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.06, price: 3042.02, ref_id: 39
2025-03-18, TRADE PROFIT: $-21.42 [Regime: TRENDING]
2025-03-19, TREND: Pullback complete, EMA8=3031.71 | ADX=31.8
2025-03-19,   SHORT: Entry=3029.88, SL=3033.72, TP=3022.20, Size=0.05
---- [WARNING 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3033.718695321262 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3033.718695321262 to 3033.71.
---- [WARNING 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3022.202609357476 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3022.202609357476 to 3022.2.
2025-03-19 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.05, price: 3029.88, ref_id: 40
2025-03-19 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3033.71, ref_id: 41
2025-03-19 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3022.2, ref_id: 42
2025-03-19 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.05, price: 3029.88, ref_id: 40
2025-03-19 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3033.71, ref_id: 41
2025-03-19 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3022.2, ref_id: 42
2025-03-19, SELL EXECUTED @ 3029.90, Size: -0.05
2025-03-19 22:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.05, executed_price: 3029.9, ref_id: 40
2025-03-19, BUY EXECUTED @ 3033.71, Size: 0.05
2025-03-20 00:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.05, executed_price: 3033.71, ref_id: 41
2025-03-19, Order Failed: Canceled
2025-03-20 00:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.05, price: 3022.2, ref_id: 42
2025-03-19, TRADE PROFIT: $-19.05 [Regime: TRENDING]
2025-03-21, TREND: Pullback complete, EMA8=3013.23 | ADX=30.3
2025-03-21,   SHORT: Entry=3010.90, SL=3016.31, TP=3000.08, Size=0.04
---- [WARNING 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3016.310588758445 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3016.310588758445 to 3016.31.
---- [WARNING 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3000.07882248311 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3000.07882248311 to 3000.07.
2025-03-21 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.04, price: 3010.9, ref_id: 43
2025-03-21 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.04, price: 3016.31, ref_id: 44
2025-03-21 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.04, price: 3000.07, ref_id: 45
2025-03-21 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.04, price: 3010.9, ref_id: 43
2025-03-21 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.04, price: 3016.31, ref_id: 44
2025-03-21 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.04, price: 3000.07, ref_id: 45
2025-03-21, SELL EXECUTED @ 3010.91, Size: -0.04
2025-03-21 23:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.04, executed_price: 3010.91, ref_id: 43
2025-03-21, BUY EXECUTED @ 3016.31, Size: 0.04
2025-03-22 00:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.04, executed_price: 3016.31, ref_id: 44
2025-03-21, Order Failed: Canceled
2025-03-22 00:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.04, price: 3000.07, ref_id: 45
2025-03-21, TRADE PROFIT: $-21.60 [Regime: TRENDING]
2025-03-24, TREND: Pullback complete, EMA8=3012.26 | ADX=35.3
2025-03-24,   SHORT: Entry=3007.90, SL=3012.64, TP=2998.43, Size=0.04
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3012.636683212698 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3012.636683212698 to 3012.63.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2998.4266335746042 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2998.4266335746042 to 2998.42.
2025-03-24 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.04, price: 3007.9, ref_id: 46
2025-03-24 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.04, price: 3012.63, ref_id: 47
2025-03-24 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2998.42, ref_id: 48
2025-03-24 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.04, price: 3007.9, ref_id: 46
2025-03-24 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.04, price: 3012.63, ref_id: 47
2025-03-24 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.04, price: 2998.42, ref_id: 48
2025-03-24, SELL EXECUTED @ 3007.72, Size: -0.04
2025-03-24 23:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.04, executed_price: 3007.72, ref_id: 46
2025-03-24, BUY EXECUTED @ 3012.63, Size: 0.04
2025-03-24 23:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.04, executed_price: 3012.63, ref_id: 47
2025-03-24, Order Failed: Canceled
2025-03-24 23:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.04, price: 2998.42, ref_id: 48
2025-03-24, TRADE PROFIT: $-19.64 [Regime: TRENDING]
2025-03-24, TREND: Pullback complete, EMA8=3011.09 | ADX=34.7
2025-03-24,   SHORT: Entry=3009.76, SL=3014.40, TP=3000.47, Size=0.04
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3014.402561330644 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3014.402561330644 to 3014.4.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3000.4748773387123 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3000.4748773387123 to 3000.47.
2025-03-24 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.04, price: 3009.76, ref_id: 49
2025-03-24 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.04, price: 3014.4, ref_id: 50
2025-03-24 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.04, price: 3000.47, ref_id: 51
2025-03-24 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.04, price: 3009.76, ref_id: 49
2025-03-24 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.04, price: 3014.4, ref_id: 50
2025-03-24 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.04, price: 3000.47, ref_id: 51
2025-03-24, SELL EXECUTED @ 3009.77, Size: -0.04
2025-03-24 23:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.04, executed_price: 3009.77, ref_id: 49
2025-03-24, BUY EXECUTED @ 3014.40, Size: 0.04
2025-03-24 23:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.04, executed_price: 3014.4, ref_id: 50
2025-03-24, Order Failed: Canceled
2025-03-24 23:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.04, price: 3000.47, ref_id: 51
2025-03-24, TRADE PROFIT: $-18.52 [Regime: TRENDING]
2025-03-24, TREND: Pullback complete, EMA8=3013.15 | ADX=26.1
2025-03-24,   SHORT: Entry=3011.43, SL=3015.21, TP=3003.86, Size=0.05
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3015.2140601116566 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3015.2140601116566 to 3015.21.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3003.8618797766862 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3003.8618797766862 to 3003.86.
2025-03-25 00:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.05, price: 3011.43, ref_id: 52
2025-03-25 00:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3015.21, ref_id: 53
2025-03-25 00:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3003.86, ref_id: 54
2025-03-25 00:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.05, price: 3011.43, ref_id: 52
2025-03-25 00:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3015.21, ref_id: 53
2025-03-25 00:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3003.86, ref_id: 54
2025-03-24, SELL EXECUTED @ 3011.42, Size: -0.05
2025-03-25 00:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.05, executed_price: 3011.42, ref_id: 52
2025-03-24, BUY EXECUTED @ 3003.86, Size: 0.05
2025-03-25 02:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.05, executed_price: 3003.86, ref_id: 54
2025-03-24, Order Failed: Canceled
2025-03-25 02:10:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.05, price: 3015.21, ref_id: 53
2025-03-24, TRADE PROFIT: $37.80 [Regime: TRENDING]
2025-03-25, TREND: Pullback complete, EMA8=3028.32 | ADX=26.9
2025-03-25,   LONG: Entry=3033.69, SL=3029.69, TP=3041.70, Size=0.05
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3029.686362395709 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3029.686362395709 to 3029.68.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3041.697275208582 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3041.697275208582 to 3041.69.
2025-03-25 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.05, price: 3033.69, ref_id: 55
2025-03-25 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.05, price: 3029.68, ref_id: 56
2025-03-25 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.05, price: 3041.69, ref_id: 57
2025-03-25 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.05, price: 3033.69, ref_id: 55
2025-03-25 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.05, price: 3029.68, ref_id: 56
2025-03-25 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.05, price: 3041.69, ref_id: 57
2025-03-25, BUY EXECUTED @ 3033.74, Size: 0.05
2025-03-25 22:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.05, executed_price: 3033.74, ref_id: 55
2025-03-25, SELL EXECUTED @ 3029.68, Size: -0.05
2025-03-25 22:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.05, executed_price: 3029.68, ref_id: 56
2025-03-25, Order Failed: Canceled
2025-03-25 22:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.05, price: 3041.69, ref_id: 57
2025-03-25, TRADE PROFIT: $-20.30 [Regime: TRENDING]
2025-03-25, TREND: Pullback complete, EMA8=3022.90 | ADX=29.2
2025-03-25,   SHORT: Entry=3022.22, SL=3025.78, TP=3015.09, Size=0.05
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3025.783070425886 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3025.783070425886 to 3025.78.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3015.093859148228 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3015.093859148228 to 3015.09.
2025-03-26 00:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.05, price: 3022.22, ref_id: 58
2025-03-26 00:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3025.78, ref_id: 59
2025-03-26 00:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3015.09, ref_id: 60
2025-03-26 00:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.05, price: 3022.22, ref_id: 58
2025-03-26 00:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3025.78, ref_id: 59
2025-03-26 00:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3015.09, ref_id: 60
2025-03-25, SELL EXECUTED @ 3022.24, Size: -0.05
2025-03-26 00:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.05, executed_price: 3022.24, ref_id: 58
2025-03-26, BUY EXECUTED @ 3025.78, Size: 0.05
2025-03-26 10:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.05, executed_price: 3025.78, ref_id: 59
2025-03-26, Order Failed: Canceled
2025-03-26 10:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.05, price: 3015.09, ref_id: 60
2025-03-26, TRADE PROFIT: $-17.70 [Regime: TRENDING]
2025-03-26, TREND: Pullback complete, EMA8=3019.31 | ADX=31.6
2025-03-26,   SHORT: Entry=3018.16, SL=3022.06, TP=3010.36, Size=0.05
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3022.0585611516944 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3022.0585611516944 to 3022.05.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3010.362877696611 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3010.362877696611 to 3010.36.
2025-03-26 22:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.05, price: 3018.16, ref_id: 61
2025-03-26 22:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3022.05, ref_id: 62
2025-03-26 22:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3010.36, ref_id: 63
2025-03-26 22:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.05, price: 3018.16, ref_id: 61
2025-03-26 22:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.05, price: 3022.05, ref_id: 62
2025-03-26 22:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.05, price: 3010.36, ref_id: 63
2025-03-26, SELL EXECUTED @ 3018.15, Size: -0.05
2025-03-26 22:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.05, executed_price: 3018.15, ref_id: 61
2025-03-27, BUY EXECUTED @ 3022.05, Size: 0.05
2025-03-27 08:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.05, executed_price: 3022.05, ref_id: 62
2025-03-27, Order Failed: Canceled
2025-03-27 08:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.05, price: 3010.36, ref_id: 63
2025-03-27, TRADE PROFIT: $-19.50 [Regime: TRENDING]
2025-03-27, TREND: Pullback complete, EMA8=3055.06 | ADX=31.7
2025-03-27,   LONG: Entry=3056.31, SL=3050.92, TP=3067.10, Size=0.03
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3050.9153445418956 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3050.9153445418956 to 3050.91.
---- [WARNING 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 3067.0993109162087 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 16:13:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 3067.0993109162087 to 3067.09.
2025-03-27 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 3056.31, ref_id: 64
2025-03-27 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 3050.91, ref_id: 65
2025-03-27 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 3067.09, ref_id: 66
2025-03-27 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 3056.31, ref_id: 64
2025-03-27 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 3050.91, ref_id: 65
2025-03-27 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 3067.09, ref_id: 66
2025-03-27, BUY EXECUTED @ 3056.37, Size: 0.03
2025-03-27 23:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 3056.37, ref_id: 64
2025-03-27, SELL EXECUTED @ 3050.91, Size: -0.03
2025-03-28 00:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 3050.91, ref_id: 65
2025-03-27, Order Failed: Canceled
2025-03-28 00:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 3067.09, ref_id: 66
2025-03-27, TRADE PROFIT: $-16.38 [Regime: TRENDING]

=== BACKTEST RESULTS ===
--------- Returns ---------
{
    "rtot": -0.0006935000000000202,
    "ravg": -1.3070014955045845e-05,
    "rnorm": -0.013872946890240568,
    "rnorm100": 38.729468902405685,
    "rtot_new": 0.930649999999998,
    "rnorm_new": -0.38729468902405684
}
===========================
---- [INFO 2025-12-15 16:13:15 +0800 strategy_utils.extract_suggest_improvements_and_plot_run_results:348]: ==== Full analyzers output: =========
"{'returns': OrderedDict({'rtot': -0.0006935000000000202, 'ravg': -1.3070014955045845e-05, 'rnorm': -0.013872946890240568, 'rnorm100': 38.729468902405685, 'rtot_new': 0.930649999999998, 'rnorm_new': -0.38729468902405684}), 'drawdown': AutoOrderedDict({'len': 2827, 'drawdown': 10.116949858074555, 'moneydown': 209.50200000000518, 'max': AutoOrderedDict({'len': 2827, 'drawdown': 10.116949858074555, 'moneydown': 209.50200000000518})}), 'vwr': OrderedDict({'vwr': -0.0007789972825036941}), 'tradeanalyzer': AutoOrderedDict({'total': AutoOrderedDict({'total': 22, 'open': 0, 'closed': 22}), 'streak': AutoOrderedDict({'won': AutoOrderedDict({'current': 0, 'longest': 2}), 'lost': AutoOrderedDict({'current': 4, 'longest': 8})}), 'pnl': AutoOrderedDict({'gross': AutoOrderedDict({'total': -138.700000000005, 'average': -6.304545454545681}), 'net': AutoOrderedDict({'total': -138.700000000005, 'average': -6.304545454545681})}), 'won': AutoOrderedDict({'total': 5, 'pnl': AutoOrderedDict({'total': 190.359"
========== Backtest finished after 0:00:07.676746!
