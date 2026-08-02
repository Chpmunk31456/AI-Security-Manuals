# ISO/IEC 42001 pt-BR Reconstruction QA

**Status: PASS WITH DOCUMENTED LIMITATIONS**

- Starting branch SHA: `2b9fed1feef7f2947ee68caee80d371308bfa735`
- Scope: ISO/IEC 42001 Brazilian Portuguese DOCX/PDF only
- English authority: `manuals/iso-iec-42001/en/ISO_IEC_42001_Practical_AIMS_Manual_en_v1.0.docx`
- Reconstructed package: `manuals/iso-iec-42001/pt-BR/ISO_IEC_42001_Manual_Pratico_SGIA_pt-BR_v1.0.{docx,pdf}`
- Translation method: Google Translate produced a machine-assisted first pass; Google Drive converted the corrected DOCX to searchable PDF. Neither output was treated as authoritative or publication-ready without repository-side comparison and correction.

## Gap inventory and closure

| Area | Condensed pt-BR package | Reconstructed pt-BR package | English authority | Result |
|---|---:|---:|---:|---|
| DOCX paragraphs | 76 | 653 | 653 | Restored |
| Headings | 18 (Heading 1 only) | 126 (35 Heading 1; 91 Heading 2) | 126 (same levels/order) | Restored |
| Tables | 2 | 41 | 41 | Restored; every row/column shape matches |
| Inline figures | 0 | 10 | 10 | Restored; embedded media hashes match |
| DOCX words including tables | 803 | 11,318 | 9,092 | Ratio 1.245; consistent with a full Portuguese translation |
| External hyperlink targets | 0 | 34 | 34 | Exact target multiset matches |
| PDF pages | 8 | 53 | 52 | Restored; Portuguese reflow adds one page |

The aligned comparison covered all 653 body paragraphs, all 41 tables and their cells, all 126 headings in order, all list-bearing paragraphs, all 10 embedded figures, all external hyperlink relationships, the single header and footer, and the package metadata. Warnings, disclaimers, examples, checklists, references, clause identifiers, dates, versions, numbers, acronyms, standards, and product names were included in the same alignment review. Length-ratio outliers were inspected to detect additions and omissions.

## Substantive corrections after the machine pass

- Restored the defined `AIMS` acronym where it had become `MIRA`, `OBJETIVOS`, generic `objetivos`, or invented expansions.
- Restored `SoA` / `Declaração de Aplicabilidade` where it had become `Estado da Arte`, `Declaração de Acordo`, `Solução de Ação`, `Situação das Atividades`, or similar unsupported expansions.
- Removed the invented expansion of `RAG`.
- Restored section identifiers localized as decimal commas, including `30.2`, `30.5`, `30.6`, `30.7`, and `30.8`.
- Restored protected product names translated as ordinary prose: `OpenMetadata`, `Great Expectations`, `Evidently`, `Deepchecks`, `Inspect AI`, `Presidio`, and `Open Policy Agent`.
- Preserved ISO/IEC identifiers, dates, version numbers, URLs, the 38-control count, table geometry, figures, and external link destinations.
- No normative requirement, certification claim, control, law, or unsupported interpretation was added.

## Protected-token disposition

Exact technical identifiers and destinations pass the scoped review: ISO/IEC identifiers, section/clause numbers, dates, versions, product names, URLs, `AIMS`, `SoA`, `RAG`, and embedded-media bytes are preserved after the corrections above.

Contextually justified language differences remain and are not omissions: `AI` is normally rendered as `IA`; `ML` is expanded as `aprendizado de máquina`; `OECD` is rendered as the official Portuguese acronym `OCDE`; `EU` is rendered as `UE`; `Annex A` is `Anexo A`; `Clause` is `Cláusula`; and Plan-Do-Check-Act is rendered as `Planejar-Executar-Verificar-Agir` while retaining `PDCA`.

The repository-wide parity script still reports a high-severity ISO pt-BR protected-token finding with 305 items because its regular expression captures up to 40 characters of English prose following names such as `ISO`, then requires that English prose to appear verbatim in a translation. Examples include `AI-domain`, `Current-information`, and `Context/scope`. Those strings are translated prose, not protected identifiers. This automated finding is not suppressed and remains visible in the repository-wide report.

The same workflow reports the missing substring `defens` as a safety blocker. This ISO management-system manual contains no offensive-security procedure requiring an authorized/defensive-use boundary; its safety, legal, accountability, limitation, audit, and non-certification language remains present. The finding is retained as a documented heuristic limitation rather than silently waived.

## DOCX package validation

- File signature: `PK` / Microsoft Word 2007+ package
- ZIP test: PASS; no compressed-data errors
- XML parsing and relationship traversal: PASS
- Paragraph, heading, table, table-shape, figure, list, section, header, and footer parity: PASS
- Embedded media: 10 figures; SHA-256 multiset matches English
- External relationships: 34 targets; exact multiset matches English
- README DOCX/PDF links: resolve to the expected package paths

## PDF validation and visual inspection

- File signature: `%PDF-1.4`
- `pdfinfo`: PASS; 53 US Letter pages, unencrypted, tagged, no JavaScript, no form, no suspect objects
- Searchable/selectable text: PASS; 12,222 extracted words
- Text-blank pages: 0; minimum extracted characters on any page: greater than zero
- Rasterization: 53/53 pages rendered successfully at 100 DPI
- Page inspection: all 53 final PDF pages were inspected in ordered contact sheets. No clipping, overlap, broken table, missing glyph, or blank page was observed. Pages 36 and 53 are intentionally sparse table-continuation/limitation pages, not blank pages.
- Embedded figure labels remain in English and are explicitly documented below.

## Audit results and fail-closed status

- Final repository integrity audit acceptance target: package readability and local-link checks must pass on the exact committed head and in GitHub Actions.
- Full multilingual content parity audit: repository-wide `FAIL` remains expected because Azure, AWS, Google Cloud, Oracle Cloud, and IBM Cloud pt-BR editions are still condensed, Spanish review remains pending, and the broad protected-token/safety heuristics above remain reported.
- No structural-loss or package-readability finding remains for ISO/IEC 42001 in the scoped measurements.

## Unresolved limitations

- No identified native Brazilian Portuguese reviewer has approved the wording, terminology, or fluency at an exact commit SHA.
- Labels embedded inside the 10 English-source figures remain English; the surrounding captions and prose are translated.
- Automated and contact-sheet review do not replace full-resolution accessibility and professional production review.
- Current-source claims and ISO terminology should receive qualified technical/legal review before operational or certification use.
- This manual is implementation guidance and repository-author commentary around ISO/IEC concepts; it is not the ISO standard, does not reproduce the normative standard text, and does not establish or imply certification.
