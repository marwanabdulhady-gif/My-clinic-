# Phase 5 — QA & delivery (08 EHR Consultation)

Run `../00_program/qa-checklist.md` first.

## 1. Module-specific test cases

| # | Test | Expected | Status |
|---|---|---|---|
| T1 | Every screenshot in the built package reviewed for names, DOB, MRN, phone, ID, addresses, radiology/lab reports of real people | None found; DPO signs (D6) | pending |
| T2 | No frame from `IT.mp4` or `media/08_it-ehr-walkthrough/` in the package | None | pending |
| T3 | Every simulation step matches the current EHR build (button names, order of steps) | Match (B5) | pending |
| T4 | Typing steps accept the agreed variants (`E11`, `e11`, `type 2 diabetes`) | Accepted | pending |
| T5 | Wrong click shows the hint; keyboard users can complete each simulation | Pass | pending |
| T6 | Mandatory field list on `ehr-011`/`ehr-012` matches the system (B4) | Match | pending |
| T7 | Drug names approved by Pharmacy; non-formulary example correct | Approved (B6) | pending |
| T8 | Disclaimer present on `ehr-001` | Present (B7) | pending |
| T9 | Screenshots readable on a 13-inch laptop and a tablet | Readable | pending |
| T10 | Pilot with 4 new clinicians, then compare with their first week's incomplete-consultation count | Recorded | pending |

## 2. LMS delivery

- Package: `MC_08_EHR-Consultation_v1.0_1.2.zip`. Assign to physicians and clinical staff before their first clinic session (ideally with EHR access granted the same day).
- Quick-reference card posted on the intranet and printed for consultation rooms.

## 3. Maintenance triggers

- Any EHR release that changes the consultation, order, summary, SMS or referral screens → re-capture affected steps (minor version).
- Formulary change affecting the examples.

## 4. Sign-off record

| Scope | Reviewer (role) | Revision | Date | Evidence | Decision |
|---|---|---|---|---|---|
| PHI decision (D6) | DPO + IT | | | | |
| Screenshots and steps | EHR lead | | | | |
| Clinical examples + disclaimer | Medical Director | | | | |
| Drug examples | Pharmacy lead | | | | |
| Narration & voice | L&D | | | | |
| Built package PHI check | DPO | | | | |
| LMS test | LMS admin | | | | |
| Final release | Course owner | | | | |
