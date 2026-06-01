from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class KycVerificationResult:
    extracted_fields: dict[str, str]
    confidence: float
    flags: list[str]
    manual_review_required: bool


def verify_document(text: str) -> KycVerificationResult:
    fields = {
        "name": _extract(r"Name:\s*([A-Za-z ]+)", text),
        "document_id": _extract(r"Document ID:\s*([A-Z0-9-]+)", text),
        "expiry": _extract(r"Expiry:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text),
        "address": _extract(r"Address:\s*(.+)", text),
    }
    flags: list[str] = []
    for key, value in fields.items():
        if not value:
            flags.append(f"missing_{key}")
    if "expired" in text.lower():
        flags.append("document_marked_expired")
    confidence = max(0.0, 1.0 - 0.2 * len(flags))
    return KycVerificationResult(fields, confidence, flags, manual_review_required=bool(flags) or confidence < 0.8)


def _extract(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.I)
    return match.group(1).strip() if match else ""
