# fintech-ai-compliance-kit

A beginner-friendly engineering starter kit for compliance-aware AI in financial workflows.

Financial AI systems are not judged only by prediction accuracy. Teams also need documentation, validation evidence, explanations, audit trails, review states, and clear limits on where a model should be used. This repository turns those ideas into small, runnable Python examples.

This project is educational only. It is not legal, regulatory, banking, investment, or compliance advice.

## What This Project Includes

- A model card generator for documenting model purpose, data, validation, limits, monitoring, and ownership.
- A human-readable model card template.
- A lightweight SHAP-style explanation wrapper for tabular models.
- An audit trail object for model decisions and reviewer state.
- A fraud detection comparison between a structured baseline and an LLM-style rule classifier.
- A synthetic KYC document verification pipeline.

## Project Structure

```text
.
|-- audit/
|   `-- audit_trail.py
|-- compliance/
|   |-- model_card.py
|   `-- model_card_template.md
|-- examples/
|   |-- fraud_detection_demo.py
|   `-- kyc_verification_demo.py
|-- explainability/
|   `-- shap_wrapper.py
|-- fraud/
|   |-- compare_results.py
|   |-- llm_classifier.py
|   `-- xgb_baseline.py
|-- kyc/
|   `-- verifier.py
|-- tests/
|-- pyproject.toml
`-- README.md
```

## Quickstart

Clone the repository:

```bash
git clone https://github.com/haiderrmasood99/fintech-ai-compliance-kit.git
cd fintech-ai-compliance-kit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the package with test dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the demos:

```bash
python examples/fraud_detection_demo.py
python examples/kyc_verification_demo.py
```

Run the tests:

```bash
python -m pytest
```

## How The Pieces Fit Together

```text
model decision -> explanation -> audit event -> reviewer status -> model card evidence
KYC document -> extraction -> validation -> confidence score -> manual review flag
```

The goal is to show how engineering artifacts support review and accountability. The examples are intentionally small so you can read the whole flow in one sitting.

## Fraud Comparison

| Approach | Best When | Weakness |
|---|---|---|
| Structured baseline | You have clean transaction features such as amount, account age, chargebacks, and country risk | It does not understand messy text or document narratives |
| LLM-style classifier | You have free-text explanations, document notes, or ambiguous descriptions | It can be slower, harder to calibrate, and more expensive |

The demo is intentionally honest: a classical structured model can be the better primary signal when the data is clean and tabular.

## KYC Demo

The KYC verifier uses synthetic document text. It extracts fields, checks required values, calculates confidence, and flags cases that need manual review.

It does not process real identity documents, upload files, call external APIs, or store personal data.

## Model Card Template

Use `compliance/model_card_template.md` when you need a human-readable checklist for:

- Model purpose.
- Intended use.
- Data lineage.
- Validation.
- Limitations.
- Monitoring.
- Governance.

## Production Notes

- Keep real customer data out of git.
- Store audit records in an append-only system with access control.
- Review model limitations with legal, compliance, risk, and business owners.
- Monitor drift, override rates, reviewer outcomes, and segment-level performance.
- Treat explanations as evidence for review, not as proof that a model is correct.
