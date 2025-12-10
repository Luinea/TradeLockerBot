# Changelog

All notable changes to the TradeLockerBot project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
