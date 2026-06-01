from __future__ import annotations

import math


def score_transaction(amount: float, account_age_days: int, prior_chargebacks: int, country_risk: float) -> float:
    logit = -3.0
    logit += min(amount / 1000, 5) * 0.45
    logit += max(0, 90 - account_age_days) / 90 * 1.2
    logit += prior_chargebacks * 0.9
    logit += country_risk * 1.5
    return 1 / (1 + math.exp(-logit))
