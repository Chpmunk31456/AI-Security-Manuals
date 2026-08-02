# Oracle Cloud pt-BR Reconstruction QA

**Status: PASS WITH DOCUMENTED LIMITATIONS**

## Scope and authority

The English `Oracle_Cloud_AI_Security_Manual_en_v1.0.docx` is authoritative. The former pt-BR edition was a condensed 806-word package with 110 aggregate paragraphs, 18 headings, 2 tables, no figures, no hyperlinks, and no bookmarks. It was replaced with a complete Brazilian Portuguese reconstruction.

Google Translate and Google Drive were used only for a machine-assisted first pass and document conversion. That output was not treated as authoritative or publication-ready. The final package was repaired and rebuilt locally against the English source, including controlled reuse of 15 exact paragraphs from already validated project translation memories.

## Reproducible structure inventory

| Metric | English | pt-BR | Result |
|---|---:|---:|---|
| Body paragraphs | 238 | 238 | PASS |
| Paragraphs including table cells | 311 | 311 | PASS |
| Nonempty aggregate paragraphs | 305 | 305 | PASS |
| Words including table cells | 3,275 | 4,150 | PASS (ratio 1.267) |
| Headings | 25 | 25 | PASS |
| Heading 1 / Heading 2 | 23 / 2 | 23 / 2 | PASS |
| Numbered-list paragraphs | 10 | 10 | PASS |
| Tables | 3 | 3 | PASS; shapes 8x3, 11x2, and 9x3 match |
| Inline figures | 2 | 2 | PASS |
| Embedded media files | 2 | 2 | PASS |
| Hyperlinks | 36 | 36 | PASS |
| Bookmarks | 25 | 25 | PASS |
| Sections | 1 | 1 | PASS |

## Corrections and protected tokens

The rebuild restored authoritative styles, numbering, bookmarks, internal PAGEREF links, external hyperlinks, tables, figures, headers, footers, and metadata. It corrected reproducible mistranslations affecting `RAG`, `MCP`, prompt injection, embeddings, guardrails, vector stores, `tenancy`, `landing zone`, `instance principals`, `resource principals`, `OWASP Top 10 for LLM Applications`, and protected Oracle service names including `OCI Audit`, `OCI Vault`, `Cloud Guard`, `Security Zones`, `Vulnerability Scanning Service`, `OS Management Hub`, `Service Connector Hub`, and `Logging Analytics`.

URLs, identifiers, standards, product names, versions, dates, and field structures were retained or contextually reconciled against English. The project glossary records controlled dispositions.

## DOCX, PDF, accessibility, and visual validation

- DOCX begins with `PK`, opens as Office Open XML, contains 22 ZIP members, and has no corrupt member.
- Automated accessibility audit reports zero high-, medium-, or low-severity findings.
- PDF contains 12 searchable, nonblank pages with 37,796 extracted non-whitespace characters; the minimum on any page is 583.
- PDF metadata identifies the Portuguese title and author.
- All 12 pages were rasterized at 110 DPI and inspected. No blank page, clipping, overlap, missing glyph, broken table, unreadable link, or distorted figure was observed.
- The final metadata-only PDF rewrite produced pixel-identical page images across all 12 pages.
- SHA-256 values are recorded in the scoped and repository-wide checksum files.

## Limitations requiring human review

- Two embedded English-source figures retain English labels. They were preserved rather than edited without an authoritative localized source.
- Native Brazilian Portuguese linguistic approval is pending; no reviewer identity, date, scope, or exact-SHA approval exists.
- Independent Oracle Cloud security, legal/regulatory, human accessibility, and professional prepress approval remain pending.
- Machine-assisted translation must not be represented as human-reviewed publication approval.
- Repository-wide multilingual parity remains `FAIL` because other manuals remain incomplete or pending review.

No unsupported normative, certification, legal, or cloud-provider claim was intentionally added. Stop and obtain qualified human review before treating this package as fully approved for publication.
