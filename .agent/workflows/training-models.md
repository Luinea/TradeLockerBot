---
description: Use when training ML models for trading - ensures reproducibility, proper hyperparameter logging, experiment tracking, and validation monitoring; prevents overfitting and non-reproducible results
---

# Training Models Workflow

## Overview

Training produces the **weights** that power your trading decisions. Poor training = poor trades.

**Core principle:** Every training run must be reproducible and comparable to previous runs.

## When to Use

- Running `train_*.py` scripts
- Tuning hyperparameters
- Comparing model performance across experiments
- Re-training after data updates

## The Training Discipline

### 1. Set Random Seeds (Reproducibility)

**ALWAYS** set seeds before training:

```python
import numpy as np
import random

RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

# In XGBoost/sklearn
classifier = RegimeClassifier(params={'random_state': RANDOM_SEED})
```

**Why:** Without seeds, you can't reproduce results. "It worked yesterday" is worthless.

### 2. Log Hyperparameters

Record EVERY hyperparameter before training:

```python
params = {
    'n_estimators': 100,
    'max_depth': 4,
    'learning_rate': 0.1,
    'random_state': 42
}

print("=" * 50)
print("Training Configuration")
print("=" * 50)
for k, v in params.items():
    print(f"  {k}: {v}")
```

**Why:** You'll forget what settings produced good results.

### 3. Monitor Class Imbalance

Check label distribution BEFORE training:

```python
print(f"TRENDING (1): {labels.sum():,} ({labels.mean()*100:.1f}%)")
print(f"CHOPPY (0): {(~labels.astype(bool)).sum():,} ({(1-labels.mean())*100:.1f}%)")

# If heavily imbalanced (>70/30), consider:
# - class_weight='balanced' in sklearn
# - scale_pos_weight in XGBoost
```

**Why:** 95% accuracy on 95/5 split is just predicting the majority class.

### 4. Use Validation Set for Early Stopping

Don't train blind - monitor validation loss:

```python
# Split: train/val/test (60/20/20)
X_train, X_temp, y_train, y_temp = train_test_split(
    features, labels, test_size=0.4, shuffle=False
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, shuffle=False
)

# Train with early stopping
classifier.train(X_train, y_train, eval_set=(X_val, y_val))
```

**Why:** Validation loss increasing = overfitting. Stop early.

### 5. Log All Metrics

Capture training output systematically:

```python
metrics = classifier.train(X_train, y_train)

results = {
    'timestamp': datetime.now().isoformat(),
    'train_accuracy': metrics['accuracy'],
    'test_accuracy': (classifier.predict(X_test) == y_test).mean(),
    'n_train': len(X_train),
    'n_test': len(X_test),
    'feature_importance': metrics['feature_importance'],
    'params': params
}

# Save to experiment log
with open('training_log.json', 'a') as f:
    f.write(json.dumps(results) + '\n')
```

### 6. Compare to Baseline

Always report improvement over previous best:

```python
PREVIOUS_BEST = 0.72  # From last experiment

print(f"Test accuracy: {test_accuracy:.1%}")
print(f"Previous best: {PREVIOUS_BEST:.1%}")
print(f"Improvement:   {(test_accuracy - PREVIOUS_BEST):+.1%}")
```

### 7. Save with Metadata

Include training context in saved model:

```python
# In RegimeClassifier.save() or wrapper
save_data = {
    'model': self.model,
    'feature_names': self.feature_names,
    'params': self.params,
    'train_date': datetime.now().isoformat(),
    'train_accuracy': metrics['accuracy'],
    'test_accuracy': test_accuracy
}
```

## Common Rationalizations (And Why They're Wrong)

| Excuse | Reality |
|--------|---------|
| "I'll remember the hyperparameters" | You won't. Log them. |
| "Random seeds don't matter for production" | Debugging matters. You need reproducibility. |
| "Class imbalance is fine, accuracy is 95%" | You're predicting majority class. Check precision/recall. |
| "I don't need validation, I have test set" | Test set is for final evaluation only. Use validation for tuning. |
| "Training took an hour, I can't re-run" | That's why you log everything. One wasted hour now saves 10 later. |
| "The model improved, ship it" | Improved over what? Compare to baseline. |

## Training Script Template

```python
#!/usr/bin/env python3
"""Train model with proper discipline."""

import json
from datetime import datetime
from pathlib import Path
import numpy as np
import random

# Set seeds FIRST
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

def main():
    # 1. Log configuration
    params = {'n_estimators': 100, 'max_depth': 4, 'random_state': RANDOM_SEED}
    print(f"Config: {params}")
    
    # 2. Load data & features (see /creating-models)
    ...
    
    # 3. Check class balance
    print(f"Class balance: {labels.mean():.1%} positive")
    
    # 4. Split with validation
    X_train, X_temp, y_train, y_temp = train_test_split(
        features, labels, test_size=0.4, shuffle=False
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, shuffle=False
    )
    
    # 5. Train with monitoring
    classifier = RegimeClassifier(params)
    metrics = classifier.train(X_train, y_train, eval_set=(X_val, y_val))
    
    # 6. Evaluate
    test_acc = (classifier.predict(X_test) == y_test).mean()
    print(f"Train: {metrics['accuracy']:.1%}, Test: {test_acc:.1%}")
    
    # 7. Log experiment
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'params': params,
        'train_acc': metrics['accuracy'],
        'test_acc': test_acc
    }
    print(f"Result: {json.dumps(log_entry)}")
    
    # 8. Save model
    classifier.save("../models/model.pkl")

if __name__ == '__main__':
    main()
```

## Verification Checklist

Before marking training complete:

- [ ] Random seed set at script start
- [ ] Hyperparameters logged to console/file
- [ ] Class imbalance checked and addressed
- [ ] Validation set used (train/val/test split)
- [ ] Both train AND test accuracy reported
- [ ] Compared to previous baseline
- [ ] Training config saved with model

## Red Flags - STOP

- No random seed → Results not reproducible
- Only training accuracy reported → Overfitting hidden
- No class balance check → Accuracy is misleading
- "Trust me it's better" → Show the comparison
