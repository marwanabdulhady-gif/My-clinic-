# Phase 5 — QA & delivery (02 Safety in Practice)

Run `../00_program/qa-checklist.md` first.

## 1. Module-specific test cases

| # | Test | Expected | Status |
|---|---|---|---|
| T1 | Store room (`hs2-011`): count visible hazards with 3 colleagues who haven't seen the key | Everyone finds the 6 keyed hazards; nobody finds an unintended one | pending |
| T2 | Code Red drill: best path, one-mistake path, two-mistake path (lives 0), hint use | Correct endings; debrief shown; score counted once | pending |
| T3 | Escape room: each alias accepted (`15`, `15 minutes`, `fifteen`; `orange`, `Code Orange`) and case-insensitive | Accepted | pending |
| T4 | Escape room: lives exhausted, retry | Restarts at puzzle 1; no double score | pending |
| T5 | Code Orange wording identical to module 01 (`hs1-507`) | Identical (D1) | pending |
| T6 | Extensions on `hs2-020` match the switchboard list | Match (D2) | pending |
| T7 | No H&S 2 PDF artwork present unless D12 closed | Asset provenance shows own/ai-generated only | pending |
| T8 | Register table: no supplier names or internal codes beyond what EHS approved | Approved | pending |
| T9 | Spill-kit steps (`hs2-053`) match the EHS-approved procedure (B4) | Match | pending |
| T10 | Keyboard-only completion of `hs2-031`, `hs2-041`, `hs2-070`, `hs2-032` | Possible | pending |
| T11 | SCORM 1.2 resume after Part E | Resumes with scores (suspend data under 4,096 chars) | pending |
| T12 | Pilot median seat time | 25–40 minutes | pending |

## 2. LMS delivery

- Package: `MC_02_SafetyLab_v1.0_1.2.zip`.
- Prerequisite: module 01 completed (LMS rule).
- Due within 10 days of start date.

## 3. Maintenance triggers

- Spill-kit contents or procedure change.
- The department register format changes.
- Code sheet or extensions change (shared with module 01).

## 4. Sign-off record

| Scope | Reviewer (role) | Revision | Date | Evidence | Decision |
|---|---|---|---|---|---|
| Phase 0 decisions | Safety & Security Manager | | | | |
| Store-room key and illustration | Safety & Security Manager | | | | |
| Drill and escape-room scripts | Safety & Security Manager; EHS | | | | |
| Narration & voice | L&D | | | | |
| Built package (preview) | Safety & Security Manager | | | | |
| LMS test | LMS admin | | | | |
| Final release | Course owner | | | | |
