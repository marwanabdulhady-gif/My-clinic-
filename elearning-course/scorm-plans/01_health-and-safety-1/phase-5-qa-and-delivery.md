# Phase 5 — QA & delivery (01 Facility Management & Safety)

Run the common checklist in `../00_program/qa-checklist.md` first. Then these module-specific tests.

## 1. Module-specific test cases

| # | Test | Expected | Status |
|---|---|---|---|
| T1 | Every code name and extension on `hs1-301`/`302` matches the facility code poster (D2) | Exact match, bilingual names correct | pending |
| T2 | Code Orange rule identical in `hs1-507` feedback, `hs1-950` and module 02 | One wording everywhere (D1) | pending |
| T3 | `hs1-405` and `hs1-508` usable by keyboard only | All items placed without a mouse | pending |
| T4 | `hs1-503` NFPA quiz does not rely on colour | Each quadrant labelled by position and text | pending |
| T5 | Waste bins on `hs1-508` match the real bin colours (B7) | Match | pending |
| T6 | Dose bands on `hs1-905` match the RSO-confirmed values (B4) | Match | pending |
| T7 | Walk every route of `hs1-205`, `hs1-409`, `hs1-507`, `hs1-802`, `hs1-950` (best, poor, lives exhausted, hint) | Feedback shown; score counted once | pending |
| T8 | Section menu: jump to section 9 first, then back to section 1 | Free navigation; progress kept | pending |
| T9 | Close the browser after section 5, reopen in LMS | Resumes at section 5 with scores kept (SCORM 2004) | pending |
| T10 | Score exactly 176/220 (80%) | Passed | pending |
| T11 | Score 175/220 | Failed; LMS shows incomplete or failed per completion rule | pending |
| T12 | `hs1-980` results breakdown | 10 objectives listed; weak ones flagged below 70% | pending |
| T13 | No `[Facility Name]`, `[Month Year]` or `5555` text anywhere | Search returns nothing | pending |
| T14 | Seat time in pilot | 45–65 minutes median | pending |

## 2. LMS delivery

- Package: `MC_01_FMS_v1.0_1.2.zip`.
- LMS activity settings: new attempt allowed after fail; record highest score; launch in a new window (recommended for Moodle).
- After the package: LMS attestation step for the safety acknowledgement (D14).
- Assign to: all new staff, due within 7 days of start date. Annual refresher: same package, or a short refresher built later from the section checks.

## 3. Maintenance triggers (re-open Phase 0)

- The facility's emergency code sheet or extensions change.
- CBAHI publishes a new FMS chapter edition.
- Radiation regulation or facility dose bands change.
- A drill or incident review finds a common error not covered by a scored screen.

## 4. Sign-off record

| Scope | Reviewer (role) | Revision | Date | Evidence | Decision |
|---|---|---|---|---|---|
| Phase 0 decisions | Safety & Security Manager | | | decision log | |
| Storyboard & visuals | Safety & Security Manager; L&D | | | | |
| Section 8 content | Biomedical Engineering lead | | | | |
| Section 9 content | Radiation Safety Officer | | | | |
| Narration script & voice | L&D | | | | |
| Built package (preview) | Safety & Security Manager | | | | |
| LMS test | L&D / LMS admin | | | | |
| Final release | Course owner | | | | |
