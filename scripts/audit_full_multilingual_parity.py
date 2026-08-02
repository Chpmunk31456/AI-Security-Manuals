#!/usr/bin/env python3
"""Fail-closed structural and package parity audit for AI Security Manuals."""
from __future__ import annotations
import hashlib, json, re, sys, zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from docx import Document
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MANUALS = ROOT / "manuals"
QA = ROOT / "qa" / "full-multilingual-parity"
QA.mkdir(parents=True, exist_ok=True)
LANGS = ("en", "es-419", "pt-BR")
PROTECTED = re.compile(r"(?:https?://\S+|\b(?:ISO(?:/IEC)?|NIST|OWASP|MITRE|AWS|Azure|Google Cloud|Oracle Cloud|IBM Cloud|CVE|API|CLI|IAM|MFA|TLS|HTTP|HTTPS|TCP|UDP|JSON|YAML|XML|PDF|DOCX)\b|\b\d+(?:\.\d+){1,4}\b|\b[A-Z]{2,}(?:-[A-Z0-9]+)*\b)")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def docx_info(path: Path) -> dict:
    out = {"valid": False, "paragraphs": 0, "words": 0, "headings": [], "tables": 0, "images": 0, "tokens": {}}
    try:
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            if bad:
                out["error"] = f"corrupt ZIP member: {bad}"
                return out
            out["images"] = sum(1 for n in z.namelist() if n.startswith("word/media/"))
        doc = Document(path)
        texts = []
        for p in doc.paragraphs:
            t = p.text.strip()
            if not t:
                continue
            texts.append(t)
            if p.style and p.style.name.lower().startswith("heading"):
                out["headings"].append({"style": p.style.name, "text": t})
        for table in doc.tables:
            for row in table.rows:
                texts.extend(c.text.strip() for c in row.cells if c.text.strip())
        full = "\n".join(texts)
        out.update(valid=True, paragraphs=len(texts), words=len(re.findall(r"\b\w+\b", full)), tables=len(doc.tables), tokens=dict(Counter(PROTECTED.findall(full))))
    except Exception as e:
        out["error"] = repr(e)
    return out


def pdf_info(path: Path) -> dict:
    out = {"valid": False, "pages": 0, "words": 0, "blank_pages": [], "tokens": {}}
    try:
        r = PdfReader(str(path))
        texts = []
        for i, page in enumerate(r.pages, 1):
            t = page.extract_text() or ""
            if len(t.strip()) < 20:
                out["blank_pages"].append(i)
            texts.append(t)
        full = "\n".join(texts)
        out.update(valid=True, pages=len(r.pages), words=len(re.findall(r"\b\w+\b", full)), tokens=dict(Counter(PROTECTED.findall(full))))
    except Exception as e:
        out["error"] = repr(e)
    return out


def local_links() -> list[dict]:
    findings = []
    rx = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        if "\ufffd" in text:
            findings.append({"severity":"HIGH","file":str(md.relative_to(ROOT)),"finding":"Unicode replacement character"})
        for raw in rx.findall(text):
            target = raw.split("#", 1)[0].strip().strip("<>")
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            dest = (md.parent / unquote(target)).resolve()
            if ROOT.resolve() not in dest.parents and dest != ROOT.resolve():
                findings.append({"severity":"HIGH","file":str(md.relative_to(ROOT)),"finding":f"link escapes repository: {raw}"})
            elif not dest.exists():
                findings.append({"severity":"BLOCKER","file":str(md.relative_to(ROOT)),"finding":f"broken local link: {raw}"})
    return findings


def family_dirs() -> list[Path]:
    found = []
    for en in MANUALS.rglob("en"):
        if en.is_dir() and all((en.parent / lang).is_dir() for lang in LANGS):
            found.append(en.parent)
    return sorted(set(found))


def one_file(folder: Path, suffix: str) -> Path | None:
    files = sorted(folder.glob(f"*{suffix}"))
    return files[0] if len(files) == 1 else None


def main() -> int:
    inventory, findings, families = [], local_links(), []
    for family in family_dirs():
        rec = {"family": str(family.relative_to(ROOT)), "languages": {}, "status": "PASS"}
        for lang in LANGS:
            folder = family / lang
            langrec = {}
            for ext in (".docx", ".pdf"):
                p = one_file(folder, ext)
                if not p:
                    findings.append({"severity":"BLOCKER","file":str(folder.relative_to(ROOT)),"finding":f"expected exactly one {ext} file"})
                    continue
                info = docx_info(p) if ext == ".docx" else pdf_info(p)
                info.update(path=str(p.relative_to(ROOT)), sha256=sha256(p), bytes=p.stat().st_size)
                langrec[ext[1:]] = info
                inventory.append({"family":rec["family"],"language":lang,"format":ext[1:],**info})
                if not info.get("valid"):
                    findings.append({"severity":"BLOCKER","file":str(p.relative_to(ROOT)),"finding":info.get("error","package invalid")})
            rec["languages"][lang] = langrec
        en = rec["languages"].get("en", {}).get("docx", {})
        en_heads = [h["style"] for h in en.get("headings", [])]
        for lang in ("es-419", "pt-BR"):
            loc = rec["languages"].get(lang, {}).get("docx", {})
            loc_heads = [h["style"] for h in loc.get("headings", [])]
            if en_heads != loc_heads:
                findings.append({"severity":"HIGH","file":rec["family"],"finding":f"{lang} heading-style sequence differs from English","english_count":len(en_heads),"localized_count":len(loc_heads)})
            ew, lw = en.get("words",0), loc.get("words",0)
            ratio = (lw / ew) if ew else 0
            if not 0.70 <= ratio <= 1.45:
                findings.append({"severity":"HIGH","file":rec["family"],"finding":f"{lang} DOCX word-count ratio outside 0.70-1.45","ratio":round(ratio,3)})
            et, lt = Counter(en.get("tokens",{})), Counter(loc.get("tokens",{}))
            missing = sorted((et-lt).elements())[:100]
            if missing:
                findings.append({"severity":"HIGH","file":rec["family"],"finding":f"{lang} missing protected tokens found in English","examples":missing[:25],"count":len(missing)})
        families.append(rec)
    sev = Counter(f["severity"] for f in findings)
    overall = "FAIL" if sev["BLOCKER"] or sev["HIGH"] else "BLOCKED PENDING HUMAN REVIEW"
    summary = {"status":overall,"family_count":len(families),"edition_count":len(inventory),"findings_by_severity":dict(sev),"human_review_required":True,
               "limitation":"Automated structural/package/token checks cannot certify sentence-level semantic equivalence or native-language editorial approval."}
    (QA/"FULL_MULTILINGUAL_CONTENT_PARITY_INVENTORY.json").write_text(json.dumps(inventory,indent=2,ensure_ascii=False),encoding="utf-8")
    (QA/"FULL_MULTILINGUAL_CONTENT_PARITY_FINDINGS.json").write_text(json.dumps(findings,indent=2,ensure_ascii=False),encoding="utf-8")
    lines=["# Full Multilingual Content Parity Audit","",f"**Status:** {overall}","",f"Manual families: {len(families)}  ",f"Publication files audited: {len(inventory)}  ",f"Findings: {dict(sev)}","","## Scope and conclusion","","The audit validates repository links, DOCX ZIP/XML readability, PDF text extraction, package inventories, heading-style parity, word-count ratios, and protected-token retention across English, Latin American Spanish, and Brazilian Portuguese editions.","","It does **not** claim native-language or sentence-level semantic approval. Every family remains blocked pending documented human editorial review unless separate exact-SHA evidence exists.","","## Findings"]
    if findings:
        for f in findings:
            lines.append(f"- **{f['severity']}** — `{f['file']}` — {f['finding']}")
    else:
        lines.append("- No automated blocker or high-severity defects detected.")
    lines += ["","## Release rule","","Do not mark an edition fully approved until automated defects are resolved and English technical, Spanish native-language, Portuguese native-language, accessibility, and page-by-page visual reviews are documented at the exact candidate SHA."]
    (QA/"FULL_MULTILINGUAL_CONTENT_PARITY_AUDIT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    sums=[]
    for row in inventory:
        sums.append(f"{row['sha256']}  {row['path']}")
    (QA/"FULL_MULTILINGUAL_SHA256SUMS.txt").write_text("\n".join(sorted(sums))+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    return 1 if overall == "FAIL" else 0

if __name__ == "__main__":
    sys.exit(main())
