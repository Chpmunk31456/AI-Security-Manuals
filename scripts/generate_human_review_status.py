#!/usr/bin/env python3
"""Generate a deterministic Markdown dashboard from the human-review matrix."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "qa" / "human-review" / "REVIEW_MATRIX.csv"
OUTPUT = ROOT / "qa" / "human-review" / "HUMAN_REVIEW_STATUS.md"

ISSUES = {
    "ai-risk-management": 12,
    "aws": 13,
    "google-cloud": 14,
    "ibm-cloud": 15,
    "microsoft-azure": 16,
    "oracle-cloud": 17,
    "iso-iec-42001": 18,
    "kali-linux-ai-security-forensics": 19,
}

FAMILY_NAMES = {
    "ai-risk-management": "AI Risk Management",
    "aws": "AWS AI Security",
    "google-cloud": "Google Cloud AI Security",
    "ibm-cloud": "IBM Cloud AI Security",
    "microsoft-azure": "Microsoft Azure AI Security",
    "oracle-cloud": "Oracle Cloud AI Security",
    "iso-iec-42001": "ISO/IEC 42001",
    "kali-linux-ai-security-forensics": "Kali Linux AI Security and Forensics",
}


def main() -> None:
    with MATRIX.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    required = {"gate_id", "family", "language", "discipline", "status", "reviewer", "evidence_path", "exact_sha", "completed_date", "notes"}
    if not rows or not required.issubset(rows[0]):
        raise SystemExit("review matrix is empty or missing required columns")

    by_family: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_family[row["family"]].append(row)

    overall = Counter(row["status"] for row in rows)
    approved_shas = sorted({row["exact_sha"] for row in rows if row["status"] == "APPROVED" and row["exact_sha"]})

    lines = [
        "# Human Review Status Dashboard",
        "",
        "**Publication status: BLOCKED PENDING HUMAN REVIEW**",
        "",
        "This dashboard is generated from `REVIEW_MATRIX.csv`. It reports evidence state only; it does not create or imply approval.",
        "",
        "## Overall status",
        "",
        f"- Total required gates: **{len(rows)}**",
        f"- Pending: **{overall.get('PENDING', 0)}**",
        f"- In review: **{overall.get('IN_REVIEW', 0)}**",
        f"- Approved: **{overall.get('APPROVED', 0)}**",
        f"- Rejected: **{overall.get('REJECTED', 0)}**",
        f"- Approved exact SHA set: **{', '.join(approved_shas) if approved_shas else 'none'}**",
        "",
        "## Family status",
        "",
        "| Manual family | Tracker | Total | Pending | In review | Approved | Rejected |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    for family in FAMILY_NAMES:
        family_rows = by_family.get(family, [])
        counts = Counter(row["status"] for row in family_rows)
        issue = ISSUES[family]
        lines.append(
            f"| {FAMILY_NAMES[family]} | [#{issue}](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/{issue}) "
            f"| {len(family_rows)} | {counts.get('PENDING', 0)} | {counts.get('IN_REVIEW', 0)} "
            f"| {counts.get('APPROVED', 0)} | {counts.get('REJECTED', 0)} |"
        )

    lines += [
        "",
        "## Release blockers",
        "",
    ]
    blockers = [row for row in rows if row["status"] != "APPROVED"]
    if blockers:
        for row in blockers:
            lines.append(
                f"- `{row['gate_id']}` — `{row['family']}` / `{row['language']}` / `{row['discipline']}` — **{row['status']}**"
            )
    else:
        lines.append("- No matrix blockers remain. Final exact-SHA and workflow verification is still required before release.")

    lines += [
        "",
        "## Control references",
        "",
        "- Master release issue: [#20](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/20)",
        "- Draft publication PR: [#11](https://github.com/Chpmunk31456/AI-Security-Manuals/pull/11)",
        "- Evidence rules: `qa/human-review/README.md`",
        "- Attestation template: `qa/human-review/REVIEW_ATTESTATION_TEMPLATE.md`",
        "- Review packet workflow: `.github/workflows/build-human-review-packets.yml`",
        "",
        "Do not mark PR #11 ready or merge it until every required gate has attributable evidence at one frozen exact candidate SHA.",
    ]

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"generated {OUTPUT.relative_to(ROOT)} from {len(rows)} gates")


if __name__ == "__main__":
    main()
