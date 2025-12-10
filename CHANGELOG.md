# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added - EUR_USD Professional Trading Strategy (2025-12-10)
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
