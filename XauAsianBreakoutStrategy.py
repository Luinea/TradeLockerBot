"""
XAU/USD Asian Range Breakout Strategy.

This strategy respects Gold's market structure:
1. Asian Session (01:00-08:00 GMT): Low volatility, defines the "box"
2. London/NY (08:00-17:00 GMT): High volatility, trades breakouts

Logic:
- Phase 1 (Asia): Record highest high and lowest low of the session
- Phase 2 (London/NY): Trade breakouts of this range, filtered by EMA50 trend
- End of Day: Close all positions at 22:00 GMT

Why this works better than complex filtering:
- Avoids "chop" naturally (price stays in range = no trades)
- Catches the London Open momentum (most profitable time for Gold)
- Simple trend filter prevents fakeouts
"""

import backtrader as bt
import datetime


class XauAsianBreakoutStrategy(bt.Strategy):
    """
    Gold Asian Range Breakout Strategy.
    
    Logic:
    1. Define Asian Session (01:00 - 08:00 GMT).
    2. Record High and Low of this session (the "Box").
    3. London/NY Session (08:00 - 17:00):
       - BUY if Price closes ABOVE Asian High (and Price > EMA 50).
       - SELL if Price closes BELOW Asian Low (and Price < EMA 50).
    4. Cancels pending signals at end of day (22:00).
    """

    params = (
        # === EMA TREND FILTER ===
        ("ema_period", 50),
        
        # === SESSION TIMES (GMT) ===
        ("asian_start", 1),    # 01:00 GMT - Range starts
        ("asian_end", 8),      # 08:00 GMT - Range definition ends
        ("trade_start", 8),    # 08:00 GMT - Trading begins (London Open)
        ("trade_end", 17),     # 17:00 GMT - No new entries after NY afternoon
        ("session_end", 22),   # 22:00 GMT - Close all trades
        
        # === BREAKOUT BUFFER ===
        ("breakout_buffer", 0.5),  # Minimum pips above/below range for valid breakout
        
        # === RISK MANAGEMENT ===
        ("atr_period", 14),
        ("sl_atr_mult", 1.5),  # Stop Loss distance (ATR multiplier)
        ("tp_atr_mult", 3.0),  # Take Profit (higher RR for breakout)
        ("risk_per_trade", 0.02),  # 2% risk per trade
        ("max_lots", 0.5),
        ("contract_size", 100),
        
        # === DAILY LIMITS ===
        ("max_daily_trades", 2),  # Only 2 trades per day (one long, one short max)
        ("max_daily_loss", 100.0),  # $100 max daily loss
    )

    def __init__(self):
        # === INDICATORS ===
        self.ema = bt.indicators.EMA(self.data.close, period=self.params.ema_period)
        self.atr = bt.indicators.ATR(self.data, period=self.params.atr_period)
        
        # === RANGE TRACKING ===
        self.range_high = None
        self.range_low = None
        self.range_formed = False
        self.range_date = None  # Track which day the range belongs to
        
        # === TRADE TRACKING ===
        self.order = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.traded_long_today = False
        self.traded_short_today = False

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.datetime(0)
        print(f'{dt}: {txt}')

    def start(self):
        print("XAU Asian Breakout Strategy Started")

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status == order.Completed:
            action = 'BUY' if order.isbuy() else 'SELL'
            self.log(f'{action} EXECUTED @ {order.executed.price:.2f}, Size: {order.executed.size:.2f}')
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log(f'TRADE PROFIT: ${trade.pnlcomm:.2f}')
        self.daily_pnl += trade.pnlcomm

    def next(self):
        if self.order:
            return  # Pending order exists
        
        current_dt = self.datas[0].datetime.datetime(0)
        current_hour = current_dt.hour
        current_minute = current_dt.minute
        current_date = current_dt.date()
        price = self.data.close[0]
        
        # === DAILY RESET ===
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date
            self.traded_long_today = False
            self.traded_short_today = False
            self.range_formed = False
            self.range_high = None
            self.range_low = None
        
        # === CHECK DAILY LIMITS ===
        if self.daily_pnl <= -self.params.max_daily_loss:
            return
        if self.daily_trades >= self.params.max_daily_trades:
            return
        
        # ========================================
        # PHASE 1: DEFINE ASIAN RANGE (01:00 - 08:00)
        # ========================================
        if self.params.asian_start <= current_hour < self.params.asian_end:
            # Initialize range at start of Asian session
            if self.range_high is None:
                self.range_high = self.data.high[0]
                self.range_low = self.data.low[0]
                self.range_date = current_date
            else:
                # Update High/Low as session progresses
                self.range_high = max(self.range_high, self.data.high[0])
                self.range_low = min(self.range_low, self.data.low[0])
        
        # Mark range as complete at 08:00
        if current_hour == self.params.asian_end and not self.range_formed:
            if self.range_high is not None and self.range_low is not None:
                self.range_formed = True
                range_size = self.range_high - self.range_low
                self.log(f"RANGE FORMED: High={self.range_high:.2f}, Low={self.range_low:.2f}, Size={range_size:.2f}")
        
        # ========================================
        # PHASE 2: TRADE BREAKOUTS (08:00 - 17:00)
        # ========================================
        if self.range_formed and self.params.trade_start <= current_hour < self.params.trade_end:
            
            # Skip if already in position
            if self.position:
                return
            
            buffer = self.params.breakout_buffer
            
            # === BUY BREAKOUT ===
            # 1. Price closes above Asian High + buffer
            # 2. Trend is Bullish (Price > EMA 50)
            # 3. Haven't already taken a long today
            if price > (self.range_high + buffer) and price > self.ema[0]:
                if not self.traded_long_today:
                    self.entry_trade('LONG')
            
            # === SELL BREAKOUT ===
            # 1. Price closes below Asian Low - buffer
            # 2. Trend is Bearish (Price < EMA 50)
            # 3. Haven't already taken a short today
            elif price < (self.range_low - buffer) and price < self.ema[0]:
                if not self.traded_short_today:
                    self.entry_trade('SHORT')
        
        # ========================================
        # PHASE 3: END OF DAY CLEANUP (22:00)
        # ========================================
        if current_hour >= self.params.session_end:
            if self.position:
                self.log("END OF DAY: Closing position")
                self.close()
            self.range_formed = False

    def entry_trade(self, direction):
        """Execute a breakout trade with proper position sizing."""
        # Calculate Stop Loss and Take Profit distances
        sl_dist = self.atr[0] * self.params.sl_atr_mult
        tp_dist = self.atr[0] * self.params.tp_atr_mult
        
        if sl_dist <= 0:
            return
        
        # Calculate Position Size based on Risk
        equity = self.broker.getvalue()
        risk_amt = equity * self.params.risk_per_trade
        
        # Size = Risk / (SL_Distance * Contract_Size)
        size = risk_amt / (sl_dist * self.params.contract_size)
        size = round(min(size, self.params.max_lots), 2)
        
        if size <= 0.01:
            return
        
        price = self.data.close[0]
        
        if direction == 'LONG':
            sl_price = price - sl_dist
            tp_price = price + tp_dist
            self.log(f"BUY BREAKOUT: Price={price:.2f} > RangeHigh={self.range_high:.2f}")
            self.log(f"  Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}")
            # Use Market order for entry (TradeLocker requirement)
            self.order = self.buy_bracket(
                size=size,
                exectype=bt.Order.Market,  # Entry must be Market, not Limit
                limitprice=tp_price,
                stopprice=sl_price
            )
            self.traded_long_today = True
            self.daily_trades += 1
            
        elif direction == 'SHORT':
            sl_price = price + sl_dist
            tp_price = price - tp_dist
            self.log(f"SELL BREAKOUT: Price={price:.2f} < RangeLow={self.range_low:.2f}")
            self.log(f"  Entry={price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}, Size={size}")
            # Use Market order for entry (TradeLocker requirement)
            self.order = self.sell_bracket(
                size=size,
                exectype=bt.Order.Market,  # Entry must be Market, not Limit
                limitprice=tp_price,
                stopprice=sl_price
            )
            self.traded_short_today = True
            self.daily_trades += 1

    # TradeLocker UI metadata
    params_metadata = {
        "ema_period": {
            "label": "EMA Trend Filter Period",
            "helper_text": "EMA period for trend confirmation (default: 50)",
            "value_type": "int",
        },
        "asian_start": {
            "label": "Asian Session Start",
            "helper_text": "Hour (GMT) when Asian range measurement starts",
            "value_type": "int",
        },
        "asian_end": {
            "label": "Asian Session End",
            "helper_text": "Hour (GMT) when range is finalized and trading begins",
            "value_type": "int",
        },
        "risk_per_trade": {
            "label": "Risk Per Trade (%)",
            "helper_text": "Percentage of equity to risk per trade (default: 0.02 = 2%)",
            "value_type": "float",
        },
        "tp_atr_mult": {
            "label": "Take Profit (ATR Multiple)",
            "helper_text": "TP distance as multiple of ATR (default: 3.0 for 1:3 RR)",
            "value_type": "float",
        },
    }
