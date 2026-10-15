# Storyboard — 01 Facility Management & Safety

![My Clinic logo](../../00_program/brand/logo-preview.png)

> **Review pack v0.2 · 2026-10-15.** This document completes the screen-card, narration, visual-plan,
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
| Module | 01 — My Clinic — Facility Management & Safety |
| Module prefix | `hs1-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | 2026-10-15 |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control |
| Audience | All new staff, clinical and non-clinical, in their first week |
| Seat-time budget | ~55 minutes |
| SCORM / completion / pass mark | SCORM 2004 4th edition · viewed_all_and_passed · pass 80% (176 / 220) |
| Scored screens / total points | 24 / 220 (Phase 4 expectation: 24 / 220) |
| Source file | `elearning-course/md/01_health-and-safety-1_facility-management-and-safety.md` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-15) |
| Module colour | Ambitious teal #008C99 |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | B1–B10; program D1, D2, D11 and D14 |
| Narration reconciliation | Detailed card scripts: 5.8 min; Phase 3 per-screen targets: 16.5 min; Phase 3 rough module estimate: ~19 min. Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review. The difference is not padded with generated sentences (G11/C20): [`narration-gaps.md`](narration-gaps.md) lists the 42 screens that need authored prose. |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
| `hs1-o1` | Name the eight FMS plans and match each to its purpose. | `hs1-104` |
| `hs1-o2` | Apply the AREC cycle and the hierarchy of controls to a workplace hazard. | `hs1-204`, `hs1-205` |
| `hs1-o3` | Match each MOH emergency code to its meaning and follow the common response pattern. | `hs1-302`, `hs1-304` |
| `hs1-o4` | Respond to a fire using RACE and PASS, choosing the correct extinguisher and evacuation type. | `hs1-402`, `hs1-403`, `hs1-405`, `hs1-407`, `hs1-408`, `hs1-409` |
| `hs1-o5` | Interpret GHS pictograms and the NFPA diamond, decide on Code Orange, and segregate waste correctly. | `hs1-502`, `hs1-503`, `hs1-504`, `hs1-507`, `hs1-508` |
| `hs1-o6` | Apply ID, visitor, contractor and premises security rules. | `hs1-602` |
| `hs1-o7` | Identify emergency power, utility shut-offs and HVAC rules in a clinical area. | `hs1-702` |
| `hs1-o8` | Take faulty or overdue medical equipment out of use and report it to Biomedical Engineering. | `hs1-802`, `hs1-803` |
| `hs1-o9` | Apply ALARA, dose-limit bands and laser classes to stay safe near radiation and lasers. | `hs1-902`, `hs1-905`, `hs1-906` |
| `hs1-o10` | Combine the plans in one connected emergency (capstone). | `hs1-950` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `hs1-s0` | Welcome | `hs1-000`–`hs1-002` |
| `hs1-s1` | 1 · The eight FMS plans | `hs1-101`–`hs1-104` |
| `hs1-s2` | 2 · Occupational Health & Safety | `hs1-201`–`hs1-206` |
| `hs1-s3` | 3 · Emergency codes | `hs1-301`–`hs1-305` |
| `hs1-s4` | 4 · Fire safety | `hs1-401`–`hs1-410` |
| `hs1-s5` | 5 · Hazardous materials & waste | `hs1-501`–`hs1-508` |
| `hs1-s6` | 6 · Security | `hs1-601`–`hs1-602` |
| `hs1-s7` | 7 · Utilities | `hs1-701`–`hs1-702` |
| `hs1-s8` | 8 · Medical equipment | `hs1-801`–`hs1-803` |
| `hs1-s9` | 9 · Radiation & laser | `hs1-901`–`hs1-907` |
| `hs1-s10` | Capstone & completion | `hs1-950`–`hs1-990` |

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

### `hs1-000` — Facility Management & Safety

**Status:** `Draft — ready for SME review` · **Section / node:** Welcome / `hs1-s0` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open the course |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.1 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Facility Management & Safety |
| Body / keywords | "Facility Management & Safety" · "Your first-week safety essentials" |
| Word count (excl. title) | 7 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L1 Title |
| Logo | `logo-horizontal-white.png`, 48 px at top-left |
| Visual concept | Official navy title gradient with supplied white My Clinic logo, large Montserrat course title, and a cropped white petal watermark. Noor is placed l1 half-body bottom-right. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `primary` · text `on_primary` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | Supplied white petal mark at 8–10% opacity, cropped off the right edge. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-welcome · placement L1 half-body bottom-right · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Official navy title background supplied by My Clinic; no content is baked into it.` | photo | Official navy title background supplied by My Clinic; no content is baked into it. | own / official My Clinic asset | Decorative navy title gradient. | Yes |
| `Supplied My Clinic horizontal white logo lock-up.` | icon | Supplied My Clinic horizontal white logo lock-up. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-welcome at L1 half-body bottom-right.` | illustration | Approved program companion pose char-noor-welcome at L1 half-body bottom-right. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "Facility Management & Safety" · "Your first-week safety essentials" |
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
| Tone | warm |
| Target seconds | 15 |
| Word count / estimated seconds | 26 words / ≈ 11.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Welcome to Facility Management & Safety. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift.

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
  "id": "hs1-000",
  "title": "Facility Management & Safety",
  "section": "Welcome",
  "node_id": "hs1-s0",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-000",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-000`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-001` — Why it matters; how the course works

**Status:** `Draft — ready for SME review` · **Section / node:** Welcome / `hs1-s0` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Why it matters; how the course works |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.1, 3 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why it matters; how the course works |
| Body / keywords | 3 icons: Protect patients · Protect you · Pass the CBAHI survey; "9 short sections · resume any time" |
| Word count (excl. title) | 16 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for why it matters; how the course works, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. Noor is placed l3 right column, half-body. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-explaining · placement L3 right column, half-body · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-explaining at L3 right column, half-body.` | illustration | Approved program companion pose char-noor-explaining at L3 right column, half-body. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 3 icons: Protect patients · Protect you · Pass the CBAHI survey; "9 short sections · resume any time" |
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
| Target seconds | 30 |
| Word count / estimated seconds | 21 words / ≈ 9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: CBAHI surveyors ask staff, not just managers. On my first day I didn't know where the nearest call point was.

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
  "id": "hs1-001",
  "title": "Why it matters; how the course works",
  "section": "Welcome",
  "node_id": "hs1-s0",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-001",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-001`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-002` — Unscored confidence check (baseline)

**Status:** `Draft — ready for SME review` · **Section / node:** Welcome / `hs1-s0` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Unscored confidence check (baseline) |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Unscored confidence check (baseline) |
| Body / keywords | "How confident are you to act in a fire right now?" 1–4 |
| Word count (excl. title) | 13 |
| Instruction | Reflection text: "We'll come back to this at the end." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for unscored confidence check (baseline), using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "How confident are you to act in a fire right now?" 1–4 |
| Build / feedback brief | Reflection text: "We'll come back to this at the end." |
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
| Tone | reflective |
| Target seconds | 8 |
| Word count / estimated seconds | 19 words / ≈ 8.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: This reflection is not scored. Choose the response that helps you set one intention for your next shift.

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
  "type": "poll",
  "id": "hs1-002",
  "title": "Unscored confidence check (baseline)",
  "section": "Welcome",
  "node_id": "hs1-s0",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-002",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-002`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-101` — Why the chapter exists

**Status:** `Draft — ready for SME review` · **Section / node:** 1 · The eight FMS plans / `hs1-s1` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Why the chapter exists |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.3 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why the chapter exists |
| Body / keywords | Survey requirement · Everyone's responsibility · One connected system |
| Word count (excl. title) | 7 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for why the chapter exists, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Survey requirement · Everyone's responsibility · One connected system |
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
| Target seconds | 35 |
| Word count / estimated seconds | 14 words / ≈ 6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The chapter is a survey requirement, a shared responsibility, and one connected system.

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
  "id": "hs1-101",
  "title": "Why the chapter exists",
  "section": "1 · The eight FMS plans",
  "node_id": "hs1-s1",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-101",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-101`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-102` — The eight plans

**Status:** `Draft — ready for SME review` · **Section / node:** 1 · The eight FMS plans / `hs1-s1` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explore the eight plans |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.4–8 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The eight plans |
| Body / keywords | Icon grid of 8 plans (own SVG). Each region opens: purpose + 4 main functions |
| Word count (excl. title) | 14 |
| Instruction | All 8 regions must be opened |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for explore the eight plans, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. |
| edumints layout | n/a (interaction screen) |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-8plans` | diagram | hs1-img-8plans: 4×2 grid, one line icon per plan, label under each; hotspot rects per tile Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "Eight Facility Management and Safety plans shown as icons." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Icon grid of 8 plans (own SVG). Each region opens: purpose + 4 main functions |
| Build / feedback brief | All 8 regions must be opened |
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
| Target seconds | 25 |
| Word count / estimated seconds | 12 words / ≈ 5.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Open each marker in turn before you decide what happens next.

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
  "id": "hs1-102",
  "title": "The eight plans",
  "section": "1 · The eight FMS plans",
  "node_id": "hs1-s1",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-102",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-8plans> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-102`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-103` — Plans ↔ codes link

**Status:** `Draft — ready for SME review` · **Section / node:** 1 · The eight FMS plans / `hs1-s1` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Plans ↔ codes link |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.3 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Plans ↔ codes link |
| Body / keywords | "A fire is a Code Red. A chemical spill is a Code Orange." |
| Word count (excl. title) | 13 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for plans ↔ codes link, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "A fire is a Code Red. A chemical spill is a Code Orange." |
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
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Plans and codes are two views of the same system: give one example of each.

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
  "id": "hs1-103",
  "title": "Plans ↔ codes link",
  "section": "1 · The eight FMS plans",
  "node_id": "hs1-s1",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-103",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-103`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-104` — Plans

**Status:** `Draft — ready for SME review` · **Section / node:** 1 · The eight FMS plans / `hs1-s1` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check plans |
| Objective(s) | `hs1-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.5–8 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Plans |
| Body / keywords | 8 pairs: plan ↔ purpose (one sentence each) |
| Word count (excl. title) | 7 |
| Instruction | Per-pair feedback; correct set shown after submit |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for check plans. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | 8 pairs: plan ↔ purpose (one sentence each) |
| Build / feedback brief | Per-pair feedback; correct set shown after submit |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Per-pair feedback; correct set shown after submit |
| Feedback — incorrect | Retry/incorrect feedback route: Per-pair feedback; correct set shown after submit |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Match each item to the person or step that owns it, then read the feedback.

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
  "id": "hs1-104",
  "title": "Plans",
  "section": "1 · The eight FMS plans",
  "node_id": "hs1-s1",
  "objective_ids": [
    "hs1-o1"
  ],
  "points": 10,
  "narration_script_id": "hs1-104",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-104`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-201` — Four core terms

**Status:** `Draft — ready for SME review` · **Section / node:** 2 · Occupational Health & Safety / `hs1-s2` · **Type:** `flashcards` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Four core terms |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.10 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Four core terms |
| Body / keywords | Health · Safety · Hazard · Risk (front term, back definition + example) |
| Word count (excl. title) | 9 |
| Instruction | Flip |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for four core terms, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Health · Safety · Hazard · Risk (front term, back definition + example) |
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
| Target seconds | 25 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Risk is likelihood plus severity. A hazard is the thing, risk is the chance it hurts someone.

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
  "id": "hs1-201",
  "title": "Four core terms",
  "section": "2 · Occupational Health & Safety",
  "node_id": "hs1-s2",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-201",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-201`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-202` — Incident types

**Status:** `Draft — ready for SME review` · **Section / node:** 2 · Occupational Health & Safety / `hs1-s2` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Incident types |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.11 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Incident types |
| Body / keywords | Near miss · First aid · Medical treatment · Lost time · Fatality. Near miss tagged "most valuable to report" |
| Word count (excl. title) | 16 |
| Instruction | Open each |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for incident types, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Near miss · First aid · Medical treatment · Lost time · Fatality. Near miss tagged "most valuable to report" |
| Build / feedback brief | Open each |
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
| Target seconds | 30 |
| Word count / estimated seconds | 13 words / ≈ 5.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: A near miss is the most valuable report: it is free learning.

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
  "id": "hs1-202",
  "title": "Incident types",
  "section": "2 · Occupational Health & Safety",
  "node_id": "hs1-s2",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-202",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-202`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-203` — AREC cycle

**Status:** `Draft — ready for SME review` · **Section / node:** 2 · Occupational Health & Safety / `hs1-s2` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | AREC cycle |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.12 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | AREC cycle |
| Body / keywords | Circular SVG: Anticipate → Recognise → Evaluate → Control |
| Word count (excl. title) | 6 |
| Instruction | 4 labels with short text |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for arec cycle, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-arec` | diagram | hs1-img-arec: 4-stage circular arrow, brand colours Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "AREC cycle: Anticipate, Recognise, Evaluate, Control." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Circular SVG: Anticipate → Recognise → Evaluate → Control |
| Build / feedback brief | 4 labels with short text |
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
| Target seconds | 30 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: AREC as a habit before every task, not a form.

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
  "id": "hs1-203",
  "title": "AREC cycle",
  "section": "2 · Occupational Health & Safety",
  "node_id": "hs1-s2",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-203",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-arec> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-203`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-204` — Hierarchy of controls

**Status:** `Draft — ready for SME review` · **Section / node:** 2 · Occupational Health & Safety / `hs1-s2` · **Type:** `sorting` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Hierarchy of controls |
| Objective(s) | `hs1-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.13 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Hierarchy of controls |
| Body / keywords | Order most → least effective: Elimination, Substitution, Engineering, Administrative, PPE |
| Word count (excl. title) | 9 |
| Instruction | Feedback: "PPE is the last line of defence, not the first." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for hierarchy of controls. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Order most → least effective: Elimination, Substitution, Engineering, Administrative, PPE |
| Build / feedback brief | Feedback: "PPE is the last line of defence, not the first." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: "PPE is the last line of defence, not the first." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "PPE is the last line of defence, not the first." |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Put the steps in the order you would follow at work, then read the feedback.

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
  "id": "hs1-204",
  "title": "Hierarchy of controls",
  "section": "2 · Occupational Health & Safety",
  "node_id": "hs1-s2",
  "objective_ids": [
    "hs1-o2"
  ],
  "points": 10,
  "narration_script_id": "hs1-204",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-204`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-205` — AREC + controls + rights

**Status:** `Draft — ready for SME review` · **Section / node:** 2 · Occupational Health & Safety / `hs1-s2` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Apply AREC + controls + rights |
| Objective(s) | `hs1-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.12–15 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | AREC + controls + rights |
| Body / keywords | Corridor with a trailing cable across a walkway near a patient waiting area (illustration). 3 nodes: (1) what do you do first; (2) which control is strongest (re-route cable / cover / sign / warn); (3) supervisor says "leave it … |
| Word count (excl. title) | 37 |
| Instruction | Each choice has a why feedback; pass_score 2 of 3 best choices |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for apply arec + controls + rights. Noor is placed l5 avatar above situation. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-avatar-neutral → -happy / -concern · placement L5 avatar above situation · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-avatar-neutral → -happy / -concern at L5 avatar above situation.` | illustration | Approved program companion pose char-noor-avatar-neutral → -happy / -concern at L5 avatar above situation. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Corridor with a trailing cable across a walkway near a patient waiting area (illustration). 3 nodes: (1) what do you do first; (2) which control is strongest (re-route cable / cover / sign / warn); (3) supervisor says "leave it, we're busy" → use your right to stop unsafe work, contact your Safety Liaison |
| Build / feedback brief | Each choice has a why feedback; pass_score 2 of 3 best choices |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | pass_score 2 of 3 best choices |
| Feedback — correct | Source feedback route: Each choice has a why feedback; pass_score 2 of 3 best choices |
| Feedback — incorrect | Retry/incorrect feedback route: Each choice has a why feedback; pass_score 2 of 3 best choices |
| Per-choice feedback (scenarios) | Each choice has a why feedback; pass_score 2 of 3 best choices |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Play the situation through and decide, then read the feedback.

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
  "id": "hs1-205",
  "title": "AREC + controls + rights",
  "section": "2 · Occupational Health & Safety",
  "node_id": "hs1-s2",
  "objective_ids": [
    "hs1-o2"
  ],
  "points": 15,
  "narration_script_id": "hs1-205",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-205`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-206` — Who to contact + your rights

**Status:** `Draft — ready for SME review` · **Section / node:** 2 · Occupational Health & Safety / `hs1-s2` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Who to contact + your rights |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.14–15 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Who to contact + your rights |
| Body / keywords | Department Safety Liaison (ask your supervisor on day 1) · Right to stop unsafe work · Right to be consulted · Right to training |
| Word count (excl. title) | 21 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for who to contact + your rights, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. Omar is placed l3 tip card bottom-left. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-neutral + tip card · placement L3 tip card bottom-left · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-avatar-neutral + tip card at L3 tip card bottom-left.` | illustration | Approved program companion pose char-omar-avatar-neutral + tip card at L3 tip card bottom-left. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Department Safety Liaison (ask your supervisor on day 1) · Right to stop unsafe work · Right to be consulted · Right to training |
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
| Target seconds | 30 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: You can stop unsafe work without fear. If you're unsure, ask your supervisor who your liaison is.

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
  "id": "hs1-206",
  "title": "Who to contact + your rights",
  "section": "2 · Occupational Health & Safety",
  "node_id": "hs1-s2",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-206",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-206`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-301` — The codes

**Status:** `Draft — ready for SME review` · **Section / node:** 3 · Emergency codes / `hs1-s3` · **Type:** `flashcards` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Learn the codes |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.17–18 |
| Depends on Phase 0 | ⚠ PENDING D2; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The codes |
| Body / keywords | 11 cards: front = code name + colour chip (bilingual EN/AR), back = meaning + extension (pending D2) |
| Word count (excl. title) | 15 |
| Instruction | Flip |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for learn the codes, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. Noor is placed l3 tip card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-avatar-neutral + tip card · placement L3 tip card · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-codes-chips` | diagram | hs1-img-codes-chips: 11 colour chips with code names printed Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | (decorative — name is in text) | No |
| `Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card.` | illustration | Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 11 cards: front = code name + colour chip (bilingual EN/AR), back = meaning + extension (pending D2) |
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
| Target seconds | 30 |
| Word count / estimated seconds | 17 words / ≈ 7.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Codes are announced overhead. Learn the meaning, then your site's extension. Code Blue is 2222 everywhere.

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
  "id": "hs1-301",
  "title": "The codes",
  "section": "3 · Emergency codes",
  "node_id": "hs1-s3",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-301",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-codes-chips> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D2; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-301`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-302` — Codes

**Status:** `Draft — ready for SME review` · **Section / node:** 3 · Emergency codes / `hs1-s3` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check codes |
| Objective(s) | `hs1-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.17–18 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Codes |
| Body / keywords | 8 pairs (randomised): Red–Fire, Orange–Hazmat spill, White–Violent situation, Black–Bomb threat, Pink–Child/infant abduction, Blue–Cardiac arrest, Yellow–External disaster, Brown–Utility failure |
| Word count (excl. title) | 27 |
| Instruction | Feedback per pair |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for check codes. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | 8 pairs (randomised): Red–Fire, Orange–Hazmat spill, White–Violent situation, Black–Bomb threat, Pink–Child/infant abduction, Blue–Cardiac arrest, Yellow–External disaster, Brown–Utility failure |
| Build / feedback brief | Feedback per pair |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback per pair |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback per pair |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Match each item to the person or step that owns it, then read the feedback.

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
  "id": "hs1-302",
  "title": "Codes",
  "section": "3 · Emergency codes",
  "node_id": "hs1-s3",
  "objective_ids": [
    "hs1-o3"
  ],
  "points": 10,
  "narration_script_id": "hs1-302",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-302`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-303` — Two announcements

**Status:** `Draft — ready for SME review` · **Section / node:** 3 · Emergency codes / `hs1-s3` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Two announcements |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.19 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Two announcements |
| Body / keywords | Hospital Evacuation (go to assembly point) · End of Disaster (stand down only on this signal) |
| Word count (excl. title) | 15 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for two announcements, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Hospital Evacuation (go to assembly point) · End of Disaster (stand down only on this signal) |
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
| Target seconds | 25 |
| Word count / estimated seconds | 17 words / ≈ 7.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Evacuation and End of Disaster are announcements, not colours. Only stand down on the official all-clear.

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
  "id": "hs1-303",
  "title": "Two announcements",
  "section": "3 · Emergency codes",
  "node_id": "hs1-s3",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-303",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-303`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-304` — Common response pattern

**Status:** `Draft — ready for SME review` · **Section / node:** 3 · Emergency codes / `hs1-s3` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Common response pattern |
| Objective(s) | `hs1-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.20 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Common response pattern |
| Body / keywords | Recognise → Activate → Respond → Stand down |
| Word count (excl. title) | 5 |
| Instruction | Feedback reinforces "wait for the official all-clear" |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for common response pattern. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Recognise → Activate → Respond → Stand down |
| Build / feedback brief | Feedback reinforces "wait for the official all-clear" |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback reinforces "wait for the official all-clear" |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback reinforces "wait for the official all-clear" |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Put the steps in the order you would follow at work, then read the feedback.

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
  "id": "hs1-304",
  "title": "Common response pattern",
  "section": "3 · Emergency codes",
  "node_id": "hs1-s3",
  "objective_ids": [
    "hs1-o3"
  ],
  "points": 5,
  "narration_script_id": "hs1-304",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-304`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-305` — Who responds

**Status:** `Draft — ready for SME review` · **Section / node:** 3 · Emergency codes / `hs1-s3` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Who responds |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.21 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Who responds |
| Body / keywords | ERT diagram: Safety · Security · Nursing · Facility · Operation around an Incident Commander |
| Word count (excl. title) | 11 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for who responds, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-ert` | diagram | hs1-img-ert: Incident Commander centre, 5 team nodes Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "Emergency Response Team: Safety, Security, Nursing, Facility, Operation." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | ERT diagram: Safety · Security · Nursing · Facility · Operation around an Incident Commander |
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
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The ERT is five teams. You are part of the response even if you're not on it.

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
  "id": "hs1-305",
  "title": "Who responds",
  "section": "3 · Emergency codes",
  "node_id": "hs1-s3",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-305",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-ert> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-305`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-401` — Fire triangle + smoke

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Fire triangle + smoke |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.23 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Fire triangle + smoke |
| Body / keywords | Triangle: Heat · Fuel · Oxygen. Callout: "Smoke, not flame, is the leading cause of death." |
| Word count (excl. title) | 14 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for fire triangle + smoke, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-triangle` | diagram | hs1-img-triangle: Fire triangle with three labelled sides Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "Fire triangle: heat, fuel and oxygen." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Triangle: Heat · Fuel · Oxygen. Callout: "Smoke, not flame, is the leading cause of death." |
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
| Target seconds | 30 |
| Word count / estimated seconds | 23 words / ≈ 9.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Remove one side of the triangle and the fire stops. Smoke kills first, which is why RACE rescues and contains before extinguishing.

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
  "id": "hs1-401",
  "title": "Fire triangle + smoke",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-401",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-triangle> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-401`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-402` — RACE

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | RACE |
| Objective(s) | `hs1-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.24 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | RACE |
| Body / keywords | Rescue → Alarm → Contain → Extinguish/Evacuate |
| Word count (excl. title) | 5 |
| Instruction | Feedback explains why rescue and contain come before extinguishing |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for race. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Rescue → Alarm → Contain → Extinguish/Evacuate |
| Build / feedback brief | Feedback explains why rescue and contain come before extinguishing |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback explains why rescue and contain come before extinguishing |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback explains why rescue and contain come before extinguishing |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Put the steps in the order you would follow at work, then read the feedback.

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
  "id": "hs1-402",
  "title": "RACE",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [
    "hs1-o4"
  ],
  "points": 5,
  "narration_script_id": "hs1-402",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-402`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-403` — PASS

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | PASS |
| Objective(s) | `hs1-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.24 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | PASS |
| Body / keywords | Pull → Aim (low, at the base) → Squeeze → Sweep |
| Word count (excl. title) | 8 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for pass. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Pull → Aim (low, at the base) → Squeeze → Sweep |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Put the steps in the order you would follow at work, then read the feedback.

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
  "id": "hs1-403",
  "title": "PASS",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [
    "hs1-o4"
  ],
  "points": 5,
  "narration_script_id": "hs1-403",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-403`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-404` — Find the equipment

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Find the equipment |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.25–26 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Find the equipment |
| Body / keywords | Clinic corridor illustration with 8 regions: smoke detector, heat detector, call point, extinguisher, fire blanket, sprinkler, evacuation chair, assembly-point sign |
| Word count (excl. title) | 20 |
| Instruction | Each region: what it is + when you use it |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for find the equipment, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. |
| edumints layout | n/a (interaction screen) |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-corridor` | illustration | hs1-img-corridor: Generated 2026-10-14 — SME visual check required before hotspot coordinates are set. | ai-generated route, production/visual QA pending | Clinic corridor showing a call point, extinguisher, fire blanket, sprinkler, evacuation chair and assembly sign. | No |

**AI image prompt (recorded production prompt)**

```text
Single clean flat vector illustration for a My Clinic e-learning course. Clinic corridor showing a call point, extinguisher, fire blanket, sprinkler, evacuation chair and assembly sign. Use navy #003867 outlines, white space, soft blue-grey #C0CED9, and Ambitious teal #008C99 as the only value-colour highlight. No text, no letters, no numbers, no logos, no watermark, no patient/staff likeness, and no generated My Clinic mark.
```

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Clinic corridor illustration with 8 regions: smoke detector, heat detector, call point, extinguisher, fire blanket, sprinkler, evacuation chair, assembly-point sign |
| Build / feedback brief | Each region: what it is + when you use it |
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
| Word count / estimated seconds | 12 words / ≈ 5.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Walk the corridor. Know where these are before you need them.

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
  "id": "hs1-404",
  "title": "Find the equipment",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-404",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-corridor> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-404`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-405` — Extinguisher classes

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Extinguisher classes |
| Objective(s) | `hs1-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.27–28 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Extinguisher classes |
| Body / keywords | Items: "Burning paper bin", "Petrol leak", "Smoking photocopier", "Magnesium shavings", "Pantry pan fire" → targets Class A / B / C / D / K |
| Word count (excl. title) | 20 |
| Instruction | Keyboard-operable; feedback: "Check the label before you pull the pin." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for extinguisher classes. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Items: "Burning paper bin", "Petrol leak", "Smoking photocopier", "Magnesium shavings", "Pantry pan fire" → targets Class A / B / C / D / K |
| Build / feedback brief | Keyboard-operable; feedback: "Check the label before you pull the pin." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Keyboard-operable; feedback: "Check the label before you pull the pin." |
| Feedback — incorrect | Retry/incorrect feedback route: Keyboard-operable; feedback: "Check the label before you pull the pin." |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Place each item where it belongs, then read the feedback.

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
  "id": "hs1-405",
  "title": "Extinguisher classes",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [
    "hs1-o4"
  ],
  "points": 10,
  "narration_script_id": "hs1-405",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-405`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-406` — Evacuation types

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Evacuation types |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.29 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Evacuation types |
| Body / keywords | Horizontal (first response, same floor) · Vertical (stairwells, never elevators) · Full (whole building, assembly point) |
| Word count (excl. title) | 14 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for evacuation types, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Horizontal (first response, same floor) · Vertical (stairwells, never elevators) · Full (whole building, assembly point) |
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
| Target seconds | 35 |
| Word count / estimated seconds | 13 words / ≈ 5.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Horizontal first. Vertical by stairs. Full evacuation only for the worst events.

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
  "type": "tabs",
  "id": "hs1-406",
  "title": "Evacuation types",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-406",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-406`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-407` — Choose the evacuation

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Choose the evacuation |
| Objective(s) | `hs1-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.29 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Choose the evacuation |
| Body / keywords | "Smoke in Room 3; fire doors at the end of the corridor; patients on the same floor are not in danger yet. First move?" → Horizontal to the next compartment |
| Word count (excl. title) | 29 |
| Instruction | Wrong options explain why (elevator, full evacuation too early) |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for choose the evacuation. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "Smoke in Room 3; fire doors at the end of the corridor; patients on the same floor are not in danger yet. First move?" → Horizontal to the next compartment |
| Build / feedback brief | Wrong options explain why (elevator, full evacuation too early) |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Wrong options explain why (elevator, full evacuation too early) |
| Feedback — incorrect | Retry/incorrect feedback route: Wrong options explain why (elevator, full evacuation too early) |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "id": "hs1-407",
  "title": "Choose the evacuation",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [
    "hs1-o4"
  ],
  "points": 5,
  "narration_script_id": "hs1-407",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-407`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-408` — Oxygen myth

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `true_false` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Oxygen myth |
| Objective(s) | `hs1-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.31 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Oxygen myth |
| Body / keywords | "Oxygen is flammable." → False: oxidiser, intensifies fire |
| Word count (excl. title) | 7 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for oxygen myth. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "Oxygen is flammable." → False: oxidiser, intensifies fire |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "type": "true_false",
  "id": "hs1-408",
  "title": "Oxygen myth",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [
    "hs1-o4"
  ],
  "points": 5,
  "narration_script_id": "hs1-408",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-408`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-409` — Put RACE into action

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `decision_scenario` · **Scored:** Yes (20 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Put RACE into action |
| Objective(s) | `hs1-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.23–31 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Put RACE into action |
| Body / keywords | Night shift: smoke from a waste bin in a patient room. Nodes: (1) first action (rescue patient); (2) the call — what to say (code, location, ID & name); (3) contain (remove O₂ cylinder and alcohol rub, close door); (4) … |
| Word count (excl. title) | 38 |
| Instruction | Each node has consequences; pass_score 3 of 4 |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for put race into action. Noor is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-avatar-neutral → -happy / -concern · placement L5 avatar · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-avatar-neutral → -happy / -concern at L5 avatar.` | illustration | Approved program companion pose char-noor-avatar-neutral → -happy / -concern at L5 avatar. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Night shift: smoke from a waste bin in a patient room. Nodes: (1) first action (rescue patient); (2) the call — what to say (code, location, ID & name); (3) contain (remove O₂ cylinder and alcohol rub, close door); (4) fire grows past the bin → evacuate horizontally |
| Build / feedback brief | Each node has consequences; pass_score 3 of 4 |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 20 |
| Pass rule (scenarios / games) | pass_score 3 of 4 |
| Feedback — correct | Source feedback route: Each node has consequences; pass_score 3 of 4 |
| Feedback — incorrect | Retry/incorrect feedback route: Each node has consequences; pass_score 3 of 4 |
| Per-choice feedback (scenarios) | Each node has consequences; pass_score 3 of 4 |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Play the situation through and decide, then read the feedback.

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
  "id": "hs1-409",
  "title": "Put RACE into action",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [
    "hs1-o4"
  ],
  "points": 20,
  "narration_script_id": "hs1-409",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-409`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-410` — Fire prevention

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Fire prevention |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.30 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Fire prevention |
| Body / keywords | 7 icons: candles · unauthorised welding · extensions · heaters/boilers · smoking & vaping · unauthorised microwaves · uncontrolled flammables |
| Word count (excl. title) | 14 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for fire prevention, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | 7 icons: candles · unauthorised welding · extensions · heaters/boilers · smoking & vaping · unauthorised microwaves · uncontrolled flammables |
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
| Target seconds | 25 |
| Word count / estimated seconds | 12 words / ≈ 5.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Prevention rules exist because each item started a real fire somewhere.

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
  "id": "hs1-410",
  "title": "Fire prevention",
  "section": "4 · Fire safety",
  "node_id": "hs1-s4",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-410",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-410`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-501` — Ordering & inventory

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Ordering & inventory |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.33 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Ordering & inventory |
| Body / keywords | Approved procurement only · On the inventory with SDS · Never accept an unlabelled container |
| Word count (excl. title) | 13 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for ordering & inventory, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Approved procurement only · On the inventory with SDS · Never accept an unlabelled container |
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
| Target seconds | 25 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Chemicals come in one door only — procurement — and never without a label and an SDS.

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
  "id": "hs1-501",
  "title": "Ordering & inventory",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-501",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-501`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-502` — GHS pictograms

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | GHS pictograms |
| Objective(s) | `hs1-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.34 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | GHS pictograms |
| Body / keywords | 9 pairs: pictogram (own SVG via left_html image or name) ↔ hazard |
| Word count (excl. title) | 12 |
| Instruction | Feedback per pair |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for ghs pictograms. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-ghs-1` | diagram | hs1-img-ghs-1: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-2` | diagram | hs1-img-ghs-2: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-3` | diagram | hs1-img-ghs-3: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-4` | diagram | hs1-img-ghs-4: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-5` | diagram | hs1-img-ghs-5: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-6` | diagram | hs1-img-ghs-6: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-7` | diagram | hs1-img-ghs-7: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-8` | diagram | hs1-img-ghs-8: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |
| `hs1-img-ghs-9` | diagram | hs1-img-ghs-9: 9 GHS pictograms redrawn (red diamond, black symbol) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | name of each pictogram | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 9 pairs: pictogram (own SVG via left_html image or name) ↔ hazard |
| Build / feedback brief | Feedback per pair |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback per pair |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback per pair |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Match each item to the person or step that owns it, then read the feedback.

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
  "id": "hs1-502",
  "title": "GHS pictograms",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [
    "hs1-o5"
  ],
  "points": 10,
  "narration_script_id": "hs1-502",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-ghs-1> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-2> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-3> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-4> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-5> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-6> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-7> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-8> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <hs1-img-ghs-9> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-502`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-503` — NFPA diamond parts

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `labeled_diagram` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | NFPA diamond parts |
| Objective(s) | `hs1-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.35–36 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | NFPA diamond parts |
| Body / keywords | Place 4 labels: Health (blue) · Flammability (red) · Reactivity (yellow) · Special (white) |
| Word count (excl. title) | 11 |
| Instruction | Colour + position + text label (not colour alone) |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for nfpa diamond parts. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-nfpa-blank` | diagram | hs1-img-nfpa-blank: Generic NFPA 704 diamond, quadrants without labels Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "Empty NFPA hazard diamond with four quadrants." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Place 4 labels: Health (blue) · Flammability (red) · Reactivity (yellow) · Special (white) |
| Build / feedback brief | Colour + position + text label (not colour alone) |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Colour + position + text label (not colour alone) |
| Feedback — incorrect | Retry/incorrect feedback route: Colour + position + text label (not colour alone) |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Label the parts you can name, then read the feedback.

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
  "id": "hs1-503",
  "title": "NFPA diamond parts",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [
    "hs1-o5"
  ],
  "points": 10,
  "narration_script_id": "hs1-503",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-nfpa-blank> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-503`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-504` — A diamond

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Read a diamond |
| Objective(s) | `hs1-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.36 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | A diamond |
| Body / keywords | Diamond shows Health 3 · Flammability 0 · Reactivity 1 · Special W. "What does this tell you before opening?" → serious health hazard; do not use water |
| Word count (excl. title) | 24 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for read a diamond. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-nfpa-301w` | diagram | hs1-img-nfpa-301w: Diamond with 3/0/1/W Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "NFPA diamond: health 3, flammability 0, reactivity 1, special W." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Diamond shows Health 3 · Flammability 0 · Reactivity 1 · Special W. "What does this tell you before opening?" → serious health hazard; do not use water |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "id": "hs1-504",
  "title": "A diamond",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [
    "hs1-o5"
  ],
  "points": 5,
  "narration_script_id": "hs1-504",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-nfpa-301w> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-504`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-505` — Store, handle, transport

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Store, handle, transport |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.37–38 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Store, handle, transport |
| Body / keywords | Storage per SDS · Designated carts & routes · PPE per SDS · Flammable cabinet (double-walled, self-latching) · SDS at point of use |
| Word count (excl. title) | 18 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for store, handle, transport, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Storage per SDS · Designated carts & routes · PPE per SDS · Flammable cabinet (double-walled, self-latching) · SDS at point of use |
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
| Target seconds | 30 |
| Word count / estimated seconds | 9 words / ≈ 3.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Storage, transport and handling all follow the SDS.

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
  "id": "hs1-505",
  "title": "Store, handle, transport",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-505",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-505`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-506` — Eyewash and showers

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Eyewash and showers |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.39 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Eyewash and showers |
| Body / keywords | "Find your nearest one today." "Flush ≥ 15 minutes." Photo of a unit (own) |
| Word count (excl. title) | 13 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for eyewash and showers, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. Omar is placed l3 tip card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-neutral + tip card · placement L3 tip card · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-eyewash` | photo | hs1-img-eyewash: Own photo of a My Clinic eyewash/shower unit Placement: Screen visual; production placement reviewed by the SME. PENDING My Clinic photo permission and Facilities/EHS approval of the pictured unit. | client photo, permission/SME review pending | "Combined eyewash and emergency shower station." | No |
| `Approved program companion pose char-omar-avatar-neutral + tip card at L3 tip card.` | illustration | Approved program companion pose char-omar-avatar-neutral + tip card at L3 tip card. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "Find your nearest one today." "Flush ≥ 15 minutes." Photo of a unit (own) |
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
| Word count / estimated seconds | 13 words / ≈ 5.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Find your nearest eyewash today. 15 minutes feels long — don't stop early.

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
  "id": "hs1-506",
  "title": "Eyewash and showers",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-506",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-eyewash> — Screen visual; production placement reviewed by the SME.. PENDING My Clinic photo permission and Facilities/EHS approval of the pictured unit."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-506`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-507` — Code Orange decision

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Code Orange decision |
| Objective(s) | `hs1-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.40 |
| Depends on Phase 0 | ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Code Orange decision |
| Body / keywords | 3 short cases: (a) small spill of hand rub; (b) a spill over the threshold of surface disinfectant; (c) a few mL of a highly toxic reagent → Code Orange? + 4 response steps (isolate & warn → PPE per … |
| Word count (excl. title) | 36 |
| Instruction | Rule shown in feedback (text depends on D1) |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for code orange decision. Noor is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-avatar-concern (intro) · placement L5 avatar · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-avatar-concern (intro) at L5 avatar.` | illustration | Approved program companion pose char-noor-avatar-concern (intro) at L5 avatar. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 3 short cases: (a) small spill of hand rub; (b) a spill over the threshold of surface disinfectant; (c) a few mL of a highly toxic reagent → Code Orange? + 4 response steps (isolate & warn → PPE per SDS → contain with right kit → report) |
| Build / feedback brief | Rule shown in feedback (text depends on D1) |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Rule shown in feedback (text depends on D1) |
| Feedback — incorrect | Retry/incorrect feedback route: Rule shown in feedback (text depends on D1) |
| Per-choice feedback (scenarios) | Rule shown in feedback (text depends on D1) |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Play the situation through and decide, then read the feedback.

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
  "id": "hs1-507",
  "title": "Code Orange decision",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [
    "hs1-o5"
  ],
  "points": 15,
  "narration_script_id": "hs1-507",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-507`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-508` — Waste segregation

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Waste segregation |
| Objective(s) | `hs1-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.41 |
| Depends on Phase 0 | ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Waste segregation |
| Body / keywords | Items: used needle, blood-soaked dressing, paper towel (clean), scalpel blade, gloves with body fluid, food wrapper → General / Infectious / Sharps |
| Word count (excl. title) | 19 |
| Instruction | Feedback: "Never recap." Bin colours per B7 shown as text + colour |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for waste segregation. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Items: used needle, blood-soaked dressing, paper towel (clean), scalpel blade, gloves with body fluid, food wrapper → General / Infectious / Sharps |
| Build / feedback brief | Feedback: "Never recap." Bin colours per B7 shown as text + colour |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: "Never recap." Bin colours per B7 shown as text + colour |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "Never recap." Bin colours per B7 shown as text + colour |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 13 words / ≈ 5.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Never recap. Place each item where it belongs, then read the feedback.

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
  "id": "hs1-508",
  "title": "Waste segregation",
  "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5",
  "objective_ids": [
    "hs1-o5"
  ],
  "points": 10,
  "narration_script_id": "hs1-508",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-508`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-601` — Security rules

**Status:** `Draft — ready for SME review` · **Section / node:** 6 · Security / `hs1-s6` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Security rules |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.43–44 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Security rules |
| Body / keywords | People: ID always · contractor permits · visitor badges · Premises: CCTV · lost & found → Security · designated parking · no smoking anywhere |
| Word count (excl. title) | 17 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for security rules, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | People: ID always · contractor permits · visitor badges · Premises: CCTV · lost & found → Security · designated parking · no smoking anywhere |
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
| Target seconds | 30 |
| Word count / estimated seconds | 15 words / ≈ 6.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Your badge identifies you. Everyone without one in a restricted area is your concern.

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
  "type": "tabs",
  "id": "hs1-601",
  "title": "Security rules",
  "section": "6 · Security",
  "node_id": "hs1-s6",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-601",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-601`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-602` — Apply

**Status:** `Draft — ready for SME review` · **Section / node:** 6 · Security / `hs1-s6` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Apply |
| Objective(s) | `hs1-o6` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.43 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Apply |
| Body / keywords | "A man without a badge is in the staff-only medication room and says he is a contractor." Best action → politely ask for permit/badge; if none, call Security; do not leave him alone |
| Word count (excl. title) | 33 |
| Instruction | Wrong options explain risks |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for apply. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "A man without a badge is in the staff-only medication room and says he is a contractor." Best action → politely ask for permit/badge; if none, call Security; do not leave him alone |
| Build / feedback brief | Wrong options explain risks |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Wrong options explain risks |
| Feedback — incorrect | Retry/incorrect feedback route: Wrong options explain risks |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "id": "hs1-602",
  "title": "Apply",
  "section": "6 · Security",
  "node_id": "hs1-s6",
  "objective_ids": [
    "hs1-o6"
  ],
  "points": 5,
  "narration_script_id": "hs1-602",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-602`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-701` — Utility walk-around

**Status:** `Draft — ready for SME review` · **Section / node:** 7 · Utilities / `hs1-s7` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Utility walk-around |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.46–47 |
| Depends on Phase 0 | ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Utility walk-around |
| Body / keywords | Treatment-room illustration: red emergency socket (per B6), standard socket, UPS-backed monitor, unauthorised extension (crossed), water shut-off valve, HVAC vent in isolation room |
| Word count (excl. title) | 22 |
| Instruction | Region text: what it is, what you do |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for utility walk-around, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. |
| edumints layout | n/a (interaction screen) |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-treatment-room` | illustration | hs1-img-treatment-room: Room with sockets, UPS monitor, extension, valve, vent Placement: Screen visual; production placement reviewed by the SME. PENDING 01 B6; Facilities confirms equipment, sockets and visual targets before illustration/hotspots. | ai-generated route, production/visual QA pending | "Treatment room showing sockets, a valve and an air vent." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Treatment-room illustration: red emergency socket (per B6), standard socket, UPS-backed monitor, unauthorised extension (crossed), water shut-off valve, HVAC vent in isolation room |
| Build / feedback brief | Region text: what it is, what you do |
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
| Target seconds | 25 |
| Word count / estimated seconds | 15 words / ≈ 6.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Red sockets are on generator power. Know your shut-off valves. Isolation-room vents protect everyone.

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
  "id": "hs1-701",
  "title": "Utility walk-around",
  "section": "7 · Utilities",
  "node_id": "hs1-s7",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-701",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-treatment-room> — Screen visual; production placement reviewed by the SME.. PENDING 01 B6; Facilities confirms equipment, sockets and visual targets before illustration/hotspots."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-701`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-702` — Apply

**Status:** `Draft — ready for SME review` · **Section / node:** 7 · Utilities / `hs1-s7` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Apply |
| Objective(s) | `hs1-o7` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.47 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Apply |
| Body / keywords | "The isolation room is cold. A visitor asks you to close the vent." → Never disable isolation-room vents; report to Maintenance |
| Word count (excl. title) | 20 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for apply. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "The isolation room is cold. A visitor asks you to close the vent." → Never disable isolation-room vents; report to Maintenance |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "id": "hs1-702",
  "title": "Apply",
  "section": "7 · Utilities",
  "node_id": "hs1-s7",
  "objective_ids": [
    "hs1-o7"
  ],
  "points": 5,
  "narration_script_id": "hs1-702",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-702`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-801` — Labels, PPM, tagging

**Status:** `Draft — ready for SME review` · **Section / node:** 8 · Medical equipment / `hs1-s8` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Labels, PPM, tagging |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.49 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Labels, PPM, tagging |
| Body / keywords | Inspection label (date + status) · PPM schedule · "Out of Service" tag |
| Word count (excl. title) | 10 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for labels, ppm, tagging, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Inspection label (date + status) · PPM schedule · "Out of Service" tag |
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
| Target seconds | 25 |
| Word count / estimated seconds | 12 words / ≈ 5.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Labels tell you if a device is safe to use today.

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
  "id": "hs1-801",
  "title": "Labels, PPM, tagging",
  "section": "8 · Medical equipment",
  "node_id": "hs1-s8",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-801",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-801`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-802` — Spot it, report it

**Status:** `Draft — ready for SME review` · **Section / node:** 8 · Medical equipment / `hs1-s8` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Spot it, report it |
| Objective(s) | `hs1-o8` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.49–52 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Spot it, report it |
| Body / keywords | An infusion pump's label is 2 months overdue; the ward is busy. Nodes: use or not → tag out of service → who to notify (Biomedical Engineering) → colleague suggests moving a pump from another room (never relocate without BME) |
| Word count (excl. title) | 37 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for spot it, report it. Omar is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-neutral → -happy / -concern · placement L5 avatar · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-pump-label` | illustration | hs1-img-pump-label: Infusion pump with an overdue inspection label (fictional dates); label dates and overdue status in editable HTML, not AI-rendered lettering. Placement: Screen visual; production placement reviewed by the SME. PENDING Biomedical/Facilities confirmation of the inspection-label rule; fictional dates in an editable HTML overlay. | ai-generated route, production/visual QA pending | "Infusion pump with an overdue inspection label." | No |
| `Approved program companion pose char-omar-avatar-neutral → -happy / -concern at L5 avatar.` | illustration | Approved program companion pose char-omar-avatar-neutral → -happy / -concern at L5 avatar. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | An infusion pump's label is 2 months overdue; the ward is busy. Nodes: use or not → tag out of service → who to notify (Biomedical Engineering) → colleague suggests moving a pump from another room (never relocate without BME) |
| Build / feedback brief | n/a — informational screen. |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
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
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Play the situation through and decide, then read the feedback.

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
  "id": "hs1-802",
  "title": "Spot it, report it",
  "section": "8 · Medical equipment",
  "node_id": "hs1-s8",
  "objective_ids": [
    "hs1-o8"
  ],
  "points": 15,
  "narration_script_id": "hs1-802",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-pump-label> — Screen visual; production placement reviewed by the SME.. PENDING Biomedical/Facilities confirmation of the inspection-label rule; fictional dates in an editable HTML overlay."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-802`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-803` — Oxygen cylinders

**Status:** `Draft — ready for SME review` · **Section / node:** 8 · Medical equipment / `hs1-s8` · **Type:** `true_false` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Oxygen cylinders |
| Objective(s) | `hs1-o8` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.51 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Oxygen cylinders |
| Body / keywords | "Store cylinders upright and secured, with full and empty clearly separated." → True |
| Word count (excl. title) | 12 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for oxygen cylinders. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "Store cylinders upright and secured, with full and empty clearly separated." → True |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "type": "true_false",
  "id": "hs1-803",
  "title": "Oxygen cylinders",
  "section": "8 · Medical equipment",
  "node_id": "hs1-s8",
  "objective_ids": [
    "hs1-o8"
  ],
  "points": 5,
  "narration_script_id": "hs1-803",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-803`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-901` — Ionising vs non-ionising

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Ionising vs non-ionising |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.54–55 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Ionising vs non-ionising |
| Body / keywords | Ionising: X-ray, CT → dosimeters, shielding · Non-ionising: MRI, ultrasound, laser · MRI: magnet always on, screening every time · X-ray rooms: lead apron, stand behind the shield |
| Word count (excl. title) | 24 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for ionising vs non-ionising, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Ionising: X-ray, CT → dosimeters, shielding · Non-ionising: MRI, ultrasound, laser · MRI: magnet always on, screening every time · X-ray rooms: lead apron, stand behind the shield |
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
| Target seconds | 35 |
| Word count / estimated seconds | 10 words / ≈ 4.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Ionising vs non-ionising. The MRI magnet is always on.

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
  "type": "tabs",
  "id": "hs1-901",
  "title": "Ionising vs non-ionising",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-901",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-901`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-902` — Protection principles

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `matching` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Protection principles |
| Objective(s) | `hs1-o9` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.56 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Protection principles |
| Body / keywords | Justification · Optimisation · Limitation ↔ definitions |
| Word count (excl. title) | 4 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for protection principles. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Justification · Optimisation · Limitation ↔ definitions |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Match each item to the person or step that owns it, then read the feedback.

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
  "id": "hs1-902",
  "title": "Protection principles",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [
    "hs1-o9"
  ],
  "points": 5,
  "narration_script_id": "hs1-902",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-902`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-903` — ALARA

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | ALARA |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.57 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | ALARA |
| Body / keywords | Time · Distance · Shielding around a source icon |
| Word count (excl. title) | 7 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for alara, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `hs1-img-alara` | diagram | hs1-img-alara: Source icon with time/distance/shield labels Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "ALARA: time, distance, shielding." | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Time · Distance · Shielding around a source icon |
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
| Target seconds | 25 |
| Word count / estimated seconds | 8 words / ≈ 3.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Time, distance, shielding — three levers you control.

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
  "id": "hs1-903",
  "title": "ALARA",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-903",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <hs1-img-alara> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-903`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-904` — Staying accountable

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Staying accountable |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.58 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Staying accountable |
| Body / keywords | OSL dosimeter · Lead apron · RSO is your contact |
| Word count (excl. title) | 8 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for staying accountable, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | OSL dosimeter · Lead apron · RSO is your contact |
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
| Target seconds | 25 |
| Word count / estimated seconds | 9 words / ≈ 3.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Wear your badge. The RSO is your contact.

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
  "id": "hs1-904",
  "title": "Staying accountable",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-904",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-904`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-905` — Dose bands

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Dose bands |
| Objective(s) | `hs1-o9` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.59 |
| Depends on Phase 0 | ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Dose bands |
| Body / keywords | "A quarterly OSL reading shows 2.0 mSv. What happens?" → Notification level: you are informed and monitored (values pending B4) |
| Word count (excl. title) | 20 |
| Instruction | Feedback shows the 3 bands table |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for dose bands. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | "A quarterly OSL reading shows 2.0 mSv. What happens?" → Notification level: you are informed and monitored (values pending B4) |
| Build / feedback brief | Feedback shows the 3 bands table |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback shows the 3 bands table |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback shows the 3 bands table |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Decide as you would on shift, then read the feedback.

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
  "id": "hs1-905",
  "title": "Dose bands",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [
    "hs1-o9"
  ],
  "points": 5,
  "narration_script_id": "hs1-905",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-905`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-906` — Laser classes

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `matching` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Laser classes |
| Objective(s) | `hs1-o9` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.61 |
| Depends on Phase 0 | ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Laser classes |
| Body / keywords | 1/1M · 2/2M · 3R · 3B · 4 ↔ hazard (wording per B5) |
| Word count (excl. title) | 11 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for laser classes. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | 1/1M · 2/2M · 3R · 3B · 4 ↔ hazard (wording per B5) |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Match each item to the person or step that owns it, then read the feedback.

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
  "id": "hs1-906",
  "title": "Laser classes",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [
    "hs1-o9"
  ],
  "points": 5,
  "narration_script_id": "hs1-906",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-906`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-907` — Laser hazards & measures

**Status:** `Draft — ready for SME review` · **Section / node:** 9 · Radiation & laser / `hs1-s9` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Laser hazards & measures |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.62–64 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Laser hazards & measures |
| Body / keywords | Eyes (often no pain) · Skin burns · High voltage → Eye protection · Beam management · Control reflections · Training |
| Word count (excl. title) | 15 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for laser hazards & measures, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Eyes (often no pain) · Skin burns · High voltage → Eye protection · Beam management · Control reflections · Training |
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
| Target seconds | 25 |
| Word count / estimated seconds | 15 words / ≈ 6.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Laser eye injuries often don't hurt at first — that's why protection is not optional.

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
  "id": "hs1-907",
  "title": "Laser hazards & measures",
  "section": "9 · Radiation & laser",
  "node_id": "hs1-s9",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-907",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-907`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-950` — "One shift, three plans"

**Status:** `Draft — ready for SME review` · **Section / node:** Capstone & completion / `hs1-s10` · **Type:** `game` · **Scored:** Yes (25 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | "One shift, three plans" |
| Objective(s) | `hs1-o10` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.3, 24, 40, 49 |
| Depends on Phase 0 | ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | "One shift, three plans" |
| Body / keywords | Mixed case: (1) during a busy clinic a cleaner knocks over a large bottle of disinfectant next to an oxygen cylinder → Code Orange or not (D1), move O₂ away; (2) an alarm sounds → which code is announced for … |
| Word count (excl. title) | 38 |
| Instruction | Debrief node lists which plan each decision belonged to |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for "one shift, three plans". Noor + Omar is placed l5. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Noor + Omar · pose char-noor-explaining; char-omar-avatar in node 3 · placement L5 · speaks: Noor + Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-explaining; char-omar-avatar in node 3 at L5.` | illustration | Approved program companion pose char-noor-explaining; char-omar-avatar in node 3 at L5. | own / official My Clinic asset | Noor + Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Mixed case: (1) during a busy clinic a cleaner knocks over a large bottle of disinfectant next to an oxygen cylinder → Code Orange or not (D1), move O₂ away; (2) an alarm sounds → which code is announced for smoke; RACE choice; (3) afterwards you notice the suction unit's label is expired → tag and report. Mechanics: score + 3 lives + 1 hint per node; no timer |
| Build / feedback brief | Debrief node lists which plan each decision belonged to |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 25 |
| Pass rule (scenarios / games) | No separate pass rule stated; 3 lives in the Phase 2 brief. |
| Feedback — correct | Source feedback route: Debrief node lists which plan each decision belonged to |
| Feedback — incorrect | Retry/incorrect feedback route: Debrief node lists which plan each decision belonged to |
| Per-choice feedback (scenarios) | Debrief node lists which plan each decision belonged to |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; 3 lives; retry/score handling is finalised in Phase 4. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR / OMAR |
| Tone | encouraging |
| Target seconds | 20 |
| Word count / estimated seconds | 19 words / ≈ 8.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Play the round, then read the feedback.
>
> OMAR: That is the habit we want from every new colleague.

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
  "type": "game",
  "id": "hs1-950",
  "title": "\"One shift, three plans\"",
  "section": "Capstone & completion",
  "node_id": "hs1-s10",
  "objective_ids": [
    "hs1-o10"
  ],
  "points": 25,
  "narration_script_id": "hs1-950",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-950`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-980` — Show strengths by section

**Status:** `Draft — ready for SME review` · **Section / node:** Capstone & completion / `hs1-s10` · **Type:** `results_breakdown` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Show strengths by section |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Show strengths by section |
| Body / keywords | Sections = objectives hs1-o1…hs1-o10; weak_threshold 70 |
| Word count (excl. title) | 7 |
| Instruction | "Revisit" links to weak sections |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm results panel showing each objective as an HTML progress row, with plain-language next steps and a small companion feedback card. Noor is placed l6 right, half-body. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-success · placement L6 right, half-body · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-success at L6 right, half-body.` | illustration | Approved program companion pose char-noor-success at L6 right, half-body. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Sections = objectives hs1-o1…hs1-o10; weak_threshold 70 |
| Build / feedback brief | "Revisit" links to weak sections |
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
| Tone | supportive |
| Target seconds | 15 |
| Word count / estimated seconds | 29 words / ≈ 12.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Your results are organised by objective. Notice where you were confident, then revisit any section that needs another practical try. Use that insight to choose what to revisit.

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
  "id": "hs1-980",
  "title": "Show strengths by section",
  "section": "Capstone & completion",
  "node_id": "hs1-s10",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-980",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-980`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-981` — Confidence re-check

**Status:** `Draft — ready for SME review` · **Section / node:** Capstone & completion / `hs1-s10` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Confidence re-check |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Confidence re-check |
| Body / keywords | Same question as hs1-002 |
| Word count (excl. title) | 4 |
| Instruction | Reflection: compare with start |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for confidence re-check, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
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
| Items / options / nodes | Same question as hs1-002 |
| Build / feedback brief | Reflection: compare with start |
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
| Tone | reflective |
| Target seconds | 8 |
| Word count / estimated seconds | 19 words / ≈ 8.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: This reflection is not scored. Choose the response that helps you set one intention for your next shift.

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
  "type": "poll",
  "id": "hs1-981",
  "title": "Confidence re-check",
  "section": "Capstone & completion",
  "node_id": "hs1-s10",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-981",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-981`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs1-990` — Completion actions

**Status:** `Draft — ready for SME review` · **Section / node:** Capstone & completion / `hs1-s10` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Completion actions |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.65 |
| Depends on Phase 0 | ⚠ PENDING D14; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Completion actions |
| Body / keywords | ✔ Locate your evacuation route and assembly point · ✔ Save emergency numbers · ✔ Find your nearest eyewash · ✔ Ask your supervisor who your Safety Liaison is · ✔ Sign the acknowledgement (D14) · Contact: Safety & Security … |
| Word count (excl. title) | 29 |
| Instruction | show_score: true |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A confident light closing screen with four short takeaways, the supplied My Clinic logo, and space for the next-module hand-off. Noor + Omar is placed l6. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Noor + Omar · pose char-noor-success + char-omar-avatar-happy · placement L6 · speaks: Noor + Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-success + char-omar-avatar-happy at L6.` | illustration | Approved program companion pose char-noor-success + char-omar-avatar-happy at L6. | own / official My Clinic asset | Noor + Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | ✔ Locate your evacuation route and assembly point · ✔ Save emergency numbers · ✔ Find your nearest eyewash · ✔ Ask your supervisor who your Safety Liaison is · ✔ Sign the acknowledgement (D14) · Contact: Safety & Security Manager |
| Build / feedback brief | show_score: true |
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
| Speaker(s) | NOOR / OMAR |
| Tone | confident |
| Target seconds | 30 |
| Word count / estimated seconds | 45 words / ≈ 19.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you.
>
> OMAR: Carry this practical rule into your next decision.

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
  "id": "hs1-990",
  "title": "Completion actions",
  "section": "Capstone & completion",
  "node_id": "hs1-s10",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs1-990",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D14; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs1-990`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---


## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `hs1-000` | `title_slide` | N | 0 | 7 | 26 | 11 | Draft |
| 2 | `hs1-001` | `content_slide` | N | 0 | 16 | 21 | 9 | Draft |
| 3 | `hs1-002` | `poll` | N | 0 | 13 | 19 | 8 | Draft |
| 4 | `hs1-101` | `content_slide` | N | 0 | 7 | 14 | 6 | Draft |
| 5 | `hs1-102` | `hotspot` | N | 0 | 14 | 12 | 5 | Draft |
| 6 | `hs1-103` | `content_slide` | N | 0 | 13 | 16 | 7 | Draft |
| 7 | `hs1-104` | `matching` | Y | 10 | 7 | 16 | 7 | Draft |
| 8 | `hs1-201` | `flashcards` | N | 0 | 9 | 18 | 8 | Draft |
| 9 | `hs1-202` | `accordion` | N | 0 | 16 | 13 | 6 | Draft |
| 10 | `hs1-203` | `labeled_diagram` | N | 0 | 6 | 11 | 5 | Draft |
| 11 | `hs1-204` | `sorting` | Y | 10 | 9 | 16 | 7 | Draft |
| 12 | `hs1-205` | `decision_scenario` | Y | 15 | 37 | 11 | 5 | Draft |
| 13 | `hs1-206` | `accordion` | N | 0 | 21 | 18 | 8 | Draft |
| 14 | `hs1-301` | `flashcards` | N | 0 | 15 | 17 | 7 | Draft |
| 15 | `hs1-302` | `matching` | Y | 10 | 27 | 16 | 7 | Draft |
| 16 | `hs1-303` | `content_slide` | N | 0 | 15 | 17 | 7 | Draft |
| 17 | `hs1-304` | `sorting` | Y | 5 | 5 | 16 | 7 | Draft |
| 18 | `hs1-305` | `labeled_diagram` | N | 0 | 11 | 18 | 8 | Draft |
| 19 | `hs1-401` | `labeled_diagram` | N | 0 | 14 | 23 | 10 | Draft |
| 20 | `hs1-402` | `sorting` | Y | 5 | 5 | 16 | 7 | Draft |
| 21 | `hs1-403` | `sorting` | Y | 5 | 8 | 16 | 7 | Draft |
| 22 | `hs1-404` | `hotspot` | N | 0 | 20 | 12 | 5 | Draft |
| 23 | `hs1-405` | `drag_drop` | Y | 10 | 20 | 11 | 5 | Draft |
| 24 | `hs1-406` | `tabs` | N | 0 | 14 | 13 | 6 | Draft |
| 25 | `hs1-407` | `mcq` | Y | 5 | 29 | 11 | 5 | Draft |
| 26 | `hs1-408` | `true_false` | Y | 5 | 7 | 11 | 5 | Draft |
| 27 | `hs1-409` | `decision_scenario` | Y | 20 | 38 | 11 | 5 | Draft |
| 28 | `hs1-410` | `content_slide` | N | 0 | 14 | 12 | 5 | Draft |
| 29 | `hs1-501` | `content_slide` | N | 0 | 13 | 16 | 7 | Draft |
| 30 | `hs1-502` | `matching` | Y | 10 | 12 | 16 | 7 | Draft |
| 31 | `hs1-503` | `labeled_diagram` | Y | 10 | 11 | 11 | 5 | Draft |
| 32 | `hs1-504` | `mcq` | Y | 5 | 24 | 11 | 5 | Draft |
| 33 | `hs1-505` | `accordion` | N | 0 | 18 | 9 | 4 | Draft |
| 34 | `hs1-506` | `content_slide` | N | 0 | 13 | 13 | 6 | Draft |
| 35 | `hs1-507` | `decision_scenario` | Y | 15 | 36 | 11 | 5 | Draft |
| 36 | `hs1-508` | `drag_drop` | Y | 10 | 19 | 13 | 6 | Draft |
| 37 | `hs1-601` | `tabs` | N | 0 | 17 | 15 | 6 | Draft |
| 38 | `hs1-602` | `mcq` | Y | 5 | 33 | 11 | 5 | Draft |
| 39 | `hs1-701` | `hotspot` | N | 0 | 22 | 15 | 6 | Draft |
| 40 | `hs1-702` | `mcq` | Y | 5 | 20 | 11 | 5 | Draft |
| 41 | `hs1-801` | `content_slide` | N | 0 | 10 | 12 | 5 | Draft |
| 42 | `hs1-802` | `decision_scenario` | Y | 15 | 37 | 11 | 5 | Draft |
| 43 | `hs1-803` | `true_false` | Y | 5 | 12 | 11 | 5 | Draft |
| 44 | `hs1-901` | `tabs` | N | 0 | 24 | 10 | 4 | Draft |
| 45 | `hs1-902` | `matching` | Y | 5 | 4 | 16 | 7 | Draft |
| 46 | `hs1-903` | `labeled_diagram` | N | 0 | 7 | 8 | 3 | Draft |
| 47 | `hs1-904` | `accordion` | N | 0 | 8 | 9 | 4 | Draft |
| 48 | `hs1-905` | `mcq` | Y | 5 | 20 | 11 | 5 | Draft |
| 49 | `hs1-906` | `matching` | Y | 5 | 11 | 16 | 7 | Draft |
| 50 | `hs1-907` | `content_slide` | N | 0 | 15 | 15 | 6 | Draft |
| 51 | `hs1-950` | `game` | Y | 25 | 38 | 19 | 8 | Draft |
| 52 | `hs1-980` | `results_breakdown` | N | 0 | 7 | 29 | 12 | Draft |
| 53 | `hs1-981` | `poll` | N | 0 | 4 | 19 | 8 | Draft |
| 54 | `hs1-990` | `summary` | N | 0 | 29 | 45 | 19 | Draft |
| | **Totals** | | **24** | **220** | | **814** | **349 ≈ 5.8 min** | Draft |

### Narration authoring gaps

42 of 54 screens are below 70% of their Phase 3 target because generated narration is no longer padded (G11/C20). See [`narration-gaps.md`](narration-gaps.md) for the worklist.

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `hs1-img-corridor` | illustration | Generated file | ai-generated | Yes | Generated 2026-10-14 — SME visual check required before hotspot coordinates are set. |
| `hs1-img-arec` | diagram | Generated file | own | Yes | Generated native SVG. |
| `hs1-img-ert` | diagram | Generated file | own | Yes | Generated native SVG. |
| `hs1-img-triangle` | diagram | Generated file | own | Yes | Generated native SVG. |
| `hs1-img-alara` | diagram | Generated file | own | Yes | Generated native SVG. |
| `hs1-img-nfpa-blank` | diagram | Generated file | own | Yes | Generated native SVG. |
| `hs1-img-nfpa-301w` | diagram | Generated file | own | Yes | Generated native SVG. |
| `hs1-img-8plans` | SVG icon grid | hs1-102 | own | Yes | Planned |
| `hs1-img-arec` | SVG cycle | hs1-203 | own | Yes | Planned |
| `hs1-img-ert` | SVG diagram | hs1-305 | own | Yes | Planned |
| `hs1-img-triangle` | SVG | hs1-401 | own | Yes | Planned |
| `hs1-img-corridor` | illustration | hs1-404 | ai-generated (reviewed) or own | Yes | Planned |
| `hs1-img-ghs-1` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-2` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-3` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-4` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-5` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-6` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-7` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-8` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-ghs-9` | SVG pictograms | hs1-502 | own / public-domain (UN GHS) | Yes | Planned |
| `hs1-img-nfpa-blank` | SVG | hs1-503 | own | Yes | Planned |
| `hs1-img-nfpa-301w` | SVG | hs1-504 | own | Yes | Planned |
| `hs1-img-eyewash` | photo | hs1-506 | own (with permission) | Yes | Planned |
| `hs1-img-treatment-room` | illustration | hs1-701 | ai-generated (reviewed) | Yes | Planned |
| `hs1-img-pump-label` | illustration | hs1-802 | ai-generated (reviewed) | Yes | Planned |
| `hs1-img-alara` | SVG | hs1-903 | own | Yes | Planned |
| `hs1-img-codes-chips` | SVG set | hs1-301 | own | Yes | Planned |
| `char-noor-*` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |
| `char-omar-*` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |
| `hs1-aud-*` | narration audio | all narrated screens | ai-generated (TTS) | Yes | Planned |

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
| 1 | All affected cards | Code Orange threshold | `B1` · Safety Manager | Yes |
| 2 | All affected cards | Code names and extension numbers (11 codes + 2 announcements) | `B2` · Safety Manager | Yes |
| 3 | All affected cards | [Facility Name], [Month Year] placeholders | `B3` · L&D | Yes |
| 4 | All affected cards | Radiation dose limits and bands (2 mSv / 3 months, 20 mSv / year; 1.25 / 1.25–3.75 / > 3.75 mSv) | `B4` · RSO | Yes |
| 5 | All affected cards | Laser class table wording ("3" vs "3R" vs "3B") | `B5` · RSO | Yes |
| 6 | All affected cards | Emergency (red) socket colour and generator timing ("within seconds") | `B6` · Facilities | Yes |
| 7 | All affected cards | Waste segregation bin colours | `B7` · Infection Control / EHS | Yes |
| 8 | All affected cards | Department Safety Liaison list | `B8` · Safety Manager | Yes |
| 9 | All affected cards | Accreditation references (CBAHI chapter name, ISO 45001 rights) | `B9` · Quality / Accreditation | Yes |
| 10 | All affected cards | Completion actions (acknowledgement form, evacuation route, numbers) | `B10` · L&D | Yes |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| `AREC` | A-R-E-C | `hs1-203` |
| `CBAHI` | see-bah-hee | `hs1-001` |
| `ERT` | E-R-T | `hs1-305` |
| `MRI` | M-R-I | `hs1-901` |
| `RACE` | race | `hs1-401` |
| `RSO` | R-S-O | `hs1-904` |
| `SDS` | S-D-S | `hs1-501`, `hs1-505` |

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan (24 scored / 220 points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
