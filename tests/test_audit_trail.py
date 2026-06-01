from audit.audit_trail import AuditTrail


def test_audit_trail_records_decision_metadata() -> None:
    trail = AuditTrail()

    event = trail.record_decision("fraud-model", "txn-1", "review", "input-hash", "explanation-1")

    assert event.reviewer_status == "pending_review"
    assert trail.to_json_ready()[0]["decision_id"] == "txn-1"
