========== Starting to setup a Backtest:
Using configuration: symbolName='XAUUSD.PRO' symbolId=781 resolution='30m' commission=0.0 startDate=datetime.datetime(2025, 2, 1, 0, 0, tzinfo=TzInfo(UTC)) endDate=datetime.datetime(2025, 12, 10, 0, 0, tzinfo=TzInfo(UTC)) leverage=100.0 margin=2500.0 strategyParamsInput={'asian_start_hour': 0, 'asian_end_hour': 8, 'trade_end_hour': 20, 'risk_per_trade_percent': 0.01, 'max_daily_trades': 3, 'max_daily_loss': 75, 'max_drawdown_percent': 0.06, 'max_lots': 0.5, 'contract_size': 100, 'tp_risk_reward': 1.5, 'use_trailing_stop': True, 'trailing_activation_pct': 0.4, 'trailing_distance_pct': 0.5}
---- [INFO 2025-12-10 15:19:24 +0800 strategy_utils.add_sizer_to_cerebro:297]: Using default sizer 'TLLotSizer'
========== Setup finished. Backtest is running...
---, London Breakout Strategy Started
2025-02-03, BREAKOUT BUY: Price 2797.82 > Asian High 2793.80
---- [WARNING 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2784.1000000000004 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2784.1000000000004 to 2784.1.
---- [WARNING 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2818.3999999999996 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2818.3999999999996 to 2818.4.
2025-02-03 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.02, price: 2797.82, ref_id: 1
2025-02-03 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2784.1, ref_id: 2
2025-02-03 17:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2818.4, ref_id: 3
2025-02-03 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.02, price: 2797.82, ref_id: 1
2025-02-03 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.02, price: 2784.1, ref_id: 2
2025-02-03 17:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.02, price: 2818.4, ref_id: 3
2025-02-03, LONG Entry @ 2797.73
2025-02-03 17:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.02, executed_price: 2797.73, ref_id: 1
2025-02-03 23:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.02, executed_price: 2818.4, ref_id: 3
2025-02-03 23:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.02, price: 2784.1, ref_id: 2
2025-02-03, TRADE PROFIT, GROSS 41.34, NET 41.34
2025-02-03, 2025-02-03, Daily PnL: $41.34
2025-02-03, BREAKOUT BUY: Price 2828.67 > Asian High 2793.80
---- [WARNING 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2784.1000000000004 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2784.1000000000004 to 2784.1.
---- [WARNING 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2895.5249999999996 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2895.5249999999996 to 2895.52.
2025-02-03 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2828.67, ref_id: 4
2025-02-03 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2784.1, ref_id: 5
2025-02-03 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2895.52, ref_id: 6
2025-02-03 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2828.67, ref_id: 4
2025-02-03 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2784.1, ref_id: 5
2025-02-03 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2895.52, ref_id: 6
2025-02-03, LONG Entry @ 2828.92
2025-02-03 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2828.92, ref_id: 4
2025-02-03, End of Day - Closing Positions
2025-02-04 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2818.31, ref_id: 7
2025-02-04 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2818.31, ref_id: 7
2025-02-04 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2818.3, ref_id: 7
2025-02-03, TRADE PROFIT, GROSS -10.62, NET -10.62
2025-02-03, 2025-02-03, Daily PnL: $30.72
2025-02-04, BREAKOUT BUY: Price 2834.92 > Asian High 2823.34
---- [WARNING 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2864.1400000000003 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2864.1400000000003 to 2864.14.
2025-02-04 22:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2834.92, ref_id: 8
2025-02-04 22:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2815.44, ref_id: 9
2025-02-04 22:00:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2864.14, ref_id: 10
2025-02-04 22:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2834.92, ref_id: 8
2025-02-04 22:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Stop, size: -0.01, price: 2815.44, ref_id: 9
2025-02-04 22:00:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Limit, size: -0.01, price: 2864.14, ref_id: 10
2025-02-04, LONG Entry @ 2834.94
2025-02-04 22:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2834.94, ref_id: 8
2025-02-04, End of Day - Closing Positions
2025-02-05 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2843.01, ref_id: 11
2025-02-05 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2843.01, ref_id: 11
2025-02-05 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2843.1, ref_id: 11
2025-02-04, TRADE PROFIT, GROSS 8.16, NET 8.16
2025-02-04, 2025-02-04, Daily PnL: $8.16
2025-02-05, SHORT Entry @ 2864.14
2025-02-05 16:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Limit, executed_size: -0.01, executed_price: 2864.14, ref_id: 10
2025-02-05 16:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Sell, exec_type: Stop, size: -0.01, price: 2815.44, ref_id: 9
2025-02-05, End of Day - Closing Positions
2025-02-06 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2863.53, ref_id: 12
2025-02-06 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2863.53, ref_id: 12
2025-02-06 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2863.71, ref_id: 12
2025-02-05, TRADE PROFIT, GROSS 0.43, NET 0.43
2025-02-05, 2025-02-05, Daily PnL: $0.43
2025-02-06, BREAKOUT SELL: Price 2855.87 < Asian Low 2859.05
2025-02-06 16:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2855.87, ref_id: 13
2025-02-06 16:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 14
2025-02-06 16:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2841.68, ref_id: 15
2025-02-06 16:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2855.87, ref_id: 13
2025-02-06 16:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 14
2025-02-06 16:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2841.68, ref_id: 15
2025-02-06, SHORT Entry @ 2855.84
2025-02-06 16:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2855.84, ref_id: 13
2025-02-06 20:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.03, executed_price: 2865.33, ref_id: 14
2025-02-06 20:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.03, price: 2841.68, ref_id: 15
2025-02-06, TRADE PROFIT, GROSS -28.47, NET -28.47
2025-02-06, 2025-02-06, Daily PnL: $-28.47
2025-02-06, BREAKOUT SELL: Price 2856.73 < Asian Low 2859.05
2025-02-06 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.03, price: 2856.73, ref_id: 16
2025-02-06 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 17
2025-02-06 22:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2843.83, ref_id: 18
2025-02-06 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.03, price: 2856.73, ref_id: 16
2025-02-06 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 17
2025-02-06 22:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.03, price: 2843.83, ref_id: 18
2025-02-06, SHORT Entry @ 2856.69
2025-02-06 22:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.03, executed_price: 2856.69, ref_id: 16
2025-02-06 23:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Limit, executed_size: 0.03, executed_price: 2843.83, ref_id: 18
2025-02-06 23:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Stop, size: 0.03, price: 2865.33, ref_id: 17
2025-02-06, TRADE PROFIT, GROSS 38.58, NET 38.58
2025-02-06, 2025-02-06, Daily PnL: $10.11
2025-02-06, BREAKOUT SELL: Price 2842.00 < Asian Low 2859.05
---- [WARNING 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:291]: Order price 2807.005 is not a multiple of the tick size 0.01.
---- [INFO 2025-12-10 15:19:24 +0800 order_validation.validate_and_get_updated_order_params:293]: Adjusted order price from 2807.005 to 2807.0.
2025-02-06 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Sell, exec_type: Market, size: -0.01, price: 2842.0, ref_id: 19
2025-02-06 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2865.33, ref_id: 20
2025-02-06 23:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2807.0, ref_id: 21
2025-02-06 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Sell, exec_type: Market, size: -0.01, price: 2842.0, ref_id: 19
2025-02-06 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Stop, size: 0.01, price: 2865.33, ref_id: 20
2025-02-06 23:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Limit, size: 0.01, price: 2807.0, ref_id: 21
2025-02-06, SHORT Entry @ 2841.90
2025-02-06 23:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Sell, exec_type: Market, executed_size: -0.01, executed_price: 2841.9, ref_id: 19
2025-02-06, End of Day - Closing Positions
2025-02-07 04:30:00 +0800 [STRATEGY] Order Submitted to the broker | type: Buy, exec_type: Market, size: 0.01, price: 2853.76, ref_id: 22
2025-02-07 04:30:00 +0800 [STRATEGY] Order Accepted by the broker | type: Buy, exec_type: Market, size: 0.01, price: 2853.76, ref_id: 22
2025-02-07 04:30:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Market, executed_size: 0.01, executed_price: 2853.79, ref_id: 22
2025-02-06, TRADE PROFIT, GROSS -11.89, NET -11.89
2025-02-06, 2025-02-06, Daily PnL: $-1.78
2025-02-07, LONG Entry @ 2865.33
2025-02-07 10:00:00 +0800 [STRATEGY] Order Completed by the broker | type: Buy, exec_type: Stop, executed_size: 0.01, executed_price: 2865.33, ref_id: 20
2025-02-07 10:00:00 +0800 [STRATEGY] Order Canceled by the user | type: Buy, exec_type: Limit, size: 0.01, price: 2807.0, ref_id: 21
2025-02-07, Trailing Stop ACTIVATED for LONG @ profit=0.94, threshold=0.00
2025-02-07, Trailing SL Updated: 2865.33 ? 2866.27 (trail dist=0.00)
Process failed: 'charmap' codec can't encode character '\u2192' in position 41: character maps to <undefined>
Traceback: Traceback (most recent call last):
  File "tl_worker\worker.py", line 230, in <module>
  File "backtrader\cerebro.py", line 1209, in run
  File "backtrader\cerebro.py", line 1383, in runstrategies
  File "backtrader\cerebro.py", line 1721, in _runnext
  File "backtrader\strategy.py", line 348, in _next
  File "backtrader\lineiterator.py", line 271, in _next
  File "<string>", line 200, in next
  File "<string>", line 65, in log
  File "tl_worker\worker.py", line 131, in new_print
  File "encodings\cp1252.py", line 19, in encode
UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 41: character maps to <undefined>


Backtest exited.
--> Process FAILED with error code: 2!