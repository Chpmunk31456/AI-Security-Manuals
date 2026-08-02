# Full Multilingual Content Parity Audit

**Status: FAIL**

- Baseline: `main` at `be497599c055d3f611298d999c501a8d84e768d5`
- Audit date: 2026-08-01
- Scope: all eight manual families, 24 language editions, 48 DOCX/PDF packages
- Authority rule: English is the baseline; no repository evidence displaced it.

## Decision

No manual family satisfies the publication gate. Seven Brazilian Portuguese packages are condensed five-page summaries rather than translations of their English baselines. Kali has near-structural parity, but automated comparison is not a substitute for a qualified Brazilian Portuguese and Latin American Spanish semantic review. Protected-token mismatches and source-link defects remain. No package was silently rebuilt.

| Family | EN PDF pages | es-419 PDF pages | pt-BR PDF pages | Result |
|---|---:|---:|---:|---|
| AI Risk Management | 45 | 48 | 5 | FAIL |
| ISO/IEC 42001 | 52 | 54 | 5 | FAIL |
| Kali Linux / AI Security / Forensics | 70 | 65 | 69 | BLOCKED PENDING HUMAN REVIEW |
| Microsoft Azure | 97 | 94 | 5 | FAIL |
| AWS | 88 | 94 | 5 | FAIL |
| Google Cloud | 93 | 94 | 5 | FAIL |
| Oracle Cloud | 12 | 12 | 5 | FAIL |
| IBM Cloud | 12 | 12 | 5 | FAIL |

## Evidence and method

The machine-readable inventory records exact paths, SHA-256 hashes, sizes, DOCX and PDF word counts, headings, tables, images, links, page counts, metadata, ZIP/XML results, and searchable-text results. Structural checks compared heading and table counts and protected-token sets. All 1,046 PDF pages were rasterized successfully and inspected in contact sheets for gross blank-page, truncation, and rendering anomalies. That inspection does not certify fine typography, language quality, legal accuracy, or accessibility.

## Publication blockers

1. Seven pt-BR editions contain about 800 DOCX words and 18 headings, compared with English baselines of 3,180–15,230 words and 25–207 headings.
2. Those editions omit most sections, tables, examples, warnings, appendices, references, protected tokens, and safety context.
3. Exact protected-token parity fails in both translated language sets and requires contextual adjudication; the JSON lists observed differences.
4. Source-link defects include malformed AWS/Google URLs and misleading ISO numeric URLs. A path such as `iso.org/standard/42001` identifies an unrelated withdrawn standard, not ISO/IEC 42001.
5. No native-language approval record identifies reviewer, date, scope, and exact commit SHA.

## Corrections made

- Added reproducible inventory, findings, checksums, and audit reports.
- Added prominent README warnings so condensed pt-BR packages are not represented as full parity editions.
- Documented authoritative-source and human-review blockers.

The packaged manuals were not rewritten because completing seven translations and adjudicating semantic parity requires qualified review. Rebuilding unchanged packages would create false confidence.
