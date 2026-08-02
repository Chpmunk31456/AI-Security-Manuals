# Microsoft Azure pt-BR Reconstruction QA

**Status: PASS WITH DOCUMENTED LIMITATIONS**

- Starting branch SHA: `6917d042c18f2139285c566d552407a0029d4609`
- Scope: Microsoft Azure Brazilian Portuguese DOCX/PDF only
- English authority: `manuals/cloud-ai-security/microsoft-azure/en/Securing_Enterprise_AI_on_Microsoft_Azure_en_v1.0.docx`
- Machine-assisted first pass: Google Translate; not treated as authoritative or publication-ready

## Gap inventory and closure

| Area | Reconstructed pt-BR | English authority | Result |
|---|---:|---:|---|
| Body paragraphs | 1,563 | 1,563 | Exact parity |
| Paragraphs including table cells | 1,777 | 1,777 | Exact parity |
| Headings | 207 (37 Heading 1; 170 Heading 2) | 207 (same levels/order) | Exact parity |
| Tables | 61 | 61 | Exact count and row/column shapes |
| Inline figures | 8 | 8 | Preserved |
| Embedded media files | 7 | 7 | Preserved |
| External hyperlink targets | 22 | 22 | Exact target parity |
| List paragraphs | 848 | 848 | Exact parity |
| DOCX words including tables | 19,647 | 15,437 | Ratio 1.273; consistent with a complete Portuguese translation |
| PDF pages | 100 | 97 | Portuguese reflow adds three pages |

The aligned review covered headings and section order, paragraphs, lists, tables, figures, warnings, disclaimers, authorization and safety language, examples, checklists, references, hyperlinks, commands, code, URLs, paths, numbers, dates, versions, acronyms, standards, and Microsoft product names. The reconstruction does not add unsupported requirements or claims.

## Substantive corrections after the machine pass

- Removed invented expansions of `RAG`, `NHI`, and `LLM` and restored their intended technical meanings.
- Corrected mistranslations of prompt injection and related safety terminology.
- Restored protected product names including Microsoft Purview, Microsoft Defender for Cloud, Azure Policy, Azure API Management, Azure Key Vault, Zero Trust, OpenAI API, and Anthropic.
- Corrected glossary entries for `Chunk`, `Control`, `Embedding`, `Fine-tuning`, `Groundedness`, `Guardrail`, `Prompt`, `RAG`, `Red teaming`, `Security trimming`, `Service principal`, `Shadow AI`, `Tool calling`, and `Zero Trust`.
- Restored numeric formatting where the machine pass altered percentages.
- Rebuilt the static table of contents from the translated heading hierarchy and verified its page destinations against the final PDF outline.
- Restored `word/numbering.xml` byte-for-byte from the English authority after the machine pass changed list definitions and caused overlapping list markers in LibreOffice.

## Protected-token disposition

Scoped checks found exact parity for URLs, numbers, table geometry, heading hierarchy, list assignments, and the reviewed Microsoft/product identifiers. The repository-wide heuristic still reports 183 protected-token differences because it captures English prose following protected names (for example, strings beginning `Azure Policy ...`) and requires that prose to remain untranslated. Those are translated sentences, not missing identifiers; the finding remains visible and is not suppressed.

The repository-wide safety heuristic reports missing substring `defens`. The complete pt-BR manual retains the English authority's lawful, explicitly authorized testing boundaries, including written authorization, agreed scope, permitted environments, stop conditions, least privilege, audit evidence, and prohibition on testing production or third-party systems without authorization. The broad substring finding is documented rather than silently waived.

## DOCX package validation

- File signature: `PK` / Office Open XML package
- ZIP and XML integrity: PASS
- Paragraph, style, heading, table, table-shape, figure, list, section, header, footer, relationship, and hyperlink checks: PASS
- Metadata: Portuguese title, subject, and keywords; author retained
- Local Git blob: `fac8f83ce5894f41dcdb8b91cc707e2a8abd1044`

## PDF validation and visual inspection

- File signature: `%PDF-1.7`
- `pdfinfo`: PASS; 100 US Letter pages, unencrypted, tagged, no JavaScript, no forms, no suspect objects
- Searchable/selectable text: PASS with 165,542 extracted characters and 20,841 extracted words using `pypdf`
- Text-blank pages: 0
- Rasterization: 100/100 pages rendered successfully at 150 DPI
- Page inspection: all 100 final PDF pages were inspected in order. No translation-introduced clipping, overlap, broken table, blank page, or missing glyph was observed after restoring the authoritative list numbering.
- Local Git blob: `a63487a8a8066c5bd2400eec8ae6ce2111fe4d08`

## Audit results and fail-closed status

- Final repository integrity audit must pass on the exact committed head locally and in GitHub Actions.
- Full multilingual content parity remains repository-wide `FAIL` because AWS, Google Cloud, Oracle Cloud, and IBM Cloud pt-BR editions remain condensed and all Spanish editions remain under review.
- No Azure pt-BR package-readability, heading-loss, table-loss, or word-count structural-loss finding remains.

## Unresolved limitations

- No identified native Brazilian Portuguese reviewer has approved wording, terminology, or fluency at an exact commit SHA.
- Labels embedded inside the seven English-source media files remain English.
- Two reused English-source architecture figures contain clipped text within the source artwork; the same clipping is reproducible in the authoritative English PDF. It was preserved rather than redrawn or silently altered and requires a future source-figure production correction.
- Automated and page-image review do not replace qualified accessibility, cloud-security, legal, or native-language review.
- Cloud services and guidance change over time; current operational decisions must be checked against official Microsoft and cited primary sources.
