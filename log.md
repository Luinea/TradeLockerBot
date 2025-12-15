========== Starting to setup a Backtest:
Using configuration: symbolName='XAUUSD.PRO' symbolId=781 resolution='5m' commission=0.0 startDate=datetime.datetime(2024, 4, 1, 0, 0, tzinfo=TzInfo(UTC)) endDate=datetime.datetime(2024, 6, 30, 0, 0, tzinfo=TzInfo(UTC)) leverage=100.0 margin=2000.0 strategyParamsInput={'adx_period': 14, 'adx_trend_enter': 30, 'adx_trend_exit': 20, 'adx_min_threshold': 12, 'atr_min_pips': 3, 'require_rising_adx': True, 'bb_period': 20, 'bb_dev': 2, 'ema_fast': 8, 'ema_medium': 21, 'ema_slow': 50, 'rsi_period': 14, 'rsi_oversold': 35, 'rsi_overbought': 65, 'stoch_k': 5, 'stoch_d': 3, 'stoch_slow': 3, 'stoch_oversold': 25, 'stoch_overbought': 75, 'asian_start_hour': 1, 'asian_end_hour': 8, 'trade_start_hour': 8, 'trade_end_hour': 17, 'breakout_buffer': 0.5, 'use_ha_filter': True, 'atr_period': 14, 'atr_sl_multiplier': 2, 'tp_risk_reward': 1.5, 'max_hold_minutes': 60, 'risk_per_trade_percent': 0.01, 'max_daily_trades': 3, 'max_daily_loss': 75, 'max_drawdown_percent': 0.06, 'max_lots': 0.5, 'contract_size': 100, 'cooldown_minutes': 30, 'ema_macro': 200, 'trade_with_trend_only': True, 'use_mean_reversion': False}
---- [INFO 2025-12-15 23:58:11 +0800 strategy_utils.add_sizer_to_cerebro:297]: Using default sizer 'TLLotSizer'
========== Setup finished. Backtest is running...
---, XAU Hybrid Adaptive Strategy Started
2024-04-02, ASIAN RANGE: High=2259.82, Low=2246.66, Size=13.16
2024-04-02, REGIME CHANGE: RANGING -> TRENDING (ADX=31.0 > 30)
2024-04-02, REGIME CHANGE: TRENDING -> RANGING (ADX=18.9 < 20)
2024-04-02, REDUCED SIZE: ADX=23.1 < 20, sizing halved to 0.01
2024-04-02, ASIAN BREAKOUT UP: Price=2272.86 > Range High=2259.82 | ADX=23.1 | Regime=RANGING
2024-04-02,   LONG: Entry=2272.86, SL=2265.91, TP=2283.29, Size=0.01
---- [WARNING 2025-12-15 23:58:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2265.9080454967807 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2265.9080454967807 to 2265.9.
---- [WARNING 2025-12-15 23:58:11 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2283.2879317548295 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:11 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2283.2879317548295 to 2283.28.
2024-04-02 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2272.86, ref_id: 1
2024-04-02 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2265.9, ref_id: 2
2024-04-02 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2283.28, ref_id: 3
2024-04-02 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2272.86, ref_id: 1
2024-04-02 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2265.9, ref_id: 2
2024-04-02 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2283.28, ref_id: 3
2024-04-02, BUY EXECUTED @ 2273.01, Size: 0.01
2024-04-02 22:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2273.01, ref_id: 1
2024-04-02, SELL EXECUTED @ 2265.90, Size: -0.01
2024-04-02 22:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2265.9, ref_id: 2
2024-04-02, Order Failed: Canceled
2024-04-02 22:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2283.28, ref_id: 3
2024-04-02, TRADE PROFIT: $-7.11 [Regime: RANGING]
2024-04-03, ASIAN RANGE: High=2287.94, Low=2270.50, Size=17.44
2024-04-03, REGIME CHANGE: RANGING -> TRENDING (ADX=46.0 > 30)
2024-04-03, REGIME CHANGE: TRENDING -> RANGING (ADX=19.1 < 20)
2024-04-03, REGIME CHANGE: RANGING -> TRENDING (ADX=30.3 > 30)
2024-04-03, TREND PULLBACK: Price > EMA8=2286.11 | ADX=27.6 | Regime=TRENDING
2024-04-03,   LONG: Entry=2290.35, SL=2284.03, TP=2299.82, Size=0.03
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2284.033663283098 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2284.033663283098 to 2284.03.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2299.824505075352 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2299.824505075352 to 2299.82.
2024-04-04 00:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2290.35, ref_id: 4
2024-04-04 00:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2284.03, ref_id: 5
2024-04-04 00:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2299.82, ref_id: 6
2024-04-04 00:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2290.35, ref_id: 4
2024-04-04 00:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2284.03, ref_id: 5
2024-04-04 00:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2299.82, ref_id: 6
2024-04-03, BUY EXECUTED @ 2290.36, Size: 0.03
2024-04-04 00:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2290.36, ref_id: 4
2024-04-03, TIME EXIT: Position held > 60 mins - closing at market
2024-04-03, Order Failed: Canceled
2024-04-04 01:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.03, price: 2284.03, ref_id: 5
2024-04-03, Order Failed: Canceled
2024-04-04 01:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2299.82, ref_id: 6
2024-04-04 01:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2292.1, ref_id: 7
2024-04-04 01:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2292.1, ref_id: 7
2024-04-03, SELL EXECUTED @ 2292.14, Size: -0.03
2024-04-04 01:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2292.14, ref_id: 7
2024-04-03, TRADE PROFIT: $5.34 [Regime: TRENDING]
2024-04-04, ASIAN RANGE: High=2304.45, Low=2291.87, Size=12.58
2024-04-04, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)
2024-04-04, REGIME CHANGE: RANGING -> TRENDING (ADX=30.2 > 30)
2024-04-04, REGIME CHANGE: TRENDING -> RANGING (ADX=19.3 < 20)
2024-04-05, ASIAN RANGE: High=2290.56, Low=2267.72, Size=22.84
2024-04-05, REGIME CHANGE: RANGING -> TRENDING (ADX=31.6 > 30)
2024-04-05, REGIME CHANGE: TRENDING -> RANGING (ADX=19.1 < 20)
2024-04-05, REDUCED SIZE: ADX=21.4 < 20, sizing halved to 0.01
2024-04-05, ASIAN BREAKOUT UP: Price=2298.40 > Range High=2290.56 | ADX=21.4 | Regime=RANGING
2024-04-05,   LONG: Entry=2298.40, SL=2290.22, TP=2310.67, Size=0.01
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2290.21869916906 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2290.21869916906 to 2290.21.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2310.6719512464106 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2310.6719512464106 to 2310.67.
2024-04-05 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2298.4, ref_id: 8
2024-04-05 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2290.21, ref_id: 9
2024-04-05 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2310.67, ref_id: 10
2024-04-05 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2298.4, ref_id: 8
2024-04-05 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2290.21, ref_id: 9
2024-04-05 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2310.67, ref_id: 10
2024-04-05, BUY EXECUTED @ 2298.44, Size: 0.01
2024-04-05 21:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2298.44, ref_id: 8
2024-04-05, TIME EXIT: Position held > 60 mins - closing at market
2024-04-05, Order Failed: Canceled
2024-04-05 22:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2290.21, ref_id: 9
2024-04-05, Order Failed: Canceled
2024-04-05 22:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2310.67, ref_id: 10
2024-04-05 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2301.51, ref_id: 11
2024-04-05 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2301.51, ref_id: 11
2024-04-05, SELL EXECUTED @ 2301.54, Size: -0.01
2024-04-05 22:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2301.54, ref_id: 11
2024-04-05, TRADE PROFIT: $3.10 [Regime: RANGING]
2024-04-05, REGIME CHANGE: RANGING -> TRENDING (ADX=38.3 > 30)
2024-04-05, TREND PULLBACK: Price > EMA8=2317.89 | ADX=38.8 | Regime=TRENDING
2024-04-05,   LONG: Entry=2322.27, SL=2312.34, TP=2337.16, Size=0.02
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2312.3421833677794 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2312.3421833677794 to 2312.34.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2337.161724948331 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2337.161724948331 to 2337.16.
2024-04-05 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2322.27, ref_id: 12
2024-04-05 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2312.34, ref_id: 13
2024-04-05 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2337.16, ref_id: 14
2024-04-05 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2322.27, ref_id: 12
2024-04-05 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2312.34, ref_id: 13
2024-04-05 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2337.16, ref_id: 14
2024-04-05, BUY EXECUTED @ 2322.20, Size: 0.02
2024-04-05 23:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2322.2, ref_id: 12
2024-04-05, TIME EXIT: Position held > 60 mins - closing at market
2024-04-05, Order Failed: Canceled
2024-04-06 00:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.02, price: 2312.34, ref_id: 13
2024-04-05, Order Failed: Canceled
2024-04-06 00:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2337.16, ref_id: 14
2024-04-06 00:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2328.56, ref_id: 15
2024-04-06 00:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2328.56, ref_id: 15
2024-04-05, SELL EXECUTED @ 2328.55, Size: -0.02
2024-04-06 00:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2328.55, ref_id: 15
2024-04-05, TRADE PROFIT: $12.70 [Regime: TRENDING]
2024-04-05, TREND PULLBACK: Price > EMA8=2325.53 | ADX=33.0 | Regime=TRENDING
2024-04-05,   LONG: Entry=2326.71, SL=2320.39, TP=2336.20, Size=0.03
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2320.385790132111 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2320.385790132111 to 2320.38.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2336.1963148018335 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2336.1963148018335 to 2336.19.
2024-04-06 00:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2326.71, ref_id: 16
2024-04-06 00:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2320.38, ref_id: 17
2024-04-06 00:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2336.19, ref_id: 18
2024-04-06 00:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2326.71, ref_id: 16
2024-04-06 00:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2320.38, ref_id: 17
2024-04-06 00:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2336.19, ref_id: 18
2024-04-05, BUY EXECUTED @ 2326.81, Size: 0.03
2024-04-06 00:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2326.81, ref_id: 16
2024-04-07, SELL EXECUTED @ 2320.38, Size: -0.03
2024-04-08 06:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2320.38, ref_id: 17
2024-04-07, Order Failed: Canceled
2024-04-08 06:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2336.19, ref_id: 18
2024-04-07, TRADE PROFIT: $-19.29 [Regime: TRENDING]
2024-04-08, ASIAN RANGE: High=2354.05, Low=2302.90, Size=51.15
2024-04-08, REGIME CHANGE: TRENDING -> RANGING (ADX=13.2 < 20)
2024-04-08, REGIME CHANGE: RANGING -> TRENDING (ADX=30.7 > 30)
2024-04-08, TREND PULLBACK: Price < EMA8=2329.91 | ADX=28.8 | Regime=TRENDING
2024-04-08,   SHORT: Entry=2327.41, SL=2334.64, TP=2316.56, Size=0.03
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2334.6430768839623 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2334.6430768839623 to 2334.64.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2316.5603846740564 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2316.5603846740564 to 2316.56.
2024-04-08 21:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2327.41, ref_id: 19
2024-04-08 21:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2334.64, ref_id: 20
2024-04-08 21:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2316.56, ref_id: 21
2024-04-08 21:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2327.41, ref_id: 19
2024-04-08 21:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2334.64, ref_id: 20
2024-04-08 21:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2316.56, ref_id: 21
2024-04-08, SELL EXECUTED @ 2327.43, Size: -0.03
2024-04-08 21:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2327.43, ref_id: 19
2024-04-08, BUY EXECUTED @ 2334.64, Size: 0.03
2024-04-08 21:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.03, executed_price: 2334.64, ref_id: 20
2024-04-08, Order Failed: Canceled
2024-04-08 21:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2316.56, ref_id: 21
2024-04-08, TRADE PROFIT: $-21.63 [Regime: TRENDING]
2024-04-08, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-04-09, ASIAN RANGE: High=2356.96, Low=2337.78, Size=19.18
2024-04-09, REGIME CHANGE: RANGING -> TRENDING (ADX=39.5 > 30)
2024-04-09, TREND PULLBACK: Price > EMA8=2355.56 | ADX=27.1 | Regime=TRENDING
2024-04-09,   LONG: Entry=2358.01, SL=2351.38, TP=2367.96, Size=0.03
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2351.3768039783995 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2351.3768039783995 to 2351.37.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2367.959794032401 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2367.959794032401 to 2367.95.
2024-04-09 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2358.01, ref_id: 22
2024-04-09 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2351.37, ref_id: 23
2024-04-09 22:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2367.95, ref_id: 24
2024-04-09 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2358.01, ref_id: 22
2024-04-09 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2351.37, ref_id: 23
2024-04-09 22:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2367.95, ref_id: 24
2024-04-09, BUY EXECUTED @ 2357.98, Size: 0.03
2024-04-09 22:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2357.98, ref_id: 22
2024-04-09, SELL EXECUTED @ 2351.37, Size: -0.03
2024-04-09 22:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2351.37, ref_id: 23
2024-04-09, Order Failed: Canceled
2024-04-09 22:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2367.95, ref_id: 24
2024-04-09, TRADE PROFIT: $-19.83 [Regime: TRENDING]
2024-04-09, BLOCKED: SHORT but price 2349.27 > EMA200 2349.22
2024-04-09, TREND PULLBACK: Price < EMA8=2348.22 | ADX=25.9 | Regime=TRENDING
2024-04-09,   SHORT: Entry=2345.75, SL=2354.28, TP=2332.96, Size=0.02
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2354.278194982319 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2354.278194982319 to 2354.27.
---- [WARNING 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2332.957707526522 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:12 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2332.957707526522 to 2332.95.
2024-04-09 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2345.75, ref_id: 25
2024-04-09 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2354.27, ref_id: 26
2024-04-09 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2332.95, ref_id: 27
2024-04-09 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2345.75, ref_id: 25
2024-04-09 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2354.27, ref_id: 26
2024-04-09 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2332.95, ref_id: 27
2024-04-09, SELL EXECUTED @ 2345.73, Size: -0.02
2024-04-09 23:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2345.73, ref_id: 25
2024-04-09, TIME EXIT: Position held > 60 mins - closing at market
2024-04-09, Order Failed: Canceled
2024-04-10 00:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2354.27, ref_id: 26
2024-04-09, Order Failed: Canceled
2024-04-10 00:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2332.95, ref_id: 27
2024-04-10 00:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2346.7, ref_id: 28
2024-04-10 00:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2346.7, ref_id: 28
2024-04-09, BUY EXECUTED @ 2346.80, Size: 0.02
2024-04-10 00:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2346.8, ref_id: 28
2024-04-09, TRADE PROFIT: $-2.14 [Regime: TRENDING]
2024-04-10, ASIAN RANGE: High=2360.05, Low=2344.75, Size=15.30
2024-04-10, REGIME CHANGE: TRENDING -> RANGING (ADX=18.4 < 20)
2024-04-10, REGIME CHANGE: RANGING -> TRENDING (ADX=30.5 > 30)
2024-04-10, REGIME CHANGE: TRENDING -> RANGING (ADX=19.7 < 20)
2024-04-10, REDUCED SIZE: ADX=21.8 < 20, sizing halved to 0.01
2024-04-10, ASIAN BREAKOUT DOWN: Price=2329.72 < Range Low=2344.75 | ADX=21.8 | Regime=RANGING
2024-04-10,   SHORT: Entry=2329.72, SL=2335.93, TP=2320.41, Size=0.01
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2335.927207597889 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2335.927207597889 to 2335.92.
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2320.409188603166 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2320.409188603166 to 2320.4.
2024-04-10 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2329.72, ref_id: 29
2024-04-10 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2335.92, ref_id: 30
2024-04-10 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2320.4, ref_id: 31
2024-04-10 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2329.72, ref_id: 29
2024-04-10 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2335.92, ref_id: 30
2024-04-10 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2320.4, ref_id: 31
2024-04-10, SELL EXECUTED @ 2329.76, Size: -0.01
2024-04-10 20:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2329.76, ref_id: 29
2024-04-10, BUY EXECUTED @ 2338.51, Size: 0.01
2024-04-10 20:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.01, executed_price: 2338.51, ref_id: 30
2024-04-10, Order Failed: Canceled
2024-04-10 20:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2320.4, ref_id: 31
2024-04-10, TRADE PROFIT: $-8.75 [Regime: RANGING]
2024-04-10, REGIME CHANGE: RANGING -> TRENDING (ADX=33.5 > 30)
2024-04-10, TREND PULLBACK: Price < EMA8=2341.13 | ADX=25.1 | Regime=TRENDING
2024-04-10,   SHORT: Entry=2332.03, SL=2342.81, TP=2315.86, Size=0.02
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2342.810288618982 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2342.810288618982 to 2342.81.
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2315.859567071527 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2315.859567071527 to 2315.85.
2024-04-10 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2332.03, ref_id: 32
2024-04-10 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2342.81, ref_id: 33
2024-04-10 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2315.85, ref_id: 34
2024-04-10 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2332.03, ref_id: 32
2024-04-10 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2342.81, ref_id: 33
2024-04-10 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2315.85, ref_id: 34
2024-04-10, SELL EXECUTED @ 2332.15, Size: -0.02
2024-04-10 23:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2332.15, ref_id: 32
2024-04-10, TIME EXIT: Position held > 60 mins - closing at market
2024-04-10, Order Failed: Canceled
2024-04-11 00:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2342.81, ref_id: 33
2024-04-10, Order Failed: Canceled
2024-04-11 00:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2315.85, ref_id: 34
2024-04-11 00:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2338.21, ref_id: 35
2024-04-11 00:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2338.21, ref_id: 35
2024-04-10, BUY EXECUTED @ 2338.22, Size: 0.02
2024-04-11 00:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2338.22, ref_id: 35
2024-04-10, TRADE PROFIT: $-12.14 [Regime: TRENDING]
2024-04-10, REGIME CHANGE: TRENDING -> RANGING (ADX=13.6 < 20)
2024-04-11, ASIAN RANGE: High=2346.86, Low=2333.86, Size=13.00
2024-04-11, REGIME CHANGE: RANGING -> TRENDING (ADX=30.1 > 30)
2024-04-11, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-04-11, REDUCED SIZE: ADX=22.6 < 20, sizing halved to 0.01
2024-04-11, ASIAN BREAKOUT DOWN: Price=2333.16 < Range Low=2333.86 | ADX=22.6 | Regime=RANGING
2024-04-11,   SHORT: Entry=2333.16, SL=2340.71, TP=2321.83, Size=0.01
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2340.7136971791197 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2340.7136971791197 to 2340.71.
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2321.82945423132 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2321.82945423132 to 2321.82.
2024-04-11 22:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2333.16, ref_id: 36
2024-04-11 22:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2340.71, ref_id: 37
2024-04-11 22:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2321.82, ref_id: 38
2024-04-11 22:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2333.16, ref_id: 36
2024-04-11 22:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2340.71, ref_id: 37
2024-04-11 22:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2321.82, ref_id: 38
2024-04-11, SELL EXECUTED @ 2333.33, Size: -0.01
2024-04-11 22:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2333.33, ref_id: 36
2024-04-11, BUY EXECUTED @ 2340.71, Size: 0.01
2024-04-11 23:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.01, executed_price: 2340.71, ref_id: 37
2024-04-11, Order Failed: Canceled
2024-04-11 23:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2321.82, ref_id: 38
2024-04-11, TRADE PROFIT: $-7.38 [Regime: RANGING]
2024-04-12, ASIAN RANGE: High=2398.85, Low=2376.64, Size=22.21
2024-04-12, REGIME CHANGE: RANGING -> TRENDING (ADX=34.3 > 30)
2024-04-12, REGIME CHANGE: TRENDING -> RANGING (ADX=18.9 < 20)
2024-04-12, REDUCED SIZE: ADX=16.4 < 20, sizing halved to 0.01
2024-04-12, ASIAN BREAKOUT UP: Price=2402.50 > Range High=2398.85 | ADX=16.4 | Regime=RANGING
2024-04-12,   LONG: Entry=2402.50, SL=2395.48, TP=2413.03, Size=0.01
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2395.4786198180796 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2395.4786198180796 to 2395.47.
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2413.032070272881 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2413.032070272881 to 2413.03.
2024-04-12 21:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2402.5, ref_id: 39
2024-04-12 21:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2395.47, ref_id: 40
2024-04-12 21:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2413.03, ref_id: 41
2024-04-12 21:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2402.5, ref_id: 39
2024-04-12 21:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2395.47, ref_id: 40
2024-04-12 21:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2413.03, ref_id: 41
2024-04-12, BUY EXECUTED @ 2402.55, Size: 0.01
2024-04-12 21:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2402.55, ref_id: 39
2024-04-12, SELL EXECUTED @ 2413.03, Size: -0.01
2024-04-12 22:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2413.03, ref_id: 41
2024-04-12, Order Failed: Canceled
2024-04-12 22:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2395.47, ref_id: 40
2024-04-12, TRADE PROFIT: $10.48 [Regime: RANGING]
2024-04-12, REGIME CHANGE: RANGING -> TRENDING (ADX=36.8 > 30)
2024-04-12, TREND PULLBACK: Price < EMA8=2395.39 | ADX=36.5 | Regime=TRENDING
2024-04-12,   SHORT: Entry=2389.42, SL=2402.99, TP=2369.07, Size=0.01
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2402.9868291015378 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2402.9868291015378 to 2402.98.
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2369.069756347694 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2369.069756347694 to 2369.06.
2024-04-13 00:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2389.42, ref_id: 42
2024-04-13 00:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2402.98, ref_id: 43
2024-04-13 00:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2369.06, ref_id: 44
2024-04-13 00:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2389.42, ref_id: 42
2024-04-13 00:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2402.98, ref_id: 43
2024-04-13 00:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2369.06, ref_id: 44
2024-04-12, SELL EXECUTED @ 2389.43, Size: -0.01
2024-04-13 00:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2389.43, ref_id: 42
2024-04-12, BUY EXECUTED @ 2369.06, Size: 0.01
2024-04-13 00:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.01, executed_price: 2369.06, ref_id: 44
2024-04-12, Order Failed: Canceled
2024-04-13 00:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2402.98, ref_id: 43
2024-04-12, TRADE PROFIT: $20.37 [Regime: TRENDING]
2024-04-15, ASIAN RANGE: High=2364.67, Low=2348.37, Size=16.30
2024-04-15, REGIME CHANGE: TRENDING -> RANGING (ADX=19.3 < 20)
2024-04-15, REGIME CHANGE: RANGING -> TRENDING (ADX=30.5 > 30)
2024-04-15, REGIME CHANGE: TRENDING -> RANGING (ADX=19.1 < 20)
2024-04-15, REDUCED SIZE: ADX=16.6 < 20, sizing halved to 0.01
2024-04-15, ASIAN BREAKOUT DOWN: Price=2345.31 < Range Low=2348.37 | ADX=16.6 | Regime=RANGING
2024-04-15,   SHORT: Entry=2345.31, SL=2351.97, TP=2335.32, Size=0.01
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2351.967574597086 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2351.967574597086 to 2351.96.
---- [WARNING 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2335.323638104371 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:13 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2335.323638104371 to 2335.32.
2024-04-15 21:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2345.31, ref_id: 45
2024-04-15 21:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2351.96, ref_id: 46
2024-04-15 21:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2335.32, ref_id: 47
2024-04-15 21:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2345.31, ref_id: 45
2024-04-15 21:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2351.96, ref_id: 46
2024-04-15 21:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2335.32, ref_id: 47
2024-04-15, SELL EXECUTED @ 2345.31, Size: -0.01
2024-04-15 21:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2345.31, ref_id: 45
2024-04-15, BUY EXECUTED @ 2335.32, Size: 0.01
2024-04-15 22:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.01, executed_price: 2335.32, ref_id: 47
2024-04-15, Order Failed: Canceled
2024-04-15 22:10:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2351.96, ref_id: 46
2024-04-15, TRADE PROFIT: $9.99 [Regime: RANGING]
2024-04-15, REGIME CHANGE: RANGING -> TRENDING (ADX=36.9 > 30)
2024-04-15, REGIME CHANGE: TRENDING -> RANGING (ADX=19.3 < 20)
2024-04-16, ASIAN RANGE: High=2389.28, Low=2364.52, Size=24.76
2024-04-16, REGIME CHANGE: RANGING -> TRENDING (ADX=45.0 > 30)
2024-04-16, REGIME CHANGE: TRENDING -> RANGING (ADX=20.0 < 20)
2024-04-16, REDUCED SIZE: ADX=21.3 < 20, sizing halved to 0.01
2024-04-16, ASIAN BREAKOUT UP: Price=2390.92 > Range High=2389.28 | ADX=21.3 | Regime=RANGING
2024-04-16,   LONG: Entry=2390.92, SL=2381.65, TP=2404.83, Size=0.01
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2381.6484279449655 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2381.6484279449655 to 2381.64.
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2404.8273580825517 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2404.8273580825517 to 2404.82.
2024-04-16 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2390.92, ref_id: 48
2024-04-16 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2381.64, ref_id: 49
2024-04-16 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2404.82, ref_id: 50
2024-04-16 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2390.92, ref_id: 48
2024-04-16 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2381.64, ref_id: 49
2024-04-16 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2404.82, ref_id: 50
2024-04-16, BUY EXECUTED @ 2391.12, Size: 0.01
2024-04-16 23:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2391.12, ref_id: 48
2024-04-16, SELL EXECUTED @ 2381.64, Size: -0.01
2024-04-16 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2381.64, ref_id: 49
2024-04-16, Order Failed: Canceled
2024-04-16 23:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2404.82, ref_id: 50
2024-04-16, TRADE PROFIT: $-9.48 [Regime: RANGING]
2024-04-17, ASIAN RANGE: High=2386.21, Low=2372.69, Size=13.52
2024-04-17, REGIME CHANGE: RANGING -> TRENDING (ADX=31.8 > 30)
2024-04-17, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-04-17, REDUCED SIZE: ADX=19.2 < 20, sizing halved to 0.01
2024-04-17, ASIAN BREAKOUT UP: Price=2387.21 > Range High=2386.21 | ADX=19.2 | Regime=RANGING
2024-04-17,   LONG: Entry=2387.21, SL=2380.37, TP=2397.47, Size=0.01
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2380.3713568521935 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2380.3713568521935 to 2380.37.
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2397.46796472171 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2397.46796472171 to 2397.46.
2024-04-17 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2387.21, ref_id: 51
2024-04-17 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2380.37, ref_id: 52
2024-04-17 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2397.46, ref_id: 53
2024-04-17 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2387.21, ref_id: 51
2024-04-17 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2380.37, ref_id: 52
2024-04-17 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2397.46, ref_id: 53
2024-04-17, BUY EXECUTED @ 2387.21, Size: 0.01
2024-04-17 23:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2387.21, ref_id: 51
2024-04-17, SELL EXECUTED @ 2380.37, Size: -0.01
2024-04-18 00:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2380.37, ref_id: 52
2024-04-17, Order Failed: Canceled
2024-04-18 00:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2397.46, ref_id: 53
2024-04-17, TRADE PROFIT: $-6.84 [Regime: RANGING]
2024-04-17, REGIME CHANGE: RANGING -> TRENDING (ADX=39.5 > 30)
2024-04-18, ASIAN RANGE: High=2380.93, Low=2364.05, Size=16.88
2024-04-18, REGIME CHANGE: TRENDING -> RANGING (ADX=19.1 < 20)
2024-04-19, ASIAN RANGE: High=2417.77, Low=2377.71, Size=40.06
2024-04-22, ASIAN RANGE: High=2384.23, Low=2351.53, Size=32.70
2024-04-22, REGIME CHANGE: RANGING -> TRENDING (ADX=40.7 > 30)
2024-04-22, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-04-22, REGIME CHANGE: RANGING -> TRENDING (ADX=32.7 > 30)
2024-04-22, TREND PULLBACK: Price < EMA8=2339.31 | ADX=40.7 | Regime=TRENDING
2024-04-22,   SHORT: Entry=2337.19, SL=2344.50, TP=2326.23, Size=0.03
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2344.498535575192 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2344.498535575192 to 2344.49.
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2326.2271966372127 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2326.2271966372127 to 2326.22.
2024-04-22 21:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2337.19, ref_id: 54
2024-04-22 21:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2344.49, ref_id: 55
2024-04-22 21:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2326.22, ref_id: 56
2024-04-22 21:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2337.19, ref_id: 54
2024-04-22 21:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2344.49, ref_id: 55
2024-04-22 21:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2326.22, ref_id: 56
2024-04-22, SELL EXECUTED @ 2337.27, Size: -0.03
2024-04-22 21:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2337.27, ref_id: 54
2024-04-22, TIME EXIT: Position held > 60 mins - closing at market
2024-04-22, Order Failed: Canceled
2024-04-22 22:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2344.49, ref_id: 55
2024-04-22, Order Failed: Canceled
2024-04-22 22:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2326.22, ref_id: 56
2024-04-22 22:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2340.39, ref_id: 57
2024-04-22 22:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2340.39, ref_id: 57
2024-04-22, BUY EXECUTED @ 2340.40, Size: 0.03
2024-04-22 22:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2340.4, ref_id: 57
2024-04-22, TRADE PROFIT: $-9.39 [Regime: TRENDING]
2024-04-22, TREND PULLBACK: Price < EMA8=2336.52 | ADX=20.3 | Regime=TRENDING
2024-04-22,   SHORT: Entry=2335.43, SL=2341.68, TP=2326.05, Size=0.03
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2341.683008413399 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2341.683008413399 to 2341.68.
---- [WARNING 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2326.0504873799014 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:14 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2326.0504873799014 to 2326.05.
2024-04-22 23:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2335.43, ref_id: 58
2024-04-22 23:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2341.68, ref_id: 59
2024-04-22 23:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2326.05, ref_id: 60
2024-04-22 23:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2335.43, ref_id: 58
2024-04-22 23:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2341.68, ref_id: 59
2024-04-22 23:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2326.05, ref_id: 60
2024-04-22, SELL EXECUTED @ 2335.43, Size: -0.03
2024-04-22 23:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2335.43, ref_id: 58
2024-04-22, TIME EXIT: Position held > 60 mins - closing at market
2024-04-22, Order Failed: Canceled
2024-04-23 00:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2341.68, ref_id: 59
2024-04-22, Order Failed: Canceled
2024-04-23 00:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2326.05, ref_id: 60
2024-04-23 00:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2330.98, ref_id: 61
2024-04-23 00:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2330.98, ref_id: 61
2024-04-22, BUY EXECUTED @ 2330.85, Size: 0.03
2024-04-23 00:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2330.85, ref_id: 61
2024-04-22, TRADE PROFIT: $13.74 [Regime: TRENDING]
2024-04-23, ASIAN RANGE: High=2334.40, Low=2295.58, Size=38.82
2024-04-23, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-04-23, REGIME CHANGE: RANGING -> TRENDING (ADX=31.6 > 30)
2024-04-23, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-04-23, REGIME CHANGE: RANGING -> TRENDING (ADX=31.1 > 30)
2024-04-23, TREND PULLBACK: Price > EMA8=2319.19 | ADX=23.6 | Regime=TRENDING
2024-04-23,   LONG: Entry=2319.52, SL=2311.35, TP=2331.78, Size=0.02
---- [WARNING 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2311.3459344489584 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2311.3459344489584 to 2311.34.
---- [WARNING 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2331.7810983265626 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2331.7810983265626 to 2331.78.
2024-04-23 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2319.52, ref_id: 62
2024-04-23 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2311.34, ref_id: 63
2024-04-23 23:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2331.78, ref_id: 64
2024-04-23 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2319.52, ref_id: 62
2024-04-23 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2311.34, ref_id: 63
2024-04-23 23:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2331.78, ref_id: 64
2024-04-23, BUY EXECUTED @ 2319.21, Size: 0.02
2024-04-23 23:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2319.21, ref_id: 62
2024-04-23, TIME EXIT: Position held > 60 mins - closing at market
2024-04-23, Order Failed: Canceled
2024-04-24 00:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.02, price: 2311.34, ref_id: 63
2024-04-23, Order Failed: Canceled
2024-04-24 00:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.02, price: 2331.78, ref_id: 64
2024-04-24 00:20:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2326.0, ref_id: 65
2024-04-24 00:20:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2326.0, ref_id: 65
2024-04-23, SELL EXECUTED @ 2325.90, Size: -0.02
2024-04-24 00:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2325.9, ref_id: 65
2024-04-23, TRADE PROFIT: $13.38 [Regime: TRENDING]
2024-04-24, ASIAN RANGE: High=2331.22, Low=2315.78, Size=15.44
2024-04-24, REGIME CHANGE: TRENDING -> RANGING (ADX=18.9 < 20)
2024-04-24, REDUCED SIZE: ADX=20.5 < 20, sizing halved to 0.01
2024-04-24, ASIAN BREAKOUT UP: Price=2336.21 > Range High=2331.22 | ADX=20.5 | Regime=RANGING
2024-04-24,   LONG: Entry=2336.21, SL=2329.96, TP=2345.59, Size=0.01
---- [WARNING 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2329.957872149446 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2329.957872149446 to 2329.95.
---- [WARNING 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2345.588191775831 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2345.588191775831 to 2345.58.
2024-04-24 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2336.21, ref_id: 66
2024-04-24 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2329.95, ref_id: 67
2024-04-24 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2345.58, ref_id: 68
2024-04-24 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2336.21, ref_id: 66
2024-04-24 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2329.95, ref_id: 67
2024-04-24 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2345.58, ref_id: 68
2024-04-24, BUY EXECUTED @ 2336.22, Size: 0.01
2024-04-24 23:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2336.22, ref_id: 66
2024-04-24, SELL EXECUTED @ 2329.95, Size: -0.01
2024-04-24 23:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2329.95, ref_id: 67
2024-04-24, Order Failed: Canceled
2024-04-24 23:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2345.58, ref_id: 68
2024-04-24, TRADE PROFIT: $-6.27 [Regime: RANGING]
2024-04-25, ASIAN RANGE: High=2326.11, Low=2305.12, Size=20.99
2024-04-25, REGIME CHANGE: RANGING -> TRENDING (ADX=32.3 > 30)
2024-04-25, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-04-25, REDUCED SIZE: ADX=19.5 < 20, sizing halved to 0.01
2024-04-25, ASIAN BREAKOUT UP: Price=2333.51 > Range High=2326.11 | ADX=19.5 | Regime=RANGING
2024-04-25,   LONG: Entry=2333.51, SL=2325.26, TP=2345.89, Size=0.01
---- [WARNING 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2325.2585133956227 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2325.2585133956227 to 2325.25.
---- [WARNING 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2345.8872299065665 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:15 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2345.8872299065665 to 2345.88.
2024-04-25 22:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2333.51, ref_id: 69
2024-04-25 22:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2325.25, ref_id: 70
2024-04-25 22:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2345.88, ref_id: 71
2024-04-25 22:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2333.51, ref_id: 69
2024-04-25 22:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2325.25, ref_id: 70
2024-04-25 22:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2345.88, ref_id: 71
2024-04-25, BUY EXECUTED @ 2333.40, Size: 0.01
2024-04-25 22:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2333.4, ref_id: 69
2024-04-25, TIME EXIT: Position held > 60 mins - closing at market
2024-04-25, Order Failed: Canceled
2024-04-25 23:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2325.25, ref_id: 70
2024-04-25, Order Failed: Canceled
2024-04-25 23:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2345.88, ref_id: 71
2024-04-25 23:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2331.43, ref_id: 72
2024-04-25 23:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2331.43, ref_id: 72
2024-04-25, SELL EXECUTED @ 2331.65, Size: -0.01
2024-04-25 23:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2331.65, ref_id: 72
2024-04-25, TRADE PROFIT: $-1.75 [Regime: RANGING]
2024-04-26, ASIAN RANGE: High=2346.89, Low=2326.30, Size=20.59
2024-04-26, REGIME CHANGE: RANGING -> TRENDING (ADX=46.8 > 30)
2024-04-26, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-04-29, ASIAN RANGE: High=2337.89, Low=2319.97, Size=17.92
2024-04-29, REGIME CHANGE: RANGING -> TRENDING (ADX=30.7 > 30)
2024-04-29, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)
2024-04-30, ASIAN RANGE: High=2336.13, Low=2315.36, Size=20.77
2024-04-30, REGIME CHANGE: RANGING -> TRENDING (ADX=54.7 > 30)
2024-04-30, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-04-30, REGIME CHANGE: RANGING -> TRENDING (ADX=31.0 > 30)
2024-04-30, TREND PULLBACK: Price < EMA8=2303.75 | ADX=27.0 | Regime=TRENDING
2024-04-30,   SHORT: Entry=2301.37, SL=2308.61, TP=2290.51, Size=0.03
---- [WARNING 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2308.612770047564 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2308.612770047564 to 2308.61.
---- [WARNING 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2290.505844928654 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2290.505844928654 to 2290.5.
2024-04-30 22:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2301.37, ref_id: 73
2024-04-30 22:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2308.61, ref_id: 74
2024-04-30 22:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2290.5, ref_id: 75
2024-04-30 22:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2301.37, ref_id: 73
2024-04-30 22:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2308.61, ref_id: 74
2024-04-30 22:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2290.5, ref_id: 75
2024-04-30, SELL EXECUTED @ 2301.46, Size: -0.03
2024-04-30 22:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2301.46, ref_id: 73
2024-04-30, TIME EXIT: Position held > 60 mins - closing at market
2024-04-30, Order Failed: Canceled
2024-04-30 23:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2308.61, ref_id: 74
2024-04-30, Order Failed: Canceled
2024-04-30 23:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2290.5, ref_id: 75
2024-04-30 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2299.05, ref_id: 76
2024-04-30 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2299.05, ref_id: 76
2024-04-30, BUY EXECUTED @ 2299.10, Size: 0.03
2024-04-30 23:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2299.1, ref_id: 76
2024-04-30, TRADE PROFIT: $7.08 [Regime: TRENDING]
2024-04-30, REGIME CHANGE: TRENDING -> RANGING (ADX=18.9 < 20)
2024-05-01, ASIAN RANGE: High=2289.71, Low=2281.56, Size=8.15
2024-05-01, REGIME CHANGE: RANGING -> TRENDING (ADX=30.5 > 30)
2024-05-01, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)
2024-05-02, ASIAN RANGE: High=2326.44, Low=2308.14, Size=18.30
2024-05-02, REGIME CHANGE: RANGING -> TRENDING (ADX=30.8 > 30)
2024-05-02, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-05-02, REDUCED SIZE: ADX=26.7 < 20, sizing halved to 0.01
2024-05-02, ASIAN BREAKOUT DOWN: Price=2288.88 < Range Low=2308.14 | ADX=26.7 | Regime=RANGING
2024-05-02,   SHORT: Entry=2288.88, SL=2295.40, TP=2279.11, Size=0.01
---- [WARNING 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2295.3957910948698 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2295.3957910948698 to 2295.39.
---- [WARNING 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2279.1063133576954 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2279.1063133576954 to 2279.1.
2024-05-02 21:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2288.88, ref_id: 77
2024-05-02 21:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2295.39, ref_id: 78
2024-05-02 21:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2279.1, ref_id: 79
2024-05-02 21:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2288.88, ref_id: 77
2024-05-02 21:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2295.39, ref_id: 78
2024-05-02 21:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2279.1, ref_id: 79
2024-05-02, SELL EXECUTED @ 2288.89, Size: -0.01
2024-05-02 21:55:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2288.89, ref_id: 77
2024-05-02, BUY EXECUTED @ 2295.39, Size: 0.01
2024-05-02 22:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.01, executed_price: 2295.39, ref_id: 78
2024-05-02, Order Failed: Canceled
2024-05-02 22:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2279.1, ref_id: 79
2024-05-02, TRADE PROFIT: $-6.50 [Regime: RANGING]
2024-05-03, ASIAN RANGE: High=2308.74, Low=2297.77, Size=10.97
2024-05-03, REDUCED SIZE: ADX=28.4 < 20, sizing halved to 0.01
2024-05-03, ASIAN BREAKOUT UP: Price=2315.42 > Range High=2308.74 | ADX=28.4 | Regime=RANGING
2024-05-03,   LONG: Entry=2315.42, SL=2308.67, TP=2325.54, Size=0.01
---- [WARNING 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2308.6746156144554 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2308.6746156144554 to 2308.67.
---- [WARNING 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2325.538076578317 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:16 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2325.538076578317 to 2325.53.
2024-05-03 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2315.42, ref_id: 80
2024-05-03 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2308.67, ref_id: 81
2024-05-03 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2325.53, ref_id: 82
2024-05-03 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2315.42, ref_id: 80
2024-05-03 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2308.67, ref_id: 81
2024-05-03 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2325.53, ref_id: 82
2024-05-03, BUY EXECUTED @ 2315.31, Size: 0.01
2024-05-03 20:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2315.31, ref_id: 80
2024-05-03, SELL EXECUTED @ 2308.67, Size: -0.01
2024-05-03 20:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.01, executed_price: 2308.67, ref_id: 81
2024-05-03, Order Failed: Canceled
2024-05-03 20:45:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2325.53, ref_id: 82
2024-05-03, TRADE PROFIT: $-6.64 [Regime: RANGING]
2024-05-06, ASIAN RANGE: High=2324.15, Low=2295.76, Size=28.39
2024-05-06, REGIME CHANGE: RANGING -> TRENDING (ADX=47.9 > 30)
2024-05-06, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-05-06, REGIME CHANGE: RANGING -> TRENDING (ADX=30.2 > 30)
2024-05-06, TREND PULLBACK: Price > EMA8=2326.68 | ADX=26.7 | Regime=TRENDING
2024-05-06,   LONG: Entry=2327.95, SL=2321.64, TP=2337.41, Size=0.03
---- [WARNING 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2321.6433727820922 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2321.6433727820922 to 2321.64.
---- [WARNING 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2337.409940826861 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2337.409940826861 to 2337.4.
2024-05-06 22:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2327.95, ref_id: 83
2024-05-06 22:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2321.64, ref_id: 84
2024-05-06 22:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2337.4, ref_id: 85
2024-05-06 22:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2327.95, ref_id: 83
2024-05-06 22:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2321.64, ref_id: 84
2024-05-06 22:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2337.4, ref_id: 85
2024-05-06, BUY EXECUTED @ 2327.94, Size: 0.03
2024-05-06 22:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2327.94, ref_id: 83
2024-05-06, SELL EXECUTED @ 2321.64, Size: -0.03
2024-05-06 22:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2321.64, ref_id: 84
2024-05-06, Order Failed: Canceled
2024-05-06 22:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2337.4, ref_id: 85
2024-05-06, TRADE PROFIT: $-18.90 [Regime: TRENDING]
2024-05-06, REGIME CHANGE: TRENDING -> RANGING (ADX=15.4 < 20)
2024-05-07, ASIAN RANGE: High=2329.94, Low=2317.71, Size=12.23
2024-05-07, REGIME CHANGE: RANGING -> TRENDING (ADX=30.2 > 30)
2024-05-07, REGIME CHANGE: TRENDING -> RANGING (ADX=19.7 < 20)
2024-05-08, ASIAN RANGE: High=2321.34, Low=2307.09, Size=14.25
2024-05-08, REGIME CHANGE: RANGING -> TRENDING (ADX=49.2 > 30)
2024-05-08, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-05-08, REGIME CHANGE: RANGING -> TRENDING (ADX=30.3 > 30)
2024-05-09, ASIAN RANGE: High=2319.72, Low=2307.52, Size=12.20
2024-05-09, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-05-09, REGIME CHANGE: RANGING -> TRENDING (ADX=30.1 > 30)
2024-05-09, TREND PULLBACK: Price > EMA8=2330.94 | ADX=33.3 | Regime=TRENDING
2024-05-09,   LONG: Entry=2332.47, SL=2325.31, TP=2343.22, Size=0.03
---- [WARNING 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2325.3060741304466 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2325.3060741304466 to 2325.3.
---- [WARNING 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2343.215888804329 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:17 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2343.215888804329 to 2343.21.
2024-05-09 23:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2332.47, ref_id: 86
2024-05-09 23:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2325.3, ref_id: 87
2024-05-09 23:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2343.21, ref_id: 88
2024-05-09 23:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2332.47, ref_id: 86
2024-05-09 23:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2325.3, ref_id: 87
2024-05-09 23:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2343.21, ref_id: 88
2024-05-09, BUY EXECUTED @ 2332.46, Size: 0.03
2024-05-09 23:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2332.46, ref_id: 86
2024-05-09, TIME EXIT: Position held > 60 mins - closing at market
2024-05-09, Order Failed: Canceled
2024-05-10 00:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.03, price: 2325.3, ref_id: 87
2024-05-09, Order Failed: Canceled
2024-05-10 00:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2343.21, ref_id: 88
2024-05-10 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2329.83, ref_id: 89
2024-05-10 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2329.83, ref_id: 89
2024-05-09, SELL EXECUTED @ 2329.85, Size: -0.03
2024-05-10 00:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2329.85, ref_id: 89
2024-05-09, TRADE PROFIT: $-7.83 [Regime: TRENDING]
2024-05-10, ASIAN RANGE: High=2370.31, Low=2347.15, Size=23.16
2024-05-10, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-05-13, ASIAN RANGE: High=2364.50, Low=2346.55, Size=17.95
2024-05-13, REGIME CHANGE: RANGING -> TRENDING (ADX=43.6 > 30)
2024-05-13, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)
2024-05-13, REDUCED SIZE: ADX=17.4 < 20, sizing halved to 0.01
2024-05-13, ASIAN BREAKOUT DOWN: Price=2337.27 < Range Low=2346.55 | ADX=17.4 | Regime=RANGING
2024-05-13,   SHORT: Entry=2337.27, SL=2343.36, TP=2328.14, Size=0.01
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2343.359051067521 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2343.359051067521 to 2343.35.
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2328.1364233987188 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2328.1364233987188 to 2328.13.
2024-05-13 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2337.27, ref_id: 90
2024-05-13 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2343.35, ref_id: 91
2024-05-13 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2328.13, ref_id: 92
2024-05-13 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2337.27, ref_id: 90
2024-05-13 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2343.35, ref_id: 91
2024-05-13 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2328.13, ref_id: 92
2024-05-13, SELL EXECUTED @ 2337.28, Size: -0.01
2024-05-13 23:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2337.28, ref_id: 90
2024-05-13, TIME EXIT: Position held > 60 mins - closing at market
2024-05-13, Order Failed: Canceled
2024-05-14 00:10:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2343.35, ref_id: 91
2024-05-13, Order Failed: Canceled
2024-05-14 00:10:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2328.13, ref_id: 92
2024-05-14 00:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2336.62, ref_id: 93
2024-05-14 00:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2336.62, ref_id: 93
2024-05-13, BUY EXECUTED @ 2336.59, Size: 0.01
2024-05-14 00:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2336.59, ref_id: 93
2024-05-13, TRADE PROFIT: $0.69 [Regime: RANGING]
2024-05-13, REGIME CHANGE: RANGING -> TRENDING (ADX=33.2 > 30)
2024-05-14, ASIAN RANGE: High=2345.98, Low=2335.93, Size=10.05
2024-05-14, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-05-14, REDUCED SIZE: ADX=12.1 < 20, sizing halved to 0.01
2024-05-14, ASIAN BREAKOUT UP: Price=2353.74 > Range High=2345.98 | ADX=12.1 | Regime=RANGING
2024-05-14,   LONG: Entry=2353.74, SL=2347.32, TP=2363.37, Size=0.01
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2347.318599596128 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2347.318599596128 to 2347.31.
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2363.372100605807 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2363.372100605807 to 2363.37.
2024-05-14 22:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2353.74, ref_id: 94
2024-05-14 22:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2347.31, ref_id: 95
2024-05-14 22:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2363.37, ref_id: 96
2024-05-14 22:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2353.74, ref_id: 94
2024-05-14 22:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2347.31, ref_id: 95
2024-05-14 22:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2363.37, ref_id: 96
2024-05-14, BUY EXECUTED @ 2353.75, Size: 0.01
2024-05-14 22:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2353.75, ref_id: 94
2024-05-14, TIME EXIT: Position held > 60 mins - closing at market
2024-05-14, Order Failed: Canceled
2024-05-14 23:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2347.31, ref_id: 95
2024-05-14, Order Failed: Canceled
2024-05-14 23:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2363.37, ref_id: 96
2024-05-14 23:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2351.38, ref_id: 97
2024-05-14 23:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2351.38, ref_id: 97
2024-05-14, SELL EXECUTED @ 2351.38, Size: -0.01
2024-05-14 23:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2351.38, ref_id: 97
2024-05-14, TRADE PROFIT: $-2.37 [Regime: RANGING]
2024-05-15, ASIAN RANGE: High=2364.73, Low=2354.88, Size=9.85
2024-05-15, REGIME CHANGE: RANGING -> TRENDING (ADX=30.5 > 30)
2024-05-15, TREND PULLBACK: Price > EMA8=2367.74 | ADX=39.0 | Regime=TRENDING
2024-05-15,   LONG: Entry=2375.82, SL=2368.71, TP=2386.49, Size=0.03
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2368.706713867765 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2368.706713867765 to 2368.7.
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2386.489929198353 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2386.489929198353 to 2386.48.
2024-05-15 20:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2375.82, ref_id: 98
2024-05-15 20:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2368.7, ref_id: 99
2024-05-15 20:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2386.48, ref_id: 100
2024-05-15 20:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2375.82, ref_id: 98
2024-05-15 20:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2368.7, ref_id: 99
2024-05-15 20:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2386.48, ref_id: 100
2024-05-15, BUY EXECUTED @ 2375.73, Size: 0.03
2024-05-15 20:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2375.73, ref_id: 98
2024-05-15, SELL EXECUTED @ 2368.70, Size: -0.03
2024-05-15 21:20:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2368.7, ref_id: 99
2024-05-15, Order Failed: Canceled
2024-05-15 21:20:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2386.48, ref_id: 100
2024-05-15, TRADE PROFIT: $-21.09 [Regime: TRENDING]
2024-05-15, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-05-15, REDUCED SIZE: ADX=18.3 < 20, sizing halved to 0.01
2024-05-15, ASIAN BREAKOUT UP: Price=2374.49 > Range High=2364.73 | ADX=18.3 | Regime=RANGING
2024-05-15,   LONG: Entry=2374.49, SL=2367.11, TP=2385.56, Size=0.01
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2367.1130054984683 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2367.1130054984683 to 2367.11.
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2385.5554917522973 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2385.5554917522973 to 2385.55.
2024-05-15 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2374.49, ref_id: 101
2024-05-15 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2367.11, ref_id: 102
2024-05-15 23:10:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2385.55, ref_id: 103
2024-05-15 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2374.49, ref_id: 101
2024-05-15 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2367.11, ref_id: 102
2024-05-15 23:10:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2385.55, ref_id: 103
2024-05-15, BUY EXECUTED @ 2374.47, Size: 0.01
2024-05-15 23:10:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2374.47, ref_id: 101
2024-05-15, SELL EXECUTED @ 2385.55, Size: -0.01
2024-05-15 23:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2385.55, ref_id: 103
2024-05-15, Order Failed: Canceled
2024-05-15 23:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2367.11, ref_id: 102
2024-05-15, TRADE PROFIT: $11.08 [Regime: RANGING]
2024-05-16, ASIAN RANGE: High=2397.26, Low=2384.75, Size=12.51
2024-05-16, REGIME CHANGE: RANGING -> TRENDING (ADX=30.7 > 30)
2024-05-16, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-05-16, REDUCED SIZE: ADX=18.5 < 20, sizing halved to 0.01
2024-05-16, ASIAN BREAKOUT DOWN: Price=2374.47 < Range Low=2384.75 | ADX=18.5 | Regime=RANGING
2024-05-16,   SHORT: Entry=2374.47, SL=2380.48, TP=2365.46, Size=0.01
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2380.47537021967 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2380.47537021967 to 2380.47.
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2365.4619446704946 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2365.4619446704946 to 2365.46.
2024-05-16 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2374.47, ref_id: 104
2024-05-16 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2380.47, ref_id: 105
2024-05-16 21:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2365.46, ref_id: 106
2024-05-16 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2374.47, ref_id: 104
2024-05-16 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2380.47, ref_id: 105
2024-05-16 21:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2365.46, ref_id: 106
2024-05-16, SELL EXECUTED @ 2374.45, Size: -0.01
2024-05-16 21:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2374.45, ref_id: 104
2024-05-16, TIME EXIT: Position held > 60 mins - closing at market
2024-05-16, Order Failed: Canceled
2024-05-16 22:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2380.47, ref_id: 105
2024-05-16, Order Failed: Canceled
2024-05-16 22:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2365.46, ref_id: 106
2024-05-16 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2374.59, ref_id: 107
2024-05-16 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2374.59, ref_id: 107
2024-05-16, BUY EXECUTED @ 2374.58, Size: 0.01
2024-05-16 22:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2374.58, ref_id: 107
2024-05-16, TRADE PROFIT: $-0.13 [Regime: RANGING]
2024-05-17, ASIAN RANGE: High=2387.80, Low=2373.98, Size=13.82
2024-05-17, REGIME CHANGE: RANGING -> TRENDING (ADX=30.3 > 30)
2024-05-17, TREND PULLBACK: Price > EMA8=2408.08 | ADX=28.0 | Regime=TRENDING
2024-05-17,   LONG: Entry=2408.16, SL=2401.34, TP=2418.39, Size=0.03
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2401.3426352701954 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2401.3426352701954 to 2401.34.
---- [WARNING 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2418.3860470947066 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:18 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2418.3860470947066 to 2418.38.
2024-05-18 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2408.16, ref_id: 108
2024-05-18 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2401.34, ref_id: 109
2024-05-18 00:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2418.38, ref_id: 110
2024-05-18 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2408.16, ref_id: 108
2024-05-18 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2401.34, ref_id: 109
2024-05-18 00:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2418.38, ref_id: 110
2024-05-17, BUY EXECUTED @ 2408.13, Size: 0.03
2024-05-18 00:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2408.13, ref_id: 108
2024-05-17, TIME EXIT: Position held > 60 mins - closing at market
2024-05-17, Order Failed: Canceled
2024-05-18 01:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.03, price: 2401.34, ref_id: 109
2024-05-17, Order Failed: Canceled
2024-05-18 01:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2418.38, ref_id: 110
2024-05-18 01:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2409.52, ref_id: 111
2024-05-18 01:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2409.52, ref_id: 111
2024-05-17, SELL EXECUTED @ 2409.54, Size: -0.03
2024-05-18 01:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2409.54, ref_id: 111
2024-05-17, TRADE PROFIT: $4.23 [Regime: TRENDING]
2024-05-20, ASIAN RANGE: High=2449.99, Low=2423.92, Size=26.07
2024-05-20, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-05-20, REGIME CHANGE: RANGING -> TRENDING (ADX=30.4 > 30)
2024-05-20, TREND PULLBACK: Price < EMA8=2416.96 | ADX=39.7 | Regime=TRENDING
2024-05-20,   SHORT: Entry=2412.73, SL=2421.41, TP=2399.72, Size=0.02
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2421.406647238994 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2421.406647238994 to 2421.4.
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2399.715029141509 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2399.715029141509 to 2399.71.
2024-05-20 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2412.73, ref_id: 112
2024-05-20 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2421.4, ref_id: 113
2024-05-20 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2399.71, ref_id: 114
2024-05-20 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2412.73, ref_id: 112
2024-05-20 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2421.4, ref_id: 113
2024-05-20 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2399.71, ref_id: 114
2024-05-20, SELL EXECUTED @ 2412.72, Size: -0.02
2024-05-20 21:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2412.72, ref_id: 112
2024-05-20, BUY EXECUTED @ 2421.40, Size: 0.02
2024-05-20 22:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.02, executed_price: 2421.4, ref_id: 113
2024-05-20, Order Failed: Canceled
2024-05-20 22:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2399.71, ref_id: 114
2024-05-20, TRADE PROFIT: $-17.36 [Regime: TRENDING]
2024-05-20, REGIME CHANGE: TRENDING -> RANGING (ADX=19.7 < 20)
2024-05-21, ASIAN RANGE: High=2433.05, Low=2406.41, Size=26.64
2024-05-21, REGIME CHANGE: RANGING -> TRENDING (ADX=30.4 > 30)
2024-05-21, REGIME CHANGE: TRENDING -> RANGING (ADX=19.1 < 20)
2024-05-21, REGIME CHANGE: RANGING -> TRENDING (ADX=30.4 > 30)
2024-05-22, ASIAN RANGE: High=2426.54, Low=2411.60, Size=14.94
2024-05-22, REGIME CHANGE: TRENDING -> RANGING (ADX=12.8 < 20)
2024-05-22, REGIME CHANGE: RANGING -> TRENDING (ADX=32.2 > 30)
2024-05-22, TREND PULLBACK: Price < EMA8=2390.26 | ADX=46.0 | Regime=TRENDING
2024-05-22,   SHORT: Entry=2388.65, SL=2396.53, TP=2376.83, Size=0.02
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2396.529694414431 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2396.529694414431 to 2396.52.
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2376.8304583783533 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2376.8304583783533 to 2376.83.
2024-05-22 23:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2388.65, ref_id: 115
2024-05-22 23:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2396.52, ref_id: 116
2024-05-22 23:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2376.83, ref_id: 117
2024-05-22 23:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2388.65, ref_id: 115
2024-05-22 23:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2396.52, ref_id: 116
2024-05-22 23:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2376.83, ref_id: 117
2024-05-22, SELL EXECUTED @ 2388.62, Size: -0.02
2024-05-22 23:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2388.62, ref_id: 115
2024-05-22, TIME EXIT: Position held > 60 mins - closing at market
2024-05-22, Order Failed: Canceled
2024-05-23 00:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2396.52, ref_id: 116
2024-05-22, Order Failed: Canceled
2024-05-23 00:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2376.83, ref_id: 117
2024-05-23 00:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2391.99, ref_id: 118
2024-05-23 00:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2391.99, ref_id: 118
2024-05-22, BUY EXECUTED @ 2392.01, Size: 0.02
2024-05-23 00:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2392.01, ref_id: 118
2024-05-22, TRADE PROFIT: $-6.78 [Regime: TRENDING]
2024-05-23, ASIAN RANGE: High=2381.91, Low=2354.99, Size=26.92
2024-05-23, REGIME CHANGE: TRENDING -> RANGING (ADX=19.8 < 20)
2024-05-23, REGIME CHANGE: RANGING -> TRENDING (ADX=30.8 > 30)
2024-05-23, TREND PULLBACK: Price < EMA8=2348.31 | ADX=28.5 | Regime=TRENDING
2024-05-23,   SHORT: Entry=2345.52, SL=2355.56, TP=2330.46, Size=0.02
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2355.5568868015303 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2355.5568868015303 to 2355.55.
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2330.464669797704 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2330.464669797704 to 2330.46.
2024-05-23 22:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2345.52, ref_id: 119
2024-05-23 22:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2355.55, ref_id: 120
2024-05-23 22:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2330.46, ref_id: 121
2024-05-23 22:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2345.52, ref_id: 119
2024-05-23 22:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2355.55, ref_id: 120
2024-05-23 22:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2330.46, ref_id: 121
2024-05-23, SELL EXECUTED @ 2345.52, Size: -0.02
2024-05-23 22:55:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2345.52, ref_id: 119
2024-05-23, TIME EXIT: Position held > 60 mins - closing at market
2024-05-23, Order Failed: Canceled
2024-05-23 23:55:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2355.55, ref_id: 120
2024-05-23, Order Failed: Canceled
2024-05-23 23:55:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2330.46, ref_id: 121
2024-05-23 23:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2347.35, ref_id: 122
2024-05-23 23:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2347.35, ref_id: 122
2024-05-23, BUY EXECUTED @ 2347.34, Size: 0.02
2024-05-23 23:55:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2347.34, ref_id: 122
2024-05-23, TRADE PROFIT: $-3.64 [Regime: TRENDING]
2024-05-23, TREND PULLBACK: Price < EMA8=2345.68 | ADX=20.4 | Regime=TRENDING
2024-05-23,   SHORT: Entry=2344.72, SL=2351.56, TP=2334.47, Size=0.03
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2351.556486510606 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2351.556486510606 to 2351.55.
---- [WARNING 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2334.4652702340904 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:19 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2334.4652702340904 to 2334.46.
2024-05-24 00:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2344.72, ref_id: 123
2024-05-24 00:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2351.55, ref_id: 124
2024-05-24 00:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2334.46, ref_id: 125
2024-05-24 00:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2344.72, ref_id: 123
2024-05-24 00:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2351.55, ref_id: 124
2024-05-24 00:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2334.46, ref_id: 125
2024-05-23, SELL EXECUTED @ 2344.75, Size: -0.03
2024-05-24 00:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2344.75, ref_id: 123
2024-05-23, TIME EXIT: Position held > 60 mins - closing at market
2024-05-23, Order Failed: Canceled
2024-05-24 01:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2351.55, ref_id: 124
2024-05-23, Order Failed: Canceled
2024-05-24 01:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2334.46, ref_id: 125
2024-05-24 01:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2341.35, ref_id: 126
2024-05-24 01:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2341.35, ref_id: 126
2024-05-23, BUY EXECUTED @ 2341.34, Size: 0.03
2024-05-24 01:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2341.34, ref_id: 126
2024-05-23, TRADE PROFIT: $10.23 [Regime: TRENDING]
2024-05-24, ASIAN RANGE: High=2340.59, Low=2325.46, Size=15.13
2024-05-24, REGIME CHANGE: TRENDING -> RANGING (ADX=19.8 < 20)
2024-05-27, ASIAN RANGE: High=2347.59, Low=2334.63, Size=12.96
2024-05-27, REGIME CHANGE: RANGING -> TRENDING (ADX=32.3 > 30)
2024-05-27, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-05-27, REGIME CHANGE: RANGING -> TRENDING (ADX=30.6 > 30)
2024-05-27, REGIME CHANGE: TRENDING -> RANGING (ADX=19.8 < 20)
2024-05-28, ASIAN RANGE: High=2356.36, Low=2341.35, Size=15.01
2024-05-28, REGIME CHANGE: RANGING -> TRENDING (ADX=41.3 > 30)
2024-05-28, REGIME CHANGE: TRENDING -> RANGING (ADX=19.1 < 20)
2024-05-28, REGIME CHANGE: RANGING -> TRENDING (ADX=30.5 > 30)
2024-05-28, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-05-29, ASIAN RANGE: High=2361.35, Low=2350.63, Size=10.72
2024-05-29, REGIME CHANGE: RANGING -> TRENDING (ADX=30.5 > 30)
2024-05-29, REGIME CHANGE: TRENDING -> RANGING (ADX=18.9 < 20)
2024-05-30, ASIAN RANGE: High=2339.87, Low=2322.58, Size=17.29
2024-05-30, REGIME CHANGE: RANGING -> TRENDING (ADX=31.0 > 30)
2024-05-30, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-05-31, ASIAN RANGE: High=2347.73, Low=2337.01, Size=10.72
2024-05-31, REGIME CHANGE: RANGING -> TRENDING (ADX=32.0 > 30)
2024-05-31, TREND PULLBACK: Price < EMA8=2331.41 | ADX=41.6 | Regime=TRENDING
2024-05-31,   SHORT: Entry=2330.11, SL=2336.78, TP=2320.11, Size=0.03
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2336.775359235849 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2336.775359235849 to 2336.77.
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2320.111961146227 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2320.111961146227 to 2320.11.
2024-06-01 00:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2330.11, ref_id: 127
2024-06-01 00:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2336.77, ref_id: 128
2024-06-01 00:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2320.11, ref_id: 129
2024-06-01 00:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2330.11, ref_id: 127
2024-06-01 00:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2336.77, ref_id: 128
2024-06-01 00:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2320.11, ref_id: 129
2024-05-31, SELL EXECUTED @ 2330.06, Size: -0.03
2024-06-01 00:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2330.06, ref_id: 127
2024-05-31, TIME EXIT: Position held > 60 mins - closing at market
2024-05-31, Order Failed: Canceled
2024-06-01 01:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2336.77, ref_id: 128
2024-05-31, Order Failed: Canceled
2024-06-01 01:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2320.11, ref_id: 129
2024-06-01 01:05:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2332.86, ref_id: 130
2024-06-01 01:05:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2332.86, ref_id: 130
2024-05-31, BUY EXECUTED @ 2332.87, Size: 0.03
2024-06-01 01:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2332.87, ref_id: 130
2024-05-31, TRADE PROFIT: $-8.43 [Regime: TRENDING]
2024-06-03, ASIAN RANGE: High=2331.01, Low=2314.73, Size=16.28
2024-06-03, TREND PULLBACK: Price > EMA8=2337.36 | ADX=39.1 | Regime=TRENDING
2024-06-03,   LONG: Entry=2339.99, SL=2333.88, TP=2349.16, Size=0.03
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2333.876580087545 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2333.876580087545 to 2333.87.
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2349.160129868682 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2349.160129868682 to 2349.16.
2024-06-03 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2339.99, ref_id: 131
2024-06-03 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2333.87, ref_id: 132
2024-06-03 22:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2349.16, ref_id: 133
2024-06-03 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2339.99, ref_id: 131
2024-06-03 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2333.87, ref_id: 132
2024-06-03 22:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2349.16, ref_id: 133
2024-06-03, BUY EXECUTED @ 2340.05, Size: 0.03
2024-06-03 22:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2340.05, ref_id: 131
2024-06-03, TIME EXIT: Position held > 60 mins - closing at market
2024-06-03, Order Failed: Canceled
2024-06-03 23:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.03, price: 2333.87, ref_id: 132
2024-06-03, Order Failed: Canceled
2024-06-03 23:25:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2349.16, ref_id: 133
2024-06-03 23:25:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2341.37, ref_id: 134
2024-06-03 23:25:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2341.37, ref_id: 134
2024-06-03, SELL EXECUTED @ 2341.39, Size: -0.03
2024-06-03 23:25:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2341.39, ref_id: 134
2024-06-03, TRADE PROFIT: $4.02 [Regime: TRENDING]
2024-06-04, ASIAN RANGE: High=2352.38, Low=2340.69, Size=11.69
2024-06-04, TREND PULLBACK: Price < EMA8=2327.71 | ADX=29.9 | Regime=TRENDING
2024-06-04,   SHORT: Entry=2324.06, SL=2330.75, TP=2314.03, Size=0.03
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2330.7477082974337 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2330.7477082974337 to 2330.74.
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2314.0284375538495 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2314.0284375538495 to 2314.02.
2024-06-04 22:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2324.06, ref_id: 135
2024-06-04 22:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2330.74, ref_id: 136
2024-06-04 22:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2314.02, ref_id: 137
2024-06-04 22:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2324.06, ref_id: 135
2024-06-04 22:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2330.74, ref_id: 136
2024-06-04 22:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2314.02, ref_id: 137
2024-06-04, SELL EXECUTED @ 2324.03, Size: -0.03
2024-06-04 22:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2324.03, ref_id: 135
2024-06-04, TIME EXIT: Position held > 60 mins - closing at market
2024-06-04, Order Failed: Canceled
2024-06-04 23:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2330.74, ref_id: 136
2024-06-04, Order Failed: Canceled
2024-06-04 23:15:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2314.02, ref_id: 137
2024-06-04 23:15:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2322.85, ref_id: 138
2024-06-04 23:15:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2322.85, ref_id: 138
2024-06-04, BUY EXECUTED @ 2323.27, Size: 0.03
2024-06-04 23:15:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2323.27, ref_id: 138
2024-06-04, TRADE PROFIT: $2.28 [Regime: TRENDING]
2024-06-04, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)
2024-06-05, ASIAN RANGE: High=2341.66, Low=2325.87, Size=15.79
2024-06-05, REGIME CHANGE: RANGING -> TRENDING (ADX=31.1 > 30)
2024-06-05, TREND PULLBACK: Price > EMA8=2341.05 | ADX=25.1 | Regime=TRENDING
2024-06-05,   LONG: Entry=2345.60, SL=2338.77, TP=2355.84, Size=0.03
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2338.773243897886 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2338.773243897886 to 2338.77.
---- [WARNING 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2355.8401341531708 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:21 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2355.8401341531708 to 2355.84.
2024-06-05 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2345.6, ref_id: 139
2024-06-05 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2338.77, ref_id: 140
2024-06-05 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2355.84, ref_id: 141
2024-06-05 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2345.6, ref_id: 139
2024-06-05 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2338.77, ref_id: 140
2024-06-05 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2355.84, ref_id: 141
2024-06-05, BUY EXECUTED @ 2345.63, Size: 0.03
2024-06-05 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2345.63, ref_id: 139
2024-06-05, TIME EXIT: Position held > 60 mins - closing at market
2024-06-05, Order Failed: Canceled
2024-06-05 23:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.03, price: 2338.77, ref_id: 140
2024-06-05, Order Failed: Canceled
2024-06-05 23:30:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2355.84, ref_id: 141
2024-06-05 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2351.97, ref_id: 142
2024-06-05 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2351.97, ref_id: 142
2024-06-05, SELL EXECUTED @ 2351.96, Size: -0.03
2024-06-05 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2351.96, ref_id: 142
2024-06-05, TRADE PROFIT: $18.99 [Regime: TRENDING]
2024-06-06, ASIAN RANGE: High=2374.93, Low=2355.25, Size=19.68
2024-06-06, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-06-06, REGIME CHANGE: RANGING -> TRENDING (ADX=31.3 > 30)
2024-06-07, ASIAN RANGE: High=2387.68, Low=2369.41, Size=18.27
2024-06-07, TREND PULLBACK: Price < EMA8=2331.81 | ADX=51.1 | Regime=TRENDING
2024-06-07,   SHORT: Entry=2320.36, SL=2328.22, TP=2308.57, Size=0.02
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2328.222912767548 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2328.222912767548 to 2328.22.
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2308.5656308486778 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2308.5656308486778 to 2308.56.
2024-06-07 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2320.36, ref_id: 143
2024-06-07 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2328.22, ref_id: 144
2024-06-07 20:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2308.56, ref_id: 145
2024-06-07 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2320.36, ref_id: 143
2024-06-07 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2328.22, ref_id: 144
2024-06-07 20:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2308.56, ref_id: 145
2024-06-07, SELL EXECUTED @ 2320.34, Size: -0.02
2024-06-07 20:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2320.34, ref_id: 143
2024-06-07, TIME EXIT: Position held > 60 mins - closing at market
2024-06-07, Order Failed: Canceled
2024-06-07 21:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2328.22, ref_id: 144
2024-06-07, Order Failed: Canceled
2024-06-07 21:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2308.56, ref_id: 145
2024-06-07 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2320.78, ref_id: 146
2024-06-07 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2320.78, ref_id: 146
2024-06-07, BUY EXECUTED @ 2320.79, Size: 0.02
2024-06-07 21:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2320.79, ref_id: 146
2024-06-07, TRADE PROFIT: $-0.90 [Regime: TRENDING]
2024-06-07, TREND PULLBACK: Price < EMA8=2316.58 | ADX=35.6 | Regime=TRENDING
2024-06-07,   SHORT: Entry=2314.59, SL=2323.19, TP=2301.69, Size=0.02
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2323.1928492168277 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2323.1928492168277 to 2323.19.
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2301.685726174759 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2301.685726174759 to 2301.68.
2024-06-07 22:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2314.59, ref_id: 147
2024-06-07 22:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2323.19, ref_id: 148
2024-06-07 22:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2301.68, ref_id: 149
2024-06-07 22:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2314.59, ref_id: 147
2024-06-07 22:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2323.19, ref_id: 148
2024-06-07 22:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2301.68, ref_id: 149
2024-06-07, SELL EXECUTED @ 2314.58, Size: -0.02
2024-06-07 22:55:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2314.58, ref_id: 147
2024-06-07, TIME EXIT: Position held > 60 mins - closing at market
2024-06-07, Order Failed: Canceled
2024-06-07 23:55:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2323.19, ref_id: 148
2024-06-07, Order Failed: Canceled
2024-06-07 23:55:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2301.68, ref_id: 149
2024-06-07 23:55:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2307.64, ref_id: 150
2024-06-07 23:55:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2307.64, ref_id: 150
2024-06-07, BUY EXECUTED @ 2307.73, Size: 0.02
2024-06-07 23:55:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2307.73, ref_id: 150
2024-06-07, TRADE PROFIT: $13.70 [Regime: TRENDING]
2024-06-10, ASIAN RANGE: High=2301.36, Low=2287.74, Size=13.62
2024-06-10, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-06-10, REGIME CHANGE: RANGING -> TRENDING (ADX=30.9 > 30)
2024-06-10, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-06-10, REGIME CHANGE: RANGING -> TRENDING (ADX=31.2 > 30)
2024-06-11, ASIAN RANGE: High=2311.96, Low=2297.73, Size=14.23
2024-06-11, REGIME CHANGE: TRENDING -> RANGING (ADX=19.0 < 20)
2024-06-11, REGIME CHANGE: RANGING -> TRENDING (ADX=32.3 > 30)
2024-06-11, REGIME CHANGE: TRENDING -> RANGING (ADX=19.3 < 20)
2024-06-12, ASIAN RANGE: High=2317.75, Low=2310.74, Size=7.01
2024-06-12, REGIME CHANGE: RANGING -> TRENDING (ADX=30.1 > 30)
2024-06-12, TREND PULLBACK: Price > EMA8=2336.58 | ADX=52.3 | Regime=TRENDING
2024-06-12,   LONG: Entry=2340.19, SL=2333.61, TP=2350.07, Size=0.03
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2333.6066561101225 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2333.6066561101225 to 2333.6.
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2350.0650158348167 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2350.0650158348167 to 2350.06.
2024-06-12 21:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2340.19, ref_id: 151
2024-06-12 21:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2333.6, ref_id: 152
2024-06-12 21:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2350.06, ref_id: 153
2024-06-12 21:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2340.19, ref_id: 151
2024-06-12 21:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2333.6, ref_id: 152
2024-06-12 21:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2350.06, ref_id: 153
2024-06-12, BUY EXECUTED @ 2340.23, Size: 0.03
2024-06-12 21:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2340.23, ref_id: 151
2024-06-12, SELL EXECUTED @ 2333.60, Size: -0.03
2024-06-12 21:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2333.6, ref_id: 152
2024-06-12, Order Failed: Canceled
2024-06-12 21:40:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2350.06, ref_id: 153
2024-06-12, TRADE PROFIT: $-19.89 [Regime: TRENDING]
2024-06-12, REGIME CHANGE: TRENDING -> RANGING (ADX=19.7 < 20)
2024-06-12, REDUCED SIZE: ADX=17.9 < 20, sizing halved to 0.01
2024-06-12, ASIAN BREAKOUT UP: Price=2329.92 > Range High=2317.75 | ADX=17.9 | Regime=RANGING
2024-06-12,   LONG: Entry=2329.92, SL=2323.50, TP=2339.55, Size=0.01
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2323.5014936800926 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2323.5014936800926 to 2323.5.
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2339.547759479861 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2339.547759479861 to 2339.54.
2024-06-12 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2329.92, ref_id: 154
2024-06-12 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2323.5, ref_id: 155
2024-06-12 23:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2339.54, ref_id: 156
2024-06-12 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2329.92, ref_id: 154
2024-06-12 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2323.5, ref_id: 155
2024-06-12 23:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2339.54, ref_id: 156
2024-06-12, BUY EXECUTED @ 2329.96, Size: 0.01
2024-06-12 23:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2329.96, ref_id: 154
2024-06-12, TIME EXIT: Position held > 60 mins - closing at market
2024-06-12, Order Failed: Canceled
2024-06-13 00:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2323.5, ref_id: 155
2024-06-12, Order Failed: Canceled
2024-06-13 00:35:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.01, price: 2339.54, ref_id: 156
2024-06-13 00:35:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2335.11, ref_id: 157
2024-06-13 00:35:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2335.11, ref_id: 157
2024-06-12, SELL EXECUTED @ 2335.12, Size: -0.01
2024-06-13 00:35:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2335.12, ref_id: 157
2024-06-12, TRADE PROFIT: $5.16 [Regime: RANGING]
2024-06-13, ASIAN RANGE: High=2321.54, Low=2308.15, Size=13.39
2024-06-13, REGIME CHANGE: RANGING -> TRENDING (ADX=31.4 > 30)
2024-06-13, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-06-13, REGIME CHANGE: RANGING -> TRENDING (ADX=30.7 > 30)
2024-06-13, TREND PULLBACK: Price > EMA8=2319.36 | ADX=33.6 | Regime=TRENDING
2024-06-13,   LONG: Entry=2322.83, SL=2315.97, TP=2333.12, Size=0.03
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2315.9699830930485 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2315.9699830930485 to 2315.96.
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2333.1200253604275 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2333.1200253604275 to 2333.12.
2024-06-13 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.03, price: 2322.83, ref_id: 158
2024-06-13 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2315.96, ref_id: 159
2024-06-13 21:40:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2333.12, ref_id: 160
2024-06-13 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.03, price: 2322.83, ref_id: 158
2024-06-13 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.03, price: 2315.96, ref_id: 159
2024-06-13 21:40:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.03, price: 2333.12, ref_id: 160
2024-06-13, BUY EXECUTED @ 2322.73, Size: 0.03
2024-06-13 21:40:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.03, executed_price: 2322.73, ref_id: 158
2024-06-13, SELL EXECUTED @ 2315.96, Size: -0.03
2024-06-13 21:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Stop, executed_size: -0.03, executed_price: 2315.96, ref_id: 159
2024-06-13, Order Failed: Canceled
2024-06-13 21:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Limit, size: -0.03, price: 2333.12, ref_id: 160
2024-06-13, TRADE PROFIT: $-20.31 [Regime: TRENDING]
2024-06-13, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-06-13, REDUCED SIZE: ADX=18.2 < 20, sizing halved to 0.01
2024-06-13, ASIAN BREAKOUT DOWN: Price=2306.60 < Range Low=2308.15 | ADX=18.2 | Regime=RANGING
2024-06-13,   SHORT: Entry=2306.60, SL=2313.34, TP=2296.49, Size=0.01
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2313.342494845811 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2313.342494845811 to 2313.34.
---- [WARNING 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2296.4862577312833 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:22 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2296.4862577312833 to 2296.48.
2024-06-13 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2306.6, ref_id: 161
2024-06-13 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2313.34, ref_id: 162
2024-06-13 23:45:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2296.48, ref_id: 163
2024-06-13 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2306.6, ref_id: 161
2024-06-13 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2313.34, ref_id: 162
2024-06-13 23:45:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2296.48, ref_id: 163
2024-06-13, SELL EXECUTED @ 2306.54, Size: -0.01
2024-06-13 23:45:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2306.54, ref_id: 161
2024-06-13, BUY EXECUTED @ 2296.48, Size: 0.01
2024-06-14 00:05:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.01, executed_price: 2296.48, ref_id: 163
2024-06-13, Order Failed: Canceled
2024-06-14 00:05:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.01, price: 2313.34, ref_id: 162
2024-06-13, TRADE PROFIT: $10.06 [Regime: RANGING]
2024-06-13, REGIME CHANGE: RANGING -> TRENDING (ADX=34.0 > 30)
2024-06-14, ASIAN RANGE: High=2316.74, Low=2303.09, Size=13.65
2024-06-14, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)
2024-06-17, ASIAN RANGE: High=2328.93, Low=2315.49, Size=13.44
2024-06-18, ASIAN RANGE: High=2325.68, Low=2315.01, Size=10.67
2024-06-18, REGIME CHANGE: RANGING -> TRENDING (ADX=34.2 > 30)
2024-06-19, ASIAN RANGE: High=2332.73, Low=2326.54, Size=6.19
2024-06-19, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-06-20, ASIAN RANGE: High=2345.64, Low=2328.94, Size=16.70
2024-06-20, REGIME CHANGE: RANGING -> TRENDING (ADX=37.0 > 30)
2024-06-20, REGIME CHANGE: TRENDING -> RANGING (ADX=19.2 < 20)
2024-06-20, REGIME CHANGE: RANGING -> TRENDING (ADX=32.5 > 30)
2024-06-20, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-06-21, ASIAN RANGE: High=2365.61, Low=2355.13, Size=10.48
2024-06-21, REGIME CHANGE: RANGING -> TRENDING (ADX=35.3 > 30)
2024-06-21, REGIME CHANGE: TRENDING -> RANGING (ADX=19.6 < 20)
2024-06-21, REGIME CHANGE: RANGING -> TRENDING (ADX=31.1 > 30)
2024-06-21, TREND PULLBACK: Price < EMA8=2335.67 | ADX=58.7 | Regime=TRENDING
2024-06-21,   SHORT: Entry=2333.05, SL=2341.36, TP=2320.59, Size=0.02
---- [WARNING 2025-12-15 23:58:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2341.357738397631 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2341.357738397631 to 2341.35.
---- [WARNING 2025-12-15 23:58:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2320.5883924035547 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-15 23:58:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2320.5883924035547 to 2320.58.
2024-06-21 22:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.02, price: 2333.05, ref_id: 164
2024-06-21 22:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2341.35, ref_id: 165
2024-06-21 22:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2320.58, ref_id: 166
2024-06-21 22:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.02, price: 2333.05, ref_id: 164
2024-06-21 22:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.02, price: 2341.35, ref_id: 165
2024-06-21 22:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.02, price: 2320.58, ref_id: 166
2024-06-21, SELL EXECUTED @ 2333.11, Size: -0.02
2024-06-21 22:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.02, executed_price: 2333.11, ref_id: 164
2024-06-21, TIME EXIT: Position held > 60 mins - closing at market
2024-06-21, Order Failed: Canceled
2024-06-21 23:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.02, price: 2341.35, ref_id: 165
2024-06-21, Order Failed: Canceled
2024-06-21 23:50:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.02, price: 2320.58, ref_id: 166
2024-06-21 23:50:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2327.18, ref_id: 167
2024-06-21 23:50:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2327.18, ref_id: 167
2024-06-21, BUY EXECUTED @ 2327.21, Size: 0.02
2024-06-21 23:50:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2327.21, ref_id: 167
2024-06-21, TRADE PROFIT: $11.80 [Regime: TRENDING]
2024-06-24, ASIAN RANGE: High=2331.75, Low=2319.02, Size=12.73
2024-06-24, REGIME CHANGE: TRENDING -> RANGING (ADX=19.5 < 20)
2024-06-25, ASIAN RANGE: High=2330.91, Low=2322.76, Size=8.15
2024-06-25, REGIME CHANGE: RANGING -> TRENDING (ADX=31.0 > 30)
2024-06-26, ASIAN RANGE: High=2321.63, Low=2309.65, Size=11.98
2024-06-26, REGIME CHANGE: TRENDING -> RANGING (ADX=15.9 < 20)
2024-06-26, REGIME CHANGE: RANGING -> TRENDING (ADX=31.1 > 30)
2024-06-26, REGIME CHANGE: TRENDING -> RANGING (ADX=19.8 < 20)
2024-06-27, ASIAN RANGE: High=2303.40, Low=2296.55, Size=6.85
2024-06-27, REGIME CHANGE: RANGING -> TRENDING (ADX=31.8 > 30)
2024-06-27, REGIME CHANGE: TRENDING -> RANGING (ADX=19.9 < 20)
2024-06-28, ASIAN RANGE: High=2328.80, Low=2319.04, Size=9.76
2024-06-28, REGIME CHANGE: RANGING -> TRENDING (ADX=31.0 > 30)
2024-06-28, REGIME CHANGE: TRENDING -> RANGING (ADX=19.4 < 20)

=== BACKTEST RESULTS ===
--------- Returns ---------
{
    "rtot": -0.00042175000000001516,
    "ravg": -2.4265226901510987e-06,
    "rnorm": -0.018385279954320134,
    "rnorm100": 83.85279954320134,
    "rtot_new": 0.9578249999999985,
    "rnorm_new": -0.8385279954320134
}
===========================
---- [INFO 2025-12-15 23:58:25 +0800 strategy_utils.extract_suggest_improvements_and_plot_run_results:348]: ==== Full analyzers output: =========
"{'returns': OrderedDict({'rtot': -0.00042175000000001516, 'ravg': -2.4265226901510987e-06, 'rnorm': -0.018385279954320134, 'rnorm100': 83.85279954320134, 'rtot_new': 0.9578249999999985, 'rnorm_new': -0.8385279954320134}), 'drawdown': AutoOrderedDict({'len': 16481, 'drawdown': 5.254489611205504, 'moneydown': 106.24000000000296, 'max': AutoOrderedDict({'len': 16481, 'drawdown': 6.927181993085878, 'moneydown': 140.06000000000404})}), 'vwr': OrderedDict({'vwr': -0.00015441063928904136}), 'tradeanalyzer': AutoOrderedDict({'total': AutoOrderedDict({'total': 47, 'open': 0, 'closed': 47}), 'streak': AutoOrderedDict({'won': AutoOrderedDict({'current': 2, 'longest': 3}), 'lost': AutoOrderedDict({'current': 0, 'longest': 7})}), 'pnl': AutoOrderedDict({'gross': AutoOrderedDict({'total': -84.350000000002, 'average': -1.7946808510638723}), 'net': AutoOrderedDict({'total': -84.350000000002, 'average': -1.7946808510638723})}), 'won': AutoOrderedDict({'total': 20, 'pnl': AutoOrderedDict({'total': 188.4"
========== Backtest finished after 0:00:15.597558!
