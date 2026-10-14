# Storyboard — 08 EHR Consultation Workflow: Guided Simulation

![My Clinic logo](../../00_program/brand/logo-preview.png)

> **Review pack v0.2 · 2026-10-14.** This document completes the screen-card, narration, visual-plan,
> asset-register and visual-review documentation for every core screen in
> [`../phase-2-storyboard.md`](../phase-2-storyboard.md). It is a review artefact, **not an approved
> policy or production SCORM package**. Source-lock decisions are deliberately retained as `⚠ PENDING`.

**Companion documents:** [`screen-visuals.html`](screen-visuals.html) ·
[`visual-plan.json`](visual-plan.json) · [`narration-script.json`](narration-script.json) ·
[`voice_talent.md`](voice_talent.md) · [`asset-register.md`](asset-register.md) · [`lint-report.json`](lint-report.json).

---

## A. Module header

| Field | Value |
|---|---|
| Module | 08 — My Clinic — EHR Consultation Workflow: Guided Simulation |
| Module prefix | `ehr-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead |
| Audience | Physicians and clinical staff who document consultations in the clinic EHR |
| Seat-time budget | ~25 minutes |
| SCORM / completion / pass mark | SCORM 1.2 · viewed_all_and_passed · pass 80% (72 / 90) |
| Scored screens / total points | 11 / 90 (Phase 4 expectation: 11 / 90) |
| Source file | `elearning-course/md/08_video-it-ehr-consultation-walkthrough.md` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-14) |
| Module colour | Dark teal #006E78 |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | B1–B10; program D6 and D11 |
| Narration reconciliation | Detailed card scripts: 5.1 min; Phase 3 per-screen targets: 5.1 min; Phase 3 rough module estimate: ~5 min. Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review. |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
| `ehr-o1` | Open a consultation and complete the mandatory fields. | `ehr-010`, `ehr-012` |
| `ehr-o2` | Add a primary diagnosis using ICD-10 code or name search. | `ehr-020` |
| `ehr-o3` | Place medication, lab and package orders linked to the assessed diagnosis. | `ehr-031`, `ehr-032`, `ehr-033`, `ehr-034` |
| `ehr-o4` | Produce the consultation summary, send education by SMS, and make a referral with follow-up. | `ehr-040`, `ehr-041`, `ehr-050` |
| `ehr-o5` | Put the complete consultation workflow in the correct order. | `ehr-051` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `ehr-sA` | The workflow | `ehr-000`–`ehr-002` |
| `ehr-sB` | Open & document | `ehr-010`–`ehr-012` |
| `ehr-sC` | Diagnosis | `ehr-020`–`ehr-020` |
| `ehr-sD` | Orders | `ehr-030`–`ehr-034` |
| `ehr-sE` | Summary & education | `ehr-040`–`ehr-042` |
| `ehr-sF` | Referral & finish | `ehr-050`–`ehr-091` |

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

### `ehr-000` — EHR Consultation Workflow: Guided Simulation

**Status:** `Draft — ready for SME review` · **Section / node:** The workflow / `ehr-sA` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | EHR Consultation Workflow: Guided Simulation |
| Body / keywords | "EHR consultation workflow" · "Guided practice on a test patient" |
| Word count (excl. title) | 9 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L1 Title |
| Logo | `logo-horizontal-white.png`, 48 px at top-left |
| Visual concept | Official navy title gradient with supplied white My Clinic logo, large Montserrat course title, and a cropped white petal watermark. Omar is placed l1 half-body bottom-right. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `primary` · text `on_primary` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | Supplied white petal mark at 8–10% opacity, cropped off the right edge. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-welcome · placement L1 half-body bottom-right · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Official navy title background supplied by My Clinic; no content is baked into it.` | photo | Official navy title background supplied by My Clinic; no content is baked into it. | own / official My Clinic asset | Decorative navy title gradient. | Yes |
| `Supplied My Clinic horizontal white logo lock-up.` | icon | Supplied My Clinic horizontal white logo lock-up. | own / official My Clinic asset | My Clinic logo. | No |
| `ehr-capture-sheet` | diagram | ehr-capture-sheet: Generated capture checklist only; not an EHR screenshot and not a substitute for B2 test-environment assets. | own SVG | Checklist showing safe test-environment screenshot requirements. | No |
| `Approved program companion pose char-omar-welcome at L1 half-body bottom-right.` | illustration | Approved program companion pose char-omar-welcome at L1 half-body bottom-right. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "EHR consultation workflow" · "Guided practice on a test patient" |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | warm |
| Target seconds | 12 |
| Word count / estimated seconds | 28 words / ≈ 12 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Welcome to EHR Consultation Workflow: Guided Simulation. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "title_slide",
  "id": "ehr-000",
  "title": "EHR Consultation Workflow: Guided Simulation",
  "section": "The workflow",
  "node_id": "ehr-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-000",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-000`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-001` — Why + disclaimer

**Status:** `Draft — ready for SME review` · **Section / node:** The workflow / `ehr-sA` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Why + disclaimer |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why + disclaimer |
| Body / keywords | Complete, linked, on the day · Disclaimer (B7) · "Everything here is a test patient." |
| Word count (excl. title) | 13 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for why + disclaimer, using a navy header, concise keyword cards and one Dark teal #006E78 highlight. Omar is placed l3 right column. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-explaining · placement L3 right column · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ehr-capture-sheet` | diagram | ehr-capture-sheet: Generated capture checklist only; not an EHR screenshot and not a substitute for B2 test-environment assets. | own SVG | Checklist showing safe test-environment screenshot requirements. | No |
| `Approved program companion pose char-omar-explaining at L3 right column.` | illustration | Approved program companion pose char-omar-explaining at L3 right column. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Complete, linked, on the day · Disclaimer (B7) · "Everything here is a test patient." |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | calm, practical |
| Target seconds | 25 |
| Word count / estimated seconds | 57 words / ≈ 24.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Complete, specific, linked — on the day. Read the disclaimer. Keep the main point connected to a familiar task or conversation. That connection makes the information easier to use when it matters. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "ehr-001",
  "title": "Why + disclaimer",
  "section": "The workflow",
  "node_id": "ehr-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-001",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-001`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-002` — Workflow map

**Status:** `Draft — ready for SME review` · **Section / node:** The workflow / `ehr-sA` · **Type:** `timeline` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Workflow map |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | process map |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Workflow map |
| Body / keywords | 9 steps as events: 1 Open · 2 Document · 3 Diagnose · 4 Order · 5 Review orders · 6 Summary · 7 Educate · 8 Refer & follow up · 9 Complete |
| Word count (excl. title) | 25 |
| Instruction | Click through |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for workflow map, using a navy header, concise keyword cards and one Dark teal #006E78 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 9 steps as events: 1 Open · 2 Document · 3 Diagnose · 4 Order · 5 Review orders · 6 Summary · 7 Educate · 8 Refer & follow up · 9 Complete |
| Build / feedback brief | Click through |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | calm, practical |
| Target seconds | 30 |
| Word count / estimated seconds | 67 words / ≈ 28.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The nine steps at a glance. Track the order carefully, then picture how you would move through the same sequence at work. The next action should follow from the step before it. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "timeline",
  "id": "ehr-002",
  "title": "Workflow map",
  "section": "The workflow",
  "node_id": "ehr-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-002",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-002`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-010` — The consultation

**Status:** `Draft — ready for SME review` · **Section / node:** Open & document / `ehr-sB` · **Type:** `simulation` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open the consultation |
| Objective(s) | `ehr-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 00:00–00:30 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The consultation |
| Body / keywords | Step 1: today's consultation list → click the test patient. Step 2: open the consultation form |
| Word count (excl. title) | 15 |
| Instruction | Hints name the panel |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for open the consultation. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: today's consultation list → click the test patient. Step 2: open the consultation form |
| Build / feedback brief | Hints name the panel |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Hints name the panel |
| Feedback — incorrect | Retry/incorrect feedback route: Hints name the panel |
| Per-choice feedback (scenarios) | Hints name the panel |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 24 words / ≈ 10.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Focus on the action that fits.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-010",
  "title": "The consultation",
  "section": "Open & document",
  "node_id": "ehr-sB",
  "objective_ids": [
    "ehr-o1"
  ],
  "points": 5,
  "narration_script_id": "ehr-010",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-010`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-011` — Mandatory fields

**Status:** `Draft — ready for SME review` · **Section / node:** Open & document / `ehr-sB` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Mandatory fields |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 00:30 |
| Depends on Phase 0 | ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Mandatory fields |
| Body / keywords | Consultation form screenshot; regions = each mandatory section (B4): chief complaint · duration · HPI · past history (allergies, medications) · examination · plan of care |
| Word count (excl. title) | 20 |
| Instruction | Each region: what to write, "save as you go" |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for mandatory fields, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. |
| edumints layout | n/a (interaction screen) |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Consultation form screenshot; regions = each mandatory section (B4): chief complaint · duration · HPI · past history (allergies, medications) · examination · plan of care |
| Build / feedback brief | Each region: what to write, "save as you go" |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | calm, practical |
| Target seconds | 25 |
| Word count / estimated seconds | 61 words / ≈ 26.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The mandatory sections. Save as you go. Let each marker add context rather than rushing to a conclusion. The full picture matters before a workplace decision is made. Carry the idea into your next decision. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "hotspot",
  "id": "ehr-011",
  "title": "Mandatory fields",
  "section": "Open & document",
  "node_id": "ehr-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-011",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-011`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-012` — Why it won't complete

**Status:** `Draft — ready for SME review` · **Section / node:** Open & document / `ehr-sB` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Why it won't complete |
| Objective(s) | `ehr-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 07:30 banner |
| Depends on Phase 0 | ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why it won't complete |
| Body / keywords | "You press Complete and the system refuses. The form shows chief complaint, HPI and examination filled in." Most likely cause → plan of care (or another mandatory field per B4) is empty |
| Word count (excl. title) | 31 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Dark teal #006E78 progress cue for why it won't complete. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "You press Complete and the system refuses. The form shows chief complaint, HPI and examination filled in." Most likely cause → plan of care (or another mandatory field per B4) is empty |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "ehr-012",
  "title": "Why it won't complete",
  "section": "Open & document",
  "node_id": "ehr-sB",
  "objective_ids": [
    "ehr-o1"
  ],
  "points": 5,
  "narration_script_id": "ehr-012",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-012`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-020` — Add the primary diagnosis

**Status:** `Draft — ready for SME review` · **Section / node:** Diagnosis / `ehr-sC` · **Type:** `simulation` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Add the primary diagnosis |
| Objective(s) | `ehr-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 01:00–02:00 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Add the primary diagnosis |
| Body / keywords | Step 1: click Add Diagnosis. Step 2: type E11 (accepted: E11, e11, type 2 diabetes). Step 3: choose Type 2 diabetes mellitus from results. Step 4: mark as primary / problem; onset, chronicity. Step 5: click the star to add … |
| Word count (excl. title) | 39 |
| Instruction | Feedback: "Specific primary diagnosis = fewer rejections (module 05)." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for add the primary diagnosis. Omar is placed l5 avatar above the simulation. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-neutral + tip card · placement L5 avatar above the simulation · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-avatar-neutral + tip card at L5 avatar above the simulation.` | illustration | Approved program companion pose char-omar-avatar-neutral + tip card at L5 avatar above the simulation. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: click Add Diagnosis. Step 2: type E11 (accepted: E11, e11, type 2 diabetes). Step 3: choose Type 2 diabetes mellitus from results. Step 4: mark as primary / problem; onset, chronicity. Step 5: click the star to add to favourites |
| Build / feedback brief | Feedback: "Specific primary diagnosis = fewer rejections (module 05)." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | E11, e11, type 2 diabetes |
| Points | 10 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Feedback: "Specific primary diagnosis = fewer rejections (module 05)." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "Specific primary diagnosis = fewer rejections (module 05)." |
| Per-choice feedback (scenarios) | Feedback: "Specific primary diagnosis = fewer rejections (module 05)." |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 20 |
| Word count / estimated seconds | 48 words / ≈ 20.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Feedback explains the reasoning after you respond. Use the rule you practised. Focus on the action that fits. Feedback explains the reasoning after you respond. Use the rule you practised.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-020",
  "title": "Add the primary diagnosis",
  "section": "Diagnosis",
  "node_id": "ehr-sC",
  "objective_ids": [
    "ehr-o2"
  ],
  "points": 10,
  "narration_script_id": "ehr-020",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-020`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-030` — How to find an order

**Status:** `Draft — ready for SME review` · **Section / node:** Orders / `ehr-sD` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | How to find an order |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 02:30–03:00 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | How to find an order |
| Body / keywords | Search by service · lab · referral · package · order profile · Form Wizard reviews a package before you finalise |
| Word count (excl. title) | 16 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for how to find an order, using a navy header, concise keyword cards and one Dark teal #006E78 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Search by service · lab · referral · package · order profile · Form Wizard reviews a package before you finalise |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | calm, practical |
| Target seconds | 25 |
| Word count / estimated seconds | 59 words / ≈ 25.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Five ways to find an order. The Form Wizard checks a package before you commit. As you read, focus on the decision this information supports in your own role. The aim is a practical next action, not a phrase to memorise. Pause and connect this to your role. Use the principle in context. Keep the next action clear.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "ehr-030",
  "title": "How to find an order",
  "section": "Orders",
  "node_id": "ehr-sD",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-030",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-030`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-031` — Medication order

**Status:** `Draft — ready for SME review` · **Section / node:** Orders / `ehr-sD` · **Type:** `simulation` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Medication order |
| Objective(s) | `ehr-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 03:30–04:30 |
| Depends on Phase 0 | ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Medication order |
| Body / keywords | Step 1: open order search. Step 2: type the drug name (B6 example). Step 3: set route, dose, frequency, duration. Step 4: choose the assessed diagnosis (E11). Step 5: add instructions to the patient. Step 6: press Order |
| Word count (excl. title) | 38 |
| Instruction | Feedback: "The order isn't placed until you press Order." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for medication order. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: open order search. Step 2: type the drug name (B6 example). Step 3: set route, dose, frequency, duration. Step 4: choose the assessed diagnosis (E11). Step 5: add instructions to the patient. Step 6: press Order |
| Build / feedback brief | Feedback: "The order isn't placed until you press Order." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Feedback: "The order isn't placed until you press Order." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "The order isn't placed until you press Order." |
| Per-choice feedback (scenarios) | Feedback: "The order isn't placed until you press Order." |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 36 words / ≈ 15.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Focus on the action that fits. Feedback explains the reasoning after you respond. Use the rule you practised.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-031",
  "title": "Medication order",
  "section": "Orders",
  "node_id": "ehr-sD",
  "objective_ids": [
    "ehr-o3"
  ],
  "points": 15,
  "narration_script_id": "ehr-031",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-031`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-032` — Lab package via Form Wizard

**Status:** `Draft — ready for SME review` · **Section / node:** Orders / `ehr-sD` · **Type:** `simulation` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Lab package via Form Wizard |
| Objective(s) | `ehr-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 03:00 |
| Depends on Phase 0 | ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Lab package via Form Wizard |
| Body / keywords | Step 1: search the package (B6). Step 2: Form Wizard step 1 — review items. Step 3: remove an item not needed. Step 4: finalise |
| Word count (excl. title) | 24 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for lab package via form wizard. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: search the package (B6). Step 2: Form Wizard step 1 — review items. Step 3: remove an item not needed. Step 4: finalise |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — informational screen. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 25 words / ≈ 10.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Feedback explains the reasoning after you respond.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-032",
  "title": "Lab package via Form Wizard",
  "section": "Orders",
  "node_id": "ehr-sD",
  "objective_ids": [
    "ehr-o3"
  ],
  "points": 10,
  "narration_script_id": "ehr-032",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-032`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-033` — Non-formulary

**Status:** `Draft — ready for SME review` · **Section / node:** Orders / `ehr-sD` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Non-formulary |
| Objective(s) | `ehr-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 1:40–4:50 |
| Depends on Phase 0 | ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Non-formulary |
| Body / keywords | "You order ⚠ PENDING non-formulary item, B6. The system flags it. What does that mean?" → it needs approval before it can be dispensed; consider a formulary alternative |
| Word count (excl. title) | 26 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Dark teal #006E78 progress cue for non-formulary. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "You order ⚠ PENDING non-formulary item, B6. The system flags it. What does that mean?" → it needs approval before it can be dispensed; consider a formulary alternative |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "ehr-033",
  "title": "Non-formulary",
  "section": "Orders",
  "node_id": "ehr-sD",
  "objective_ids": [
    "ehr-o3"
  ],
  "points": 5,
  "narration_script_id": "ehr-033",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-033`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-034` — Why link to a diagnosis

**Status:** `Draft — ready for SME review` · **Section / node:** Orders / `ehr-sD` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Why link to a diagnosis |
| Objective(s) | `ehr-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 03:30 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why link to a diagnosis |
| Body / keywords | "Why must each order be linked to the assessed diagnosis?" → it shows medical necessity to the reviewer and keeps the record consistent; unlinked orders are a common rejection cause |
| Word count (excl. title) | 29 |
| Instruction | Link to module 05 |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Dark teal #006E78 progress cue for why link to a diagnosis. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "Why must each order be linked to the assessed diagnosis?" → it shows medical necessity to the reviewer and keeps the record consistent; unlinked orders are a common rejection cause |
| Build / feedback brief | Link to module 05 |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Link to module 05 |
| Feedback — incorrect | Retry/incorrect feedback route: Link to module 05 |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "ehr-034",
  "title": "Why link to a diagnosis",
  "section": "Orders",
  "node_id": "ehr-sD",
  "objective_ids": [
    "ehr-o3"
  ],
  "points": 5,
  "narration_script_id": "ehr-034",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-034`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-040` — Consultation summary

**Status:** `Draft — ready for SME review` · **Section / node:** Summary & education / `ehr-sE` · **Type:** `simulation` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Consultation summary |
| Objective(s) | `ehr-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 06:20–07:00 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Consultation summary |
| Body / keywords | Step 1: open Consultation Summary. Step 2: check lab orders, special tests, referrals. Step 3: Download and Print |
| Word count (excl. title) | 18 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for consultation summary. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: open Consultation Summary. Step 2: check lab orders, special tests, referrals. Step 3: Download and Print |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — informational screen. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 24 words / ≈ 10.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Focus on the action that fits.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-040",
  "title": "Consultation summary",
  "section": "Summary & education",
  "node_id": "ehr-sE",
  "objective_ids": [
    "ehr-o4"
  ],
  "points": 5,
  "narration_script_id": "ehr-040",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-040`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-041` — SMS education

**Status:** `Draft — ready for SME review` · **Section / node:** Summary & education / `ehr-sE` · **Type:** `simulation` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | SMS education |
| Objective(s) | `ehr-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 07:00 |
| Depends on Phase 0 | ⚠ PENDING B8; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | SMS education |
| Body / keywords | Step 1: open Send SMS – educational material. Step 2: choose department. Step 3: type E11. Step 4: select the leaflet. Step 5: Send (B8) |
| Word count (excl. title) | 24 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for sms education. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: open Send SMS – educational material. Step 2: choose department. Step 3: type E11. Step 4: select the leaflet. Step 5: Send (B8) |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — informational screen. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 12 |
| Word count / estimated seconds | 30 words / ≈ 12.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Feedback explains the reasoning after you respond. Use the rule you practised.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-041",
  "title": "SMS education",
  "section": "Summary & education",
  "node_id": "ehr-sE",
  "objective_ids": [
    "ehr-o4"
  ],
  "points": 10,
  "narration_script_id": "ehr-041",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B8; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-041`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-042` — Patient & family education

**Status:** `Draft — ready for SME review` · **Section / node:** Summary & education / `ehr-sE` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Patient & family education |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 07:30 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Patient & family education |
| Body / keywords | Checklist: infection control · medication use · disease/condition · treatment · health & lifestyle · other · "Required before finalising" |
| Word count (excl. title) | 14 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for patient & family education, using a navy header, concise keyword cards and one Dark teal #006E78 highlight. Noor is placed l3 tip card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-avatar-neutral + tip card · placement L3 tip card · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card.` | illustration | Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Checklist: infection control · medication use · disease/condition · treatment · health & lifestyle · other · "Required before finalising" |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | calm, practical |
| Target seconds | 20 |
| Word count / estimated seconds | 47 words / ≈ 20.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Patient & family education is required before you finish. As you read, focus on the decision this information supports in your own role. The aim is a practical next action, not a phrase to memorise. Pause and connect this to your role. Use the principle in context.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "ehr-042",
  "title": "Patient & family education",
  "section": "Summary & education",
  "node_id": "ehr-sE",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-042",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-042`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-050` — Internal referral + follow-up

**Status:** `Draft — ready for SME review` · **Section / node:** Referral & finish / `ehr-sF` · **Type:** `simulation` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Internal referral + follow-up |
| Objective(s) | `ehr-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 07:40–08:20 |
| Depends on Phase 0 | ⚠ PENDING B9; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Internal referral + follow-up |
| Body / keywords | Step 1: open referral. Step 2: specialty = Endocrinology. Step 3: type the reason (approved example phrase, e.g. "poorly controlled type 2 diabetes"; variants listed in input_accepted). Step 4: type = Internal; timing = within a month (B9). Step 5 … |
| Word count (excl. title) | 39 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Dark teal #006E78 progress cue for internal referral + follow-up. Omar is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-neutral · placement L5 avatar · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-avatar-neutral at L5 avatar.` | illustration | Approved program companion pose char-omar-avatar-neutral at L5 avatar. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Step 1: open referral. Step 2: specialty = Endocrinology. Step 3: type the reason (approved example phrase, e.g. "poorly controlled type 2 diabetes"; variants listed in input_accepted). Step 4: type = Internal; timing = within a month (B9). Step 5: follow-up toggle + interval. Step 6: Save |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — informational screen. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 36 words / ≈ 15.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Feedback explains the reasoning after you respond. Use the rule you practised. Focus on the action that fits.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "ehr-050",
  "title": "Internal referral + follow-up",
  "section": "Referral & finish",
  "node_id": "ehr-sF",
  "objective_ids": [
    "ehr-o4"
  ],
  "points": 10,
  "narration_script_id": "ehr-050",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B9; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-050`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-051` — The whole workflow

**Status:** `Draft — ready for SME review` · **Section / node:** Referral & finish / `ehr-sF` · **Type:** `sorting` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | The whole workflow |
| Objective(s) | `ehr-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | process map |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The whole workflow |
| Body / keywords | 9 steps from ehr-002 in order |
| Word count (excl. title) | 6 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Dark teal #006E78 progress cue for the whole workflow. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 9 steps from ehr-002 in order |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Confirm the source-mapped response and explain why it supports the stated on-the-job action. |
| Feedback — incorrect | Explain which source-mapped detail to reconsider, then allow a retry; do not reveal the answer in narration. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "sorting",
  "id": "ehr-051",
  "title": "The whole workflow",
  "section": "Referral & finish",
  "node_id": "ehr-sF",
  "objective_ids": [
    "ehr-o5"
  ],
  "points": 10,
  "narration_script_id": "ehr-051",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-051`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-052` — Complete the encounter

**Status:** `Draft — ready for SME review` · **Section / node:** Referral & finish / `ehr-sF` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Complete the encounter |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 08:20 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Complete the encounter |
| Body / keywords | "Record saved successfully" → Complete · What happens if a field is missing · Where to get help (IT service desk) |
| Word count (excl. title) | 18 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for complete the encounter, using a navy header, concise keyword cards and one Dark teal #006E78 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "Record saved successfully" → Complete · What happens if a field is missing · Where to get help (IT service desk) |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | calm, practical |
| Target seconds | 20 |
| Word count / estimated seconds | 44 words / ≈ 18.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Completing the encounter. Where to get help. Keep the main point connected to a familiar task or conversation. That connection makes the information easier to use when it matters. Apply the point to a familiar task. Carry the idea into your next decision.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "ehr-052",
  "title": "Complete the encounter",
  "section": "Referral & finish",
  "node_id": "ehr-sF",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-052",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-052`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-090` — Results

**Status:** `Draft — ready for SME review` · **Section / node:** Referral & finish / `ehr-sF` · **Type:** `results_breakdown` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Results |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Results |
| Body / keywords | ehr-o1…o5 |
| Word count (excl. title) | 2 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm results panel showing each objective as an HTML progress row, with plain-language next steps and a small companion feedback card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | ehr-o1…o5 |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | supportive |
| Target seconds | 10 |
| Word count / estimated seconds | 21 words / ≈ 9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Your results are organised by objective. Notice where you were confident, then revisit any section that needs another practical try.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "results_breakdown",
  "id": "ehr-090",
  "title": "Results",
  "section": "Referral & finish",
  "node_id": "ehr-sF",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-090",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-090`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ehr-091` — Close

**Status:** `Draft — ready for SME review` · **Section / node:** Referral & finish / `ehr-sF` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Close |
| Body / keywords | Complete, specific, linked · Links: EHR quick-reference card (PDF), IT service desk |
| Word count (excl. title) | 11 |
| Instruction | show_score |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A confident light closing screen with four short takeaways, the supplied My Clinic logo, and space for the next-module hand-off. Omar is placed l6 right. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Dark teal #006E78 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-success · placement L6 right · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ehr-pdf-quickref` | illustration | ehr-pdf-quickref: 1-page EHR consultation quick-reference card | own SVG | Close visual. | No |
| `Approved program companion pose char-omar-success at L6 right.` | illustration | Approved program companion pose char-omar-success at L6 right. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Complete, specific, linked · Links: EHR quick-reference card (PDF), IT service desk |
| Build / feedback brief | show_score |
| Correct answer(s) / completion rule | n/a — no scored response on this screen. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 0 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | n/a — informational/exploratory screen. |
| Feedback — incorrect | n/a — informational/exploratory screen. |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | confident |
| Target seconds | 15 |
| Word count / estimated seconds | 36 words / ≈ 15.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you.

New lexicon terms: See `narration-script.json` and `voice_talent.md`.

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native focusable controls; matching, sorting and drag/drop use keyboard pick-and-place equivalents. |
| Not colour-only | Labels, icons, position and explanatory text carry every safety, feedback and category meaning. |
| Captions / transcript | `narration_text` is generated from the narration script; any later video receives WebVTT captions. |
| Timing | Untimed. Any future media control must allow pause, replay and extended reading time. |

#### 7. Build fields (edumints)

```json
{
  "type": "summary",
  "id": "ehr-091",
  "title": "Close",
  "section": "Referral & finish",
  "node_id": "ehr-sF",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ehr-091",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ehr-091`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---


## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `ehr-000` | `title_slide` | N | 0 | 9 | 28 | 12 | Draft |
| 2 | `ehr-001` | `content_slide` | N | 0 | 13 | 57 | 24 | Draft |
| 3 | `ehr-002` | `timeline` | N | 0 | 25 | 67 | 29 | Draft |
| 4 | `ehr-010` | `simulation` | Y | 5 | 15 | 24 | 10 | Draft |
| 5 | `ehr-011` | `hotspot` | N | 0 | 20 | 61 | 26 | Draft |
| 6 | `ehr-012` | `mcq` | Y | 5 | 31 | 18 | 8 | Draft |
| 7 | `ehr-020` | `simulation` | Y | 10 | 39 | 48 | 21 | Draft |
| 8 | `ehr-030` | `content_slide` | N | 0 | 16 | 59 | 25 | Draft |
| 9 | `ehr-031` | `simulation` | Y | 15 | 38 | 36 | 15 | Draft |
| 10 | `ehr-032` | `simulation` | Y | 10 | 24 | 25 | 11 | Draft |
| 11 | `ehr-033` | `mcq` | Y | 5 | 26 | 18 | 8 | Draft |
| 12 | `ehr-034` | `mcq` | Y | 5 | 29 | 18 | 8 | Draft |
| 13 | `ehr-040` | `simulation` | Y | 5 | 18 | 24 | 10 | Draft |
| 14 | `ehr-041` | `simulation` | Y | 10 | 24 | 30 | 13 | Draft |
| 15 | `ehr-042` | `content_slide` | N | 0 | 14 | 47 | 20 | Draft |
| 16 | `ehr-050` | `simulation` | Y | 10 | 39 | 36 | 15 | Draft |
| 17 | `ehr-051` | `sorting` | Y | 10 | 6 | 18 | 8 | Draft |
| 18 | `ehr-052` | `content_slide` | N | 0 | 18 | 44 | 19 | Draft |
| 19 | `ehr-090` | `results_breakdown` | N | 0 | 2 | 21 | 9 | Draft |
| 20 | `ehr-091` | `summary` | N | 0 | 11 | 36 | 15 | Draft |
| | **Totals** | | **11** | **90** | | **715** | **306 ≈ 5.1 min** | Draft |

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `ehr-capture-sheet` | diagram | Generated file | own | Yes | Generated capture checklist only; not an EHR screenshot and not a substitute for B2 test-environment assets. |
| `ehr-pdf-quickref` | PDF | ehr-091 | own | n/a | Planned |
| `ehr-vid-walkthrough (optional)` | MP4 + VTT | ehr-060 | own | Yes | Planned |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
| 1 | All affected cards | Patient identifiers in IT.mp4 (5:10–6:10 full record; 7:10–7:20 phone; 8:30 ID) | `B1` · IT + DPO | Yes |
| 2 | All affected cards | Test environment + test patient ("Test Simplified Template Launch" or new) for all new screenshots | `B2` · EHR lead | Yes |
| 3 | All affected cards | EHR product name and version | `B3` · EHR lead | Yes |
| 4 | All affected cards | Mandatory fields before completing a consultation | `B4` · EHR lead | Yes |
| 5 | All affected cards | Button and screen names (Today's consultation, Add Diagnosis, Order History, Form Wizard, Consultation Summary, Download and Print, Send SMS, Referral) | `B5` · EHR lead | Yes |
| 6 | All affected cards | Medication and lab examples (lornoxicam, diclofenac, Fevadol non-formulary, Augmentin; CBC, TSH, ECG; vitamin D, "hair package") | `B6` · Pharmacy + Medical Director | Yes |
| 7 | All affected cards | Clinical disclaimer | `B7` · Medical Director | Yes |
| 8 | All affected cards | SMS education: department list and ICD-10 linked leaflets | `B8` · EHR lead | Yes |
| 9 | All affected cards | Referral timing options (next available, within a week, two weeks, a month) and internal vs external | `B9` · EHR lead | Yes |
| 10 | All affected cards | Sick-leave panel (printing disabled) | `B10` · EHR lead | Yes |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| `EHR` | E-H-R | `ehr-000` |

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan (11 scored / 90 points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
