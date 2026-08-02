#!/usr/bin/env python3
"""Validate the fail-closed human-review release matrix.

This validator never creates or infers an approval. It verifies schema,
controlled status values, evidence requirements, attributable identity, dates,
and exact-SHA consistency. The repository remains blocked while any row is
PENDING or CHANGES_REQUIRED.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "qa" / "human-review" / "REVIEW_MATRIX.csv"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED_COLUMNS = [
    "gate_id", "family", "language", "discipline", "status", "reviewer",
    "evidence_path", "exact_sha", "completed_date", "notes",
]
ALLOWED_STATUS = {"PENDING", "APPROVED", "APPROVED_WITH_LIMITATIONS", "CHANGES_REQUIRED"}
APPROVAL_STATUS = {"APPROVED", "APPROVED_WITH_LIMITATIONS"}


def main() -> int:
    errors: list[str] = []
    with MATRIX.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != REQUIRED_COLUMNS:
            errors.append(f"unexpected columns: {reader.fieldnames!r}")
        rows = list(reader)

    gate_ids = [row.get("gate_id", "") for row in rows]
    duplicates = sorted(gate for gate, count in Counter(gate_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate gate IDs: {duplicates}")

    approval_shas: set[str] = set()
    status_counts: Counter[str] = Counter()
    for line_number, row in enumerate(rows, 2):
        status = row.get("status", "")
        status_counts[status] += 1
        if status not in ALLOWED_STATUS:
            errors.append(f"line {line_number}: invalid status {status!r}")
            continue

        evidence = row.get("evidence_path", "").strip()
        reviewer = row.get("reviewer", "").strip()
        exact_sha = row.get("exact_sha", "").strip()
        completed = row.get("completed_date", "").strip()

        if status in APPROVAL_STATUS | {"CHANGES_REQUIRED"}:
            if not reviewer:
                errors.append(f"line {line_number}: attributable reviewer required")
            if not evidence:
                errors.append(f"line {line_number}: evidence path required")
            else:
                evidence_file = (ROOT / evidence).resolve()
                if ROOT.resolve() not in evidence_file.parents:
                    errors.append(f"line {line_number}: evidence path escapes repository")
                elif not evidence_file.is_file():
                    errors.append(f"line {line_number}: evidence file does not exist: {evidence}")
            if not SHA_RE.fullmatch(exact_sha):
                errors.append(f"line {line_number}: exact 40-character SHA required")
            if not DATE_RE.fullmatch(completed):
                errors.append(f"line {line_number}: completion date must be YYYY-MM-DD")

        if status in APPROVAL_STATUS:
            approval_shas.add(exact_sha)
        if status == "APPROVED_WITH_LIMITATIONS" and not row.get("notes", "").strip():
            errors.append(f"line {line_number}: limitations must be recorded in notes")

    if len(approval_shas) > 1:
        errors.append(f"approvals reference multiple candidate SHAs: {sorted(approval_shas)}")

    pending = status_counts["PENDING"]
    changes = status_counts["CHANGES_REQUIRED"]
    print(f"rows={len(rows)} status_counts={dict(status_counts)}")
    if errors:
        print("MATRIX INVALID")
        for error in errors:
            print(f"- {error}")
        return 2
    if pending or changes:
        print(f"BLOCKED PENDING HUMAN REVIEW: pending={pending}, changes_required={changes}")
        return 0
    print("HUMAN REVIEW MATRIX COMPLETE — separate merge authorization is still required")
    return 0


if __name__ == "__main__":
    sys.exit(main())
