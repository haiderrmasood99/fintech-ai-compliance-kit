from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Explanation:
    prediction: float
    baseline: float
    contributions: dict[str, float]


class LinearContributionExplainer:
    """A tiny SHAP-style wrapper for linear/tabular demos without heavy dependencies."""

    def __init__(self, feature_names: list[str], coefficients: list[float], baseline: float = 0.0) -> None:
        if len(feature_names) != len(coefficients):
            raise ValueError("feature_names and coefficients must have same length")
        self.feature_names = feature_names
        self.coefficients = np.array(coefficients, dtype=float)
        self.baseline = baseline

    def explain(self, features: list[float]) -> Explanation:
        values = np.array(features, dtype=float)
        if values.shape[0] != self.coefficients.shape[0]:
            raise ValueError("feature length mismatch")
        contributions = values * self.coefficients
        prediction = float(self.baseline + contributions.sum())
        return Explanation(
            prediction=prediction,
            baseline=self.baseline,
            contributions={name: float(value) for name, value in zip(self.feature_names, contributions)},
        )
