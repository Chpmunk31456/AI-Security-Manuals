# AWS pt-BR Reconstruction QA

**Status: PASS WITH DOCUMENTED LIMITATIONS**

- Starting branch SHA: `15f424bd6b295a4e5e8a17b31566cbae76f1cb0f`
- Package candidate SHA: to be recorded after the first publication commit
- Scope: AWS Brazilian Portuguese DOCX/PDF only
- English authority: `manuals/cloud-ai-security/aws/en/Securing_Enterprise_AI_on_AWS_en_v1.0.docx`
- Previous condensed package: the same pt-BR DOCX/PDF paths, previously 76 body paragraphs and a five-page PDF
- Reconstructed package: `manuals/cloud-ai-security/aws/pt-BR/Protecao_de_IA_Empresarial_na_AWS_pt-BR_v1.0.docx` and `.pdf`
- Translation method: Google Translate and Google Drive were used only for a machine-assisted first pass; English remained authoritative

## Gap inventory and closure

| Area | English authority | Reconstructed pt-BR | Result |
|---|---:|---:|---|
| Body paragraphs | 1,356 | 1,356 | Exact parity |
| Paragraphs including table cells | 1,634 | 1,634 | Exact parity |
| Headings | 207 (37 Heading 1; 170 Heading 2) | 207 (same levels/order) | Exact parity |
| List paragraphs | 715 | 715 | Exact parity |
| Tables | 62 | 62 | Exact count and row/column shapes |
| Inline figures | 8 | 8 | Preserved |
| Embedded media files | 7 | 7 | Preserved |
| External hyperlink targets | 22 | 22 | Exact parity |
| All hyperlinks | 51 | 51 | Exact parity |
| Bookmarks | 29 | 29 | Exact parity |
| Sections / explicit page breaks | 1 / 7 | 1 / 7 | Exact parity |
| DOCX words including tables | 14,678 | 18,737 | Ratio 1.277; consistent with a complete Portuguese translation |
| PDF pages | 88 | 86 | Portuguese reflow; all pages nonblank |

The aligned review covered headings and order, paragraphs, lists and nesting, all table shapes, figures, captions, warnings, disclaimers, lawful-authorization boundaries, examples, exercises, checklists, references, hyperlinks, commands, code, URLs, paths, identifiers, numbers, dates, versions, acronyms, standards, product names, and service names. No unsupported AWS behavior, normative requirement, certification statement, or legal claim was added.

## Corrections and protected-token dispositions

- `Identity Center do IAM` was a mistranslation and was corrected to the protected service name `IAM Identity Center`.
- `Guarda-corpos de rocha matriz da Amazônia` was a mistranslation and was corrected to `Amazon Bedrock Guardrails`.
- English custom paragraph styles, numbering definitions, and 29 internal bookmarks were restored from the authoritative DOCX after Google conversion normalized or removed them.
- Reviewed AWS service/product names and all URLs have exact target parity after correction.
- The only remaining minimum-list count difference is English `Detective` used as the ordinary adjective in “Detective controls.” Portuguese correctly renders this as `controles detectivos`; it is an acceptable contextual translation and not an occurrence of the Amazon Detective product.
- Generic terms such as account ID, region, Availability Zone, role, policy, permission boundary, resource policy, trust policy, and presigned URL were translated contextually. Differences were reviewed as acceptable technical localization, not omissions.
- Code, commands, CLI syntax and flags, URLs, identifiers, standards numbers, versions, and numeric values were preserved where translation would change operation or meaning.
- The repository-wide heuristic still emits 182 pt-BR protected-token differences because it treats complete English prose fragments beginning with protected names (for example, `AWS Config results ...`) as tokens that must remain wholly untranslated. Aligned paragraph review confirms that the protected identifiers remain and the surrounding prose is translated; these are documented tokenization artifacts, not true omissions.
- The repository-wide safety heuristic reports missing English stem `defens`. The pt-BR manual uses Portuguese `defesa` while retaining the complete authorization and defensive-use boundaries. This is an acceptable localization artifact and remains visible rather than suppressed.

## Safety and authorization review

The pt-BR edition retains the English authority's written-authorization requirement, approved scope, permitted-environment limits, synthetic/low-risk data preference, third-party and production restrictions, least privilege, cost controls, stop conditions, rollback, cleanup, evidence protection, credential protection, incident response, and legal/regulatory limitations. No warning or obligation was intentionally weakened.

## DOCX validation

- Signature: `50 4B 03 04` / Microsoft Word 2007+ Office Open XML package
- ZIP members: 22; ZIP test: PASS; XML and relationship parsing: PASS
- Paragraphs, styles, heading hierarchy/order, lists, numbering, table count/shapes, figures, media, hyperlinks, bookmarks, sections, headers, footers, and metadata: PASS
- LibreOffice opening/conversion: PASS without repair prompt
- Local Git blob: `2534a002cf468e9e0ad13cd150ea9707cada754b`
- SHA-256: `31a9dbf879cdf9d14cb75490e337a2e965f638638e536feb8ce5e8e7d47b6e79`

## PDF validation and visual inspection

- Signature: `%PDF-1.7`
- `pdfinfo`: PASS; 86 US Letter pages, unencrypted, tagged, no JavaScript, no forms, no suspect objects
- `pdftotext` and `pypdf`: PASS; searchable/selectable text with 138,095 extracted characters and 19,918 extracted words
- Text-blank pages: 0
- Rasterization: 86/86 pages rendered successfully
- Visual inspection: all 86 pages were inspected in order. No translation-introduced clipping, overlap, broken table, blank page, distorted figure, unreadable command, or missing glyph was observed.
- Local Git blob: `5e8a7cb81ffedbac36c6baa8f7a63dbfebd356ec`
- SHA-256: `66ee1f193339a1e64bd9886af4c081565990fb6da5b1e43916aeb41ea08fb083`

## Exact-byte and audit checkpoint

Committed and remote blob hashes will be recorded against the package candidate commit. The local blobs above are the exact bytes selected for publication; no connector-generated or alternate binary was used for validation.

- Final repository integrity audit: pending exact candidate checkout
- Full multilingual content parity audit: expected repository-wide `FAIL` until Google Cloud, Oracle Cloud, IBM Cloud, Kali, and Spanish review units are completed
- AWS acceptance requires no package-readability, heading-loss, table-loss, or structural-loss finding on the exact candidate

## Unresolved limitations

- No identified native Brazilian Portuguese reviewer has approved wording, terminology, or fluency at an exact commit SHA.
- Labels embedded inside the seven reused English-source media files remain English.
- Automated and page-image review do not replace qualified accessibility, AWS cloud-security, legal, or native-language review.
- Cloud services and guidance change over time; operational decisions must be checked against current AWS and cited primary sources.
- Repository-wide multilingual parity remains `FAIL`; this scoped status applies only to AWS pt-BR automated gates.

