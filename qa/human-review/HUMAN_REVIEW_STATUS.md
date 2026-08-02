# Human Review Status Dashboard

**Publication status: BLOCKED PENDING HUMAN REVIEW**

This dashboard is generated from `REVIEW_MATRIX.csv`. It reports evidence state only; it does not create or imply approval.

## Overall status

- Total required gates: **64**
- Pending: **64**
- In review: **0**
- Approved: **0**
- Rejected: **0**
- Approved exact SHA set: **none**

## Family status

| Manual family | Tracker | Total | Pending | In review | Approved | Rejected |
|---|---:|---:|---:|---:|---:|---:|
| AI Risk Management | [#12](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/12) | 8 | 8 | 0 | 0 | 0 |
| AWS AI Security | [#13](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/13) | 8 | 8 | 0 | 0 | 0 |
| Google Cloud AI Security | [#14](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/14) | 8 | 8 | 0 | 0 | 0 |
| IBM Cloud AI Security | [#15](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/15) | 8 | 8 | 0 | 0 | 0 |
| Microsoft Azure AI Security | [#16](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/16) | 8 | 8 | 0 | 0 | 0 |
| Oracle Cloud AI Security | [#17](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/17) | 8 | 8 | 0 | 0 | 0 |
| ISO/IEC 42001 | [#18](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/18) | 8 | 8 | 0 | 0 | 0 |
| Kali Linux AI Security and Forensics | [#19](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/19) | 8 | 8 | 0 | 0 | 0 |

## Release blockers

All 64 required matrix gates remain `PENDING`. See `REVIEW_MATRIX.csv` for the authoritative gate-level inventory.

## Control references

- Master release issue: [#20](https://github.com/Chpmunk31456/AI-Security-Manuals/issues/20)
- Draft publication PR: [#11](https://github.com/Chpmunk31456/AI-Security-Manuals/pull/11)
- Evidence rules: `qa/human-review/README.md`
- Attestation template: `qa/human-review/REVIEW_ATTESTATION_TEMPLATE.md`
- Review packet workflow: `.github/workflows/build-human-review-packets.yml`

Do not mark PR #11 ready or merge it until every required gate has attributable evidence at one frozen exact candidate SHA.
