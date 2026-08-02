# Human Review Release Gate

Automated repository integrity, reconstruction, structural parity, and curated protected-identifier checks have passed. These results do **not** establish sentence-level semantic equivalence, native-language editorial quality, legal accuracy, accessibility conformance, technical correctness, or publication readiness.

## Review freeze rule

Before any human approval begins, record and freeze the exact candidate commit SHA. Every reviewer must inspect files from that SHA and include it in the signed review record. Any subsequent content or layout change invalidates affected approvals and requires review against the new SHA.

## Required review disciplines

1. **Native Spanish editorial review (`es-419`)**
   - Meaning and completeness against English
   - Natural neutral Latin American Spanish
   - Terminology consistency
   - No untranslated or mistranslated operational instructions
   - Correct localization of acronyms and institution names

2. **Native Brazilian Portuguese editorial review (`pt-BR`)**
   - Meaning and completeness against English
   - Natural Brazilian Portuguese
   - Terminology consistency
   - No untranslated or mistranslated operational instructions
   - Correct localization of acronyms and institution names

3. **Technical and security review**
   - Commands, configurations, examples, security controls, architecture statements, cloud-service names, and threat descriptions
   - No unsafe defaults, invented capabilities, obsolete instructions, or misleading guarantees

4. **Accessibility review**
   - Heading hierarchy, reading order, table comprehensibility, alternative text or equivalent descriptions, contrast, link meaning, selectable/searchable text, and keyboard/screen-reader usability where applicable

5. **Legal and regulatory review**
   - Regulatory references, standards claims, licensing language, disclaimers, jurisdictional limits, and statements that could be interpreted as legal advice or certification

6. **Professional prepress and page-level visual review**
   - Every PDF page inspected at normal and zoomed view
   - No clipping, overlap, orphaned headings, broken tables, blank pages, missing glyphs, distorted figures, or inaccessible URLs
   - Embedded English-source figure labels explicitly accepted, localized, or recorded as a release limitation

## Required evidence

Each approval record must include:

- Reviewer name and role
- Relevant qualifications or basis for review
- Review discipline
- Language and manual family scope
- Exact commit SHA
- Review start and completion dates
- Files reviewed
- Method used
- Findings and dispositions
- Explicit result: `APPROVED`, `APPROVED WITH DOCUMENTED LIMITATIONS`, or `CHANGES REQUIRED`
- Reviewer signature or attributable GitHub identity

## Release rule

Do not mark the multilingual package approved, mark PR #11 ready, or merge it until all required rows in `REVIEW_MATRIX.csv` have attributable evidence at the same exact candidate SHA. A missing review is a blocked gate, not an implicit approval.
