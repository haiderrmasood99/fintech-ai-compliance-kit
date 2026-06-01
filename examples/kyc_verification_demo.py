from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from kyc.verifier import verify_document


def main() -> None:
    synthetic_doc = """Name: Ada Example
Document ID: SYN-12345
Expiry: 2028-12-31
Address: 123 Synthetic Street
"""
    result = verify_document(synthetic_doc)
    print("KYC verification")
    print(result)


if __name__ == "__main__":
    main()
