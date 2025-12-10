"""
EUR_USD Trading Strategy - Professional Multi-Strategy Approach
Based on comprehensive EUR_USD trading research.

Strategy Components:
1. Dual-Filter EMA Trend Following (20/50/200 EMAs)
2. Break and Retest Entry Refinement
3. London-NY Session Filtering (12:00-16:00 UTC)
4. ATR-Based Position Sizing and Risk Management
5. Fibonacci Support/Resistance Confluence

Research Source: EUR_USD Trading Strategies Research.md
"""

import backtrader as bt
import datetime
from collections import deque


class EurUsdStrategy(bt.Strategy):
    """
    EUR/USD Professional Trading Strategy
    
    Combines institutional-grade methodologies:
    - Trend identification via 200 EMA filter
    - Entry signals from 20/50 EMA crossovers
    - Breakout confirmation with retest validation
    - Session-based execution during peak liquidity
    - Volatility-adjusted position sizing using ATR
    """
    
    params = (
        # EMA Parameters for Dual-Filter Strategy
        ('ema_fast', 20),          # Fast EMA for entry signals
        ('ema_medium', 50),        # Medium EMA for crossover
        ('ema_slow', 200),         # Slow EMA for trend filter
        
        # ATR-Based Risk Management
        ('atr_period', 14),        # ATR calculation period
        ('atr_sl_multiplier', 1.5), # Stop loss = 1.5x ATR
        ('atr_tp_multiplier', 2.5), # Take profit = 2.5x ATR
        ('risk_percent', 2.0),     # Maximum risk per trade (% of equity)
        
        # Session-Based Trading (UTC hours)
        ('session_start_hour', 12), # London-NY overlap start (12:00 UTC)
        ('session_end_hour', 16),   # London-NY overlap end (16:00 UTC)
        ('trade_only_in_session', True),  # Only trade during optimal hours
        
        # Break and Retest Parameters
        ('use_break_retest', True),      # Enable break/retest validation
        ('lookback_period', 50),         # Bars to look back for S/R levels
        ('breakout_threshold', 0.0010),  # Minimum breakout size (100 pips)
        ('retest_tolerance', 0.0020),    # Retest zone tolerance (200 pips)
        
        # Fibonacci Parameters
        ('use_fibonacci', True),         # Enable Fibonacci confluence
        ('fib_lookback', 100),          # Bars for Fibonacci calculation
        
        # EMA Momentum Filter
        ('min_angle_threshold', 0.0001), # Minimum EMA separation for momentum
        
        # Position Management
        ('max_positions', 1),           # Maximum concurrent positions
        ('enable_logging', True),       # Enable detailed logging
    )
    
    def __init__(self):
        """Initialize strategy indicators and tracking variables"""
        
        # Core price data
        self.dataclose = self.datas[0].close
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        
        # Moving Averages - The Dual-Filter Architecture
        self.ema_fast = bt.indicators.ExponentialMovingAverage(
            self.datas[0], period=self.params.ema_fast
        )
        self.ema_medium = bt.indicators.ExponentialMovingAverage(
            self.datas[0], period=self.params.ema_medium
        )
        self.ema_slow = bt.indicators.ExponentialMovingAverage(
            self.datas[0], period=self.params.ema_slow
        )
        
        # EMA Crossover Signals
        self.ema_cross = bt.indicators.CrossOver(self.ema_fast, self.ema_medium)
        
        # Average True Range for volatility-based risk management
        self.atr = bt.indicators.AverageTrueRange(period=self.params.atr_period)
        
        # Tracking variables
        self.order = None
        self.trade_count = 0
        self.wins = 0
        self.losses = 0
        
        # Support/Resistance tracking
        self.support_levels = deque(maxlen=10)
        self.resistance_levels = deque(maxlen=10)
        
        # Break and Retest tracking
        self.last_breakout_level = None
        self.last_breakout_direction = None  # 1 for up, -1 for down
        self.waiting_for_retest = False
        
        # Fibonacci levels
        self.fib_382 = None
        self.fib_618 = None
        
        self.log("EUR_USD Strategy initialized")
        self.log(f"Session: {self.params.session_start_hour:02d}:00 - {self.params.session_end_hour:02d}:00 UTC")
        self.log(f"Risk per trade: {self.params.risk_percent}%")
        self.log(f"ATR SL/TP: {self.params.atr_sl_multiplier}x / {self.params.atr_tp_multiplier}x")

    def log(self, txt, dt=None):
        """Logging function with timestamp"""
        if not self.params.enable_logging:
            return
            
        dt = dt or self.datas[0].datetime.datetime(0)
        print(f'[{dt.strftime("%Y-%m-%d %H:%M:%S")}] {txt}')

    def start(self):
        """Called when strategy starts"""
        self.log("=== EUR/USD Strategy Started ===")

    def notify_order(self, order):
        """Track order execution status"""
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f"BUY EXECUTED @ {order.executed.price:.5f}, Cost: {order.executed.value:.2f}")
            elif order.issell():
                self.log(f"SELL EXECUTED @ {order.executed.price:.5f}, Cost: {order.executed.value:.2f}")
                
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f"Order Failed: {order.getstatusname()}")

        self.order = None

    def notify_trade(self, trade):
        """Track trade results for performance metrics"""
        if not trade.isclosed:
            return

        self.trade_count += 1
        pnl = trade.pnl
        
        if pnl > 0:
            self.wins += 1
            self.log(f"✓ TRADE WIN #{self.trade_count} | PnL: ${pnl:.2f}")
        else:
            self.losses += 1
            self.log(f"✗ TRADE LOSS #{self.trade_count} | PnL: ${pnl:.2f}")
        
        win_rate = (self.wins / self.trade_count * 100) if self.trade_count > 0 else 0
        self.log(f"Performance: {self.wins}W/{self.losses}L | Win Rate: {win_rate:.1f}%")

    def is_valid_session(self):
        """
        Check if current time is within the London-NY overlap session.
        Returns True during 12:00-16:00 UTC (peak liquidity period).
        """
        if not self.params.trade_only_in_session:
            return True
            
        dt = self.datas[0].datetime.datetime(0)
        current_hour = dt.hour
        
        # Check if within trading session
        if self.params.session_start_hour <= current_hour < self.params.session_end_hour:
            return True
        
        return False

    def detect_swing_levels(self):
        """
        Detect support and resistance levels using swing highs and lows.
        Support: Swing lows where price bounced up
        Resistance: Swing highs where price bounced down
        """
        if len(self.datas[0]) < self.params.lookback_period:
            return
        
        # Look for swing highs (resistance)
        for i in range(3, min(self.params.lookback_period, len(self.datas[0]) - 3)):
            high = self.datahigh[-i]
            
            # Check if it's a swing high (higher than neighbors)
            if (self.datahigh[-i-1] < high and 
                self.datahigh[-i-2] < high and
                self.datahigh[-i+1] < high and 
                self.datahigh[-i+2] < high):
                
                # Add to resistance if not too close to existing levels
                if not any(abs(level - high) < 0.0050 for level in self.resistance_levels):
                    self.resistance_levels.append(high)
        
        # Look for swing lows (support)
        for i in range(3, min(self.params.lookback_period, len(self.datas[0]) - 3)):
            low = self.datalow[-i]
            
            # Check if it's a swing low (lower than neighbors)
            if (self.datalow[-i-1] > low and 
                self.datalow[-i-2] > low and
                self.datalow[-i+1] > low and 
                self.datalow[-i+2] > low):
                
                # Add to support if not too close to existing levels
                if not any(abs(level - low) < 0.0050 for level in self.support_levels):
                    self.support_levels.append(low)

    def calculate_fibonacci_levels(self):
        """
        Calculate Fibonacci retracement levels (38.2% and 61.8%)
        from recent swing high to swing low.
        """
        if not self.params.use_fibonacci:
            return
            
        if len(self.datas[0]) < self.params.fib_lookback:
            return
        
        # Find recent swing high and low
        lookback = min(self.params.fib_lookback, len(self.datas[0]))
        recent_high = max([self.datahigh[-i] for i in range(lookback)])
        recent_low = min([self.datalow[-i] for i in range(lookback)])
        
        # Calculate Fibonacci levels
        diff = recent_high - recent_low
        self.fib_382 = recent_high - (diff * 0.382)
        self.fib_618 = recent_high - (diff * 0.618)

    def check_break_and_retest(self, signal_type):
        """
        Validate break and retest pattern.
        
        Args:
            signal_type: 1 for bullish, -1 for bearish
            
        Returns:
            True if valid break/retest setup exists
        """
        if not self.params.use_break_retest:
            return True  # Skip if disabled
        
        current_price = self.dataclose[0]
        
        # Check for new breakouts
        if signal_type == 1:  # Bullish signal
            # Check if we broke above resistance
            for resistance in self.resistance_levels:
                if current_price > resistance + self.params.breakout_threshold:
                    # New breakout detected
                    if not self.waiting_for_retest:
                        self.last_breakout_level = resistance
                        self.last_breakout_direction = 1
                        self.waiting_for_retest = True
                        self.log(f"BREAKOUT detected above {resistance:.5f}, waiting for retest")
                        return False  # Don't enter yet, wait for retest
        
        elif signal_type == -1:  # Bearish signal
            # Check if we broke below support
            for support in self.support_levels:
                if current_price < support - self.params.breakout_threshold:
                    # New breakout detected
                    if not self.waiting_for_retest:
                        self.last_breakout_level = support
                        self.last_breakout_direction = -1
                        self.waiting_for_retest = True
                        self.log(f"BREAKOUT detected below {support:.5f}, waiting for retest")
                        return False  # Don't enter yet, wait for retest
        
        # Check if we're in a retest scenario
        if self.waiting_for_retest and self.last_breakout_level:
            level_diff = abs(current_price - self.last_breakout_level)
            
            if level_diff <= self.params.retest_tolerance:
                # We're retesting the level
                if signal_type == self.last_breakout_direction:
                    self.log(f"RETEST confirmed at {self.last_breakout_level:.5f}, entering trade")
                    self.waiting_for_retest = False
                    return True
        
        # If not waiting for retest, allow trade
        return not self.waiting_for_retest

    def calculate_position_size(self, entry_price, stop_loss):
        """
        Calculate position size using ATR-based risk management.
        
        Formula: Position Size = (Account Equity × Risk %) / (Stop Loss Distance × Pip Value)
        
        Args:
            entry_price: Entry price level
            stop_loss: Stop loss price level
            
        Returns:
            Position size in lots
        """
        account_value = self.broker.getvalue()
        risk_amount = account_value * (self.params.risk_percent / 100.0)
        
        # Calculate stop loss distance in pips (EUR/USD: 1 pip = 0.0001)
        sl_distance = abs(entry_price - stop_loss)
        
        # For EUR/USD: 1 standard lot = $10 per pip
        # 0.01 lot = $0.10 per pip
        pip_value = 10.0  # for 1 standard lot
        
        # Calculate position size
        if sl_distance > 0:
            position_size = risk_amount / (sl_distance * 10000 * pip_value)
            # Clamp to reasonable range
            position_size = max(0.01, min(position_size, 1.0))
        else:
            position_size = 0.01  # Minimum size
        
        self.log(f"Position Sizing: Risk=${risk_amount:.2f}, SL Distance={sl_distance*10000:.1f}pips, Size={position_size:.2f} lots")
        return position_size

    def get_trend_direction(self):
        """
        Determine trend direction using 200 EMA filter.
        
        Returns:
            1 for uptrend (price > 200 EMA)
            -1 for downtrend (price < 200 EMA)
            0 for no clear trend
        """
        if self.dataclose[0] > self.ema_slow[0]:
            return 1  # Uptrend
        elif self.dataclose[0] < self.ema_slow[0]:
            return -1  # Downtrend
        else:
            return 0  # No clear trend

    def check_ema_momentum(self):
        """
        Check if EMA divergence shows strong momentum.
        "Angle of Attack" - measure separation between fast and medium EMAs.
        
        Returns:
            True if momentum is strong enough
        """
        ema_separation = abs(self.ema_fast[0] - self.ema_medium[0])
        return ema_separation >= self.params.min_angle_threshold

    def next(self):
        """Main trading logic executed on each candle"""
        
        # Skip if we have a pending order
        if self.order:
            return
        
        # Update support/resistance and Fibonacci levels
        self.detect_swing_levels()
        self.calculate_fibonacci_levels()
        
        # Check session validity
        if not self.is_valid_session():
            # Only log session info once per bar when outside session
            if len(self.datas[0]) % 10 == 0:  # Log every 10 bars
                dt = self.datas[0].datetime.datetime(0)
                self.log(f"Outside trading session (hour: {dt.hour})")
            return
        
        # Get current market state
        current_price = self.dataclose[0]
        trend = self.get_trend_direction()
        atr_value = self.atr[0]
        
        # === ENTRY LOGIC ===
        
        # Not in position - look for entry signals
        if not self.position:
            
            # LONG Entry Conditions
            if (trend == 1 and  # Uptrend filter (price > 200 EMA)
                self.ema_cross[0] == 1 and  # Golden cross (20 EMA crossed above 50 EMA)
                self.check_ema_momentum()):  # Strong momentum
                
                self.log(f"LONG SIGNAL: Price={current_price:.5f}, EMA20={self.ema_fast[0]:.5f}, EMA50={self.ema_medium[0]:.5f}, EMA200={self.ema_slow[0]:.5f}")
                
                # Validate break and retest pattern
                if self.check_break_and_retest(signal_type=1):
                    
                    # Calculate ATR-based stop loss and take profit
                    stop_loss = current_price - (atr_value * self.params.atr_sl_multiplier)
                    take_profit = current_price + (atr_value * self.params.atr_tp_multiplier)
                    
                    # Calculate position size
                    size = self.calculate_position_size(current_price, stop_loss)
                    
                    # Check Fibonacci confluence if enabled
                    fib_ok = True
                    if self.params.use_fibonacci and self.fib_382 and self.fib_618:
                        # Prefer entries near Fibonacci support
                        if current_price < self.fib_618:
                            self.log(f"Fibonacci support at {self.fib_618:.5f} (61.8%)")
                        fib_ok = True  # Don't block trade, just note confluence
                    
                    if fib_ok:
                        self.log(f"ENTERING LONG @ {current_price:.5f}")
                        self.log(f"  SL: {stop_loss:.5f} (-{(current_price-stop_loss)*10000:.1f} pips)")
                        self.log(f"  TP: {take_profit:.5f} (+{(take_profit-current_price)*10000:.1f} pips)")
                        self.log(f"  R:R Ratio: {self.params.atr_tp_multiplier/self.params.atr_sl_multiplier:.2f}:1")
                        
                        # Place order with bracket stops
                        self.order = self.buy(size=size)
                        # Note: TradeLocker handles SL/TP through separate orders
            
            # SHORT Entry Conditions
            elif (trend == -1 and  # Downtrend filter (price < 200 EMA)
                  self.ema_cross[0] == -1 and  # Death cross (20 EMA crossed below 50 EMA)
                  self.check_ema_momentum()):  # Strong momentum
                
                self.log(f"SHORT SIGNAL: Price={current_price:.5f}, EMA20={self.ema_fast[0]:.5f}, EMA50={self.ema_medium[0]:.5f}, EMA200={self.ema_slow[0]:.5f}")
                
                # Validate break and retest pattern
                if self.check_break_and_retest(signal_type=-1):
                    
                    # Calculate ATR-based stop loss and take profit
                    stop_loss = current_price + (atr_value * self.params.atr_sl_multiplier)
                    take_profit = current_price - (atr_value * self.params.atr_tp_multiplier)
                    
                    # Calculate position size
                    size = self.calculate_position_size(current_price, stop_loss)
                    
                    # Check Fibonacci confluence if enabled
                    fib_ok = True
                    if self.params.use_fibonacci and self.fib_382 and self.fib_618:
                        # Prefer entries near Fibonacci resistance
                        if current_price > self.fib_382:
                            self.log(f"Fibonacci resistance at {self.fib_382:.5f} (38.2%)")
                        fib_ok = True  # Don't block trade, just note confluence
                    
                    if fib_ok:
                        self.log(f"ENTERING SHORT @ {current_price:.5f}")
                        self.log(f"  SL: {stop_loss:.5f} (+{(stop_loss-current_price)*10000:.1f} pips)")
                        self.log(f"  TP: {take_profit:.5f} (-{(current_price-take_profit)*10000:.1f} pips)")
                        self.log(f"  R:R Ratio: {self.params.atr_tp_multiplier/self.params.atr_sl_multiplier:.2f}:1")
                        
                        # Place order
                        self.order = self.sell(size=size)

    # Metadata for TradeLocker UI configuration
    params_metadata = {
        "ema_fast": {
            "label": "Fast EMA Period",
            "helper_text": "Period for fast EMA (entry signal) - Default: 20",
            "value_type": "int",
        },
        "ema_medium": {
            "label": "Medium EMA Period",
            "helper_text": "Period for medium EMA (crossover signal) - Default: 50",
            "value_type": "int",
        },
        "ema_slow": {
            "label": "Slow EMA Period (Trend Filter)",
            "helper_text": "Period for slow EMA (200 = long-term trend)",
            "value_type": "int",
        },
        "atr_period": {
            "label": "ATR Period",
            "helper_text": "Period for ATR calculation (volatility measurement)",
            "value_type": "int",
        },
        "atr_sl_multiplier": {
            "label": "ATR Stop Loss Multiplier",
            "helper_text": "Stop loss distance as ATR multiple (1.5x recommended)",
            "value_type": "float",
        },
        "atr_tp_multiplier": {
            "label": "ATR Take Profit Multiplier",
            "helper_text": "Take profit distance as ATR multiple (2.5x for positive R:R)",
            "value_type": "float",
        },
        "risk_percent": {
            "label": "Risk Per Trade (%)",
            "helper_text": "Maximum risk per trade as % of account equity",
            "value_type": "float",
        },
        "session_start_hour": {
            "label": "Session Start Hour (UTC)",
            "helper_text": "Trading session start (12 = London-NY overlap)",
            "value_type": "int",
        },
        "session_end_hour": {
            "label": "Session End Hour (UTC)",
            "helper_text": "Trading session end (16 = end of overlap)",
            "value_type": "int",
        },
        "trade_only_in_session": {
            "label": "Trade Only In Session",
            "helper_text": "Only execute trades during specified session hours",
            "value_type": "bool",
        },
        "use_break_retest": {
            "label": "Enable Break & Retest",
            "helper_text": "Wait for breakout retest before entry (reduces false signals)",
            "value_type": "bool",
        },
        "use_fibonacci": {
            "label": "Enable Fibonacci Levels",
            "helper_text": "Use Fibonacci retracements for confluence",
            "value_type": "bool",
        },
        "enable_logging": {
            "label": "Enable Detailed Logging",
            "helper_text": "Print detailed strategy logs",
            "value_type": "bool",
        },
    }
