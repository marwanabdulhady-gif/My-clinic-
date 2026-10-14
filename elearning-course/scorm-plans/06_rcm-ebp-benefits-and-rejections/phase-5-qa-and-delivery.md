# Phase 5 — QA & delivery (06 RCM Part B)

Run `../00_program/qa-checklist.md` first.

## 1. Module-specific test cases

| # | Test | Expected | Status |
|---|---|---|---|
| T1 | Every benefit, limit and exclusion matches the official EBP document | Signed by payer relations (B3, B5–B7) | pending |
| T2 | No claim number, patient, provider or date from slide 6 appears anywhere | None (B8) | pending |
| T3 | Regulator name identical to module 05 | Identical (D4) | pending |
| T4 | Cover shows the policy effective date, not the 2023 talk date | Correct (B1) | pending |
| T5 | `rcmb-060` behaves adaptively and can't be inflated by replay | Pass | pending |
| T6 | Added/amended sort matches the official classification | Match | pending |
| T7 | Pilot (3 physicians + 3 RCM staff) median seat time | 15–25 minutes | pending |

## 2. LMS delivery

- Package: `MC_06_RCM-B_v1.0_1.2.zip`. Assign to physicians, dentists and RCM/approvals staff; due within 30 days; re-assign whenever the EBP changes.

## 3. Maintenance triggers

- New EBP version or CHI circular.
- New top rejection comment in the monthly log.

## 4. Sign-off record

| Scope | Reviewer (role) | Revision | Date | Evidence | Decision |
|---|---|---|---|---|---|
| Phase 0 decisions | RCM lead | | | | |
| Benefit statements + adaptive bank | Payer relations | | | | |
| Rebuilt rejection log | DPO; Coding lead | | | | |
| Narration & voice | L&D | | | | |
| LMS test | LMS admin | | | | |
| Final release | Course owner | | | | |
