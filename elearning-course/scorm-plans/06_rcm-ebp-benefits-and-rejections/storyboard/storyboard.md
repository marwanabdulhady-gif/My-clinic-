# Storyboard — 06 RCM Part B: New EBP Benefits & Claim-Rejection Analysis

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
| Module | 06 — My Clinic — RCM Part B: New EBP Benefits & Claim-Rejection Analysis |
| Module prefix | `rcmb-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | RCM lead (lead); Payer Relations; Coding lead; Data Protection Officer |
| Audience | Physicians and RCM staff |
| Seat-time budget | ~20 minutes |
| SCORM / completion / pass mark | SCORM 1.2 · viewed_all_and_passed · pass 80% (64 / 80) |
| Scored screens / total points | 7 / 80 (Phase 4 expectation: 7 / 80) |
| Source file | `elearning-course/md/06_rcm-billing-documentation-slides-2026.md` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-14) |
| Module colour | Collaborative burgundy #7C0041 |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | B1–B9; program D4, D5 and D11 |
| Narration reconciliation | Detailed card scripts: 4.7 min; Phase 3 per-screen targets: 4.7 min; Phase 3 rough module estimate: ~5 min. Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review. |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
| `rcmb-o1` | Distinguish benefits added by the new EBP from benefits amended by it. | `rcmb-010` |
| `rcmb-o2` | Apply EBP coverage rules, limits and exclusions to patient requests. | `rcmb-021`, `rcmb-031`, `rcmb-041`, `rcmb-060` |
| `rcmb-o3` | Classify claim rejections by cause and choose the correct rework. | `rcmb-051`, `rcmb-052` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `rcmb-sA` | What changed | `rcmb-000`–`rcmb-001` |
| `rcmb-sB` | Benefits in practice | `rcmb-010`–`rcmb-041` |
| `rcmb-sC` | Reading rejections | `rcmb-050`–`rcmb-052` |
| `rcmb-sD` | Practice & close | `rcmb-060`–`rcmb-091` |

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

### `rcmb-000` — RCM Part B: New EBP Benefits & Claim-Rejection Analysis

**Status:** `Draft — ready for SME review` · **Section / node:** What changed / `rcmb-sA` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 1 |
| Depends on Phase 0 | ⚠ PENDING B1; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | RCM Part B: New EBP Benefits & Claim-Rejection Analysis |
| Body / keywords | "What's new in the EBP — and why claims get rejected" · "RCM Part B" · policy effective date (B1) |
| Word count (excl. title) | 17 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L1 Title |
| Logo | `logo-horizontal-white.png`, 48 px at top-left |
| Visual concept | Official navy title gradient with supplied white My Clinic logo, large Montserrat course title, and a cropped white petal watermark. Omar is placed l1 half-body bottom-right. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `primary` · text `on_primary` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | "What's new in the EBP — and why claims get rejected" · "RCM Part B" · policy effective date (B1) |
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
| Word count / estimated seconds | 31 words / ≈ 13.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Welcome to RCM Part B: New EBP Benefits & Claim-Rejection Analysis. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift.

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
  "id": "rcmb-000",
  "title": "RCM Part B: New EBP Benefits & Claim-Rejection Analysis",
  "section": "What changed",
  "node_id": "rcmb-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-000",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B1; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-000`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-001` — Frame

**Status:** `Draft — ready for SME review` · **Section / node:** What changed / `rcmb-sA` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Frame |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 3, 8 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Frame |
| Body / keywords | The EBP added new benefits and amended others · Coverage depends on the table of benefits and the documentation · Partial coverage ≠ full approval |
| Word count (excl. title) | 22 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for frame, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | The EBP added new benefits and amended others · Coverage depends on the table of benefits and the documentation · Partial coverage ≠ full approval |
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
| Word count / estimated seconds | 73 words / ≈ 31.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Benefits change. Documentation decides whether a covered service is actually paid. Keep the main point connected to a familiar task or conversation. That connection makes the information easier to use when it matters. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role.

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
  "id": "rcmb-001",
  "title": "Frame",
  "section": "What changed",
  "node_id": "rcmb-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-001",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-001`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-010` — Sort the benefits

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Sort the benefits |
| Objective(s) | `rcmb-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 8 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Sort the benefits |
| Body / keywords | Cards: prevention exams · STDs · adult vaccination · home care for inpatients · temporary contraception · telemedicine · menopause/perimenopause cover · kidney transplant · diabetes programme → Added; mental health · optical · congenital anomalies · dental · dialysis … |
| Word count (excl. title) | 28 |
| Instruction | Feedback per card |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for sort the benefits. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `rcmb-img-benefit-icons` | icon | rcmb-img-benefit-icons: Generated native icon sheet; labels remain HTML in the course. | own SVG | A set of generic line icons for health benefits. | No |
| `rcmb-img-benefit-icons` | diagram | rcmb-img-benefit-icons: Line icons per benefit | own SVG | decorative | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Cards: prevention exams · STDs · adult vaccination · home care for inpatients · temporary contraception · telemedicine · menopause/perimenopause cover · kidney transplant · diabetes programme → Added; mental health · optical · congenital anomalies · dental · dialysis limit · weight-loss surgery · OPD co-payment → Amended |
| Build / feedback brief | Feedback per card |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback per card |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback per card |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
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
  "type": "drag_drop",
  "id": "rcmb-010",
  "title": "Sort the benefits",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [
    "rcmb-o1"
  ],
  "points": 10,
  "narration_script_id": "rcmb-010",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-010`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-020` — What's covered

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | What's covered |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 9 |
| Depends on Phase 0 | ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | What's covered |
| Body / keywords | Early exams: mammogram · Pap smear · FIT/colonoscopy · dietary counselling (risk criteria, B7) · FBS/HbA1c · lipids · DEXA · Adult vaccines: Tdap · PCV13 · PPSV23 · influenza · STDs: treatment whatever the mode of infection (list) |
| Word count (excl. title) | 30 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for what's covered, with one open item at a time, navy structure, and a Collaborative burgundy #7C0041 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `rcmb-img-benefit-icons` | icon | rcmb-img-benefit-icons: Generated native icon sheet; labels remain HTML in the course. | own SVG | A set of generic line icons for health benefits. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Early exams: mammogram · Pap smear · FIT/colonoscopy · dietary counselling (risk criteria, B7) · FBS/HbA1c · lipids · DEXA · Adult vaccines: Tdap · PCV13 · PPSV23 · influenza · STDs: treatment whatever the mode of infection (list) |
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
| Word count / estimated seconds | 89 words / ≈ 38.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Prevention is now covered: think of the patient in front of you who is due a screen. Move through the items one at a time and connect each point with a practical response. The aim is to use the information, not just recognise it. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role. Use the principle in context. Keep the next action clear.

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
  "id": "rcmb-020",
  "title": "What's covered",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-020",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-020`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-021` — Apply

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Apply |
| Objective(s) | `rcmb-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 9 |
| Depends on Phase 0 | ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Apply |
| Body / keywords | "A 52-year-old with BMI 32 and high cholesterol asks for help with diet to lower her heart risk." → covered behavioural/dietary consultation; document BMI and risk factors (B7) |
| Word count (excl. title) | 29 |
| Instruction | Distractors explain what's missing |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for apply. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | "A 52-year-old with BMI 32 and high cholesterol asks for help with diet to lower her heart risk." → covered behavioural/dietary consultation; document BMI and risk factors (B7) |
| Build / feedback brief | Distractors explain what's missing |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Distractors explain what's missing |
| Feedback — incorrect | Retry/incorrect feedback route: Distractors explain what's missing |
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
  "id": "rcmb-021",
  "title": "Apply",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [
    "rcmb-o2"
  ],
  "points": 5,
  "narration_script_id": "rcmb-021",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B7; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-021`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-030` — Mental-health benefit

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Mental-health benefit |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 10; script |
| Depends on Phase 0 | ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Mental-health benefit |
| Body / keywords | Included conditions (9) · Excluded: hypnosis, rehabilitation · Limit per policy period (B5) · Pre-authorisation for sub-limit services · Document: indication, link symptoms to a valid psychiatric diagnosis, justify referral |
| Word count (excl. title) | 26 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for mental-health benefit, with one open item at a time, navy structure, and a Collaborative burgundy #7C0041 active-state cue. Noor is placed l3 tip card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | Included conditions (9) · Excluded: hypnosis, rehabilitation · Limit per policy period (B5) · Pre-authorisation for sub-limit services · Document: indication, link symptoms to a valid psychiatric diagnosis, justify referral |
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

> NOOR: Mental-health cover is wider, but it has a limit and needs pre-authorisation for some services. Open one section at a time and pause on the detail that changes what you would do next. That link turns information into a practical response. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision.

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
  "id": "rcmb-030",
  "title": "Mental-health benefit",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-030",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-030`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-031` — Exclusion

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `true_false` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Exclusion |
| Objective(s) | `rcmb-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 10 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Exclusion |
| Body / keywords | "Hypnosis for alcohol use is covered under the mental-health benefit." → False |
| Word count (excl. title) | 11 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for exclusion. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | "Hypnosis for alcohol use is covered under the mental-health benefit." → False |
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
  "type": "true_false",
  "id": "rcmb-031",
  "title": "Exclusion",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [
    "rcmb-o2"
  ],
  "points": 5,
  "narration_script_id": "rcmb-031",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-031`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-040` — Five benefits

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Five benefits |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 11–12 |
| Depends on Phase 0 | ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Five benefits |
| Body / keywords | Home care for inpatients (wound care, IV meds, catheter care) · Telemedicine (MOH-licensed centre, CHI rules) · Diabetes 360° programme (team + specialist visits) · Women's health (menopausal/perimenopausal hormone therapy) + family planning (hormonal contraceptives, IUD) · Kidney transplant (limit … |
| Word count (excl. title) | 35 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for five benefits, with one open item at a time, navy structure, and a Collaborative burgundy #7C0041 active-state cue. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | None. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `rcmb-img-benefit-icons` | icon | rcmb-img-benefit-icons: Generated native icon sheet; labels remain HTML in the course. | own SVG | A set of generic line icons for health benefits. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Home care for inpatients (wound care, IV meds, catheter care) · Telemedicine (MOH-licensed centre, CHI rules) · Diabetes 360° programme (team + specialist visits) · Women's health (menopausal/perimenopausal hormone therapy) + family planning (hormonal contraceptives, IUD) · Kidney transplant (limit, B5) |
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
| Target seconds | 45 |
| Word count / estimated seconds | 102 words / ≈ 43.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Five benefits that change what you can offer at discharge, by phone, for diabetes and for women's health. Use the tabs as a short reference, not a checklist to race through. Notice which detail would guide your next conversation or decision. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role. Use the principle in context. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task. Carry the idea into your next decision. Pause and connect this to your role.

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
  "id": "rcmb-040",
  "title": "Five benefits",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-040",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-040`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-041` — Key condition or limit

**Status:** `Draft — ready for SME review` · **Section / node:** Benefits in practice / `rcmb-sB` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Key condition or limit |
| Objective(s) | `rcmb-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 10–12 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Key condition or limit |
| Body / keywords | Mental health ↔ sub-limit per policy period + pre-auth · Kidney transplant ↔ up to the policy limit · Telemedicine ↔ MOH-licensed centre · Home care ↔ after an inpatient stay (wound/IV/catheter) · Family planning ↔ hormonal contraceptives and IUDs … |
| Word count (excl. title) | 32 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for key condition or limit. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | Mental health ↔ sub-limit per policy period + pre-auth · Kidney transplant ↔ up to the policy limit · Telemedicine ↔ MOH-licensed centre · Home care ↔ after an inpatient stay (wound/IV/catheter) · Family planning ↔ hormonal contraceptives and IUDs · Women's health ↔ menopausal hormone therapy |
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
  "id": "rcmb-041",
  "title": "Key condition or limit",
  "section": "Benefits in practice",
  "node_id": "rcmb-sB",
  "objective_ids": [
    "rcmb-o2"
  ],
  "points": 10,
  "narration_script_id": "rcmb-041",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-041`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-050` — A log

**Status:** `Draft — ready for SME review` · **Section / node:** Reading rejections / `rcmb-sC` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Read a log |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 6 |
| Depends on Phase 0 | ⚠ PENDING B8; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | A log |
| Body / keywords | Rebuilt HTML table, 8 rows, invented claim ids (B8): diagnosis · service · rejection comment. Comments drawn from slide 6: "pain, unspecified" · "fever" · "requires pre-authorisation as per policy" · "consultation within the free follow-up period" · "radiology: two … |
| Word count (excl. title) | 34 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for read a log, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. Omar is placed l3 right column. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-explaining · placement L3 right column · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `rcmb-tbl-log` | diagram | rcmb-tbl-log: Rebuilt rejection rows (B8); invented ids CLM-0001…; no names, dates or providers | own SVG | A log visual. | No |
| `Approved program companion pose char-omar-explaining at L3 right column.` | illustration | Approved program companion pose char-omar-explaining at L3 right column. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Rebuilt HTML table, 8 rows, invented claim ids (B8): diagnosis · service · rejection comment. Comments drawn from slide 6: "pain, unspecified" · "fever" · "requires pre-authorisation as per policy" · "consultation within the free follow-up period" · "radiology: two views" · "no proof of billed service" · "duplicate billing" · "renal panel must include required tests" |
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
| Word count / estimated seconds | 72 words / ≈ 30.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: How to read a rejection comment. Each one tells you what to fix. The first time I read our log I recognised two of my own claims. Notice which part of the information you would need first in practice. Use that as the starting point for a safe, respectful next action. Keep the next action clear. Think of the first detail you would check. Apply the point to a familiar task.

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
  "id": "rcmb-050",
  "title": "A log",
  "section": "Reading rejections",
  "node_id": "rcmb-sC",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-050",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B8; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-050`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-051` — Classify

**Status:** `Draft — ready for SME review` · **Section / node:** Reading rejections / `rcmb-sC` · **Type:** `drag_drop` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Classify |
| Objective(s) | `rcmb-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 6 |
| Depends on Phase 0 | ⚠ PENDING B9; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Classify |
| Body / keywords | The 8 comments → Documentation · Coding · Policy / pre-auth · Timing / follow-up period · Billing process (categories per B9) |
| Word count (excl. title) | 15 |
| Instruction | Feedback explains the cause and the fix |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for classify. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | The 8 comments → Documentation · Coding · Policy / pre-auth · Timing / follow-up period · Billing process (categories per B9) |
| Build / feedback brief | Feedback explains the cause and the fix |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback explains the cause and the fix |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback explains the cause and the fix |
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
  "id": "rcmb-051",
  "title": "Classify",
  "section": "Reading rejections",
  "node_id": "rcmb-sC",
  "objective_ids": [
    "rcmb-o3"
  ],
  "points": 15,
  "narration_script_id": "rcmb-051",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B9; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-051`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-052` — Rework

**Status:** `Draft — ready for SME review` · **Section / node:** Reading rejections / `rcmb-sC` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Rework |
| Objective(s) | `rcmb-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 6; 05 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Rework |
| Body / keywords | Claim rejected: "Fever — non-specific diagnosis". Node 1: resubmit unchanged / bill again / review the note ✔. Node 2: the note shows fever 3 days, dysuria, positive urinalysis → add specific/provisional diagnosis and findings ✔ vs add a second … |
| Word count (excl. title) | 35 |
| Instruction | Feedback ties back to Part A |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Collaborative burgundy #7C0041 progress cue for rework. Omar is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | Claim rejected: "Fever — non-specific diagnosis". Node 1: resubmit unchanged / bill again / review the note ✔. Node 2: the note shows fever 3 days, dysuria, positive urinalysis → add specific/provisional diagnosis and findings ✔ vs add a second random code. Node 3: resubmit with the supporting document ✔ vs new claim (duplicate) |
| Build / feedback brief | Feedback ties back to Part A |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Feedback ties back to Part A |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback ties back to Part A |
| Per-choice feedback (scenarios) | Feedback ties back to Part A |
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
  "type": "decision_scenario",
  "id": "rcmb-052",
  "title": "Rework",
  "section": "Reading rejections",
  "node_id": "rcmb-sC",
  "objective_ids": [
    "rcmb-o3"
  ],
  "points": 15,
  "narration_script_id": "rcmb-052",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-052`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-060` — Covered or not?

**Status:** `Draft — ready for SME review` · **Section / node:** Practice & close / `rcmb-sD` · **Type:** `adaptive_practice` · **Scored:** Yes (20 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Covered or not? |
| Objective(s) | `rcmb-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 8–12 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Covered or not? |
| Body / keywords | Bank of 15 patient requests across all benefits (e.g. adult influenza vaccine; PCOS hormonal panel; telemedicine follow-up from an unlicensed app; IUD insertion; home IV antibiotics after discharge; bipolar disorder management; hypnosis; DEXA for a postmenopausal woman). max_items 8, target_success … |
| Word count (excl. title) | 43 |
| Instruction | Per-item feedback with the rule |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for covered or not?. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | Bank of 15 patient requests across all benefits (e.g. adult influenza vaccine; PCOS hormonal panel; telemedicine follow-up from an unlicensed app; IUD insertion; home IV antibiotics after discharge; bipolar disorder management; hypnosis; DEXA for a postmenopausal woman). max_items 8, target_success 0.7, pass_ratio 0.6 |
| Build / feedback brief | Per-item feedback with the rule |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 20 |
| Pass rule (scenarios / games) | target_success 0 |
| Feedback — correct | Source feedback route: Per-item feedback with the rule |
| Feedback — incorrect | Retry/incorrect feedback route: Per-item feedback with the rule |
| Per-choice feedback (scenarios) | Per-item feedback with the rule |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 23 words / ≈ 9.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The next choice asks you to apply the rule in a workplace situation. Read carefully, then choose. Use the rule you practised.

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
  "type": "adaptive_practice",
  "id": "rcmb-060",
  "title": "Covered or not?",
  "section": "Practice & close",
  "node_id": "rcmb-sD",
  "objective_ids": [
    "rcmb-o2"
  ],
  "points": 20,
  "narration_script_id": "rcmb-060",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-060`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-090` — Results

**Status:** `Draft — ready for SME review` · **Section / node:** Practice & close / `rcmb-sD` · **Type:** `results_breakdown` · **Scored:** No

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
| Body / keywords | rcmb-o1…o3 |
| Word count (excl. title) | 2 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm results panel showing each objective as an HTML progress row, with plain-language next steps and a small companion feedback card. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | rcmb-o1…o3 |
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
  "id": "rcmb-090",
  "title": "Results",
  "section": "Practice & close",
  "node_id": "rcmb-sD",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-090",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-090`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcmb-091` — Close

**Status:** `Draft — ready for SME review` · **Section / node:** Practice & close / `rcmb-sD` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | 14 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Close |
| Body / keywords | Know what's new · Document to the benefit's criteria · Check limits and pre-auth · Rework, don't resubmit · Link: EBP one-page summary (PDF) |
| Word count (excl. title) | 20 |
| Instruction | show_score |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A confident light closing screen with four short takeaways, the supplied My Clinic logo, and space for the next-module hand-off. Omar + Noor is placed l6. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar + Noor · pose char-omar-success + char-noor-avatar-happy · placement L6 · speaks: Omar + Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `rcmb-pdf-ebp` | illustration | rcmb-pdf-ebp: One-page EBP summary from the official document (B3), approved by payer relations | own SVG | Close visual. | No |
| `Approved program companion pose char-omar-success + char-noor-avatar-happy at L6.` | illustration | Approved program companion pose char-omar-success + char-noor-avatar-happy at L6. | own / official My Clinic asset | Omar + Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Know what's new · Document to the benefit's criteria · Check limits and pre-auth · Rework, don't resubmit · Link: EBP one-page summary (PDF) |
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
| Word count / estimated seconds | 50 words / ≈ 21.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you. Use the principle in context.
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
  "id": "rcmb-091",
  "title": "Close",
  "section": "Practice & close",
  "node_id": "rcmb-sD",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcmb-091",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcmb-091`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---


## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `rcmb-000` | `title_slide` | N | 0 | 17 | 31 | 13 | Draft |
| 2 | `rcmb-001` | `content_slide` | N | 0 | 22 | 73 | 31 | Draft |
| 3 | `rcmb-010` | `drag_drop` | Y | 10 | 28 | 24 | 10 | Draft |
| 4 | `rcmb-020` | `tabs` | N | 0 | 30 | 89 | 38 | Draft |
| 5 | `rcmb-021` | `mcq` | Y | 5 | 29 | 18 | 8 | Draft |
| 6 | `rcmb-030` | `accordion` | N | 0 | 26 | 81 | 35 | Draft |
| 7 | `rcmb-031` | `true_false` | Y | 5 | 11 | 18 | 8 | Draft |
| 8 | `rcmb-040` | `tabs` | N | 0 | 35 | 102 | 44 | Draft |
| 9 | `rcmb-041` | `matching` | Y | 10 | 32 | 18 | 8 | Draft |
| 10 | `rcmb-050` | `content_slide` | N | 0 | 34 | 72 | 31 | Draft |
| 11 | `rcmb-051` | `drag_drop` | Y | 15 | 15 | 18 | 8 | Draft |
| 12 | `rcmb-052` | `decision_scenario` | Y | 15 | 35 | 18 | 8 | Draft |
| 13 | `rcmb-060` | `adaptive_practice` | Y | 20 | 43 | 23 | 10 | Draft |
| 14 | `rcmb-090` | `results_breakdown` | N | 0 | 2 | 21 | 9 | Draft |
| 15 | `rcmb-091` | `summary` | N | 0 | 20 | 50 | 21 | Draft |
| | **Totals** | | **7** | **80** | | **656** | **281 ≈ 4.7 min** | Draft |

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `rcmb-img-benefit-icons` | icon | Generated file | own | Yes | Generated native icon sheet; labels remain HTML in the course. |
| `rcmb-img-benefit-icons` | SVG ×12 | rcmb-010, 020, 040 | own | Yes | Planned |
| `rcmb-tbl-log` | HTML table | rcmb-050, 051 | own | n/a | Planned |
| `rcmb-pdf-ebp` | PDF | rcmb-091 | own | n/a | Planned |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
| 1 | All affected cards | Deck date "August 30, 2023" vs file name "2026" | `B1` · RCM lead | Yes |
| 2 | All affected cards | Regulator name CCHI vs CHI | `B2` · RCM lead | Yes |
| 3 | All affected cards | Every benefit on slides 8–12 checked against the official EBP document (text is small and approximate) | `B3` · Payer relations | Yes |
| 4 | All affected cards | Counts: "18 added / 10 amended" vs 10 and 8 headline items | `B4` · Payer relations | Yes |
| 5 | All affected cards | Limits: mental health 50,000 SAR per policy period; kidney transplant 250,000 SAR | `B5` · Payer relations | Yes |
| 6 | All affected cards | Optical cover wording ("life-threatening congenital illness for beneficiaries up to 14 years") | `B6` · Payer relations | Yes |
| 7 | All affected cards | Behavioural/dietary consultation criteria ("BMI > 30 or ≥ 2 risk factors") | `B7` · Payer relations | Yes |
| 8 | All affected cards | Rejection log (slide 6): claim numbers, provider names, dates | `B8` · RCM lead + DPO | Yes |
| 9 | All affected cards | Rejection categories | `B9` · Coding lead | Yes |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| `EBP` | E-B-P | `rcmb-000` |
| `RCM` | R-C-M | `rcmb-000` |

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan (7 scored / 80 points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
