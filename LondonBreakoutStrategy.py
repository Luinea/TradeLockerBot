import backtrader as bt
import datetime

class LondonBreakoutStrategy(bt.Strategy):
    """
    London Breakout Strategy for XAUUSD.
    Captures volatility at London Open (08:00 GMT) by trading breakouts of the Asian Session (00:00-08:00).
    """
    
    params = (
        ("asian_start_hour", 0),
        ("asian_end_hour", 8),
        ("trade_end_hour", 20),
        
        # Risk Limits (FundedHero)
        ("risk_per_trade_percent", 0.01),
        ("max_daily_trades", 3),
        ("max_daily_loss", 75.0),
        ("max_drawdown_percent", 0.06), # 6% Hard Stop
        ("max_lots", 0.5),
        
        # Symbol specifics
        ("contract_size", 100),
        ("tp_risk_reward", 2.0),
    )

    def __init__(self):
        self.order = None
        self.daily_trades = 0
        self.daily_pnl = 0.0
        self.last_trade_date = None
        self.daily_peak_equity = 0.0  # Changed: daily reset instead of permanent
        
        # Range tracking
        self.asian_high = -1.0
        self.asian_low = 999999.0
        self.range_established = False
        # Previous day's range (fallback for 30m timeframe)
        self.prev_asian_high = -1.0
        self.prev_asian_low = 999999.0

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
        self.log("London Breakout Strategy Started")
        self.daily_peak_equity = self.broker.getvalue()

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

    def next(self):
        # --- DAILY RESET ---
        current_date = self.datas[0].datetime.date(0)
        if self.last_trade_date != current_date:
            self.daily_trades = 0
            self.daily_pnl = 0.0
            self.last_trade_date = current_date
            # Reset drawdown tracking daily (allows recovery)
            self.daily_peak_equity = self.broker.getvalue()
            # Save previous day's range (fallback for 30m timeframe)
            if self.asian_high > 0:  # Only save if we had a valid range
                self.prev_asian_high = self.asian_high
                self.prev_asian_low = self.asian_low
            # Reset range for new day
            self.asian_high = -1.0
            self.asian_low = 999999.0
            self.range_established = False
        
        # --- DAILY RISK MANAGEMENT ---
        current_equity = self.broker.getvalue()
        
        # Update daily peak
        if current_equity > self.daily_peak_equity:
            self.daily_peak_equity = current_equity
            
        # Calculate daily drawdown
        daily_drawdown_pct = (self.daily_peak_equity - current_equity) / self.daily_peak_equity
        
        # Daily drawdown limit (stop trading for the day)
        if daily_drawdown_pct > self.params.max_drawdown_percent:
            self.log(f"Daily Drawdown {daily_drawdown_pct*100:.2f}% exceeds limit. Stopping for today.")
            if self.position: self.close()
            if self.order: self.broker.cancel(self.order)
            return

        # Daily loss limit
        if self.daily_pnl <= -self.params.max_daily_loss:
            return # Daily Stop

        # --- STRATEGY LOGIC ---
        dt = self.datas[0].datetime.datetime(0)
        hour = dt.hour
        price = self.data.close[0]

        # 1. Asian Session (Range Building)
        if hour >= self.params.asian_start_hour and hour < self.params.asian_end_hour:
            if price > self.asian_high: self.asian_high = price
            if price < self.asian_low: self.asian_low = price
            self.range_established = True
            
        # 2. London Session (Trading)
        elif hour >= self.params.asian_end_hour and hour < self.params.trade_end_hour:
            # Fallback: Use previous day's range if current day has no Asian session bars (30m timeframe issue)
            if not self.range_established and self.prev_asian_high > 0:
                self.asian_high = self.prev_asian_high
                self.asian_low = self.prev_asian_low
                self.range_established = True
                self.log(f"Using previous day's Asian range: High={self.asian_high:.2f}, Low={self.asian_low:.2f}")
            
            if not self.range_established:
                return
                
            # Only block if we have a meaningful position (prevent tiny residual positions from blocking trading)
            if self.order or (self.position and abs(self.position.size) >= 0.01):
                return
                
            if self.daily_trades >= self.params.max_daily_trades:
                return
            
            # Entry Logic
            if self.asian_high == -1: return 
            
            # BUY Breakout
            if price > self.asian_high:
                # Calculate Risk (SL at Mid-Range)
                sl_price = (self.asian_high + self.asian_low) / 2
                sl_dist = price - sl_price
                if sl_dist <= 0: return 
                
                tp_dist = sl_dist * self.params.tp_risk_reward
                tp_price = price + tp_dist
                
                risk_amt = self.broker.getvalue() * self.params.risk_per_trade_percent
                size = round(risk_amt / (sl_dist * self.params.contract_size), 2)
                if size > self.params.max_lots: size = self.params.max_lots
                
                if size > 0:
                    self.log(f'BREAKOUT BUY: Price {price:.2f} > Asian High {self.asian_high:.2f}')
                    self.buy_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                    self.daily_trades += 1

            # SELL Breakout
            elif price < self.asian_low:
                # Calculate Risk (SL at Mid-Range)
                sl_price = (self.asian_high + self.asian_low) / 2
                sl_dist = sl_price - price
                if sl_dist <= 0: return
                
                tp_dist = sl_dist * self.params.tp_risk_reward
                tp_price = price - tp_dist
                
                risk_amt = self.broker.getvalue() * self.params.risk_per_trade_percent
                size = round(risk_amt / (sl_dist * self.params.contract_size), 2)
                if size > self.params.max_lots: size = self.params.max_lots
                
                if size > 0:
                    self.log(f'BREAKOUT SELL: Price {price:.2f} < Asian Low {self.asian_low:.2f}')
                    self.sell_bracket(size=size, exectype=bt.Order.Market, stopprice=sl_price, limitprice=tp_price)
                    self.daily_trades += 1
        
        # 3. End of Day (Close All)
        elif hour >= self.params.trade_end_hour:
            # Check if we have a meaningful position before closing
            # Prevents 0.0 lot orders from floating point errors
            if self.position and abs(self.position.size) >= 0.01:
                self.log("End of Day - Closing Positions")
                self.close()
            if self.order:
                self.broker.cancel(self.order)
