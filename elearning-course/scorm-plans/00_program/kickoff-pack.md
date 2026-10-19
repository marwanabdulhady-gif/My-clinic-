# Phase 0 kick-off pack — My Clinic induction e-learning

![My Clinic logo](brand/logo-preview.png)

> **Document MC-KO-01 · v0.2 · 2026-10-19** (v0.1 2026-10-14). Working pack for the Phase 0 kick-off meeting
> (proposed **Monday 2026-10-19**, week 1 of the proposal timeline). It exists so the meeting
> **closes decisions** instead of discovering them: every open item already has an owner role, a
> draft recommendation and a due date in the [decision sheet](decision-sheet.md).
> Nothing in this pack is approved course content; recommended answers are drafts for the named
> owner to confirm in writing.

---

## 1. What is ready, in one paragraph

Eight SCORM packages (six client courses), 207 core screens, 95 scored activities, ~62 minutes of
two-voice narration, all at **storyboard v0.2** with clean planning lint, a branded visual board per
module, an asset register per module and a client-shareable Word rendering per module. Proposal
**Rev01** matches those numbers. What is *not* ready is every fact that My Clinic owns: 102 open
decisions (28 safety/PHI/incident, 3 programme enablers, 71 module content facts), the voice route
(D10), the LMS and SCORM version (D9), brand confirmation (D11), and the module-08 test-environment
captures. Release builds cannot start until the tier-1 and tier-3 rows are closed.

**New since v0.1 (2026-10-19):** all eight packages exist as compiled, validated **v0.1-draft SCORM
packages** (open facts shown as `⚠ Draft — pending`); the full-size Noor and Dr. Omar artwork is in;
every screen carries the My Clinic brand weave. Because My Clinic runs Oracle Applications Cloud, the
packages are now **SCORM 1.2 for Oracle Learning**, and an 8-minute **Oracle Learning sample package**
with a test guide is ready for the LMS team — bring the result of that test to close D9.

## 2. Proposed 90-minute session

| Min | Item | Lead | Outcome before leaving the room |
|---|---|---|---|
| 0–10 | Programme shape: 6 courses / 8 packages, learning path `03 → 07 → 01 → 02 → 04 → 05 → 06 → 08`, Rev01 figures, 9–10 week plan | L2S | Shared picture; no debate on scope |
| 10–25 | Walk one storyboard end to end (module 04, 13 screens): what a v0.2 card contains, the `⚠ PENDING` convention, what the Word pack shows | L2S | Reviewers know how to read the pack |
| 25–45 | **Tier 1** (28 rows): D1 Code Orange, D2 code sheet + real extensions, D5 personal data, D6 IT video/PHI, D8 24-hour rule, plus the safety, radiation, IPSG, identifier and test-environment rows | Safety Manager, RSO, Nursing Director, DPO, IT | Owner + date confirmed per row; where the draft recommendation is accepted, say so and write it down |
| 45–60 | **Tier 3** enablers: D9 LMS + SCORM version (Oracle Learning, SCORM 1.2 — sample test result), D10 voice route (hear the two companion voice briefs), D11 brand confirmation | L&D/IT, course owner, Marketing | Three decisions or a named date inside week 2 |
| 60–80 | **Tier 2** by module (71 rows): agree the route, not the answers — who confirms leave tables, ICD-10 edition, rejection-log rebuild, org-chart lines, branch names | Module SMEs | Each module's rows assigned with dates ≤ 2026-10-30 |
| 80–90 | Write-back procedure, tracker import of the register CSV, next checkpoint, pilot window | L2S | Calendar entries; procedure accepted |

## 3. Who should be in the room

| Role | Decisions they own in this meeting |
|---|---|
| Safety & Security Manager (SME lead 01/02) | D1, D2, D12; 01 B1–B10; 02 B1–B9 |
| Radiation Safety Officer | 01 B4, B5 |
| Facilities / Engineering + Infection Control / EHS | 01 B6, B7; 02 spill and waste rows |
| HR lead + Communications | 03 B1–B14; D3, D5, D13 |
| Director of Operations + My Care Manager | 04 B1–B7 |
| RCM lead, Coding lead, Payer Relations | 05 B1–B10; 06 B1–B9; D4 |
| Quality Director + Patient Safety / Risk Manager | 07 B1–B11, NEW-01, P01; D7, D8 |
| EHR Applications lead + DPO + IT | 08 B1–B10; D6 |
| L&D / course owner | D9, D10, D14; scope and seat time |
| Marketing | D11 |

## 4. Pre-reads (send with the invite)

1. [Proposal Rev01 (PDF)](../../proposal/MyClinic_Induction_eLearning_Proposal_e2026-MC01_Rev01.pdf) — numbers and phases.
2. [Storyboard review pack (Word index)](../client-review/MyClinic_Elearning_Storyboard_Review_Pack_v0.2.docx) and the eight module renderings in [`../client-review/`](../client-review/).
3. [Decision sheet (Markdown)](decision-sheet.md) · [tracker CSV](decision-sheet.csv) — the 102 open rows.
4. [SME / build-detail register CSV](storyboard-review-register.csv) — the 52 screen-level authoring questions (import into your tracker).
5. [Asset & template audit](asset-template-audit.md) — what exists, what is still to be supplied (consented photos, test captures; companion art is done).
6. [Programme status](programme-status.md), the [project map](../../PROJECT-MAP.md) and the [production board](storyboard-production-board.md).
7. [Oracle Learning sample package](../00_sample-oracle-pilot/build/MC_Sample_OracleLearning_1.2.zip) + [test guide](../00_sample-oracle-pilot/oracle-learning-test-guide.md) — for the LMS administrator before the D9 item.

## 5. Same-day write-back procedure

1. Owner writes the decision **and its source** (policy number, poster, email, screenshot) in the
   file named in the decision sheet's “Write back to” column: `cross-module-decisions.md` for D*,
   the module's `phase-0-source-lock.md` (§2 row + §4 verified-facts register) for B*/NEW*.
2. Status becomes `Closed (YYYY-MM-DD)` in that file.
3. L2S reruns the gate chain (roadmap §standard exit gate): generator/normaliser → `lint_planning.py`
   → `build_scorm_structure.py` → `export_storyboard_docx.py` → `build_decision_sheet.py` (the closed
   row disappears from the open list) → `export_kickoff_docx.py` → `audit_assets.py`, which must exit
   clean.
4. If a decision changes a screen (wording, number, branch name), the same PR updates the Phase 2
   row and the storyboard card — never the card alone.

## 6. What the room does not decide

- Clinical or policy judgement beyond the sources: the plans only carry what the source documents
  say, marked `⚠ PENDING` until an owner confirms.
- LMS procurement and licence cost (D9 records the platform and SCORM version only).
- Voice provider contract value (D10 records route, provider and voice ids only).
- Anything that would put real patient, staff or claim data into a package: those rows close with
  “rebuild with fictional data”, never with “use the source file”.

## 7. After the kick-off

Tier 1 + tier 3 closed → chunks **C2–C5** (SME build-detail closure per module pair) and **C6–C9**
(voices, companion art, brand, 08 captures) start in parallel; Phase 3 media production (C10–C13)
follows per module in build order. See [`next-phases-roadmap.md`](next-phases-roadmap.md).
