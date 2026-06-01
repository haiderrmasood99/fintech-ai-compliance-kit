from compliance.model_card import ModelCard, ValidationMetric


def test_model_card_generates_markdown_and_review_status() -> None:
    card = ModelCard(
        model_name="fraud-xgb",
        owner="risk-team",
        purpose="Flag high-risk transactions for review.",
        intended_use="Decision support only.",
        dataset="Synthetic transaction data.",
        limitations=["Not calibrated for new geographies."],
        validation_metrics=[ValidationMetric("auc", 0.91, 0.85)],
        monitoring_plan="Track drift and override rate weekly.",
    )

    markdown = card.to_markdown()

    assert "Model Card: fraud-xgb" in markdown
    assert card.is_ready_for_review() is True
