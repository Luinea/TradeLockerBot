import backtrader as bt
import math


class XauMeanReversionStrategy(bt.Strategy):
    """
    Mean Reversion Strategy for XAU/USD Scalping.
    
    Strategy Logic (Confluence of Three):
    - Bollinger Bands (20, 2): Price containment - 95% within bands
    - RSI (14): Exhaustion filter - oversold <30, overbought >70
    - Stochastic (5,3,3): Entry trigger on crossover
    
    Entry Rules:
    - LONG: Price below Lower BB + RSI < 30 + Stoch %K crosses above %D below 20
    - SHORT: Price above Upper BB + RSI > 70 + Stoch %K crosses below %D above 80
    
    Exit Rules:
    - Target: Middle Bollinger Band (20 SMA)
    - Stop Loss: ATR * 1.5 from entry
    
    Time Filter:
    - Only trade during London/NY Overlap (13:00-17:00 GMT)
    
    Based on Strat.md Section 4: Mean Reversion (Bollinger + RSI + Stochastic)
    """
    
    params = (
        # Bollinger Bands
        ("bb_period", 20),
        ("bb_dev", 2.0),
        
        # RSI
        ("rsi_period", 14),
        ("rsi_oversold", 30),
        ("rsi_overbought", 70),
        
        # Stochastic
        ("stoch_k", 5),
        ("stoch_d", 3),
        ("stoch_slow", 3),
        ("stoch_oversold", 20),
        ("stoch_overbought", 80),
        ("require_stoch_crossover", True),  # Set False for BB+RSI only mode
        
        # ATR for dynamic SL/TP
        ("atr_period", 14),
        ("atr_sl_multiplier", 1.5),
        
        # Time Filter (London/NY Overlap in GMT)
        ("trade_start_hour", 13),
        ("trade_end_hour", 17),
        ("use_time_filter", True),
        
        # Risk Limits (FundedHero Compliance)
        ("risk_per_trade_percent", 0.01),  # 1% risk
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06),  # 6% circuit breaker
        ("max_lots", 0.5),
        ("contract_size", 100),
        
        # Spread Filter
        ("max_spread", 0.50),  # $0.50 max spread
    )

    def __init__(self):
        # Indicators
        self.bb = bt.indicators.BollingerBands(
            self.data.close,
            period=self.params.bb_period,
            devfactor=self.params.bb_dev
        )
        
        self.rsi = bt.indicators.RSI(
            self.data.close,
            period=self.params.rsi_period
        )
        
        self.stoch = bt.indicators.Stochastic(
            self.data,
            period=self.params.stoch_k,
            period_dfast=self.params.stoch_d,
            period_dslow=self.params.stoch_slow
        )
        
        self.atr = bt.indicators.ATR(
            self.data,
            period=self.params.atr_period
        )
        
        # Stochastic crossover detection
        self.stoch_cross_up = bt.indicators.CrossOver(
            self.stoch.percK, self.stoch.percD
        )
        
        # State tracking
        self.order = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.peak_equity = 0.0

    def log(self, txt, dt=None):
        if dt is None:
            try:
                dt = self.datas[0].datetime.date(0)
                dts = dt.isoformat()
            except IndexError:
                dts = "---"
        else:
            dts = dt.isoformat() if hasattr(dt, 'isoformat') else str(dt)
        print(f'{dts}, {txt}')

    def start(self):
        self.log("XAU Mean Reversion Strategy Started")
        self.peak_equity = self.broker.getvalue()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED @ {order.executed.price:.2f}, Size: {order.executed.size:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED @ {order.executed.price:.2f}, Size: {order.executed.size:.2f}')

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(f'TRADE PROFIT, GROSS {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')
        
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date == current_date:
            self.daily_pnl += trade.pnlcomm
        else:
            self.daily_pnl = trade.pnlcomm
            self.last_trade_date = current_date
            self.daily_trades = 0
        
        self.log(f'Daily PnL: ${self.daily_pnl:.2f}')

    def is_trading_hours(self):
        """Check if current time is within London/NY Overlap (13:00-17:00 GMT)"""
        if not self.params.use_time_filter:
            return True
            
        try:
            dt = self.datas[0].datetime.datetime(0)
            hour = dt.hour
            return self.params.trade_start_hour <= hour < self.params.trade_end_hour
        except (IndexError, AttributeError):
            return False

    def next(self):
        # --- RISK MANAGEMENT ---
        
        # Permanent drawdown check
        current_equity = self.broker.getvalue()
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity
            
        drawdown_pct = (self.peak_equity - current_equity) / self.peak_equity
        if drawdown_pct > self.params.max_drawdown_percent:
            self.log(f"!!! MAX DRAWDOWN {drawdown_pct*100:.2f}% - HALTING !!!")
            if self.position:
                self.close()
            return

        # Daily reset
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date

        # Daily loss check
        if self.daily_pnl <= -self.params.max_daily_loss:
            return

        # Daily trade limit
        if self.daily_trades >= self.params.max_daily_trades:
            return
            
        # Skip if pending order or in position
        if self.order or self.position:
            return
            
        # --- TIME FILTER ---
        if not self.is_trading_hours():
            return

        # --- ENTRY LOGIC: Mean Reversion ---
        
        price = self.data.close[0]
        lower_bb = self.bb.lines.bot[0]
        upper_bb = self.bb.lines.top[0]
        mid_bb = self.bb.lines.mid[0]
        rsi_val = self.rsi[0]
        stoch_k = self.stoch.percK[0]
        stoch_d = self.stoch.percD[0]
        atr_val = self.atr[0]
        
        # LONG: Price below Lower BB + RSI oversold + Optional Stoch crossover
        long_bb = price < lower_bb
        long_rsi = rsi_val < self.params.rsi_oversold
        if self.params.require_stoch_crossover:
            long_stoch = (self.stoch_cross_up > 0 and 
                          stoch_k < self.params.stoch_oversold and 
                          stoch_d < self.params.stoch_oversold)
        else:
            # Relaxed mode: just check stoch is in oversold zone
            long_stoch = stoch_k < self.params.stoch_oversold
        
        long_signal = long_bb and long_rsi and long_stoch
        
        # SHORT: Price above Upper BB + RSI overbought + Optional Stoch crossover
        short_bb = price > upper_bb
        short_rsi = rsi_val > self.params.rsi_overbought
        if self.params.require_stoch_crossover:
            short_stoch = (self.stoch_cross_up < 0 and 
                           stoch_k > self.params.stoch_overbought and 
                           stoch_d > self.params.stoch_overbought)
        else:
            # Relaxed mode: just check stoch is in overbought zone
            short_stoch = stoch_k > self.params.stoch_overbought
        
        short_signal = short_bb and short_rsi and short_stoch
        
        # Calculate position sizing
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        sl_distance = atr_val * self.params.atr_sl_multiplier
        
        if sl_distance <= 0:
            return
            
        # Lots = Risk$ / (SL_Distance * ContractSize)
        raw_size = risk_amount / (sl_distance * self.params.contract_size)
        size = round(raw_size, 2)
        
        if size > self.params.max_lots:
            size = self.params.max_lots
            
        if size <= 0:
            return
        
        # Execute LONG
        if long_signal:
            entry_price = price
            sl_price = entry_price - sl_distance
            tp_price = mid_bb  # Target = Middle BB (Mean)
            
            self.log(f'MEAN REV LONG: Price {price:.2f} < LowerBB {lower_bb:.2f}, RSI={rsi_val:.1f}')
            self.log(f'  Entry: {entry_price:.2f}, SL: {sl_price:.2f}, TP: {tp_price:.2f}, Size: {size}')
            
            self.buy_bracket(
                size=size,
                exectype=bt.Order.Market,
                stopprice=sl_price,
                limitprice=tp_price
            )
            self.daily_trades += 1
            
        # Execute SHORT
        elif short_signal:
            entry_price = price
            sl_price = entry_price + sl_distance
            tp_price = mid_bb  # Target = Middle BB (Mean)
            
            self.log(f'MEAN REV SHORT: Price {price:.2f} > UpperBB {upper_bb:.2f}, RSI={rsi_val:.1f}')
            self.log(f'  Entry: {entry_price:.2f}, SL: {sl_price:.2f}, TP: {tp_price:.2f}, Size: {size}')
            
            self.sell_bracket(
                size=size,
                exectype=bt.Order.Market,
                stopprice=sl_price,
                limitprice=tp_price
            )
            self.daily_trades += 1

    # TradeLocker metadata for UI
    params_metadata = {
        "bb_period": {
            "label": "Bollinger Period",
            "helper_text": "Period for Bollinger Bands (default: 20)",
            "value_type": "int",
        },
        "bb_dev": {
            "label": "Bollinger Deviation",
            "helper_text": "Standard deviation multiplier (default: 2.0)",
            "value_type": "float",
        },
        "rsi_period": {
            "label": "RSI Period",
            "helper_text": "Period for RSI indicator (default: 14)",
            "value_type": "int",
        },
        "risk_per_trade_percent": {
            "label": "Risk Per Trade (%)",
            "helper_text": "Percentage of equity to risk per trade (default: 0.01 = 1%)",
            "value_type": "float",
        },
        "use_time_filter": {
            "label": "Use Time Filter",
            "helper_text": "Only trade during London/NY Overlap (13:00-17:00 GMT)",
            "value_type": "bool",
        },
    }
