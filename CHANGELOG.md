# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added - Asian Range Breakout Integration (2025-12-15)
- **Feature**: Integrated Asian Range Breakout strategy into `XauAdaptiveStrategy.py`
- **Session Structure**:
  - **Asian Session (01:00-08:00 GMT)**: Range measurement only (defines the "box")
  - **London Session (08:00-17:00 GMT)**: Breakout trading + trend following
  - **Session End (22:00 GMT)**: Close all positions
- **Breakout Logic**:
  - BUY: Price > Asian High + buffer AND Price > EMA50
  - SELL: Price < Asian Low - buffer AND Price < EMA50
  - One trade per direction per day (flags prevent overtrading)
- **New Parameters**:
  - `enable_asian_breakout`: Enable/disable the breakout strategy
  - `breakout_buffer`: Minimum pips above/below range for valid breakout
  - `use_ema_trend_filter`: Filter breakouts by EMA50 trend
  - `london_start_hour`, `london_end_hour`, `session_end_hour`
- **Fix**: Closed the "London Gap" - previous version missed 08:00-13:00 GMT trading window
- **Benefits**: Captures the high-volatility London Open (08:00) momentum moves that Gold is known for


### Added - XAU/USD Scalping Strategies Suite (2025-12-15)
- **Feature**: Implemented 3 automated XAU/USD scalping strategies based on `Strat.md` research document
- **Strategies**:
  1. **XauMeanReversionStrategy.py** - Bollinger Bands + RSI + Stochastic confluence
     - Entry: Price outside BB + RSI extreme (<30/>70) + Stochastic crossover in oversold/overbought zone
     - Exit: Target = Middle Bollinger Band (mean reversion), SL = ATR * 1.5
     - Optional `require_stoch_crossover` flag for strict/relaxed mode
  2. **XauTrendFollowingStrategy.py** - EMA Ribbon (8/21/50) pullback entries
     - Entry: EMA stack aligned + Price pulls back to 8-21 zone + Closes back in trend direction
     - Exit: ATR-based trailing stop (ATR * 2.0)
     - Captures "fat tail" moves during London/NY session
  3. **XauHeikinAshiStrategy.py** - Heikin-Ashi + Parabolic SAR + EMA 200
     - Entry: HA color change Red→Green (or Green→Red) + SAR flip + Price vs EMA200 filter
     - Exit: Immediate close on HA color reversal
- **Common Features**:
  - FundedHero-compliant risk management (1% per trade, 6% max drawdown, $75 daily loss limit)
  - London/NY Overlap time filter (13:00-17:00 GMT) for optimal spread conditions
  - ATR-based dynamic position sizing
  - TradeLocker `params_metadata` for UI configuration
- **Test Files**: Created `test_xau_mean_reversion.py`, `test_xau_trend_following.py`, `test_xau_heikin_ashi.py`
- **Verification**: Trend Following executed 5 trades (+0.06%), Mean Reversion executed 4 trades (-0.04%) with synthetic data

### Added - XAU/USD Adaptive Combined Strategy (2025-12-15)
- **Feature**: Created `XauAdaptiveStrategy.py` that combines all 3 strategies with automatic regime detection
- **Regime Detection**:
  - ADX > 25 = **TRENDING** regime: Uses EMA Ribbon pullback entries
  - ADX < 25 = **RANGING** regime: Uses Bollinger+RSI mean reversion entries
  - Heikin-Ashi color confirmation filter (optional)
- **Benefits**: Single bot adapts to changing market conditions instead of needing manual strategy switching
- **Verification**: 5 trades executed, +0.04% return on synthetic data with mixed regimes

### Fixed - XAU Adaptive Strategy Permanent Drawdown Lock (2025-12-15)
- **Bug**: Strategy halted permanently once 6% drawdown hit - never recovered on subsequent days
- **Impact**: "!!! MAX DRAWDOWN 6.51% - HALTING !!!" message repeated indefinitely through Nov 28 → Dec 12+
- **Root Cause**: `peak_equity` was set once at strategy start and never reset, meaning once drawdown exceeded threshold the strategy was locked forever
- **Fix**: Changed to `daily_peak_equity` that resets at the start of each trading day
  - Moved daily reset logic BEFORE drawdown check to ensure fresh start each day
  - Now halts for the current day only, resumes trading with a fresh peak on the next day
- **Expected Impact**: Strategy can now recover from drawdown and continue trading the following day

### Fixed - XAU Adaptive Strategy Counter-Trend Trading (2025-12-15)
- **Bug**: Strategy was taking SHORT trades during strong uptrends (e.g., March 2025 rally)
- **Root Cause**: No macro trend filter - allowed shorts when price was clearly above all EMAs
- **Fix**: Added EMA 200 macro trend filter with `trade_with_trend_only` parameter (default: True)
  - Price > EMA200: Only LONG signals allowed
  - Price < EMA200: Only SHORT signals allowed
  - Counter-trend signals now logged as "BLOCKED" for debugging
- **Expected Impact**: Fewer losing trades during strong directional months

### Fixed - XAU Adaptive Strategy Whipsaw Prevention (2025-12-15)
- **Bug**: Strategy getting "chopped" in consolidating markets (e.g., Jan-Mar 2024) due to:
  1. ADX temporarily spiking above 25 without sustained trends
  2. EMA crossovers giving false signals when EMAs are flat
  3. Binary regime switch with no buffer zone
- **Root Cause Analysis**:
  - Jan-Mar 2024: -4.11% ROI, 15.37% max DD (Image 1 failure)
  - Jul-Sep 2025: +28.34% ROI, 8.54% max DD (Image 2 success)
- **Fixes Implemented**:
  1. **ADX Hysteresis (Dead Zone)**:
     - Trend Mode: ADX > 30 (raised from 25)
     - Range Mode: ADX < 20
     - Dead Zone (20-30): NO TRADES
  2. **EMA Slope Filter**:
     - Requires EMA50 slope > 0.5 price units over 5 bars
     - Flat EMA = no trend trades (forces DEAD_ZONE)
  3. **Choppiness Index Filter**:
     - Chop > 61.8 = choppy market, blocks trend trades
     - Uses LOG10(SUM(TrueRange)/HighestHigh-LowestLow)
- **New Parameters**: `adx_range_threshold`, `ema_slope_lookback`, `min_ema_slope`, `chop_period`, `chop_threshold`, `use_slope_filter`, `use_chop_filter`

### Fixed - XAU Adaptive Strategy Squeeze Trap (2025-12-15)
- **Bug**: Low ADX (<20) during BB squeeze led to false RANGING mode, catching falling knives during breakouts
- **Root Cause**: Apr-Jun 2024 backtest: -15.28% ROI - bands tightened (squeeze), then violent breakout crushed mean reversion entries
- **Fixes Implemented**:
  1. **Bollinger Bandwidth Filter**:
     - Calculates width = (Upper - Lower) / Middle
     - If width < 0.15%, market is in SQUEEZE → forces DEAD_ZONE
     - Prevents mean reversion during volatility compression
  2. **Stochastic Crossover Confirmation**:
     - Changed from level check (`K < 25`) to crossover check (`K > D`)
     - LONG only when Stoch crosses UP (momentum turning bullish)
     - SHORT only when Stoch crosses DOWN (momentum turning bearish)
     - Avoids catching falling knives
- **New Parameters**: `min_bb_width` (0.0015), `use_squeeze_filter` (True)

### Fixed - XAU Adaptive Strategy Bollinger Band Walk (2025-12-15)
- **Bug**: Bot buying when price closes OUTSIDE BB, then "walking" down the band for 3-4 candles = instant stop-out
- **Root Cause**: `price < lower_bb` triggers during a crash, not a reversal
- **Fixes Implemented**:
  1. **Wick Rejection Rule**:
     - OLD: `price < lower_bb` (triggers during crash)
     - NEW: `low < lower_bb AND close > lower_bb` (wick dipped below but closed inside)
     - This proves buyers stepped in at that level
  2. **BB Slope Filter**:
     - Measures SMA20 movement over 3 bars
     - If slope > $1.50, bands are trending, NOT ranging
     - Disables mean reversion during "fake ranges"
  3. **Relaxed RSI Levels for Gold**:
     - Oversold: 30 → 35 (catches more opportunities)
     - Overbought: 70 → 65
- **New Parameters**: `bb_slope_threshold` (1.5), updated `min_bb_width` (0.002)

### Added - XAU Adaptive Strategy Time-Segmented Sessions (2025-12-15)
- **Problem**: Running Mean Reversion during NY Session (13:00-17:00) is suicidal - this is breakout time
- **Problem**: ADX > 30 is too late - by then the trend has moved 50-80 pips
- **Solution - Time-Based Strategy Segregation**:
  - **Asian Session (01:00-09:00 GMT)**: RANGING strategy ONLY (banks closed = safer ranges)
  - **NY Session (13:00-17:00 GMT)**: TRENDING strategy ONLY (high volatility = breakouts)
  - Session filter enforces correct strategy per time window
- **Solution - Faster Trend Entry**:
  - Lowered ADX threshold: 30 → 20 (catch moves earlier)
  - Added DI+/DI- confirmation (PlusDI > MinusDI for bullish, vice versa)
  - Now enters trends AS they start, not after 50 pips
- **New Parameters**: `asian_start_hour`, `asian_end_hour`, `ny_start_hour`, `ny_end_hour`, `use_session_filter`
- **New Indicators**: PlusDI, MinusDI for directional confirmation

### Added - XAU Asian Range Breakout Strategy (2025-12-15)
- **New File**: `XauAsianBreakoutStrategy.py`
- **Why**: Complex Adaptive Strategy over-filtered (-17.37% ROI) - simpler is better for Gold
- **Strategy Logic**:
  1. **Phase 1 (01:00-08:00 GMT)**: Measure Asian session High/Low → creates "The Box"
  2. **Phase 2 (08:00-17:00 GMT)**: Trade breakouts of the box
     - BUY: Price closes above Asian High AND Price > EMA50
     - SELL: Price closes below Asian Low AND Price < EMA50
  3. **Phase 3 (22:00 GMT)**: Close all positions, reset for next day
- **Key Advantages**:
  - Catches London Open momentum (most profitable time for Gold)
  - Avoids chop naturally (price stays in box = no trades)
  - Simple EMA50 filter prevents fakeouts
  - Higher R:R (1:3) for trend-following breakouts
- **Risk Management**: 2% risk per trade, max 2 trades/day, $100 daily loss limit### Added - EUR_USD Professional Trading Strategy (2025-12-10)
- **Feature**: Created comprehensive EUR_USD trading bot based on institutional-grade research
- **Strategy Components**:
  - **Dual-Filter EMA System**: 200 EMA trend filter + 20/50 EMA crossover signals
  - **Break and Retest**: Validates breakouts and waits for retest confirmation to filter false signals
  - **Session-Based Trading**: Only trades during London-NY overlap (12:00-16:00 UTC) for optimal liquidity and tighter spreads
  - **ATR-Based Risk Management**: Professional position sizing with 1.5x ATR stop loss and 2.5x ATR take profit (1.67:1 R:R)
  - **Fibonacci Confluence**: Uses 38.2% and 61.8% retracement levels for additional entry validation
- **Key Features**:
  - Trend direction filter prevents counter-trend trades (only longs in uptrends, shorts in downtrends)
  - "Angle of Attack" momentum filter ensures strong EMA divergence before entry
  - Support/Resistance detection using swing highs/lows
  - Dynamic position sizing based on account equity and ATR volatility
  - Comprehensive logging with trade rationale and performance metrics
- **Configurable Parameters**: 13 parameters including EMA periods, ATR multipliers, session hours, risk %, and feature toggles
- **Research Source**: Based on "EUR_USD Trading Strategies Research.md" comprehensive analysis

### Fixed - EUR_USD Strategy Initialization Error (2025-12-10)
- **Bug**: Strategy crashed on backtest initialization with `IndexError: array index out of range`
- **Impact**: Prevented any backtesting of the EUR_USD strategy
- **Root Cause**: `log()` method called from `__init__` attempted to access `self.datas[0].datetime.datetime(0)` before data was loaded into Backtrader
- **Fix**: Added try-except block in `log()` method to gracefully handle unavailable data during initialization phase, falling back to `[INIT]` prefix instead of timestamp
- **Expected Impact**: Strategy can now initialize and run backtests successfully

### Added - London Breakout Trailing Stop (2025-12-10)
- **Feature**: Implemented dynamic trailing stop to reduce max drawdown and lock in profits
- **Why**: Backtest showed excellent ROI (35.87%) and win rate (55.70%) but max drawdown (21.78%) exceeded FundedHero's 12% limit
- **Parameters**:
  - `use_trailing_stop` (True): Enable/disable trailing stop functionality
  - `trailing_activation_pct` (0.4): Activate trailing after 40% of initial TP distance reached
  - `trailing_distance_pct` (0.5): Trail SL at 50% of initial risk distance from favorable extreme
- **Mechanism**:
  - Tracks highest price for LONG positions, lowest for SHORT positions
  - Activates only after significant profit (prevents premature activation on noise)
  - Dynamically adjusts SL upward (longs) or downward (shorts) as price moves favorably
  - Never moves SL in unfavorable direction (only tightens protection)
- **Expected Impact**: Should reduce max drawdown from 21.78% to under 12% while maintaining strong ROI

### Fixed - London Breakout Position Blocking Bug (2025-12-10) **CRITICAL**
- **Bug**: Strategy stopped trading permanently after Feb 14-15 due to tiny residual positions blocking new entries
- **Impact**: After end-of-day position closes, floating point errors left microscopic positions that prevented ALL future breakout trades on BOTH 15m and 30m timeframes
- **Root Cause**: Line 135 checked `if self.position:` without size threshold, causing ANY position (even `0.0000000000000000034` lots from floating point arithmetic) to block trading forever via early return
- **Fix**: Added minimum position size check: `if self.order or (self.position and abs(self.position.size) >= 0.01):`
- **Expected Impact**: Strategy will now ignore tiny residual positions and continue taking breakout trades throughout multi-month backtests

### Fixed - London Breakout 30m Timeframe Compatibility (2025-12-10)
- **Bug**: Strategy stopped trading after Feb 14 when using 30m timeframe
- **Impact**: No Asian session bars during 00:00-08:00 on some days prevented `range_established` from being set, blocking all trading
- **Root Cause**: 30m bars (16 per Asian session) vs 15m bars (32 per session) - gaps in data prevented range establishment
- **Fix**: Added fallback mechanism to use previous day's Asian range when current day has no bars during Asian session
- **Expected Impact**: Strategy now works reliably on both 15m and 30m timeframes

### Fixed - London Breakout Strategy Permanent Lock Bug (2025-12-10)
- **Critical Bug**: Strategy had a permanent lock mechanism that prevented all trading after hitting 6% drawdown
- **Impact**: Strategy stopped trading permanently in March 2025 despite excellent performance (53.85% win rate, +4.44% ROI before halt)
- **Root Cause**: Used permanent `peak_equity` and `permanent_lock` flag that never reset
- **Fix**: Replaced with daily drawdown tracking that resets each day
  - Changed `peak_equity` → `daily_peak_equity` (resets at start of each trading day)
  - Removed `permanent_lock` flag entirely
  - Drawdown limit now stops trading for the day, not permanently
  - Strategy can recover and resume trading the next day
- **Expected Impact**: Strategy should now trade consistently throughout multi-month periods instead of stopping after first drawdown spike

### Fixed - London Breakout 0.0 Lots Bug (2025-12-10)
- **Bug**: End-of-day position closure attempted to trade 0.0 lots due to floating point rounding errors
- **Impact**: Caused order rejections: `Order size 0.0 is less than the minimum lot size 0.01`
- **Root Cause**: Floating point arithmetic created residual position sizes of `3.47e-18` which rounded to 0.0
- **Fix**: Added minimum position size check (`abs(position.size) >= 0.01`) before closing positions at end of day
- **Expected Impact**: Eliminates order rejection errors from tiny residual positions

### Changed - MACD Strategy Parameter Optimization (2025-12-10)
- **Minimum SL increased**: `min_sl_distance` from 10.0 to 20.0 pips to accommodate XAUUSD volatility on 15m timeframe
- **SL multiplier increased**: `ema_sl_multiplier` from 1.0 to 1.5 for wider stop placement relative to 200 EMA
- **Rationale**: Initial parameters were too tight for XAUUSD's price movement, causing premature stop-outs
- **Removed zero-line filter**: MACD crossovers now allowed at any level (not just below/above zero line)
  - **Impact**: Increased trade frequency from ~6 trades/month to ~12-18 trades/month
  - **Rationale**: Zero-line filter was too restrictive and missed valid trend-following opportunities
  - **Trade-off**: May increase false signals in ranging markets, but improves opportunity capture in trending markets

### Fixed
 - **Critical crash in S/R detection**: Fixed malformed conditional expression in `detect_sr_levels()` method that was causing syntax errors and crashes in TradeLocker. The expression `if i > 0 else True` was improperly structured. Now uses proper try-except blocks and starts loop at i=2 to ensure both neighbor bars exist for swing point detection.
