from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class ValidationMetric:
    name: str
    value: float
    threshold: float

    @property
    def passed(self) -> bool:
        return self.value >= self.threshold


@dataclass
class ModelCard:
    model_name: str
    owner: str
    purpose: str
    intended_use: str
    dataset: str
    limitations: list[str]
    validation_metrics: list[ValidationMetric]
    monitoring_plan: str
    approval_status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_markdown(self) -> str:
        metrics = "\n".join(
            f"- {metric.name}: {metric.value:.3f} (threshold {metric.threshold:.3f}) - {'pass' if metric.passed else 'fail'}"
            for metric in self.validation_metrics
        )
        limitations = "\n".join(f"- {item}" for item in self.limitations)
        return f"""# Model Card: {self.model_name}

Owner: {self.owner}
Status: {self.approval_status}
Created: {self.created_at}

## Purpose
{self.purpose}

## Intended Use
{self.intended_use}

## Dataset
{self.dataset}

## Limitations
{limitations}

## Validation
{metrics}

## Monitoring Plan
{self.monitoring_plan}
"""

    def is_ready_for_review(self) -> bool:
        return bool(self.owner and self.purpose and self.validation_metrics) and all(metric.passed for metric in self.validation_metrics)
