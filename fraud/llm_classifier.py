from __future__ import annotations


RISK_TERMS = {"urgent", "gift card", "crypto", "wire", "password", "unusual", "third party"}


def classify_with_llm_style_rules(narrative: str) -> dict[str, object]:
    lowered = narrative.lower()
    hits = sorted(term for term in RISK_TERMS if term in lowered)
    score = min(0.95, 0.15 + 0.18 * len(hits))
    return {
        "label": "review" if score >= 0.5 else "allow",
        "score": score,
        "reasons": hits,
    }
