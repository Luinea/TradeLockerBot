# TradeLocker XAUUSD Multi-Factor Confluence Strategy
# Designed for FundedHero $2.5K Challenge
# Uses Backtrader framework for backtesting

import backtrader as bt
from datetime import datetime, time
from enum import Enum


class MarketRegime(Enum):
    """Market regime classification"""
    TRENDING = "TRENDING"
    RANGING = "RANGING"
    NEUTRAL = "NEUTRAL"


class TrendDirection(Enum):
    """Trend direction from higher timeframe"""
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    NEUTRAL = "NEUTRAL"


class XAUUSDStrategy(bt.Strategy):
    """
    Multi-factor confluence strategy for XAUUSD backtesting.
    
    Features:
    - Regime detection (ADX + ATR ratio + MA slope)
    - Multi-timeframe analysis (4H trend + 15M entries)
    - Risk management per FundedHero trading plan
    - Consistency rule tracking
    """
    
    params = {
        # Account & Risk Parameters
        "account_size": 2500,
        "risk_percent": 1.0,          # 1% per trade = $25
        "max_daily_loss": 75,         # 3% self-imposed daily stop
        "max_trades_per_day": 3,
        
        # Lot Size Limits (for consistency rule)
        "min_lots": 0.03,
        "max_lots": 0.12,
        
        # Regime Detection Parameters
        "adx_period": 14,
        "adx_trending_threshold": 25,
        "adx_ranging_threshold": 20,
        "atr_period": 14,
        "atr_lookback": 20,
        "atr_trending_ratio": 1.2,
        "atr_ranging_ratio": 0.8,
        
        # Entry Indicator Parameters  
        "rsi_period": 14,
        "rsi_oversold": 30,
        "rsi_overbought": 70,
        "rsi_pullback_long": 40,
        "rsi_pullback_short": 60,
        "ema_fast": 21,
        "ema_slow": 50,
        "ema_trend": 200,
        
        # Exit Parameters
        "trailing_atr_multiplier": 1.5,
        "trailing_activation_r": 1.0,   # Activate after 1R profit
        
        # Key Level Parameters
        "round_number_proximity": 5.0,   # Within $5 of round number
        "prev_day_proximity": 3.0,       # Within $3 of prev day H/L
        
        # Gold-specific
        "point_value": 100,              # $1 move per 1 lot = $100
    }
    
    # TradeLocker params_metadata for UI
    params_metadata = {
        "account_size": {
            "label": "Account Size ($)",
            "helper_text": "Starting account balance",
            "value_type": "float",
        },
        "risk_percent": {
            "label": "Risk per Trade (%)",
            "helper_text": "Percentage of account to risk per trade (0.5-1.0)",
            "value_type": "float",
        },
        "max_daily_loss": {
            "label": "Max Daily Loss ($)",
            "helper_text": "Stop trading if daily loss exceeds this",
            "value_type": "float",
        },
        "max_trades_per_day": {
            "label": "Max Trades per Day",
            "helper_text": "Maximum number of trades allowed per day",
            "value_type": "int",
        },
    }
    
    def __init__(self) -> None:
        """Initialize indicators and state tracking"""
        self.order = None
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        self.trailing_active = False
        
        # Daily tracking
        self.current_date = None
        self.daily_pnl = 0.0
        self.daily_trades = 0
        self.daily_profits = {}  # date -> profit for consistency rule
        
        # Consistency rule tracking
        self.total_profit = 0.0
        self.best_day_profit = 0.0
        self.consistency_violations = []
        
        # ===== 15M (Primary) Timeframe Indicators =====
        self.close = self.datas[0].close
        self.high = self.datas[0].high
        self.low = self.datas[0].low
        
        # RSI for entry timing
        self.rsi = bt.indicators.RSI(
            self.datas[0], 
            period=self.params.rsi_period
        )
        
        # EMAs for pullback detection
        self.ema_fast = bt.indicators.EMA(
            self.datas[0], 
            period=self.params.ema_fast
        )
        
        # ADX for regime detection
        self.adx = bt.indicators.ADX(
            self.datas[0], 
            period=self.params.adx_period
        )
        
        # ATR for volatility and stop placement
        self.atr = bt.indicators.ATR(
            self.datas[0], 
            period=self.params.atr_period
        )
        
        # SMA of ATR for ratio calculation
        self.atr_sma = bt.indicators.SMA(
            self.atr, 
            period=self.params.atr_lookback
        )
        
        # EMA slope (using EMA difference)
        self.ema_slow_15m = bt.indicators.EMA(
            self.datas[0], 
            period=self.params.ema_slow
        )
        
        # ===== 4H (Secondary) Timeframe Indicators =====
        # Note: Requires adding 4H data feed with resampledata or replaydata
        if len(self.datas) > 1:
            self.ema_50_4h = bt.indicators.EMA(
                self.datas[1], 
                period=self.params.ema_slow
            )
            self.ema_200_4h = bt.indicators.EMA(
                self.datas[1], 
                period=self.params.ema_trend
            )
            self.close_4h = self.datas[1].close
            self.high_4h = self.datas[1].high
            self.low_4h = self.datas[1].low
        else:
            # Fallback: use longer EMAs on primary timeframe
            self.ema_50_4h = bt.indicators.EMA(
                self.datas[0], 
                period=self.params.ema_slow * 16  # 15M * 16 ≈ 4H
            )
            self.ema_200_4h = bt.indicators.EMA(
                self.datas[0], 
                period=self.params.ema_trend * 16
            )
            self.close_4h = self.close
            self.high_4h = self.high
            self.low_4h = self.low
        
        # Swing high/low tracking for S/R detection
        self.swing_high = bt.indicators.Highest(
            self.datas[0].high, 
            period=20
        )
        self.swing_low = bt.indicators.Lowest(
            self.datas[0].low, 
            period=20
        )
        
        # Previous day high/low
        self.prev_high = None
        self.prev_low = None
        self.day_high = None
        self.day_low = None
    
    def log(self, txt: str, dt=None) -> None:
        """Logging function for debugging"""
        dt = dt or self.datas[0].datetime.datetime(0)
        print(f"{dt.isoformat()} | {txt}")
    
    def detect_regime(self) -> MarketRegime:
        """
        Detect market regime using custom combination:
        - ADX for trend strength
        - ATR ratio for volatility expansion
        - EMA slope for directional bias
        
        Returns: MarketRegime enum
        """
        score = 0
        
        # Factor 1: ADX
        adx_value = self.adx[0]
        if adx_value > self.params.adx_trending_threshold:
            score += 1
        elif adx_value < self.params.adx_ranging_threshold:
            score -= 1
        
        # Factor 2: ATR Ratio
        if self.atr_sma[0] > 0:
            atr_ratio = self.atr[0] / self.atr_sma[0]
            if atr_ratio > self.params.atr_trending_ratio:
                score += 1
            elif atr_ratio < self.params.atr_ranging_ratio:
                score -= 1
        
        # Factor 3: EMA Slope (using 5-bar change)
        if len(self.ema_slow_15m) > 5:
            ema_slope = (self.ema_slow_15m[0] - self.ema_slow_15m[-5]) / 5
            slope_threshold = self.atr[0] * 0.01  # 1% of ATR
            if abs(ema_slope) > slope_threshold:
                score += 1
            elif abs(ema_slope) < slope_threshold * 0.5:
                score -= 1
        
        # Determine regime
        if score >= 2:
            return MarketRegime.TRENDING
        elif score <= -2:
            return MarketRegime.RANGING
        else:
            return MarketRegime.NEUTRAL
    
    def get_trend_direction(self) -> TrendDirection:
        """
        Determine trend direction from 4H timeframe.
        
        Returns: TrendDirection enum
        """
        price = self.close_4h[0]
        ema50 = self.ema_50_4h[0]
        ema200 = self.ema_200_4h[0]
        
        # Check for higher highs / lower lows (using 4H swing points)
        if len(self.datas) > 1:
            # Use actual 4H data
            recent_highs = [self.high_4h[-i] for i in range(min(5, len(self.high_4h)))]
            recent_lows = [self.low_4h[-i] for i in range(min(5, len(self.low_4h)))]
        else:
            recent_highs = [self.swing_high[-i] for i in range(min(5, len(self.swing_high)))]
            recent_lows = [self.swing_low[-i] for i in range(min(5, len(self.swing_low)))]
        
        higher_highs = all(recent_highs[i] >= recent_highs[i+1] for i in range(len(recent_highs)-1)) if len(recent_highs) > 1 else False
        lower_lows = all(recent_lows[i] <= recent_lows[i+1] for i in range(len(recent_lows)-1)) if len(recent_lows) > 1 else False
        
        # Bullish: Price > EMA50 > EMA200 + higher highs
        if price > ema50 > ema200 and higher_highs:
            return TrendDirection.BULLISH
        
        # Bearish: Price < EMA50 < EMA200 + lower lows
        if price < ema50 < ema200 and lower_lows:
            return TrendDirection.BEARISH
        
        return TrendDirection.NEUTRAL
    
    def is_near_key_level(self) -> bool:
        """
        Check if price is near a key level for confluence.
        Key levels: round numbers, previous day H/L
        """
        price = self.close[0]
        
        # Check round numbers (2600, 2650, 2700, etc.)
        round_50 = round(price / 50) * 50
        if abs(price - round_50) <= self.params.round_number_proximity:
            return True
        
        # Check previous day high/low
        if self.prev_high and self.prev_low:
            if abs(price - self.prev_high) <= self.params.prev_day_proximity:
                return True
            if abs(price - self.prev_low) <= self.params.prev_day_proximity:
                return True
        
        return False
    
    def calculate_lot_size(self, sl_distance: float) -> float:
        """
        Calculate position size based on risk management.
        
        Formula: Lot Size = Risk Amount / (SL in $ × 100)
        
        Args:
            sl_distance: Stop loss distance in price (e.g., $4.00)
        
        Returns:
            Lot size clipped to min/max limits
        """
        risk_amount = self.params.account_size * (self.params.risk_percent / 100)
        
        if sl_distance <= 0:
            return self.params.min_lots
        
        # Lot size calculation for gold
        lot_size = risk_amount / (sl_distance * self.params.point_value)
        
        # Enforce consistency limits
        lot_size = max(self.params.min_lots, min(self.params.max_lots, lot_size))
        
        # Round to 2 decimal places
        return round(lot_size, 2)
    
    def check_daily_limits(self) -> bool:
        """
        Check if trading is allowed based on daily limits.
        
        Returns:
            True if trading is allowed, False otherwise
        """
        # Check daily loss limit
        if self.daily_pnl <= -self.params.max_daily_loss:
            self.log(f"Daily loss limit reached: ${self.daily_pnl:.2f}")
            return False
        
        # Check max trades per day
        if self.daily_trades >= self.params.max_trades_per_day:
            self.log(f"Max trades per day reached: {self.daily_trades}")
            return False
        
        return True
    
    def check_entry_conditions(self) -> tuple:
        """
        Check all entry conditions for both regimes.
        
        Returns:
            (should_enter, direction, sl_distance)
        """
        regime = self.detect_regime()
        trend = self.get_trend_direction()
        
        # No trade in NEUTRAL regime or trend
        if regime == MarketRegime.NEUTRAL or trend == TrendDirection.NEUTRAL:
            return (False, None, 0)
        
        # Key level filter (optional but increases win rate)
        near_key_level = self.is_near_key_level()
        
        price = self.close[0]
        rsi = self.rsi[0]
        ema = self.ema_fast[0]
        atr = self.atr[0]
        
        # ===== TRENDING REGIME ENTRIES =====
        if regime == MarketRegime.TRENDING:
            
            # LONG: 4H bullish + pullback to EMA21 + RSI < 40
            if trend == TrendDirection.BULLISH:
                pullback_to_ema = abs(price - ema) < atr * 0.5
                rsi_condition = rsi < self.params.rsi_pullback_long
                
                if pullback_to_ema and rsi_condition:
                    sl_distance = atr * 1.5  # 1.5 ATR stop
                    return (True, "LONG", sl_distance)
            
            # SHORT: 4H bearish + pullback to EMA21 + RSI > 60
            elif trend == TrendDirection.BEARISH:
                pullback_to_ema = abs(price - ema) < atr * 0.5
                rsi_condition = rsi > self.params.rsi_pullback_short
                
                if pullback_to_ema and rsi_condition:
                    sl_distance = atr * 1.5
                    return (True, "SHORT", sl_distance)
        
        # ===== RANGING REGIME ENTRIES =====
        elif regime == MarketRegime.RANGING:
            swing_high = self.swing_high[0]
            swing_low = self.swing_low[0]
            
            # LONG: RSI oversold + near swing low
            if rsi < self.params.rsi_oversold:
                near_support = abs(price - swing_low) < atr * 0.5
                if near_support:
                    sl_distance = atr * 1.0  # Tighter stop for ranging
                    return (True, "LONG", sl_distance)
            
            # SHORT: RSI overbought + near swing high
            elif rsi > self.params.rsi_overbought:
                near_resistance = abs(price - swing_high) < atr * 0.5
                if near_resistance:
                    sl_distance = atr * 1.0
                    return (True, "SHORT", sl_distance)
        
        return (False, None, 0)
    
    def update_daily_tracking(self) -> None:
        """Update daily tracking variables on new day"""
        current_dt = self.datas[0].datetime.date(0)
        
        if self.current_date != current_dt:
            # Store previous day's H/L
            if self.day_high is not None:
                self.prev_high = self.day_high
                self.prev_low = self.day_low
            
            # Record yesterday's P&L for consistency tracking
            if self.current_date is not None and self.daily_pnl != 0:
                self.daily_profits[self.current_date] = self.daily_pnl
                
                # Update best day and check consistency
                if self.daily_pnl > self.best_day_profit:
                    self.best_day_profit = self.daily_pnl
                
                # Check 20% consistency rule
                if self.total_profit > 0:
                    consistency_ratio = self.best_day_profit / self.total_profit
                    if consistency_ratio > 0.20:
                        self.consistency_violations.append({
                            "date": self.current_date,
                            "best_day": self.best_day_profit,
                            "total_profit": self.total_profit,
                            "ratio": consistency_ratio
                        })
            
            # Reset daily counters
            self.current_date = current_dt
            self.daily_pnl = 0.0
            self.daily_trades = 0
            self.day_high = self.high[0]
            self.day_low = self.low[0]
        else:
            # Update daily high/low
            if self.high[0] > self.day_high:
                self.day_high = self.high[0]
            if self.low[0] < self.day_low:
                self.day_low = self.low[0]
    
    def manage_trailing_stop(self) -> None:
        """Manage trailing stop for trending positions"""
        if not self.position or not self.entry_price:
            return
        
        price = self.close[0]
        atr = self.atr[0]
        trailing_distance = atr * self.params.trailing_atr_multiplier
        
        if self.position.size > 0:  # Long position
            # Calculate current R
            if self.stop_loss:
                risk = self.entry_price - self.stop_loss
                current_r = (price - self.entry_price) / risk if risk > 0 else 0
                
                # Activate trailing after 1R profit
                if current_r >= self.params.trailing_activation_r:
                    self.trailing_active = True
                
                # Update trailing stop
                if self.trailing_active:
                    new_stop = price - trailing_distance
                    if new_stop > self.stop_loss:
                        self.stop_loss = new_stop
                        
        elif self.position.size < 0:  # Short position
            if self.stop_loss:
                risk = self.stop_loss - self.entry_price
                current_r = (self.entry_price - price) / risk if risk > 0 else 0
                
                if current_r >= self.params.trailing_activation_r:
                    self.trailing_active = True
                
                if self.trailing_active:
                    new_stop = price + trailing_distance
                    if new_stop < self.stop_loss:
                        self.stop_loss = new_stop
    
    def next(self) -> None:
        """Main trading logic executed on each bar"""
        # Update daily tracking
        self.update_daily_tracking()
        
        # Skip if order is pending
        if self.order:
            return
        
        # Manage existing position
        if self.position:
            self.manage_trailing_stop()
            
            # Check stop loss hit
            if self.position.size > 0 and self.low[0] <= self.stop_loss:
                self.order = self.close()
                self.log(f"Long SL hit at {self.stop_loss:.2f}")
                return
            elif self.position.size < 0 and self.high[0] >= self.stop_loss:
                self.order = self.close()
                self.log(f"Short SL hit at {self.stop_loss:.2f}")
                return
            
            return
        
        # Check if trading is allowed
        if not self.check_daily_limits():
            return
        
        # Check entry conditions
        should_enter, direction, sl_distance = self.check_entry_conditions()
        
        if should_enter:
            lot_size = self.calculate_lot_size(sl_distance)
            price = self.close[0]
            
            if direction == "LONG":
                self.entry_price = price
                self.stop_loss = price - sl_distance
                self.take_profit = price + (sl_distance * 2)  # 2R target
                self.trailing_active = False
                
                self.order = self.buy(size=lot_size)
                self.daily_trades += 1
                
                regime = self.detect_regime().value
                self.log(f"LONG Entry: {price:.2f} | SL: {self.stop_loss:.2f} | "
                        f"TP: {self.take_profit:.2f} | Size: {lot_size} | Regime: {regime}")
                
            elif direction == "SHORT":
                self.entry_price = price
                self.stop_loss = price + sl_distance
                self.take_profit = price - (sl_distance * 2)
                self.trailing_active = False
                
                self.order = self.sell(size=lot_size)
                self.daily_trades += 1
                
                regime = self.detect_regime().value
                self.log(f"SHORT Entry: {price:.2f} | SL: {self.stop_loss:.2f} | "
                        f"TP: {self.take_profit:.2f} | Size: {lot_size} | Regime: {regime}")
    
    def notify_order(self, order) -> None:
        """Handle order notifications"""
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f"BUY EXECUTED: Price={order.executed.price:.2f}, "
                        f"Size={order.executed.size:.2f}")
            else:
                self.log(f"SELL EXECUTED: Price={order.executed.price:.2f}, "
                        f"Size={order.executed.size:.2f}")
        
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f"Order Canceled/Margin/Rejected: {order.status}")
        
        self.order = None
    
    def notify_trade(self, trade) -> None:
        """Handle trade notifications and P&L tracking"""
        if not trade.isclosed:
            return
        
        pnl = trade.pnl
        self.daily_pnl += pnl
        self.total_profit += pnl
        
        self.log(f"TRADE CLOSED: PnL=${pnl:.2f} | Daily PnL=${self.daily_pnl:.2f} | "
                f"Total=${self.total_profit:.2f}")
        
        # Reset position tracking
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        self.trailing_active = False
    
    def stop(self) -> None:
        """Called at the end of backtest - print summary"""
        self.log("=" * 60)
        self.log("BACKTEST COMPLETE - SUMMARY")
        self.log("=" * 60)
        self.log(f"Final Account Value: ${self.broker.getvalue():.2f}")
        self.log(f"Total Profit: ${self.total_profit:.2f}")
        self.log(f"Return: {(self.total_profit / self.params.account_size) * 100:.2f}%")
        self.log(f"Best Day Profit: ${self.best_day_profit:.2f}")
        
        # Consistency rule check
        if self.total_profit > 0:
            consistency_ratio = (self.best_day_profit / self.total_profit) * 100
            self.log(f"Consistency Ratio: {consistency_ratio:.1f}% (must be <20%)")
            if consistency_ratio > 20:
                self.log("⚠️ WARNING: Consistency rule violated!")
                self.log(f"   Violations: {len(self.consistency_violations)}")
        
        # Phase targets check
        phase1_target = self.params.account_size * 0.08  # 8%
        phase2_target = self.params.account_size * 0.05  # 5%
        
        if self.total_profit >= phase1_target:
            self.log(f"✅ Phase 1 Target PASSED (${phase1_target:.2f})")
        else:
            self.log(f"❌ Phase 1 Target NOT MET (need ${phase1_target:.2f})")
        
        self.log("=" * 60)
