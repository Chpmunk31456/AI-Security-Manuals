# English Baseline Audit

**Status: FAIL**

All eight English DOCX and PDF packages open, their DOCX archives pass ZIP/XML integrity checks, and every PDF exposes searchable text. All English PDF pages rasterized without a zero-byte render. These mechanical checks do not establish technical correctness.

English remains authoritative for translation comparison. It does not pass the requested source-verification gate because claim-level verification is incomplete and source defects remain:

- malformed links splice unrelated product names into AWS and Google documentation URLs;
- `https://www.iso.org/standard/42001` resolves to an unrelated withdrawn standard number rather than ISO/IEC 42001;
- time-sensitive framework counts and cloud product behavior require owner-by-owner verification at the candidate commit.

Validated primary-source anchors include NIST AI RMF 1.0 and its Govern/Map/Measure/Manage Playbook, NIST AI 600-1, the OWASP GenAI/LLM project, MITRE ATLAS, and official cloud-provider documentation. These anchors do not constitute verification of every sentence.

No blocker was guessed away. English baseline status remains `FAIL` until source-link corrections and claim-level review are completed.
