from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from audit.audit_trail import AuditTrail
from explainability.shap_wrapper import LinearContributionExplainer
from fraud.compare_results import compare_models


def main() -> None:
    transaction = {
        "amount": 1850,
        "account_age_days": 12,
        "prior_chargebacks": 1,
        "country_risk": 0.6,
        "narrative": "Urgent third party wire request with crypto notes.",
    }
    comparison = compare_models(transaction)
    explainer = LinearContributionExplainer(
        ["amount_k", "new_account", "chargebacks", "country_risk"],
        [0.45, 1.2, 0.9, 1.5],
        baseline=-3.0,
    )
    explanation = explainer.explain([1.85, 0.86, 1, 0.6])
    audit = AuditTrail()
    event = audit.record_decision(
        model_name="fraud-xgb-baseline",
        decision_id="txn-001",
        decision=comparison["xgb_baseline"]["label"],
        input_reference="txn-hash-001",
        explanation_reference="explanation-001",
    )
    print("Fraud comparison")
    print(comparison)
    print("Explanation")
    print(explanation)
    print("Audit event")
    print(event)


if __name__ == "__main__":
    main()
