"""
Scalping Trading Strategy for Backtrader

Implements 6 Price Action / Smart Money Concepts (SMC) patterns:
1. Pin Bar + Inside Bar Combo
2. VWAP Rejection with Engulfing Pin Bar
3. Inside Bar Liquidity Clear Out (Fake Out)
4. Momentum Fading (Consecutive Wicks)
5. Power Candles (Volume Spread Analysis)
6. Tower Top / Tower Bottom Reversals

Based on: "I Tried Every Strategy, This Scalping Trading Course Changed Everything"

Author: TradeLockerBot
Timeframe: 1-minute (scalping)
Instrument: XAUUSD
"""

import backtrader as bt
import math
from collections import namedtuple
from datetime import datetime

# Named tuples for pattern data
PinBar = namedtuple('PinBar', ['high', 'low', 'close', 'direction', 'bar_idx'])
InsideBar = namedtuple('InsideBar', ['high', 'low', 'parent_high', 'parent_low', 'bar_idx'])
SDZone = namedtuple('SDZone', ['top', 'bottom', 'type', 'created_bar', 'touches'])
TowerPattern = namedtuple('TowerPattern', ['type', 'start_bar', 'base_bars', 'reversal_bar'])


class VWAP(bt.Indicator):
    """
    Volume Weighted Average Price (VWAP) Indicator
    
    Calculates cumulative VWAP that resets daily.
    Also tracks VWAP slope to determine if it's rising/falling.
    """
    lines = ('vwap', 'vwap_upper', 'vwap_lower')
    params = (
        ('std_dev', 2.0),  # Standard deviation bands
    )
    
    def __init__(self):
        self.cumvol = 0.0
        self.cumtp = 0.0
        self.cumsq = 0.0
        self.prev_date = None
    
    def next(self):
        # Get current date for daily reset
        try:
            current_date = self.data.datetime.date(0)
        except (AttributeError, ValueError):
            current_date = None
        
        # Reset at start of new day
        if current_date != self.prev_date:
            self.cumvol = 0.0
            self.cumtp = 0.0
            self.cumsq = 0.0
            self.prev_date = current_date
        
        # Typical price = (High + Low + Close) / 3
        typical_price = (self.data.high[0] + self.data.low[0] + self.data.close[0]) / 3.0
        volume = self.data.volume[0] if self.data.volume[0] > 0 else 1.0
        
        # Cumulative values
        self.cumvol += volume
        self.cumtp += typical_price * volume
        self.cumsq += (typical_price ** 2) * volume
        
        # Calculate VWAP
        if self.cumvol > 0:
            vwap_val = self.cumtp / self.cumvol
            self.lines.vwap[0] = vwap_val
            
            # Standard deviation bands
            variance = (self.cumsq / self.cumvol) - (vwap_val ** 2)
            std_dev = math.sqrt(max(0, variance))
            self.lines.vwap_upper[0] = vwap_val + (std_dev * self.params.std_dev)
            self.lines.vwap_lower[0] = vwap_val - (std_dev * self.params.std_dev)
        else:
            self.lines.vwap[0] = self.data.close[0]
            self.lines.vwap_upper[0] = self.data.close[0]
            self.lines.vwap_lower[0] = self.data.close[0]


class ScalpingStrategy(bt.Strategy):
    """
    Scalping Strategy implementing 6 Price Action / SMC patterns.
    
    Patterns:
    1. Pin Bar + Inside Bar: Reversal/continuation at S/D zones
    2. VWAP Rejection: Engulfing pin bar at VWAP line
    3. Liquidity Clear Out: False breakout / stop hunt
    4. Momentum Fading: Consecutive wicks showing exhaustion
    5. Power Candles: High-volume strong candles
    6. Tower Top/Bottom: Three-phase reversal pattern
    
    Risk Management:
    - 1% risk per trade
    - Max 4 consecutive losses then stop
    - Partial profits at 1:1 RR
    """
    
    params = (
        # ===== PATTERN SELECTION =====
        ('pattern_pinbar_inside', True),
        ('pattern_vwap_rejection', True),
        ('pattern_liquidity_fakeout', True),
        ('pattern_momentum_fade', True),
        ('pattern_power_candle', True),
        ('pattern_tower', True),
        
        # ===== TRADING HOURS (UTC) =====
        ('session_start_hour', 8),    # 08:00 UTC
        ('session_end_hour', 20),     # 20:00 UTC
        
        # ===== RISK MANAGEMENT =====
        ('risk_per_trade_percent', 0.01),   # 1% risk per trade
        ('rr_ratio', 2.0),                   # 1:2 Risk:Reward
        ('partial_profit_rr', 1.0),          # Take 50% at 1:1
        ('partial_profit_pct', 0.5),         # Close 50% of position
        ('max_consecutive_losses', 4),       # Stop after 4 losses
        ('max_daily_trades', 5),
        ('max_drawdown_percent', 0.12),      # 12% max DD (FundedHero)
        ('max_lots', 0.5),
        ('contract_size', 100),              # XAUUSD contract size
        
        # ===== PIN BAR PARAMETERS =====
        ('pinbar_wick_ratio', 2.0),          # Wick must be 2x body
        ('pinbar_body_max_pct', 0.33),       # Body < 33% of range
        
        # ===== INSIDE BAR PARAMETERS =====
        ('inside_bar_breakout_buffer', 0.5),  # Pips beyond IB for entry
        
        # ===== VWAP PARAMETERS =====
        ('vwap_rejection_pips', 2.0),        # Max distance from VWAP
        
        # ===== POWER CANDLE PARAMETERS =====
        ('power_candle_body_ratio', 0.7),    # Body > 70% of range
        ('volume_ma_period', 20),
        ('volume_threshold_mult', 1.5),      # Volume > 1.5x average
        
        # ===== MOMENTUM FADE PARAMETERS =====
        ('consecutive_wicks_count', 3),      # Need 3 consecutive wicks
        ('wick_min_pct', 0.4),               # Wick > 40% of candle
        
        # ===== TOWER PARAMETERS =====
        ('tower_base_candles', 3),           # Minimum base candles
        ('tower_body_ratio', 0.6),           # Trend candle body > 60%
        
        # ===== SUPPLY/DEMAND ZONES =====
        ('sd_zone_lookback', 20),
        ('sd_zone_min_strength', 2),         # Minimum touches
        ('sd_zone_atr_mult', 1.5),           # Zone size = ATR * mult
        
        # ===== TECHNICAL =====
        ('atr_period', 14),
        ('verbose', True),
    )
    
    def __init__(self):
        # ===== INDICATORS =====
        self.atr = bt.indicators.ATR(self.data, period=self.params.atr_period)
        self.vwap = VWAP(self.data)
        self.volume_ma = bt.indicators.SMA(self.data.volume, period=self.params.volume_ma_period)
        
        # ===== PATTERN STATE =====
        self.last_pin_bar = None
        self.last_inside_bar = None
        self.supply_zones = []
        self.demand_zones = []
        
        # ===== TRADE STATE =====
        self.order = None
        self.entry_price = None
        self.sl_price = None
        self.tp_price = None
        self.partial_taken = False
        self.entry_pattern = None
        
        # ===== RISK STATE =====
        self.consecutive_losses = 0
        self.daily_trades = 0
        self.current_date = None
        self.permanent_lock = False
        self.peak_equity = 0.0
        
        # ===== TRACKING =====
        self.bar_executed = 0
    
    def log(self, txt, dt=None):
        """Logging utility"""
        if not self.params.verbose:
            return
        if dt is None:
            try:
                dt = self.datas[0].datetime.datetime(0)
                dts = dt.strftime('%Y-%m-%d %H:%M')
            except (IndexError, ValueError):
                dts = "---"
        else:
            dts = dt.strftime('%Y-%m-%d %H:%M') if hasattr(dt, 'strftime') else str(dt)
        print(f'{dts} | {txt}')
    
    def start(self):
        self.log("Scalping Strategy Started - 6 Patterns Active")
        self.peak_equity = self.broker.getvalue()
    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'LONG EXECUTED @ {order.executed.price:.2f} [{self.entry_pattern}]')
            else:
                self.log(f'SHORT EXECUTED @ {order.executed.price:.2f} [{self.entry_pattern}]')
            self.bar_executed = len(self)
        
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log(f'Order Failed: {order.getstatusname()}')
        
        self.order = None
    
    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        
        pnl = trade.pnlcomm
        self.log(f'TRADE CLOSED - PnL: ${pnl:.2f} [{self.entry_pattern}]')
        
        # Track consecutive losses
        if pnl < 0:
            self.consecutive_losses += 1
            self.log(f'Consecutive losses: {self.consecutive_losses}')
            if self.consecutive_losses >= self.params.max_consecutive_losses:
                self.log(f'!!! {self.consecutive_losses} CONSECUTIVE LOSSES - STOPPING FOR DAY !!!')
        else:
            self.consecutive_losses = 0  # Reset on win
        
        # Reset trade state
        self.entry_price = None
        self.sl_price = None
        self.tp_price = None
        self.partial_taken = False
        self.entry_pattern = None
    
    # =========================================================================
    # CANDLESTICK PATTERN DETECTION
    # =========================================================================
    
    def detect_pin_bar(self, lookback=0):
        """
        Detect Pin Bar pattern.
        
        A Pin Bar has:
        - Small body (< 33% of total range)
        - Long wick (> 2x body size)
        - Wick on one side indicates rejection
        
        Returns: PinBar namedtuple or None
        """
        if len(self.data) < 2:
            return None
        
        o = self.data.open[lookback]
        h = self.data.high[lookback]
        l = self.data.low[lookback]
        c = self.data.close[lookback]
        
        body = abs(c - o)
        total_range = h - l
        
        if total_range == 0:
            return None
        
        body_pct = body / total_range
        
        # Check if body is small enough
        if body_pct > self.params.pinbar_body_max_pct:
            return None
        
        # Calculate wicks
        body_top = max(o, c)
        body_bottom = min(o, c)
        upper_wick = h - body_top
        lower_wick = body_bottom - l
        
        # Determine direction based on dominant wick
        if lower_wick > upper_wick * self.params.pinbar_wick_ratio:
            # Bullish pin bar (long lower wick = rejection of lows)
            direction = 'BULLISH'
        elif upper_wick > lower_wick * self.params.pinbar_wick_ratio:
            # Bearish pin bar (long upper wick = rejection of highs)
            direction = 'BEARISH'
        else:
            return None
        
        return PinBar(
            high=h,
            low=l,
            close=c,
            direction=direction,
            bar_idx=len(self) + lookback
        )
    
    def detect_inside_bar(self, lookback=0):
        """
        Detect Inside Bar pattern.
        
        An Inside Bar is completely contained within the previous candle's range.
        
        Returns: InsideBar namedtuple or None
        """
        if len(self.data) < 2:
            return None
        
        # Current candle
        curr_h = self.data.high[lookback]
        curr_l = self.data.low[lookback]
        
        # Previous candle (mother bar)
        prev_h = self.data.high[lookback - 1]
        prev_l = self.data.low[lookback - 1]
        
        # Check if current is inside previous
        if curr_h <= prev_h and curr_l >= prev_l:
            return InsideBar(
                high=curr_h,
                low=curr_l,
                parent_high=prev_h,
                parent_low=prev_l,
                bar_idx=len(self) + lookback
            )
        
        return None
    
    def detect_engulfing_pin_bar(self, lookback=0):
        """
        Detect Engulfing Pin Bar (VWAP Rejection pattern).
        
        A candle that:
        1. Engulfs the previous candle's body
        2. Has a long wick rejecting a level (VWAP)
        
        Returns: dict with direction and rejection info, or None
        """
        if len(self.data) < 2:
            return None
        
        # Current candle
        curr_o = self.data.open[lookback]
        curr_h = self.data.high[lookback]
        curr_l = self.data.low[lookback]
        curr_c = self.data.close[lookback]
        
        # Previous candle
        prev_o = self.data.open[lookback - 1]
        prev_c = self.data.close[lookback - 1]
        
        prev_body_top = max(prev_o, prev_c)
        prev_body_bottom = min(prev_o, prev_c)
        
        curr_body_top = max(curr_o, curr_c)
        curr_body_bottom = min(curr_o, curr_c)
        
        # Check engulfing
        if not (curr_body_top > prev_body_top and curr_body_bottom < prev_body_bottom):
            return None
        
        # Check for pin bar characteristics
        body = abs(curr_c - curr_o)
        total_range = curr_h - curr_l
        
        if total_range == 0:
            return None
        
        upper_wick = curr_h - curr_body_top
        lower_wick = curr_body_bottom - curr_l
        
        # Check if it has significant wick (rejection)
        if lower_wick > body * 0.5 and curr_c > curr_o:
            return {
                'direction': 'BULLISH',
                'rejection_level': curr_l,
                'entry_price': curr_c
            }
        elif upper_wick > body * 0.5 and curr_c < curr_o:
            return {
                'direction': 'BEARISH',
                'rejection_level': curr_h,
                'entry_price': curr_c
            }
        
        return None
    
    def detect_power_candle(self, lookback=0):
        """
        Detect Power Candle (VSA pattern).
        
        A Power Candle has:
        1. Wide range (spread) compared to recent candles
        2. Small or no wicks (decisive sentiment)
        3. Above-average volume
        
        Returns: dict with direction and strength, or None
        """
        if len(self.data) < self.params.volume_ma_period:
            return None
        
        curr_o = self.data.open[lookback]
        curr_h = self.data.high[lookback]
        curr_l = self.data.low[lookback]
        curr_c = self.data.close[lookback]
        curr_v = self.data.volume[lookback]
        
        body = abs(curr_c - curr_o)
        total_range = curr_h - curr_l
        
        if total_range == 0:
            return None
        
        body_ratio = body / total_range
        
        # Check body ratio (must be large candle with small wicks)
        if body_ratio < self.params.power_candle_body_ratio:
            return None
        
        # Check volume (must be above average)
        vol_threshold = self.volume_ma[lookback] * self.params.volume_threshold_mult
        if curr_v < vol_threshold:
            return None
        
        # Check if candle is significant compared to ATR
        if total_range < self.atr[lookback]:
            return None
        
        direction = 'BULLISH' if curr_c > curr_o else 'BEARISH'
        
        return {
            'direction': direction,
            'range': total_range,
            'volume_ratio': curr_v / self.volume_ma[lookback] if self.volume_ma[lookback] > 0 else 1.0
        }
    
    def detect_consecutive_wicks(self, lookback=0):
        """
        Detect Momentum Fading pattern (consecutive wicks).
        
        Look for 2-3 consecutive candles with overlapping wicks
        in the same direction, indicating exhaustion.
        
        Returns: dict with direction, or None
        """
        count = self.params.consecutive_wicks_count
        if len(self.data) < count + 1:
            return None
        
        lower_wicks = []
        upper_wicks = []
        
        for i in range(count):
            idx = lookback - i
            o = self.data.open[idx]
            h = self.data.high[idx]
            l = self.data.low[idx]
            c = self.data.close[idx]
            
            body_top = max(o, c)
            body_bottom = min(o, c)
            total_range = h - l
            
            if total_range == 0:
                return None
            
            upper_wick = h - body_top
            lower_wick = body_bottom - l
            
            lower_wicks.append(lower_wick / total_range)
            upper_wicks.append(upper_wick / total_range)
        
        min_wick_pct = self.params.wick_min_pct
        
        # Check for consecutive lower wicks (bullish - buyers stepping in)
        if all(w >= min_wick_pct for w in lower_wicks):
            return {'direction': 'BULLISH', 'wick_count': count}
        
        # Check for consecutive upper wicks (bearish - sellers stepping in)
        if all(w >= min_wick_pct for w in upper_wicks):
            return {'direction': 'BEARISH', 'wick_count': count}
        
        return None
    
    def detect_liquidity_fakeout(self, lookback=0):
        """
        Detect Inside Bar Liquidity Clear Out (Fake Out).
        
        Pattern:
        1. Inside Bar forms
        2. Next candle breaks out of IB range
        3. Same candle snaps back into range (pin bar wick)
        
        Returns: dict with direction, or None
        """
        if len(self.data) < 4:
            return None
        
        # Check for inside bar 2 bars ago
        ib = self.detect_inside_bar(lookback - 1)
        if ib is None:
            return None
        
        # Current candle should be the "fakeout" candle
        curr_h = self.data.high[lookback]
        curr_l = self.data.low[lookback]
        curr_c = self.data.close[lookback]
        
        # Check for false break above (bearish fakeout → short)
        if curr_h > ib.parent_high and curr_c < ib.parent_high:
            return {
                'direction': 'SHORT',  # Trade opposite to fakeout
                'fakeout_level': ib.parent_high,
                'entry_price': curr_c
            }
        
        # Check for false break below (bullish fakeout → long)
        if curr_l < ib.parent_low and curr_c > ib.parent_low:
            return {
                'direction': 'LONG',  # Trade opposite to fakeout
                'fakeout_level': ib.parent_low,
                'entry_price': curr_c
            }
        
        return None
    
    def detect_tower_pattern(self, lookback=0):
        """
        Detect Tower Top / Tower Bottom reversal.
        
        Pattern:
        1. Large trend candle
        2. Series of small candles (base)
        3. Large reversal candle in opposite direction
        
        The reversal candle must have higher volume than base candles.
        
        Returns: TowerPattern namedtuple or None
        """
        min_base = self.params.tower_base_candles
        if len(self.data) < min_base + 3:
            return None
        
        # Check current candle (potential reversal candle)
        curr_o = self.data.open[lookback]
        curr_h = self.data.high[lookback]
        curr_l = self.data.low[lookback]
        curr_c = self.data.close[lookback]
        curr_v = self.data.volume[lookback]
        
        curr_body = abs(curr_c - curr_o)
        curr_range = curr_h - curr_l
        
        if curr_range == 0:
            return None
        
        # Reversal candle must be significant
        if curr_body / curr_range < self.params.tower_body_ratio:
            return None
        
        reversal_direction = 'BULLISH' if curr_c > curr_o else 'BEARISH'
        
        # Check base candles (should be small)
        base_volumes = []
        for i in range(1, min_base + 1):
            idx = lookback - i
            o = self.data.open[idx]
            h = self.data.high[idx]
            l = self.data.low[idx]
            c = self.data.close[idx]
            v = self.data.volume[idx]
            
            body = abs(c - o)
            rng = h - l
            
            if rng == 0:
                return None
            
            # Base candles should have small bodies (dojis, spinning tops)
            if body / rng > 0.5:
                return None
            
            base_volumes.append(v)
        
        # Check trend candle (before base)
        trend_idx = lookback - min_base - 1
        trend_o = self.data.open[trend_idx]
        trend_c = self.data.close[trend_idx]
        trend_h = self.data.high[trend_idx]
        trend_l = self.data.low[trend_idx]
        
        trend_body = abs(trend_c - trend_o)
        trend_range = trend_h - trend_l
        
        if trend_range == 0:
            return None
        
        # Trend candle must be significant
        if trend_body / trend_range < self.params.tower_body_ratio:
            return None
        
        trend_direction = 'BULLISH' if trend_c > trend_o else 'BEARISH'
        
        # Reversal must be opposite to trend
        if trend_direction == reversal_direction:
            return None
        
        # Volume confirmation: reversal volume > average base volume
        avg_base_vol = sum(base_volumes) / len(base_volumes) if base_volumes else 0
        if curr_v <= avg_base_vol:
            return None
        
        pattern_type = 'TOWER_BOTTOM' if reversal_direction == 'BULLISH' else 'TOWER_TOP'
        
        return TowerPattern(
            type=pattern_type,
            start_bar=len(self) + trend_idx,
            base_bars=min_base,
            reversal_bar=len(self) + lookback
        )
    
    # =========================================================================
    # SUPPLY/DEMAND ZONE DETECTION
    # =========================================================================
    
    def update_sd_zones(self):
        """
        Identify and update Supply/Demand zones from price action.
        
        Supply Zone: Area where price fell sharply from (resistance)
        Demand Zone: Area where price rose sharply from (support)
        """
        if len(self.data) < self.params.sd_zone_lookback:
            return
        
        # Simple S/D detection based on swing points and ATR
        atr_val = self.atr[0] if self.atr[0] > 0 else 5.0
        zone_size = atr_val * self.params.sd_zone_atr_mult
        
        # Check for demand zone (strong bounce up)
        lookback = 10
        lowest_idx = 0
        lowest_low = float('inf')
        
        for i in range(1, min(lookback, len(self.data))):
            if self.data.low[-i] < lowest_low:
                lowest_low = self.data.low[-i]
                lowest_idx = -i
        
        # If price bounced significantly from lowest point
        if self.data.close[0] > lowest_low + zone_size:
            zone = SDZone(
                top=lowest_low + zone_size,
                bottom=lowest_low,
                type='DEMAND',
                created_bar=len(self),
                touches=1
            )
            # Add if not duplicate
            if not any(abs(z.bottom - zone.bottom) < zone_size for z in self.demand_zones):
                self.demand_zones.append(zone)
                self.demand_zones = self.demand_zones[-10:]  # Keep last 10
        
        # Check for supply zone (strong drop down)
        highest_idx = 0
        highest_high = 0
        
        for i in range(1, min(lookback, len(self.data))):
            if self.data.high[-i] > highest_high:
                highest_high = self.data.high[-i]
                highest_idx = -i
        
        if self.data.close[0] < highest_high - zone_size:
            zone = SDZone(
                top=highest_high,
                bottom=highest_high - zone_size,
                type='SUPPLY',
                created_bar=len(self),
                touches=1
            )
            if not any(abs(z.top - zone.top) < zone_size for z in self.supply_zones):
                self.supply_zones.append(zone)
                self.supply_zones = self.supply_zones[-10:]
    
    def is_at_demand_zone(self):
        """Check if price is at a demand zone"""
        price = self.data.close[0]
        for zone in self.demand_zones:
            if zone.bottom <= price <= zone.top:
                return zone
        return None
    
    def is_at_supply_zone(self):
        """Check if price is at a supply zone"""
        price = self.data.close[0]
        for zone in self.supply_zones:
            if zone.bottom <= price <= zone.top:
                return zone
        return None
    
    # =========================================================================
    # TRADE MANAGEMENT
    # =========================================================================
    
    def calculate_position_size(self, sl_distance):
        """Calculate position size based on risk percentage"""
        risk_amount = self.broker.getvalue() * self.params.risk_per_trade_percent
        
        if sl_distance <= 0:
            return 0
        
        raw_size = risk_amount / (sl_distance * self.params.contract_size)
        size = round(raw_size, 2)
        
        if size > self.params.max_lots:
            size = self.params.max_lots
        
        return max(size, 0.01)
    
    def is_trading_hours(self):
        """Check if we're in trading hours"""
        try:
            hour = self.datas[0].datetime.datetime(0).hour
            return self.params.session_start_hour <= hour < self.params.session_end_hour
        except (AttributeError, ValueError):
            return True
    
    def check_circuit_breakers(self):
        """Check if trading should be stopped"""
        # Permanent lock (max drawdown)
        if self.permanent_lock:
            return True
        
        # Max consecutive losses
        if self.consecutive_losses >= self.params.max_consecutive_losses:
            return True
        
        # Max daily trades
        if self.daily_trades >= self.params.max_daily_trades:
            return True
        
        # Max drawdown check
        current_equity = self.broker.getvalue()
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity
        
        drawdown_pct = (self.peak_equity - current_equity) / self.peak_equity if self.peak_equity > 0 else 0
        
        if drawdown_pct > self.params.max_drawdown_percent:
            self.log(f'!!! MAX DRAWDOWN {drawdown_pct*100:.1f}% - PERMANENT LOCK !!!')
            self.permanent_lock = True
            return True
        
        return False
    
    def execute_entry(self, direction, sl_price, pattern_name):
        """Execute a trade entry with SL/TP bracket"""
        entry_price = self.data.close[0]
        sl_distance = abs(entry_price - sl_price)
        
        if sl_distance <= 0:
            return
        
        # Calculate TP based on R:R ratio
        if direction == 'LONG':
            tp_price = entry_price + (sl_distance * self.params.rr_ratio)
        else:
            tp_price = entry_price - (sl_distance * self.params.rr_ratio)
        
        size = self.calculate_position_size(sl_distance)
        
        if size <= 0:
            return
        
        self.log(f'{direction} ENTRY [{pattern_name}]: Price={entry_price:.2f}, SL={sl_price:.2f}, TP={tp_price:.2f}')
        
        if direction == 'LONG':
            self.buy_bracket(
                size=size,
                exectype=bt.Order.Market,
                stopprice=sl_price,
                limitprice=tp_price
            )
        else:
            self.sell_bracket(
                size=size,
                exectype=bt.Order.Market,
                stopprice=sl_price,
                limitprice=tp_price
            )
        
        self.entry_price = entry_price
        self.sl_price = sl_price
        self.tp_price = tp_price
        self.entry_pattern = pattern_name
        self.daily_trades += 1
    
    # =========================================================================
    # MAIN LOOP
    # =========================================================================
    
    def next(self):
        """Main strategy logic - scan for patterns and manage trades"""
        
        # Daily reset
        try:
            current_date = self.datas[0].datetime.date(0)
            if self.current_date != current_date:
                self.current_date = current_date
                self.daily_trades = 0
                self.consecutive_losses = 0
                self.log(f'=== NEW DAY: {current_date} ===')
        except (AttributeError, ValueError):
            pass
        
        # Circuit breakers
        if self.check_circuit_breakers():
            return
        
        # Skip if order pending or in position
        if self.order or self.position:
            return
        
        # Trading hours filter
        if not self.is_trading_hours():
            return
        
        # Update S/D zones
        self.update_sd_zones()
        
        # Need minimum bars for indicators
        if len(self.data) < max(self.params.atr_period, self.params.volume_ma_period) + 5:
            return
        
        # =====================================================================
        # PATTERN 1: PIN BAR + INSIDE BAR COMBO
        # The inside bar should form right after the pin bar (IB is contained in pin)
        # =====================================================================
        if self.params.pattern_pinbar_inside:
            # Check if current bar is inside bar with pin bar as mother
            pin = self.detect_pin_bar(-1)  # Pin bar from previous candle
            
            if pin:
                # Check if current candle is contained within the pin bar
                curr_h = self.data.high[0]
                curr_l = self.data.low[0]
                
                if curr_h <= pin.high and curr_l >= pin.low:
                    # Inside bar confirmed - now check for S/D zone OR nearby support
                    demand_zone = self.is_at_demand_zone()
                    supply_zone = self.is_at_supply_zone()
                    
                    # Check for recent swing low as fallback demand zone
                    recent_low = min(self.data.low[-i] for i in range(min(10, len(self.data))))
                    near_support = abs(self.data.close[0] - recent_low) < self.atr[0] * 2
                    
                    # Recent high for supply zone fallback
                    recent_high = max(self.data.high[-i] for i in range(min(10, len(self.data))))
                    near_resistance = abs(self.data.close[0] - recent_high) < self.atr[0] * 2
                    
                    # Bullish pin + IB at demand zone or near support → LONG
                    if pin.direction == 'BULLISH' and (demand_zone or near_support):
                        sl = pin.low - self.params.inside_bar_breakout_buffer
                        self.execute_entry('LONG', sl, 'PinBar+IB')
                        return
                    
                    # Bearish pin + IB at supply zone or near resistance → SHORT
                    if pin.direction == 'BEARISH' and (supply_zone or near_resistance):
                        sl = pin.high + self.params.inside_bar_breakout_buffer
                        self.execute_entry('SHORT', sl, 'PinBar+IB')
                        return
        
        # =====================================================================
        # PATTERN 2: VWAP REJECTION WITH ENGULFING PIN BAR
        # =====================================================================
        if self.params.pattern_vwap_rejection:
            engulf = self.detect_engulfing_pin_bar(0)
            
            if engulf:
                vwap_val = self.vwap.vwap[0]
                vwap_prev = self.vwap.vwap[-1] if len(self.vwap.vwap) > 1 else vwap_val
                price = self.data.close[0]
                
                # VWAP slope (rising or falling)
                vwap_rising = vwap_val > vwap_prev
                
                # Distance from VWAP
                dist_from_vwap = abs(price - vwap_val)
                max_dist = self.params.vwap_rejection_pips
                
                # Bullish: Price above rising VWAP, engulfing with rejection
                if engulf['direction'] == 'BULLISH' and vwap_rising and dist_from_vwap < max_dist:
                    sl = engulf['rejection_level'] - 1.0
                    self.execute_entry('LONG', sl, 'VWAP-Rejection')
                    return
                
                # Bearish: Price below falling VWAP, engulfing with rejection
                if engulf['direction'] == 'BEARISH' and not vwap_rising and dist_from_vwap < max_dist:
                    sl = engulf['rejection_level'] + 1.0
                    self.execute_entry('SHORT', sl, 'VWAP-Rejection')
                    return
        
        # =====================================================================
        # PATTERN 3: INSIDE BAR LIQUIDITY CLEAR OUT (FAKE OUT)
        # =====================================================================
        if self.params.pattern_liquidity_fakeout:
            fakeout = self.detect_liquidity_fakeout(0)
            
            if fakeout:
                if fakeout['direction'] == 'LONG':
                    sl = fakeout['fakeout_level'] - 2.0
                    self.execute_entry('LONG', sl, 'LiquidityFakeout')
                    return
                else:
                    sl = fakeout['fakeout_level'] + 2.0
                    self.execute_entry('SHORT', sl, 'LiquidityFakeout')
                    return
        
        # =====================================================================
        # PATTERN 4: MOMENTUM FADING (CONSECUTIVE WICKS)
        # =====================================================================
        if self.params.pattern_momentum_fade:
            wicks = self.detect_consecutive_wicks(0)
            
            if wicks:
                demand_zone = self.is_at_demand_zone()
                supply_zone = self.is_at_supply_zone()
                
                # Bullish wicks at demand → LONG
                if wicks['direction'] == 'BULLISH' and demand_zone:
                    sl = demand_zone.bottom - 1.0
                    self.execute_entry('LONG', sl, 'MomentumFade')
                    return
                
                # Bearish wicks at supply → SHORT
                if wicks['direction'] == 'BEARISH' and supply_zone:
                    sl = supply_zone.top + 1.0
                    self.execute_entry('SHORT', sl, 'MomentumFade')
                    return
        
        # =====================================================================
        # PATTERN 5: POWER CANDLES (VSA)
        # =====================================================================
        if self.params.pattern_power_candle:
            power = self.detect_power_candle(0)
            
            if power:
                # Use ATR-based SL for power candle entries
                atr_val = self.atr[0] if self.atr[0] > 0 else 5.0
                
                if power['direction'] == 'BULLISH':
                    sl = self.data.low[0] - atr_val * 0.5
                    self.execute_entry('LONG', sl, 'PowerCandle')
                    return
                else:
                    sl = self.data.high[0] + atr_val * 0.5
                    self.execute_entry('SHORT', sl, 'PowerCandle')
                    return
        
        # =====================================================================
        # PATTERN 6: TOWER TOP / TOWER BOTTOM
        # =====================================================================
        if self.params.pattern_tower:
            tower = self.detect_tower_pattern(0)
            
            if tower:
                base_candles = self.params.tower_base_candles
                
                if tower.type == 'TOWER_BOTTOM':
                    # Find lowest point of formation for SL
                    formation_low = min(self.data.low[-i] for i in range(base_candles + 2))
                    sl = formation_low - 1.0
                    self.execute_entry('LONG', sl, 'TowerBottom')
                    return
                else:  # TOWER_TOP
                    # Find highest point of formation for SL
                    formation_high = max(self.data.high[-i] for i in range(base_candles + 2))
                    sl = formation_high + 1.0
                    self.execute_entry('SHORT', sl, 'TowerTop')
                    return
