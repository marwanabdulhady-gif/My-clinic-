# Storyboard — 05 RCM Part A: Documentation & ICD-10 Coding That Gets Approved

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
| Module | 05 — My Clinic — RCM Part A: Documentation & ICD-10 Coding That Gets Approved |
| Module prefix | `rcma-` |
| Storyboard version | `v0.2` |
| Author | Arena agent — production-documentation pass |
| Date | 2026-10-15 |
| Status | `Draft — ready for SME review; blocked from production by open source-lock items` |
| SME reviewer (role) | RCM lead (lead); Coding lead; Payer Relations; Medical Director |
| Audience | Physicians and dentists |
| Seat-time budget | ~25 minutes |
| SCORM / completion / pass mark | SCORM 1.2 · viewed_all_and_passed · pass 80% (80 / 100) |
| Scored screens / total points | 10 / 100 (Phase 4 expectation: 10 / 100) |
| Source file | `elearning-course/md/05_rcm-billing-documentation-script.md` |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-15) |
| Module colour | Collaborative burgundy #7C0041 |
| Theme | Official `brand-kit.json` plus the lint adapter `brand-kit.edumints.json`; Montserrat; supplied logo PNGs only |
| Phase 0 items still open | B1–B10; program D4 and D11 |
| Narration reconciliation | Detailed card scripts: 2.3 min; Phase 3 per-screen targets: 6.4 min; Phase 3 rough module estimate: ~8 min. Use the detailed per-screen targets for production timing and reconcile the older rough module estimate at SME review. The difference is not padded with generated sentences (G11/C20): [`narration-gaps.md`](narration-gaps.md) lists the 16 screens that need authored prose. |

### Production guardrails

- The supplied client logo remains a supplied PNG on every screen. It is **never** generated, redrawn, or included in an AI-image prompt.
- `⚠ PENDING` means an owner has not approved a source fact. Keep it in the editable build text until Phase 0 closes.
- The EHR source video and its withheld frames are **not** reused. Module 08 waits for test-environment captures and DPO approval.
- Generated visuals are concept assets only until the named SME checks factual details, especially interaction hotspots and physical equipment.

### Objectives covered

| Objective id | Objective | Assessed by |
|---|---|---|
| `rcma-o1` | Document a complete, medically necessary clinical picture. | `rcma-012`, `rcma-013` |
| `rcma-o2` | Select a specific, covered ICD-10 code, using a provisional diagnosis when justified. | `rcma-021`, `rcma-023` |
| `rcma-o3` | Avoid defensive medicine and unjustified early repetition of tests. | `rcma-031`, `rcma-032`, `rcma-033` |
| `rcma-o4` | Classify rejection causes and apply coverage awareness. | `rcma-040`, `rcma-042` |
| `rcma-o5` | Improve a weak consultation note so that it is clear, strong and defensible. | `rcma-050` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `rcma-sA` | Why it matters | `rcma-000`–`rcma-002` |
| `rcma-sB` | Documentation strategy | `rcma-010`–`rcma-013` |
| `rcma-sC` | ICD-10 coding | `rcma-020`–`rcma-023` |
| `rcma-sD` | Defensive medicine & ordering | `rcma-030`–`rcma-033` |
| `rcma-sE` | Rejections & coverage | `rcma-040`–`rcma-042` |
| `rcma-sF` | Fix the note | `rcma-050`–`rcma-091` |

### Proposed changes

None. The source Phase 2 ids, order, screen types and scoring allocation are retained exactly. Any
change must be proposed in Phase 2/4 before a build starts.

---

## B. Screen cards

### `rcma-000` — RCM Part A: Documentation & Coding

**Status:** `Draft — ready for SME review` · **Section / node:** Why it matters / `rcma-sA` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Slide 1 |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | RCM Part A: Documentation & Coding |
| Body / keywords | "Documentation & coding that gets approved" · "RCM Part A" |
| Word count (excl. title) | 8 |
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
| Items / options / nodes | "Documentation & coding that gets approved" · "RCM Part A" |
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

> OMAR: Welcome to RCM Part A: Documentation & Coding. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift.

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
  "id": "rcma-000",
  "title": "RCM Part A: Documentation & Coding",
  "section": "Why it matters",
  "node_id": "rcma-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-000",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-000`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-001` — The core idea

**Status:** `Draft — ready for SME review` · **Section / node:** Why it matters / `rcma-sA` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | The core idea |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Physician responsibility |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The core idea |
| Body / keywords | "The payer doesn't see your patient. The payer sees your note." · Clinical decision + documentation + coding = optimised payment |
| Word count (excl. title) | 17 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for the core idea, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. Omar is placed l3 right column. |
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
| `rcma-img-reviewer` | diagram | rcma-img-reviewer: Generated native SVG. | own SVG, final content review required | A reviewer sees a written note rather than the patient encounter. | No |
| `Approved program companion pose char-omar-explaining at L3 right column.` | illustration | Approved program companion pose char-omar-explaining at L3 right column. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | "The payer doesn't see your patient. The payer sees your note." · Clinical decision + documentation + coding = optimised payment |
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
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: The reviewer only has your note. Good documentation protects the patient, you and the clinic.

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
  "id": "rcma-001",
  "title": "The core idea",
  "section": "Why it matters",
  "node_id": "rcma-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-001",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <rcma-img-reviewer> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-001`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-002` — Productive failure

**Status:** `Draft — ready for SME review` · **Section / node:** Why it matters / `rcma-sA` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Productive failure |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Common errors |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Productive failure |
| Body / keywords | "What do you think is the #1 cause of rejections at My Clinic?" (4 causes) |
| Word count (excl. title) | 15 |
| Instruction | Reflection: "Hold that thought — we'll check it later." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for productive failure, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
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
| Items / options / nodes | "What do you think is the #1 cause of rejections at My Clinic?" (4 causes) |
| Build / feedback brief | Reflection: "Hold that thought — we'll check it later." |
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
| Tone | reflective |
| Target seconds | 8 |
| Word count / estimated seconds | 19 words / ≈ 8.1 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: This reflection is not scored. Choose the response that helps you set one intention for your next shift.

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
  "id": "rcma-002",
  "title": "Productive failure",
  "section": "Why it matters",
  "node_id": "rcma-sA",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-002",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-002`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-010` — Always / Avoid

**Status:** `Draft — ready for SME review` · **Section / node:** Documentation strategy / `rcma-sB` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Always / Avoid |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Documentation strategy |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Always / Avoid |
| Body / keywords | Always: chief complaint & HPI · relevant findings · link symptoms to the working diagnosis · labs/imaging when needed · Avoid: vague notes · diagnosis without support · copy-paste · "fatigue only", "body pain" |
| Word count (excl. title) | 27 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A white content stage for always / avoid, with one open item at a time, navy structure, and a Collaborative burgundy #7C0041 active-state cue. |
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
| Items / options / nodes | Always: chief complaint & HPI · relevant findings · link symptoms to the working diagnosis · labs/imaging when needed · Avoid: vague notes · diagnosis without support · copy-paste · "fatigue only", "body pain" |
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
| Target seconds | 35 |
| Word count / estimated seconds | 8 words / ≈ 3.4 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: What always goes in, what never should.

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
  "id": "rcma-010",
  "title": "Always / Avoid",
  "section": "Documentation strategy",
  "node_id": "rcma-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-010",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-010`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-011` — Weak vs strong

**Status:** `Draft — ready for SME review` · **Section / node:** Documentation strategy / `rcma-sB` · **Type:** `image_compare` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Weak vs strong |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Medical necessity |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Weak vs strong |
| Body / keywords | Before: "Patient given IV fluids." · After: "Dehydration signs (HR 112, dry mucosa) — IV fluids started for stabilisation." Rendered as two note cards (SVG) |
| Word count (excl. title) | 23 |
| Instruction | Slider; caption: same treatment, different outcome |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A paired before-and-after comparison for weak vs strong, with a draggable divider, descriptive HTML captions and a clean light background. Noor is placed l3 tip card. |
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
| `rcma-img-note-weak` | diagram | rcma-img-note-weak: Generated native SVG using fictional teaching text. | own SVG, final content review required | Weak generic clinical note stating only that IV fluids were given. | No |
| `rcma-img-note-strong` | diagram | rcma-img-note-strong: Generated native SVG using fictional teaching text. | own SVG, final content review required | Stronger generic clinical note linking dehydration signs to IV fluids. | No |
| `-strong` | diagram | -strong: Two identical-size EHR-style note cards (generic, no vendor UI), weak vs strong text Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | "Weak note: patient given IV fluids." / "Strong note: dehydration signs, IV fluids for stabilisation." | No |
| `Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card.` | illustration | Approved program companion pose char-noor-avatar-neutral + tip card at L3 tip card. | own / official My Clinic asset | Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Before: "Patient given IV fluids." · After: "Dehydration signs (HR 112, dry mucosa) — IV fluids started for stabilisation." Rendered as two note cards (SVG) |
| Build / feedback brief | Slider; caption: same treatment, different outcome |
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

> NOOR: Same patient, same fluids. One note gets paid.

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
  "id": "rcma-011",
  "title": "Weak vs strong",
  "section": "Documentation strategy",
  "node_id": "rcma-sB",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-011",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <rcma-img-note-weak> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <-strong> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-011`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-012` — The full clinical picture

**Status:** `Draft — ready for SME review` · **Section / node:** Documentation strategy / `rcma-sB` · **Type:** `sorting` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | The full clinical picture |
| Objective(s) | `rcma-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Full history |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The full clinical picture |
| Body / keywords | Order: Chief complaint → HPI → relevant past history → clinical findings → assessment → plan with duration & follow-up |
| Word count (excl. title) | 14 |
| Instruction | Feedback: "Good documentation tells a story, not just a diagnosis." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for the full clinical picture. |
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
| Items / options / nodes | Order: Chief complaint → HPI → relevant past history → clinical findings → assessment → plan with duration & follow-up |
| Build / feedback brief | Feedback: "Good documentation tells a story, not just a diagnosis." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: "Good documentation tells a story, not just a diagnosis." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "Good documentation tells a story, not just a diagnosis." |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Put the steps in the order you would follow at work, then read the feedback.

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
  "id": "rcma-012",
  "title": "The full clinical picture",
  "section": "Documentation strategy",
  "node_id": "rcma-sB",
  "objective_ids": [
    "rcma-o1"
  ],
  "points": 10,
  "narration_script_id": "rcma-012",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-012`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-013` — Medical necessity

**Status:** `Draft — ready for SME review` · **Section / node:** Documentation strategy / `rcma-sB` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Medical necessity |
| Objective(s) | `rcma-o1` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Medical necessity |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Medical necessity |
| Body / keywords | "Which note best justifies a CBC?" options: "Routine CBC" / "Fatigue" / "Fatigue for 6 weeks, pallor, menorrhagia — rule out anaemia" ✔ / "Patient requested blood test" |
| Word count (excl. title) | 23 |
| Instruction | Feedback explains what the reviewer asks: why was this done? |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for medical necessity. |
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
| Items / options / nodes | "Which note best justifies a CBC?" options: "Routine CBC" / "Fatigue" / "Fatigue for 6 weeks, pallor, menorrhagia — rule out anaemia" ✔ / "Patient requested blood test" |
| Build / feedback brief | Feedback explains what the reviewer asks: why was this done? |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback explains what the reviewer asks: why was this done? |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback explains what the reviewer asks: why was this done? |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Decide as you would on shift, then read the feedback.

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
  "id": "rcma-013",
  "title": "Medical necessity",
  "section": "Documentation strategy",
  "node_id": "rcma-sB",
  "objective_ids": [
    "rcma-o1"
  ],
  "points": 5,
  "narration_script_id": "rcma-013",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-013`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-020` — Coding is clinical translation

**Status:** `Draft — ready for SME review` · **Section / node:** ICD-10 coding / `rcma-sC` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Coding is clinical translation |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | ICD-10 core |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Coding is clinical translation |
| Body / keywords | Primary = main condition treated · Secondary = complexity · Specific code = higher acceptance · #1 rejection cause: non-specific symptom coding |
| Word count (excl. title) | 16 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for coding is clinical translation, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. |
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
| Items / options / nodes | Primary = main condition treated · Secondary = complexity · Specific code = higher acceptance · #1 rejection cause: non-specific symptom coding |
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
| Target seconds | 35 |
| Word count / estimated seconds | 9 words / ≈ 3.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Coding is clinical translation. Specific codes get accepted.

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
  "id": "rcma-020",
  "title": "Coding is clinical translation",
  "section": "ICD-10 coding",
  "node_id": "rcma-sC",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-020",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-020`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-021` — Symptom → supported diagnosis

**Status:** `Draft — ready for SME review` · **Section / node:** ICD-10 coding / `rcma-sC` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Symptom → supported diagnosis |
| Objective(s) | `rcma-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | ICD-10 core |
| Depends on Phase 0 | ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Symptom → supported diagnosis |
| Body / keywords | Presentations ↔ codes (final codes per B4): "Vomiting + diarrhoea, 2 days, dehydration" ↔ gastroenteritis code · "Sore throat, fever, tonsillar exudate" ↔ J03 Acute tonsillitis · "Headache, BP 168/102 on two readings" ↔ I10 Hypertension · "Polyuria, HbA1c 8.1%" … |
| Word count (excl. title) | 34 |
| Instruction | Feedback: "Don't stop at the symptom." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for symptom → supported diagnosis. |
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
| Items / options / nodes | Presentations ↔ codes (final codes per B4): "Vomiting + diarrhoea, 2 days, dehydration" ↔ gastroenteritis code · "Sore throat, fever, tonsillar exudate" ↔ J03 Acute tonsillitis · "Headache, BP 168/102 on two readings" ↔ I10 Hypertension · "Polyuria, HbA1c 8.1%" ↔ E11 Type 2 diabetes |
| Build / feedback brief | Feedback: "Don't stop at the symptom." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: "Don't stop at the symptom." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "Don't stop at the symptom." |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Match each item to the person or step that owns it, then read the feedback.

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
  "id": "rcma-021",
  "title": "Symptom → supported diagnosis",
  "section": "ICD-10 coding",
  "node_id": "rcma-sC",
  "objective_ids": [
    "rcma-o2"
  ],
  "points": 10,
  "narration_script_id": "rcma-021",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B4; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-021`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-022` — Provisional diagnosis

**Status:** `Draft — ready for SME review` · **Section / node:** ICD-10 coding / `rcma-sC` · **Type:** `worked_example` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Provisional diagnosis |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Golden tip; Professional diagnosis |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Provisional diagnosis |
| Body / keywords | Fever 3 days + dysuria + suprapubic pain → urinalysis and culture ordered → document a provisional diagnosis linked to the findings → confirm or change when results return. Self-explanation: "Why is a provisional diagnosis better than 'fever' here?" |
| Word count (excl. title) | 34 |
| Instruction | Unscored |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A step-by-step worked example for provisional diagnosis, using numbered white cards, restrained navy connectors and a single Collaborative burgundy #7C0041 emphasis. |
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
| Items / options / nodes | Fever 3 days + dysuria + suprapubic pain → urinalysis and culture ordered → document a provisional diagnosis linked to the findings → confirm or change when results return. Self-explanation: "Why is a provisional diagnosis better than 'fever' here?" |
| Build / feedback brief | Unscored |
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
| Word count / estimated seconds | 17 words / ≈ 7.3 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Follow the example one step at a time, then identify why the next step makes sense.

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
  "id": "rcma-022",
  "title": "Provisional diagnosis",
  "section": "ICD-10 coding",
  "node_id": "rcma-sC",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-022",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-022`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-023` — Covered or not as primary?

**Status:** `Draft — ready for SME review` · **Section / node:** ICD-10 coding / `rcma-sC` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Covered or not as primary? |
| Objective(s) | `rcma-o2` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Uncovered codes |
| Depends on Phase 0 | ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Covered or not as primary? |
| Body / keywords | Items: E66 Obesity (BMI 31) · L70 Acne · L66 Hair loss · L21 Seborrhoeic dermatitis · N97 Female infertility · General check-up · J03 Acute tonsillitis · E11 Type 2 diabetes · Obesity with BMI 42 referred for bariatric … |
| Word count (excl. title) | 32 |
| Instruction | Feedback: "Link to a covered condition when it truly exists, or don't use it as the main diagnosis." |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for covered or not as primary?. |
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
| Items / options / nodes | Items: E66 Obesity (BMI 31) · L70 Acne · L66 Hair loss · L21 Seborrhoeic dermatitis · N97 Female infertility · General check-up · J03 Acute tonsillitis · E11 Type 2 diabetes · Obesity with BMI 42 referred for bariatric surgery (B5) → Avoid as primary (uncovered) / Covered when clinically supported |
| Build / feedback brief | Feedback: "Link to a covered condition when it truly exists, or don't use it as the main diagnosis." |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: "Link to a covered condition when it truly exists, or don't use it as the main diagnosis." |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: "Link to a covered condition when it truly exists, or don't use it as the main diagnosis." |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Place each item where it belongs, then read the feedback.

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
  "id": "rcma-023",
  "title": "Covered or not as primary?",
  "section": "ICD-10 coding",
  "node_id": "rcma-sC",
  "objective_ids": [
    "rcma-o2"
  ],
  "points": 10,
  "narration_script_id": "rcma-023",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B5; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-023`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-030` — More tests ≠ better care

**Status:** `Draft — ready for SME review` · **Section / node:** Defensive medicine & ordering / `rcma-sD` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | More tests ≠ better care |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Defensive medicine; Excessive ordering |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | More tests ≠ better care |
| Body / keywords | Follow initial work-up protocols · No supplements without indication · Repeat only at evidence-based intervals · If you deviate, document why |
| Word count (excl. title) | 18 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for more tests ≠ better care, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. |
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
| Items / options / nodes | Follow initial work-up protocols · No supplements without indication · Repeat only at evidence-based intervals · If you deviate, document why |
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
| Target seconds | 35 |
| Word count / estimated seconds | 13 words / ≈ 5.6 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Defensive medicine feels safe but gets rejected. Follow work-up protocols, document deviations.

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
  "id": "rcma-030",
  "title": "More tests ≠ better care",
  "section": "Defensive medicine & ordering",
  "node_id": "rcma-sD",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-030",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-030`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-031` — Joint-pain case

**Status:** `Draft — ready for SME review` · **Section / node:** Defensive medicine & ordering / `rcma-sD` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Joint-pain case |
| Objective(s) | `rcma-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Defensive medicine |
| Depends on Phase 0 | ⚠ PENDING B10; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Joint-pain case |
| Body / keywords | Node 1: 45-year-old with multi-joint pain, first visit, no history → order everything (CRP, ESR, anti-DNA, anti-Ro, anti-La) vs initial work-up (CRP, ESR) ✔. Node 2: same patient, rheumatoid arthritis already diagnosed by a rheumatologist elsewhere → document the history … |
| Word count (excl. title) | 38 |
| Instruction | Feedback quotes the script's example (B10) |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Collaborative burgundy #7C0041 progress cue for joint-pain case. Omar is placed l5 avatar. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-avatar-thinking → -happy / -concern · placement L5 avatar · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-avatar-thinking → -happy / -concern at L5 avatar.` | illustration | Approved program companion pose char-omar-avatar-thinking → -happy / -concern at L5 avatar. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | Node 1: 45-year-old with multi-joint pain, first visit, no history → order everything (CRP, ESR, anti-DNA, anti-Ro, anti-La) vs initial work-up (CRP, ESR) ✔. Node 2: same patient, rheumatoid arthritis already diagnosed by a rheumatologist elsewhere → document the history and the specialist diagnosis; the full panel is justified in one request ✔ |
| Build / feedback brief | Feedback quotes the script's example (B10) |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 15 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Feedback quotes the script's example (B10) |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback quotes the script's example (B10) |
| Per-choice feedback (scenarios) | Feedback quotes the script's example (B10) |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 15 |
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
  "id": "rcma-031",
  "title": "Joint-pain case",
  "section": "Defensive medicine & ordering",
  "node_id": "rcma-sD",
  "objective_ids": [
    "rcma-o3"
  ],
  "points": 15,
  "narration_script_id": "rcma-031",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B10; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-031`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-032` — Timing

**Status:** `Draft — ready for SME review` · **Section / node:** Defensive medicine & ordering / `rcma-sD` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Timing |
| Objective(s) | `rcma-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Excessive ordering |
| Depends on Phase 0 | ⚠ PENDING B3; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Timing |
| Body / keywords | "Your diabetic patient's HbA1c was done 6 weeks ago. He asks for another." Best action → don't repeat yet unless there's a documented clinical reason; next test at the approved interval (B3) |
| Word count (excl. title) | 31 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for timing. |
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
| Items / options / nodes | "Your diabetic patient's HbA1c was done 6 weeks ago. He asks for another." Best action → don't repeat yet unless there's a documented clinical reason; next test at the approved interval (B3) |
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
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Decide as you would on shift, then read the feedback.

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
  "id": "rcma-032",
  "title": "Timing",
  "section": "Defensive medicine & ordering",
  "node_id": "rcma-sD",
  "objective_ids": [
    "rcma-o3"
  ],
  "points": 5,
  "narration_script_id": "rcma-032",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B3; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-032`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-033` — Supplements

**Status:** `Draft — ready for SME review` · **Section / node:** Defensive medicine & ordering / `rcma-sD` · **Type:** `true_false` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Supplements |
| Objective(s) | `rcma-o3` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Defensive medicine |
| Depends on Phase 0 | ⚠ PENDING B8; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Supplements |
| Body / keywords | "Prescribing a combined multivitamin 'for general wellness' with no documented deficiency is likely to be rejected." → True (B8) |
| Word count (excl. title) | 18 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for supplements. |
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
| Items / options / nodes | "Prescribing a combined multivitamin 'for general wellness' with no documented deficiency is likely to be rejected." → True (B8) |
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
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Decide as you would on shift, then read the feedback.

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
  "id": "rcma-033",
  "title": "Supplements",
  "section": "Defensive medicine & ordering",
  "node_id": "rcma-sD",
  "objective_ids": [
    "rcma-o3"
  ],
  "points": 5,
  "narration_script_id": "rcma-033",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B8; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-033`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-040` — Four causes

**Status:** `Draft — ready for SME review` · **Section / node:** Rejections & coverage / `rcma-sE` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Four causes |
| Objective(s) | `rcma-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Common errors |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Four causes |
| Body / keywords | Rejection notes → causes: "No indication for the MRI" → missing justification · "Diagnosis: fever" → non-specific · "No examination findings recorded" → incomplete · "Antibiotic billed for a viral URTI code" → mismatch (+ 4 more) |
| Word count (excl. title) | 28 |
| Instruction | Feedback reveals the poll answer from rcma-002 |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for four causes. |
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
| Items / options / nodes | Rejection notes → causes: "No indication for the MRI" → missing justification · "Diagnosis: fever" → non-specific · "No examination findings recorded" → incomplete · "Antibiotic billed for a viral URTI code" → mismatch (+ 4 more) |
| Build / feedback brief | Feedback reveals the poll answer from rcma-002 |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 10 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback reveals the poll answer from rcma-002 |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback reveals the poll answer from rcma-002 |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 10 |
| Word count / estimated seconds | 16 words / ≈ 6.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Let's check your earlier guess. Place each item where it belongs, then read the feedback.

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
  "id": "rcma-040",
  "title": "Four causes",
  "section": "Rejections & coverage",
  "node_id": "rcma-sE",
  "objective_ids": [
    "rcma-o4"
  ],
  "points": 10,
  "narration_script_id": "rcma-040",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-040`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-041` — Coverage changes

**Status:** `Draft — ready for SME review` · **Section / node:** Rejections & coverage / `rcma-sE` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Coverage changes |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Updates; Physician responsibility |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Coverage changes |
| Body / keywords | Benefits are added and amended often · Know what's covered, adapt documentation · "If you don't document it properly, it won't be covered — even if it's clinically correct." · Next: Part B covers the new EBP |
| Word count (excl. title) | 33 |
| Instruction | n/a — informational screen. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A clean My Clinic content stage for coverage changes, using a navy header, concise keyword cards and one Collaborative burgundy #7C0041 highlight. |
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
| Items / options / nodes | Benefits are added and amended often · Know what's covered, adapt documentation · "If you don't document it properly, it won't be covered — even if it's clinically correct." · Next: Part B covers the new EBP |
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
| Word count / estimated seconds | 9 words / ≈ 3.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Coverage changes often. Part B covers what's new.

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
  "id": "rcma-041",
  "title": "Coverage changes",
  "section": "Rejections & coverage",
  "node_id": "rcma-sE",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-041",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-041`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-042` — Coverage check

**Status:** `Draft — ready for SME review` · **Section / node:** Rejections & coverage / `rcma-sE` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Coverage check |
| Objective(s) | `rcma-o4` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | Amended benefits |
| Depends on Phase 0 | ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Coverage check |
| Body / keywords | "Which hormonal assessment is likely to be approved?" → menopausal symptoms ✔ vs PCOS work-up (B6) |
| Word count (excl. title) | 14 |
| Instruction | Feedback: the same service can be accepted or rejected depending on indication and documentation |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A focused question stage with a concise stem, generous white answer cards, a navy header and one Collaborative burgundy #7C0041 progress cue for coverage check. |
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
| Items / options / nodes | "Which hormonal assessment is likely to be approved?" → menopausal symptoms ✔ vs PCOS work-up (B6) |
| Build / feedback brief | Feedback: the same service can be accepted or rejected depending on indication and documentation |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | or rejected depending on indication and documentation |
| Points | 5 |
| Pass rule (scenarios / games) | n/a — not a scenario/game pass rule. |
| Feedback — correct | Source feedback route: Feedback: the same service can be accepted or rejected depending on indication and documentation |
| Feedback — incorrect | Retry/incorrect feedback route: Feedback: the same service can be accepted or rejected depending on indication and documentation |
| Per-choice feedback (scenarios) | n/a — not a branching scenario/game; any puzzle or simulation feedback is recorded above. |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | encouraging |
| Target seconds | 8 |
| Word count / estimated seconds | 11 words / ≈ 4.7 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Decide as you would on shift, then read the feedback.

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
  "id": "rcma-042",
  "title": "Coverage check",
  "section": "Rejections & coverage",
  "node_id": "rcma-sE",
  "objective_ids": [
    "rcma-o4"
  ],
  "points": 5,
  "narration_script_id": "rcma-042",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B6; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-042`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-050` — Fix the note

**Status:** `Draft — ready for SME review` · **Section / node:** Fix the note / `rcma-sF` · **Type:** `game` · **Scored:** Yes (25 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Fix the note |
| Objective(s) | `rcma-o5` |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | To summarise |
| Depends on Phase 0 | ⚠ PENDING B12; do not turn these source values into release policy until the named owner closes them. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Fix the note |
| Body / keywords | 3 invented notes, one node each: (1) "Body pain. Vit D + B12 + multivitamin." → choose the best rewrite (findings, deficiency evidence, single indicated supplement, follow-up); (2) "Cough. Augmentin." → choose specific diagnosis + findings justifying antibiotic; (3) "Check-up … |
| Word count (excl. title) | 35 |
| Instruction | Debrief: the 6-point checklist from the script's summary |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A calm scenario stage with one decision at a time, spacious white choice cards, a navy header and a Collaborative burgundy #7C0041 progress cue for fix the note. Omar + Noor is placed l5. |
| edumints layout | n/a (interaction screen) |
| Colours | background `surface` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `none`; reduced-motion mode uses no movement. |
| Companion | Omar + Noor · pose char-omar-avatar (host); char-noor-tip (hints) · placement L5 · speaks: Omar + Noor. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `rcma-img-notes-1` | diagram | rcma-img-notes-1: Invented notes in HTML (real text) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | Editable on-screen diagram; equivalent text provided in HTML. | No |
| `rcma-img-notes-2` | diagram | rcma-img-notes-2: Invented notes in HTML (real text) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | Editable on-screen diagram; equivalent text provided in HTML. | No |
| `rcma-img-notes-3` | diagram | rcma-img-notes-3: Invented notes in HTML (real text) Placement: Screen visual; production placement reviewed by the SME. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. | own SVG, final content review required | Editable on-screen diagram; equivalent text provided in HTML. | No |
| `Approved program companion pose char-omar-avatar (host); char-noor-tip (hints) at L5.` | illustration | Approved program companion pose char-omar-avatar (host); char-noor-tip (hints) at L5. | own / official My Clinic asset | Omar + Noor companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | 3 invented notes, one node each: (1) "Body pain. Vit D + B12 + multivitamin." → choose the best rewrite (findings, deficiency evidence, single indicated supplement, follow-up); (2) "Cough. Augmentin." → choose specific diagnosis + findings justifying antibiotic; (3) "Check-up. Full labs." → link to a covered condition or bill as appropriate. Score + 1 hint per node, no lives, no timer |
| Build / feedback brief | Debrief: the 6-point checklist from the script's summary |
| Correct answer(s) / completion rule | Use the complete source answer route in Items / options / nodes above; it is copied verbatim from Phase 2 and retains any ⚠ PENDING marker. |
| Accepted variants (typed answers) | n/a — no typed-answer variants are specified in Phase 2. |
| Points | 25 |
| Pass rule (scenarios / games) | Completion and pass handling remain the Phase 4 build decision; preserve the full Phase 2 route above. |
| Feedback — correct | Source feedback route: Debrief: the 6-point checklist from the script's summary |
| Feedback — incorrect | Retry/incorrect feedback route: Debrief: the 6-point checklist from the script's summary |
| Per-choice feedback (scenarios) | Debrief: the 6-point checklist from the script's summary |
| Hint (if any) | n/a — no hint is specified in Phase 2; do not invent one before SME review. |
| Retry / lives | Untimed and keyboard-operable; allow retry unless the approved Phase 4/LMS policy says otherwise. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR / NOOR |
| Tone | encouraging |
| Target seconds | 15 |
| Word count / estimated seconds | 23 words / ≈ 9.9 s at 140 wpm |
| Cue targets | None in this review draft; final build may add cue IDs after visual timing review. |

> OMAR: Three notes, your pen. Play the round, then read the feedback.
>
> NOOR: That is the habit we want from every new colleague.

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
  "id": "rcma-050",
  "title": "Fix the note",
  "section": "Fix the note",
  "node_id": "rcma-sF",
  "objective_ids": [
    "rcma-o5"
  ],
  "points": 25,
  "narration_script_id": "rcma-050",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs.",
  "notes": "Planned Phase 3 visual placements (not production assets): <rcma-img-notes-1> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <rcma-img-notes-2> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production.; <rcma-img-notes-3> — Screen visual; production placement reviewed by the SME.. PENDING relevant Phase 0 and SME visual approval; provenance recorded before production."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: ⚠ PENDING B12; do not turn these source values into release policy until the named owner closes them.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-050`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-090` — Results

**Status:** `Draft — ready for SME review` · **Section / node:** Fix the note / `rcma-sF` · **Type:** `results_breakdown` · **Scored:** No

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
| Body / keywords | rcma-o1…o5, weak below 70% |
| Word count (excl. title) | 5 |
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
| Items / options / nodes | rcma-o1…o5, weak below 70% |
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
  "id": "rcma-090",
  "title": "Results",
  "section": "Fix the note",
  "node_id": "rcma-sF",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-090",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-090`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---
### `rcma-091` — List to keep

**Status:** `Draft — ready for SME review` · **Section / node:** Fix the note / `rcma-sF` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Checklist to keep |
| Objective(s) | — |
| On-the-job action | Use this screen’s rule or decision during the work described in the action map. |
| Source | To summarise |
| Depends on Phase 0 | Shared dependency: program brand confirmation D11. Review the module source-lock register before production. |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | List to keep |
| Body / keywords | ✔ Be specific; avoid uncovered codes and combined supplements · ✔ Full data + plan with duration and outcome · ✔ Justify every service with a specific code; provisional diagnosis if needed · ✔ Think like a clinician and a … |
| Word count (excl. title) | 32 |
| Instruction | show_score |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close |
| Logo | `logo-horizontal-navy.png`, 30 px in the 64 px header at top-left |
| Visual concept | A confident light closing screen with four short takeaways, the supplied My Clinic logo, and space for the next-module hand-off. Omar is placed l6 right. |
| edumints layout | text_media / full_media as shown in screen-visuals.html |
| Colours | background `light` · text `dark` · highlight `secondary` / Collaborative burgundy #7C0041 · navy `#003867` remains structural |
| Typography | Montserrat: 28–30 px screen title; 14–18 px body/options; 11–14 px labels; no body text below 14 px. |
| Watermark | None behind body text or questions. |
| Icons | One consistent own-SVG line-icon family; semantic labels remain HTML text. |
| Animation / reveal | `fade-up`; reduced-motion mode uses no movement. |
| Companion | Omar · pose char-omar-success · placement L6 right · speaks: Omar. |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `Supplied My Clinic horizontal navy logo lock-up in the header.` | icon | Supplied My Clinic horizontal navy logo lock-up in the header. | own / official My Clinic asset | My Clinic logo. | No |
| `Approved program companion pose char-omar-success at L6 right.` | illustration | Approved program companion pose char-omar-success at L6 right. | own / official My Clinic asset | Omar companion guide supporting this learning moment. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items / options / nodes | ✔ Be specific; avoid uncovered codes and combined supplements · ✔ Full data + plan with duration and outcome · ✔ Justify every service with a specific code; provisional diagnosis if needed · ✔ Think like a clinician and a reviewer · ✔ If you skip a protocol, document why · ✔ Clear, strong, defensible. Next: Part B |
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
| Target seconds | 25 |
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
  "id": "rcma-091",
  "title": "List to keep",
  "section": "Fix the note",
  "node_id": "rcma-sF",
  "objective_ids": [],
  "points": 0,
  "narration_script_id": "rcma-091",
  "asset_status": "Review hand-off only; resolve Phase 0 dependencies before adding production asset IDs."
}
```

> This is valid JSON review metadata, not a finished production screen schema. Phase 4 adds the
type-specific fields, measured hotspot coordinates and final asset IDs only after the pending source
lock items have written SME decisions.

#### 8. Notes for SME and developer

- Open questions: Shared dependency: program brand confirmation D11. Review the module source-lock register before production.
- Developer notes: Keep all policy wording as editable HTML, preserve the supplied client logo, and use the exact screen id `rcma-091`. Do not reuse source-video or source-deck imagery where the Phase 0 file prohibits it.

---


## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `rcma-000` | `title_slide` | N | 0 | 8 | 28 | 12 | Draft |
| 2 | `rcma-001` | `content_slide` | N | 0 | 17 | 16 | 7 | Draft |
| 3 | `rcma-002` | `poll` | N | 0 | 15 | 19 | 8 | Draft |
| 4 | `rcma-010` | `tabs` | N | 0 | 27 | 8 | 3 | Draft |
| 5 | `rcma-011` | `image_compare` | N | 0 | 23 | 9 | 4 | Draft |
| 6 | `rcma-012` | `sorting` | Y | 10 | 14 | 16 | 7 | Draft |
| 7 | `rcma-013` | `mcq` | Y | 5 | 23 | 11 | 5 | Draft |
| 8 | `rcma-020` | `content_slide` | N | 0 | 16 | 9 | 4 | Draft |
| 9 | `rcma-021` | `matching` | Y | 10 | 34 | 16 | 7 | Draft |
| 10 | `rcma-022` | `worked_example` | N | 0 | 34 | 17 | 7 | Draft |
| 11 | `rcma-023` | `drag_drop` | Y | 10 | 32 | 11 | 5 | Draft |
| 12 | `rcma-030` | `content_slide` | N | 0 | 18 | 13 | 6 | Draft |
| 13 | `rcma-031` | `decision_scenario` | Y | 15 | 38 | 11 | 5 | Draft |
| 14 | `rcma-032` | `mcq` | Y | 5 | 31 | 11 | 5 | Draft |
| 15 | `rcma-033` | `true_false` | Y | 5 | 18 | 11 | 5 | Draft |
| 16 | `rcma-040` | `drag_drop` | Y | 10 | 28 | 16 | 7 | Draft |
| 17 | `rcma-041` | `content_slide` | N | 0 | 33 | 9 | 4 | Draft |
| 18 | `rcma-042` | `mcq` | Y | 5 | 14 | 11 | 5 | Draft |
| 19 | `rcma-050` | `game` | Y | 25 | 35 | 23 | 10 | Draft |
| 20 | `rcma-090` | `results_breakdown` | N | 0 | 5 | 21 | 9 | Draft |
| 21 | `rcma-091` | `summary` | N | 0 | 32 | 36 | 15 | Draft |
| | **Totals** | | **10** | **100** | | **322** | **138 ≈ 2.3 min** | Draft |

### Narration authoring gaps

16 of 21 screens are below 70% of their Phase 3 target because generated narration is no longer padded (G11/C20). See [`narration-gaps.md`](narration-gaps.md) for the worklist.

### Asset list

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `rcma-img-note-weak` | diagram | Generated file | own | Yes | Generated native SVG using fictional teaching text. |
| `rcma-img-note-strong` | diagram | Generated file | own | Yes | Generated native SVG using fictional teaching text. |
| `rcma-img-reviewer` | diagram | Generated file | own | Yes | Generated native SVG. |
| `rcma-img-note-weak` | SVG note cards | rcma-011 | own | Yes | Planned |
| `-strong` | SVG note cards | rcma-011 | own | Yes | Planned |
| `rcma-img-reviewer` | SVG | rcma-001 | own | Yes | Planned |
| `rcma-img-notes-1` | HTML | rcma-050 | own | n/a | Planned |
| `rcma-img-notes-2` | HTML | rcma-050 | own | n/a | Planned |
| `rcma-img-notes-3` | HTML | rcma-050 | own | n/a | Planned |
| `rcma-pdf-checklist` | PDF | rcma-091 | own | n/a | Planned |
| `char-noor-*` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |
| `char-omar-*` | character set (program-wide) | see "Companions in this module" | ai-generated (masters approved first) | Yes | Planned |

### Open questions for the SME

| # | Screen id | Question | Phase 0 owner | Blocks build? |
|---|---|---|---|---|
| 1 | All affected cards | Regulator name CCHI vs CHI | `B1` · RCM lead | Yes |
| 2 | All affected cards | Vitamin D repeat interval ("not less than 118") | `B2` · RCM lead + payer relations | Yes |
| 3 | All affected cards | HbA1c repeat interval ("before 89 day") | `B3` · RCM lead | Yes |
| 4 | All affected cards | ICD-10 edition used for claims in KSA (ICD-10-AM?) and the exact codes for each example: R50, R05, R11, K52, J03, I10, E66, L70, L66, L21, N46, N97, general check-up (Z00?) | `B4` · Coding lead | Yes |
| 5 | All affected cards | Obesity: uncovered, but covered with BMI > 40 and surgical referral | `B5` · Payer relations | Yes |
| 6 | All affected cards | PCOS hormonal assessment rejected vs menopause hormonal assessment and HRT approved | `B6` · Payer relations | Yes |
| 7 | All affected cards | Mental-health sub-limit 50,000 SAR + pre-authorisation | `B7` · Payer relations | Yes |
| 8 | All affected cards | "Combined supplements are treated as defensive medicine" | `B8` · RCM lead | Yes |
| 9 | All affected cards | Pre-authorisation workflow ("submit diagnosis with the request to get pre-authorisation at the first attempt") | `B9` · RCM lead | Yes |
| 10 | All affected cards | Clinical examples (IV fluids for dehydration; multi-joint pain with anti-DNA/anti-Ro/anti-La) | `B10` · Medical Director | Yes |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| `RCM` | R-C-M | `rcma-000` |

### Self-check

- [x] Every Phase 2 core screen has a card, in the same id order.
- [x] Screen scoring totals reconcile to the Phase 2/4 plan (10 scored / 100 points).
- [x] Every screen has a visual brief, supplied-logo instruction, narration segment and accessibility notes.
- [x] Every meaningful generated or planned image is listed with an alt-text route and provenance status.
- [x] Template structural review ran on every card: all eight sections and every Phase 2 interaction brief are present; human SME/content approval remains pending.
- [x] No real patient, staff, claim or contact data is introduced.
- [ ] SME review and Phase 0 approval are complete — **not yet; do not move to production.**
- [ ] Production voice selection / D10 approval is complete — **not yet.**
- [ ] Type-specific production JSON, final asset IDs and SCORM build have been validated — **Phase 4 work, not claimed here.**
