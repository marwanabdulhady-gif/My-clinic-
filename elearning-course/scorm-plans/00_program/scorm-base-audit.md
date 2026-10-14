# Base SCORM structure audit — all eight packages

Generated 2026-10-14 by `tools/audit_scorm_base.py`. **Clean — no hard failures.**

> Planning-stage audit of the storyboard build blocks and the generated structure documents. No SCORM package has been built or launched, so nothing here is an LMS or SCORM conformance result.

## Programme totals

| Measure | Value | Reconciles with |
|---|---:|---|
| Packages | 8 | six commercial courses → eight SCORM packages |
| Screens | 207 | programme structure §1 |
| Scored screens | 95 | programme structure §1 |
| Interaction records | 95 | one per scored screen |
| Scenario / game / simulation screens | 26 | Rev01: 26 experiences |
| LMS objectives | 44 | per-package §5 |
| Objectives on a single scored screen | 14 | programme gap G4 |
| Scored screens with authored feedback | 26 / 95 | Phase 4 build work |
| Excluded-mechanic mentions | 0 | gamification-plan.md |

## Per package

| # | Package | SCORM | Screens | Scored | Pts | Pass | Objectives | Scenarios | Interactions | Resume (est./limit) | Checklist | Structure doc |
|---|---|---|---:|---:|---:|---|---:|---|---|---|---|---|
| 01 | health-and-safety-1 | 2004 | 54 | 24 | 220 | 80% (176) | 10 | 5/5 | choice×5, matching×7, performance×6, sequencing×4, true-false×2 | 2,448 / 64,000 | 10/12 | fresh |
| 02 | health-and-safety-2 | 1.2 | 26 | 13 | 145 | 80% (116) | 7 | 3/3 | choice×3, fill-in×2, matching×4, performance×3, sequencing×1 | 1,248 / 4,096 | 10/12 | fresh |
| 03 | hr-employee-induction | 2004 | 36 | 15 | 145 | 70% (102) | 6 | 4/4 | choice×5, fill-in×1, matching×5, performance×3, true-false×1 | 1,584 / 64,000 | 12/12 | fresh |
| 04 | operations-and-my-care | 1.2 | 13 | 4 | 50 | 70% (35) | 3 | 1/1 | choice×1, matching×2, performance×1 | 504 / 4,096 | 10/12 | fresh |
| 05 | rcm-documentation-and-coding | 1.2 | 21 | 10 | 100 | 80% (80) | 5 | 2/2 | choice×3, matching×3, performance×2, sequencing×1, true-false×1 | 984 / 4,096 | 10/12 | fresh |
| 06 | rcm-ebp-benefits-and-rejections | 1.2 | 15 | 7 | 80 | 80% (64) | 3 | 2/2 | choice×2, matching×3, performance×1, true-false×1 | 696 / 4,096 | 10/12 | fresh |
| 07 | quality-safety-and-risk | 1.2 | 22 | 11 | 95 | 80% (76) | 5 | 2/2 | fill-in×1, matching×4, performance×2, sequencing×3, true-false×1 | 1,056 / 4,096 | 11/12 | fresh |
| 08 | it-ehr-consultation | 1.2 | 20 | 11 | 90 | 80% (72) | 5 | 7/7 | choice×3, performance×7, sequencing×1 | 1,008 / 4,096 | 10/12 | fresh |

## Base requirements per package

| Requirement | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 |
|---|---|---|---|---|---|---|---|---|
| Manifest: one organization, one item, one SCO resource **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Pass mark written to the manifest | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Every objective has at least one scored screen **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Every scored screen names its objective **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Every scored screen maps to an interaction type **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Completion rule set **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Resume state fits the SCORM version's suspend_data limit **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gamification rules recorded for every scenario screen **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Answer feedback authored for the scored checks | ⚠ | ⚠ | ✅ | ⚠ | ⚠ | ⚠ | ✅ | ⚠ |
| No excluded gamification mechanic introduced **(hard)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Motion spec present for every screen | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Thin-evidence objectives flagged for SME sign-off | ⚠ | ⚠ | ✅ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |

⛔ = hard failure (blocks the Phase 4 gate) · ⚠ = open work, SME sign-off or Phase 4 authoring.

## Open items

- **01 01_health-and-safety-1** — Answer feedback authored for the scored checks; Thin-evidence objectives flagged for SME sign-off
- **02 02_health-and-safety-2** — Answer feedback authored for the scored checks; Thin-evidence objectives flagged for SME sign-off
- **04 04_operations-and-my-care** — Answer feedback authored for the scored checks; Thin-evidence objectives flagged for SME sign-off
- **05 05_rcm-documentation-and-coding** — Answer feedback authored for the scored checks; Thin-evidence objectives flagged for SME sign-off
- **06 06_rcm-ebp-benefits-and-rejections** — Answer feedback authored for the scored checks; Thin-evidence objectives flagged for SME sign-off
- **07 07_quality-safety-and-risk** — Thin-evidence objectives flagged for SME sign-off
- **08 08_it-ehr-consultation** — Answer feedback authored for the scored checks; Thin-evidence objectives flagged for SME sign-off

## Hard failures

- none

## What this audit does not cover

- SCORM conformance: no package has been built, launched or tested against an LMS.
- Answer-key or SME approval status: see each pack's Phase 0 decision sheet and `programme-status.md`.
- The real `suspend_data` payload, which only the built player can measure; the figures here are the documented estimate.
