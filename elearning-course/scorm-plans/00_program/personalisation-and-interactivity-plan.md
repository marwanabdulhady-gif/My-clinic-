# Personalisation and interactivity plan

![My Clinic logo](brand/logo-preview.png)

**2026-10-19 · applies to all eight packages · owner decisions D15, D16 and D17 below**

The storyboards already match proposal Rev01: 207 screens, 95 scored, 26 scenarios, the same pass marks. The full check is in [`storyboard-proposal-check.md`](storyboard-proposal-check.md). They still felt flat for two reasons:
- every module opens with four or more screens before the learner does anything;
- nothing changes with the learner's job.

This plan fixes both **without touching anything scored**. Every scored activity, point, objective and pass mark stays exactly as reviewed.

---

## 1. Who the induction is for (assumed role catalogue)

Assumed until My Clinic confirms (decision **D15**). The source is [`roles.json`](roles.json).

| Role | Group in the packages | LMS learning path (order) |
|---|---|---|
| Physician (consultant, specialist, GP) | Clinical | 03 → 07 → 01 → 02 → 04 → 05 → 06 → 08 |
| Dentist and dental assistant | Clinical | 03 → 07 → 01 → 02 → 04 → 05 → 06 → 08 |
| Nurse | Clinical | 03 → 07 → 01 → 02 → 04 → 08 |
| Allied health (lab, radiology, pharmacy, physiotherapy) | Clinical | 03 → 07 → 01 → 02 → 04 |
| Reception, call centre, patient experience (PXO) | Front office & My Care | 03 → 07 → 01 → 02 → 04 |
| My Care coordinator and home care | Front office & My Care | 03 → 07 → 01 → 02 → 04 |
| RCM: insurance, billing, coding | Support & back office | 03 → 07 → 01 → 02 → 04 → 05 → 06 |
| Admin and support: HR, finance, IT, facilities, housekeeping, security | Support & back office | 03 → 01 → 02 → 04 |
| Managers and team leaders | any | their role path, plus the D14 attestation step as approver |

Personalisation works on **two levels**:

1. **LMS level — which packages a person gets.** These are Oracle Learning assignment rules by job role, as in the table. No package change is needed. The LMS cannot tell a package the learner's role (SCORM 1.2 has no role field), hence level 2.
2. **Inside each package — what the learner sees.** A one-click role picker sets `role` and `role_label`. After that:
   - role-tip screens appear only for that role;
   - closing screens speak to the learner ("As a front-office colleague: …");
   - the learner's own guesses and choices are replayed at the end.

   "Show me every role's tips" shows all roles side by side in tabs.

## 2. How it is built: the personalisation layer

The layer for each module is `<module>/production/personalisation.json`. `tools/personalise.py` applies it at build time, on top of the storyboard; the storyboard itself is never edited. The compiler fields it uses come from edumints @ 4bbf459:
- `variables`;
- a `branching` screen with `set_vars`;
- `visible_if: {var: "role", cmp: "==", value}`;
- `{{role_label}}` text interpolation;
- `exploration` screens with `<span data-exploration-ref>` replay.

Guards (the build stops if any is broken):
- nothing scored is added, removed or changed;
- only an unscored screen may be converted;
- ids stay unique;
- the closing screen is never hidden, so "viewed all" still completes;
- a step that needs a picture not made yet (`requires_asset`) is held back until the file exists. The media job list already asks for that picture.

Checked on 2026-10-19:
- All eight compile (0 lint errors, `validate_package` ok), and total points are unchanged (220 / 145 / 145 / 50 / 100 / 80 / 95 / 90).
- Visual walk-through of 03, 04 and 05 in the preview: picker, role tip for the chosen role only, quick checks, predictions, flip cards, the new 04 results screen and `{{role_label}}` on the close.

## 3. What is in each package now

| Package | Role picker | Role tip (one per group + "all") | Quick checks (unscored) | Prediction / guess replayed at the end | Converted screens | Learner sees |
|---|---|---|---|---|---|---|
| 01 FMS | `hs1-003` · Clinical / Front office & My Care / Support | `hs1-411` Your part in a Code Red | `hs1-303c` after the fire · `hs1-501c` unlabelled bottle | — | `hs1-410` → explore hotspot **when `hs1-img-staffroom` exists** (7 hazards) | 58 (54 + 4) |
| 02 Safety Lab | `hs2-002` | `hs2-031r` Your role in a real drill | `hs2-050c` Code Orange | `hs2-001p` how many hazards (slider) | — | 30 (26 + 4) |
| 03 Welcome On Board | `hr-003` · Medical / Front office / Back office | `hr-072` Your dress code | — | `hr-030p` your ethics principle | `hr-014`, `hr-022` → flip cards (leaders by role, no names: D5) | 39 (36 + 3) |
| 04 Who Does What | `ops-003` · Front office / My Care / Clinical / Support | `ops-034` Your first call | `ops-012` in the clinic now | `ops-001p` who takes this? | **`ops-089` results by objective** (closes the Rev01 gap) | 18 (13 + 5) |
| 05 RCM A | `rcma-003` · Physician / Dentist / RCM | `rcma-024` Specific coding in your work | `rcma-041c` covered? | (existing `rcma-002` poll) | — | 24 (21 + 3) |
| 06 RCM B | `rcmb-002` · Physician or dentist / RCM | `rcmb-053` Your part in rework | — | `rcmb-001p` how many new benefits | — | 18 (15 + 3) |
| 07 Clinical Governance | `qsr-003` | `qsr-024` Safety goals in your role | — | — | — | 24 (22 + 2) |
| 08 EHR | `ehr-003` · Physician / Nurse / Other | `ehr-043` Your part in the consultation | — | — | — | 22 (20 + 2) |

Every package's closing screen now carries one role line: "As a {{role_label}}: …". Role-tip wording is marked *Proposed — SME to confirm* on screen.

**Screen count (decision D16).** A learner sees **233** screens across the eight packages instead of 207, all extra ones unscored. The build files hold 257, because the role variants are hidden. Rev01 says "≈207 screens". Record this as a free value-add in the change log, or trim it.

## 4. More hotspots from the pictures we generate

Hotspot boxes now live in a map file next to each picture (`production/hotspots/<asset>.json`), not in the storyboard. So a newly generated picture can carry more hotspots than the original plan; [`media-production-runbook.md`](media-production-runbook.md) §3 has the tool and the rules.
- **Done:** the corridor picture (`hs1-404`) keeps its 8 checked boxes and gains a 9th, the stairwell exit (proposed, SME to confirm).
- **Staged:** `hs1-410` becomes a 7-hazard staff-room explore once `hs1-img-staffroom` is generated. The job, with its regions, is already in `01_…/production/media-jobs.json`.
- **Rule:** extra hotspots go live at once on explore and unscored screens. On a scored find-the-hazard screen they change the answer key, so they wait for SME approval.

## 5. Not built yet (backlog, from the 73-row audit)

[`interactivity-upgrades.json`](interactivity-upgrades.json) lists every proposal. Still open:
- **Explore hotspots on existing diagrams:** `hs1-305`, `ops-011`, `ops-021`, `qsr-010`, `qsr-040`. Each needs region boxes mapped on its SVG.
- **Explore hotspots on new or rebuilt pictures:**
  - `hs1-801` (pump): check it does not give away the `hs1-802` answer.
  - `hs2-060` (chemical register): needs B5.
  - `rcmb-050` (rejection log): needs B8.
  - `ehr-030` and `ehr-052`: need the captures.
- **Flip cards:** `hs1-103` and `hs1-907`; `rcma-020` and `rcma-030` (keep their tables).
- **Timelines:** `hr-080` and `qsr-050` (D8).
- **Picture for `rcma-012`–`rcma-050`:** the longest text-only run (lint `text_only_run`).

Mission framing ("Mission 3 of 9") is ready to switch on. It uses an `on_enter` counter and **no** visible points, badges or timers, in line with [`gamification-plan.md`](gamification-plan.md).

## 6. Optional motion-graphics videos (decision D17)

Nine 35–55 s clips are planned in [`media-video-plan.json`](media-video-plan.json): a programme welcome, one opener per package, and the existing `qsr-060` slot. They would be built with HyperFrames; [`video-tooling.md`](video-tooling.md) has the comparison with Remotion and the others. Rev01 needs none, so each clip is a value-add or a change request.

## 7. Decisions for the owner

| # | Decision | Recommendation |
|---|---|---|
| D15 | Confirm the role catalogue and LMS paths (§1) | Use as is; HR confirms job-family → role mapping in Oracle |
| D16 | +26 unscored screens per learner across the programme | Accept as a free value-add, logged in the proposal change log |
| D17 | Optional motion-graphics clips | Start with the programme welcome and `qsr-060`; decide the rest after the pilot |
