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

## Remaining Brazilian Portuguese remediation

Microsoft Azure, AWS, Google Cloud, Oracle Cloud, and IBM Cloud remain incomplete condensed editions. Kali Linux remains pending protected-token and native-language review.

## Latin American Spanish

All eight Spanish editions remain pending controlled protected-token and native-language review.

## Publication rule

Repository-wide status remains `FAIL`. Do not claim full multilingual parity until all high-severity findings are resolved or explicitly adjudicated and native-language, accessibility, technical, and page-level visual reviews are recorded at an exact commit SHA.
