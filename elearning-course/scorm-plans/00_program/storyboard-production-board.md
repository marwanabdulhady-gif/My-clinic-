# My Clinic — storyboard production board

![My Clinic logo](brand/logo-preview.png)

> Consolidated review status as at **2026-10-14**. This is a production-documentation board, not a statement that policy, clinical, payer or EHR content is approved.

**Client-shareable Word renderings:** [`../client-review/README.md`](../client-review/README.md). The Markdown/JSON/HTML files below remain the editable production source.

**SME/build-detail queue:** [`storyboard-review-register.md`](storyboard-review-register.md) · [`CSV import`](storyboard-review-register.csv).

## What is now documented

| Module | Screen cards | Scored / points | Script + visual plan | Branded screen review | Asset register | Planning lint | Production status |
|---|---:|---:|---|---|---|---|---|
| 01 — [Facility Management & Safety](../01_health-and-safety-1/storyboard/storyboard.md) | 54 | 24 / 220 | [JSON](../01_health-and-safety-1/storyboard/narration-script.json) · [visual plan](../01_health-and-safety-1/storyboard/visual-plan.json) | [HTML](../01_health-and-safety-1/storyboard/screen-visuals.html) | [register](../01_health-and-safety-1/storyboard/asset-register.md) | [Clean report](../01_health-and-safety-1/storyboard/lint-report.json) | Draft — SME/source-lock review |
| 02 — [Safety in Practice: Hazard, Fire & Chemical Lab](../02_health-and-safety-2/storyboard/storyboard.md) | 26 | 13 / 145 | [JSON](../02_health-and-safety-2/storyboard/narration-script.json) · [visual plan](../02_health-and-safety-2/storyboard/visual-plan.json) | [HTML](../02_health-and-safety-2/storyboard/screen-visuals.html) | [register](../02_health-and-safety-2/storyboard/asset-register.md) | [Clean report](../02_health-and-safety-2/storyboard/lint-report.json) | Draft — SME/source-lock review |
| 04 — [Who Does What: Operations & My Care](../04_operations-and-my-care/storyboard/storyboard.md) | 13 | 4 / 50 | [JSON](../04_operations-and-my-care/storyboard/narration-script.json) · [visual plan](../04_operations-and-my-care/storyboard/visual-plan.json) | [HTML](../04_operations-and-my-care/storyboard/screen-visuals.html) | [register](../04_operations-and-my-care/storyboard/asset-register.md) | [Clean report](../04_operations-and-my-care/storyboard/lint-report.json) | Draft — SME/source-lock review |
| 05 — [RCM Part A: Documentation & ICD-10 Coding That Gets Approved](../05_rcm-documentation-and-coding/storyboard/storyboard.md) | 21 | 10 / 100 | [JSON](../05_rcm-documentation-and-coding/storyboard/narration-script.json) · [visual plan](../05_rcm-documentation-and-coding/storyboard/visual-plan.json) | [HTML](../05_rcm-documentation-and-coding/storyboard/screen-visuals.html) | [register](../05_rcm-documentation-and-coding/storyboard/asset-register.md) | [Clean report](../05_rcm-documentation-and-coding/storyboard/lint-report.json) | Draft — SME/source-lock review |
| 06 — [RCM Part B: New EBP Benefits & Claim-Rejection Analysis](../06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md) | 15 | 7 / 80 | [JSON](../06_rcm-ebp-benefits-and-rejections/storyboard/narration-script.json) · [visual plan](../06_rcm-ebp-benefits-and-rejections/storyboard/visual-plan.json) | [HTML](../06_rcm-ebp-benefits-and-rejections/storyboard/screen-visuals.html) | [register](../06_rcm-ebp-benefits-and-rejections/storyboard/asset-register.md) | [Clean report](../06_rcm-ebp-benefits-and-rejections/storyboard/lint-report.json) | Draft — SME/source-lock review |
| 08 — [EHR Consultation Workflow: Guided Simulation](../08_it-ehr-consultation/storyboard/storyboard.md) | 20 | 11 / 90 | [JSON](../08_it-ehr-consultation/storyboard/narration-script.json) · [visual plan](../08_it-ehr-consultation/storyboard/visual-plan.json) | [HTML](../08_it-ehr-consultation/storyboard/screen-visuals.html) | [register](../08_it-ehr-consultation/storyboard/asset-register.md) | [Clean report](../08_it-ehr-consultation/storyboard/lint-report.json) | Draft — SME/source-lock review |
| 03 — Welcome On Board | 36 | 15 / 145 | Existing storyboard, visual plan and narration script | Existing brand mockups | Existing preview/audio reference | Not rerun in this pass | Draft — SME review |
| 07 — Clinical Governance | 22 core | 11 / 95 | Existing storyboard | Existing brand mockups | Pending policy/source review | Not available in this pass | Draft — SME review |

## Phase gate snapshot

| Phase | What is materially complete | What cannot be claimed yet |
|---|---|---|
| 0 — Source lock | Owners, conflicts and explicit open decisions are documented for all eight modules. | No module with open B/D records is released to production. |
| 1 — Action map | Objectives, practice and seat-time budgets are in every module folder. | SMEs still approve objectives and evidence. |
| 2a — Screen list | All eight plans have a Phase 2 screen list. | Changes must return to Phase 2 before build. |
| 2b — Storyboard cards | 03 and 07 existed; 01, 02, 04, 05, 06 and 08 now have complete review-card packs. | Pending values cannot be treated as course facts. |
| 3 — Narration/assets | Each new pack now has an editable narration script, voice-talent table, visual plan, asset register and logo placement rules. | D10 voice choice, approved scripts, EHR test captures and asset approval remain open. |
| 4–5 — Build/QA | Build plans and QA plans exist. | No SCORM project, package, LMS test, QA sign-off or completion data is claimed. |

## Decisions that still gate release

1. **Safety:** Code Orange threshold, real emergency extensions, waste colours, radiation/laser details and facility-specific information (modules 01–02).
2. **Operations:** live reporting lines, abbreviation expansions and escalation ownership (module 04).
3. **RCM:** current payer/regulator wording, ICD-10 validation, benefits/limits and de-identified rejection classifications (modules 05–06).
4. **EHR:** only a test environment/test patient may be captured; the existing source video is never a production asset (module 08).
5. **Programme:** Marketing brand confirmation D11, two approved narration voices D10 and every asset’s provenance/approval record.

## Asset work completed in this pass

- Generated native editable SVG diagrams where facts can be changed after SME review.
- Generated three review-only, no-logo visual assets: the facility safety corridor, safety lab storeroom and Operations reception scenario.
- Added the `brand-kit.edumints.json` adapter to resolve the known official-brand-kit formality mismatch without changing the client’s official `brand-kit.json`.
- Added HTML visual review boards that use the supplied My Clinic logo and obey the Montserrat / navy / module-colour system.

## Next hand-off

1. Start with the screen-level [SME/build-detail register](storyboard-review-register.md), then circulate the matching `storyboard/storyboard.md` and `screen-visuals.html` to each named SME.
2. Close Phase 0 records in writing; update only the source-lock file and cards that cite that decision.
3. Choose/approve Noor and Dr. Omar voice samples under D10 before generating shipping audio.
4. For module 08, capture test-environment screenshots and obtain DPO approval before any simulation build.
5. The visual-plan and narration-script lint reports are currently clean for the six new packs; rerun them, plus `lint_authoring_plan(stage=planning)`, after any approved edit and before Phase 4 build.
