from __future__ import annotations

from .llm_classifier import classify_with_llm_style_rules
from .xgb_baseline import score_transaction


def compare_models(transaction: dict[str, object]) -> dict[str, object]:
    xgb_score = score_transaction(
        amount=float(transaction["amount"]),
        account_age_days=int(transaction["account_age_days"]),
        prior_chargebacks=int(transaction["prior_chargebacks"]),
        country_risk=float(transaction["country_risk"]),
    )
    llm = classify_with_llm_style_rules(str(transaction.get("narrative", "")))
    return {
        "xgb_baseline": {"score": xgb_score, "label": "review" if xgb_score >= 0.5 else "allow"},
        "llm_classifier": llm,
        "recommendation": "use_xgb_for_structured_primary_signal",
    }
