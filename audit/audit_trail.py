from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    model_name: str
    decision_id: str
    decision: str
    input_reference: str
    explanation_reference: str
    reviewer_status: str
    created_at: str


class AuditTrail:
    def __init__(self) -> None:
        self.events: list[AuditEvent] = []

    def record_decision(
        self,
        model_name: str,
        decision_id: str,
        decision: str,
        input_reference: str,
        explanation_reference: str,
        reviewer_status: str = "pending_review",
    ) -> AuditEvent:
        event = AuditEvent(
            event_id=str(uuid4()),
            model_name=model_name,
            decision_id=decision_id,
            decision=decision,
            input_reference=input_reference,
            explanation_reference=explanation_reference,
            reviewer_status=reviewer_status,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self.events.append(event)
        return event

    def to_json_ready(self) -> list[dict[str, str]]:
        return [asdict(event) for event in self.events]
