# Full Multilingual Content Parity Audit

**Status:** FAIL

Manual families: 8  
Publication files audited: 48  
Findings: {'HIGH': 19}

## Scope and conclusion

The audit validates repository links, DOCX ZIP/XML readability, PDF text extraction, package inventories, heading-style parity, word-count ratios, and protected-token retention across English, Latin American Spanish, and Brazilian Portuguese editions.

It does **not** claim native-language or sentence-level semantic approval. Every family remains blocked pending documented human editorial review unless separate exact-SHA evidence exists.

## Findings
- **HIGH** — `manuals\ai-risk-management` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\ai-risk-management` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\aws` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\aws` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\google-cloud` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\google-cloud` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\ibm-cloud` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\ibm-cloud` — pt-BR heading-style sequence differs from English
- **HIGH** — `manuals\cloud-ai-security\ibm-cloud` — pt-BR DOCX word-count ratio outside 0.70-1.45
- **HIGH** — `manuals\cloud-ai-security\ibm-cloud` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\microsoft-azure` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\microsoft-azure` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\oracle-cloud` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\cloud-ai-security\oracle-cloud` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\iso-iec-42001` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\iso-iec-42001` — pt-BR missing protected tokens found in English
- **HIGH** — `manuals\kali-linux-ai-security-forensics` — es-419 missing protected tokens found in English
- **HIGH** — `manuals\kali-linux-ai-security-forensics` — pt-BR heading-style sequence differs from English
- **HIGH** — `manuals\kali-linux-ai-security-forensics` — pt-BR missing protected tokens found in English

## Release rule

Do not mark an edition fully approved until automated defects are resolved and English technical, Spanish native-language, Portuguese native-language, accessibility, and page-by-page visual reviews are documented at the exact candidate SHA.
