# My Clinic e-learning — project map

![My Clinic logo](scorm-plans/00_program/brand/logo-preview.png)

> **As at 2026-10-19.** One page to find everything: the programme by phase, every module by phase, the check against the proposal, and the Oracle Learning sample. Detailed status and gaps: [`scorm-plans/00_program/programme-status.md`](scorm-plans/00_program/programme-status.md).

✅ done (draft, ready for review) · 🟡 in progress / draft built · ⬜ not started · 🔒 waiting on My Clinic

## 1. Where the project is

```text
Phase 0  Source lock & decisions      🔒  102 open decisions — kick-off with My Clinic not yet held
Phase 1  Action map & objectives      ✅  all 8 (SME approval pending)
Phase 2  Storyboards                  ✅  all 8 at v0.2 · 207 screens · client Word pack ready
Phase 3  Narration & media            🟡  scripts written (6 packs need a rewrite, G11) · companion art done · voices, images, captures pending
Phase 4  SCORM build                  🟡  v0.1-draft packages for all 8 (real compiler, 0 lint errors, SCORM 1.2) + Oracle sample
Phase 5  QA, LMS test, pilot          ⬜  harness tests passed on the sample · Oracle Learning test not yet run
```

## 2. Programme work by phase

| Phase | Programme deliverables | Status |
|---|---|---|
| **0 — Source lock** | [Decision sheet (102 rows)](scorm-plans/00_program/decision-sheet.md) · [D1–D14](scorm-plans/00_program/cross-module-decisions.md) · [Kick-off pack](scorm-plans/00_program/kickoff-pack.md) | 🔒 waiting on kick-off |
| **1 — Action map** | One `phase-1-action-map.md` per module (objectives, evidence, seat time) | ✅ |
| **2 — Storyboards** | [Storyboard template](scorm-plans/00_program/storyboard-template/) · [Review register](scorm-plans/00_program/storyboard-review-register.md) · [Client Word pack](scorm-plans/client-review/) · [Brand identity](scorm-plans/00_program/brand/brand-identity.md) · [Companions](scorm-plans/00_program/characters/companions.md) | ✅ v0.2, SME review pending |
| **3 — Narration & media** | [Narration & lexicon](scorm-plans/00_program/narration-and-lexicon.md) · [Visual & motion brief](scorm-plans/00_program/visual-and-motion-agent-brief.md) · [Motion spec](scorm-plans/00_program/motion-and-animation-spec.md) · full-size companion art | 🟡 voices (D10), 21–22 scene images, Oracle/EHR captures pending |
| **4 — Build** | [SCORM structure](scorm-plans/00_program/scorm-structure.md) · [Build pipeline](scorm-plans/00_program/build-pipeline.md) · [Draft builds](scorm-plans/00_program/draft-builds.md) | 🟡 drafts built; release builds after Phases 0 and 3 |
| **5 — QA & delivery** | [Oracle compatibility](scorm-plans/00_program/oracle-learning-compatibility.md) · [Oracle sample + test guide](scorm-plans/00_sample-oracle-pilot/) · [XSD validation](scorm-plans/00_program/xsd-validation.md) · [QA checklist](scorm-plans/00_program/qa-checklist.md) | 🟡 sample ready to send |

All programme files, grouped by phase: [`scorm-plans/00_program/README.md`](scorm-plans/00_program/README.md).

## 3. Module by module

Every module folder has the same files: `README.md`, `phase-0-source-lock.md` … `phase-5-qa-and-delivery.md`, `storyboard/`, `build/` and `scorm-structure.md`.

| Module | Proposal course | Phase 0 | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|---|---|---|---|---|---|---|---|
| **01** Facility Management & Safety | 1 HSE | [🔒 source lock](scorm-plans/01_health-and-safety-1/phase-0-source-lock.md) | [✅ action map](scorm-plans/01_health-and-safety-1/phase-1-action-map.md) | [✅ screen list](scorm-plans/01_health-and-safety-1/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/01_health-and-safety-1/storyboard/storyboard.md) · [board](scorm-plans/01_health-and-safety-1/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/01_health-and-safety-1/phase-3-narration-and-assets.md) · [script](scorm-plans/01_health-and-safety-1/storyboard/narration-script.json) · [assets](scorm-plans/01_health-and-safety-1/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/01_health-and-safety-1/build/MC_01_FMS_v0.1-draft_1.2.zip) · [preview](scorm-plans/01_health-and-safety-1/build/preview.html) · [structure](scorm-plans/01_health-and-safety-1/scorm-structure.md) · [plan](scorm-plans/01_health-and-safety-1/phase-4-build.md) | [⬜ QA plan](scorm-plans/01_health-and-safety-1/phase-5-qa-and-delivery.md) |
| **02** Safety in Practice Lab | 1 HSE | [🔒 source lock](scorm-plans/02_health-and-safety-2/phase-0-source-lock.md) | [✅ action map](scorm-plans/02_health-and-safety-2/phase-1-action-map.md) | [✅ screen list](scorm-plans/02_health-and-safety-2/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/02_health-and-safety-2/storyboard/storyboard.md) · [board](scorm-plans/02_health-and-safety-2/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/02_health-and-safety-2/phase-3-narration-and-assets.md) · [script](scorm-plans/02_health-and-safety-2/storyboard/narration-script.json) · [assets](scorm-plans/02_health-and-safety-2/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/02_health-and-safety-2/build/MC_02_SafetyLab_v0.1-draft_1.2.zip) · [preview](scorm-plans/02_health-and-safety-2/build/preview.html) · [structure](scorm-plans/02_health-and-safety-2/scorm-structure.md) · [plan](scorm-plans/02_health-and-safety-2/phase-4-build.md) | [⬜ QA plan](scorm-plans/02_health-and-safety-2/phase-5-qa-and-delivery.md) |
| **03** Welcome On Board (HR) | 2 HR | [🔒 source lock](scorm-plans/03_hr-employee-induction/phase-0-source-lock.md) | [✅ action map](scorm-plans/03_hr-employee-induction/phase-1-action-map.md) | [✅ screen list](scorm-plans/03_hr-employee-induction/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/03_hr-employee-induction/storyboard/storyboard.md) · [board](scorm-plans/03_hr-employee-induction/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/03_hr-employee-induction/phase-3-narration-and-assets.md) · [script](scorm-plans/03_hr-employee-induction/storyboard/narration-script.json) · [assets](scorm-plans/03_hr-employee-induction/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/03_hr-employee-induction/build/MC_03_WelcomeOnBoard_v0.1-draft_1.2.zip) · [preview](scorm-plans/03_hr-employee-induction/build/preview.html) · [structure](scorm-plans/03_hr-employee-induction/scorm-structure.md) · [plan](scorm-plans/03_hr-employee-induction/phase-4-build.md) | [⬜ QA plan](scorm-plans/03_hr-employee-induction/phase-5-qa-and-delivery.md) |
| **04** Who Does What: Operations & My Care | 3 Operations | [🔒 source lock](scorm-plans/04_operations-and-my-care/phase-0-source-lock.md) | [✅ action map](scorm-plans/04_operations-and-my-care/phase-1-action-map.md) | [✅ screen list](scorm-plans/04_operations-and-my-care/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/04_operations-and-my-care/storyboard/storyboard.md) · [board](scorm-plans/04_operations-and-my-care/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/04_operations-and-my-care/phase-3-narration-and-assets.md) · [script](scorm-plans/04_operations-and-my-care/storyboard/narration-script.json) · [assets](scorm-plans/04_operations-and-my-care/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/04_operations-and-my-care/build/MC_04_OpsMyCare_v0.1-draft_1.2.zip) · [preview](scorm-plans/04_operations-and-my-care/build/preview.html) · [structure](scorm-plans/04_operations-and-my-care/scorm-structure.md) · [plan](scorm-plans/04_operations-and-my-care/phase-4-build.md) | [⬜ QA plan](scorm-plans/04_operations-and-my-care/phase-5-qa-and-delivery.md) |
| **05** RCM Part A: Documentation & Coding | 4 RCM | [🔒 source lock](scorm-plans/05_rcm-documentation-and-coding/phase-0-source-lock.md) | [✅ action map](scorm-plans/05_rcm-documentation-and-coding/phase-1-action-map.md) | [✅ screen list](scorm-plans/05_rcm-documentation-and-coding/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/05_rcm-documentation-and-coding/storyboard/storyboard.md) · [board](scorm-plans/05_rcm-documentation-and-coding/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/05_rcm-documentation-and-coding/phase-3-narration-and-assets.md) · [script](scorm-plans/05_rcm-documentation-and-coding/storyboard/narration-script.json) · [assets](scorm-plans/05_rcm-documentation-and-coding/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/05_rcm-documentation-and-coding/build/MC_05_RCM-A_v0.1-draft_1.2.zip) · [preview](scorm-plans/05_rcm-documentation-and-coding/build/preview.html) · [structure](scorm-plans/05_rcm-documentation-and-coding/scorm-structure.md) · [plan](scorm-plans/05_rcm-documentation-and-coding/phase-4-build.md) | [⬜ QA plan](scorm-plans/05_rcm-documentation-and-coding/phase-5-qa-and-delivery.md) |
| **06** RCM Part B: EBP Benefits & Rejections | 4 RCM | [🔒 source lock](scorm-plans/06_rcm-ebp-benefits-and-rejections/phase-0-source-lock.md) | [✅ action map](scorm-plans/06_rcm-ebp-benefits-and-rejections/phase-1-action-map.md) | [✅ screen list](scorm-plans/06_rcm-ebp-benefits-and-rejections/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md) · [board](scorm-plans/06_rcm-ebp-benefits-and-rejections/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/06_rcm-ebp-benefits-and-rejections/phase-3-narration-and-assets.md) · [script](scorm-plans/06_rcm-ebp-benefits-and-rejections/storyboard/narration-script.json) · [assets](scorm-plans/06_rcm-ebp-benefits-and-rejections/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/06_rcm-ebp-benefits-and-rejections/build/MC_06_RCM-B_v0.1-draft_1.2.zip) · [preview](scorm-plans/06_rcm-ebp-benefits-and-rejections/build/preview.html) · [structure](scorm-plans/06_rcm-ebp-benefits-and-rejections/scorm-structure.md) · [plan](scorm-plans/06_rcm-ebp-benefits-and-rejections/phase-4-build.md) | [⬜ QA plan](scorm-plans/06_rcm-ebp-benefits-and-rejections/phase-5-qa-and-delivery.md) |
| **07** Clinical Governance: Quality, Safety & Risk | 5 Quality | [🔒 source lock](scorm-plans/07_quality-safety-and-risk/phase-0-source-lock.md) | [✅ action map](scorm-plans/07_quality-safety-and-risk/phase-1-action-map.md) | [✅ screen list](scorm-plans/07_quality-safety-and-risk/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/07_quality-safety-and-risk/storyboard/storyboard.md) · [board](scorm-plans/07_quality-safety-and-risk/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/07_quality-safety-and-risk/phase-3-narration-and-assets.md) · [script](scorm-plans/07_quality-safety-and-risk/storyboard/narration-script.json) · [assets](scorm-plans/07_quality-safety-and-risk/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/07_quality-safety-and-risk/build/MC_07_ClinicalGov_v0.1-draft_1.2.zip) · [preview](scorm-plans/07_quality-safety-and-risk/build/preview.html) · [structure](scorm-plans/07_quality-safety-and-risk/scorm-structure.md) · [plan](scorm-plans/07_quality-safety-and-risk/phase-4-build.md) | [⬜ QA plan](scorm-plans/07_quality-safety-and-risk/phase-5-qa-and-delivery.md) |
| **08** EHR Consultation Workflow | 6 IT | [🔒 source lock](scorm-plans/08_it-ehr-consultation/phase-0-source-lock.md) | [✅ action map](scorm-plans/08_it-ehr-consultation/phase-1-action-map.md) | [✅ screen list](scorm-plans/08_it-ehr-consultation/phase-2-storyboard.md) · [✅ storyboard v0.2](scorm-plans/08_it-ehr-consultation/storyboard/storyboard.md) · [board](scorm-plans/08_it-ehr-consultation/storyboard/screen-visuals.html) | [🟡 narration + assets](scorm-plans/08_it-ehr-consultation/phase-3-narration-and-assets.md) · [script](scorm-plans/08_it-ehr-consultation/storyboard/narration-script.json) · [assets](scorm-plans/08_it-ehr-consultation/storyboard/asset-register.md) | [🟡 v0.1-draft zip](scorm-plans/08_it-ehr-consultation/build/MC_08_EHR_v0.1-draft_1.2.zip) · [preview](scorm-plans/08_it-ehr-consultation/build/preview.html) · [structure](scorm-plans/08_it-ehr-consultation/scorm-structure.md) · [plan](scorm-plans/08_it-ehr-consultation/phase-4-build.md) | [⬜ QA plan](scorm-plans/08_it-ehr-consultation/phase-5-qa-and-delivery.md) |

Build order (learning path): **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.

## 4. Check against the proposal (Rev01)

| Proposal Rev01 | Now in the repo | Match |
|---|---|---|
| 6 courses as 8 SCORM packages | 8 module folders, 8 draft packages | ✅ |
| 207 screens | 54+26+36+13+21+15+22+20 = **207** | ✅ |
| 95 scored activities | 24+13+15+4+10+7+11+11 = **95** | ✅ |
| 26 scenarios, games and simulations | `scorm-base-audit`: **26** | ✅ |
| Pass marks HSE/RCM/Quality/IT 80%, HR/Ops 70% | same in every package | ✅ |
| ~4 h seat time | 55+33+45+15+25+20+25+25 min | ✅ |
| 81 test cases | 14+12+12+8+9+7+9+10 = **81** | ✅ |
| ~62 min narration in two voices | scripts ≈ 60 min (16.0+6.4+11.7+4.3+6.1+4.6+6.0+4.9); voices not recorded (D10) | 🟡 scripts ok, audio pending |
| Noor and Dr. Omar as guides | in all 8 packages, full-size art | ✅ |
| SCORM 1.2 or 2004 to match the LMS | **SCORM 1.2 for all 8** — matches Oracle Learning | ✅ (confirm with sample test) |
| Approved storyboards (Word/PDF) | v0.2 Word pack ready; approval pending | 🟡 |
| Narration audio, captions, transcripts | captions/transcripts in the packages; audio pending D10 | 🟡 |
| Asset pack with provenance | SVGs, companions, 3 scenes done; 21–22 scenes, 4 photos, 36 screenshots pending | 🟡 |
| 5 job aids (HR quick ref, desk checklist, EBP summary, EHR card, emergency-code cards) | planned in asset registers; not produced (facts pending Phase 0) | ⬜ |
| QTI 2.1 export | compiler supports `export_qti`; not run yet | ⬜ |
| LMS upload, test, admin guide | Oracle sample + test guide ready; admin guide not written | 🟡 |
| Phases 0–5 over 9–10 weeks | same phase model; clock starts at kick-off | ✅ |

**Verdict:** every number the client pays for matches. The open items are the ones the proposal itself places after the kick-off (approvals, voice, media, job aids, QTI, LMS hand-over).

## 5. Oracle Learning sample

My Clinic uses Oracle Applications Cloud, so the courses will run in **Oracle Learning**. The sample package lets their LMS team test upload, launch, tracking and resume now:

- Package: [`MC_Sample_OracleLearning_1.2.zip`](scorm-plans/00_sample-oracle-pilot/build/MC_Sample_OracleLearning_1.2.zip) (8 min, 13 screens, 4 scored checks, motion graphics, both guides, brand weave)
- Guide to send: [`oracle-learning-test-guide.md`](scorm-plans/00_sample-oracle-pilot/oracle-learning-test-guide.md)
- Why SCORM 1.2, and the evidence: [`oracle-learning-compatibility.md`](scorm-plans/00_program/oracle-learning-compatibility.md)

## 6. Folder guide

```text
elearning-course/
├── PROJECT-MAP.md            ← this page
├── md/                       source content, one Markdown file per source (8)
├── media/                    source screenshots (reference only)
├── proposal/                 L2S proposal Rev00, Rev01 (docx + pdf)
└── scorm-plans/
    ├── README.md             phase model, package map, timeline
    ├── 00_program/           programme files by phase (see its README)
    ├── 00_sample-oracle-pilot/  Oracle Learning sample package + test guide
    ├── 01_ … 08_/            one folder per SCORM package (phases 0–5, storyboard/, build/)
    ├── client-review/        Word storyboard pack for My Clinic
    └── tools/                build, audit, lint and test scripts
```
