#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
REPORT_JSON = ROOT / "final-integrity-report.json"
REPORT_MD = ROOT / "final-integrity-report.md"

errors: list[str] = []
warnings: list[str] = []
metrics: dict[str, int] = {}


def add_error(msg: str) -> None:
    errors.append(msg)


def add_warning(msg: str) -> None:
    warnings.append(msg)


def markdown_links(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if "\ufffd" in text:
        add_warning(f"Unicode replacement character found: {path.relative_to(ROOT)}")
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1).strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        yield target


def check_markdown_links() -> None:
    md_files = sorted(ROOT.rglob("*.md"))
    total = 0
    for md in md_files:
        for target in markdown_links(md):
            total += 1
            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                add_error(f"Local link escapes repository: {md.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                add_error(f"Broken local link: {md.relative_to(ROOT)} -> {target}")
    metrics["markdown_files"] = len(md_files)
    metrics["local_links"] = total


def check_docx() -> None:
    files = sorted(ROOT.rglob("*.docx"))
    required = {"[Content_Types].xml", "word/document.xml", "_rels/.rels"}
    for path in files:
        try:
            with zipfile.ZipFile(path) as zf:
                bad = zf.testzip()
                if bad:
                    add_error(f"Corrupt DOCX member {bad}: {path.relative_to(ROOT)}")
                names = set(zf.namelist())
                missing = required - names
                if missing:
                    add_error(f"DOCX missing package parts {sorted(missing)}: {path.relative_to(ROOT)}")
                xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
                plain = re.sub(r"<[^>]+>", " ", xml)
                plain = re.sub(r"\s+", " ", plain).strip()
                if len(plain) < 500:
                    add_error(f"DOCX appears near-empty: {path.relative_to(ROOT)}")
                if "\ufffd" in plain:
                    add_warning(f"DOCX contains replacement characters: {path.relative_to(ROOT)}")
        except Exception as exc:
            add_error(f"DOCX cannot be opened: {path.relative_to(ROOT)} ({exc})")
    metrics["docx_files"] = len(files)


def check_pdfs() -> None:
    files = sorted(ROOT.rglob("*.pdf"))
    for path in files:
        try:
            data = path.read_bytes()
            if not data.startswith(b"%PDF-"):
                add_error(f"Invalid PDF signature: {path.relative_to(ROOT)}")
                continue
            reader = PdfReader(path)
            if not reader.pages:
                add_error(f"PDF has no pages: {path.relative_to(ROOT)}")
                continue
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            if len(re.sub(r"\s+", "", text)) < 300:
                add_error(f"PDF is not sufficiently searchable: {path.relative_to(ROOT)}")
        except Exception as exc:
            add_error(f"PDF cannot be inspected: {path.relative_to(ROOT)} ({exc})")
    metrics["pdf_files"] = len(files)


def check_language_inventory() -> None:
    manual_roots = [p for p in (ROOT / "manuals").rglob("*") if p.is_dir() and (p / "en").is_dir()]
    for manual in sorted(manual_roots):
        rel = manual.relative_to(ROOT)
        for locale in ("en", "es-419", "pt-BR"):
            loc = manual / locale
            if not loc.is_dir():
                add_error(f"Missing language directory {locale}: {rel}")
                continue
            docx = list(loc.glob("*.docx"))
            pdf = list(loc.glob("*.pdf"))
            if len(docx) != 1:
                add_error(f"Expected exactly one DOCX in {rel / locale}, found {len(docx)}")
            if len(pdf) != 1:
                add_error(f"Expected exactly one PDF in {rel / locale}, found {len(pdf)}")
            if not (loc / "README.md").exists():
                add_warning(f"Missing language README: {rel / locale}")
    metrics["manual_families"] = len(manual_roots)


def check_root_catalog() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for path in sorted((ROOT / "manuals").rglob("*.docx")) + sorted((ROOT / "manuals").rglob("*.pdf")):
        rel = path.relative_to(ROOT).as_posix()
        if rel not in readme:
            add_warning(f"Binary not listed in root README catalog: {rel}")


def write_reports() -> None:
    result = {"status": "fail" if errors else "pass", "metrics": metrics, "errors": errors, "warnings": warnings}
    REPORT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Final Integrity Audit", "", f"**Status:** {'FAIL' if errors else 'PASS'}", "", "## Metrics"]
    for key, val in sorted(metrics.items()):
        lines.append(f"- {key.replace('_', ' ').title()}: {val}")
    lines += ["", "## Errors"]
    lines += [f"- {e}" for e in errors] or ["- None"]
    lines += ["", "## Warnings"]
    lines += [f"- {w}" for w in warnings] or ["- None"]
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    check_markdown_links()
    check_docx()
    check_pdfs()
    check_language_inventory()
    check_root_catalog()
    write_reports()
    print(REPORT_MD.read_text(encoding="utf-8"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
