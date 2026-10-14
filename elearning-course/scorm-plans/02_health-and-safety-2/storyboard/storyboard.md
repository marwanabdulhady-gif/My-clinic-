# Storyboard — 02 Safety in Practice: Hazard, Fire & Chemical Lab

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
| Module | 02 — My Clinic — Safety in Practice: Hazard, Fire & Chemical Lab |
| Module prefix | `hs2-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | Safety Manager (lead); EHS; Facilities; Infection Control |
| Audience | All new staff, after module 01 |
| Seat-time budget | ~33 minutes |
| SCORM / completion / pass mark | SCORM 1.2 · viewed_all_and_passed · pass 80% (116 / 145) |
| Scored screens / total points | 13 / 145 (Phase 4 expectation: 13 / 145) |
| Source file | `elearning-course/md/02_health-and-safety-2_safety-hazards-fire-and-chemicals.md` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-14) |
| Module colour | Ambitious teal #008C99 |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | B1–B9; program D1, D2, D11 and D12 |
| Narration reconciliation | Detailed card scripts: 6.7 min; Phase 3 per-screen targets: 6.7 min; Phase 3 rough module estimate: ~8 min. Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review. |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
| `hs2-o1` | Identify common hazards in a work area and estimate risk as likelihood × impact. | `hs2-012`, `hs2-013` |
| `hs2-o2` | Carry out RACE in a simulated Code Red, including a complete alarm call. | `hs2-030` |
| `hs2-o3` | Choose the right evacuation tool and read an evacuation plan legend. | `hs2-031`, `hs2-032` |
| `hs2-o4` | Select the right extinguisher type for a given fire. | `hs2-041` |
| `hs2-o5` | Triage a spill, choose the correct kit and follow the spill-kit procedure. | `hs2-052`, `hs2-053` |
| `hs2-o6` | Use GHS, NFPA and the department chemical register to decide safe handling. | `hs2-061`, `hs2-062`, `hs2-063`, `hs2-064` |
| `hs2-o7` | Recognise prohibited items under hospital regulations. | `hs2-070` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `hs2-sA` | A · Spot the hazard | `hs2-000`–`hs2-013` |
| `hs2-sB` | B · Code Red drill | `hs2-020`–`hs2-030` |
| `hs2-sC` | C · Evacuation | `hs2-031`–`hs2-033` |
| `hs2-sD` | D · Extinguishers | `hs2-040`–`hs2-041` |
| `hs2-sE` | E · Spills | `hs2-050`–`hs2-053` |
| `hs2-sF` | F · Labels & register | `hs2-060`–`hs2-064` |
| `hs2-sG` | G · Regulations & close | `hs2-070`–`hs2-090` |

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

### `hs2-000` — Safety in Practice: Hazard, Fire & Chemical Lab

**Status:** `Draft — ready for SME review` · **Section / node:** A · Spot the hazard / `hs2-sA` · **Type:** `title_slide` · **Scored:** No

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
| Title | Safety in Practice: Hazard, Fire & Chemical Lab |
| Body / keywords | "Safety in Practice" · "Hazard, fire and chemical lab" |
| Word count (excl. title) | 8 |
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
| Items / options / nodes | "Safety in Practice" · "Hazard, fire and chemical lab" |
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
| Target seconds | 12 |
| Word count / estimated seconds | 30 words / ≈ 12.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Welcome to Safety in Practice: Hazard, Fire & Chemical Lab. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift.

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
  "id": "hs2-000",
  "title": "Safety in Practice: Hazard, Fire & Chemical Lab",
  "section": "A · Spot the hazard",
  "node_id": "hs2-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-000",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-000`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-001` — The lab

**Status:** `Draft — ready for SME review` · **Section / node:** A · Spot the hazard / `hs2-sA` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Frame the lab |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.1 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The lab |
| Body / keywords | "Safety = measures that protect life, health and environment." · "Today you practise, not read." |
| Word count (excl. title) | 13 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for frame the lab, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
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
| Items / options / nodes | "Safety = measures that protect life, health and environment." · "Today you practise, not read." |
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

> NOOR: Safety is the habits that protect life, health and environment. Today you practise them. Keep the main point connected to a familiar task or conversation. That connection makes the information easier to use when it matters. Use the principle in context. Keep the next action clear.

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
  "id": "hs2-001",
  "title": "The lab",
  "section": "A · Spot the hazard",
  "node_id": "hs2-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-001",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-001`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-010` — Teach risk scoring

**Status:** `Draft — ready for SME review` · **Section / node:** A · Spot the hazard / `hs2-sA` · **Type:** `worked_example` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Teach risk scoring |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.2; 07 matrix |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Teach risk scoring |
| Body / keywords | Problem: wet floor at the clinic entrance during rain. Steps: (1) name the hazard; (2) likelihood 4 (busy entrance) ; (3) impact 3 (fall injury); (4) risk = 4 × 3 = 12; (5) control: mat + sign + mop … |
| Word count (excl. title) | 34 |
| Instruction | Unscored self-explanation |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A step-by-step worked example for teach risk scoring, using numbered white cards, restrained navy connectors and a single Ambitious teal #008C99 emphasis. |
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
| Items / options / nodes | Problem: wet floor at the clinic entrance during rain. Steps: (1) name the hazard; (2) likelihood 4 (busy entrance) ; (3) impact 3 (fall injury); (4) risk = 4 × 3 = 12; (5) control: mat + sign + mop schedule. Self-explanation prompt: "Why is the sign not enough on its own?" |
| Build / feedback brief | Unscored self-explanation |
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
| Target seconds | 45 |
| Word count / estimated seconds | 103 words / ≈ 44.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Walk through the wet-floor example aloud. Explain why likelihood and impact are scored separately. Follow the example one step at a time, then identify why the next step makes sense. The value is the reasoning you can carry into a similar case. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role.

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
  "type": "worked_example",
  "id": "hs2-010",
  "title": "Teach risk scoring",
  "section": "A · Spot the hazard",
  "node_id": "hs2-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-010",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-010`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-011` — Find the hazards

**Status:** `Draft — ready for SME review` · **Section / node:** A · Spot the hazard / `hs2-sA` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Find the hazards |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.4 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Find the hazards |
| Body / keywords | New illustration of a store room/office (based on p.4 idea). Answer key (6 regions): trailing cables across the walkway · boxes stacked above shoulder height · blocked fire exit / extinguisher · unlabelled bottle on a shelf · liquid spill … |
| Word count (excl. title) | 37 |
| Instruction | Each region explains the hazard and the control |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for find the hazards, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. Noor is placed l3 tip card. |
| edumints layout | n/a (interaction screen) |
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
| `hs2-img-storeroom` | illustration | hs2-img-storeroom: Generated 2026-10-14 — Safety Manager must confirm the six-hotspot answer key before use. | ai-generated, visual QA required | Clinic store room with cables, high boxes, blocked exit, unlabelled bottle, spill by socket and a person on a wheeled chair. | No |
| `Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card.` | illustration | Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

**AI image prompt (recorded production prompt)**

```text
Single clean flat vector illustration for a My Clinic e-learning course. Clinic store room with cables, high boxes, blocked exit, unlabelled bottle, spill by socket and a person on a wheeled chair. Use navy #003867 outlines, white space, soft blue-grey #C0CED9, and Ambitious teal #008C99 as the only value-colour highlight. No text, no letters, no numbers, no logos, no watermark, no patient/staff likeness, and no generated My Clinic mark.
```

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | New illustration of a store room/office (based on p.4 idea). Answer key (6 regions): trailing cables across the walkway · boxes stacked above shoulder height · blocked fire exit / extinguisher · unlabelled bottle on a shelf · liquid spill near a socket · person standing on a wheeled chair to reach a shelf |
| Build / feedback brief | Each region explains the hazard and the control |
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
| Word count / estimated seconds | 37 words / ≈ 15.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Set up the store room. There are six hazards. Open them all. I walked past a blocked exit for a week before I noticed it. Let each marker add context rather than rushing to a conclusion.

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
  "id": "hs2-011",
  "title": "Find the hazards",
  "section": "A · Spot the hazard",
  "node_id": "hs2-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-011",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-011`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-012` — Prioritise

**Status:** `Draft — ready for SME review` · **Section / node:** A · Spot the hazard / `hs2-sA` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Prioritise |
| Objective(s) | `hs2-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.4 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Prioritise |
| Body / keywords | "Which hazard in the room do you report and fix first?" → blocked fire exit (high impact for everyone) |
| Word count (excl. title) | 18 |
| Instruction | Feedback compares likelihood and impact of each option |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for prioritise. |
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
| Items / options / nodes | "Which hazard in the room do you report and fix first?" → blocked fire exit (high impact for everyone) |
| Build / feedback brief | Feedback compares likelihood and impact of each option |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback compares likelihood and impact of each option |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback compares likelihood and impact of each option |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-012",
  "title": "Prioritise",
  "section": "A · Spot the hazard",
  "node_id": "hs2-sA",
  "objective_ids": [
    "hs2-o1"
  ],
  "points": 5,
  "narration_script_id": "hs2-012",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-012`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-013` — Score a risk

**Status:** `Draft — ready for SME review` · **Section / node:** A · Spot the hazard / `hs2-sA` · **Type:** `fill_blank` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Score a risk |
| Objective(s) | `hs2-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.2 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Score a risk |
| Body / keywords | "Likelihood 2, impact 5. Risk score = ___" → accepted: 10 |
| Word count (excl. title) | 8 |
| Instruction | Feedback: "Low likelihood, but severe harm still needs a control." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for score a risk. |
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
| Items / options / nodes | "Likelihood 2, impact 5. Risk score = ___" → accepted: 10 |
| Build / feedback brief | Feedback: "Low likelihood, but severe harm still needs a control." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | 10 Feedback: "Low likelihood, but severe harm still needs a control |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: "Low likelihood, but severe harm still needs a control." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "Low likelihood, but severe harm still needs a control." |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "type": "fill_blank",
  "id": "hs2-013",
  "title": "Score a risk",
  "section": "A · Spot the hazard",
  "node_id": "hs2-sA",
  "objective_ids": [
    "hs2-o1"
  ],
  "points": 5,
  "narration_script_id": "hs2-013",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-013`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-020` — Bilingual code poster

**Status:** `Draft — ready for SME review` · **Section / node:** B · Code Red drill / `hs2-sB` · **Type:** `flashcards` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Bilingual code poster |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.5 |
| Depends on Phase 0 | ⚠ PENDING D2; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Bilingual code poster |
| Body / keywords | 10 colour codes + 2 announcements; front EN + AR name and colour chip, back meaning + extension (D2). Code Blue 2222 |
| Word count (excl. title) | 19 |
| Instruction | Flip |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for bilingual code poster, with one open item at a time, navy structure, and a Ambitious teal #008C99 active-state cue. |
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
| Items / options / nodes | 10 colour codes + 2 announcements; front EN + AR name and colour chip, back meaning + extension (D2). Code Blue 2222 |
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
| Word count / estimated seconds | 58 words / ≈ 24.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The poster on the wall is bilingual. Learn both names. Check your site's extensions. Use the cards for active recall rather than a quick scan. The key is knowing what the term changes in your next action. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task.

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
  "id": "hs2-020",
  "title": "Bilingual code poster",
  "section": "B · Code Red drill",
  "node_id": "hs2-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-020",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D2; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-020`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-030` — Code Red drill

**Status:** `Draft — ready for SME review` · **Section / node:** B · Code Red drill / `hs2-sB` · **Type:** `game` · **Scored:** Yes (25 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Code Red drill |
| Objective(s) | `hs2-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.7–14 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Code Red drill |
| Body / keywords | Setting: afternoon clinic, smoke from a consultation room. Nodes: (1) Rescue — patient in the room vs. phone first; (2) Alarm — shout "Code Red", pull the call point, then choose the complete call script (code type + location + … |
| Word count (excl. title) | 36 |
| Instruction | Each wrong choice shows the poster rule (pp.7–11) as feedback; debrief lists the RACE step for each decision |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for code red drill. Noor + Omar is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Noor + Omar · pose char-noor-avatar (host); char-omar-avatar (node 2) · placement L5 avatar · speaks: Noor + Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-avatar (host); char-omar-avatar (node 2) at L5 avatar.` | illustration | Approved program companion pose char-noor-avatar (host); char-omar-avatar (node 2) at L5 avatar. | own / official My Clinic asset | Noor + Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Setting: afternoon clinic, smoke from a consultation room. Nodes: (1) Rescue — patient in the room vs. phone first; (2) Alarm — shout "Code Red", pull the call point, then choose the complete call script (code type + location + ID & name) from 3 scripts; (3) Contain — select items to remove: O₂ cylinder ✔, alcohol rub ✔, patient file ✘; close the door ✔; (4) small bin fire vs spreading fire → Extinguish (if trained) or Evacuate; (5) evacuate a wheelchair patient from the 1st floor: stairs with evacuation chair vs elevator; (6) arrive at the assembly point → wait for the all-clear. Mechanics: score, 2 lives, 1 text hint per node, no timer |
| Build / feedback brief | Each wrong choice shows the poster rule (pp.7–11) as feedback; debrief lists the RACE step for each decision |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 25 |
| Pass rule (scenarios / games) | No separate pass rule stated; 2 lives in the Phase 2 brief. |
| Feedback — correct | Source feedback route: Each wrong choice shows the poster rule (pp.7–11) as feedback; debrief lists the RACE step for each decision |
| Feedback — incorrect | Retry/incorrect feedback route: Each wrong choice shows the poster rule (pp.7–11) as feedback; debrief lists the RACE step for each decision |
| Per-choice feedback (scenarios) | Each wrong choice shows the poster rule (pp.7–11) as feedback; debrief lists the RACE step for each decision |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; 2 lives; retry/score handling is finalised in Phase 4. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR / OMAR |
| Tone | encouraging |
| Target seconds | 20 |
| Word count / estimated seconds | 50 words / ≈ 21.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Use the rule you practised. Focus on the action that fits. Feedback explains the reasoning after you respond. Use the rule you practised.
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
  "type": "game",
  "id": "hs2-030",
  "title": "Code Red drill",
  "section": "B · Code Red drill",
  "node_id": "hs2-sB",
  "objective_ids": [
    "hs2-o2"
  ],
  "points": 25,
  "narration_script_id": "hs2-030",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-030`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-031` — Tool ↔ patient

**Status:** `Draft — ready for SME review` · **Section / node:** C · Evacuation / `hs2-sC` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Tool ↔ patient |
| Objective(s) | `hs2-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.8, 13 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Tool ↔ patient |
| Body / keywords | Items: "Bedbound adult on the 2nd floor", "Adult who can't walk, stairs needed", "Newborn in the nursery", "Infant carried by staff" → targets: Evacuation mattress · Evacuation chair · Newborn evacuation chair · Baby mover / apron |
| Word count (excl. title) | 32 |
| Instruction | Keyboard pick-and-place |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for tool ↔ patient. |
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
| Items / options / nodes | Items: "Bedbound adult on the 2nd floor", "Adult who can't walk, stairs needed", "Newborn in the nursery", "Infant carried by staff" → targets: Evacuation mattress · Evacuation chair · Newborn evacuation chair · Baby mover / apron |
| Build / feedback brief | Keyboard pick-and-place |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Keyboard pick-and-place |
| Feedback — incorrect | Retry/incorrect feedback route: Keyboard pick-and-place |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-031",
  "title": "Tool ↔ patient",
  "section": "C · Evacuation",
  "node_id": "hs2-sC",
  "objective_ids": [
    "hs2-o3"
  ],
  "points": 10,
  "narration_script_id": "hs2-031",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-031`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-032` — A plan

**Status:** `Draft — ready for SME review` · **Section / node:** C · Evacuation / `hs2-sC` · **Type:** `labeled_diagram` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Read a plan |
| Objective(s) | `hs2-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.12 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | A plan |
| Body / keywords | Generic own floor plan (Zones A–E). Place 6 labels: call point · extinguisher · fire hose reel · fire blanket · evacuation route · assembly point ("you are here" given) |
| Word count (excl. title) | 26 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for read a plan. |
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
| Items / options / nodes | Generic own floor plan (Zones A–E). Place 6 labels: call point · extinguisher · fire hose reel · fire blanket · evacuation route · assembly point ("you are here" given) |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-032",
  "title": "A plan",
  "section": "C · Evacuation",
  "node_id": "hs2-sC",
  "objective_ids": [
    "hs2-o3"
  ],
  "points": 10,
  "narration_script_id": "hs2-032",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-032`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-033` — Assembly points

**Status:** `Draft — ready for SME review` · **Section / node:** C · Evacuation / `hs2-sC` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Assembly points |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.12, 14 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Assembly points |
| Body / keywords | Inside assembly point · Outside assembly point · "Find your unit's plan on the wall today." Horizontal → vertical → full (recap from 01) |
| Word count (excl. title) | 20 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for assembly points, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
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
| Items / options / nodes | Inside assembly point · Outside assembly point · "Find your unit's plan on the wall today." Horizontal → vertical → full (recap from 01) |
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
| Word count / estimated seconds | 59 words / ≈ 25.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Inside vs outside assembly points. Find your unit's plan today. As you read, focus on the decision this information supports in your own role. The aim is a practical next action, not a phrase to memorise. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision.

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
  "id": "hs2-033",
  "title": "Assembly points",
  "section": "C · Evacuation",
  "node_id": "hs2-sC",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-033",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-033`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-040` — The label

**Status:** `Draft — ready for SME review` · **Section / node:** D · Extinguishers / `hs2-sD` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Read the label |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.15–16 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The label |
| Body / keywords | Own photo of a My Clinic dry-powder extinguisher. Regions: safety pin · pressure gauge (needle in green) · class / agent label · instructions panel (PASS) · last inspection tag |
| Word count (excl. title) | 25 |
| Instruction | Each region: what to check |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A high-clarity central visual for read the label, with large keyboard-reachable hotspot markers, a short instruction panel and no text baked into the image. |
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

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Own photo of a My Clinic dry-powder extinguisher. Regions: safety pin · pressure gauge (needle in green) · class / agent label · instructions panel (PASS) · last inspection tag |
| Build / feedback brief | Each region: what to check |
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
| Word count / estimated seconds | 45 words / ≈ 19.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Before you need it, know how to read the label and check the gauge. Explore the marked areas at your own pace, then compare the details you found. Use those details to identify the next practical action. Apply the point to a familiar task.

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
  "id": "hs2-040",
  "title": "The label",
  "section": "D · Extinguishers",
  "node_id": "hs2-sD",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-040",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-040`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-041` — Match the fire

**Status:** `Draft — ready for SME review` · **Section / node:** D · Extinguishers / `hs2-sD` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Match the fire |
| Objective(s) | `hs2-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.17–18 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Match the fire |
| Body / keywords | Scenes: "Sparking computer", "Pan of oil in the staff kitchen", "Burning cardboard", "Spilled solvent on fire" → CO₂ · Wet chemical · Water / ABC powder · Foam |
| Word count (excl. title) | 23 |
| Instruction | Feedback ties agent to class (A, B, C, K) |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for match the fire. |
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
| Items / options / nodes | Scenes: "Sparking computer", "Pan of oil in the staff kitchen", "Burning cardboard", "Spilled solvent on fire" → CO₂ · Wet chemical · Water / ABC powder · Foam |
| Build / feedback brief | Feedback ties agent to class (A, B, C, K) |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback ties agent to class (A, B, C, K) |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback ties agent to class (A, B, C, K) |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-041",
  "title": "Match the fire",
  "section": "D · Extinguishers",
  "node_id": "hs2-sD",
  "objective_ids": [
    "hs2-o4"
  ],
  "points": 10,
  "narration_script_id": "hs2-041",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-041`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-050` — What is HAZMAT; Code Orange

**Status:** `Draft — ready for SME review` · **Section / node:** E · Spills / `hs2-sE` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | What is HAZMAT; Code Orange |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.21–22 |
| Depends on Phase 0 | ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | What is HAZMAT; Code Orange |
| Body / keywords | Definition (p.21) · Code Orange = chemical or biological release · Rule from D1 |
| Word count (excl. title) | 12 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for what is hazmat; code orange, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
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
| Items / options / nodes | Definition (p.21) · Code Orange = chemical or biological release · Rule from D1 |
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
| Word count / estimated seconds | 56 words / ≈ 24 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: HAZMAT is chemical or biological. One clear rule decides Code Orange. Notice which part of the information you would need first in practice. Use that as the starting point for a safe, respectful next action. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task.

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
  "id": "hs2-050",
  "title": "What is HAZMAT; Code Orange",
  "section": "E · Spills",
  "node_id": "hs2-sE",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-050",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-050`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-051` — Two kits

**Status:** `Draft — ready for SME review` · **Section / node:** E · Spills / `hs2-sE` · **Type:** `image_compare` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Two kits |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.28 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Two kits |
| Body / keywords | Before = Chemical spill kit (red case) · After = Biological spill kit (yellow, biohazard) · caption: contents of each |
| Word count (excl. title) | 16 |
| Instruction | Slider |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A paired before-and-after comparison for two kits, with a draggable divider, descriptive HTML captions and a clean light background. |
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
| Items / options / nodes | Before = Chemical spill kit (red case) · After = Biological spill kit (yellow, biohazard) · caption: contents of each |
| Build / feedback brief | Slider |
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
| Word count / estimated seconds | 36 words / ≈ 15.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Two kits, two colours, two jobs. Compare the two views carefully and look for the detail that changes the decision or next action. The contrast is there to make the practical signal easier to spot.

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
  "type": "image_compare",
  "id": "hs2-051",
  "title": "Two kits",
  "section": "E · Spills",
  "node_id": "hs2-sE",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-051",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-051`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-052` — Spill triage

**Status:** `Draft — ready for SME review` · **Section / node:** E · Spills / `hs2-sE` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Spill triage |
| Objective(s) | `hs2-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.22 |
| Depends on Phase 0 | ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Spill triage |
| Body / keywords | 3 nodes: (1) urine sample dropped in the lab corridor → biological kit, no Code Orange; (2) large spill of surface disinfectant above the threshold → Code Orange; (3) small amount of a reagent marked "highly toxic" → Code Orange … |
| Word count (excl. title) | 37 |
| Instruction | Feedback quotes the single rule (D1) |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Ambitious teal #008C99 progress cue for spill triage. Omar is placed l5 avatar. |
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
| `Approved program companion pose char-omar-avatar-neutral → -happy / -concern at L5 avatar.` | illustration | Approved program companion pose char-omar-avatar-neutral → -happy / -concern at L5 avatar. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 3 nodes: (1) urine sample dropped in the lab corridor → biological kit, no Code Orange; (2) large spill of surface disinfectant above the threshold → Code Orange; (3) small amount of a reagent marked "highly toxic" → Code Orange regardless of volume |
| Build / feedback brief | Feedback quotes the single rule (D1) |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Feedback quotes the single rule (D1) |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback quotes the single rule (D1) |
| Per-choice feedback (scenarios) | Feedback quotes the single rule (D1) |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-052",
  "title": "Spill triage",
  "section": "E · Spills",
  "node_id": "hs2-sE",
  "objective_ids": [
    "hs2-o5"
  ],
  "points": 15,
  "narration_script_id": "hs2-052",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING D1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-052`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-053` — Spill-kit procedure

**Status:** `Draft — ready for SME review` · **Section / node:** E · Spills / `hs2-sE` · **Type:** `sorting` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Spill-kit procedure |
| Objective(s) | `hs2-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.29 (authored) |
| Depends on Phase 0 | ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Spill-kit procedure |
| Body / keywords | 7 steps (B4): PPE per SDS → isolate & warn → contain the edges → absorb / neutralise → bag, seal, label → clean & report → restock the kit |
| Word count (excl. title) | 21 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for spill-kit procedure. |
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
| Items / options / nodes | 7 steps (B4): PPE per SDS → isolate & warn → contain the edges → absorb / neutralise → bag, seal, label → clean & report → restock the kit |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-053",
  "title": "Spill-kit procedure",
  "section": "E · Spills",
  "node_id": "hs2-sE",
  "objective_ids": [
    "hs2-o5"
  ],
  "points": 10,
  "narration_script_id": "hs2-053",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-053`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-060` — How to read a register

**Status:** `Draft — ready for SME review` · **Section / node:** F · Labels & register / `hs2-sF` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | How to read a register |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.25 |
| Depends on Phase 0 | ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | How to read a register |
| Body / keywords | Anonymised register table (5 rows, from B5): name · hazard class · purpose · quantity · SDS ✓ · NFPA H/F/R/S. Callouts on the SDS and NFPA columns |
| Word count (excl. title) | 25 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for how to read a register, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
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
| Items / options / nodes | Anonymised register table (5 rows, from B5): name · hazard class · purpose · quantity · SDS ✓ · NFPA H/F/R/S. Callouts on the SDS and NFPA columns |
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
| Word count / estimated seconds | 81 words / ≈ 34.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: Read a register row left to right: what it is, why it's here, is the SDS on file, what the diamond says. As you read, focus on the decision this information supports in your own role. The aim is a practical next action, not a phrase to memorise. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task.

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
  "id": "hs2-060",
  "title": "How to read a register",
  "section": "F · Labels & register",
  "node_id": "hs2-sF",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-060",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-060`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-061` — GHS hazard statements

**Status:** `Draft — ready for SME review` · **Section / node:** F · Labels & register / `hs2-sF` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | GHS hazard statements |
| Objective(s) | `hs2-o6` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.23 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | GHS hazard statements |
| Body / keywords | 9 pairs: pictogram ↔ example hazard text from p.23 (e.g. Flame over circle ↔ "oxidiser — can intensify fire") |
| Word count (excl. title) | 18 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for ghs hazard statements. |
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
| Items / options / nodes | 9 pairs: pictogram ↔ example hazard text from p.23 (e.g. Flame over circle ↔ "oxidiser — can intensify fire") |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-061",
  "title": "GHS hazard statements",
  "section": "F · Labels & register",
  "node_id": "hs2-sF",
  "objective_ids": [
    "hs2-o6"
  ],
  "points": 10,
  "narration_script_id": "hs2-061",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-061`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-062` — Register decision

**Status:** `Draft — ready for SME review` · **Section / node:** F · Labels & register / `hs2-sF` · **Type:** `mcq` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Register decision |
| Objective(s) | `hs2-o6` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.25–26 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Register decision |
| Body / keywords | Row: "Surface disinfectant X — SDS ✘". "You need it for a cleaning task now. What do you do?" → don't use; report the missing SDS to your supervisor / EHS |
| Word count (excl. title) | 27 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for register decision. |
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
| Items / options / nodes | Row: "Surface disinfectant X — SDS ✘". "You need it for a cleaning task now. What do you do?" → don't use; report the missing SDS to your supervisor / EHS |
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
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-062",
  "title": "Register decision",
  "section": "F · Labels & register",
  "node_id": "hs2-sF",
  "objective_ids": [
    "hs2-o6"
  ],
  "points": 10,
  "narration_script_id": "hs2-062",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-062`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-063` — NFPA in practice

**Status:** `Draft — ready for SME review` · **Section / node:** F · Labels & register / `hs2-sF` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | NFPA in practice |
| Objective(s) | `hs2-o6` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.24, 26 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | NFPA in practice |
| Body / keywords | Row shows NFPA 2-3-0. "Where must it be stored?" → approved flammable cabinet, away from heat |
| Word count (excl. title) | 16 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for nfpa in practice. |
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
| Items / options / nodes | Row shows NFPA 2-3-0. "Where must it be stored?" → approved flammable cabinet, away from heat |
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
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-063",
  "title": "NFPA in practice",
  "section": "F · Labels & register",
  "node_id": "hs2-sF",
  "objective_ids": [
    "hs2-o6"
  ],
  "points": 5,
  "narration_script_id": "hs2-063",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-063`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-064` — Chemical store lockout (capstone)

**Status:** `Draft — ready for SME review` · **Section / node:** F · Labels & register / `hs2-sF` · **Type:** `escape_room` · **Scored:** Yes (20 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Chemical store lockout (capstone) |
| Objective(s) | `hs2-o6` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | pp.22–27 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Chemical store lockout (capstone) |
| Body / keywords | Intro: the store door is locked; four checks unlock it. Puzzles: (1) "Health rating of the solvent on the diamond?" → 2; (2) "Which register row is missing its SDS? Enter the row number." → 4; (3) "How many minutes … |
| Word count (excl. title) | 38 |
| Instruction | Debrief explains each answer and where to find it at work |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for chemical store lockout (capstone). Noor is placed l5 avatar beside hint text. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Ambitious teal #008C99 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Noor · pose char-noor-tip (hints) · placement L5 avatar beside hint text · speaks: Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-noor-tip (hints) at L5 avatar beside hint text.` | illustration | Approved program companion pose char-noor-tip (hints) at L5 avatar beside hint text. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Intro: the store door is locked; four checks unlock it. Puzzles: (1) "Health rating of the solvent on the diamond?" → 2; (2) "Which register row is missing its SDS? Enter the row number." → 4; (3) "How many minutes do you flush eyes after a splash?" → 15 (aliases 15 minutes, fifteen); (4) "Which code do you call for this spill (photo + volume)?" → orange / code orange. Lives 3; one text hint each |
| Build / feedback brief | Debrief explains each answer and where to find it at work |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | 15 minutes, fifteen |
| Points | 20 |
| Pass rule (scenarios / games) | No separate pass rule stated; Lives 3 in the Phase 2 brief. |
| Feedback — correct | Source feedback route: Debrief explains each answer and where to find it at work |
| Feedback — incorrect | Retry/incorrect feedback route: Debrief explains each answer and where to find it at work |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | One text hint per puzzle; Phase 2 specifies the count, while final hint wording needs the approved build brief. |
| Retry / lives | Untimed and keyboard-operable; Lives 3; retry/score handling is finalised in Phase 4. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 36 words / ≈ 15.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Focus on the action that fits. Feedback explains the reasoning after you respond. Use the rule you practised.

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
  "type": "escape_room",
  "id": "hs2-064",
  "title": "Chemical store lockout (capstone)",
  "section": "F · Labels & register",
  "node_id": "hs2-sF",
  "objective_ids": [
    "hs2-o6"
  ],
  "points": 20,
  "narration_script_id": "hs2-064",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-064`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-070` — Allowed or prohibited?

**Status:** `Draft — ready for SME review` · **Section / node:** G · Regulations & close / `hs2-sG` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Allowed or prohibited? |
| Objective(s) | `hs2-o7` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.30; 01 p.30 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Allowed or prohibited? |
| Body / keywords | Items: scented candle · personal fan heater · extension cord from home · e-cigarette · Facilities-approved power strip · BME-tagged suction unit · reheating lunch for 10 minutes · kettle in the staff pantry (approved) → Allowed / Prohibited (union … |
| Word count (excl. title) | 31 |
| Instruction | Feedback cites the fire risk |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Ambitious teal #008C99 progress cue for allowed or prohibited?. |
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
| Items / options / nodes | Items: scented candle · personal fan heater · extension cord from home · e-cigarette · Facilities-approved power strip · BME-tagged suction unit · reheating lunch for 10 minutes · kettle in the staff pantry (approved) → Allowed / Prohibited (union list, Phase 0 §3; approved items confirmed by Safety Manager) |
| Build / feedback brief | Feedback cites the fire risk |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback cites the fire risk |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback cites the fire risk |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 18 words / ≈ 7.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose.

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
  "id": "hs2-070",
  "title": "Allowed or prohibited?",
  "section": "G · Regulations & close",
  "node_id": "hs2-sG",
  "objective_ids": [
    "hs2-o7"
  ],
  "points": 10,
  "narration_script_id": "hs2-070",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-070`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-080` — Per-objective results

**Status:** `Draft — ready for SME review` · **Section / node:** G · Regulations & close / `hs2-sG` · **Type:** `results_breakdown` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Per-objective results |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Per-objective results |
| Body / keywords | hs2-o1…o7, weak below 70% |
| Word count (excl. title) | 5 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm results panel showing each objective as an HTML progress row, with plain-language next steps and a small companion feedback card. |
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
| Items / options / nodes | hs2-o1…o7, weak below 70% |
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
| Tone | supportive |
| Target seconds | 12 |
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
  "id": "hs2-080",
  "title": "Per-objective results",
  "section": "G · Regulations & close",
  "node_id": "hs2-sG",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-080",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-080`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-081` — Commit

**Status:** `Draft — ready for SME review` · **Section / node:** G · Regulations & close / `hs2-sG` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Commit |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | — |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Commit |
| Body / keywords | "Name one hazard you'll check in your own area this week." |
| Word count (excl. title) | 11 |
| Instruction | Reflection text |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for commit, using a navy header, concise keyword cards and one Ambitious teal #008C99 highlight. |
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
| Items / options / nodes | "Name one hazard you'll check in your own area this week." |
| Build / feedback brief | Reflection text |
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
  "id": "hs2-081",
  "title": "Commit",
  "section": "G · Regulations & close",
  "node_id": "hs2-sG",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-081",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-081`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `hs2-090` — Close

**Status:** `Draft — ready for SME review` · **Section / node:** G · Regulations & close / `hs2-sG` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | p.31 |
| Depends on Phase 0 | ⚠ PENDING B9; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Close |
| Body / keywords | What you practised · Contact: Safety & Security (extension B9) · Next: module 04 / your unit's drill schedule |
| Word count (excl. title) | 15 |
| Instruction | n/a — informational screen. |

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
| Items / options / nodes | What you practised · Contact: Safety & Security (extension B9) · Next: module 04 / your unit's drill schedule |
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
| Speaker(s) | NOOR / OMAR |
| Tone | confident |
| Target seconds | 20 |
| Word count / estimated seconds | 52 words / ≈ 22.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> NOOR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you. Pause and connect this to your role.
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
  "id": "hs2-090",
  "title": "Close",
  "section": "G · Regulations & close",
  "node_id": "hs2-sG",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "hs2-090",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B9; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `hs2-090`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---


## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `hs2-000` | `title_slide` | N | 0 | 8 | 30 | 13 | Draft |
| 2 | `hs2-001` | `content_slide` | N | 0 | 13 | 47 | 20 | Draft |
| 3 | `hs2-010` | `worked_example` | N | 0 | 34 | 103 | 44 | Draft |
| 4 | `hs2-011` | `hotspot` | N | 0 | 37 | 37 | 16 | Draft |
| 5 | `hs2-012` | `mcq` | Y | 5 | 18 | 18 | 8 | Draft |
| 6 | `hs2-013` | `fill_blank` | Y | 5 | 8 | 18 | 8 | Draft |
| 7 | `hs2-020` | `flashcards` | N | 0 | 19 | 58 | 25 | Draft |
| 8 | `hs2-030` | `game` | Y | 25 | 36 | 50 | 21 | Draft |
| 9 | `hs2-031` | `drag_drop` | Y | 10 | 32 | 18 | 8 | Draft |
| 10 | `hs2-032` | `labeled_diagram` | Y | 10 | 26 | 18 | 8 | Draft |
| 11 | `hs2-033` | `content_slide` | N | 0 | 20 | 59 | 25 | Draft |
| 12 | `hs2-040` | `hotspot` | N | 0 | 25 | 45 | 19 | Draft |
| 13 | `hs2-041` | `drag_drop` | Y | 10 | 23 | 18 | 8 | Draft |
| 14 | `hs2-050` | `content_slide` | N | 0 | 12 | 56 | 24 | Draft |
| 15 | `hs2-051` | `image_compare` | N | 0 | 16 | 36 | 15 | Draft |
| 16 | `hs2-052` | `decision_scenario` | Y | 15 | 37 | 18 | 8 | Draft |
| 17 | `hs2-053` | `sorting` | Y | 10 | 21 | 18 | 8 | Draft |
| 18 | `hs2-060` | `content_slide` | N | 0 | 25 | 81 | 35 | Draft |
| 19 | `hs2-061` | `matching` | Y | 10 | 18 | 18 | 8 | Draft |
| 20 | `hs2-062` | `mcq` | Y | 10 | 27 | 18 | 8 | Draft |
| 21 | `hs2-063` | `mcq` | Y | 5 | 16 | 18 | 8 | Draft |
| 22 | `hs2-064` | `escape_room` | Y | 20 | 38 | 36 | 15 | Draft |
| 23 | `hs2-070` | `drag_drop` | Y | 10 | 31 | 18 | 8 | Draft |
| 24 | `hs2-080` | `results_breakdown` | N | 0 | 5 | 29 | 12 | Draft |
| 25 | `hs2-081` | `poll` | N | 0 | 11 | 19 | 8 | Draft |
| 26 | `hs2-090` | `summary` | N | 0 | 15 | 52 | 22 | Draft |
| | **Totals** | | **13** | **145** | | **936** | **401 ≈ 6.7 min** | Draft |

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `hs2-img-storeroom` | illustration | Generated file | ai-generated | Yes | Generated 2026-10-14 — Safety Manager must confirm the six-hotspot answer key before use. |
| `hs2-img-floorplan` | diagram | Generated file | own | Yes | Generated native generic floor-plan SVG; never a real floor plan. |
| `hs2-img-nfpa-230` | diagram | Generated file | own | Yes | Generated native SVG. |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
| 1 | All affected cards | Code Orange threshold ("⚠ PENDING 1 L minor" vs " 500 mL Code Orange") | `B1` · Safety Manager | Yes |
| 2 | All affected cards | Extension "5555" placeholder on the bilingual code table | `B2` · Safety Manager + Switchboard | Yes |
| 3 | All affected cards | "First Clinic" template / other author in PDF metadata | `B3` · Safety Manager | Yes |
| 4 | All affected cards | Spill-kit procedure page is blank | `B4` · EHS | Yes |
| 5 | All affected cards | Chemical register example (Radiology, Sep 2025): product names, volumes, NFPA ratings small and partly unreadable | `B5` · EHS | Yes |
| 6 | All affected cards | Hazard-spotting picture has no answer key | `B6` · Safety Manager | Yes |
| 7 | All affected cards | Facility evacuation floor plan (the sample map is generic) | `B7` · Safety Manager | Yes |
| 8 | All affected cards | Assembly point signs (inside / outside) | `B8` · Safety Manager | Yes |
| 9 | All affected cards | Empty contact boxes on the closing page | `B9` · Safety Manager | Yes |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| `HAZMAT` | haz-mat | `hs2-050` |
| `SDS` | S-D-S | `hs2-060` |

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan (13 scored / 145 points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
