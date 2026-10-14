# Storyboard — 04 Who Does What: Operations & My Care

![My Clinic logo](../../00_program/brand/logo-preview.png)

> **Review pack v0.2 · 2026-10-14.** This document completes the screen-card, narration, visual-plan,
> asset-register and visual-review documentation for every core screen in
> [`../phase-2-storyboard.md`](../phase-2-storyboard.md). It is a review artefact, **not an approved
> policy or production SCORM package**. Source-lock decisions are deliberately retained as `⚠ PENDING`.

**Companion documents:** [`screen-visuals.html`](screen-visuals.html) ·
[`visual-plan.json`](visual-plan.json) · [`narration-script.json`](narration-script.json) ·
[`voice_talent.md`](voice_talent.md) · [`asset-register.md`](asset-register.md) · [`lint-report.json`](lint-report.json) ·
[`programme SME/build-detail register`](../../00_program/storyboard-review-register.md).

---

## A. Module header

| Field | Value |
|---|---|
| Module | 04 — My Clinic — Who Does What: Operations & My Care |
| Module prefix | `ops-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | Director of Operations (lead); My Care Manager; Patient Experience senior manager |
| Audience | Front-line, PX and clinical staff |
| Seat-time budget | ~15 minutes |
| SCORM / completion / pass mark | SCORM 1.2 · viewed_all_and_passed · pass 70% (35 / 50) |
| Scored screens / total points | 4 / 50 (Phase 4 expectation: 4 / 50) |
| Source file | `elearning-course/md/04_operations-and-my-care-structure.md` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-14) |
| Module colour | Responsible magenta #9D3293 |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | B1–B7; program D3, D5 and D11 |
| Narration reconciliation | Detailed card scripts: 4.4 min; Phase 3 per-screen targets: 4.4 min; Phase 3 rough module estimate: ~5 min. Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review. |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
| `ops-o1` | Distinguish the activities owned by Operations from those owned by My Care. | `ops-030` |
| `ops-o2` | Route common patient requests to the right team and role. | `ops-031`, `ops-032` |
| `ops-o3` | Explain the main roles and abbreviations in each structure. | `ops-033` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `ops-s1` | The patient journey | `ops-000`–`ops-002` |
| `ops-s2` | Operations | `ops-010`–`ops-011` |
| `ops-s3` | My Care | `ops-020`–`ops-022` |
| `ops-s4` | Practice: right team, first time | `ops-030`–`ops-090` |

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

### `ops-000` — Who Does What: Operations & My Care

**Status:** `Draft — ready for SME review` · **Section / node:** The patient journey / `ops-s1` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 1, 4 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Who Does What: Operations & My Care |
| Body / keywords | "Who Does What" · "Operations & My Care" |
| Word count (excl. title) | 6 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L1 Title |
| Logo | `logo-horizontal-white.png`, 48 px at top-left |
| Visual concept | Official navy title gradient with supplied white My Clinic logo, large Montserrat course title, and a cropped white petal watermark. Omar is placed l1 half-body bottom-right. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `primary` · text `on_primary` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
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
| `Approved program companion pose char-omar-welcome at L1 half-body bottom-right.` | illustration | Approved program companion pose char-omar-welcome at L1 half-body bottom-right. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "Who Does What" · "Operations & My Care" |
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
| Word count / estimated seconds | 29 words / ≈ 12.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Welcome to Who Does What: Operations & My Care. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift.

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
  "id": "ops-000",
  "title": "Who Does What: Operations & My Care",
  "section": "The patient journey",
  "node_id": "ops-s1",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-000",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-000`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-001` — Why it matters

**Status:** `Draft — ready for SME review` · **Section / node:** The patient journey / `ops-s1` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Why it matters |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why it matters |
| Body / keywords | "Right team, first time." · A patient shouldn't have to tell their story twice. |
| Word count (excl. title) | 13 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for why it matters, using a navy header, concise keyword cards and one Responsible magenta #9D3293 highlight. Omar is placed l3 right column. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-explaining · placement L3 right column · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-explaining at L3 right column.` | illustration | Approved program companion pose char-omar-explaining at L3 right column. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "Right team, first time." · A patient shouldn't have to tell their story twice. |
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
| Word count / estimated seconds | 58 words / ≈ 24.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Routing matters. A patient who repeats their story loses trust. I once sent the same patient to three desks in one morning. She never forgot it — and neither did I. Keep the main point connected to a familiar task or conversation. That connection makes the information easier to use when it matters. Use the principle in context.

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
  "id": "ops-001",
  "title": "Why it matters",
  "section": "The patient journey",
  "node_id": "ops-s1",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-001",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-001`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-002` — Patient journey

**Status:** `Draft — ready for SME review` · **Section / node:** The patient journey / `ops-s1` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Patient journey |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 2, 5 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Patient journey |
| Body / keywords | Horizontal journey: Book → Arrive & register → Consult → Lab / Radiology / Pharmacy → Leave → Follow-up. Each stage shows which team leads (Operations, My Care or both) |
| Word count (excl. title) | 22 |
| Instruction | Open all 6 stages |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for patient journey, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. |
| edumints layout | n/a (interaction screen) |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ops-img-journey` | diagram | ops-img-journey: Generated native SVG. | own SVG | Patient journey from booking to follow-up. | No |
| `ops-img-journey` | diagram | ops-img-journey: 6-stage horizontal journey, icons, team colour tags + text labels | own SVG | "Patient journey from booking to follow-up." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Horizontal journey: Book → Arrive & register → Consult → Lab / Radiology / Pharmacy → Leave → Follow-up. Each stage shows which team leads (Operations, My Care or both) |
| Build / feedback brief | Open all 6 stages |
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
| Word count / estimated seconds | 50 words / ≈ 21.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Walk the journey. Notice where each team leads. Let each marker add context rather than rushing to a conclusion. The full picture matters before a workplace decision is made. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task.

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
  "id": "ops-002",
  "title": "Patient journey",
  "section": "The patient journey",
  "node_id": "ops-s1",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-002",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-002`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-010` — Operations activities

**Status:** `Draft — ready for SME review` · **Section / node:** Operations / `ops-s2` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Operations activities |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 2 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Operations activities |
| Body / keywords | 7 items from slide 2, each with one example ("Recovery: a patient waited 40 minutes; the PX officer apologises and fixes the next visit") |
| Word count (excl. title) | 24 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for operations activities, with one open item at a time, navy structure, and a Responsible magenta #9D3293 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ops-img-activities` | diagram | ops-img-activities: Line icons; slide 2/5 "sticky note" style not copied | own SVG | decorative | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 7 items from slide 2, each with one example ("Recovery: a patient waited 40 minutes; the PX officer apologises and fixes the next visit") |
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
| Target seconds | 40 |
| Word count / estimated seconds | 91 words / ≈ 39 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Operations runs the day: environment, KPIs, recovery on the spot. Use each section to build the picture step by step. Before moving on, identify the action or check that belongs to your role. Ask early when a situation does not match the rule. Good habits here are quiet: check, confirm, continue. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision.

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
  "type": "accordion",
  "id": "ops-010",
  "title": "Operations activities",
  "section": "Operations",
  "node_id": "ops-s2",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-010",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-010`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-011` — Operations structure

**Status:** `Draft — ready for SME review` · **Section / node:** Operations / `ops-s2` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Operations structure |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 3 |
| Depends on Phase 0 | ⚠ PENDING B1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Operations structure |
| Body / keywords | Redrawn role-only chart (B1): Director of Operations → PX & Operations Sr. Manager · Patient Access & PX Sr. Manager · Operations Sr. Manager → PX Managers → PXOs/FMs at sites J1–J4, PR1, VIP team, Check-Up Unit, In-Patient |
| Word count (excl. title) | 33 |
| Instruction | Labels with one-line role description |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for operations structure, using a navy header, concise keyword cards and one Responsible magenta #9D3293 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ops-img-ops-chart` | diagram | ops-img-ops-chart: Generated role-only draft SVG; SME approval B1 required. | own SVG | Draft Operations role structure. | No |
| `ops-img-ops-chart` | diagram | ops-img-ops-chart: Role-only Operations chart (from B1) | own SVG | "Operations structure by role." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Redrawn role-only chart (B1): Director of Operations → PX & Operations Sr. Manager · Patient Access & PX Sr. Manager · Operations Sr. Manager → PX Managers → PXOs/FMs at sites J1–J4, PR1, VIP team, Check-Up Unit, In-Patient |
| Build / feedback brief | Labels with one-line role description |
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
| Word count / estimated seconds | 73 words / ≈ 31.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Read the chart by roles. Names are in the directory because they change. Read each label as a prompt for what to check or who should act next. The useful step is linking the visual with a real decision. Good habits here are quiet: check, confirm, continue. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check.

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
  "type": "labeled_diagram",
  "id": "ops-011",
  "title": "Operations structure",
  "section": "Operations",
  "node_id": "ops-s2",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-011",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-011`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-020` — My Care activities

**Status:** `Draft — ready for SME review` · **Section / node:** My Care / `ops-s3` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | My Care activities |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 5 |
| Depends on Phase 0 | ⚠ PENDING B3; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | My Care activities |
| Body / keywords | 7 items from slide 5, with DMP/CHP expanded (B3) |
| Word count (excl. title) | 10 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for my care activities, with one open item at a time, navy structure, and a Responsible magenta #9D3293 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ops-img-activities` | diagram | ops-img-activities: Line icons; slide 2/5 "sticky note" style not copied | own SVG | decorative | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 7 items from slide 5, with DMP/CHP expanded (B3) |
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
| Target seconds | 40 |
| Word count / estimated seconds | 90 words / ≈ 38.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: My Care is the relationship after the visit: follow-ups, programmes, referrals. Read the sections in sequence, then compare the points that matter most in practice. Keep the next action clearer than the terminology. Link it to the task waiting for you tomorrow. If one detail stays with you, let it be the safe one. Ask early when a situation does not match the rule. Good habits here are quiet: check, confirm, continue. Pause and connect this to your role. Use the principle in context. Keep the next action clear.

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
  "type": "accordion",
  "id": "ops-020",
  "title": "My Care activities",
  "section": "My Care",
  "node_id": "ops-s3",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-020",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B3; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-020`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-021` — My Care structure

**Status:** `Draft — ready for SME review` · **Section / node:** My Care / `ops-s3` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | My Care structure |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 6 |
| Depends on Phase 0 | ⚠ PENDING B2; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | My Care structure |
| Body / keywords | Redrawn role-only chart (B2): Director of Operations → Patient Access & PX Sr. Manager → My Care Manager → Onboarding leaders, site leaders (J1; J2–J4) → Coordinators; QA leader |
| Word count (excl. title) | 25 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for my care structure, using a navy header, concise keyword cards and one Responsible magenta #9D3293 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ops-img-mycare-chart` | diagram | ops-img-mycare-chart: Generated role-only draft SVG; SME approval B2 required. | own SVG | Draft My Care role structure. | No |
| `ops-img-mycare-chart` | diagram | ops-img-mycare-chart: Role-only My Care chart (from B2) | own SVG | "My Care structure by role." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Redrawn role-only chart (B2): Director of Operations → Patient Access & PX Sr. Manager → My Care Manager → Onboarding leaders, site leaders (J1; J2–J4) → Coordinators; QA leader |
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

> OMAR: My Care structure: managers, site leaders, coordinators, quality. Use the labels to connect each part of the visual with the responsibility or action it supports. The diagram is a working reference, not a test to memorise. If one detail stays with you, let it be the safe one. Ask early when a situation does not match the rule.

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
  "type": "labeled_diagram",
  "id": "ops-021",
  "title": "My Care structure",
  "section": "My Care",
  "node_id": "ops-s3",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-021",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B2; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-021`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-022` — Abbreviations

**Status:** `Draft — ready for SME review` · **Section / node:** My Care / `ops-s3` · **Type:** `flashcards` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Abbreviations |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 3, 5 |
| Depends on Phase 0 | ⚠ PENDING B3; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Abbreviations |
| Body / keywords | PXO · FM · Coord · DMP · CHP · HHC · PR1 · VIP team (B3) |
| Word count (excl. title) | 10 |
| Instruction | Flip |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for abbreviations, with one open item at a time, navy structure, and a Responsible magenta #9D3293 active-state cue. Noor is placed l3 tip card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
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
| Items / options / nodes | PXO · FM · Coord · DMP · CHP · HHC · PR1 · VIP team (B3) |
| Build / feedback brief | Flip |
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
| Target seconds | 15 |
| Word count / estimated seconds | 35 words / ≈ 15 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The abbreviations you'll hear on day one. Take the cards one at a time and test whether you can explain the point in your own words. That makes the information easier to use later.

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
  "type": "flashcards",
  "id": "ops-022",
  "title": "Abbreviations",
  "section": "My Care",
  "node_id": "ops-s3",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-022",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B3; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-022`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-030` — Sort the work

**Status:** `Draft — ready for SME review` · **Section / node:** Practice: right team, first time / `ops-s4` · **Type:** `drag_drop` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Sort the work |
| Objective(s) | `ops-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 2, 5 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Sort the work |
| Body / keywords | 10 cards → Operations / My Care: lab TAT KPI · clinic look and feel · on-spot complaint at reception · end-to-end journey · support a doctor's inquiry · monthly follow-up call · insurance medication follow-up · hypertension programme booking … |
| Word count (excl. title) | 32 |
| Instruction | Feedback on each card; overlap items explained |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Responsible magenta #9D3293 progress cue for sort the work. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
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
| Items / options / nodes | 10 cards → Operations / My Care: lab TAT KPI · clinic look and feel · on-spot complaint at reception · end-to-end journey · support a doctor's inquiry · monthly follow-up call · insurance medication follow-up · hypertension programme booking · telemedicine coordination · internal referral priority |
| Build / feedback brief | Feedback on each card; overlap items explained |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback on each card; overlap items explained |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback on each card; overlap items explained |
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
  "type": "drag_drop",
  "id": "ops-030",
  "title": "Sort the work",
  "section": "Practice: right team, first time",
  "node_id": "ops-s4",
  "objective_ids": [
    "ops-o1"
  ],
  "points": 15,
  "narration_script_id": "ops-030",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-030`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-031` — Who do I call?

**Status:** `Draft — ready for SME review` · **Section / node:** Practice: right team, first time / `ops-s4` · **Type:** `decision_scenario` · **Scored:** Yes (20 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Who do I call? |
| Objective(s) | `ops-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 2, 5 |
| Depends on Phase 0 | ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Who do I call? |
| Body / keywords | 4 nodes (routing per B7): (1) A patient at reception is upset that her lab result isn't ready → Operations / PX officer on site; (2) A diabetic patient asks who will remind him about his 3-month review → My … |
| Word count (excl. title) | 37 |
| Instruction | Each choice explains the owner and the role |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Responsible magenta #9D3293 progress cue for who do i call?. Omar is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-neutral → -happy / -concern · placement L5 avatar · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `ops-img-reception-scenario` | illustration | ops-img-reception-scenario: Generated 2026-10-14 — generic fictional scene; final routing remains subject to B7. | ai-generated, visual QA required | A patient talks to a patient-experience officer at a clinic reception desk. | No |
| `ops-img-scenes-1..4` | illustration | ops-img-scenes-1..4: Reception, phone follow-up, insurance call, pharmacy queue | ai-generated, visual QA required | per scene | No |
| `Approved program companion pose char-omar-avatar-neutral → -happy / -concern at L5 avatar.` | illustration | Approved program companion pose char-omar-avatar-neutral → -happy / -concern at L5 avatar. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

**AI image prompt (recorded production prompt)**

```text
Single clean flat vector illustration for a My Clinic e-learning course. A patient talks to a patient-experience officer at a clinic reception desk. Use navy #003867 outlines, white space, soft blue-grey #C0CED9, and Responsible magenta #9D3293 as the only value-colour highlight. No text, no letters, no numbers, no logos, no watermark, no patient/staff likeness, and no generated My Clinic mark.
```

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 4 nodes (routing per B7): (1) A patient at reception is upset that her lab result isn't ready → Operations / PX officer on site; (2) A diabetic patient asks who will remind him about his 3-month review → My Care; (3) A patient's insurer rejected his monthly medication → My Care insurance follow-up; (4) A doctor reports the pharmacy queue is causing delays every afternoon → Operations |
| Build / feedback brief | Each choice explains the owner and the role |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 20 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Each choice explains the owner and the role |
| Feedback — incorrect | Retry/incorrect feedback route: Each choice explains the owner and the role |
| Per-choice feedback (scenarios) | Each choice explains the owner and the role |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 31 words / ≈ 13.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Focus on the action that fits. Feedback explains the reasoning after you respond.

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
  "type": "decision_scenario",
  "id": "ops-031",
  "title": "Who do I call?",
  "section": "Practice: right team, first time",
  "node_id": "ops-s4",
  "objective_ids": [
    "ops-o2"
  ],
  "points": 20,
  "narration_script_id": "ops-031",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-031`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-032` — Escalation

**Status:** `Draft — ready for SME review` · **Section / node:** Practice: right team, first time / `ops-s4` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Escalation |
| Objective(s) | `ops-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 3 |
| Depends on Phase 0 | ⚠ PENDING B1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Escalation |
| Body / keywords | "The PX officer can't resolve a complaint on the spot. Who is the next step?" → site Patient Experience Manager (per B1) |
| Word count (excl. title) | 21 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Responsible magenta #9D3293 progress cue for escalation. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
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
| Items / options / nodes | "The PX officer can't resolve a complaint on the spot. Who is the next step?" → site Patient Experience Manager (per B1) |
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
  "id": "ops-032",
  "title": "Escalation",
  "section": "Practice: right team, first time",
  "node_id": "ops-s4",
  "objective_ids": [
    "ops-o2"
  ],
  "points": 5,
  "narration_script_id": "ops-032",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-032`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-033` — Roles

**Status:** `Draft — ready for SME review` · **Section / node:** Practice: right team, first time / `ops-s4` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Roles |
| Objective(s) | `ops-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 3, 6 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Roles |
| Body / keywords | PXO ↔ "patient experience on site" · My Care Coordinator ↔ "follow-ups and bookings" · My Care Onboarding Leader ↔ "enrols patients in My Care" · Operations Sr. Manager ↔ "daily operations" · QA Leader ↔ "quality of My Care … |
| Word count (excl. title) | 31 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Responsible magenta #9D3293 progress cue for roles. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
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
| Items / options / nodes | PXO ↔ "patient experience on site" · My Care Coordinator ↔ "follow-ups and bookings" · My Care Onboarding Leader ↔ "enrols patients in My Care" · Operations Sr. Manager ↔ "daily operations" · QA Leader ↔ "quality of My Care calls/service" |
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
  "type": "matching",
  "id": "ops-033",
  "title": "Roles",
  "section": "Practice: right team, first time",
  "node_id": "ops-s4",
  "objective_ids": [
    "ops-o3"
  ],
  "points": 10,
  "narration_script_id": "ops-033",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-033`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `ops-090` — Close

**Status:** `Draft — ready for SME review` · **Section / node:** Practice: right team, first time / `ops-s4` · **Type:** `summary` · **Scored:** No

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
| Body / keywords | Right team, first time · Link: live staff directory (intranet) · Next: module 05/06 (clinicians) or 08 (EHR) |
| Word count (excl. title) | 17 |
| Instruction | show_score |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A confident light closing screen with four short takeaways, the supplied My Clinic logo, and space for the next-module hand-off. Omar + Noor is placed l6. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Responsible magenta #9D3293 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar + Noor · pose char-omar-success + char-noor-avatar-happy · placement L6 · speaks: Omar + Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-success + char-noor-avatar-happy at L6.` | illustration | Approved program companion pose char-omar-success + char-noor-avatar-happy at L6. | own / official My Clinic asset | Omar + Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Right team, first time · Link: live staff directory (intranet) · Next: module 05/06 (clinicians) or 08 (EHR) |
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
| Speaker(s) | OMAR / NOOR |
| Tone | confident |
| Target seconds | 20 |
| Word count / estimated seconds | 45 words / ≈ 19.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you.
>
> NOOR: Carry this practical rule into your next decision.

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
  "id": "ops-090",
  "title": "Close",
  "section": "Practice: right team, first time",
  "node_id": "ops-s4",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "ops-090",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `ops-090`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---


## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `ops-000` | `title_slide` | N | 0 | 6 | 29 | 12 | Draft |
| 2 | `ops-001` | `content_slide` | N | 0 | 13 | 58 | 25 | Draft |
| 3 | `ops-002` | `hotspot` | N | 0 | 22 | 50 | 21 | Draft |
| 4 | `ops-010` | `accordion` | N | 0 | 24 | 91 | 39 | Draft |
| 5 | `ops-011` | `labeled_diagram` | N | 0 | 33 | 73 | 31 | Draft |
| 6 | `ops-020` | `accordion` | N | 0 | 10 | 90 | 39 | Draft |
| 7 | `ops-021` | `labeled_diagram` | N | 0 | 25 | 59 | 25 | Draft |
| 8 | `ops-022` | `flashcards` | N | 0 | 10 | 35 | 15 | Draft |
| 9 | `ops-030` | `drag_drop` | Y | 15 | 32 | 18 | 8 | Draft |
| 10 | `ops-031` | `decision_scenario` | Y | 20 | 37 | 31 | 13 | Draft |
| 11 | `ops-032` | `mcq` | Y | 5 | 21 | 18 | 8 | Draft |
| 12 | `ops-033` | `matching` | Y | 10 | 31 | 18 | 8 | Draft |
| 13 | `ops-090` | `summary` | N | 0 | 17 | 45 | 19 | Draft |
| | **Totals** | | **4** | **50** | | **615** | **264 ≈ 4.4 min** | Draft |

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `ops-img-reception-scenario` | illustration | Generated file | ai-generated | Yes | Generated 2026-10-14 — generic fictional scene; final routing remains subject to B7. |
| `ops-img-journey` | diagram | Generated file | own | Yes | Generated native SVG. |
| `ops-img-ops-chart` | diagram | Generated file | own | Yes | Generated role-only draft SVG; SME approval B1 required. |
| `ops-img-mycare-chart` | diagram | Generated file | own | Yes | Generated role-only draft SVG; SME approval B2 required. |
| `ops-img-journey` | SVG | ops-002 | own | Yes | Planned |
| `ops-img-ops-chart` | SVG | ops-011 | own | Yes | Planned |
| `ops-img-mycare-chart` | SVG | ops-021 | own | Yes | Planned |
| `ops-img-activities` | SVG icons ×14 | ops-010, ops-020 | own | Yes | Planned |
| `ops-img-scenes-1..4` | illustrations | ops-031 | ai-generated | Yes | Planned |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
| 1 | All affected cards | Reporting lines for the Operations chart | `B1` · Director of Operations | Yes |
| 2 | All affected cards | Reporting lines for the My Care chart | `B2` · My Care Manager | Yes |
| 3 | All affected cards | Abbreviations: FM, DMP, CHP, PR1, VIP team, Check Up Unit, In Patient | `B3` · Operations | Yes |
| 4 | All affected cards | Which headcount (PXOs/FMs/Coords) belongs to which unit | `B4` · Director of Operations | Yes |
| 5 | All affected cards | PR1 vs PRC; J1–J4 names | `B5` · HR + Operations | Yes |
| 6 | All affected cards | Names on screen | `B6` · HR + DPO | Yes |
| 7 | All affected cards | Escalation routes for the scenario (who handles on-spot complaints, insurance follow-ups, priority bookings, telemedicine coordination) | `B7` · PX Sr. Manager + My Care Manager | Yes |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| — | No module-specific pronunciation addition is used in the current draft. | — |

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan (4 scored / 50 points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
