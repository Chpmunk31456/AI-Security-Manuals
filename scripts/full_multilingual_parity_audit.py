#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json, re, sys, zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
MANUALS = ROOT / "manuals"
QA = ROOT / "qa"
BASELINE = "be497599c055d3f611298d999c501a8d84e768d5"
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
}
LANGS = ("en", "es-419", "pt-BR")
ALLOWED = {"PASS", "PASS WITH DOCUMENTED LIMITATIONS", "FAIL", "BLOCKED PENDING HUMAN REVIEW"}

def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""): h.update(chunk)
    return h.hexdigest()

def words(text): return re.findall(r"\b[\wÀ-ÿ]+(?:[-'][\wÀ-ÿ]+)*\b", text, re.UNICODE)
def text_of(el): return "".join(t.text or "" for t in el.findall(".//w:t", NS)).strip()
def norm(s): return re.sub(r"\s+", " ", s).strip()

def docx_info(path: Path):
    out={"zip_integrity":"PASS","xml_integrity":"PASS","paragraphs":[],"headings":[],"tables":0,"table_rows":0,"images":0,"links":[],"metadata":{}}
    try:
        with zipfile.ZipFile(path) as z:
            bad=z.testzip()
            if bad: out["zip_integrity"]="FAIL: "+bad
            names=z.namelist(); out["images"]=sum(n.startswith("word/media/") and not n.endswith("/") for n in names)
            root=ET.fromstring(z.read("word/document.xml"))
            for p in root.findall(".//w:p", NS):
                t=norm(text_of(p))
                if not t: continue
                out["paragraphs"].append(t)
                ps=p.find("./w:pPr/w:pStyle",NS)
                style=ps.get("{%s}val"%NS["w"]) if ps is not None else ""
                if style.lower().startswith("heading") or re.match(r"^(t[ií]tulo|titre)",style.lower()): out["headings"].append({"style":style,"text":t})
            tabs=root.findall(".//w:tbl",NS); out["tables"]=len(tabs); out["table_rows"]=sum(len(t.findall("./w:tr",NS)) for t in tabs)
            rels={}
            if "word/_rels/document.xml.rels" in names:
                rr=ET.fromstring(z.read("word/_rels/document.xml.rels"))
                rels={e.get("Id"):e.get("Target") for e in rr}
            for h in root.findall(".//w:hyperlink",NS):
                rid=h.get("{%s}id"%NS["r"]); target=rels.get(rid)
                if target: out["links"].append(target)
            if "docProps/core.xml" in names:
                cr=ET.fromstring(z.read("docProps/core.xml"))
                for tag in ("title","creator","language","description"):
                    e=cr.find("dc:"+tag,NS)
                    if e is not None and e.text: out["metadata"][tag]=e.text
    except Exception as e:
        out["zip_integrity"]="FAIL"; out["xml_integrity"]="FAIL: "+str(e)
    txt="\n".join(out["paragraphs"]); out["word_count"]=len(words(txt)); out["character_count"]=len(txt)
    return out

def pdf_info(path: Path):
    out={"readable":"PASS","searchable_text":"PASS","blank_pages":[],"page_word_counts":[],"metadata":{},"links":[]}
    try:
        r=PdfReader(str(path)); out["pages"]=len(r.pages)
        if r.metadata: out["metadata"]={str(k):str(v) for k,v in r.metadata.items() if v is not None}
        chunks=[]
        for i,p in enumerate(r.pages,1):
            t=p.extract_text() or ""; chunks.append(t); wc=len(words(t)); out["page_word_counts"].append(wc)
            if wc<5: out["blank_pages"].append(i)
            for a in p.get("/Annots",[]) or []:
                try:
                    obj=a.get_object(); act=obj.get("/A"); uri=act.get("/URI") if act else None
                    if uri: out["links"].append(str(uri))
                except Exception: pass
        text="\n".join(chunks); out["word_count"]=len(words(text)); out["character_count"]=len(text)
        if out["word_count"]<100: out["searchable_text"]="FAIL"
    except Exception as e:
        out.update({"readable":"FAIL: "+str(e),"searchable_text":"FAIL","pages":0,"word_count":0,"character_count":0})
    return out

def protected(text):
    pats=[r"https?://[^\s)\]>]+",r"\b(?:NIST|ISO(?:/IEC)?|OWASP|MITRE|ATT&CK|AWS|Azure|Google Cloud|Oracle Cloud|IBM Cloud|Kali Linux)\b[^\n,;:.]{0,40}",r"\b[A-Z]{2,}(?:[-_/][A-Z0-9.]+)+\b",r"\b\d+(?:\.\d+){1,3}\b",r"\b(?:TCP|UDP)\s*\d{1,5}\b"]
    return sorted(set(x.strip() for p in pats for x in re.findall(p,text,re.I)))

def family_dirs():
    out=[]
    for en in MANUALS.rglob("en"):
        if en.is_dir() and all((en.parent/l).is_dir() for l in LANGS): out.append(en.parent)
    return sorted(out)

def markdown_links():
    findings=[]; inventory=[]
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts: continue
        text=p.read_text(encoding="utf-8",errors="replace")
        for label,target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)",text):
            if re.match(r"^(?:https?://|mailto:|#)",target):
                inventory.append({"source":str(p.relative_to(ROOT)).replace("\\","/"),"target":target,"kind":"external","exists":None}); continue
            clean=unquote(target.split("#",1)[0]); dest=(p.parent/clean).resolve(); ok=dest.exists()
            rec={"source":str(p.relative_to(ROOT)).replace("\\","/"),"target":target,"kind":"local","exists":ok}; inventory.append(rec)
            if not ok: findings.append({"severity":"HIGH","category":"broken_local_link","path":rec["source"],"detail":target})
    return inventory,findings

def main():
    QA.mkdir(exist_ok=True)
    inv={"baseline_sha":BASELINE,"families":[],"files":[],"readme_links":[]}; findings=[]
    for fam in family_dirs():
        frec={"family":str(fam.relative_to(MANUALS)).replace("\\","/"),"editions":{}}
        infos={}
        for lang in LANGS:
            d=fam/lang; docs=list(d.glob("*.docx")); pdfs=list(d.glob("*.pdf"))
            if len(docs)!=1 or len(pdfs)!=1:
                findings.append({"severity":"BLOCKER","category":"package_cardinality","family":frec["family"],"language":lang,"detail":f"DOCX={len(docs)} PDF={len(pdfs)}"}); continue
            di=docx_info(docs[0]); pi=pdf_info(pdfs[0]); infos[lang]=(di,pi)
            ed={"docx":str(docs[0].relative_to(ROOT)).replace("\\","/"),"pdf":str(pdfs[0].relative_to(ROOT)).replace("\\","/"),"docx_sha256":sha(docs[0]),"pdf_sha256":sha(pdfs[0]),"docx_metrics":{k:v for k,v in di.items() if k!="paragraphs"},"pdf_metrics":pi}
            frec["editions"][lang]=ed; inv["files"] += [{"path":ed["docx"],"sha256":ed["docx_sha256"],"bytes":docs[0].stat().st_size},{"path":ed["pdf"],"sha256":ed["pdf_sha256"],"bytes":pdfs[0].stat().st_size}]
            if di["zip_integrity"]!="PASS" or di["xml_integrity"]!="PASS": findings.append({"severity":"BLOCKER","category":"docx_integrity","family":frec["family"],"language":lang,"detail":di["zip_integrity"]+" / "+di["xml_integrity"]})
            if pi["readable"]!="PASS" or pi["searchable_text"]!="PASS" or pi["blank_pages"]: findings.append({"severity":"BLOCKER","category":"pdf_validation","family":frec["family"],"language":lang,"detail":pi})
            ratio=pi.get("word_count",0)/max(di["word_count"],1)
            if not .75<=ratio<=1.25: findings.append({"severity":"HIGH","category":"docx_pdf_text_mismatch","family":frec["family"],"language":lang,"detail":{"docx_words":di["word_count"],"pdf_words":pi.get("word_count"),"ratio":round(ratio,3)}})
        if "en" in infos:
            en,_=infos["en"]; en_text="\n".join(en["paragraphs"]); en_tokens=protected(en_text)
            for lang in ("es-419","pt-BR"):
                if lang not in infos: continue
                di,pi=infos[lang]; ratio=di["word_count"]/max(en["word_count"],1); hratio=len(di["headings"])/max(len(en["headings"]),1)
                if not .70<=ratio<=1.35: findings.append({"severity":"HIGH","category":"translation_word_ratio","family":frec["family"],"language":lang,"detail":round(ratio,3)})
                if len(di["headings"])!=len(en["headings"]): findings.append({"severity":"HIGH","category":"heading_count_parity","family":frec["family"],"language":lang,"detail":{"en":len(en["headings"]),"localized":len(di["headings"]),"ratio":round(hratio,3)}})
                if di["tables"]!=en["tables"] or di["table_rows"]!=en["table_rows"]: findings.append({"severity":"HIGH","category":"table_parity","family":frec["family"],"language":lang,"detail":{"en_tables":en["tables"],"localized_tables":di["tables"],"en_rows":en["table_rows"],"localized_rows":di["table_rows"]}})
                loc_text="\n".join(di["paragraphs"]); loc_tokens=protected(loc_text)
                missing=sorted(set(en_tokens)-set(loc_tokens))
                if missing: findings.append({"severity":"HIGH","category":"protected_token_parity","family":frec["family"],"language":lang,"detail":{"missing_count":len(missing),"sample":missing[:30]}})
                safety={"es-419":["autoriz","legal","defens"],"pt-BR":["autoriz","legal","defens"]}[lang]
                absent=[x for x in safety if x not in loc_text.lower()]
                if absent: findings.append({"severity":"BLOCKER","category":"safety_language","family":frec["family"],"language":lang,"detail":{"missing_concepts":absent}})
        inv["families"].append(frec)
    links,lf=markdown_links(); inv["readme_links"]=links; findings+=lf
    inv["summary"]={"family_count":len(inv["families"]),"edition_count":sum(len(f["editions"]) for f in inv["families"]),"package_file_count":len(inv["files"]),"finding_count":len(findings)}
    status="FAIL" if any(f["severity"] in ("BLOCKER","HIGH") for f in findings) else "BLOCKED PENDING HUMAN REVIEW"
    result={"baseline_sha":BASELINE,"status":status,"findings":findings,"limitations":["Paragraph-level semantic equivalence requires qualified native-language human review.","Official-source currency requires documented claim-by-claim human adjudication where product documentation is time-sensitive.","Automated structural and token checks do not establish translation approval."]}
    (QA/"FULL_MULTILINGUAL_CONTENT_PARITY_INVENTORY.json").write_text(json.dumps(inv,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (QA/"FULL_MULTILINGUAL_CONTENT_PARITY_FINDINGS.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    sums=[f"{x['sha256']}  {x['path']}" for x in inv["files"]]
    (QA/"FULL_MULTILINGUAL_SHA256SUMS.txt").write_text("\n".join(sums)+"\n",encoding="utf-8")
    print(json.dumps({"status":status,**inv["summary"],"severity":Counter(f["severity"] for f in findings)},default=dict))
if __name__=="__main__": main()
