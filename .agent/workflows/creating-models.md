---
description: Use when creating ML models for trade decisions, regime classification, or entry/exit signals - ensures proper feature engineering, time-series validation, and integration with the Orchestrator pipeline
---

# Creating Trading Models

## Overview

Trading models are the **decision-makers** that determine whether to trade. They classify market conditions (e.g., TRENDING vs CHOPPY) and enable the Orchestrator to select appropriate strategies.

**Core principle:** A model without proper backtesting and integration is just gambling with extra steps.

## When to Use

- Creating a new classifier (regime, volatility, trend)
- Building entry/exit signal models
- Adding ML-based trade filtering
- Replacing or improving existing `RegimeClassifier`

## Prerequisites

Before starting, verify:

```bash
# Required data in data/raw/
ls ../data/raw/*.csv

# Required dependencies
pip install xgboost pandas scikit-learn
```

## The Process

### 1. Feature Engineering (Use Existing Calculator)

**DO NOT** create raw OHLCV-based models. Use `FeatureCalculator`:

```python
from src.ml.features import FeatureCalculator

feature_calc = FeatureCalculator()
features = feature_calc.calculate_all(df)
# Returns: atr_14, atr_50, adx_14, bb_width_20, ema_dist_50, ema_dist_200
```

Need custom features? **Extend** `FeatureCalculator`, don't bypass it.

### 2. Label Creation (Based on Trading Outcomes)

Labels must reflect **actual trading performance**, not just price direction:

```python
def create_labels(df: pd.DataFrame, features: pd.DataFrame) -> pd.Series:
    """
    TRENDING (1): ADX > 25 AND significant price movement
    CHOPPY (0): ADX < 25 OR range-bound
    """
    adx = features['adx_14']
    forward_returns = df['close'].pct_change(5).shift(-5)
    
    trending_adx = adx > 25
    significant_move = forward_returns.abs() > 0.003  # 0.3% in 5 bars
    
    return (trending_adx & significant_move).astype(int)
```

**Red flag:** If labels don't relate to tradeable outcomes, you're optimizing the wrong thing.

### 3. Train/Test Split (Time-Series Aware)

**NEVER** use `shuffle=True` for time-series data:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features_clean, labels_clean,
    test_size=0.2,
    random_state=42,
    shuffle=False  # CRITICAL: preserve time order
)
```

### 4. Model Training (Follow RegimeClassifier Pattern)

```python
from src.ml.classifier import RegimeClassifier

classifier = RegimeClassifier()
metrics = classifier.train(X_train, y_train)

print(f"Training accuracy: {metrics['accuracy']*100:.1f}%")
print(f"Feature importance: {metrics['feature_importance']}")
```

### 5. Validation (Test Set Performance)

```python
test_preds = classifier.predict(X_test)
test_accuracy = (test_preds == y_test).mean()
print(f"Test accuracy: {test_accuracy*100:.1f}%")

# If test << train accuracy, you're overfitting
```

### 6. Save Model (Standard Location)

```python
from pathlib import Path

model_path = Path(__file__).parent.parent / "models" / "your_model.pkl"
classifier.save(str(model_path))
```

**Location:** All models go in `models/` as `.pkl` files.

### 7. Integration with Orchestrator

Update `Orchestrator` to use the new model:

```python
# In orchestrator.py
def run(self, df, current_time=None):
    # Calculate features
    features = self.feature_calculator.calculate_all(df)
    
    # Get model prediction
    if self.classifier.model is not None:
        regime_result = self.classifier.predict_regime(features)
        regime = regime_result['regime']
        confidence = regime_result['confidence']
```

## Common Rationalizations (And Why They're Wrong)

| Excuse | Reality |
|--------|---------|
| "Raw OHLCV is enough for the model" | Models need engineered features. FeatureCalculator exists for a reason. |
| "I'll test on the same data I trained on" | That's not testing, that's memorizing. Use train_test_split. |
| "Shuffling the data gives more samples" | Destroys time-series structure. Future data leaks into training. |
| "98% accuracy is great!" | Check TEST accuracy. Training accuracy is meaningless. |
| "I'll integrate later" | Dead models don't trade. Wire it to Orchestrator now. |
| "I'll save it somewhere convenient" | `models/` directory. `.pkl` format. No exceptions. |

## File Structure Reference

```
AlgoTradingProject/
├── models/
│   └── regime_classifier.pkl     # Trained model files
├── python/
│   ├── src/ml/
│   │   ├── classifier.py         # RegimeClassifier (template)
│   │   └── features.py           # FeatureCalculator
│   ├── train_classifier.py       # Training script (reference)
│   └── src/core/
│       └── orchestrator.py       # Model integration point
```

## Verification Checklist

Before considering work complete:

- [ ] Features calculated via `FeatureCalculator` (not raw OHLCV)
- [ ] Labels based on trading outcomes (not arbitrary)
- [ ] Train/test split with `shuffle=False`
- [ ] Test accuracy reported (not just training)
- [ ] Model saved to `models/` as `.pkl`
- [ ] Integrated with or wired to `Orchestrator`
- [ ] Ran `python train_*.py` successfully with output

## Red Flags - STOP and Reconsider

- Using raw price data without feature engineering
- No train/test split
- Test accuracy not reported
- Model file saved outside `models/`
- No clear path to Orchestrator integration
- "I tested manually" (run the script)

## Quick Start Template

```python
#!/usr/bin/env python3
"""Train a new trading model."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import pandas as pd
from sklearn.model_selection import train_test_split

from src.ml.features import FeatureCalculator
from src.ml.classifier import RegimeClassifier  # Or your custom class

def main():
    # 1. Load data
    df = pd.read_csv("../data/raw/XAUUSD.csv", ...)
    
    # 2. Calculate features
    feature_calc = FeatureCalculator()
    features = feature_calc.calculate_all(df)
    
    # 3. Create labels (customize for your use case)
    labels = create_your_labels(df, features)
    
    # 4. Split (time-series aware)
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, shuffle=False
    )
    
    # 5. Train
    classifier = RegimeClassifier()
    metrics = classifier.train(X_train, y_train)
    
    # 6. Validate
    test_preds = classifier.predict(X_test)
    print(f"Test accuracy: {(test_preds == y_test).mean()*100:.1f}%")
    
    # 7. Save
    classifier.save("../models/your_model.pkl")

if __name__ == '__main__':
    main()
```
