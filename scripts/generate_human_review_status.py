#!/usr/bin/env python3
"""Generate the human-review dashboard from the authoritative matrix."""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "qa" / "human-review" / "REVIEW_MATRIX.csv"
OUTPUT = ROOT / "qa" / "human-review" / "HUMAN_REVIEW_STATUS.md"

FAMILIES = {
    "ai-risk-management": ("AI Risk Management", 12),
    "cloud-ai-security/aws": ("AWS AI Security", 13),
    "cloud-ai-security/google-cloud": ("Google Cloud AI Security", 14),
    "cloud-ai-security/ibm-cloud": ("IBM Cloud AI Security", 15),
    "cloud-ai-security/microsoft-azure": ("Microsoft Azure AI Security", 16),
    "cloud-ai-security/oracle-cloud": ("Oracle Cloud AI Security", 17),
    "iso-iec-42001": ("ISO/IEC 42001", 18),
    "kali-linux-ai-security-forensics": ("Kali Linux AI Security and Forensics", 19),
}


def main() -> None:
    with MATRIX.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    by_family: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row["family"] not in FAMILIES:
            raise SystemExit(f"unexpected family: {row['family']}")
        by_family[row["family"]].append(row)

    counts = Counter(row["status"] for row in rows)
    approved_shas = sorted({row["exact_sha"] for row in rows if row["status"] == "APPROVED" and row["exact_sha"]})
    blockers = sum(1 for row in rows if row["status"] != "APPROVED")
    status = "BLOCKED PENDING HUMAN REVIEW" if blockers else "REVIEWER APPROVAL RECORDED; FINAL RELEASE CONTROLS REQUIRED"

    lines = [
        "# Human Review Status Dashboard",
        "",
        f"**Status: {status}**",
        "",
        "This dashboard is generated from `REVIEW_MATRIX.csv`. It records the reviewer's attestation and does not independently verify reviewer qualifications or the substance of the human review.",
        "",
        "## Overall status",
        "",
        f"- Total required gates: **{len(rows)}**",
        f"- Pending: **{counts.get('PENDING', 0)}**",
        f"- In review: **{counts.get('IN_REVIEW', 0)}**",
        f"- Approved in matrix: **{counts.get('APPROVED', 0)}**",
        f"- Rejected: **{counts.get('REJECTED', 0)}**",
        f"- Reviewed publication SHA: **{', '.join(approved_shas) if approved_shas else 'none'}**",
        "",
        "## Family status",
        "",
        "| Manual family | Tracker | Total | Pending | In review | Approved | Rejected |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    for family, (name, issue) in FAMILIES.items():
        family_counts = Counter(row["status"] for row in by_family[family])
        lines.append(
            f"| {name} | [#{issue}](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/{issue}) "
            f"| {len(by_family[family])} | {family_counts.get('PENDING', 0)} | {family_counts.get('IN_REVIEW', 0)} "
            f"| {family_counts.get('APPROVED', 0)} | {family_counts.get('REJECTED', 0)} |"
        )

    lines += [
        "",
        "## Remaining release control",
        "",
        (
            f"{blockers} matrix rows remain non-approved."
            if blockers
            else "No matrix rows remain pending or rejected. Workflow verification and the repository release decision remain separate actions."
        ),
        "",
        "## Evidence",
        "",
        "- Attestation: `qa/human-review/evidence/alberto-leiva-all-families-attestation-2026-08-02.md`",
        "- Master release issue: [#20](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/20)",
        "- Pull request: [#11](https://github.com/Chpmunk31456/AI-Security-Manuals/pull/11)",
        "",
        "All matrix approvals reference publication SHA `7e634dd197ebb8a697ccb3d0cf61b5160f69b3e4`. Later administrative evidence commits do not alter those reviewed publication files.",
    ]

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"generated {OUTPUT.relative_to(ROOT)} from {len(rows)} gates")


if __name__ == "__main__":
    main()
