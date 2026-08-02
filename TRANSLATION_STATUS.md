# Translation Parity Status

**Current status: FAIL - remediation required**

## AI Risk Management pt-BR

**Status: PASS WITH DOCUMENTED LIMITATIONS** for automated structure and package checks; native-language approval remains pending.

The condensed five-page package was replaced with a complete reconstruction from the English baseline at `5be029a5cbb156ff32e1f6032a677f96b8aaa933`. The reconstructed DOCX preserves 574 paragraphs, 99 headings, 42 tables, and 10 inline figures. Its searchable PDF contains 47 nonblank pages.

Automated protected-token review still requires contextual disposition for `AI RMF`, `API`, and section-number tokens `26.4`, `26.7`, and `26.9`. Embedded figure labels inherited from the English source have not received native-language localization approval. No native Brazilian Portuguese approval is claimed.

See [`qa/ai-risk-management/PT_BR_RECONSTRUCTION_QA.md`](qa/ai-risk-management/PT_BR_RECONSTRUCTION_QA.md).

## ISO/IEC 42001 pt-BR

**Status: PASS WITH DOCUMENTED LIMITATIONS** for automated structure and package checks; native-language approval remains pending.

The condensed eight-page package was replaced with a complete reconstruction from the English authority. The reconstructed DOCX preserves 653 paragraphs, 126 headings, 41 tables, 10 inline figures, 34 external hyperlink targets, and the original table shapes and embedded media. Its searchable PDF contains 53 nonblank pages.

Google Translate and Google Drive were used only for a machine-assisted first pass and document conversion. Reproducible mistranslations of `AIMS`, `SoA`, `RAG`, section identifiers, and product names were corrected against English. Embedded figure labels remain English, and no native Brazilian Portuguese approval is claimed.

See [`qa/iso-iec-42001/PT_BR_RECONSTRUCTION_QA.md`](qa/iso-iec-42001/PT_BR_RECONSTRUCTION_QA.md).

## Microsoft Azure pt-BR

**Status: PASS WITH DOCUMENTED LIMITATIONS** for automated structure and package checks; native-language approval remains pending.

The condensed package was replaced with a complete reconstruction from the English authority. The reconstructed DOCX preserves 1,563 body paragraphs, 207 headings, 61 tables, 8 inline figures, 7 embedded media files, 22 external hyperlink targets, and 848 list paragraphs. Its searchable PDF contains 100 nonblank pages.

Google Translate was used only for a machine-assisted first pass. Reproducible mistranslations affecting `RAG`, `NHI`, `LLM`, prompt injection, glossary entries, and protected Microsoft product names were corrected against English. English-source figure labels remain embedded, and no native Brazilian Portuguese approval is claimed.

See [`qa/microsoft-azure/PT_BR_RECONSTRUCTION_QA.md`](qa/microsoft-azure/PT_BR_RECONSTRUCTION_QA.md).

## AWS pt-BR

**Status: PASS WITH DOCUMENTED LIMITATIONS** for automated structure, package, and visual checks; native-language approval remains pending.

The condensed five-page package was replaced with a complete reconstruction from the English authority. The reconstructed DOCX preserves 1,356 body paragraphs, 1,634 paragraphs including table cells, 207 headings, 715 list paragraphs, 62 tables, 8 inline figures, 7 embedded media files, 22 external hyperlink targets, 51 total hyperlinks, and 29 bookmarks. Its searchable PDF contains 86 nonblank pages.

Google Translate and Google Drive were used only for a machine-assisted first pass. The review corrected `IAM Identity Center` and `Amazon Bedrock Guardrails`, restored authoritative styles, list numbering, and bookmarks, and retained all reviewed AWS service names and URLs. Embedded English-source figure labels remain English, and no native Brazilian Portuguese approval is claimed.

See [`qa/aws/PT_BR_RECONSTRUCTION_QA.md`](qa/aws/PT_BR_RECONSTRUCTION_QA.md).

## Google Cloud pt-BR

**Status: PASS WITH DOCUMENTED LIMITATIONS** for automated structure, package, and visual checks; native-language approval remains pending.

The condensed package was replaced with a complete reconstruction from the English authority. The reconstructed DOCX preserves 1,356 body paragraphs, 1,634 paragraphs including table cells, 207 headings, 715 list paragraphs, 62 tables, 8 inline figures, 7 embedded media files, 53 hyperlinks, 29 bookmarks, and the authoritative section order and table shapes. Its searchable PDF contains 93 nonblank pages, all rendered and inspected.

Google Translate and Google Drive were used only for a machine-assisted first pass. Contextual review corrected mistranslations affecting `Vertex AI`, `Security Command Center`, `Sensitive Data Protection`, `Cloud Audit Logs`, `RAG`, `shadow AI`, `Embeddings`, `Prompt`, protected Google product names, and governance terminology. Embedded English-source figure labels remain English, and no native Brazilian Portuguese approval is claimed.

See [`qa/google-cloud/PT_BR_RECONSTRUCTION_QA.md`](qa/google-cloud/PT_BR_RECONSTRUCTION_QA.md).

## Oracle Cloud Infrastructure pt-BR

**Status: PASS WITH DOCUMENTED LIMITATIONS** for automated structure, package, accessibility, and visual checks; native-language approval remains pending.

The condensed 806-word package was replaced with a complete reconstruction from the English authority. The reconstructed DOCX preserves 238 body paragraphs, 311 paragraphs including table cells, 25 headings, 10 numbered-list paragraphs, 3 tables, 2 inline figures, 2 embedded media files, 36 hyperlinks, 25 bookmarks, and the authoritative section order and table shapes. Its searchable PDF contains 12 nonblank pages, all rendered and inspected.

Google Translate and Google Drive were used only for a machine-assisted first pass and document conversion. Contextual review corrected mistranslations affecting `RAG`, `MCP`, prompt injection, embeddings, guardrails, vector stores, OCI identity terminology, and protected Oracle service names. Two embedded English-source figures retain English labels, and no native Brazilian Portuguese approval is claimed.

See [`qa/oracle-cloud/PT_BR_RECONSTRUCTION_QA.md`](qa/oracle-cloud/PT_BR_RECONSTRUCTION_QA.md).

## Remaining Brazilian Portuguese remediation

IBM Cloud remains an incomplete condensed edition. Kali Linux remains pending protected-token and native-language review.

## Latin American Spanish

All eight Spanish editions remain pending controlled protected-token and native-language review.

## Publication rule

Repository-wide status remains `FAIL`. Do not claim full multilingual parity until all high-severity findings are resolved or explicitly adjudicated and native-language, accessibility, technical, and page-level visual reviews are recorded at an exact commit SHA.
