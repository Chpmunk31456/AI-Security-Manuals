# Google Cloud pt-BR Reconstruction QA

**Status: PASS WITH DOCUMENTED LIMITATIONS**

## Scope and authority

The English `Securing_Enterprise_AI_on_Google_Cloud_en_v1.0.docx` is authoritative. The former pt-BR edition was a condensed 806-word package with 110 paragraphs, 18 headings, and 2 tables. It was replaced with a complete Brazilian Portuguese reconstruction.

Google Translate and Google Drive were used only to create a machine-assisted first pass from the public English DOCX. That output was not treated as authoritative or publication-ready. The final package was repaired and rebuilt locally against the English source.

## Reproducible structure inventory

| Metric | English | pt-BR | Result |
|---|---:|---:|---|
| Body paragraphs | 1,356 | 1,356 | PASS |
| Paragraphs including table cells | 1,634 | 1,634 | PASS |
| Words including table cells | 14,681 | 18,747 | PASS WITH DOCUMENTED LIMITATIONS (ratio 1.277) |
| Headings | 207 | 207 | PASS |
| Heading 1 / Heading 2 | 37 / 170 | 37 / 170 | PASS |
| List paragraphs | 715 | 715 | PASS |
| Tables | 62 | 62 | PASS; shapes and order match |
| Inline figures | 8 | 8 | PASS |
| Embedded media files | 7 | 7 | PASS |
| Hyperlinks | 53 | 53 | PASS |
| Bookmarks | 29 | 29 | PASS |
| Sections | 1 | 1 | PASS |

## Corrections and protected tokens

The review restored authoritative styles, numbering, bookmarks, tables, figures, hyperlinks, headers, footers, and metadata. It corrected mistranslations involving `Vertex AI`, `Security Command Center`, `Sensitive Data Protection`, `Cloud Audit Logs`, `RAG`, `shadow AI`, `landing zone`, `Organization Policy Service`, `NHI`, `Embeddings`, `Prompt`, control crosswalk terminology, assume-compromise language, and protected Google product names. URLs, identifiers, standards, commands, code, file paths, numbers, dates, versions, and product names were retained or contextually reconciled against English.

The broad automated token heuristic remains unsuppressed and may flag translated prose surrounding protected identifiers. Contextual alignment confirmed the listed identifiers themselves remain unchanged. The project glossary records the controlled dispositions.

## DOCX and PDF validation

- DOCX begins with `PK`, opens as Office Open XML, contains 22 ZIP members, and `ZipFile.testzip()` returns no corrupt member.
- PDF begins with `%PDF-1.7`, contains 93 pages, and exposes searchable/selectable text on every page (138,130 extracted non-whitespace characters; minimum 131 on any page).
- PDF metadata identifies the Portuguese title and LibreOffice producer.
- All 93 pages were rasterized at 110 DPI and inspected. No blank page, clipping, overlap, missing glyph, broken table, unreadable command, or distorted figure was observed.
- SHA-256 values are recorded in the scoped and repository-wide checksum files.

## Limitations requiring human review

- Seven embedded English-source media files retain English labels. They were preserved rather than edited without an authoritative localized source.
- Native Brazilian Portuguese linguistic approval is pending; no reviewer identity, date, scope, or exact-SHA approval exists.
- Independent Google Cloud security, legal/regulatory, accessibility, and professional prepress approval remain pending.
- Machine-assisted translation must not be represented as human-reviewed publication approval.
- Repository-wide multilingual parity remains `FAIL` because other manuals remain incomplete or pending review.

No unsupported normative, certification, legal, or cloud-provider claim was intentionally added. Stop and obtain qualified human review before treating this package as fully approved for publication.
