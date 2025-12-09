# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2025-12-09

### Fixed
- **TradeLocker Compatibility**: Removed `enum` module import which is not allowed by TradeLocker security policy
- Replaced `MarketRegime` and `TrendDirection` Enum classes with string constants
- Removed `datetime` module import (not needed)
- Replaced emoji characters (⚠️, ✅, ❌) with ASCII text for encoding compatibility

## [1.0.0] - 2025-12-09

### Added
- **XAUUSDStrategy.py**: Complete multi-factor confluence backtesting strategy
  - Regime detection using ADX + ATR ratio + EMA slope combination
  - Multi-timeframe analysis (4H for trend direction, 15M for entries)
  - Trending regime entries: Pullback to EMA21 with RSI confirmation
  - Ranging regime entries: RSI overbought/oversold at swing levels
  - Key level filter (round numbers, previous day H/L)
  - Trailing stop system activated after 1R profit
  - Risk management per FundedHero trading plan:
    - 1% risk per trade ($25 on $2,500 account)
    - Max 3 trades per day
    - Self-imposed $75 daily loss limit
    - Lot size consistency limits (0.03 - 0.12)
  - 20% consistency rule tracking and violation reporting
  - Backtest summary with Phase 1/2 target validation

- **Plan.md**: FundedHero $2.5K Challenge trading plan documentation
