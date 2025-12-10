# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
- **London Breakout 0.0 Lots Bug (2025-12-10)**:
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
