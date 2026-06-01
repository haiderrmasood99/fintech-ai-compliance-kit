# fintech-ai-compliance-kit

SR 11-7 is not just paperwork. It changes your architecture.

This repo translates model risk, explainability, auditability, fraud comparison, and KYC verification into concrete engineering artifacts.

Educational only. This is not legal, regulatory, banking, or compliance advice.

## Quickstart

```powershell
cd "D:\W6H\Github Content\fintech-ai-compliance-kit"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
python examples\fraud_detection_demo.py
python examples\kyc_verification_demo.py
python -m pytest
```

## Architecture

```text
model decision -> explanation -> audit event -> reviewer status -> model card evidence
KYC document -> extraction -> validation -> confidence -> manual review flag
```

## Fraud Comparison

| Approach | Best When | Weakness |
|---|---|---|
| XGBoost-style baseline | structured transaction signals | weak on free-text narratives |
| LLM classifier | messy document or narrative context | slower, costlier, harder to calibrate |

The demo is honest: the classical baseline wins on clean structured data.

## What It Contains

- `compliance/model_card.py`: SR 11-7-style model card generator.
- `compliance/model_card_template.md`: human-readable template.
- `explainability/shap_wrapper.py`: dependency-light SHAP-style contribution wrapper.
- `audit/audit_trail.py`: decision audit trail with reviewer state.
- `fraud/`: classical baseline, LLM-style classifier, comparison helper.
- `kyc/verifier.py`: synthetic KYC extraction and validation pipeline.
