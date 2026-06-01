from explainability.shap_wrapper import LinearContributionExplainer
from fraud.compare_results import compare_models
from kyc.verifier import verify_document


def test_fraud_comparison_returns_both_models() -> None:
    result = compare_models(
        {
            "amount": 2000,
            "account_age_days": 10,
            "prior_chargebacks": 1,
            "country_risk": 0.7,
            "narrative": "urgent crypto wire",
        }
    )

    assert result["xgb_baseline"]["label"] == "review"
    assert result["llm_classifier"]["label"] == "review"


def test_linear_contribution_explainer_outputs_feature_contributions() -> None:
    explainer = LinearContributionExplainer(["amount", "risk"], [0.5, 2.0], baseline=-1.0)

    explanation = explainer.explain([2.0, 0.5])

    assert explanation.prediction == 1.0
    assert explanation.contributions["amount"] == 1.0


def test_kyc_verifier_flags_missing_fields() -> None:
    result = verify_document("Name: Ada Example\nDocument ID: SYN-12345")

    assert result.manual_review_required is True
    assert "missing_expiry" in result.flags
    assert "missing_address" in result.flags


def test_kyc_verifier_passes_complete_synthetic_document() -> None:
    result = verify_document("Name: Ada Example\nDocument ID: SYN-12345\nExpiry: 2028-12-31\nAddress: 123 Synthetic Street")

    assert result.manual_review_required is False
    assert result.confidence == 1.0
