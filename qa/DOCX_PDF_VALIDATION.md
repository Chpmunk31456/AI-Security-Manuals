# DOCX and PDF Validation

**Status: FAIL**

## Mechanical results

- 24/24 DOCX files: ZIP archives readable; XML members parse; relationships and embedded media inventoried.
- 24/24 PDFs: readable; page counts inventoried; searchable text present; no text-empty pages detected.
- 1,046/1,046 PDF pages: rasterized to non-empty JPEG images at 36 DPI.
- Contact-sheet inspection: no gross blank-page or whole-page rendering failure observed.
- DOCX/PDF word-count ratios remain sufficiently close to identify each pair as the same packaged edition.

## Why the status is FAIL

Mechanical validity cannot compensate for missing content. Seven pt-BR packages are structurally incomplete. Low-resolution contact-sheet inspection is suitable for gross defects, not fine clipping, font substitution, missing-glyph adjudication, accessibility, or print-production approval. A qualified human must inspect final rebuilt packages at normal zoom before publication.

Exact counts, metadata, media lists, link targets, and hashes are in `FULL_MULTILINGUAL_CONTENT_PARITY_INVENTORY.json`.
