# Translation Parity Status

**Current status: FAIL — remediation required**

The repository's package-integrity audit passes: files open, PDFs contain searchable text, DOCX packages are readable, and local links resolve.

A stricter English–Spanish–Portuguese parity audit at candidate SHA `19af0d897962c1d0ef4f8f767590873eb18854ea` found 31 high-severity discrepancies.

## Brazilian Portuguese

The following Portuguese editions are materially shorter than their English baselines and cannot currently be represented as complete translations:

- AI Risk Management — 8.8% of English DOCX word count
- Microsoft Azure AI Security — 5.2%
- AWS AI Security — 5.4%
- Google Cloud AI Security — 5.4%
- IBM Cloud AI Security — 24.9%
- Oracle Cloud AI Security — 24.6%
- ISO/IEC 42001 — 8.1%

These editions also lose substantial heading structure and protected technical tokens.

The Kali Linux / AI Security / Digital Forensics Portuguese edition is structurally close to English but still requires protected-token and native-language review.

## Latin American Spanish

All eight Spanish editions triggered protected-token differences against English. These findings require controlled review to distinguish actual omissions or mistranslations from benign translation differences.

## Publication rule

Until remediation and exact-SHA review are complete:

- do not describe the affected Portuguese files as full equivalents of the English manuals;
- do not claim that Spanish or Portuguese editions are error-free;
- retain the downloads only as review candidates;
- rebuild affected DOCX/PDF packages after correction;
- require automated parity, technical, native-language, accessibility, and page-by-page visual review before approval.

See [`qa/full-multilingual-parity/FULL_MULTILINGUAL_CONTENT_PARITY_AUDIT.md`](qa/full-multilingual-parity/FULL_MULTILINGUAL_CONTENT_PARITY_AUDIT.md) for the controlled findings.
