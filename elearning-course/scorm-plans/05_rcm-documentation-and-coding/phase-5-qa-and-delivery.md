# Phase 5 — QA & delivery (05 RCM Part A)

Run `../00_program/qa-checklist.md` first.

## 1. Module-specific test cases

| # | Test | Expected | Status |
|---|---|---|---|
| T1 | Every ICD-10 code and title checked by the coding lead in the edition used | Signed list | pending |
| T2 | Regulator name consistent with module 06 | Identical (D4) | pending |
| T3 | Repeat-test intervals match the confirmed values (B2, B3) | Match | pending |
| T4 | No real patient, claim or physician data in any example | None | pending |
| T5 | `rcma-002` poll answer revealed in `rcma-040` feedback | Shown | pending |
| T6 | `rcma-050` all three nodes: best, weaker, hint | Correct feedback; score counted once | pending |
| T7 | Clinical disclaimer present | Present | pending |
| T8 | Pilot with 4–6 physicians from different specialties: perceived relevance ≥ 4/5 | Met | pending |
| T9 | Pilot median seat time | 20–30 minutes | pending |

## 2. LMS delivery

- Package: `MC_05_RCM-A_v1.0_1.2.zip`. Assign to physicians and dentists; due within 30 days of start; refresher yearly.
- Desk checklist PDF also posted on the intranet.

## 3. Impact check (after 3 months)

Compare the rejection rate by reason (missing justification, non-specific diagnosis, incomplete documentation, mismatch) for trained vs not-yet-trained physicians. Share results with the RCM lead and adjust the scenario content.

## 4. Maintenance triggers

- Payer coverage or ICD-10 edition change.
- New top-5 rejection reason in the monthly report.
- Review every 6 months.

## 5. Sign-off record

| Scope | Reviewer (role) | Revision | Date | Evidence | Decision |
|---|---|---|---|---|---|
| Phase 0 decisions | RCM/CDI physician lead | | | | |
| Codes | Coding lead | | | | |
| Clinical vignettes | Medical Director | | | | |
| Coverage statements | Payer relations | | | | |
| Narration & voice | L&D | | | | |
| LMS test | LMS admin | | | | |
| Final release | Course owner | | | | |
