# Changelog

All notable changes to the TradeLockerBot project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- **Critical crash in S/R detection**: Fixed malformed conditional expression in `detect_sr_levels()` method that was causing syntax errors and crashes in TradeLocker. The expression `if i > 0 else True` was improperly structured. Now uses proper try-except blocks and starts loop at i=2 to ensure both neighbor bars exist for swing point detection.
- **London Breakout Strategy Permanent Lock Bug (2025-12-10)**:
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
- **EMA SL multiplier increased**: `ema_sl_multiplier` from 1.0 to 1.5 to provide more breathing room for trend pullbacks
- **Zero-line filter REMOVED**: MACD crossovers now allowed at any level (not just below/above zero) to increase trade frequency from 6 to 12-18 trades/month
- **S/R filter default**: Changed to OFF (`use_sr_filter=False`) after testing showed it was too restrictive
- **Rationale**: Backtest analysis (Feb 2025) showed:
  - 10-pip SL too tight: 64% stop loss hit rate, only 33% win rate on minimum SL trades
  - Zero-line filter too restrictive: Only 6 trades/month, limiting profitability
  - With optimizations: 50% win rate, +2.04% ROI, 2.04% max drawdown
  - Expected with zero-line removal: 12-18 trades/month, maintaining 45-50% win rate target

### Changed - MacdStrategy Enhancement (TradingLab Rules)
- **Zero-line crossover filter**: Long entries now require MACD to cross above signal while both are below zero line; short entries require crossing below signal while both are above zero line (per TradingLab video methodology)
- **200 EMA-based stop loss**: Stop loss now calculated dynamically based on distance to 200 EMA instead of fixed 20 pips, with configurable multiplier (`ema_sl_multiplier`) and minimum distance safeguard (`min_sl_distance`)
- **Risk/Reward ratio**: Updated from 2.0:1 to 1.5:1 as per TradingLab strategy specification
- **Enhanced logging**: Entry logs now include SL distance for better trade analysis

### Added - MacdStrategy Enhancement
- Support/Resistance detection using swing high/low algorithm with configurable lookback period
- Price action filter: Long entries require price near support level; short entries require price near resistance level
- New parameters:
  - `min_sl_distance` (10.0): Minimum SL distance as fallback when EMA distance is too small
  - `ema_sl_multiplier` (1.0): Multiplier for EMA-based SL distance calculation
  - `sr_lookback` (20): Number of bars to look back for swing high/low detection
  - `sr_threshold` (5.0): Maximum price distance to S/R level for trade confirmation
  - `use_sr_filter` (True): Toggle to enable/disable S/R filtering
- Helper methods:
  - `detect_sr_levels()`: Identifies support and resistance levels from recent price action
  - `near_support()`: Checks if current price is within threshold of any support level
  - `near_resistance()`: Checks if current price is within threshold of any resistance level

### Removed
- Fixed `sl_pips` parameter (replaced by dynamic EMA-based calculation)

## [Earlier Versions]

Previous changes were not tracked in this changelog.
