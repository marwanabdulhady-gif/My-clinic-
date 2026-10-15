# Storyboard — 03 Welcome On Board: My Clinic & HR Essentials

![My Clinic logo](../../00_program/brand/logo-preview.png)

> **Review pack v0.2 · 2026-10-14.** Screen-by-screen storyboard for module 03. One card per screen listed in
> [`../phase-2-storyboard.md`](../phase-2-storyboard.md), same ids, same order, same types and points.
> Written against [`../../00_program/storyboard-template/README.md`](../../00_program/storyboard-template/README.md).
> v0.2 retrofits the course companions **Dr. Omar** (lead host) and **Noor** (co-host) from
> [`../../00_program/characters/companions.md`](../../00_program/characters/companions.md): every spoken line is
> tagged `OMAR:` / `NOOR:`, and the shared programme assets `char-omar-*` / `char-noor-*` replace the old
> module-only character art. It is a review artefact, **not an approved policy or production SCORM package**;
> source-lock decisions stay marked `⚠ PENDING`.

**Companion documents:** [`screen-visuals.html`](screen-visuals.html) ·
[`visual-plan.json`](visual-plan.json) · [`narration-script.json`](narration-script.json) ·
[`audio-script-export.json`](audio-script-export.json) · [`voice_talent.md`](voice_talent.md) ·
[`asset-register.md`](asset-register.md) · [`lint-report.json`](lint-report.json)

---

## A. Module header

| Field | Value |
|---|---|
| Module | 03 — My Clinic — Welcome On Board: My Clinic & HR Essentials |
| Module prefix | `hr-` |
| Storyboard version | `v0.2` (v0.1 → v0.2: companions retrofit, speaker-tagged narration, review-pack files) |
| Author | Arena agent (storyboarding run 1; v0.2 companion retrofit), for HR + Comms review |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review` (blocked from production by the open Phase 0 items below) |
| SME reviewer (role) | HR Business Partner / Head of Human Capital (SME lead); Corporate Communications for screens `hr-020`–`hr-023` |
| Audience | All new employees (clinical and non-clinical), day 1–3 |
| Seat-time budget | Proposal target ~45 minutes; Phase 1 allocation ~46 minutes (A 3 · B 6 · C 5 · D 6 · E 10 · F 6 · G 5 · H 2 · I 2 · Close 1); reconcile the 1-minute difference at SME review / pilot. |
| SCORM / completion / pass mark | SCORM 2004 4th ed · `viewed_all_and_passed` · passing score **70** (= 102 of 145 points) |
| Scored screens / total points | 15 / 145 |
| Source file | `elearning-course/md/03_hr-employee-induction.md` (from `HR.pptx`, 62 slides, *Confidential*) |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (version/date read: `2026-10-14`) |
| Module colour | Caring purple `#652D8C` |
| Theme | `brand_to_theme(00_program/brand/brand-kit.json)` + `style-minimal`; module colour `#652D8C` as `secondary` |
| Phase 0 items still open | B1, B2, B3, B4, B5/D3, B6/D5, B7, B8, B9, B10, B11, B12, B13, B14/D8; program D10 (voices) |
| Companions | Lead host **Dr. Omar** (`OMAR:`), co-host **Noor** (`NOOR:`) — [`companions.md`](../../00_program/characters/companions.md) §6 and Phase 3 "Companions in this module". Visible on 8 of 36 screens (`hr-000`, `hr-001`, `hr-002`, `hr-031`, `hr-043`, `hr-044`, `hr-061`, `hr-091`); every other screen is Dr. Omar's voice only. Shared art only: `char-omar-*` / `char-noor-*` (companions.md §3) |
| Narration | 36 screens narrated in 39 recorded lines (Dr. Omar 35, Noor 4); two-voice screens `hr-000` and `hr-091`; totals in §C |

### Objectives covered

| Objective id | Objective | Assessed by (screen ids) |
|---|---|---|
| `hr-o1` | Link My Clinic's values and 7C strategy to everyday actions in your role. | `hr-011`, `hr-013` |
| `hr-o2` | Apply the code of ethics and patients' rights and responsibilities to workplace situations. | `hr-031`, `hr-032`, `hr-033` |
| `hr-o3` | Decide whether a leave request is eligible and how many days apply. | `hr-042`, `hr-044`, `hr-045` |
| `hr-o4` | Calculate a GOSI deduction and an overtime payment. | `hr-052`, `hr-054` |
| `hr-o5` | Choose the correct system (Oracle, intranet, Qiwa, Mumaris) and submit a leave request in Oracle. | `hr-060`, `hr-061`, `hr-062` |
| `hr-o6` | Apply ID card, dress-code and resignation rules. | `hr-071`, `hr-081` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `hr-sA` | A · Welcome | `hr-000`–`hr-002` |
| `hr-sB` | B · Our values & strategy | `hr-010`–`hr-014` |
| `hr-sC` | C · Our clinic | `hr-020`–`hr-023` |
| `hr-sD` | D · Ethics & patients' rights | `hr-030`–`hr-033` |
| `hr-sE` | E · Your leave | `hr-040`–`hr-045` |
| `hr-sF` | F · Pay & social insurance | `hr-050`–`hr-054` |
| `hr-sG` | G · Systems & licences | `hr-060`–`hr-062` |
| `hr-sH` | H · ID, benefits & dress code | `hr-070`–`hr-071` |
| `hr-sI` | I · Contracts & leaving | `hr-080`–`hr-081` |
| `hr-sZ` | Z · Close | `hr-090`–`hr-091` |

### Shared build conventions used in every card

| Convention | Value |
|---|---|
| `section` | Matches the *Section title* column above (for example `E · Your leave`). |
| `reveal` | `"auto"` on every narrated content screen; `"none"` on questions, games and interactions; `"click"` where the card says so. |
| `animation` | `fade-up` (default) unless the card says otherwise. |
| `narration_text` | Every card with a narration script carries `narration_text` = the script with `[[cue:…]]` / `[[pause:…]]` markup removed and the speaker labels (`OMAR:` / `NOOR:`) **kept**, for captions and the transcript. On `hr-061` the tip line is played with the end-of-simulation feedback, so it lives in the feedback HTML rather than in `narration_text`. |
| Speakers | Every spoken line starts `OMAR:` or `NOOR:` (companions.md §5). Two-voice screens are split into one `narration-script.json` segment per line (`part` = `omar-1`, `noor-1`) and joined into one audio file per screen with 0.3 s silence. |
| `notes` | Companion placement, pose asset ids and alt text are recorded in the schema's `notes` field on the 8 companion screens (the screen models have no avatar field; the renderer places the companion from the card). |
| Points / objectives | Every build block states `points` and `objective_ids`, including `0` / `[]` on unscored screens (so explore-mode hotspots are never counted at the model default). |
| `narration_asset_id` | `<hr-aud-XXX>` — assigned in Phase 3/4 from `export_audio_script`. |
| `evidence_screen_ids` | Set on every scored screen to the screen that teaches the rule (K1 evidence link, `core/antislop.py` E1). |
| Asset id placeholders | Written as `<hr-img-…>` / `<hr-aud-…>` / `<hr-pdf-…>` until `add_asset` returns a real id. |

### Proposed changes

| # | Screen | Change proposed | Why | Keep original? |
|---|---|---|---|---|
| 1 | `hr-044`, node 1 | Frame the lab-technician request as a request that **already has the MD's pre-approval**, and make the tested rule *“2 days a year for technicians, never carried over”* (slides 39–40). | Phase 2 words it as “scientific leave for a conference”. The source says scientific leave is for academic exams (slide 40) and that supporting documents need the MD's pre-approval. The reframe keeps the item answerable from the source and still tests the 2-day allowance. | Yes — the original card is written; the reframe is inside it and flagged for HR. |
| 2 | `hr-071`, item `it6` | Keep the wording **“No casual days”** for back office and make front office **“Uniform for every shift”**, with per-item feedback that names the difference. | The source uses *“no casual days”* for back office (slide 58) and *“no casual attire”* for front office. Two near-identical strings would make one placement ambiguous. | Yes — flagged in the card's SME notes. |
| 3 | `hr-001` | v0.2: Dr. Omar's half-body `char-omar-explaining` pose takes the right column (`text_media`) instead of the full-bleed hero photo; `hr-img-hero` is no longer placed on any screen. | Phase 2/3 companion tables and companions.md §4 (intro screens use the lead host in the right column instead of an illustration); the hero photo was also blocked on consent (**B6 / D5**). | Yes — HR may still supply a consented team photo for the HR Quick Reference or a later version. |
| 4 | `hr-000` | v0.2: narration target 15 s → 20 s for the "meet your guides" two-voice introduction (Omar 11 s + Noor 9 s). | Two self-introductions plus the welcome do not fit in 15 s at 140 wpm; companions.md §5 allows up to 45 s for a planned two-voice welcome. | Yes — module total stays inside the Phase 3 estimate. |
| 5 | `hr-061` | v0.2: Omar's tip card appears with the end-of-simulation feedback (appended to both feedback strings) and has its own short audio line (`part` `omar-tip`). | Phase 3 companion table: "Tip: check the request status before you book travel", shown after the simulation, never during the click steps. | Yes — no change to steps, regions, points or pass rule. |

---

## B. Screen cards

### `hr-000` — Welcome On Board

**Status:** `Draft — ready for SME review` · **Section / node:** A · Welcome / `hr-sA` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open: make the learner welcome and say what the next 45 minutes give them |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slide 3 (“Welcome On Board”); slides 2–3 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Welcome On Board |
| Subtitle | My Clinic & HR essentials · about 45 minutes |
| Body / keywords | *(none — title slide)* |
| Word count (excl. title) | 0 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L1 Title (see `../../00_program/brand/screen-mockups/01-title.png`) |
| Logo | `logo-horizontal-white.png`, 48 px tall, top-left (48 px from left, 40 px from top) |
| Visual concept | Official navy gradient background (`background-title-navy.png`, `#003867 → #3B6A97`) with the supplied white five-petal watermark (`mark-white.png`) cropped off the right edge; supplied white My Clinic logo top-left; Caring purple `#652D8C` module chip above the white Montserrat Bold title and mist `#C0CED9` subtitle on the left; **"Meet your guides"**: two white rounded portrait cards bottom-right, side by side — Dr. Omar (`char-omar-welcome`) and Noor (`char-noor-welcome`) waving — with name and role under each (mockup `07-meet-your-guides.png`); tagline bottom-left; no photograph or generated logo |
| edumints layout | n/a (`title_slide`) |
| Colours (palette names + hex) | bg `primary` (navy gradient `#003867 → #3B6A97`) · text `on_primary` (white `#FFFFFF`, subtitle mist `#C0CED9`) · highlight `secondary` (Caring purple `#652D8C` module chip) · warning none |
| Typography (Montserrat) | Title Montserrat Bold 700, 40 px; subtitle Montserrat Regular 400, 18–20 px; module chip Montserrat Bold 700, 12–14 px; footer/tagline 10–12 px. |
| Watermark | Petal watermark (`mark-white.png` at 10% opacity, 520 px, cropped off the right edge) |
| Icons | None |
| Animation / reveal | Title fades up, then the subtitle 0.4 s later; Omar's card fades up as he speaks, Noor's card as she speaks (reduced motion: both visible at once) |
| Companion | **Both** — `char-omar-welcome` + `char-noor-welcome` side by side (the planned `char-duo-welcome` is built from the two `-welcome` poses, companions.md §3) · placement L1 duo, bottom-right: two white rounded portrait cards, 16 px radius, ~190 × 300 px each, 4 px top edge in the character colour (Omar teal `#008C99`, Noor purple `#652D8C`), caption under each image "Dr. Omar · Family physician" / "Noor · Senior nurse & safety liaison" (Montserrat 600, 14 px, navy) · they sit above the petal watermark and never cover the title · tip text n/a · speaks: Omar, then Noor (two-voice welcome) |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `brand-background-title-navy` | background | Supplied `00_program/brand/assets/background-title-navy.png`; official 16:9 navy gradient; no added content | own (official My Clinic brand asset) | Decorative background. | Yes |
| `brand-logo-horizontal-white` | image | Supplied `00_program/brand/assets/logo-horizontal-white.png`; unmodified white lock-up, 48 px high | own (official My Clinic brand asset) | My Clinic logo. | No |
| `brand-mark-white` | icon | Supplied `00_program/brand/assets/mark-white.png`; five-petal watermark, 520 px, 10% opacity, cropped off right edge | own (official My Clinic brand asset) | Decorative watermark. | Yes |
| `char-omar-welcome` | illustration | Shared programme companion pose (Canva media `MAHX-hEFOR4`), half-body open-palm wave, in the left portrait card; transparent PNG from `00_program/characters/assets/` | ai-generated (programme master, companions.md §3) | “Dr. Omar, a family physician, smiling and waving hello.” | No |
| `char-noor-welcome` | illustration | Shared programme companion pose (Canva media `MAHX-pFaNMU`), half-body open-palm wave, in the right portrait card | ai-generated (programme master, companions.md §3) | “Noor, a senior nurse and patient-safety liaison, smiling and waving hello.” | No |

#### 4. Interaction and scoring

n/a — title slide, no interaction and no score.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR → NOOR (two-voice screen: parts `omar-1`, `noor-1`; joined into one file with 0.3 s silence) |
| Tone | Warm |
| Target seconds | 20 (v0.1: 15) — per part: `omar-1` 11, `noor-1` 9 |
| Word count / est. seconds | 46 words / ≈ 20.0 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Welcome to My Clinic. I'm Dr. Omar, a family physician at J2. Today you'll meet who we are, and the HR rules you'll actually use.

> NOOR: [[pause:0.3]] And I'm Noor, a senior nurse at J1. Nothing here is a memory test. We'll show you where to find things.

New lexicon terms: Noor — “noor” (rhymes with *tour*); Omar — “OH-mar” (companions.md §5). J1 — “J-one”; J2 — “J-two”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction; Continue is a native button |
| Not colour-only | Title is plain `on_primary`-on-`primary` text; no meaning carried by colour |
| Captions / transcript | `narration_text` = script without markup |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "title_slide",
  "id": "hr-000",
  "title": "Welcome On Board",
  "subtitle": "My Clinic & HR essentials · about 45 minutes",
  "section": "A · Welcome",
  "node_id": "hr-sA",
  "objective_ids": [],
  "points": 0,
  "notes": "Companions (companions.md §4, mockup 07): two white rounded portrait cards bottom-right, ~190x300 px each, 4 px top edge in the character colour — Dr. Omar char-omar-welcome (alt: 'Dr. Omar, a family physician, smiling and waving hello.') and Noor char-noor-welcome (alt: 'Noor, a senior nurse and patient-safety liaison, smiling and waving hello.'). Audio: omar-1 + noor-1 joined with 0.3 s silence.",
  "background_asset_id": "<brand-background-title-navy>",
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<hr-aud-000>",
  "narration_text": "OMAR: Welcome to My Clinic. I'm Dr. Omar, a family physician at J2. Today you'll meet who we are, and the HR rules you'll actually use. NOOR: And I'm Noor, a senior nurse at J1. Nothing here is a memory test. We'll show you where to find things."
}
```

#### 8. Notes for SME and developer

- Open questions: Does HR want the real CEO welcome video here instead of a still (phase-3 §1, program D10)? If yes, this becomes a `video` screen, the duo introduction moves to `hr-001`, and the narration moves to the video transcript.
- Developer notes: use the supplied `background-title-navy.png`, `logo-horizontal-white.png` and `mark-white.png` from `00_program/brand/assets/` unchanged. No photograph, generated logo, or extra wordmark is used on this title screen. `title_slide` has no image slot: place the two companion cards from the theme/renderer as described in `notes`. This is the first course in the learning path, so it is the only title screen in the programme with both companions (companions.md §4).

---

### `hr-001` — Why we exist

**Status:** `Draft — ready for SME review` · **Section / node:** A · Welcome / `hr-sA` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the purpose, mission and goal, in plain words, and why it matters on the job |
| Objective(s) | — (supports `hr-o1`) |
| On-the-job action | — |
| Source | `HR.pptx` brand banner, slides 1–2, 8 (purpose, mission, goal) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Why we exist |
| Body / keywords | **Purpose** — helping people live longer, healthier, happier lives · **Mission** — the world's most customer-centric healthcare company · **Goal** — outstanding patient experience + excellent clinical outcomes |
| Word count (excl. title) | 24 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "A · Welcome", 2 px navy `#003867` header rule |
| Visual concept | Three stacked statement blocks in the left column on an off-white field, each with a small line icon (heart, globe-and-heart, shield-check); the purpose block is largest and sits alone at the top; Dr. Omar's half-body `explaining` pose stands in the right column, hand presenting towards the statements (companions.md §4 intro screen: the lead host replaces the illustration) |
| edumints layout | `text_media` — text blocks left, `char-omar-explaining` right (320–380 px tall, bottom-aligned, transparent PNG, no card behind him) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Single-weight line icons (heart, globe-and-heart, shield-check), 24 px grid, 1.5 px stroke, Caring purple #652D8C, own SVG |
| Animation / reveal | Blocks reveal in narration order: purpose → mission → goal; Omar is visible from the start (no movement on him) |
| Companion | Dr. Omar · `char-omar-explaining` · placement L3 right column, half-body, 320–380 px · tip text n/a · speaks: Omar, including his honest first-week story (companions.md §1, used once in the programme, here) |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `char-omar-explaining` | illustration | Shared programme companion pose (Canva media `MAHX-ljvFtE`): half-body, hand presenting to the side; right column, 320–380 px | ai-generated (programme master, companions.md §3) | “Dr. Omar, a family physician, presenting the clinic's purpose, mission and goal.” | No |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, calm |
| Target seconds | 35 |
| Word count / est. seconds | 85 words / ≈ 37.6 s (speaker labels excluded, pauses included) |
| Cue targets | `purpose`, `mission`, `goal` |

> OMAR: [[cue:purpose]] Our purpose is simple to say and hard to do: we help people live longer, healthier, happier lives, including people who are well today. [[pause:0.4]] [[cue:mission]] Our mission is to be the world's most customer-centric healthcare company. In practice, every role asks one question: did this help the patient? [[pause:0.4]] [[cue:goal]] Our goal follows from that: outstanding patient experience, alongside excellent clinical outcomes. [[pause:0.4]] Honestly, my first week here, I felt there was too much to take in. You don't need to remember everything today — just where to find it.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed; blocks readable in DOM order |
| Not colour-only | Each block is headed by real text (Purpose / Mission / Goal); icons only support |
| Captions / transcript | `narration_text` = script without markup |
| Timing | Untimed; `reveal: "auto"` with audio drives pacing, and the text is all readable before the audio ends |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-001",
  "title": "Why we exist",
  "section": "A · Welcome",
  "node_id": "hr-sA",
  "objective_ids": [],
  "points": 0,
  "notes": "Companion: Dr. Omar char-omar-explaining is the media of the text_media layout (right column, 320-380 px). Honest story: Omar's first week (companions.md §1, used once, here).",
  "layout": "text_media",
  "media_asset_id": "<char-omar-explaining>",
  "media_alt": "Dr. Omar, a family physician, presenting the clinic's purpose, mission and goal.",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Purpose</strong> — helping people live longer, healthier, happier lives</p><p><strong>Mission</strong> — the world's most customer-centric healthcare company</p><p><strong>Goal</strong> — outstanding patient experience + excellent clinical outcomes</p>",
  "narration_asset_id": "<hr-aud-001>",
  "narration_text": "OMAR: Our purpose is simple to say and hard to do: we help people live longer, healthier, happier lives, including people who are well today. Our mission is to be the world's most customer-centric healthcare company. In practice, every role asks one question: did this help the patient? Our goal follows from that: outstanding patient experience, alongside excellent clinical outcomes. Honestly, my first week here, I felt there was too much to take in. You don't need to remember everything today — just where to find it."
}
```

#### 8. Notes for SME and developer

- Open questions: None on content. The three statements are verbatim from the brand banner in the deck. Omar's first-week story is the approved line from companions.md §1.
- Developer notes: the companion image is the media of a `text_media` layout, so it carries real alt text (not decorative). `blocks` reveal as one unit. The three statements are therefore separate `<p>` elements in `body_html`, not `blocks`, so they reveal one by one.

---

### `hr-002` — One million riyals

**Status:** `Draft — ready for SME review` · **Section / node:** A · Welcome / `hr-sA` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explore: an unscored icebreaker that makes the learner commit to something they care about before any policy appears |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slide 5 (“Let Us Know Each Other”) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | One million riyals |
| Body / keywords | If you had one million Saudi riyals, where would you spend it? |
| Word count (excl. title) | 12 |
| Instruction | Pick the one closest to you, or write your own. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "A · Welcome · Check", 2 px navy `#003867` header rule |
| Visual concept | Five large tappable option cards in a single row on small screens, two rows on wide; each card has a line icon above a one-word label; a free-text box slides in under the row labelled “Other”; Dr. Omar's small half-body `listening` pose (holding a tablet) stands beside the option area on the right, outside the cards — this is an unscored icebreaker, not a question |
| edumints layout | n/a (`poll`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | Single-weight line icons on the five poll cards (family, plane, book, hands, speech-bubble), navy #003867, own SVG |
| Animation / reveal | Cards fade up in sequence over 0.6 s; the reflection panel fades in after submitting |
| Companion | Dr. Omar · `char-omar-listening` · placement small, beside the poll (~220–260 px tall, right edge of the stage, never over the option cards or the text box; hidden below 600 px width so the options keep the full row) · tip text n/a · speaks: Omar (invites the icebreaker) |

**Imagery** (the poll icon set is part of the shared line-icon family, not a per-screen asset)

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `char-omar-listening` | illustration | Shared programme companion pose (Canva media `MAHX-uifxtY`): half-body, holding a tablet, attentive; small, right of the option cards | ai-generated (programme master, companions.md §3) | “Dr. Omar, a family physician, listening with a tablet in his hand.” | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | `a` Family · `b` Travel · `c` Learning · `d` Giving back · `e` Other (free text) |
| Correct answer(s) | n/a — unscored |
| Accepted variants | n/a |
| Points | 0 |
| Feedback | Reflection (not feedback): “Whatever you chose says something you care about. At My Clinic, we start from what people care about — including yours.” |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, light |
| Target seconds | 10 |
| Word count / est. seconds | 23 words / ≈ 9.9 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Before we start: if you had one million Saudi riyals, where would you spend it? There's no right answer. Pick whatever is closest.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Options are radio inputs; the text box is a labelled input; submit is a native button |
| Not colour-only | Selection is shown by a border plus a filled radio control, not colour alone |
| Captions / transcript | `narration_text` present |
| Timing | Untimed; the poll never blocks Continue |

#### 7. Build fields (edumints)

```json
{
  "type": "poll",
  "id": "hr-002",
  "title": "One million riyals",
  "section": "A · Welcome",
  "node_id": "hr-sA",
  "objective_ids": [],
  "points": 0,
  "notes": "Companion: Dr. Omar char-omar-listening, ~220-260 px, right edge beside the option cards, never over them; hidden below 600 px width. Alt: 'Dr. Omar, a family physician, listening with a tablet in his hand.'",
  "prompt_html": "<p>If you had one million Saudi riyals, where would you spend it?</p>",
  "options": [
    {
      "id": "a",
      "text_html": "Family"
    },
    {
      "id": "b",
      "text_html": "Travel"
    },
    {
      "id": "c",
      "text_html": "Learning"
    },
    {
      "id": "d",
      "text_html": "Giving back"
    },
    {
      "id": "e",
      "text_html": "Other"
    }
  ],
  "multi": false,
  "allow_text": true,
  "reflection_html": "<p>Whatever you chose says something you care about. At My Clinic, we start from what people care about — including yours.</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-002>",
  "narration_text": "OMAR: Before we start: if you had one million Saudi riyals, where would you spend it? There's no right answer. Pick whatever is closest."
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: the poll must never block Continue — `poll` is unscored and participation-only. Place Omar from the theme/renderer as described in `notes`; he never overlaps an option card.

---

### `hr-010` — Our four values

**Status:** `Draft — ready for SME review` · **Section / node:** B · Our values & strategy / `hr-sB` · **Type:** `tabs` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: each value is a set of behaviours, not a poster |
| Objective(s) | — (teaches `hr-o1`, assessed on `hr-011`) |
| On-the-job action | A1 |
| Source | `HR.pptx` slide 9 (“Why Our Values Matter”) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Our four values |
| Body / keywords | Values are behaviours. Open each one and look for something you already do. |
| Word count (excl. title) | 14 |
| Instruction | Open each value. |

**Tab content (per tab ≤ 40 words)**

| Tab | Theme | Actions shown |
|---|---|---|
| Collaborative | Unites diverse | Act together · Treat everyone with respect · Be transparent · Embrace diverse perspectives · Deliver outstanding results |
| Responsible | Creating a culture of accountability | Own our decisions and actions · Make things happen · Demonstrate high professional standards · Hold yourself and each other accountable |
| Ambitious | Set new standards | Go above and beyond · Make new possibilities happen · Challenge the status quo · Become industry shapers · Deliver outstanding results |
| Caring | Putting empathy first | Act with empathy · Everyone matters · Love our customers · Deliver with quality |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "B · Our values & strategy", 2 px navy `#003867` header rule |
| Visual concept | Four horizontal tab labels across the top; each tab uses its supplied official square value tile with white line icon, and the active panel shows the theme line in large type plus the actions as plain HTML text |
| edumints layout | n/a (`tabs`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Four supplied official value tiles (`value-tile-collaborative-burgundy.png`, `value-tile-responsible-magenta.png`, `value-tile-ambitious-teal.png`, `value-tile-caring-purple.png`); use the white line icons in the supplied assets; do not redraw |
| Animation / reveal | Panel content fades up on each tab change |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `brand-value-tile-collaborative-burgundy` | image | Supplied `00_program/brand/assets/value-tile-collaborative-burgundy.png`; official burgundy square with white line icon | own (official My Clinic brand asset) | Decorative; the tab label carries the value name. | Yes |
| `brand-value-tile-responsible-magenta` | image | Supplied `00_program/brand/assets/value-tile-responsible-magenta.png`; official magenta square with white line icon | own (official My Clinic brand asset) | Decorative; the tab label carries the value name. | Yes |
| `brand-value-tile-ambitious-teal` | image | Supplied `00_program/brand/assets/value-tile-ambitious-teal.png`; official teal square with white line icon | own (official My Clinic brand asset) | Decorative; the tab label carries the value name. | Yes |
| `brand-value-tile-caring-purple` | image | Supplied `00_program/brand/assets/value-tile-caring-purple.png`; official Caring purple square with white line icon | own (official My Clinic brand asset) | Decorative; the tab label carries the value name. | Yes |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | 4 tabs: `collaborative`, `responsible`, `ambitious`, `caring` |
| Correct answer(s) | n/a |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, direct |
| Target seconds | 40 |
| Word count / est. seconds | 81 words / ≈ 36.7 s (speaker labels excluded, pauses included) |
| Cue targets | `intro`, `collab`, `resp`, `amb`, `care` |

> OMAR: [[cue:intro]] Every clinic has values on a wall. Ours only matter if you can see them in what people do. [[pause:0.4]] [[cue:collab]] Collaborative: we act together, treat everyone with respect, and stay transparent. [[pause:0.4]] [[cue:resp]] Responsible: own your decisions, make things happen, and hold each other to the same standard. [[pause:0.4]] [[cue:amb]] Ambitious: go above and beyond, and challenge the status quo when it stops serving patients. [[pause:0.4]] [[cue:care]] Caring: act with empathy, because everyone matters. [[pause:0.4]] As you go on, think which of these you already do without being asked.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Tabs follow the ARIA tab pattern: arrow keys move between tabs, Enter/Space activates |
| Not colour-only | Active state = underline + `aria-selected` + heavier weight, not colour alone |
| Captions / transcript | `narration_text` present; all tab text is real HTML text |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "tabs",
  "id": "hr-010",
  "title": "Our four values",
  "section": "B · Our values & strategy",
  "node_id": "hr-sB",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>Values are behaviours. Open each one and look for something you already do.</p>",
  "tabs": [
    {
      "label": "Collaborative",
      "body_html": "<p><strong>Unites diverse</strong></p><p>Act together · Treat everyone with respect · Be transparent · Embrace diverse perspectives · Deliver outstanding results</p>",
      "image_asset_id": "<brand-value-tile-collaborative-burgundy>",
      "image_alt": "Decorative icon."
    },
    {
      "label": "Responsible",
      "body_html": "<p><strong>Creating a culture of accountability</strong></p><p>Own our decisions and actions · Make things happen · Demonstrate high professional standards · Hold yourself and each other accountable</p>",
      "image_asset_id": "<brand-value-tile-responsible-magenta>",
      "image_alt": "Decorative icon."
    },
    {
      "label": "Ambitious",
      "body_html": "<p><strong>Set new standards</strong></p><p>Go above and beyond · Make new possibilities happen · Challenge the status quo · Become industry shapers · Deliver outstanding results</p>",
      "image_asset_id": "<brand-value-tile-ambitious-teal>",
      "image_alt": "Decorative icon."
    },
    {
      "label": "Caring",
      "body_html": "<p><strong>Putting empathy first</strong></p><p>Act with empathy · Everyone matters · Love our customers · Deliver with quality</p>",
      "image_asset_id": "<brand-value-tile-caring-purple>",
      "image_alt": "Decorative icon."
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-010>",
  "narration_text": "OMAR: Every clinic has values on a wall. Ours only matter if you can see them in what people do. Collaborative: we act together, treat everyone with respect, and stay transparent. Responsible: own your decisions, make things happen, and hold each other to the same standard. Ambitious: go above and beyond, and challenge the status quo when it stops serving patients. Caring: act with empathy, because everyone matters. As you go on, think which of these you already do without being asked."
}
```

#### 8. Notes for SME and developer

- Open questions: None. All eight action phrases are verbatim from slide 9.
- Developer notes: import the four supplied `value-tile-*.png` files from `00_program/brand/assets/` as four assets. Keep the tabs’ value names as HTML text; the square tiles are decorative icon art.

---

### `hr-011` — Values in action

**Status:** `Draft — ready for SME review` · **Section / node:** B · Our values & strategy / `hr-sB` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: recognise the four values in real workplace behaviour |
| Objective(s) | `hr-o1` |
| On-the-job action | A1 |
| Source | `HR.pptx` slide 9 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Values in action |
| Body / keywords | Six things people did this week. Match each one to the value behind it. |
| Word count (excl. title) | 12 |
| Instruction | Match each action to a value. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "B · Our values & strategy · Check", 2 px navy `#003867` header rule |
| Visual concept | Two columns: six plain white action cards on the left, four value tiles on the right; a drawn connector line follows the learner's pointer while a card is selected |
| edumints layout | n/a (`matching`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (text and value-colour badge cards) |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only interaction).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Pairs (left → right) | `p1` “You admit a scheduling mistake to your manager and fix it.” → Responsible · `p2` “You ask a colleague in another department for their view before you decide.” → Collaborative · `p3` “You stay with an anxious patient until the nurse arrives.” → Caring · `p4` “You suggest a faster way to book follow-up appointments.” → Ambitious · `p5` “You share the reason for a delay with the team instead of staying quiet.” → Collaborative · `p6` “You check your own work against the professional standard before you sign it off.” → Responsible |
| Correct answer(s) | As listed above. Values repeat: Responsible ×2, Collaborative ×2, Caring ×1, Ambitious ×1. |
| Points | 10 |
| Feedback — correct | Right. Notice that Responsible and Collaborative each appear twice: the values overlap in real work, and one action can show more than one. |
| Feedback — incorrect | Not all six. Read each action again and ask what the person was actually choosing to do — own it, involve others, reach further, or care for someone. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once (phase-3 §5) |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 6.9 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Here are six things people did this week. Match each one to the value behind it.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each left card is a selectable list item; the right tiles are reachable by Tab and activated with Enter/Space |
| Not colour-only | Result state uses a tick/cross glyph plus the words Correct / Not this one, not colour alone |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "matching",
  "id": "hr-011",
  "title": "Values in action",
  "section": "B · Our values & strategy",
  "node_id": "hr-sB",
  "objective_ids": [
    "hr-o1"
  ],
  "points": 10,
  "evidence_screen_ids": [
    "hr-010"
  ],
  "prompt_html": "<p>Six things people did this week. Match each one to the value behind it.</p>",
  "pairs": [
    {
      "id": "p1",
      "left_html": "You admit a scheduling mistake to your manager and fix it.",
      "right_html": "Responsible"
    },
    {
      "id": "p2",
      "left_html": "You ask a colleague in another department for their view before you decide.",
      "right_html": "Collaborative"
    },
    {
      "id": "p3",
      "left_html": "You stay with an anxious patient until the nurse arrives.",
      "right_html": "Caring"
    },
    {
      "id": "p4",
      "left_html": "You suggest a faster way to book follow-up appointments.",
      "right_html": "Ambitious"
    },
    {
      "id": "p5",
      "left_html": "You share the reason for a delay with the team instead of staying quiet.",
      "right_html": "Collaborative"
    },
    {
      "id": "p6",
      "left_html": "You check your own work against the professional standard before you sign it off.",
      "right_html": "Responsible"
    }
  ],
  "feedback": {
    "correct_html": "<p>Right. Notice that Responsible and Collaborative each appear twice: the values overlap in real work, and one action can show more than one.</p>",
    "incorrect_html": "<p>Not all six. Read each action again and ask what the person was actually choosing to do — own it, involve others, reach further, or care for someone.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-011>",
  "narration_text": "OMAR: Here are six things people did this week. Match each one to the value behind it."
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: `matching` scores all-or-nothing on the pair set. If HR wants partial credit, change the type to six `mcq` screens — that changes the scored-screen count in phase-4 §3, so it needs a plan change first.

---

### `hr-012` — The 7C strategy

**Status:** `Draft — ready for SME review` · **Section / node:** B · Our values & strategy / `hr-sB` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: where the company is going, and which pillar the learner's own role touches most |
| Objective(s) | — (supports `hr-o1`, assessed on `hr-013`) |
| On-the-job action | A2 |
| Source | `HR.pptx` slide 10 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The 7C strategy |
| Body / keywords | Seven pillars. Open the ones your role touches — you're not expected to memorise all seven. |
| Word count (excl. title) | 15 |
| Instruction | Open each pillar. |

| Panel | Headline | Key points shown |
|---|---|---|
| Closer | Convenient & easy access | Convenient physical access · Community clinics & HHC · Digital access & services · Call centre & telemedicine |
| Cure | Tackle the biggest healthcare challenge | The best Saudi doctors · Focus on clinical outcomes · Centres of excellence · Prevention & wellbeing |
| Capabilities | A repeatable business model | Repeatable operations & expansion · Robust governance & compliance · Peopleware, software, hardware · Competitive cost to serve |
| Culture | The way we do things around here | Mission, values & beliefs · Servant leadership · A culture of excellence |
| Clinicians | An attractive doctor value proposition | Caring environment · Competitive benefits · Growth & development |
| Care | A legendary service & care | Seamless experience · Empathy & compassion · Loyalty through My Care · Service & advocacy mindset |
| Cost | Competitive cost to serve | Revenue-cycle management · Operational efficiency · Overhead management |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "B · Our values & strategy", 2 px navy `#003867` header rule |
| Visual concept | Seven collapsed rows in a single column, each with a line icon, the pillar name in caps and a chevron; expanding a row reveals the headline line and the key points as a wrapped keyword row |
| edumints layout | n/a (`accordion`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Seven single-weight line icons (`hr-img-7c-icons`: headset, syringe, mind-and-gears, handshake, stethoscope, heart-hands, coins), Caring purple #652D8C, own SVG |
| Animation / reveal | Panel body expands with a 200 ms height transition |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-7c-icons` | SVG ×7 | Line icons redrawn from slide 10: headset (Closer), syringe (Cure), mind-and-gears (Capabilities), handshake (Culture), stethoscope (Clinicians), heart-hands (Care), coins (Cost) | own | Decorative — each panel is labelled in text. | Yes |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | 7 panels: `closer`, `cure`, `capabilities`, `culture`, `clinicians`, `care`, `cost` |
| Correct answer(s) | n/a |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm, clear |
| Target seconds | 45 |
| Word count / est. seconds | 99 words / ≈ 45.6 s (speaker labels excluded, pauses included) |
| Cue targets | `intro`, `closer`, `cure`, `cap`, `culture`, `clin`, `care`, `cost` |

> OMAR: [[cue:intro]] Strategy feels like someone else's job until you find your own work inside it. Here are the seven pillars. [[pause:0.4]] [[cue:closer]] Closer: convenient access — clinics, community clinics and home health care, digital services, telemedicine. [[pause:0.4]] [[cue:cure]] Cure: the best Saudi doctors, clinical outcomes, centres of excellence, prevention and wellbeing. [[pause:0.4]] [[cue:cap]] Capabilities: a repeatable model for running and growing clinics, with real governance. [[pause:0.4]] [[cue:culture]] Culture: our mission and values, servant leadership, a culture of excellence. [[pause:0.4]] [[cue:clin]] Clinicians: a caring environment, competitive benefits, room to grow. [[pause:0.4]] [[cue:care]] Care: seamless experience, empathy, loyalty built through My Care. [[pause:0.4]] [[cue:cost]] Cost: competitive cost to serve. [[pause:0.4]] Whichever one you picked, that's your line in.

New lexicon terms: My Care — “my care” (plain words, no expansion needed)

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each header is a native `<button>` with `aria-expanded`; Enter/Space toggles |
| Not colour-only | Open state uses the chevron rotation plus `aria-expanded`, not colour alone |
| Captions / transcript | `narration_text` present; all seven panels are real HTML text |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "accordion",
  "id": "hr-012",
  "title": "The 7C strategy",
  "section": "B · Our values & strategy",
  "node_id": "hr-sB",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>Seven pillars. Open the ones your role touches — you're not expected to memorise all seven.</p>",
  "items": [
    {
      "title": "Closer",
      "body_html": "<p><strong>Convenient &amp; easy access</strong></p><p>Convenient physical access · Community clinics &amp; HHC · Digital access &amp; services · Call centre &amp; telemedicine</p>",
      "image_asset_id": "<hr-img-7c-closer>",
      "image_alt": "Decorative icon."
    },
    {
      "title": "Cure",
      "body_html": "<p><strong>Tackle the biggest healthcare challenge</strong></p><p>The best Saudi doctors · Focus on clinical outcomes · Centres of excellence · Prevention &amp; wellbeing</p>",
      "image_asset_id": "<hr-img-7c-cure>",
      "image_alt": "Decorative icon."
    },
    {
      "title": "Capabilities",
      "body_html": "<p><strong>A repeatable business model</strong></p><p>Repeatable operations &amp; expansion · Robust governance &amp; compliance · Peopleware, software, hardware · Competitive cost to serve</p>",
      "image_asset_id": "<hr-img-7c-capabilities>",
      "image_alt": "Decorative icon."
    },
    {
      "title": "Culture",
      "body_html": "<p><strong>The way we do things around here</strong></p><p>Mission, values &amp; beliefs · Servant leadership · A culture of excellence</p>",
      "image_asset_id": "<hr-img-7c-culture>",
      "image_alt": "Decorative icon."
    },
    {
      "title": "Clinicians",
      "body_html": "<p><strong>An attractive doctor value proposition</strong></p><p>Caring environment · Competitive benefits · Growth &amp; development</p>",
      "image_asset_id": "<hr-img-7c-clinicians>",
      "image_alt": "Decorative icon."
    },
    {
      "title": "Care",
      "body_html": "<p><strong>A legendary service &amp; care</strong></p><p>Seamless experience · Empathy &amp; compassion · Loyalty through My Care · Service &amp; advocacy mindset</p>",
      "image_asset_id": "<hr-img-7c-care>",
      "image_alt": "Decorative icon."
    },
    {
      "title": "Cost",
      "body_html": "<p><strong>Competitive cost to serve</strong></p><p>Revenue-cycle management · Operational efficiency · Overhead management</p>",
      "image_asset_id": "<hr-img-7c-cost>",
      "image_alt": "Decorative icon."
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-012>",
  "narration_text": "OMAR: Strategy feels like someone else's job until you find your own work inside it. Here are the seven pillars. Closer: convenient access — clinics, community clinics and home health care, digital services, telemedicine. Cure: the best Saudi doctors, clinical outcomes, centres of excellence, prevention and wellbeing. Capabilities: a repeatable model for running and growing clinics, with real governance. Culture: our mission and values, servant leadership, a culture of excellence. Clinicians: a caring environment, competitive benefits, room to grow. Care: seamless experience, empathy, loyalty built through My Care. Cost: competitive cost to serve. Whichever one you picked, that's your line in."
}
```

#### 8. Notes for SME and developer

- Open questions: None. All key points are verbatim from slide 10. HHC is expanded on first use in the narration.
- Developer notes: seven panels is inside the 3–9 range in the screen-type guide.

---

### `hr-013` — Which pillar?

**Status:** `Draft — ready for SME review` · **Section / node:** B · Our values & strategy / `hr-sB` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: pick the pillar a real activity belongs to, with plausible neighbouring pillars as distractors |
| Objective(s) | `hr-o1` |
| On-the-job action | A2 |
| Source | `HR.pptx` slide 10 (Care · “Build loyalty through My Care”) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Which pillar? |
| Body / keywords | *(stem only — see prompt below)* |
| Word count (excl. title) | 0 (the stem is the prompt, not body copy) |
| Instruction | Choose one. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "B · Our values & strategy · Check", 2 px navy `#003867` header rule |
| Visual concept | Stem in large type at the top; four plain option rows beneath, each a radio control plus a single sentence; no imagery, so the decision is the only thing on screen |
| edumints layout | n/a (`mcq`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only question).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “My Care follow-up calls that build patient loyalty support which pillar?” |
| Options | `a` **Care** ✔ · `b` Closer · `c` Culture · `d` Cost |
| Correct answer(s) | `a` — Care |
| Points | 5 |
| Feedback — correct | Care. My Care follow-up calls are named in the Care pillar under “build loyalty through My Care”. Loyalty is a service and relationship outcome, not an access outcome. |
| Feedback — incorrect | Not quite. Closer is about *access* — physical, community, digital and telemedicine. Culture is mission, values and leadership. Cost is efficiency. The pillar that names My Care and loyalty is Care. |
| Per-option feedback | `a` Care — Correct. The Care pillar lists “build loyalty through My Care”. · `b` Closer — Closer covers *access*: physical, community and home health care, digital services, and the call centre and telemedicine. A phone call is access; a follow-up call that builds loyalty is Care. · `c` Culture — Culture is mission, values and servant leadership. It shapes how we behave, not this service. · `d` Cost — Cost is about cost to serve: revenue cycle, efficiency and overhead. Loyalty work sits on the service side. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 6.9 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: One to try. My Care follow-up calls build patient loyalty. Which pillar do they belong to?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native radio group; arrow keys move, Enter submits |
| Not colour-only | Correct/incorrect is shown with a glyph and the words, plus per-option text |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "hr-013",
  "title": "Which pillar?",
  "section": "B · Our values & strategy",
  "node_id": "hr-sB",
  "objective_ids": [
    "hr-o1"
  ],
  "points": 5,
  "evidence_screen_ids": [
    "hr-012"
  ],
  "prompt_html": "<p>My Care follow-up calls that build patient loyalty support which pillar?</p>",
  "options": [
    {
      "id": "a",
      "text_html": "Care",
      "correct": true,
      "feedback_html": "<p>Care. My Care follow-up calls are named in the Care pillar under “build loyalty through My Care”. Loyalty is a service and relationship outcome, not an access outcome.</p>"
    },
    {
      "id": "b",
      "text_html": "Closer",
      "feedback_html": "<p>Closer covers <em>access</em>: physical, community and home health care, digital services, and the call centre and telemedicine. A phone call is access; a follow-up call that builds loyalty is Care.</p>"
    },
    {
      "id": "c",
      "text_html": "Culture",
      "feedback_html": "<p>Culture is mission, values and servant leadership. It shapes how we behave, not this service.</p>"
    },
    {
      "id": "d",
      "text_html": "Cost",
      "feedback_html": "<p>Cost is about cost to serve: revenue cycle, efficiency and overhead. Loyalty work sits on the service side.</p>"
    }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Care. My Care follow-up calls are named in the Care pillar under “build loyalty through My Care”. Loyalty is a service and relationship outcome, not an access outcome.</p>",
    "incorrect_html": "<p>Not quite. Closer is about <em>access</em> — physical, community, digital and telemedicine. Culture is mission, values and leadership. Cost is efficiency. The pillar that names My Care and loyalty is Care.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-013>",
  "narration_text": "OMAR: One to try. My Care follow-up calls build patient loyalty. Which pillar do they belong to?"
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: none.

---

### `hr-014` — Who we serve

**Status:** `Draft — ready for SME review` · **Section / node:** B · Our values & strategy / `hr-sB` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the three groups we serve, including people who are healthy today |
| Objective(s) | — |
| On-the-job action | A1 |
| Source | `HR.pptx` slide 10 (“Who do we serve?”) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Who we serve |
| Body / keywords | Patients & families — sick or healthy · Community · Corporates & insurers |
| Word count (excl. title) | 10 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "B · Our values & strategy", 2 px navy `#003867` header rule |
| Visual concept | Three equal cards side by side, each with one line icon above a short label and a one-line caption; the first card is annotated “sick or healthy” in a smaller line |
| edumints layout | `text` |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Three single-weight line icons (`hr-img-serve-icons`: family group, community ring, briefcase-and-shield), navy #003867, own SVG |
| Animation / reveal | Cards fade up left to right in narration order |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-serve-icons` | SVG ×3 | Line icons: family group, community ring, briefcase-and-shield | own | Decorative — each card is labelled in text. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm |
| Target seconds | 20 |
| Word count / est. seconds | 44 words / ≈ 19.6 s (speaker labels excluded, pauses included) |
| Cue targets | `patients`, `community`, `corporates` |

> OMAR: [[cue:patients]] Who do we serve? First, patients and their families — sick or healthy. Many of the people who walk in today are well, and we want them to stay that way. [[pause:0.4]] [[cue:community]] Second, the community around each clinic. [[pause:0.3]] [[cue:corporates]] Third, corporates and insurers. Three groups, one standard.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed |
| Not colour-only | Labels are text; icons support only |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-014",
  "title": "Who we serve",
  "section": "B · Our values & strategy",
  "node_id": "hr-sB",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Patients &amp; families</strong> — sick or healthy</p><p><strong>Community</strong></p><p><strong>Corporates &amp; insurers</strong></p>",
  "narration_asset_id": "<hr-aud-014>",
  "narration_text": "OMAR: Who do we serve? First, patients and their families — sick or healthy. Many of the people who walk in today are well, and we want them to stay that way. Second, the community around each clinic. Third, corporates and insurers. Three groups, one standard.",
  "media_asset_id": "<hr-img-serve-icons>",
  "media_alt": "Three icons: patients and families, the wider community, and corporate and insurance partners."
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: three separate `<p>` elements so the reveal is paced per line.

---

### `hr-020` — Our story so far

**Status:** `Draft — ready for SME review` · **Section / node:** C · Our clinic / `hr-sC` · **Type:** `timeline` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: how one clinic in 2017 became a network, and what each step added |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slide 16 (company history timeline); branch codes cross-checked against slides 14–15 |
| Depends on Phase 0 | **B5 / D3** (branch names: Al Andalus vs Al Tahlia; Abhor vs Obhur) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Our story so far |
| Body / keywords | From one clinic in Jeddah to a network across the west and Riyadh. |
| Word count (excl. title) | 12 |
| Instruction | n/a |

**Events**

| Year | Title | Text (≤ 25 words) |
|---|---|---|
| 2017 | MCJ1 opens | Our first full-service outpatient clinic, in North Jeddah. |
| 2018 | New products | New products launched, widening what one clinic could offer. |
| 2019 | Corporate check-ups | The employment check-up unit starts — our first corporate service line. |
| 2021 | MCJ2 opens | Our second full-service outpatient clinic, in East Jeddah. |
| 2022 | Dental centre | My Clinic Dental (D1) opens in Jeddah. |
| 2023 | Petro-Rabigh | PRC opens — our first clinic inside a corporate community. |
| 2024 | Riyadh | R1 opens: a flagship clinic in Riyadh to establish the brand. |
| 2025 | ⚠ PENDING B5 / D3 | J3 opens — our first community clinic in Jeddah. *Name per B5/D3: Al Andalus (slide 15) or Al Tahlia (slide 16).* |
| 2026 | ⚠ PENDING B5 / D3 | J4 opens — our second community clinic in Jeddah. *Name per B5/D3: Abhor (slide 15) or Obhur (slide 16).* |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "C · Our clinic", 2 px navy `#003867` header rule |
| Visual concept | A single horizontal axis with nine year nodes; the active node lifts and its caption card slides in beneath the axis; a thin progress line fills as the learner moves along |
| edumints layout | n/a (`timeline`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (numbered year nodes on timeline) |
| Animation / reveal | Nodes appear in year order as the narration advances |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (branch photos, if cleared, sit on `hr-021`, not here).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | 9 events, 2017 → 2026 |
| Correct answer(s) | n/a |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, plain |
| Target seconds | 30 |
| Word count / est. seconds | 72 words / ≈ 32.1 s (speaker labels excluded, pauses included) |
| Cue targets | `e2017`, `e2019`, `e2023`, `e2024`, `e2025` |

> OMAR: We opened our first clinic in North Jeddah in 2017. [[cue:e2017]] [[pause:0.3]] In 2019 we started the employment check-up unit, [[cue:e2019]] our first corporate service. [[pause:0.3]] Then came East Jeddah, the dental centre, and Petro-Rabigh in 2023, [[cue:e2023]] our first clinic inside a corporate community. [[pause:0.3]] Riyadh followed in 2024, [[cue:e2024]] a flagship to put the brand on the map. [[pause:0.3]] The last two years added our first community clinics. [[cue:e2025]] Nine years, nine steps, one idea: bring good care closer.

New lexicon terms: PRC — “P-R-C”; MCJ1 — “M-C-J-one”; MCJ2 — “M-C-J-two”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each year node is a focusable button; arrow keys move along the timeline |
| Not colour-only | The year is printed on every node; the active state adds a caret, not just colour |
| Captions / transcript | `narration_text` present; every event's text is real HTML |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "timeline",
  "id": "hr-020",
  "title": "Our story so far",
  "section": "C · Our clinic",
  "node_id": "hr-sC",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>From one clinic in Jeddah to a network across the west and Riyadh.</p>",
  "events": [
    {
      "date": "2017",
      "title": "MCJ1 opens",
      "body_html": "<p>Our first full-service outpatient clinic, in North Jeddah.</p>"
    },
    {
      "date": "2018",
      "title": "New products",
      "body_html": "<p>New products launched, widening what one clinic could offer.</p>"
    },
    {
      "date": "2019",
      "title": "Corporate check-ups",
      "body_html": "<p>The employment check-up unit starts — our first corporate service line.</p>"
    },
    {
      "date": "2021",
      "title": "MCJ2 opens",
      "body_html": "<p>Our second full-service outpatient clinic, in East Jeddah.</p>"
    },
    {
      "date": "2022",
      "title": "Dental centre",
      "body_html": "<p>My Clinic Dental (D1) opens in Jeddah.</p>"
    },
    {
      "date": "2023",
      "title": "Petro-Rabigh",
      "body_html": "<p>PRC opens — our first clinic inside a corporate community.</p>"
    },
    {
      "date": "2024",
      "title": "Riyadh",
      "body_html": "<p>R1 opens: a flagship clinic in Riyadh to establish the brand.</p>"
    },
    {
      "date": "2025",
      "title": "J3 opens",
      "body_html": "<p>Our first community clinic in Jeddah. <em>Name pending decision B5 / D3.</em></p>"
    },
    {
      "date": "2026",
      "title": "J4 opens",
      "body_html": "<p>Our second community clinic in Jeddah. <em>Name pending decision B5 / D3.</em></p>"
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-020>",
  "narration_text": "OMAR: We opened our first clinic in North Jeddah in 2017. In 2019 we started the employment check-up unit, our first corporate service. Then came East Jeddah, the dental centre, and Petro-Rabigh in 2023, our first clinic inside a corporate community. Riyadh followed in 2024, a flagship to put the brand on the map. The last two years added our first community clinics. Nine years, nine steps, one idea: bring good care closer."
}
```

#### 8. Notes for SME and developer

- Open questions: **B5 / D3** — J3 and J4 branch names. The card deliberately shows the codes (J3, J4) and marks the names pending, because the codes are what staff use daily and both slides agree on them.
- Developer notes: the two pending events carry an inline `<em>` note in the body. Remove it the moment B5/D3 closes, and swap in the agreed name in the `title`.

---

### `hr-021` — Where we are

**Status:** `Draft — ready for SME review` · **Section / node:** C · Our clinic / `hr-sC` · **Type:** `hotspot` (`explore`) · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explore: connect the branch codes staff use every day to real places |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slides 14–15 (branch tables) |
| Depends on Phase 0 | **B5 / D3** (J3 / J4 names) · **B6 / D5** (branch photos) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Where we are |
| Body / keywords | Seven sites. You'll hear these codes every day — open each pin. |
| Word count (excl. title) | 11 |
| Instruction | Open all seven pins. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "C · Our clinic", 2 px navy `#003867` header rule |
| Visual concept | Minimal outline map of western Saudi Arabia with an inset for Riyadh; seven numbered pins; each pin opens a small card with the code, the branch type, the city and the year; a counter shows “3 of 7” |
| edumints layout | n/a (`hotspot`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Numbered map pin markers (1–7) in Caring purple #652D8C, own SVG |
| Animation / reveal | Pins pulse gently until opened, then settle |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-map` | SVG | 1200×800, simplified outline of the western region plus a Riyadh inset; no satellite detail; seven pin positions marked but pin graphics drawn by the player | own | Map of My Clinic sites: five in Jeddah, one in Petro-Rabigh, one in Riyadh. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Regions | `j1` rect — Jeddah, north-west of centre (top-left of the Jeddah cluster) · `j2` rect — Jeddah, east (right of the Jeddah cluster) · `d1` rect — Jeddah, centre-south · `j3` rect — Jeddah, south-west · `j4` rect — Jeddah, far south · `prc` circle — Rabigh, north along the coast · `r1` circle — Riyadh inset, centre |
| Correct answer(s) | n/a — explore mode, unscored |
| Points | 0 |
| Feedback per region | See the table below. |
| Hint | n/a |
| Retry / lives | n/a |

| Region | Card title | Card text |
|---|---|---|
| `j1` | J1 — North Jeddah | Our first full-service outpatient clinic. Opened 2017. |
| `j2` | J2 — East Jeddah | Our second full-service outpatient clinic. Opened 2021. |
| `d1` | D1 — Dental Centre | Our dental centre in Jeddah. Opened 2022. |
| `j3` | J3 — ⚠ PENDING B5 / D3 | Our first community clinic in Jeddah. Opened 2025. |
| `j4` | J4 — ⚠ PENDING B5 / D3 | Our second community clinic in Jeddah. Opened 2026. |
| `prc` | PRC — Petro-Rabigh | Our clinic in Petro-Rabigh. Opened 2023. |
| `r1` | R1 — Riyadh | Our first clinic in Riyadh — a flagship. Opened 2024. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, practical |
| Target seconds | 15 |
| Word count / est. seconds | 31 words / ≈ 13.3 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: You'll hear these codes every day, so it's worth knowing what they mean. Open all seven pins. J one, J two, D one, J three, J four, P-R-C and R one.

New lexicon terms: J1 — “J-one”; J2 — “J-two”; J3 — “J-three”; J4 — “J-four”; D1 — “D-one”; R1 — “R-one”; PRC — “P-R-C”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Pins are focusable buttons in DOM order (J1 → R1); Enter opens, Escape closes the card |
| Not colour-only | Every pin is numbered and labelled; visited pins show a filled dot plus a check glyph |
| Captions / transcript | `narration_text` present; the seven cards are also listed as text in the screen's fallback list |
| Timing | Untimed; `require_all` gates Continue, not a timer |

#### 7. Build fields (edumints)

```json
{
  "type": "hotspot",
  "id": "hr-021",
  "title": "Where we are",
  "section": "C · Our clinic",
  "node_id": "hr-sC",
  "objective_ids": [],
  "points": 0,
  "image_asset_id": "<hr-img-map>",
  "image_alt": "Map of My Clinic sites: five in Jeddah, one in Petro-Rabigh, one in Riyadh.",
  "mode": "explore",
  "require_all": true,
  "prompt_html": "<p>Seven sites. You'll hear these codes every day — open each pin.</p>",
  "regions": [
    {
      "id": "j1",
      "shape": "rect",
      "coords": [
        300,
        150,
        90,
        60
      ],
      "label_html": "J1 — North Jeddah",
      "feedback_html": "<p>Our first full-service outpatient clinic. Opened 2017.</p>"
    },
    {
      "id": "j2",
      "shape": "rect",
      "coords": [
        430,
        190,
        90,
        60
      ],
      "label_html": "J2 — East Jeddah",
      "feedback_html": "<p>Our second full-service outpatient clinic. Opened 2021.</p>"
    },
    {
      "id": "d1",
      "shape": "rect",
      "coords": [
        350,
        250,
        90,
        60
      ],
      "label_html": "D1 — Dental Centre",
      "feedback_html": "<p>Our dental centre in Jeddah. Opened 2022.</p>"
    },
    {
      "id": "j3",
      "shape": "rect",
      "coords": [
        280,
        300,
        90,
        60
      ],
      "label_html": "J3 — community clinic",
      "feedback_html": "<p>Our first community clinic in Jeddah. Opened 2025. Name pending decision B5 / D3.</p>"
    },
    {
      "id": "j4",
      "shape": "rect",
      "coords": [
        300,
        380,
        90,
        60
      ],
      "label_html": "J4 — community clinic",
      "feedback_html": "<p>Our second community clinic in Jeddah. Opened 2026. Name pending decision B5 / D3.</p>"
    },
    {
      "id": "prc",
      "shape": "circle",
      "coords": [
        250,
        470,
        32
      ],
      "label_html": "PRC — Petro-Rabigh",
      "feedback_html": "<p>Our clinic in Petro-Rabigh. Opened 2023.</p>"
    },
    {
      "id": "r1",
      "shape": "circle",
      "coords": [
        980,
        300,
        32
      ],
      "label_html": "R1 — Riyadh",
      "feedback_html": "<p>Our first clinic in Riyadh — a flagship. Opened 2024.</p>"
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-021>",
  "narration_text": "OMAR: You'll hear these codes every day, so it's worth knowing what they mean. Open all seven pins. J one, J two, D one, J three, J four, P-R-C and R one.",
  "feedback": {
    "correct_html": "<p>You have explored all seven My Clinic branches across Jeddah, Rabigh and Riyadh.</p>",
    "incorrect_html": "<p>Select each branch pin on the map to explore all seven sites.</p>",
    "show_correct_answer": true
  }
}
```

#### 8. Notes for SME and developer

- Open questions: **B5 / D3** (J3, J4 names) · **B6 / D5** (branch photos — the plan allows photos inside the pin cards once rights and consents are confirmed; without them the cards are text-only, which is the default build).
- Developer notes: `coords` for `rect` are `[x, y, w, h]` and for `circle` `[cx, cy, r]`, in the image's natural pixels. The values above are provisional against a 1200×800 map and must be re-set after the final SVG is drawn. `require_all` is only valid with `mode: "explore"` — do not switch this screen to quiz mode without also removing `require_all`.

---

### `hr-022` — Meet our leaders

**Status:** `Draft — ready for SME review` · **Section / node:** C · Our clinic / `hr-sC` · **Type:** `content_slide` (`blocks`) · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: who leads the company and what each role looks after |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slides 12–13 |
| Depends on Phase 0 | **B6 / D5** (photos and names need consent; the fallback is roles only) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Meet our leaders |
| Body / keywords | Chief Executive Officer · Chief Medical Officer · Chief Operating Officer · Chief Finance Officer |
| Word count (excl. title) | 12 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "C · Our clinic", 2 px navy `#003867` header rule |
| Visual concept | Four portrait cards in one row; each is a soft-cornered square with the role printed under it and a one-line “looks after” caption; no names until consent is recorded |
| edumints layout | `text` (blocks: caption, image, caption, image …) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (portrait / monogram role cards) |
| Animation / reveal | Cards fade up left to right in narration order |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-leaders-ceo` | photo | Consented portrait, 800×800, neutral studio background | local (consent on file — B6) | “Abdullah Alghamdi, Chief Executive Officer.” | No |
| `hr-img-leaders-cmo` | photo | Consented portrait, 800×800 | local (consent on file — B6) | “Dr Ahmed Al Zahrani, Chief Medical Officer.” | No |
| `hr-img-leaders-coo` | photo | Consented portrait, 800×800 | local (consent on file — B6) | “Hesham Abdulwahab, Chief Operating Officer.” | No |
| `hr-img-leaders-cfo` | photo | Consented portrait, 800×800 | local (consent on file — B6) | “Richard Thompson, Chief Finance Officer.” | No |

**Fallback if B6 is not closed:** replace each photo block with a monogram tile (the initials in brand `primary`), keep the role text, and drop the names. The screen then carries no personal data.

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, factual |
| Target seconds | 20 |
| Word count / est. seconds | 46 words / ≈ 20.8 s (speaker labels excluded, pauses included) |
| Cue targets | `ceo`, `cmo`, `coo`, `cfo` |

> OMAR: [[cue:ceo]] Four people lead the company. The CEO sets the direction. [[pause:0.4]] [[cue:cmo]] The CMO owns clinical standards — questions about how we practise medicine land here. [[pause:0.4]] [[cue:coo]] The COO runs the clinics day to day. [[pause:0.3]] [[cue:cfo]] The CFO looks after the money. You'll see their decisions in how your clinic runs.

New lexicon terms: CEO — “C-E-O”; CMO — “C-M-O”; COO — “C-O-O”; CFO — “C-F-O” (each role is also named in full in the on-screen text)

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed; blocks readable in DOM order |
| Not colour-only | Role names are printed text under each portrait |
| Captions / transcript | `narration_text` present; each portrait has alt text |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-022",
  "title": "Meet our leaders",
  "section": "C · Our clinic",
  "node_id": "hr-sC",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "blocks": [
    {
      "html": "<p>Chief Executive Officer — sets the direction and answers to the board.</p>"
    },
    {
      "asset_id": "<hr-img-leaders-ceo>",
      "caption": "Abdullah Alghamdi, Chief Executive Officer. Portrait pending consent B6."
    },
    {
      "html": "<p>Chief Medical Officer — owns clinical standards and outcomes.</p>"
    },
    {
      "asset_id": "<hr-img-leaders-cmo>",
      "caption": "Dr Ahmed Al Zahrani, Chief Medical Officer. Portrait pending consent B6."
    },
    {
      "html": "<p>Chief Operating Officer — runs the clinics day to day.</p>"
    },
    {
      "asset_id": "<hr-img-leaders-coo>",
      "caption": "Hesham Abdulwahab, Chief Operating Officer. Portrait pending consent B6."
    },
    {
      "html": "<p>Chief Finance Officer — looks after the money that makes it possible.</p>"
    },
    {
      "asset_id": "<hr-img-leaders-cfo>",
      "caption": "Richard Thompson, Chief Finance Officer. Portrait pending consent B6."
    }
  ],
  "narration_asset_id": "<hr-aud-022>",
  "narration_text": "OMAR: Four people lead the company. The CEO sets the direction. The CMO owns clinical standards — questions about how we practise medicine land here. The COO runs the clinics day to day. The CFO looks after the money. You'll see their decisions in how your clinic runs."
}
```

#### 8. Notes for SME and developer

- Open questions: **B6 / D5** — consent for the four portraits and names. Until it closes, ship the monogram-tile fallback and delete the name strings from the captions.
- Developer notes: all `blocks` reveal as **one** unit. If HR wants the leaders to appear one at a time, split this into four `content_slide` screens — that changes the screen count, so it needs a plan change first.

---

### `hr-023` — What we've been recognised for

**Status:** `Draft — ready for SME review` · **Section / node:** C · Our clinic / `hr-sC` · **Type:** `flashcards` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explore: the accreditation and awards, and the point that they have to be re-earned |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slides 17–18 |
| Depends on Phase 0 | **B7** (accreditation and award wording; the JCI claim must be verifiable) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | What we've been recognised for |
| Body / keywords | Flip each card. Accreditation is measured, not given — and it has to be earned again. |
| Word count (excl. title) | 13 |
| Instruction | Flip each card. |

**Cards** (front ≤ 6 words, back ≤ 30 words)

| # | Front | Back |
|---|---|---|
| 1 | CBAHI accreditation | Accredited by CBAHI, the Central Board for Accreditation of Healthcare Institutions. MCJ1 scored 98.67 in 2022 and MCJ2 scored 100 in 2023. ⚠ PENDING B7 |
| 2 | Best Clinical Patient Outcome | Best Clinical Patient Outcome, 2019–2020. ⚠ PENDING B7 |
| 3 | Best new clinic for customer service | Best new clinic for customer service, 2018. ⚠ PENDING B7 |
| 4 | Best New Premium Clinic | Best New Premium Clinic, 2018–19. ⚠ PENDING B7 |
| 5 | Most innovative corporate wellness initiative | Most innovative corporate wellness initiative in Saudi Arabia, 2019. ⚠ PENDING B7 |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "C · Our clinic", 2 px navy `#003867` header rule |
| Visual concept | Five cards in a shallow fan across the middle of the stage; flipping one rotates it on its vertical axis to reveal the back; the flipped card stays face-up and slides to the back of the fan |
| edumints layout | n/a (`flashcards`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Two single-weight line icons (`hr-img-award-icons`: trophy and laurel star), Caring purple #652D8C, own SVG |
| Animation / reveal | 300 ms vertical-axis flip, respects `prefers-reduced-motion` by cross-fading instead |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-award-icons` | SVG ×2 | Two line icons redrawn from slides 17–18: a trophy and a laurel star | own | Decorative — each card front is labelled in text. | Yes |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | 5 cards, `c1`–`c5` |
| Correct answer(s) | n/a |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Warm, honest |
| Target seconds | 15 |
| Word count / est. seconds | 39 words / ≈ 16.7 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: We're proud of these, so flip them. And hold one thought alongside them. Accreditation is measured, not given. Every score here expires, and the next survey team will look at what we did this year, not at these cards.

New lexicon terms: CBAHI — “see-bah-hee”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each card is a focusable button; Enter/Space flips; both faces are in the DOM |
| Not colour-only | Card fronts are text; the flip control carries a rotate glyph |
| Captions / transcript | `narration_text` present; all card text is real HTML |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "flashcards",
  "id": "hr-023",
  "title": "What we've been recognised for",
  "section": "C · Our clinic",
  "node_id": "hr-sC",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>Flip each card. Accreditation is measured, not given — and it has to be earned again.</p>",
  "cards": [
    {
      "front_html": "CBAHI accreditation",
      "back_html": "Accredited by CBAHI, the Central Board for Accreditation of Healthcare Institutions. MCJ1 scored 98.67 in 2022 and MCJ2 scored 100 in 2023. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-star>",
      "front_alt": "Decorative icon."
    },
    {
      "front_html": "Best Clinical Patient Outcome",
      "back_html": "Best Clinical Patient Outcome, 2019–2020. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-trophy>",
      "front_alt": "Decorative icon."
    },
    {
      "front_html": "Best new clinic for customer service",
      "back_html": "Best new clinic for customer service, 2018. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-star>",
      "front_alt": "Decorative icon."
    },
    {
      "front_html": "Best New Premium Clinic",
      "back_html": "Best New Premium Clinic, 2018–19. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-trophy>",
      "front_alt": "Decorative icon."
    },
    {
      "front_html": "Most innovative corporate wellness initiative",
      "back_html": "Most innovative corporate wellness initiative in Saudi Arabia, 2019. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-star>",
      "front_alt": "Decorative icon."
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-023>",
  "narration_text": "OMAR: We're proud of these, so flip them. And hold one thought alongside them. Accreditation is measured, not given. Every score here expires, and the next survey team will look at what we did this year, not at these cards."
}
```

#### 8. Notes for SME and developer

- Open questions: **B7** — the exact awarding body, year and wording for all five cards, and the JCI claim read from slide 18. The JCI claim is **excluded** from this card set until Comms confirms it in writing.
- Developer notes: drop the `<em>Pending B7.</em>` strings the moment B7 closes. If any award cannot be verified, delete that card rather than keep it — the remaining set still works at four cards.

---

### `hr-030` — Our code of ethics

**Status:** `Draft — ready for SME review` · **Section / node:** D · Ethics & patients' rights / `hr-sD` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the four ethics values, and the one rule to follow when a situation is unclear |
| Objective(s) | — (teaches `hr-o2`, assessed on `hr-031`) |
| On-the-job action | A3 |
| Source | `HR.pptx` slides 20–22 |
| Depends on Phase 0 | **B14 / D8** (the 24-hour incident-report window) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Our code of ethics |
| Body / keywords | Respect · Integrity · Accountability · Innovation & collaboration · **Ethical dilemma? Incident report within 24 hours + ethics team.** |
| Word count (excl. title) | 16 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "D · Ethics & patients' rights", 2 px navy `#003867` header rule |
| Visual concept | Four value blocks in a 2×2 grid with one line icon each; a single full-width warning strip below the grid carries the 24-hour rule, set in `dark` on an `accent`-tinted panel, with an exclamation icon so the meaning is not carried by colour |
| edumints layout | `text` |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C`) · warning `accent` (Responsible magenta `#9D3293` on the key rule/figure callout only) |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Four single-weight line icons (`hr-img-ethics-icons`) in navy #003867 + exclamation warning icon in magenta #9D3293, own SVG |
| Animation / reveal | Grid blocks fade up one by one, then the strip slides up last |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-ethics-icons` | SVG ×4 | Line icons: two people with a heart (Respect), open hand with a tick (Integrity), clipboard with a check (Accountability), lightbulb with a link (Innovation and collaboration) | own | Decorative — each value is labelled in text. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Serious, warm |
| Target seconds | 35 |
| Word count / est. seconds | 78 words / ≈ 35.1 s (speaker labels excluded, pauses included) |
| Cue targets | `respect`, `integrity`, `accountability`, `innovation`, `report` |

> OMAR: [[cue:respect]] Four values sit under everything. Respect — the rights, privacy and dignity of patients, families and colleagues. [[pause:0.4]] [[cue:integrity]] Integrity — be transparent, and disclose any conflict of interest. [[pause:0.4]] [[cue:accountability]] Accountability — a culture where people report safety concerns instead of staying quiet. [[pause:0.4]] [[cue:innovation]] Innovation and collaboration — research and community work that improves outcomes. [[pause:0.5]] [[cue:report]] And the rule you'll use: faced with an ethical dilemma, complete an incident report within twenty-four hours and bring in the ethics team. You're never expected to work it out alone.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed |
| Not colour-only | The 24-hour strip carries an icon and the words “within 24 hours”; the tint alone never carries meaning |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-030",
  "title": "Our code of ethics",
  "section": "D · Ethics & patients' rights",
  "node_id": "hr-sD",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Respect</strong> — uphold the rights, privacy and dignity of patients, families and colleagues.</p><p><strong>Integrity</strong> — transparent practice; disclose any potential conflict of interest.</p><p><strong>Accountability</strong> — a culture that encourages reporting safety concerns and adherence to policy.</p><p><strong>Innovation &amp; collaboration</strong> — support research and community engagement to improve quality and outcomes.</p><p><strong>Ethical dilemma? Incident report within 24 hours + ethics team.</strong> <em>Pending B14 / D8.</em></p>",
  "narration_asset_id": "<hr-aud-030>",
  "narration_text": "OMAR: Four values sit under everything. Respect — the rights, privacy and dignity of patients, families and colleagues. Integrity — be transparent, and disclose any conflict of interest. Accountability — a culture where people report safety concerns instead of staying quiet. Innovation and collaboration — research and community work that improves outcomes. And the rule you'll use: faced with an ethical dilemma, complete an incident report within twenty-four hours and bring in the ethics team. You're never expected to work it out alone.",
  "media_asset_id": "<hr-img-ethics-icons>",
  "media_alt": "Four icons for Respect, Integrity, Accountability, and Innovation and collaboration."
}
```

#### 8. Notes for SME and developer

- Open questions: **B14 / D8** — the 24-hour window must match the wording used in module 07. Until it closes, the strip carries an inline `<em>Pending B14 / D8.</em>` note.
- Developer notes: none.

---

### `hr-031` — A supplier you know

**Status:** `Draft — ready for SME review` · **Section / node:** D · Ethics & patients' rights / `hr-sD` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: disclose a conflict of interest, resist a queue-jumping request, and use the 24-hour route when unsure |
| Objective(s) | `hr-o2` |
| On-the-job action | A3 |
| Source | `HR.pptx` slides 20–21 (Integrity, Accountability, ethical decision-making and reporting) |
| Depends on Phase 0 | **B14 / D8** (24-hour incident report) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | A supplier you know |
| Body / keywords | Three moments, three decisions. Nobody is watching. |
| Word count (excl. title) | 7 |
| Instruction | Choose what you would do at each step. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario (see `../../00_program/brand/screen-mockups/05-scenario.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "D · Ethics & patients' rights", 2 px navy `#003867` header rule |
| Visual concept | A flat-illustration band across the top that changes with the node — a meeting room, then a corridor, then a quiet desk; the situation text sits on a white card below it and the choices are full-width buttons under that |
| edumints layout | n/a (`decision_scenario`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` stage and choice cards with `#D9E1E8` border) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` progress bar) · companion avatar ring in the character's colour (companions.md §4) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; situation Montserrat SemiBold 600, 17 px; choices Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (flat scene illustrations + companion avatar) |
| Animation / reveal | The situation card fades up on each node change |
| Companion | Noor · `char-noor-avatar-neutral` above each situation card, swapping to `char-noor-avatar-happy` after the best choice and `char-noor-avatar-concern` after any other choice (shown in the feedback line, after the learner has chosen) · placement L5 avatar, 56 px circle with a 3 px Caring purple `#652D8C` ring, label “Noor · Safety liaison” beside it, above the situation card; never on or beside the choice buttons · tip text n/a · speaks: Noor (scenario host) |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-ethics-meeting` | illustration | Flat meeting-room scene: table, four chairs, a laptop and a document; two brand colours | ai-generated | “A small meeting room where a supplier evaluation is being discussed.” | No |
| `hr-img-ethics-corridor` | illustration | Flat corridor scene: reception desk and a queue of two patients | ai-generated | “A clinic corridor with a reception desk and two patients waiting.” | No |
| `hr-img-ethics-desk` | illustration | Flat desk scene: laptop showing a blank report form, a cup, a notebook | ai-generated | “A desk with a laptop open on an incident report form.” | No |
| `char-noor-avatar-neutral` | illustration | Shared programme avatar (Canva media `MAHX-n4HuyU`), cropped to a 56 px circle | ai-generated (programme master, companions.md §3) | “Noor, the safety liaison, listening.” | No |
| `char-noor-avatar-happy` | illustration | Programme avatar, cropped from `char-noor-success` (companions.md §3: “to make if needed”) | ai-generated (programme master) | “Noor, the safety liaison, smiling.” | No |
| `char-noor-avatar-concern` | illustration | Programme avatar, cropped from `char-noor-concern` (to make if needed) | ai-generated (programme master) | “Noor, the safety liaison, looking concerned.” | No |

**AI image prompt** (`hr-img-ethics-meeting`, `hr-img-ethics-corridor`, `hr-img-ethics-desk` — per `brand-identity.md` §6; the companion is **not** generated here — Noor's avatars are the shared programme assets, see [`companions.md`](../../00_program/characters/companions.md) §3):

```text
Flat vector illustration for a healthcare e-learning course, 16:9,
- Scene 1 (hr-img-ethics-meeting): a modern clinic meeting room with a conference table, four chairs, a closed laptop and a plain folder;
- Scene 2 (hr-img-ethics-corridor): a calm clinic reception desk and corridor with two waiting chairs;
- Scene 3 (hr-img-ethics-desk): a quiet staff desk with a laptop, a mug and a plain notebook.
Clean minimalist style, simple geometric shapes, thin navy (#003867) outlines, white and very light blue-grey (#F4F7FA, #C0CED9) surfaces, one highlight colour Caring purple (#652D8C), small touches of magenta (#9D3293) only for nothing. Modern Saudi outpatient clinic interior, bright and calm, lots of white space, soft even lighting, no shadows or very soft flat shadows.
People: none (empty scenes; the companion avatar is layered on by the course).
No text, no letters, no numbers, no logos, no signage words, no watermarks, no brand names.
```

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Nodes | `n1` supplier evaluation · `n2` queue-jumping request · `n3` not sure what is right |
| Pass rule | `pass_score` 3 (of a maximum 3) |
| Points | 15 |
| Feedback — correct | Three out of three. You declared the conflict, you held the line on queue-jumping, and you used the reporting route instead of guessing. That is Integrity and Accountability as behaviour, not as a poster. |
| Feedback — incorrect | Below three. The pattern to hold on to: disclose a conflict early, never trade access for a favour, and when you genuinely don't know, report it within twenty-four hours and ask the ethics team. |
| Retry / lives | Replay from the start (phase-3 §5); score counted once |

**Node table**

| Node | Situation (prompt) | Choice id | Choice text | Score Δ | Goes to | Feedback (why) |
|---|---|---|---|---|---|---|
| `n1` | You're on a panel evaluating three suppliers for a clinic fit-out. One bidder is your cousin's company. The evaluation starts in an hour. | `n1a` | Say nothing — you can score their bid fairly. | 0 | `n2` | Even a fair score looks compromised. Integrity means disclosing a potential conflict of interest before the work starts, in procurement as much as in recruitment. |
| `n1` | | `n1b` | Declare the conflict in writing to the panel chair and step back from scoring that bid. | +1 | `n2` | Right. You disclose the potential conflict and remove yourself from the decision. Nobody has to guess afterwards, including you. |
| `n1` | | `n1c` | Step out of the meeting quietly and say nothing. | 0 | `n2` | Leaving is better than scoring, but silence doesn't help: the panel still doesn't know why, and the conflict stays undocumented. Declare it, then step back. |
| `n2` | A colleague from another department asks you to “help” a patient skip the queue, and offers you a gift. | `n2a` | Decline, and explain that access to care is not something we trade. | +1 | `n3` | Right. Fair access is part of Respect — every patient in that queue is waiting for the same reason. A gift makes it a transaction. |
| `n2` | | `n2b` | Do it once, then return the gift. | 0 | `n3` | Returning the gift afterwards doesn't undo it. Someone else waited longer because of a favour, and the gift makes it a transaction. |
| `n2` | | `n2c` | Ask the patient to wait outside and slot them in when it's quiet. | 0 | `n3` | Quiet or not, that patient is still moving ahead of people who waited. Decline, and say why. |
| `n3` | A week later you're not sure whether something you saw counts as an ethical issue. Nobody else has raised it. | `n3a` | Wait until you're certain before involving anyone. | 0 | `null` | Waiting is the common mistake. The policy doesn't ask you to be certain; it asks you to act on the dilemma you have. |
| `n3` | | `n3b` | Raise it with a colleague or the committee, and complete an incident report within 24 hours so the ethics team can advise. | +1 | `null` | Right. Consult colleagues for anything beyond your expertise, and complete an incident report within twenty-four hours so the ethics team can guide you. That's Accountability working. |
| `n3` | | `n3c` | Mention it informally to your line manager and leave it there. | 0 | `null` | A quiet word is a start, but it leaves no record and no route to advice. Report it within twenty-four hours and bring the ethics team in. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR (co-host — Phase 3 names Noor as host of this scenario) |
| Tone | Serious, calm |
| Target seconds | 15 |
| Word count / est. seconds | 35 words / ≈ 15.0 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> NOOR: Three moments now, and nobody is watching. First: you're on a panel evaluating suppliers for a clinic fit-out, and one bidder is your cousin's company. The evaluation starts in an hour. What do you do?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Choices are native buttons in DOM order; outcome text is announced via a live region |
| Not colour-only | Outcome lines carry a glyph and the reason text; running score is printed as “2 of 3” |
| Captions / transcript | `narration_text` present; all node text and feedback are real HTML |
| Timing | Untimed; no timer on any node |

#### 7. Build fields (edumints)

```json
{
  "type": "decision_scenario",
  "id": "hr-031",
  "title": "A supplier you know",
  "section": "D · Ethics & patients' rights",
  "node_id": "hr-sD",
  "notes": "Companion: Noor, L5 avatar 56 px with 3 px #652D8C ring and label 'Noor · Safety liaison' above each situation card: char-noor-avatar-neutral; after a choice the feedback line shows char-noor-avatar-happy (best choice) or char-noor-avatar-concern (other choices). Never beside the choice buttons.",
  "objective_ids": [
    "hr-o2"
  ],
  "points": 15,
  "evidence_screen_ids": [
    "hr-030"
  ],
  "pass_score": 3,
  "start_node_id": "n1",
  "intro_html": "<p>Three moments, three decisions. Nobody is watching.</p>",
  "nodes": [
    {
      "id": "n1",
      "prompt_html": "<p>You're on a panel evaluating three suppliers for a clinic fit-out. One bidder is your cousin's company. The evaluation starts in an hour.</p>",
      "image_asset_id": "<hr-img-ethics-meeting>",
      "image_alt": "A small meeting room where a supplier evaluation is being discussed.",
      "choices": [
        {
          "id": "n1a",
          "text_html": "Say nothing — you can score their bid fairly.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>Even a fair score looks compromised. Integrity means disclosing a potential conflict of interest before the work starts, in procurement as much as in recruitment.</p>"
        },
        {
          "id": "n1b",
          "text_html": "Declare the conflict in writing to the panel chair and step back from scoring that bid.",
          "score_delta": 1,
          "goto_node_id": "n2",
          "feedback_html": "<p>Right. You disclose the potential conflict and remove yourself from the decision. Nobody has to guess afterwards, including you.</p>"
        },
        {
          "id": "n1c",
          "text_html": "Step out of the meeting quietly and say nothing.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>Leaving is better than scoring, but silence doesn't help: the panel still doesn't know why, and the conflict stays undocumented. Declare it, then step back.</p>"
        }
      ]
    },
    {
      "id": "n2",
      "prompt_html": "<p>A colleague from another department asks you to “help” a patient skip the queue, and offers you a gift.</p>",
      "image_asset_id": "<hr-img-ethics-corridor>",
      "image_alt": "A clinic corridor with a reception desk and two patients waiting.",
      "choices": [
        {
          "id": "n2a",
          "text_html": "Decline, and explain that access to care is not something we trade.",
          "score_delta": 1,
          "goto_node_id": "n3",
          "feedback_html": "<p>Right. Fair access is part of Respect — every patient in that queue is waiting for the same reason. A gift makes it a transaction.</p>"
        },
        {
          "id": "n2b",
          "text_html": "Do it once, then return the gift.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Returning the gift afterwards doesn't undo it. Someone else waited longer because of a favour, and the gift makes it a transaction.</p>"
        },
        {
          "id": "n2c",
          "text_html": "Ask the patient to wait outside and slot them in when it's quiet.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Quiet or not, that patient is still moving ahead of people who waited. Decline, and say why.</p>"
        }
      ]
    },
    {
      "id": "n3",
      "prompt_html": "<p>A week later you're not sure whether something you saw counts as an ethical issue. Nobody else has raised it.</p>",
      "image_asset_id": "<hr-img-ethics-desk>",
      "image_alt": "A desk with a laptop open on an incident report form.",
      "choices": [
        {
          "id": "n3a",
          "text_html": "Wait until you're certain before involving anyone.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>Waiting is the common mistake. The policy doesn't ask you to be certain; it asks you to act on the dilemma you have.</p>"
        },
        {
          "id": "n3b",
          "text_html": "Raise it with a colleague or the committee, and complete an incident report within 24 hours so the ethics team can advise.",
          "score_delta": 1,
          "goto_node_id": null,
          "feedback_html": "<p>Right. Consult colleagues for anything beyond your expertise, and complete an incident report within twenty-four hours so the ethics team can guide you. That's Accountability working.</p>"
        },
        {
          "id": "n3c",
          "text_html": "Mention it informally to your line manager and leave it there.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>A quiet word is a start, but it leaves no record and no route to advice. Report it within twenty-four hours and bring the ethics team in.</p>"
        }
      ]
    }
  ],
  "feedback": {
    "correct_html": "<p>Three out of three. You declared the conflict, you held the line on queue-jumping, and you used the reporting route instead of guessing. That is Integrity and Accountability as behaviour, not as a poster.</p>",
    "incorrect_html": "<p>Below three. The pattern to hold on to: disclose a conflict early, never trade access for a favour, and when you genuinely don't know, report it within twenty-four hours and ask the ethics team.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-031>",
  "narration_text": "NOOR: Three moments now, and nobody is watching. First: you're on a panel evaluating suppliers for a clinic fit-out, and one bidder is your cousin's company. The evaluation starts in an hour. What do you do?"
}
```

#### 8. Notes for SME and developer

- Open questions: **B14 / D8** — the 24-hour window appears in `n3b` and in the closing feedback. It must match module 07.
- Developer notes: Noor's avatar and label are placed by the renderer as described in `notes`; the happy/concern avatar appears only in the feedback line after a choice, never while the learner decides. The last node's choices carry `goto_node_id: null`, which ends the scenario. `pass_score` 3 is reachable only by `n1b` → `n2a` → `n3b`. Replay resets the running score; the LMS keeps the first recorded attempt's points.

---

### `hr-032` — Rights or responsibilities?

**Status:** `Draft — ready for SME review` · **Section / node:** D · Ethics & patients' rights / `hr-sD` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: separate what patients can expect from us and their families from what we ask of them |
| Objective(s) | `hr-o2` |
| On-the-job action | A4 |
| Source | `HR.pptx` slides 24–25 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Rights or responsibilities? |
| Body / keywords | Nine statements from the notice in reception. Sort them into the right column. |
| Word count (excl. title) | 12 |
| Instruction | Place each statement under Patient right or Patient responsibility. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "D · Ethics & patients' rights · Check", 2 px navy `#003867` header rule |
| Visual concept | Two tall drop zones side by side with plain headings and one line icon each; nine draggable chips sit in a wrap row below; a placed chip shows a 1 px border and a small position number |
| edumints layout | n/a (`drag_drop`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | Two single-weight line icons on drop-zone headers (shield-heart for rights, checklist-tick for responsibilities), navy #003867, own SVG |
| Animation / reveal | Chips settle with a 120 ms spring when dropped |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only interaction).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Targets | `right` — Patient right · `resp` — Patient responsibility |
| Items | `it1` “Access to care regardless of race, gender or disability” → `right` · `it2` “Information and informed consent before treatment” → `right` · `it3` “Privacy and confidentiality” → `right` · `it4` “Pain management” → `right` · `it5` “Refuse treatment after understanding the risks” → `right` · `it6` “Ask for a patient advocacy representative” → `right` · `it7` “Give accurate health information” → `resp` · `it8` “Follow the treatment plan and attend appointments” → `resp` · `it9` “Respect other patients and staff” → `resp` |
| Correct answer(s) | Six under `right`, three under `resp`, as listed |
| Accepted variants | n/a (chip placement, not typed answers) |
| Points | 10 |
| Feedback — correct | Right. Six rights and three responsibilities. The full notice is posted in the reception area if you ever need to point someone to it. |
| Feedback — incorrect | Not quite. A right is what the patient can expect from us. A responsibility is what we ask of them so that we can look after them safely. Look again at the three that ask the patient to *do* something. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 19 words / ≈ 8.1 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Nine statements from reception. Sort each: is it what the patient can expect, or what we ask of them?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Pick-and-place: focus a chip, press Enter to pick up, arrow to a zone, Enter to drop, Escape to cancel |
| Not colour-only | Each zone is headed with text and a distinct icon; placement shows an index number |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "drag_drop",
  "id": "hr-032",
  "title": "Rights or responsibilities?",
  "section": "D · Ethics & patients' rights",
  "node_id": "hr-sD",
  "objective_ids": [
    "hr-o2"
  ],
  "points": 10,
  "evidence_screen_ids": [
    "hr-030"
  ],
  "prompt_html": "<p>Nine statements from the notice in reception. Sort them into the right column.</p>",
  "targets": [
    {
      "id": "right",
      "label_html": "Patient right"
    },
    {
      "id": "resp",
      "label_html": "Patient responsibility"
    }
  ],
  "items": [
    {
      "id": "it1",
      "text_html": "Access to care regardless of race, gender or disability",
      "correct_target_id": "right"
    },
    {
      "id": "it2",
      "text_html": "Information and informed consent before treatment",
      "correct_target_id": "right"
    },
    {
      "id": "it3",
      "text_html": "Privacy and confidentiality",
      "correct_target_id": "right"
    },
    {
      "id": "it4",
      "text_html": "Pain management",
      "correct_target_id": "right"
    },
    {
      "id": "it5",
      "text_html": "Refuse treatment after understanding the risks",
      "correct_target_id": "right"
    },
    {
      "id": "it6",
      "text_html": "Ask for a patient advocacy representative",
      "correct_target_id": "right"
    },
    {
      "id": "it7",
      "text_html": "Give accurate health information",
      "correct_target_id": "resp"
    },
    {
      "id": "it8",
      "text_html": "Follow the treatment plan and attend appointments",
      "correct_target_id": "resp"
    },
    {
      "id": "it9",
      "text_html": "Respect other patients and staff",
      "correct_target_id": "resp"
    }
  ],
  "feedback": {
    "correct_html": "<p>Right. Six rights and three responsibilities. The full notice is posted in the reception area if you ever need to point someone to it.</p>",
    "incorrect_html": "<p>Not quite. A right is what the patient can expect from us. A responsibility is what we ask of them so that we can look after them safely. Look again at the three that ask the patient to <em>do</em> something.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-032>",
  "narration_text": "OMAR: Nine statements from reception. Sort each: is it what the patient can expect, or what we ask of them?"
}
```

#### 8. Notes for SME and developer

- Open questions: None. All nine statements are verbatim from slides 24–25.
- Developer notes: patient advocacy is worded “access to a patient advocacy representative or clinic administrator on request” on slide 24; the chip shortens it to fit the 12-word limit in the screen-type guide, and the full wording stays in the feedback.

---

### `hr-033` — She said no

**Status:** `Draft — ready for SME review` · **Section / node:** D · Ethics & patients' rights / `hr-sD` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: apply the right to refuse treatment in a realistic consultation moment |
| Objective(s) | `hr-o2` |
| On-the-job action | A4 |
| Source | `HR.pptx` slide 24 (“refusal of treatment after understanding risks”) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | She said no |
| Body / keywords | *(stem only — the stem is the prompt, not body copy)* |
| Word count (excl. title) | 0 |
| Instruction | Choose one. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "D · Ethics & patients' rights · Check", 2 px navy `#003867` header rule |
| Visual concept | Stem in large type; four plain option rows; no imagery, so the decision carries the screen |
| edumints layout | n/a (`mcq`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only question).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “A patient refuses a blood test after the doctor has explained the risks. What is the right response?” |
| Options | `a` Respect the refusal, check she understood the risks, document it, and tell the doctor ✔ · `b` Ask the clinic manager to persuade her to agree · `c` Take the sample anyway, because the doctor ordered it · `d` Ask a family member to consent instead |
| Correct answer(s) | `a` |
| Points | 5 |
| Feedback — correct | Right. Refusal of treatment is a patient right once the risks are understood. Your job is to check understanding, document the refusal, and inform the doctor. |
| Feedback — incorrect | Not that one. A competent patient can refuse after the risks have been explained. Persuasion, proceeding anyway, or substituting a family member's consent all override a right. |
| Per-option feedback | `a` — Right. Check understanding, document the refusal, inform the doctor. · `b` — Bringing in a manager to talk her round turns a right into pressure. She can refuse once she understands the risks. · `c` — Proceeding against a competent patient's refusal is not consent. Stop and escalate to the doctor instead. · `d` — A family member cannot replace her consent. Only she can decide, once she understands the risks. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm |
| Target seconds | 8 |
| Word count / est. seconds | 20 words / ≈ 8.6 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Last one here. A patient refuses a blood test after the doctor has explained the risks. What do you do?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native radio group |
| Not colour-only | Result uses a glyph plus words; every option carries its own reason text |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "hr-033",
  "title": "She said no",
  "section": "D · Ethics & patients' rights",
  "node_id": "hr-sD",
  "objective_ids": [
    "hr-o2"
  ],
  "points": 5,
  "evidence_screen_ids": [
    "hr-030"
  ],
  "prompt_html": "<p>A patient refuses a blood test after the doctor has explained the risks. What is the right response?</p>",
  "options": [
    {
      "id": "a",
      "text_html": "Respect the refusal, check she understood the risks, document it, and tell the doctor",
      "correct": true,
      "feedback_html": "<p>Right. Refusal of treatment is a patient right once the risks are understood. Your job is to check understanding, document the refusal, and inform the doctor.</p>"
    },
    {
      "id": "b",
      "text_html": "Ask the clinic manager to persuade her to agree",
      "feedback_html": "<p>Bringing in a manager to talk her round turns a right into pressure. She can refuse once she understands the risks.</p>"
    },
    {
      "id": "c",
      "text_html": "Take the sample anyway, because the doctor ordered it",
      "feedback_html": "<p>Proceeding against a competent patient's refusal is not consent. Stop and escalate to the doctor instead.</p>"
    },
    {
      "id": "d",
      "text_html": "Ask a family member to consent instead",
      "feedback_html": "<p>A family member cannot replace her consent. Only she can decide, once she understands the risks.</p>"
    }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Right. Refusal of treatment is a patient right once the risks are understood. Your job is to check understanding, document the refusal, and inform the doctor.</p>",
    "incorrect_html": "<p>Not that one. A competent patient can refuse after the risks have been explained. Persuasion, proceeding anyway, or substituting a family member's consent all override a right.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-033>",
  "narration_text": "OMAR: Last one here. A patient refuses a blood test after the doctor has explained the risks. What do you do?"
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: none.

---

### `hr-040` — Where help lives

**Status:** `Draft — ready for SME review` · **Section / node:** E · Your leave / `hr-sE` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the three places help comes from, so the learner stops guessing |
| Objective(s) | — (teaches `hr-o5`; assessed on `hr-060`) |
| On-the-job action | A7 |
| Source | `HR.pptx` slides 30–31 (HR help desk per business unit; Oracle; the HR topics overview) |
| Depends on Phase 0 | **B6 / D5** (role mailboxes instead of named contacts) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Where help lives |
| Body / keywords | Your HR help desk — one per business unit · Request everything in Oracle · Full rules: **HR Quick Reference** PDF |
| Word count (excl. title) | 15 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "E · Your leave", 2 px navy `#003867` header rule |
| Visual concept | Three cards in a row, each with a line icon and a short label; the third card carries a download affordance and a small PDF glyph; beneath them a single line states the rule “if it's a request, it goes through Oracle” |
| edumints layout | `text` |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Three single-weight line icons (`hr-img-help-icons`: headset, screen-and-form, document-arrow), Caring purple #652D8C, own SVG |
| Animation / reveal | Cards fade up left to right |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-help-icons` | SVG ×3 | Line icons: headset (help desk), screen-and-form (Oracle), document-arrow (PDF) | own | Decorative — each card is labelled in text. | Yes |
| `hr-pdf-quickref` | PDF | 2 pages: leave tables, pay and GOSI, overtime, contacts. Written by HR from confirmed policy. | own | n/a (linked resource, not an image) | n/a |

#### 4. Interaction and scoring

n/a — unscored content screen. The PDF is a linked resource, not a scored interaction.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Practical, warm |
| Target seconds | 25 |
| Word count / est. seconds | 63 words / ≈ 27.8 s (speaker labels excluded, pauses included) |
| Cue targets | `desk`, `oracle`, `pdf` |

> OMAR: [[cue:desk]] Where help lives. First, your HR help desk — one per business unit, so you'll talk to people who know your clinic. [[pause:0.4]] [[cue:oracle]] Second, Oracle. If it's a request, it goes through Oracle. That's the only way it has a record. [[pause:0.4]] [[cue:pdf]] Third, the HR Quick Reference: two pages with every leave table and the pay rules. Download it now. You don't need to memorise this.

New lexicon terms: Oracle — “OR-uh-kul”; HRMS — “H-R-M-S” (only if the PDF title uses it)

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | The PDF link is a native `<a>`; the cards are static |
| Not colour-only | All three cards are labelled in text |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-040",
  "title": "Where help lives",
  "section": "E · Your leave",
  "node_id": "hr-sE",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Your HR help desk</strong> — one per business unit. <em>Role mailbox addresses pending B6 / D5.</em></p><p><strong>Request everything in Oracle.</strong> If it's a request, it needs a record.</p><p><strong>Full rules:</strong> <a href=\"{{asset:hr-pdf-quickref}}\">HR Quick Reference (PDF, 2 pages)</a></p>",
  "narration_asset_id": "<hr-aud-040>",
  "narration_text": "OMAR: Where help lives. First, your HR help desk — one per business unit, so you'll talk to people who know your clinic. Second, Oracle. If it's a request, it goes through Oracle. That's the only way it has a record. Third, the HR Quick Reference: two pages with every leave table and the pay rules. Download it now. You don't need to memorise this.",
  "media_asset_id": "<hr-img-help-icons>",
  "media_alt": "Three icons: HR help desk, Oracle self-service, and the HR Quick Reference PDF."
}
```

#### 8. Notes for SME and developer

- Open questions: **B6 / D5** — the deck names individual HR staff and personal mailboxes (slide 30). The card ships with role mailboxes only. Swap the placeholder text once HR and the DPO close B6.
- Developer notes: the `{{asset:hr-pdf-quickref}}` token is replaced with the real asset URL after `add_asset`. The build-pipeline notes that resource-link handling is limited — test the link in preview **and** in the LMS. Fallback: host the PDF on the intranet and link the URL.

---

### `hr-041` — Leave at a glance

**Status:** `Draft — ready for SME review` · **Section / node:** E · Your leave / `hr-sE` · **Type:** `accordion` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the nine leave types and the one rule worth remembering per type |
| Objective(s) | — (teaches `hr-o3`; assessed on `hr-042`, `hr-044`, `hr-045`) |
| On-the-job action | A5 |
| Source | `HR.pptx` slides 32–43 |
| Depends on Phase 0 | **B1** (sick-leave pay bands) · **B2** (compassionate-leave wording) · **B11** (Hajj leave) · **B9** (carry-over) · **B10** (scientific-leave wording) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Leave at a glance |
| Body / keywords | Nine types. Open the one you need — the full tables are in the Quick Reference. |
| Word count (excl. title) | 14 |
| Instruction | Open each leave type. |

| Panel | Key rule shown (≤ 40 words) | Pending |
|---|---|---|
| Annual | After probation, with your line manager's approval. Carry over up to 5 days; use them by end of March (consulting-room physicians: end of June). | B9 |
| Sick | Tell your line manager. Valid medical report required. First 30 days full pay; days 31–90 ⚠ PENDING B1; days 91–120 unpaid. | B1 |
| Work injury | Covers work hours and commuting. Report to your line manager **and** HR the same day or the next day. | — |
| Maternity | 12 weeks. You may start up to 4 weeks before the expected delivery date. | — |
| Exam | Paid, for **academic** exams only. Actual exam days only. Documents at least 2 weeks in advance. IELTS, TOEFL and similar are not eligible. | — |
| Scientific | Paid days per profession each year, for academic exams. Needs the MD's pre-approval. **Cannot be carried over.** | B10 |
| Hajj | Muslim employees with two full years of service. 10–15 days including Eid. Hajj permit copy required. ⚠ PENDING B11 | B11 |
| Compassionate | Marriage 5 days · paternity 3 · immediate relative 5 · sibling 3 · death of a husband ⚠ PENDING B2 | B2 |
| Official holidays | Eid al-Fitr 4 days · Eid al-Adha 4 days · Founding Day 22 February · National Day 23 September. | — |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "E · Your leave", 2 px navy `#003867` header rule |
| Visual concept | Nine collapsed rows, each with a two-letter code chip on the left (AN, SK, WI, MA, EX, SC, HJ, CO, OH), the leave name, and a chevron; expanding shows one sentence of plain text plus a single “watch out” line where a rule trips people up |
| edumints layout | n/a (`accordion`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (two-letter code chips in Caring purple #652D8C) |
| Animation / reveal | 200 ms height transition on expand |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (the code chips are CSS, not assets).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | 9 panels: `annual`, `sick`, `injury`, `maternity`, `exam`, `scientific`, `hajj`, `compassionate`, `holidays` |
| Correct answer(s) | n/a |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Practical |
| Target seconds | 40 |
| Word count / est. seconds | 91 words / ≈ 42.0 s (speaker labels excluded, pauses included) |
| Cue targets | `intro`, `annual`, `sick`, `injury`, `maternity`, `exam`, `scientific`, `hajj`, `compass`, `holidays` |

> OMAR: [[cue:intro]] Nine types. Open the ones you need. [[pause:0.3]] [[cue:annual]] Annual: after probation, five days carried over, used by end of March. [[pause:0.3]] [[cue:sick]] Sick: valid report needed. First thirty days paid in full. [[pause:0.3]] [[cue:injury]] Work injury covers commuting, and has a same-day or next-day deadline. [[pause:0.3]] [[cue:maternity]] Maternity: twelve weeks, starting up to four weeks early. [[pause:0.3]] [[cue:exam]] Exam leave: academic exams only, documents two weeks ahead. [[pause:0.3]] [[cue:scientific]] Scientific: by profession, and can't be carried over. [[pause:0.3]] [[cue:hajj]] Hajj: two years' service and a permit. [[pause:0.3]] [[cue:compass]] Compassionate: marriage, paternity, bereavement. [[pause:0.3]] [[cue:holidays]] Then Eid, Founding Day, National Day. [[pause:0.3]] We'll practise the four people ask about most.

New lexicon terms: Hajj — “hajj”; Eid — “eed”; IELTS — “eye-elts”; TOEFL — “toe-full”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native `<button>` headers with `aria-expanded` |
| Not colour-only | Code chips are text; open state uses chevron plus `aria-expanded` |
| Captions / transcript | `narration_text` present; every panel is real HTML text |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "accordion",
  "id": "hr-041",
  "title": "Leave at a glance",
  "section": "E · Your leave",
  "node_id": "hr-sE",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>Nine types. Open the one you need — the full tables are in the Quick Reference.</p>",
  "items": [
    {
      "title": "Annual",
      "body_html": "<p>After probation, with your line manager's approval. Carry over up to 5 days; use them by end of March (consulting-room physicians: end of June). <em>Pending B9.</em></p>"
    },
    {
      "title": "Sick",
      "body_html": "<p>Tell your line manager. Valid medical report required. First 30 days full pay; days 31–90 <em>pending B1</em>; days 91–120 unpaid.</p>"
    },
    {
      "title": "Work injury",
      "body_html": "<p>Covers work hours and commuting. <strong>Report to your line manager and HR the same day or the next day.</strong></p>"
    },
    {
      "title": "Maternity",
      "body_html": "<p>12 weeks. You may start up to 4 weeks before the expected delivery date.</p>"
    },
    {
      "title": "Exam",
      "body_html": "<p>Paid, for <strong>academic</strong> exams only. Actual exam days only. Documents at least 2 weeks in advance. IELTS, TOEFL and similar are not eligible.</p>"
    },
    {
      "title": "Scientific",
      "body_html": "<p>Paid days per profession each year, for academic exams. Needs the MD's pre-approval. <strong>Cannot be carried over.</strong> <em>Pending B10.</em></p>"
    },
    {
      "title": "Hajj",
      "body_html": "<p>Muslim employees with two full years of service. 10–15 days including Eid. Hajj permit copy required. <em>Pending B11.</em></p>"
    },
    {
      "title": "Compassionate",
      "body_html": "<p>Marriage 5 days · paternity 3 · immediate relative 5 · sibling 3 · death of a husband <em>pending B2</em>.</p>"
    },
    {
      "title": "Official holidays",
      "body_html": "<p>Eid al-Fitr 4 days · Eid al-Adha 4 days · Founding Day 22 February · National Day 23 September.</p>"
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-041>",
  "narration_text": "OMAR: Nine types. Open the ones you need. Annual: after probation, five days carried over, used by end of March. Sick: valid report needed. First thirty days paid in full. Work injury covers commuting, and has a same-day or next-day deadline. Maternity: twelve weeks, starting up to four weeks early. Exam leave: academic exams only, documents two weeks ahead. Scientific: by profession, and can't be carried over. Hajj: two years' service and a permit. Compassionate: marriage, paternity, bereavement. Then Eid, Founding Day, National Day. We'll practise the four people ask about most."
}
```

#### 8. Notes for SME and developer

- Open questions: **B1** (sick-leave pay bands 31–90), **B2** (compassionate-leave wording for the death of a husband), **B9** (current-year carry-over), **B10** (scientific-leave wording on slide 40, which looks copied from the exam-leave slide), **B11** (Hajj leave service requirement).
- Developer notes: nine panels is the top of the 3–9 range in the screen-type guide. Do not add a tenth without splitting the screen.

---

### `hr-042` — How many days?

**Status:** `Draft — ready for SME review` · **Section / node:** E · Your leave / `hr-sE` · **Type:** `matching` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: find the annual-leave entitlement for a grade without memorising the table |
| Objective(s) | `hr-o3` |
| On-the-job action | A5 |
| Source | `HR.pptx` slide 34 (annual entitlement by grade, working days) |
| Depends on Phase 0 | **B9** (entitlement for the current year) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | How many days? |
| Body / keywords | Four grades, four entitlements. Match each grade to its annual leave, in working days. |
| Word count (excl. title) | 13 |
| Instruction | Match each grade to its entitlement. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "E · Your leave · Check", 2 px navy `#003867` header rule |
| Visual concept | Two columns: four grade tiles on the left (H, G, F and Consultant, A to E) and four number tiles on the right (30, 27, 25, 22); a connector line follows the selection |
| edumints layout | n/a (`matching`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only interaction).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Pairs (left → right) | `p1` Grade H → 30 working days · `p2` Grade G → 27 working days · `p3` Grade F and Consultant → 25 working days · `p4` Grades A to E → 22 working days |
| Correct answer(s) | As listed |
| Points | 5 |
| Feedback — correct | Right. Entitlement rises with grade: 30, 27, 25 and 22 working days. Your contract and the Quick Reference both show your own grade. |
| Feedback — incorrect | Not quite. The entitlement rises with grade, from 22 working days at grades A to E up to 30 at grade H. Match them again. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 14 words / ≈ 6.0 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Four grades, four entitlements. Match each grade to its annual leave, in working days.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Selectable list on the left, activatable tiles on the right |
| Not colour-only | Result uses a glyph plus the words Correct / Not this one |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "matching",
  "id": "hr-042",
  "title": "How many days?",
  "section": "E · Your leave",
  "node_id": "hr-sE",
  "objective_ids": [
    "hr-o3"
  ],
  "points": 5,
  "evidence_screen_ids": [
    "hr-041"
  ],
  "prompt_html": "<p>Four grades, four entitlements. Match each grade to its annual leave, in working days. <em>Entitlement pending B9.</em></p>",
  "pairs": [
    {
      "id": "p1",
      "left_html": "Grade H",
      "right_html": "30 working days"
    },
    {
      "id": "p2",
      "left_html": "Grade G",
      "right_html": "27 working days"
    },
    {
      "id": "p3",
      "left_html": "Grade F and Consultant",
      "right_html": "25 working days"
    },
    {
      "id": "p4",
      "left_html": "Grades A to E",
      "right_html": "22 working days"
    }
  ],
  "feedback": {
    "correct_html": "<p>Right. Entitlement rises with grade: 30, 27, 25 and 22 working days. Your contract and the Quick Reference both show your own grade.</p>",
    "incorrect_html": "<p>Not quite. The entitlement rises with grade, from 22 working days at grades A to E up to 30 at grade H. Match them again.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-042>",
  "narration_text": "OMAR: Four grades, four entitlements. Match each grade to its annual leave, in working days."
}
```

#### 8. Notes for SME and developer

- Open questions: **B9** — confirm the entitlement table for the current year. If it changes, four strings change and nothing else.
- Developer notes: none.

---

### `hr-043` — Forty days of sick leave

**Status:** `Draft — ready for SME review` · **Section / node:** E · Your leave / `hr-sE` · **Type:** `worked_example` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: walk the sick-leave pay bands end to end, then ask the learner to predict the one variation that matters |
| Objective(s) | — (teaches `hr-o3`) |
| On-the-job action | A5 |
| Source | `HR.pptx` slide 35 |
| Depends on Phase 0 | **B1** (the pay percentage for days 31–90) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Forty days of sick leave |
| Body / keywords | *(problem statement in `intro_html`; steps carry their own text)* |
| Word count (excl. title) | 0 (intro is the problem, not body copy) |
| Instruction | Reveal why each step is taken, one step at a time. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "E · Your leave", 2 px navy `#003867` header rule |
| Visual concept | A five-row vertical ledger on a white card in the left ~62% of the stage: each row has a day band on the left, the action in the middle and a “Why?” control on the right; revealing a row slides its rationale panel open beneath the action; Dr. Omar's half-body `thinking` pose (hand at chin) stands in the right column, as if working the example through with the learner |
| edumints layout | n/a (`worked_example`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | `fading: "partial"` — actions are visible, rationales sit behind a per-step reveal control |
| Companion | Dr. Omar · `char-omar-thinking` · placement L3 right column, half-body, 320–380 px, bottom-aligned, clear of the ledger and its “Why?” controls · tip text n/a · speaks: Omar (talks through the example) |

**Imagery** (the ledger is CSS; no artefact screenshots are needed)

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `char-omar-thinking` | illustration | Shared programme companion pose (Canva media `MAHX-jgu1Vk`): half-body, hand at chin; right column, 320–380 px | ai-generated (programme master, companions.md §3) | “Dr. Omar, a family physician, thinking through the example.” | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Problem (`intro_html`) | “A colleague is off sick for 40 days in one year, with valid medical reports from My Clinic. How is the pay worked out?” |
| Steps | See the table below. |
| Correct answer(s) | n/a — unscored worked example |
| Points | 0 |
| Self-explanation prompt | “What changes if the medical report comes from another hospital?” |
| Retry / lives | n/a |

| # | Action | Rationale (revealed) |
|---|---|---|
| 1 | Tell your line manager you are unwell. | Notification is the first requirement. Sick leave is accepted only with a valid medical report, and your manager needs to know today, not at the end of it. |
| 2 | Days 1–30: full salary. | The first thirty days of valid sick leave in a year are paid in full. |
| 3 | Days 31–40: ⚠ PENDING B1 — 25% deducted, so 75% of salary, per the slide as written. | The second band cuts pay by a quarter. Continuous and separated periods count the same way, so the band follows the total days in the year, not one absence. |
| 4 | Days 91–120 would be unpaid. | The bands run 1–30, 31–90 and 91–120. Forty days never reaches this band, but it's the ceiling you should know. |
| 5 | If the report is from outside My Clinic, it needs Staff Health Clinic approval. | Reports from My Clinic are accepted as they are. Anything from another provider has to be approved, or the leave isn't valid. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm, precise |
| Target seconds | 40 |
| Word count / est. seconds | 95 words / ≈ 43.2 s (speaker labels excluded, pauses included) |
| Cue targets | `s1`, `s2`, `s3`, `s4`, `s5` |

> OMAR: One example, properly. A colleague is off sick forty days in a year, with valid reports. [[cue:s1]] First, she tells her line manager — that's first, not last. [[pause:0.4]] [[cue:s2]] The first thirty days are paid in full. [[pause:0.4]] [[cue:s3]] Ten days fall into the next band, and that's where pay drops. [[pause:0.4]] Note the detail people miss: it's the total in the year that sets the band, not one spell. [[pause:0.5]] [[cue:s4]] Beyond ninety days it's unpaid. [[pause:0.4]] [[cue:s5]] And if the report is from outside My Clinic, the Staff Health Clinic must approve it. [[pause:0.4]] Now: what changes if her report comes from another hospital?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each “Why?” control is a native `<button>` with `aria-expanded` |
| Not colour-only | Bands are labelled “Days 1–30”, “Days 31–40” in text, not by colour |
| Captions / transcript | `narration_text` present; all step text is real HTML |
| Timing | Untimed; the self-explanation field never blocks Continue |

#### 7. Build fields (edumints)

```json
{
  "type": "worked_example",
  "id": "hr-043",
  "title": "Forty days of sick leave",
  "section": "E · Your leave",
  "node_id": "hr-sE",
  "objective_ids": [],
  "points": 0,
  "notes": "Companion: Dr. Omar char-omar-thinking, L3 right column half-body 320-380 px, clear of the ledger; below 768 px he drops under the ledger. Alt: 'Dr. Omar, a family physician, thinking through the example.'",
  "fading": "partial",
  "intro_html": "<p>A colleague is off sick for 40 days in one year, with valid medical reports from My Clinic. How is the pay worked out?</p>",
  "steps": [
    {
      "action_html": "<p><strong>Days 1–30</strong> — tell your line manager you are unwell.</p>",
      "rationale_html": "<p>Notification is the first requirement. Sick leave is accepted only with a valid medical report, and your manager needs to know today, not at the end of it.</p>"
    },
    {
      "action_html": "<p><strong>Days 1–30</strong> — full salary.</p>",
      "rationale_html": "<p>The first thirty days of valid sick leave in a year are paid in full.</p>"
    },
    {
      "action_html": "<p><strong>Days 31–40</strong> — reduced pay. <em>Per the slide as written: 25% deducted, so 75% of salary. Pending B1.</em></p>",
      "rationale_html": "<p>The second band cuts pay by a quarter. Continuous and separated periods count the same way, so the band follows the total days in the year, not one absence.</p>"
    },
    {
      "action_html": "<p><strong>Days 91–120</strong> — unpaid.</p>",
      "rationale_html": "<p>The bands run 1–30, 31–90 and 91–120. Forty days never reaches this band, but it's the ceiling you should know.</p>"
    },
    {
      "action_html": "<p>Check the report: from outside My Clinic, it needs <strong>Staff Health Clinic approval</strong>.</p>",
      "rationale_html": "<p>Reports from My Clinic are accepted as they are. Anything from another provider has to be approved, or the leave isn't valid.</p>"
    }
  ],
  "self_explanation_prompt_html": "<p>What changes if the medical report comes from another hospital?</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-043>",
  "narration_text": "OMAR: One example, properly. A colleague is off sick forty days in a year, with valid reports. First, she tells her line manager — that's first, not last. The first thirty days are paid in full. Ten days fall into the next band, and that's where pay drops. Note the detail people miss: it's the total in the year that sets the band, not one spell. Beyond ninety days it's unpaid. And if the report is from outside My Clinic, the Staff Health Clinic must approve it. Now: what changes if her report comes from another hospital?"
}
```

#### 8. Notes for SME and developer

- Open questions: **B1** — the slide says “days 31–90: 25% deducted”. HR must confirm whether that means 75% of salary for days 31–90. The step text says exactly what the slide says and marks it pending; the narration deliberately does not state a percentage.
- Developer notes: `worked_example` is unscored (`points: 0`). Do not score this screen. Place Omar from the theme/renderer as described in `notes`; below 768 px width he drops under the ledger.

---

### `hr-044` — The leave desk

**Status:** `Draft — ready for SME review` · **Section / node:** E · Your leave / `hr-sE` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: eligibility decisions for the four leave types people ask about most |
| Objective(s) | `hr-o3` |
| On-the-job action | A5 |
| Source | `HR.pptx` slides 36–41 (work injury 36, maternity 37, exam 38, scientific 39–40, Hajj 41) |
| Depends on Phase 0 | **B10** (scientific-leave wording) · **B11** (Hajj leave service requirement) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The leave desk |
| Body / keywords | Four colleagues, four questions. You're the one they've asked. |
| Word count (excl. title) | 8 |
| Instruction | Answer each colleague. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario (see `../../00_program/brand/screen-mockups/05-scenario.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "E · Your leave", 2 px navy `#003867` header rule |
| Visual concept | A flat service-desk illustration band at the top that stays constant; below it a single request card with the colleague's first name, role and question, then full-width choice buttons; a “3 of 4 answered” counter sits in the corner |
| edumints layout | n/a (`decision_scenario`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` stage and choice cards with `#D9E1E8` border) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` progress bar) · companion avatar ring in the character's colour (companions.md §4) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; situation Montserrat SemiBold 600, 17 px; choices Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (flat scene illustration + companion avatar) |
| Animation / reveal | Request card fades up on each node change |
| Companion | Noor · `char-noor-avatar-neutral` on every node (Phase 3 lists the neutral avatar only) · placement L5 avatar, 56 px circle with a 3 px Caring purple `#652D8C` ring, label “Noor · Safety liaison” beside it, above the request card; never on or beside the choice buttons · tip text n/a · speaks: Noor (leave-desk host) |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-leavedesk` | illustration | Flat office-desk scene: a desk, a laptop, a small plant, two chairs; brand colours, white background | ai-generated | “An HR service desk with a laptop and two chairs.” | No |
| `char-noor-avatar-neutral` | illustration | Shared programme avatar (Canva media `MAHX-n4HuyU`), cropped to a 56 px circle | ai-generated (programme master, companions.md §3) | “Noor, the safety liaison, hosting the leave desk.” | No |

**AI image prompt** (`hr-img-leavedesk` — per `brand-identity.md` §6; the companion is **not** generated here — Noor's avatar is the shared programme asset, see [`companions.md`](../../00_program/characters/companions.md) §3):

```text
Flat vector illustration for a healthcare e-learning course, 16:9, an HR service desk in a modern clinic office with a laptop, a small indoor plant and two visitor chairs. Clean minimalist style, simple geometric shapes, thin navy (#003867) outlines, white and very light blue-grey (#F4F7FA, #C0CED9) surfaces, one highlight colour Caring purple (#652D8C), small touches of magenta (#9D3293) only for nothing. Modern Saudi outpatient clinic interior, bright and calm, lots of white space, soft even lighting, no shadows or very soft flat shadows.
People: none (empty desk; the companion avatar is layered on by the course).
No text, no letters, no numbers, no logos, no signage words, no watermarks, no brand names.
```

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Nodes | `n1` Yousuf, lab technician · `n2` Amal, nurse · `n3` Reem, pharmacist · `n4` Sara, receptionist |
| Pass rule | `pass_score` 3 (of a maximum 4) |
| Points | 15 |
| Feedback — correct | Three or four. You checked eligibility before you answered, which is the whole job at this desk: type of leave, who qualifies, and what document is missing. |
| Feedback — incorrect | Fewer than three. The habit to build is to check three things every time — the type of leave, the eligibility rule, and the document. Two of these four turned on eligibility, not on paperwork. |
| Retry / lives | Replay from the start; score counted once |

**Node table**

| Node | Situation (prompt) | Choice id | Choice text | Score Δ | Goes to | Feedback (why) |
|---|---|---|---|---|---|---|
| `n1` | Yousuf is a lab technician. He asks for two days of scientific leave, and he already has the MD's pre-approval for his documents. How many days can he take this year? | `n1a` | Two days — that's the technician allowance, and unused days can't be carried over. | +1 | `n2` | Right. Scientific leave is 2 days a year for lab and radiology technicians, 3 for nurses, 4 for pharmacists, 5 for other physicians and dentists, and 7 for consultants. It also can't be carried over. |
| `n1` | | `n1b` | Seven days — that's the allowance. | 0 | `n2` | Seven days is the consultants' allowance. Technicians get two. The allowance follows the profession, not the request. |
| `n1` | | `n1c` | None — scientific leave is only for consultants and physicians. | 0 | `n2` | Not so. Every profession in the table has an allowance; technicians have the smallest, at two days a year. |
| `n1` | | `n1d` | Two days now, and he can carry the rest into next year. | 0 | `n2` | The days are right, the carry-over isn't. Scientific leave cannot be carried over — unused days are lost. |
| `n2` | Amal is a nurse. She asks for exam leave to sit IELTS next month, and she has her documents ready. | `n2a` | Refuse: IELTS is not an academic examination, and it's named as not eligible. | +1 | `n3` | Right. Exam leave is paid leave for academic examinations only, and IELTS, TOEFL and Microsoft certifications are named as not eligible. Having the documents ready doesn't change eligibility. |
| `n2` | | `n2b` | Approve it — she has her documents in on time. | 0 | `n3` | Documents matter, but eligibility comes first. IELTS is not an academic examination and is named as not eligible. |
| `n2` | | `n2c` | Approve half the exam days as a goodwill gesture. | 0 | `n3` | Well meant, but the rule is about the type of exam, not the number of days. IELTS is not eligible, so there are no days to approve. |
| `n3` | Reem is a pharmacist with one full year of service. She asks for Hajj leave and has her Hajj permit ready. | `n3a` | Not yet — Hajj leave needs two full years of continuous service. | +1 | `n4` | Right. Two full years of continuous service is the eligibility rule, and one year doesn't meet it. The permit is needed, but it doesn't shorten the service requirement. |
| `n3` | | `n3b` | Yes — one year of service is enough. | 0 | `n4` | It isn't. Hajj leave is for Muslim employees with two full years of continuous service. |
| `n3` | | `n3c` | Yes, now that she has the Hajj permit. | 0 | `n4` | The permit is a requirement, not a substitute. Without two full years of service she isn't eligible, permit or not. |
| `n4` | Sara is a receptionist. She slipped on the way into work this morning and her ankle is painful. What does she need to do? | `n4a` | Tell her line manager and HR today or tomorrow — commuting is covered as a work injury. | +1 | `null` | Right. Work injury covers commuting as well as work hours, and the deadline is the same day or the following day. HR then reports the case to GOSI. |
| `n4` | | `n4b` | Wait and see whether she needs time off before reporting it. | 0 | `null` | Waiting is the mistake this rule exists to prevent. The report has to go to her line manager and HR the same day or the next day, whether or not she ends up taking time off. |
| `n4` | | `n4c` | Tell her commuting accidents aren't covered. | 0 | `null` | They are. Work injury applies during work hours and while commuting to and from work, for Saudi and expatriate employees alike. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR (co-host — Phase 3 names Noor as host of this scenario) |
| Tone | Practical, warm |
| Target seconds | 15 |
| Word count / est. seconds | 27 words / ≈ 11.6 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> NOOR: Now you're on the other side of the desk. Four colleagues, four questions. First: Yousuf, a lab technician, wants scientific leave and already has the MD's pre-approval.

New lexicon terms: GOSI — “GO-see”; IELTS — “eye-elts”; TOEFL — “toe-full”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Choices are native buttons; outcome text announced via a live region |
| Not colour-only | Outcome uses a glyph plus reason text; the counter is printed as “3 of 4” |
| Captions / transcript | `narration_text` present; all node and choice text is real HTML |
| Timing | Untimed; no timer on any node |

#### 7. Build fields (edumints)

```json
{
  "type": "decision_scenario",
  "id": "hr-044",
  "title": "The leave desk",
  "section": "E · Your leave",
  "node_id": "hr-sE",
  "notes": "Companion: Noor char-noor-avatar-neutral, L5 avatar 56 px with 3 px #652D8C ring and label 'Noor · Safety liaison' above each request card; never beside the choice buttons. Alt: 'Noor, the safety liaison, hosting the leave desk.'",
  "objective_ids": [
    "hr-o3"
  ],
  "points": 15,
  "evidence_screen_ids": [
    "hr-041"
  ],
  "pass_score": 3,
  "start_node_id": "n1",
  "intro_html": "<p>Four colleagues, four questions. You're the one they've asked.</p>",
  "nodes": [
    {
      "id": "n1",
      "prompt_html": "<p><strong>Yousuf</strong> is a lab technician. He asks for two days of scientific leave, and he already has the MD's pre-approval for his documents. How many days can he take this year?</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        {
          "id": "n1a",
          "text_html": "Two days — that's the technician allowance, and unused days can't be carried over.",
          "score_delta": 1,
          "goto_node_id": "n2",
          "feedback_html": "<p>Right. Scientific leave is 2 days a year for lab and radiology technicians, 3 for nurses, 4 for pharmacists, 5 for other physicians and dentists, and 7 for consultants. It also can't be carried over.</p>"
        },
        {
          "id": "n1b",
          "text_html": "Seven days — that's the allowance.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>Seven days is the consultants' allowance. Technicians get two. The allowance follows the profession, not the request.</p>"
        },
        {
          "id": "n1c",
          "text_html": "None — scientific leave is only for consultants and physicians.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>Not so. Every profession in the table has an allowance; technicians have the smallest, at two days a year.</p>"
        },
        {
          "id": "n1d",
          "text_html": "Two days now, and he can carry the rest into next year.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>The days are right, the carry-over isn't. Scientific leave cannot be carried over — unused days are lost.</p>"
        }
      ]
    },
    {
      "id": "n2",
      "prompt_html": "<p><strong>Amal</strong> is a nurse. She asks for exam leave to sit IELTS next month, and she has her documents ready.</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        {
          "id": "n2a",
          "text_html": "Refuse: IELTS is not an academic examination, and it's named as not eligible.",
          "score_delta": 1,
          "goto_node_id": "n3",
          "feedback_html": "<p>Right. Exam leave is paid leave for academic examinations only, and IELTS, TOEFL and Microsoft certifications are named as not eligible. Having the documents ready doesn't change eligibility.</p>"
        },
        {
          "id": "n2b",
          "text_html": "Approve it — she has her documents in on time.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Documents matter, but eligibility comes first. IELTS is not an academic examination and is named as not eligible.</p>"
        },
        {
          "id": "n2c",
          "text_html": "Approve half the exam days as a goodwill gesture.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Well meant, but the rule is about the type of exam, not the number of days. IELTS is not eligible, so there are no days to approve.</p>"
        }
      ]
    },
    {
      "id": "n3",
      "prompt_html": "<p><strong>Reem</strong> is a pharmacist with one full year of service. She asks for Hajj leave and has her Hajj permit ready.</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        {
          "id": "n3a",
          "text_html": "Not yet — Hajj leave needs two full years of continuous service.",
          "score_delta": 1,
          "goto_node_id": "n4",
          "feedback_html": "<p>Right. Two full years of continuous service is the eligibility rule, and one year doesn't meet it. The permit is needed, but it doesn't shorten the service requirement.</p>"
        },
        {
          "id": "n3b",
          "text_html": "Yes — one year of service is enough.",
          "score_delta": 0,
          "goto_node_id": "n4",
          "feedback_html": "<p>It isn't. Hajj leave is for Muslim employees with two full years of continuous service.</p>"
        },
        {
          "id": "n3c",
          "text_html": "Yes, now that she has the Hajj permit.",
          "score_delta": 0,
          "goto_node_id": "n4",
          "feedback_html": "<p>The permit is a requirement, not a substitute. Without two full years of service she isn't eligible, permit or not.</p>"
        }
      ]
    },
    {
      "id": "n4",
      "prompt_html": "<p><strong>Sara</strong> is a receptionist. She slipped on the way into work this morning and her ankle is painful. What does she need to do?</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        {
          "id": "n4a",
          "text_html": "Tell her line manager and HR today or tomorrow — commuting is covered as a work injury.",
          "score_delta": 1,
          "goto_node_id": null,
          "feedback_html": "<p>Right. Work injury covers commuting as well as work hours, and the deadline is the same day or the following day. HR then reports the case to GOSI.</p>"
        },
        {
          "id": "n4b",
          "text_html": "Wait and see whether she needs time off before reporting it.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>Waiting is the mistake this rule exists to prevent. The report has to go to her line manager and HR the same day or the next day, whether or not she ends up taking time off.</p>"
        },
        {
          "id": "n4c",
          "text_html": "Tell her commuting accidents aren't covered.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>They are. Work injury applies during work hours and while commuting to and from work, for Saudi and expatriate employees alike.</p>"
        }
      ]
    }
  ],
  "feedback": {
    "correct_html": "<p>Three or four. You checked eligibility before you answered, which is the whole job at this desk: type of leave, who qualifies, and what document is missing.</p>",
    "incorrect_html": "<p>Fewer than three. The habit to build is to check three things every time — the type of leave, the eligibility rule, and the document. Two of these four turned on eligibility, not on paperwork.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-044>",
  "narration_text": "NOOR: Now you're on the other side of the desk. Four colleagues, four questions. First: Yousuf, a lab technician, wants scientific leave and already has the MD's pre-approval."
}
```

#### 8. Notes for SME and developer

- Open questions: **B10** — slide 40's sentence about academic exams looks copied from the exam-leave slide. If HR confirms a different purpose for scientific leave, re-word `n1` and its feedback. **B11** — confirm the two-year service rule and the 10–15 day range for Hajj leave.
- Developer notes: Noor's avatar and label are placed by the renderer as described in `notes` (no avatar field in the schema). `pass_score` 3 with four nodes means one wrong answer is tolerated. `n1` deliberately has four choices; the others have three. All four `n1` choices go to `n2`, so no path is short.

---

### `hr-045` — Leave rules: quick practice

**Status:** `Draft — ready for SME review` · **Section / node:** E · Your leave / `hr-sE` · **Type:** `adaptive_practice` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: a short adaptive set on the leave numbers, so experienced hires finish early and new joiners get more |
| Objective(s) | `hr-o3` |
| On-the-job action | A5 |
| Source | `HR.pptx` slides 33–43 |
| Depends on Phase 0 | **B9** (carry-over for the current year) · **B2** (compassionate-leave days) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Leave rules: quick practice |
| Body / keywords | Answer until the practice says you're ready. It stops early if you've got it. |
| Word count (excl. title) | 12 |
| Instruction | Choose one answer each time. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "E · Your leave · Check", 2 px navy `#003867` header rule |
| Visual concept | One question at a time, centred, with three option rows; a thin progress strip at the top fills as items are answered and a small “est. 3 more” hint appears once the estimator has enough data |
| edumints layout | n/a (`adaptive_practice`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | Question cross-fades between items |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only practice).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Bank | 12 items, `q1`–`q12` (see the table below) |
| Settings | `max_items` 6 · `target_success` 0.7 · `pass_ratio` 0.6 · `adaptive.strategy` `elo` · `loop_mode` `sample` |
| Points | 15 |
| Feedback | Per item: `explain_html` shows why after answering; `scaffold_html` is the hint on a wrong answer |
| Retry / lives | No retry within a run; the run ends at `max_items` or when the estimator is satisfied |

| # | Item | Correct | Distractors | Diff. | Explain (why) | Scaffold (hint, not the answer) |
|---|---|---|---|---|---|---|
| `q1` | How many unused annual leave days can you carry over? | Up to 5 | Up to 10 · All of them | 0.25 | Carry-over is capped at 5 days. Anything above that is lost at the end of the carry-over window. | The cap is a small number — single digits. |
| `q2` | Carried-over annual leave must be used by when? | End of March | End of June · End of the year | 0.35 | Carried-over leave has to be used by the end of March of the following year. | It's the end of a spring month. |
| `q3` | A consulting-room physician carries over leave. By when must it be used? | End of June | End of March · End of the year | 0.65 | Consulting-room physicians have a later deadline: the end of June. | This group gets three months more than everyone else. |
| `q4` | How long is maternity leave? | 12 weeks | 10 weeks · 8 weeks | 0.3 | Maternity leave is 12 weeks. | It's measured in weeks, not months — and it's the longest of the three options. |
| `q5` | How early can maternity leave start? | Up to 4 weeks before the due date | Up to 2 weeks before · On the due date only | 0.6 | You may start up to 4 weeks before the expected delivery date. | The allowance is measured in weeks before the due date. |
| `q6` | Exam leave documents must be submitted how far in advance? | At least 2 weeks | At least 1 week · On the day of the exam | 0.5 | Documents — the exam schedule and course schedule, plus a result transcript afterwards — must go in at least two weeks in advance. | Think in weeks, and it's more than one. |
| `q7` | How many days of leave for your own marriage? | 5 calendar days | 3 days · 10 days | 0.25 | Marriage leave is 5 calendar days. | Marriage attracts the same number of days as bereavement of an immediate relative. |
| `q8` | How many days of paternity leave? | 3 days | 5 days · 7 days | 0.3 | Paternity leave is 3 days. | It's the same number as bereavement of a sibling. |
| `q9` | Bereavement leave for the death of a sibling? | 3 calendar days | 5 calendar days · 10 calendar days | 0.45 | Death of a sibling is 3 calendar days. Death of an immediate relative — spouse, parent or child — is 5. | Immediate relatives attract more days than siblings. |
| `q10` | How many days is each Eid holiday? | 4 days each | 3 days each · 5 days each | 0.2 | Eid al-Fitr and Eid al-Adha are each 4 days. | Both Eids are the same length. |
| `q11` | When is Founding Day? | 22 February | 23 September · 1 January | 0.4 | Founding Day is 22 February. National Day is 23 September — the two are easy to swap. | It's a February date, and the other national holiday falls in September. |
| `q12` | Can unused scientific leave be carried over? | No, never | Yes, up to 5 days · Yes, with the MD's approval | 0.55 | Scientific leave cannot be carried over. It also needs the MD's pre-approval, but approval doesn't create a carry-over. | Approval and carry-over are two different rules; only one of them is mentioned in the source. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 10 |
| Word count / est. seconds | 25 words / ≈ 10.7 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: A short practice set now. It adapts: if you're getting these, it will finish early. If you're not, it'll keep going for a few more.

New lexicon terms: Eid — “eed”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native radio group per item; Enter submits and moves on |
| Not colour-only | Result uses a glyph plus the explanation text |
| Captions / transcript | `narration_text` present; every item and explanation is real HTML |
| Timing | Untimed — no `timer_sec` on this screen |

#### 7. Build fields (edumints)

```json
{
  "type": "adaptive_practice",
  "id": "hr-045",
  "title": "Leave rules: quick practice",
  "section": "E · Your leave",
  "node_id": "hr-sE",
  "objective_ids": [
    "hr-o3"
  ],
  "points": 15,
  "evidence_screen_ids": [
    "hr-041"
  ],
  "max_items": 6,
  "target_success": 0.7,
  "pass_ratio": 0.6,
  "adaptive": {
    "strategy": "elo"
  },
  "prompt_html": "<p>Answer until the practice says you're ready. It stops early if you've got it.</p>",
  "items": [
    {
      "id": "q1",
      "difficulty": 0.2,
      "prompt_html": "<p>How many unused annual leave days can you carry over?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "Up to 5",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "Up to 10"
        },
        {
          "id": "c",
          "text_html": "All of them"
        }
      ],
      "explain_html": "<p>Carry-over is capped at 5 days. Anything above that is lost at the end of the carry-over window.</p>",
      "scaffold_html": "<p>The cap is a small number — single digits.</p>"
    },
    {
      "id": "q2",
      "difficulty": 0.35,
      "prompt_html": "<p>Carried-over annual leave must be used by when?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "End of March",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "End of June"
        },
        {
          "id": "c",
          "text_html": "End of the year"
        }
      ],
      "explain_html": "<p>Carried-over leave has to be used by the end of March of the following year.</p>",
      "scaffold_html": "<p>It's the end of a spring month.</p>"
    },
    {
      "id": "q3",
      "difficulty": 0.65,
      "prompt_html": "<p>A consulting-room physician carries over leave. By when must it be used?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "End of March"
        },
        {
          "id": "b",
          "text_html": "End of June",
          "correct": true
        },
        {
          "id": "c",
          "text_html": "End of the year"
        }
      ],
      "explain_html": "<p>Consulting-room physicians have a later deadline: the end of June.</p>",
      "scaffold_html": "<p>This group gets three months more than everyone else.</p>"
    },
    {
      "id": "q4",
      "difficulty": 0.3,
      "prompt_html": "<p>How long is maternity leave?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "12 weeks",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "10 weeks"
        },
        {
          "id": "c",
          "text_html": "8 weeks"
        }
      ],
      "explain_html": "<p>Maternity leave is 12 weeks.</p>",
      "scaffold_html": "<p>It's measured in weeks, not months — and it's the longest of the three options.</p>"
    },
    {
      "id": "q5",
      "difficulty": 0.6,
      "prompt_html": "<p>How early can maternity leave start?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "Up to 2 weeks before the due date"
        },
        {
          "id": "b",
          "text_html": "Up to 4 weeks before the due date",
          "correct": true
        },
        {
          "id": "c",
          "text_html": "On the due date only"
        }
      ],
      "explain_html": "<p>You may start up to 4 weeks before the expected delivery date.</p>",
      "scaffold_html": "<p>The allowance is measured in weeks before the due date.</p>"
    },
    {
      "id": "q6",
      "difficulty": 0.5,
      "prompt_html": "<p>Exam leave documents must be submitted how far in advance?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "At least 2 weeks",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "At least 1 week"
        },
        {
          "id": "c",
          "text_html": "On the day of the exam"
        }
      ],
      "explain_html": "<p>Documents — the exam schedule and course schedule, plus a result transcript afterwards — must go in at least two weeks in advance.</p>",
      "scaffold_html": "<p>Think in weeks, and it's more than one.</p>"
    },
    {
      "id": "q7",
      "difficulty": 0.25,
      "prompt_html": "<p>How many days of leave for your own marriage?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "5 calendar days",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "3 days"
        },
        {
          "id": "c",
          "text_html": "10 days"
        }
      ],
      "explain_html": "<p>Marriage leave is 5 calendar days.</p>",
      "scaffold_html": "<p>Marriage attracts the same number of days as bereavement of an immediate relative.</p>"
    },
    {
      "id": "q8",
      "difficulty": 0.3,
      "prompt_html": "<p>How many days of paternity leave?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "3 days",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "5 days"
        },
        {
          "id": "c",
          "text_html": "7 days"
        }
      ],
      "explain_html": "<p>Paternity leave is 3 days.</p>",
      "scaffold_html": "<p>It's the same number as bereavement of a sibling.</p>"
    },
    {
      "id": "q9",
      "difficulty": 0.45,
      "prompt_html": "<p>Bereavement leave for the death of a sibling?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "3 calendar days",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "5 calendar days"
        },
        {
          "id": "c",
          "text_html": "10 calendar days"
        }
      ],
      "explain_html": "<p>Death of a sibling is 3 calendar days. Death of an immediate relative — spouse, parent or child — is 5.</p>",
      "scaffold_html": "<p>Immediate relatives attract more days than siblings.</p>"
    },
    {
      "id": "q10",
      "difficulty": 0.2,
      "prompt_html": "<p>How many days is each Eid holiday?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "4 days each",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "3 days each"
        },
        {
          "id": "c",
          "text_html": "5 days each"
        }
      ],
      "explain_html": "<p>Eid al-Fitr and Eid al-Adha are each 4 days.</p>",
      "scaffold_html": "<p>Both Eids are the same length.</p>"
    },
    {
      "id": "q11",
      "difficulty": 0.2,
      "prompt_html": "<p>When is Founding Day?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "22 February",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "23 September"
        },
        {
          "id": "c",
          "text_html": "1 January"
        }
      ],
      "explain_html": "<p>Founding Day is 22 February. National Day is 23 September — the two are easy to swap.</p>",
      "scaffold_html": "<p>It's a February date, and the other national holiday falls in September.</p>"
    },
    {
      "id": "q12",
      "difficulty": 0.75,
      "prompt_html": "<p>Can unused scientific leave be carried over?</p>",
      "options": [
        {
          "id": "a",
          "text_html": "No, never",
          "correct": true
        },
        {
          "id": "b",
          "text_html": "Yes, up to 5 days"
        },
        {
          "id": "c",
          "text_html": "Yes, with the MD's approval"
        }
      ],
      "explain_html": "<p>Scientific leave cannot be carried over. It also needs the MD's pre-approval, but approval doesn't create a carry-over.</p>",
      "scaffold_html": "<p>Approval and carry-over are two different rules; only one of them is mentioned in the source.</p>"
    }
  ],
  "feedback": {
    "correct_html": "<p>You've got the leave numbers. Carry-over, maternity, compassionate and the holidays are the four people ask about most — they're all in the Quick Reference.</p>",
    "incorrect_html": "<p>Leave numbers are worth a second look in the HR Quick Reference. The ones people mix up are the carry-over deadline, Founding Day versus National Day, and sibling versus immediate-relative bereavement.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-045>",
  "narration_text": "OMAR: A short practice set now. It adapts: if you're getting these, it will finish early. If you're not, it'll keep going for a few more."
}
```

#### 8. Notes for SME and developer

- Open questions: **B9** — confirm `q1` and `q2` for the current year. **B2** — `q7`, `q8` and `q9` rest on the compassionate-leave table; confirm the day counts and the death-of-a-husband wording.
- Developer notes: `items` needs a minimum of 3 and the bank is 12, so `max_items` 6 is safe. `scaffold_on_wrong` is left at its default `false` because the plan specifies `loop_mode: "sample"`; turn it on only if HR wants hints during the run. No `timer_sec` — the plan rules out timers here.

---

### `hr-050` — What GOSI is

**Status:** `Draft — ready for SME review` · **Section / node:** F · Pay & social insurance / `hr-sF` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: what the deduction on the payslip is for, and why it is a benefit rather than a loss |
| Objective(s) | — (teaches `hr-o4`; assessed on `hr-052`) |
| On-the-job action | A6 |
| Source | `HR.pptx` slides 44–45 |
| Depends on Phase 0 | **B12** (current GOSI rates) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | What GOSI is |
| Body / keywords | General Organization for Social Insurance · Saudi employees only · 9.75% you + 11.75% My Clinic = **21.5%** of basic + housing |
| Word count (excl. title) | 21 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "F · Pay & social insurance", 2 px navy `#003867` header rule |
| Visual concept | A horizontal stacked bar split 9.75 / 11.75 across the full width, labelled “you” and “My Clinic” under each segment and “21.5% total” above; beneath it a single line naming what the contribution buys |
| edumints layout | `text` |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C`) · warning `accent` (Responsible magenta `#9D3293` on the key rule/figure callout only) |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (authored SVG stacked bar `hr-img-gosi-bar`) |
| Animation / reveal | Bar grows from zero, then the two segment labels fade in, then the total |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-gosi-bar` | SVG | 960×200 authored SVG stacked bar, two segments; percentages as real text, not baked in | own | “GOSI contribution: the employee pays 9.75%, My Clinic pays 11.75%, a total of 21.5%.” | No |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm, practical |
| Target seconds | 30 |
| Word count / est. seconds | 62 words / ≈ 27.4 s (speaker labels excluded, pauses included) |
| Cue targets | `what`, `who`, `split` |

> OMAR: [[cue:what]] GOSI is the General Organization for Social Insurance — the government body for social protection in Saudi Arabia. [[pause:0.4]] [[cue:who]] It applies to Saudi employees, until retirement at sixty. [[pause:0.4]] [[cue:split]] The split matters: you pay nine point seven five per cent of basic plus housing. My Clinic pays eleven point seven five. So the real contribution is twenty-one point five, and most of it isn't yours.

New lexicon terms: GOSI — “GO-see”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed |
| Not colour-only | Every segment is labelled in text with its percentage; the total is printed |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-050",
  "title": "What GOSI is",
  "section": "F · Pay & social insurance",
  "node_id": "hr-sF",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>GOSI</strong> — General Organization for Social Insurance.</p><p>Saudi employees only, until retirement at 60.</p><p>9.75% you + 11.75% My Clinic = <strong>21.5%</strong> of basic + housing. <em>Rates pending B12.</em></p>",
  "media_asset_id": "<hr-img-gosi-bar>",
  "media_alt": "GOSI contribution: the employee pays 9.75%, My Clinic pays 11.75%, a total of 21.5%.",
  "narration_asset_id": "<hr-aud-050>",
  "narration_text": "OMAR: GOSI is the General Organization for Social Insurance — the government body for social protection in Saudi Arabia. It applies to Saudi employees, until retirement at sixty. The split matters: you pay nine point seven five per cent of basic plus housing. My Clinic pays eleven point seven five. So the real contribution is twenty-one point five, and most of it isn't yours."
}
```

#### 8. Notes for SME and developer

- Open questions: **B12** — confirm the 9.75 / 11.75 / 21.5 rates against current GOSI rates for new joiners. If they change, three numbers change here, on `hr-051`, on `hr-052`, and in the Quick Reference PDF.
- Developer notes: author the bar as SVG (`svg_to_asset`) with real text, never as a flat image.

---

### `hr-051` — Working out 585 riyals

**Status:** `Draft — ready for SME review` · **Section / node:** F · Pay & social insurance / `hr-sF` · **Type:** `worked_example` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the GOSI calculation step by step, before the learner does one alone |
| Objective(s) | — (teaches `hr-o4`; assessed on `hr-052`) |
| On-the-job action | A6 |
| Source | `HR.pptx` slide 46 |
| Depends on Phase 0 | **B12** (GOSI rates) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Working out 585 riyals |
| Body / keywords | *(problem statement in `intro_html`)* |
| Word count (excl. title) | 0 |
| Instruction | Reveal why each step is taken, one step at a time. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "F · Pay & social insurance", 2 px navy `#003867` header rule |
| Visual concept | A three-row calculation ledger: each row shows one line of arithmetic in large mono-ish numerals with a “Why?” control to the right; the final row is boxed and carries the answer in the accent colour plus a SAR label |
| edumints layout | n/a (`worked_example`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | `fading: "partial"` — the arithmetic is visible, the rationale is behind a per-step control |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (the ledger is CSS).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Problem (`intro_html`) | “Basic 4,800 + housing 1,200. What is the monthly GOSI deduction from your salary?” |
| Steps | See the table below. |
| Correct answer(s) | n/a — unscored worked example |
| Points | 0 |
| Self-explanation prompt | “Which part of the salary is the percentage applied to?” |
| Retry / lives | n/a |

| # | Action | Rationale (revealed) |
|---|---|---|
| 1 | Add basic and housing: 4,800 + 1,200 = 6,000. | GOSI is charged on basic salary **plus** housing allowance, not on basic alone and not on total pay with allowances and bonuses. |
| 2 | Apply the employee rate: 6,000 × 9.75%. | Only your share is deducted from your salary. The company's 11.75% is paid on top and never appears as a deduction on your payslip. |
| 3 | Result: 585 SAR deducted each month. | 6,000 × 0.0975 = 585. This is the line you'll see on your payslip. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm, precise |
| Target seconds | 30 |
| Word count / est. seconds | 65 words / ≈ 28.7 s (speaker labels excluded, pauses included) |
| Cue targets | `s1`, `s2`, `s3` |

> OMAR: Let's do one together. Basic four thousand eight hundred, housing one thousand two hundred. [[cue:s1]] Add them — GOSI is charged on basic plus housing, so six thousand. [[pause:0.4]] [[cue:s2]] Apply your rate, nine point seven five per cent. The company's rate never touches your payslip. [[pause:0.4]] [[cue:s3]] Six thousand times nought point nought nine seven five is five hundred and eighty-five riyals a month. That's the line to look for.

New lexicon terms: SAR — say “Saudi riyals” (never “S-A-R”)

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each “Why?” control is a native `<button>` with `aria-expanded` |
| Not colour-only | The answer row is boxed and labelled “585 SAR”, not colour-coded alone |
| Captions / transcript | `narration_text` present; all arithmetic is real HTML text |
| Timing | Untimed; the self-explanation field never blocks Continue |

#### 7. Build fields (edumints)

```json
{
  "type": "worked_example",
  "id": "hr-051",
  "title": "Working out 585 riyals",
  "section": "F · Pay & social insurance",
  "node_id": "hr-sF",
  "objective_ids": [],
  "points": 0,
  "fading": "partial",
  "intro_html": "<p>Basic 4,800 + housing 1,200. What is the monthly GOSI deduction from your salary? <em>Rates pending B12.</em></p>",
  "steps": [
    {
      "action_html": "<p>Add basic and housing: 4,800 + 1,200 = <strong>6,000</strong>.</p>",
      "rationale_html": "<p>GOSI is charged on basic salary <strong>plus housing allowance</strong>, not on basic alone and not on total pay with allowances and bonuses.</p>"
    },
    {
      "action_html": "<p>Apply the employee rate: 6,000 × <strong>9.75%</strong>.</p>",
      "rationale_html": "<p>Only your share is deducted from your salary. The company's 11.75% is paid on top and never appears as a deduction on your payslip.</p>"
    },
    {
      "action_html": "<p>Result: <strong>585 SAR</strong> deducted each month.</p>",
      "rationale_html": "<p>6,000 × 0.0975 = 585. This is the line you'll see on your payslip.</p>",
      "artifact_asset_id": "<hr-img-gosi-bar>",
      "artifact_caption": "Your 9.75% employee share (585 SAR) sits alongside My Clinic's 11.75% contribution."
    }
  ],
  "self_explanation_prompt_html": "<p>Which part of the salary is the percentage applied to?</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-051>",
  "narration_text": "OMAR: Let's do one together. Basic four thousand eight hundred, housing one thousand two hundred. Add them — GOSI is charged on basic plus housing, so six thousand. Apply your rate, nine point seven five per cent. The company's rate never touches your payslip. Six thousand times nought point nought nine seven five is five hundred and eighty-five riyals a month. That's the line to look for."
}
```

#### 8. Notes for SME and developer

- Open questions: **B12** — rates.
- Developer notes: the narration says the numbers as words (“nine point seven five per cent”). If the TTS voice misreads a decimal, switch the audio to “nine and three-quarters per cent” and keep the text as is.

---

### `hr-052` — Your turn

**Status:** `Draft — ready for SME review` · **Section / node:** F · Pay & social insurance / `hr-sF` · **Type:** `fill_blank` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: do the GOSI calculation once, unaided |
| Objective(s) | `hr-o4` |
| On-the-job action | A6 |
| Source | `HR.pptx` slide 46 (same formula as the worked example) |
| Depends on Phase 0 | **B12** (GOSI rates) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Your turn |
| Body / keywords | Basic 6,000 + housing 1,500. Your monthly GOSI deduction = ___ SAR |
| Word count (excl. title) | 12 |
| Instruction | Type the number. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "F · Pay & social insurance · Check", 2 px navy `#003867` header rule |
| Visual concept | A large centred equation with a single inline input at the blank; beneath it a small muted line reminding the learner of the two inputs, and nothing else — no imagery to distract from the arithmetic |
| edumints layout | n/a (`fill_blank`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only question).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “Basic 6,000 + housing 1,500. Your monthly GOSI deduction = ___ SAR” |
| Blank | `b1` — accepted answers below |
| Accepted variants | `731.25` · `731.25 SAR` · `731.25 SR` · `731.25 riyals` · `731.25 Saudi riyals` · `731` · `731 SAR` |
| Points | 10 |
| Feedback — correct | Right. Basic 6,000 + housing 1,500 = 7,500, and 7,500 × 9.75% = 731.25 SAR a month. |
| Feedback — incorrect | Not quite. Add basic and housing first — that's 7,500 — then take 9.75% of that, not of the basic alone. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 15 words / ≈ 6.4 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Your turn. Basic six thousand, housing one thousand five hundred. What's your monthly GOSI deduction?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Labelled `<input>`; Enter submits |
| Not colour-only | Correct/incorrect uses a glyph plus the working shown as text |
| Captions / transcript | `narration_text` present; the working appears in the feedback text |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "fill_blank",
  "id": "hr-052",
  "title": "Your turn",
  "section": "F · Pay & social insurance",
  "node_id": "hr-sF",
  "objective_ids": [
    "hr-o4"
  ],
  "points": 10,
  "evidence_screen_ids": [
    "hr-051"
  ],
  "case_sensitive": false,
  "prompt_html": "<p>Basic 6,000 + housing 1,500. Your monthly GOSI deduction = ___ SAR. <em>Rates pending B12.</em></p>",
  "blanks": [
    {
      "id": "b1",
      "accepted": [
        "731.25",
        "731.25 SAR",
        "731.25 SR",
        "731.25 riyals",
        "731.25 Saudi riyals",
        "731",
        "731 SAR"
      ]
    }
  ],
  "feedback": {
    "correct_html": "<p>Right. Basic 6,000 + housing 1,500 = 7,500, and 7,500 × 9.75% = <strong>731.25 SAR</strong> a month.</p>",
    "incorrect_html": "<p>Not quite. Add basic and housing first — that's 7,500 — then take 9.75% of that, not of the basic alone.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-052>",
  "narration_text": "OMAR: Your turn. Basic six thousand, housing one thousand five hundred. What's your monthly GOSI deduction?"
}
```

#### 8. Notes for SME and developer

- Open questions: **B12** — if the rate changes, `hr-050`, `hr-051`, this screen's accepted answers and feedback, and the Quick Reference all change together.
- Developer notes: `case_sensitive: false`. The `731` variants are included so a learner who rounds is not marked wrong; if Payroll wants exact answers only, drop `731` and `731 SAR` from the accepted list.

---

### `hr-053` — Working out overtime

**Status:** `Draft — ready for SME review` · **Section / node:** F · Pay & social insurance / `hr-sF` · **Type:** `worked_example` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: the hourly rate first, then the multiplier, so the learner can rebuild it from memory |
| Objective(s) | — (teaches `hr-o4`; assessed on `hr-054`) |
| On-the-job action | A6 |
| Source | `HR.pptx` slide 48 |
| Depends on Phase 0 | **B3** (which grades are eligible for overtime) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Working out overtime |
| Body / keywords | *(problem statement in `intro_html`)* |
| Word count (excl. title) | 0 |
| Instruction | Reveal why each step is taken, one step at a time. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "F · Pay & social insurance", 2 px navy `#003867` header rule |
| Visual concept | A three-row ledger like `hr-051`, but the third row forks into two stacked results — “normal day ×1.5” and “public holiday ×2” — so the learner sees one rate and two multipliers |
| edumints layout | n/a (`worked_example`) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` on active tabs/chevrons/pins/progress) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | `fading: "partial"` |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (the ledger is CSS).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Problem (`intro_html`) | “Basic 6,000. What is your overtime rate on a normal working day, and on a public holiday?” |
| Steps | See the table below. |
| Correct answer(s) | n/a — unscored worked example |
| Points | 0 |
| Self-explanation prompt | “Why is the hourly rate worked out from 240 hours, not 208?” |
| Retry / lives | n/a |

| # | Action | Rationale (revealed) |
|---|---|---|
| 1 | Work out the hourly rate: 6,000 ÷ (30 × 8) = 6,000 ÷ 240 = 25 SAR/hour. | The formula uses a 30-day month at 8 hours a day, so 240 hours. Everything else in the calculation hangs off this one number. |
| 2 | Normal working day: 25 × 1.5 = 37.50 SAR/hour. | Overtime on a normal working day is paid at time and a half. |
| 3 | Public holiday: 25 × 2 = 50 SAR/hour. | Overtime on a public holiday is paid at double time. Note it's the same hourly rate — only the multiplier changes. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm, precise |
| Target seconds | 35 |
| Word count / est. seconds | 79 words / ≈ 35.5 s (speaker labels excluded, pauses included) |
| Cue targets | `s1`, `s2`, `s3`, `elig` |

> OMAR: [[cue:elig]] One caveat before the numbers: whether you're eligible for overtime at all depends on your grade. Check that first. [[pause:0.4]] [[cue:s1]] Now the arithmetic. Basic six thousand. Divide by thirty days times eight hours — two hundred and forty hours — and you get twenty-five riyals an hour. [[pause:0.4]] [[cue:s2]] On a normal working day, multiply by one and a half. That's thirty-seven riyals fifty. [[pause:0.4]] [[cue:s3]] On a public holiday, multiply by two. Fifty riyals an hour. [[pause:0.4]] Same hourly rate both times. Only the multiplier moves.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Each “Why?” control is a native `<button>` with `aria-expanded` |
| Not colour-only | Rows are labelled “normal working day” and “public holiday” in text |
| Captions / transcript | `narration_text` present; all arithmetic is real HTML |
| Timing | Untimed; the self-explanation field never blocks Continue |

#### 7. Build fields (edumints)

```json
{
  "type": "worked_example",
  "id": "hr-053",
  "title": "Working out overtime",
  "section": "F · Pay & social insurance",
  "node_id": "hr-sF",
  "objective_ids": [],
  "points": 0,
  "fading": "partial",
  "intro_html": "<p>Basic 6,000. What is your overtime rate on a normal working day, and on a public holiday? <em>Eligibility by grade pending B3.</em></p>",
  "steps": [
    {
      "action_html": "<p>Hourly rate: 6,000 ÷ (30 × 8) = 6,000 ÷ 240 = <strong>25 SAR/hour</strong>.</p>",
      "rationale_html": "<p>The formula uses a 30-day month at 8 hours a day, so 240 hours. Everything else in the calculation hangs off this one number.</p>",
      "artifact_asset_id": "<hr-img-gosi-bar>",
      "artifact_caption": "Hourly rate = basic salary ÷ 30 days ÷ 8 hours, then multiplied by 1.5 (regular) or 2.0 (public holiday)."
    },
    {
      "action_html": "<p>Normal working day: 25 × 1.5 = <strong>37.50 SAR/hour</strong>.</p>",
      "rationale_html": "<p>Overtime on a normal working day is paid at time and a half.</p>"
    },
    {
      "action_html": "<p>Public holiday: 25 × 2 = <strong>50 SAR/hour</strong>.</p>",
      "rationale_html": "<p>Overtime on a public holiday is paid at double time. Note it's the same hourly rate — only the multiplier changes.</p>"
    }
  ],
  "self_explanation_prompt_html": "<p>Why is the hourly rate worked out from 240 hours, not 208?</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-053>",
  "narration_text": "OMAR: One caveat before the numbers: whether you're eligible for overtime at all depends on your grade. Check that first. Now the arithmetic. Basic six thousand. Divide by thirty days times eight hours — two hundred and forty hours — and you get twenty-five riyals an hour. On a normal working day, multiply by one and a half. That's thirty-seven riyals fifty. On a public holiday, multiply by two. Fifty riyals an hour. Same hourly rate both times. Only the multiplier moves."
}
```

#### 8. Notes for SME and developer

- Open questions: **B3** — the slide says overtime “depends on grade” but gives one formula. Until HR confirms, the card states the caveat in the intro and in the narration, and does not claim that every grade is eligible.
- Developer notes: `worked_example` carries no `points`.

---

### `hr-054` — Four hours on Tuesday

**Status:** `Draft — ready for SME review` · **Section / node:** F · Pay & social insurance / `hr-sF` · **Type:** `mcq` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: apply the overtime formula to a normal working day |
| Objective(s) | `hr-o4` |
| On-the-job action | A6 |
| Source | `HR.pptx` slide 48 |
| Depends on Phase 0 | **B3** (grade eligibility) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Four hours on Tuesday |
| Body / keywords | *(stem only)* |
| Word count (excl. title) | 0 |
| Instruction | Choose one. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "F · Pay & social insurance · Check", 2 px navy `#003867` header rule |
| Visual concept | Stem in large type; four plain option rows, each a single amount; no imagery, so the arithmetic carries the screen |
| edumints layout | n/a (`mcq`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only question).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “Basic 6,000. You work 4 overtime hours on a normal working day. What is the overtime pay?” |
| Options | `a` 150 SAR ✔ · `b` 100 SAR · `c` 200 SAR · `d` 240 SAR |
| Correct answer(s) | `a` — 150 SAR |
| Points | 10 |
| Feedback — correct | Right. Hourly rate is 6,000 ÷ 240 = 25, then 25 × 1.5 × 4 hours = 150 SAR. |
| Feedback — incorrect | Not quite. Build it in three moves: 6,000 ÷ 240 = 25 an hour, × 1.5 for a normal day, × 4 hours. |
| Per-option feedback | `a` 150 SAR — Correct: 25 × 1.5 × 4 = 150. · `b` 100 SAR — That's 25 × 4. You've worked out the plain hourly pay and left out the time-and-a-half multiplier. · `c` 200 SAR — That's 25 × 2 × 4. Double time is for a public holiday, not a normal working day. · `d` 240 SAR — That doesn't come from the formula. Go back to the hourly rate first: 6,000 ÷ 240. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 20 words / ≈ 8.6 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: One for you. Basic six thousand. You work four overtime hours on a normal working day. What's the overtime pay?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native radio group |
| Not colour-only | Result uses a glyph plus words; every option carries the working |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "hr-054",
  "title": "Four hours on Tuesday",
  "section": "F · Pay & social insurance",
  "node_id": "hr-sF",
  "objective_ids": [
    "hr-o4"
  ],
  "points": 10,
  "evidence_screen_ids": [
    "hr-053"
  ],
  "prompt_html": "<p>Basic 6,000. You work 4 overtime hours on a normal working day. What is the overtime pay?</p>",
  "options": [
    {
      "id": "a",
      "text_html": "150 SAR",
      "correct": true,
      "feedback_html": "<p>Right. Hourly rate is 6,000 ÷ 240 = 25, then 25 × 1.5 × 4 hours = 150 SAR.</p>"
    },
    {
      "id": "b",
      "text_html": "100 SAR",
      "feedback_html": "<p>That's 25 × 4. You've worked out the plain hourly pay and left out the time-and-a-half multiplier.</p>"
    },
    {
      "id": "c",
      "text_html": "200 SAR",
      "feedback_html": "<p>That's 25 × 2 × 4. Double time is for a public holiday, not a normal working day.</p>"
    },
    {
      "id": "d",
      "text_html": "240 SAR",
      "feedback_html": "<p>That doesn't come from the formula. Go back to the hourly rate first: 6,000 ÷ 240.</p>"
    }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Right. Hourly rate is 6,000 ÷ 240 = 25, then 25 × 1.5 × 4 hours = 150 SAR.</p>",
    "incorrect_html": "<p>Not quite. Build it in three moves: 6,000 ÷ 240 = 25 an hour, × 1.5 for a normal day, × 4 hours.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-054>",
  "narration_text": "OMAR: One for you. Basic six thousand. You work four overtime hours on a normal working day. What's the overtime pay?"
}
```

#### 8. Notes for SME and developer

- Open questions: **B3** — if HR confirms that eligibility grades differ, add the caveat to the stem rather than changing the arithmetic.
- Developer notes: none.

---

### `hr-060` — Which system?

**Status:** `Draft — ready for SME review` · **Section / node:** G · Systems & licences / `hr-sG` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: route each HR task to the right system, so the learner stops emailing HR |
| Objective(s) | `hr-o5` |
| On-the-job action | A7 |
| Source | `HR.pptx` slides 47, 50–54, 59–60 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Which system? |
| Body / keywords | Six tasks, four systems. Match each task to where it happens. |
| Word count (excl. title) | 10 |
| Instruction | Match each task to its system. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "G · Systems & licences · Check", 2 px navy `#003867` header rule |
| Visual concept | Two columns: six task cards on the left, four system tiles on the right, each system tile carrying a small monogram (O, Q, M, I); a connector line follows the selection |
| edumints layout | n/a (`matching`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (monogram system tiles O, Q, M, I in navy #003867) |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only interaction).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Pairs (left → right) | `p1` Request annual leave → Oracle · `p2` Ask for an employment certificate → Oracle · `p3` Accept your employment contract → Qiwa · `p4` Renew your professional licence → Mumaris (SCFHS) · `p5` Read the employee guide and corporate discounts → Intranet · `p6` Resign → Oracle |
| Correct answer(s) | As listed. Oracle appears three times. |
| Points | 10 |
| Feedback — correct | Right. Three of the six run through Oracle, because they're all requests that need a record. Contracts are accepted on Qiwa, licences are renewed on Mumaris, and the guide lives on the intranet. |
| Feedback — incorrect | Not all six. Ask yourself which of these are *requests* — those go through Oracle. The contract and the licence are external platforms, and the guide is just reading. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Practical |
| Target seconds | 10 |
| Word count / est. seconds | 19 words / ≈ 8.1 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Six tasks, four systems. Match each one to where it actually happens. Most of them are the same system.

New lexicon terms: Qiwa — “KEE-wa”; Mumaris — “mu-MAH-ris”; SCFHS — “S-C-F-H-S”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Selectable list on the left, activatable tiles on the right |
| Not colour-only | Result uses a glyph plus the words; system tiles carry letter monograms as well as names |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "matching",
  "id": "hr-060",
  "title": "Which system?",
  "section": "G · Systems & licences",
  "node_id": "hr-sG",
  "objective_ids": [
    "hr-o5"
  ],
  "points": 10,
  "evidence_screen_ids": [
    "hr-040"
  ],
  "prompt_html": "<p>Six tasks, four systems. Match each task to where it happens.</p>",
  "pairs": [
    {
      "id": "p1",
      "left_html": "Request annual leave",
      "right_html": "Oracle"
    },
    {
      "id": "p2",
      "left_html": "Ask for an employment certificate",
      "right_html": "Oracle"
    },
    {
      "id": "p3",
      "left_html": "Accept your employment contract",
      "right_html": "Qiwa"
    },
    {
      "id": "p4",
      "left_html": "Renew your professional licence",
      "right_html": "Mumaris (SCFHS)"
    },
    {
      "id": "p5",
      "left_html": "Read the employee guide and corporate discounts",
      "right_html": "Intranet"
    },
    {
      "id": "p6",
      "left_html": "Resign",
      "right_html": "Oracle"
    }
  ],
  "feedback": {
    "correct_html": "<p>Right. Three of the six run through Oracle, because they're all requests that need a record. Contracts are accepted on Qiwa, licences are renewed on Mumaris, and the guide lives on the intranet.</p>",
    "incorrect_html": "<p>Not all six. Ask yourself which of these are <em>requests</em> — those go through Oracle. The contract and the licence are external platforms, and the guide is just reading.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-060>",
  "narration_text": "OMAR: Six tasks, four systems. Match each one to where it actually happens. Most of them are the same system."
}
```

#### 8. Notes for SME and developer

- Open questions: None. The routing is taken from slides 47, 50–54 and 59–60.
- Developer notes: Oracle appears as the correct answer three times. That is intentional — if a future `matching` implementation penalises repeated right-hand values, split this into two 3-pair screens (a plan change).

---

### `hr-061` — Book your leave in Oracle

**Status:** `Draft — ready for SME review` · **Section / node:** G · Systems & licences / `hr-sG` · **Type:** `simulation` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: complete the five Oracle clicks for an annual-leave request on a test account |
| Objective(s) | `hr-o5` |
| On-the-job action | A7 |
| Source | `HR.pptx` slide 51 (Oracle HR self-service screenshots and sub-steps) |
| Depends on Phase 0 | **B8** (test-account screenshots with no real employee data) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Book your leave in Oracle |
| Body / keywords | Five steps. These screenshots come from a test account, so nothing here is real. |
| Word count (excl. title) | 14 |
| Instruction | Follow the instruction on each step and click the right place. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario (see `../../00_program/brand/screen-mockups/05-scenario.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "G · Systems & licences", 2 px navy `#003867` header rule |
| Visual concept | A browser-chrome frame holding a full-width screenshot; a numbered instruction bar sits directly above the frame; the correct region is not outlined until the learner asks for a hint, at which point a dashed rectangle appears around it |
| edumints layout | n/a (`simulation`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` stage and choice cards with `#D9E1E8` border) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` progress bar) · companion avatar ring in the character's colour (companions.md §4) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; situation Montserrat SemiBold 600, 17 px; choices Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (Oracle test-account screenshots) |
| Animation / reveal | The next screenshot cross-fades in on a correct click; the tip card fades up with the end-of-simulation feedback |
| Companion | Dr. Omar · `char-omar-avatar-neutral` (40 px) in the end-of-simulation feedback banner, plus an **Omar's tip** card under the banner: 56 px avatar with a 3 px teal `#008C99` ring, white card max 360 px wide with a 4 px teal left edge, label “Omar's tip” · placement L4 feedback avatar / tip **after** the simulation only — not visible during any click step and never over the screenshot · tip text (15 words): “Submitted isn't approved. Check the request status in Oracle before you book flights or hotels.” · speaks: Omar (set-up line on entry; tip line `omar-tip` with the feedback) |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-oracle-1` | screenshot | Oracle Applications Cloud sign-in page, test account, 1920×1080 | own (test account — B8) | “Oracle sign-in page with empty username and password fields and a Sign In button.” | No |
| `hr-img-oracle-2` | screenshot | Oracle home with the Time and Absences tile | own (test account — B8) | “Oracle home page with a Time and Absences tile in the quick actions area.” | No |
| `hr-img-oracle-3` | screenshot | Time and Absences hub with the Add Leaves tile | own (test account — B8) | “Oracle Time and Absences page with an Add Leaves tile.” | No |
| `hr-img-oracle-4` | screenshot | Add Leaves form with the leave-type drop-down open, showing Annual, Bereavement, Marriage, Scientific, Sick, Study | own (test account — B8) | “Oracle Add Leaves form with the leave-type drop-down open.” | No |
| `hr-img-oracle-5` | screenshot | Add Leaves form filled, with a Submit button | own (test account — B8) | “Oracle Add Leaves form with dates entered and a Submit button.” | No |
| `char-omar-avatar-neutral` | illustration | Shared programme avatar (Canva media `MAHX-nPHDkA`), cropped to a circle: 40 px in the feedback banner, 56 px on the tip card | ai-generated (programme master, companions.md §3) | “Dr. Omar, a family physician, giving a tip.” | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Steps | See the table below. All five are click steps with `rect` regions. |
| Correct answer(s) | One region per step, `correct: true` |
| Points | 15 |
| Feedback — correct | That's the whole flow: sign in, Time and Absences, Add Leaves, choose the leave type and dates, submit. Your manager approves it in the same system, so you can see where it's got to. |
| Feedback — incorrect | Not every step. The route is always the same: sign in, then Time and Absences, then Add Leaves. The last two steps are the form itself. |
| Tip card (both outcomes) | **Omar's tip:** Submitted isn't approved. Check the request status in Oracle before you book flights or hotels. (spoken differently by Omar — see §5, part `omar-tip`) |
| Hint | One per step — see the table |
| Retry / lives | Retry the step; no lives (phase-3 §5) |

| # | Screenshot | Instruction | Region (rough position) | Hint |
|---|---|---|---|---|
| 1 | `hr-img-oracle-1` | Sign in to Oracle. | `signin` rect — the Sign In button, centre-right under the password field | “Use the <em>Sign In</em> button under the password field.” |
| 2 | `hr-img-oracle-2` | Open the area where you manage your time and leave. | `timeabs` rect — the Time and Absences tile, upper-left of the quick actions row | “Look for <em>Time and Absences</em> in the quick actions.” |
| 3 | `hr-img-oracle-3` | Open the page where you add a new leave request. | `addleaves` rect — the Add Leaves tile, centre of the hub | “Look for <em>Add Leaves</em> under Time and Absences.” |
| 4 | `hr-img-oracle-4` | Choose *Annual* from the leave-type list. | `leavetype` rect — the leave-type drop-down, upper-left of the form | “The leave type is a drop-down near the top of the form.” |
| 5 | `hr-img-oracle-5` | Send the request. | `submit` rect — the Submit button, bottom-right of the form | “<em>Submit</em> sits at the bottom of the form.” |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) — set-up `omar-1` on entry; tip `omar-tip` with the end-of-simulation feedback |
| Tone | Practical, calm |
| Target seconds | 15 — per part: `omar-1` 15, `omar-tip` 9 |
| Word count / est. seconds | 27 words / ≈ 11.6 s (speaker labels excluded, pauses included); tip line 22 words / ≈ 9.4 s |
| Cue targets | None |

> OMAR: Let's do it once for real, on a test account. Book yourself a week of annual leave. Five steps, and I'll tell you what to look for.

*Tip line — played with the end-of-simulation feedback, with the tip card (part `omar-tip`):*

> OMAR: One habit worth building. After you submit, open the request again. Wait until it shows as approved before you book any travel.

New lexicon terms: Oracle — “OR-uh-kul”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Regions are focusable buttons in DOM order; Enter activates; the hint is a native `<button>` |
| Not colour-only | The step number and instruction are text; the hint rectangle is a dashed outline plus the instruction text |
| Captions / transcript | `narration_text` present; every screenshot has alt text; the end-of-screen feedback repeats the five steps as a text list |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "simulation",
  "id": "hr-061",
  "title": "Book your leave in Oracle",
  "section": "G · Systems & licences",
  "node_id": "hr-sG",
  "notes": "Companion: Dr. Omar char-omar-avatar-neutral (40 px) in the end-of-simulation feedback banner plus the 'Omar's tip' card (56 px avatar, teal #008C99 ring, 4 px teal left edge, max 360 px) — only after the last step, never during a click step. Tip audio: part omar-tip, played with the feedback.",
  "objective_ids": [
    "hr-o5"
  ],
  "points": 15,
  "evidence_screen_ids": [
    "hr-040"
  ],
  "prompt_html": "<p>Five steps. These screenshots come from a test account, so nothing here is real.</p>",
  "steps": [
    {
      "image_asset_id": "<hr-img-oracle-1>",
      "image_alt": "Oracle sign-in page with empty username and password fields and a Sign In button.",
      "instruction_html": "<p>Sign in to Oracle.</p>",
      "regions": [
        {
          "id": "signin",
          "shape": "rect",
          "coords": [
            1180,
            620,
            180,
            56
          ],
          "correct": true,
          "label_html": "Sign In"
        }
      ],
      "hint_html": "<p>Use the <em>Sign In</em> button under the password field.</p>"
    },
    {
      "image_asset_id": "<hr-img-oracle-2>",
      "image_alt": "Oracle home page with a Time and Absences tile in the quick actions area.",
      "instruction_html": "<p>Open the area where you manage your time and leave.</p>",
      "regions": [
        {
          "id": "timeabs",
          "shape": "rect",
          "coords": [
            260,
            300,
            320,
            200
          ],
          "correct": true,
          "label_html": "Time and Absences"
        }
      ],
      "hint_html": "<p>Look for <em>Time and Absences</em> in the quick actions.</p>"
    },
    {
      "image_asset_id": "<hr-img-oracle-3>",
      "image_alt": "Oracle Time and Absences page with an Add Leaves tile.",
      "instruction_html": "<p>Open the page where you add a new leave request.</p>",
      "regions": [
        {
          "id": "addleaves",
          "shape": "rect",
          "coords": [
            420,
            310,
            220,
            140
          ],
          "correct": true,
          "label_html": "Add Leaves"
        }
      ],
      "hint_html": "<p>Look for <em>Add Leaves</em> under Time and Absences.</p>"
    },
    {
      "image_asset_id": "<hr-img-oracle-4>",
      "image_alt": "Oracle Add Leaves form with the leave-type drop-down open.",
      "instruction_html": "<p>Choose <em>Annual</em> from the leave-type list.</p>",
      "regions": [
        {
          "id": "leavetype",
          "shape": "rect",
          "coords": [
            300,
            260,
            420,
            60
          ],
          "correct": true,
          "label_html": "Leave type"
        }
      ],
      "hint_html": "<p>The leave type is a drop-down near the top of the form.</p>"
    },
    {
      "image_asset_id": "<hr-img-oracle-5>",
      "image_alt": "Oracle Add Leaves form with dates entered and a Submit button.",
      "instruction_html": "<p>Send the request.</p>",
      "regions": [
        {
          "id": "submit",
          "shape": "rect",
          "coords": [
            1500,
            900,
            180,
            56
          ],
          "correct": true,
          "label_html": "Submit"
        }
      ],
      "hint_html": "<p><em>Submit</em> sits at the bottom of the form.</p>"
    }
  ],
  "feedback": {
    "correct_html": "<p>That's the whole flow: sign in, Time and Absences, Add Leaves, choose the leave type and dates, submit. Your manager approves it in the same system, so you can see where it's got to.</p><p class=\"companion-tip companion-omar\"><strong>Omar's tip:</strong> Submitted isn't approved. Check the request status in Oracle before you book flights or hotels.</p>",
    "incorrect_html": "<p>Not every step. The route is always the same: sign in, then Time and Absences, then Add Leaves. The last two steps are the form itself.</p><p class=\"companion-tip companion-omar\"><strong>Omar's tip:</strong> Submitted isn't approved. Check the request status in Oracle before you book flights or hotels.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-061>",
  "narration_text": "OMAR: Let's do it once for real, on a test account. Book yourself a week of annual leave. Five steps, and I'll tell you what to look for."
}
```

#### 8. Notes for SME and developer

- Open questions: **B8** — every screenshot must come from a test account with no real employee data. Until HRIS supplies them, this screen cannot be built; ship the module without it and add it in a minor version, or replace it with a five-step `sorting` screen (a plan change, because the points and the objective evidence both move).
- Developer notes: Omar's avatar and tip card render only with the end-of-simulation feedback (the `companion-tip` paragraph); play `MC03-welcome-on-board_hr-061_omar-tip.mp3` with that feedback, not on screen entry. `coords` for `rect` are `[x, y, w, h]` in the image's natural pixels. All five sets above are **provisional** against 1920×1080 screenshots and must be re-measured after the final captures. Record the Oracle release in the asset notes and re-capture when the UI changes (phase-5 trigger).

---

### `hr-062` — Thirty days left

**Status:** `Draft — ready for SME review` · **Section / node:** G · Systems & licences / `hr-sG` · **Type:** `true_false` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: the licence-renewal rule that can stop someone working |
| Objective(s) | `hr-o5` |
| On-the-job action | A8 |
| Source | `HR.pptx` slide 49 (SCFHS / Mumaris) |
| Depends on Phase 0 | **B13** (the 30-day suspension rule) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Thirty days left |
| Body / keywords | *(statement only)* |
| Word count (excl. title) | 0 |
| Instruction | True or false? |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "G · Systems & licences · Check", 2 px navy `#003867` header rule |
| Visual concept | The statement in large type centred, with two wide side-by-side buttons beneath labelled True and False; no imagery, so the judgement carries the screen |
| edumints layout | n/a (`true_false`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only question).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “If your professional licence will expire in less than 30 days without renewal, HR may suspend you from work.” (⚠ PENDING B13) |
| Correct answer | `true` |
| Points | 5 |
| Feedback — correct | True. With fewer than 30 days to expiry and no renewal, HR may suspend you. Renew early on Mumaris: My Clinic covers the expense claim, but it does not pay penalties for late renewal. |
| Feedback — incorrect | It's true. My Clinic may suspend you if your licence has under 30 days left and hasn't been renewed. Renew on Mumaris well before that — the company pays the fee claim, not the late penalties. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Serious |
| Target seconds | 8 |
| Word count / est. seconds | 19 words / ≈ 8.1 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: True or false: if your licence expires in under thirty days without renewal, HR may suspend you from work.

New lexicon terms: Mumaris — “mu-MAH-ris”; SCFHS — “S-C-F-H-S”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Two native buttons; both reachable and activatable by keyboard |
| Not colour-only | Buttons are labelled True and False in text; result uses a glyph plus the explanation |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "true_false",
  "id": "hr-062",
  "title": "Thirty days left",
  "section": "G · Systems & licences",
  "node_id": "hr-sG",
  "objective_ids": [
    "hr-o5"
  ],
  "points": 5,
  "evidence_screen_ids": [
    "hr-040"
  ],
  "prompt_html": "<p>If your professional licence will expire in less than 30 days without renewal, HR may suspend you from work. <em>Pending B13.</em></p>",
  "correct": true,
  "feedback": {
    "correct_html": "<p>True. With fewer than 30 days to expiry and no renewal, HR may suspend you. Renew early on Mumaris: My Clinic covers the expense claim, but it does not pay penalties for late renewal.</p>",
    "incorrect_html": "<p>It's true. My Clinic may suspend you if your licence has under 30 days left and hasn't been renewed. Renew on Mumaris well before that — the company pays the fee claim, not the late penalties.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-062>",
  "narration_text": "OMAR: True or false: if your licence expires in under thirty days without renewal, HR may suspend you from work."
}
```

#### 8. Notes for SME and developer

- Open questions: **B13** — confirm the 30-day suspension rule with HR. If it changes, the statement, both feedback strings and the Quick Reference change together.
- Developer notes: non-clinical staff have no professional licence. If HR wants them to skip this screen, use `visible_if` on a licence-holder variable set by an earlier screen — that needs a plan change, because it introduces variables into the module.

---

### `hr-070` — Your ID card and benefits

**Status:** `Draft — ready for SME review` · **Section / node:** H · ID, benefits & dress code / `hr-sH` · **Type:** `content_slide` (`blocks`) · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: how to look after the ID card, and what the benefits package actually contains |
| Objective(s) | — (teaches `hr-o6`; assessed on `hr-071`) |
| On-the-job action | A9 |
| Source | `HR.pptx` slides 55, 57 |
| Depends on Phase 0 | **B4** (the 100 SAR lost-card penalty) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Your ID card and benefits |
| Body / keywords | Lost card → email HR. Replacement fee ⚠ PENDING B4. Damaged card → replaced free. |
| Word count (excl. title) | 15 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "H · ID, benefits & dress code", 2 px navy `#003867` header rule |
| Visual concept | A two-card row: the left card shows an ID badge with a small warning line about lost cards; the right card is a six-segment benefits wheel, each segment labelled with a one- or two-word benefit and a line icon |
| edumints layout | `text` (blocks: image, caption, image, caption) |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C`) · warning `accent` (Responsible magenta `#9D3293` on the key rule/figure callout only) |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Six single-weight line icons inside `hr-img-benefits-wheel` (shield, star, graduation-cap, laptop-home, arrow-up, tag), navy #003867, own SVG |
| Animation / reveal | Left card fades up, then the wheel segments fill in sequence |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-idcard` | illustration | Flat ID badge on a lanyard, first name only, no real logo until approved | ai-generated | “A My Clinic staff ID badge on a lanyard.” | No |
| `hr-img-benefits-wheel` | SVG | 600×600 six-segment wheel: health insurance, performance bonus, development, hybrid work, internal advancement, discounts; labels as real text | own | “Benefits wheel: health insurance, annual performance bonuses, employee development, hybrid work, internal advancement and discounts.” | No |

**AI image prompt** (`hr-img-idcard` — per `brand-identity.md` §6):

```text
Flat vector illustration for a healthcare e-learning course, 16:9, a vertical staff ID badge holder suspended on a Caring purple (#652D8C) fabric lanyard with a simple silhouette avatar icon and horizontal placeholder bars inside the card frame. Clean minimalist style, simple geometric shapes, thin navy (#003867) outlines, white and very light blue-grey (#F4F7FA, #C0CED9) surfaces, one highlight colour Caring purple (#652D8C), small touches of magenta (#9D3293) only for nothing. Bright and calm, lots of white space, soft even lighting, no shadows or very soft flat shadows.
People: no people (silhouette icon on badge only).
No text, no letters, no numbers, no logos, no signage words, no watermarks, no brand names.
```

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Practical, warm |
| Target seconds | 25 |
| Word count / est. seconds | 57 words / ≈ 25.2 s (speaker labels excluded, pauses included) |
| Cue targets | `id`, `lost`, `wheel` |

> OMAR: [[cue:id]] Two quick things. Your ID card: wear it where it can be seen. [[pause:0.4]] [[cue:lost]] Lose it, and you email HR — there's a replacement fee. Damage it, and it's replaced free. [[pause:0.4]] [[cue:wheel]] Second, what you can use from day one: health insurance, performance bonuses, development, the hybrid work policy, internal advancement and discounts. Look at the ones you'd actually use.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed; blocks readable in DOM order |
| Not colour-only | Every wheel segment is labelled in text; the ID warning line carries an icon |
| Captions / transcript | `narration_text` present; both images have alt text |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-070",
  "title": "Your ID card and benefits",
  "section": "H · ID, benefits & dress code",
  "node_id": "hr-sH",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "blocks": [
    {
      "html": "<p><strong>Lost card</strong> — email HR. Replacement fee <em>pending B4</em>.</p><p><strong>Damaged card</strong> — replaced free of charge.</p>"
    },
    {
      "asset_id": "<hr-img-idcard>",
      "caption": "A My Clinic staff ID badge on a lanyard."
    },
    {
      "html": "<p><strong>Benefits from day one:</strong> health insurance · annual performance bonuses · employee development · hybrid work policy · internal advancement · discounts.</p>"
    },
    {
      "asset_id": "<hr-img-benefits-wheel>",
      "caption": "Benefits wheel: health insurance, annual performance bonuses, employee development, hybrid work, internal advancement and discounts."
    }
  ],
  "narration_asset_id": "<hr-aud-070>",
  "narration_text": "OMAR: Two quick things. Your ID card: wear it where it can be seen. Lose it, and you email HR — there's a replacement fee. Damage it, and it's replaced free. Second, what you can use from day one: health insurance, performance bonuses, development, the hybrid work policy, internal advancement and discounts. Look at the ones you'd actually use."
}
```

#### 8. Notes for SME and developer

- Open questions: **B4** — confirm the lost-card fee. The card deliberately does **not** state the amount on screen; the amount goes in the Quick Reference and in a replacement note once HR confirms.
- Developer notes: all `blocks` reveal as one unit. The wheel is authored SVG with real text labels, not a flat image, so it reflows and stays accessible.

---

### `hr-071` — What do you wear?

**Status:** `Draft — ready for SME review` · **Section / node:** H · ID, benefits & dress code / `hr-sH` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: apply the dress code that applies to your own role |
| Objective(s) | `hr-o6` |
| On-the-job action | A9 |
| Source | `HR.pptx` slide 58 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | What do you wear? |
| Body / keywords | Six rules, three groups. Place each rule where it applies. |
| Word count (excl. title) | 9 |
| Instruction | Place each rule under Front office, Medical team or Back office. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "H · ID, benefits & dress code · Check", 2 px navy `#003867` header rule |
| Visual concept | Three drop zones in a row, each headed by a small flat figure illustration showing the outfit; six draggable chips sit in a wrap row beneath; a placed chip shows a border and an index number |
| edumints layout | n/a (`drag_drop`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None (flat role-outfit illustrations on drop-zone headers) |
| Animation / reveal | Chips settle with a 120 ms spring when dropped |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-dress-frontoffice` | illustration | Flat figure in a clinic uniform, standing, neutral background | ai-generated | “A front-office colleague in the clinic uniform.” | No |
| `hr-img-dress-medical` | illustration | Flat figure in scrubs and a coat, with a stethoscope | ai-generated | “A clinical colleague in scrubs and a coat.” | No |
| `hr-img-dress-backoffice` | illustration | Flat figure in business attire | ai-generated | “A back-office colleague in business attire.” | No |

**AI image prompt** (`hr-img-dress-frontoffice`, `hr-img-dress-medical`, `hr-img-dress-backoffice` — per `brand-identity.md` §6):

```text
Flat vector illustration for a healthcare e-learning course, 16:9, three standalone full-length character figures on neutral white cards:
- Figure 1 (hr-img-dress-frontoffice): a front-office clinic receptionist in a smart navy (#003867) clinic uniform;
- Figure 2 (hr-img-dress-medical): a clinician in navy (#003867) scrubs and a white clinical coat with a stethoscope;
- Figure 3 (hr-img-dress-backoffice): a back-office staff member in modest formal business attire.
Clean minimalist style, simple geometric shapes, thin navy (#003867) outlines, white and very light blue-grey (#F4F7FA, #C0CED9) surfaces, one highlight colour Caring purple (#652D8C) on badge lanyards, small touches of magenta (#9D3293) only for nothing. Modest, culturally appropriate clothing for Saudi Arabia, closed professional shoes, plain ID badges with no logos or text. Generic staff figures with simple faces; they must not resemble the course companions Noor or Dr. Omar (see companions.md).
No text, no letters, no numbers, no logos, no signage words, no watermarks, no brand names.
```

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Targets | `front` — Front office · `medical` — Medical team · `back` — Back office |
| Items | `it1` “Uniform for every shift” → `front` · `it2` “Scrubs and coat” → `medical` · `it3` “Business attire” → `back` · `it4` “Minimal jewellery” → `medical` · `it5` “Professional shoes” → `medical` · `it6` “No casual days” → `back` |
| Correct answer(s) | As listed. Medical team takes three, back office two, front office one. |
| Accepted variants | n/a (chip placement) |
| Points | 10 |
| Feedback — correct | Right. Front office wears the clinic uniform. The medical team wears scrubs and a coat with professional shoes and minimal jewellery. Back office is business attire, with no casual days. |
| Feedback — incorrect | Not all six. Three of them belong to the medical team, two to back office and one to front office. The one people mix up is “no casual days” — that's the back-office wording; front office says “no casual attire”. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Practical |
| Target seconds | 8 |
| Word count / est. seconds | 20 words / ≈ 8.6 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Six dress-code rules, three groups. Put each one where it applies — and pay attention to the one about casual days.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Pick-and-place: focus a chip, Enter to pick up, arrow to a zone, Enter to drop, Escape to cancel |
| Not colour-only | Each zone has a labelled illustration and a text heading; placement shows an index number |
| Captions / transcript | `narration_text` present; all rule text is real HTML |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "drag_drop",
  "id": "hr-071",
  "title": "What do you wear?",
  "section": "H · ID, benefits & dress code",
  "node_id": "hr-sH",
  "objective_ids": [
    "hr-o6"
  ],
  "points": 10,
  "evidence_screen_ids": [
    "hr-070"
  ],
  "prompt_html": "<p>Six rules, three groups. Place each rule where it applies.</p>",
  "targets": [
    {
      "id": "front",
      "label_html": "Front office"
    },
    {
      "id": "medical",
      "label_html": "Medical team"
    },
    {
      "id": "back",
      "label_html": "Back office"
    }
  ],
  "items": [
    {
      "id": "it1",
      "text_html": "Uniform for every shift",
      "correct_target_id": "front"
    },
    {
      "id": "it2",
      "text_html": "Scrubs and coat",
      "correct_target_id": "medical"
    },
    {
      "id": "it3",
      "text_html": "Business attire",
      "correct_target_id": "back"
    },
    {
      "id": "it4",
      "text_html": "Minimal jewellery",
      "correct_target_id": "medical"
    },
    {
      "id": "it5",
      "text_html": "Professional shoes",
      "correct_target_id": "medical"
    },
    {
      "id": "it6",
      "text_html": "No casual days",
      "correct_target_id": "back"
    }
  ],
  "feedback": {
    "correct_html": "<p>Right. Front office wears the clinic uniform. The medical team wears scrubs and a coat with professional shoes and minimal jewellery. Back office is business attire, with no casual days.</p>",
    "incorrect_html": "<p>Not all six. Three of them belong to the medical team, two to back office and one to front office. The one people mix up is “no casual days” — that's the back-office wording; front office says “no casual attire”.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-071>",
  "narration_text": "OMAR: Six dress-code rules, three groups. Put each one where it applies — and pay attention to the one about casual days."
}
```

#### 8. Notes for SME and developer

- Open questions: None on the rules themselves, but see *Proposed changes* item 2 in the module header — the “no casual days” / “no casual attire” wording is close enough that HR may want to re-word one of them. If HR re-words, only `it6` and the incorrect-feedback string change.
- Developer notes: the three illustrations are decorative-support, not the only cue — each zone also has a text heading.

---

### `hr-080` — If you ever leave

**Status:** `Draft — ready for SME review` · **Section / node:** I · Contracts & leaving / `hr-sI` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: how the contract is accepted, and how to leave well if it ever comes to that |
| Objective(s) | — (teaches `hr-o6`; assessed on `hr-081`) |
| On-the-job action | A10 |
| Source | `HR.pptx` slides 59–60 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | If you ever leave |
| Body / keywords | Accept your contract on Qiwa · Resign in Oracle · Notice: **2 months** both ways · EOS + experience certificate within 15 days |
| Word count (excl. title) | 21 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "I · Contracts & leaving", 2 px navy `#003867` header rule |
| Visual concept | A short horizontal four-step strip — Qiwa, Oracle, two months, 15 days — with an arrow between each; each step carries a one-line caption beneath it and a small line icon above |
| edumints layout | `text` |
| Colours (palette names + hex) | bg `light` (off-white `#F4F7FA` / card surface white `#FFFFFF`) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C`) · warning `accent` (Responsible magenta `#9D3293` on the key rule/figure callout only) |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Four single-weight line icons (`hr-img-exit-icons`: document-signature, screen-and-form, calendar, envelope-with-certificate), navy #003867, own SVG |
| Animation / reveal | Steps fade in left to right in narration order |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-exit-icons` | SVG ×4 | Line icons: document-signature (Qiwa), screen-and-form (Oracle), calendar (notice period), envelope-with-certificate (EOS) | own | Decorative — each step is labelled in text. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm, matter-of-fact |
| Target seconds | 25 |
| Word count / est. seconds | 52 words / ≈ 23.5 s (speaker labels excluded, pauses included) |
| Cue targets | `qiwa`, `oracle`, `notice`, `eos` |

> OMAR: [[cue:qiwa]] Two ends of one story. Starting: you accept your contract on Qiwa, the Ministry of Human Resources platform. [[pause:0.4]] [[cue:oracle]] Leaving: a resignation is a request, so it goes through Oracle. [[pause:0.4]] [[cue:notice]] Notice is two months, and it runs both ways. [[pause:0.4]] [[cue:eos]] End-of-service benefits and your experience certificate follow within fifteen days of your last day.

New lexicon terms: Qiwa — “KEE-wa”; EOS — say “end of service”

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed |
| Not colour-only | Every step is labelled in text; icons support only |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "hr-080",
  "title": "If you ever leave",
  "section": "I · Contracts & leaving",
  "node_id": "hr-sI",
  "objective_ids": [],
  "points": 0,
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Accept your contract</strong> on Qiwa.</p><p><strong>Resign</strong> in Oracle.</p><p><strong>Notice: 2 months</strong>, honoured by both parties.</p><p><strong>EOS + experience certificate</strong> within 15 days of your last working day.</p>",
  "narration_asset_id": "<hr-aud-080>",
  "narration_text": "OMAR: Two ends of one story. Starting: you accept your contract on Qiwa, the Ministry of Human Resources platform. Leaving: a resignation is a request, so it goes through Oracle. Notice is two months, and it runs both ways. End-of-service benefits and your experience certificate follow within fifteen days of your last day.",
  "media_asset_id": "<hr-img-exit-icons>",
  "media_alt": "Four steps: Qiwa contract, Oracle resignation, two months notice, and end-of-service settlement within 15 days."
}
```

#### 8. Notes for SME and developer

- Open questions: None. The four facts are verbatim from slides 59–60.
- Developer notes: four separate `<p>` elements so the reveal is paced per step.

---

### `hr-081` — Three weeks' notice

**Status:** `Draft — ready for SME review` · **Section / node:** I · Contracts & leaving / `hr-sI` · **Type:** `mcq` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: apply the notice rule when the learner's own interests pull the other way |
| Objective(s) | `hr-o6` |
| On-the-job action | A10 |
| Source | `HR.pptx` slide 59 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Three weeks' notice |
| Body / keywords | *(stem only)* |
| Word count (excl. title) | 0 |
| Instruction | Choose one. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "I · Contracts & leaving · Check", 2 px navy `#003867` header rule |
| Visual concept | Stem in large type; four plain option rows; no imagery, so the decision carries the screen |
| edumints layout | n/a (`mcq`) |
| Colours (palette names + hex) | bg `surface` (white `#FFFFFF` cards on off-white `#F4F7FA` stage, `#D9E1E8` border) · stem `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` chip and progress bar) · feedback `success` `#1E7B4F` / `error` `#B42318` with icon + words |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options and feedback Montserrat Regular/Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None |
| Icons | None |
| Animation / reveal | None |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (text-only question).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “You accept a new job starting in 3 weeks. What happens with your notice?” |
| Options | `a` You must serve the contractual 2 months unless My Clinic agrees otherwise; submit the resignation in Oracle ✔ · `b` You can leave in 3 weeks — a new job overrides the notice period · `c` Email your manager; Oracle is only for leave requests · `d` Give one month: notice is shorter for grades A to E |
| Correct answer(s) | `a` |
| Points | 5 |
| Feedback — correct | Right. The notice period is two months and it binds both sides, unless My Clinic agrees to something different. And a resignation is a request, so it goes in through Oracle. |
| Feedback — incorrect | Not that one. The contractual notice is two months, and it binds both sides. You can always ask HR whether they'll agree to less, but you can't assume it. |
| Per-option feedback | `a` — Right. Two months unless otherwise agreed, submitted in Oracle. · `b` — A new job doesn't override the contract. The two months stands unless My Clinic agrees to shorten it. · `c` — Oracle isn't only for leave. Resignation, letters and certificates are all service requests, and they need a record. · `d` — The notice period in your contract isn't set by grade in this policy. Assume two months unless your contract says otherwise. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Calm |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 6.9 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Last scenario. You've accepted a new job starting in three weeks. What happens with your notice?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Native radio group |
| Not colour-only | Result uses a glyph plus words; every option carries its own reason text |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "mcq",
  "id": "hr-081",
  "title": "Three weeks' notice",
  "section": "I · Contracts & leaving",
  "node_id": "hr-sI",
  "objective_ids": [
    "hr-o6"
  ],
  "points": 5,
  "evidence_screen_ids": [
    "hr-080"
  ],
  "prompt_html": "<p>You accept a new job starting in 3 weeks. What happens with your notice?</p>",
  "options": [
    {
      "id": "a",
      "text_html": "You must serve the contractual 2 months unless My Clinic agrees otherwise; submit the resignation in Oracle",
      "correct": true,
      "feedback_html": "<p>Right. The notice period is two months and it binds both sides, unless My Clinic agrees to something different. And a resignation is a request, so it goes in through Oracle.</p>"
    },
    {
      "id": "b",
      "text_html": "You can leave in 3 weeks — a new job overrides the notice period",
      "feedback_html": "<p>A new job doesn't override the contract. The two months stands unless My Clinic agrees to shorten it.</p>"
    },
    {
      "id": "c",
      "text_html": "Email your manager; Oracle is only for leave requests",
      "feedback_html": "<p>Oracle isn't only for leave. Resignation, letters and certificates are all service requests, and they need a record.</p>"
    },
    {
      "id": "d",
      "text_html": "Give one month: notice is shorter for grades A to E",
      "feedback_html": "<p>The notice period in your contract isn't set by grade in this policy. Assume two months unless your contract says otherwise.</p>"
    }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Right. The notice period is two months and it binds both sides, unless My Clinic agrees to something different. And a resignation is a request, so it goes in through Oracle.</p>",
    "incorrect_html": "<p>Not that one. The contractual notice is two months, and it binds both sides. You can always ask HR whether they'll agree to less, but you can't assume it.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-081>",
  "narration_text": "OMAR: Last scenario. You've accepted a new job starting in three weeks. What happens with your notice?"
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: none.

---

### `hr-090` — How you did

**Status:** `Draft — ready for SME review` · **Section / node:** Z · Close / `hr-sZ` · **Type:** `results_breakdown` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close: show results by objective and point the learner at what to revisit |
| Objective(s) | All six (reporting only — this screen is unscored) |
| On-the-job action | — |
| Source | — (derived from phase-1 §3 and phase-4 §3) |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | How you did |
| Body / keywords | One row per objective. Anything below 70% comes with a suggestion. |
| Word count (excl. title) | 11 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close (see `../../00_program/brand/screen-mockups/06-results.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "Your results", 2 px navy `#003867` header rule |
| Visual concept | Six rows, each with the objective name, a thin bar showing the percentage, and the points earned over points available; any row below the threshold expands to show one line of advice beneath it |
| edumints layout | n/a (`results_breakdown`) |
| Colours (palette names + hex) | bg `surface` (off-white `#F4F7FA` stage, white `#FFFFFF` breakdown rows) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` objective bars) · weak objectives flagged with `error` `#B42318` + ⚠ icon + text |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; objective labels and body Montserrat Regular/Medium 400/500, 16 px; badges Montserrat Bold 700, 12–14 px; footer 10–12 px. |
| Watermark | None |
| Icons | Status icons on objective bars (✓ in #1E7B4F for passed, ⚠ in #B42318 for needs review), own SVG |
| Animation / reveal | Rows fade up in sequence; bars grow from zero |
| Companion | None visible — voice only: Dr. Omar (lead host) narrates; no companion art on this screen |

**Imagery:** None (chart is CSS).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Sections | See the table below (one per objective, with the scored screen ids it covers) |
| Correct answer(s) | n/a |
| Points | 0 |
| Threshold | `weak_threshold` 70 (matches the course pass mark) |

| Section title | Screen ids | Available | Advice if weak |
|---|---|---|---|
| Values & strategy | `hr-011`, `hr-013` | 15 | Revisit the four values and the 7C pillars. The one to remember: Care is where My Care and patient loyalty sit. |
| Ethics & patients' rights | `hr-031`, `hr-032`, `hr-033` | 30 | Disclose conflicts early, never trade access to care, and when you're unsure, report within 24 hours. A right is what the patient can expect; a responsibility is what we ask of them. |
| Leave | `hr-042`, `hr-044`, `hr-045` | 35 | Check three things on every request: the type of leave, the eligibility rule, and the document. The tables are in the HR Quick Reference. |
| Pay & social insurance | `hr-052`, `hr-054` | 20 | GOSI is basic plus housing × 9.75%. Overtime is basic ÷ 240, then × 1.5, or × 2 on a public holiday. |
| Systems & licences | `hr-060`, `hr-061`, `hr-062` | 30 | Requests go through Oracle. Contracts on Qiwa, licences on Mumaris, guides on the intranet. Renew your licence well before it expires. |
| ID, dress code & contracts | `hr-071`, `hr-081` | 15 | Front office wears the uniform, the medical team wears scrubs and a coat, back office is business attire. Notice is two months both ways. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR (lead host) |
| Tone | Encouraging |
| Target seconds | 12 |
| Word count / est. seconds | 28 words / ≈ 12.0 s (speaker labels excluded, pauses included) |
| Cue targets | None |

> OMAR: Here's where you landed, objective by objective. Anything under seventy per cent has a note beside it. It's a list of where to look next, not a verdict.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Advice rows are plain text, always in the DOM; no interaction needed |
| Not colour-only | Each row prints the percentage and the points as text; bars are a visual aid |
| Captions / transcript | `narration_text` present; all advice is real HTML |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "results_breakdown",
  "id": "hr-090",
  "title": "How you did",
  "section": "Z · Close",
  "node_id": "hr-sZ",
  "objective_ids": [],
  "points": 0,
  "body_html": "<p>One row per objective. Anything below 70% comes with a suggestion.</p>",
  "weak_threshold": 70,
  "show_total": true,
  "sections": [
    {
      "title": "Values & strategy",
      "screen_ids": [
        "hr-011",
        "hr-013"
      ],
      "advice_html": "<p>Revisit the four values and the 7C pillars. The one to remember: Care is where My Care and patient loyalty sit.</p>"
    },
    {
      "title": "Ethics & patients' rights",
      "screen_ids": [
        "hr-031",
        "hr-032",
        "hr-033"
      ],
      "advice_html": "<p>Disclose conflicts early, never trade access to care, and when you're unsure, report within 24 hours. A right is what the patient can expect; a responsibility is what we ask of them.</p>"
    },
    {
      "title": "Leave",
      "screen_ids": [
        "hr-042",
        "hr-044",
        "hr-045"
      ],
      "advice_html": "<p>Check three things on every request: the type of leave, the eligibility rule, and the document. The tables are in the HR Quick Reference.</p>"
    },
    {
      "title": "Pay & social insurance",
      "screen_ids": [
        "hr-052",
        "hr-054"
      ],
      "advice_html": "<p>GOSI is basic plus housing × 9.75%. Overtime is basic ÷ 240, then × 1.5, or × 2 on a public holiday.</p>"
    },
    {
      "title": "Systems & licences",
      "screen_ids": [
        "hr-060",
        "hr-061",
        "hr-062"
      ],
      "advice_html": "<p>Requests go through Oracle. Contracts on Qiwa, licences on Mumaris, guides on the intranet. Renew your licence well before it expires.</p>"
    },
    {
      "title": "ID, dress code & contracts",
      "screen_ids": [
        "hr-071",
        "hr-081"
      ],
      "advice_html": "<p>Front office wears the uniform, the medical team wears scrubs and a coat, back office is business attire. Notice is two months both ways.</p>"
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-090>",
  "narration_text": "OMAR: Here's where you landed, objective by objective. Anything under seventy per cent has a note beside it. It's a list of where to look next, not a verdict."
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: `screen_ids` must match the built screen ids exactly or the breakdown shows zeros. If `hr-061` is deferred (B8), remove it from this list and lower the objective's available points to 15 in the advice text.

---

### `hr-091` — You're ready

**Status:** `Draft — ready for SME review` · **Section / node:** Z · Close / `hr-sZ` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close: say what the learner can now do, and hand them the two things they need next |
| Objective(s) | — |
| On-the-job action | — |
| Source | `HR.pptx` slides 61–62 (onboarding survey, thanks) |
| Depends on Phase 0 | None (survey URL from HR) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | You're ready |
| Body / keywords | You can now: live the values · raise a concern · answer leave and pay questions · use Oracle, Qiwa and Mumaris · keep your licence valid |
| Word count (excl. title) | 21 |
| Instruction | n/a |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close (see `../../00_program/brand/screen-mockups/06-results.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), breadcrumb "Z · Close", 2 px navy `#003867` header rule |
| Visual concept | A five-item checklist on the left, each with a small tick glyph; under it two side-by-side action cards — one for the HR Quick Reference download, one for the onboarding survey; Dr. Omar's half-body `success` pose (thumbs up) on the right; a single “Next” line along the bottom names module 07, with Noor's small happy avatar beside it because she hosts that module |
| edumints layout | n/a (`summary`) |
| Colours (palette names + hex) | bg `light` (white `#FFFFFF` stage with subtle petal watermark) · headings `primary` (navy `#003867`) · body `dark` (ink `#1F2A37`) · highlight `secondary` (Caring purple `#652D8C` checklist ticks and action cards) · warning none |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; objective labels and body Montserrat Regular/Medium 400/500, 16 px; badges Montserrat Bold 700, 12–14 px; footer 10–12 px. |
| Watermark | Petal watermark (`mark-navy.png` at 7% opacity, 440 px, cropped off the right edge) |
| Icons | Checklist tick icons in Caring purple #652D8C + download/external-link line icons in navy #003867, own SVG |
| Animation / reveal | Checklist ticks in one by one, then the action cards fade up; Noor's avatar fades in with her line |
| Companion | **Omar + Noor** — `char-omar-success` half-body, 300–360 px, right side; `char-noor-avatar-happy` 56 px with a 3 px Caring purple `#652D8C` ring on the “Next” line · placement L6 · tip text n/a · speaks: Omar, then Noor (two-voice close; Noor previews module 07) |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-pdf-quickref` | PDF | Same asset as `hr-040` | own | n/a | n/a |
| `char-omar-success` | illustration | Shared programme companion pose (Canva media `MAHX-llCU5M`): half-body, thumbs up; right side, 300–360 px | ai-generated (programme master, companions.md §3) | “Dr. Omar, a family physician, smiling and giving a thumbs up.” | No |
| `char-noor-avatar-happy` | illustration | Programme avatar cropped from `char-noor-success` (companions.md §3: “to make if needed”), 56 px circle | ai-generated (programme master) | “Noor, the safety liaison, smiling.” | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | Five “you can now” statements (see Body above) |
| Correct answer(s) | n/a |
| Points | 0 |
| Settings | `show_score: true`, `show_completion: true` |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR → NOOR (two-voice screen: parts `omar-1`, `noor-1`; joined into one file with 0.3 s silence) |
| Tone | Warm |
| Target seconds | 26 (v0.1: 25) — per part: `omar-1` 19, `noor-1` 7 |
| Word count / est. seconds | 62 words / ≈ 27.5 s (speaker labels excluded, pauses included) |
| Cue targets | `list`, `pdf`, `survey`, `next` |

> OMAR: [[cue:list]] That's the induction. You can now live the values, raise a concern the right way, answer leave and pay questions, and pick the right system. [[pause:0.3]] [[cue:pdf]] Download the HR Quick Reference. [[pause:0.3]] [[cue:survey]] And please complete the onboarding survey. Two minutes, and it shapes how we run this day.

> NOOR: [[pause:0.3]] [[cue:next]] Next, you'll join me for clinical governance: quality, patient safety and risk. Welcome to My Clinic.

New lexicon terms: Noor — “noor” (rhymes with *tour*); Omar — “OH-mar” (companions.md §5). Other terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Both action cards are native links |
| Not colour-only | Each checklist item is text with a tick glyph; links are underlined |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "summary",
  "id": "hr-091",
  "title": "You're ready",
  "section": "Z · Close",
  "node_id": "hr-sZ",
  "objective_ids": [],
  "points": 0,
  "notes": "Companions: Dr. Omar char-omar-success half-body 300-360 px right side; Noor char-noor-avatar-happy 56 px (3 px #652D8C ring) on the 'Next: module 07' line. Audio: omar-1 + noor-1 joined with 0.3 s silence.",
  "show_score": true,
  "show_completion": true,
  "body_html": "<p><strong>You can now:</strong> live the values · raise a concern the right way · answer leave and pay questions · use Oracle, Qiwa and Mumaris · keep your licence valid.</p><p><strong>Keep this:</strong> <a href=\"{{asset:hr-pdf-quickref}}\">HR Quick Reference (PDF, 2 pages)</a></p><p><strong>Please do:</strong> <a href=\"{{survey_url}}\" target=\"_blank\" rel=\"noopener\">the onboarding survey (2 minutes)</a></p><p><strong>Next:</strong> module 07 — Clinical Governance: Quality, Patient Safety &amp; Risk.</p>",
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<hr-aud-091>",
  "narration_text": "OMAR: That's the induction. You can now live the values, raise a concern the right way, answer leave and pay questions, and pick the right system. Download the HR Quick Reference. And please complete the onboarding survey. Two minutes, and it shapes how we run this day. NOOR: Next, you'll join me for clinical governance: quality, patient safety and risk. Welcome to My Clinic."
}
```

#### 8. Notes for SME and developer

- Open questions: None on content. HR must supply the live onboarding-survey URL before build; until then use `{{survey_url}}` as a placeholder and confirm in preview that the link opens in a new tab.
- Developer notes: place Omar and Noor from the theme/renderer as described in `notes`; join `omar-1` and `noor-1` into `MC03-welcome-on-board_hr-091.mp3` with 0.3 s silence (companions.md §5). `{{asset:hr-pdf-quickref}}` is replaced with the real asset URL after `add_asset`. Test both links in preview **and** in the LMS.

---

## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | Speaker(s) | Companion visible | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `hr-000` | `title_slide` | N | 0 | OMAR + NOOR | Omar + Noor | 0 | 46 | 20 | `Draft` |
| 2 | `hr-001` | `content_slide` | N | 0 | OMAR | Omar | 24 | 85 | 38 | `Draft` |
| 3 | `hr-002` | `poll` | N | 0 | OMAR | Omar | 12 | 23 | 10 | `Draft` |
| 4 | `hr-010` | `tabs` | N | 0 | OMAR | — | 14 | 81 | 37 | `Draft` |
| 5 | `hr-011` | `matching` | Y | 10 | OMAR | — | 12 | 16 | 7 | `Draft` |
| 6 | `hr-012` | `accordion` | N | 0 | OMAR | — | 15 | 99 | 46 | `Draft` |
| 7 | `hr-013` | `mcq` | Y | 5 | OMAR | — | 0 | 16 | 7 | `Draft` |
| 8 | `hr-014` | `content_slide` | N | 0 | OMAR | — | 10 | 44 | 20 | `Draft` |
| 9 | `hr-020` | `timeline` | N | 0 | OMAR | — | 12 | 72 | 32 | `Draft` |
| 10 | `hr-021` | `hotspot` | N | 0 | OMAR | — | 11 | 31 | 13 | `Draft` |
| 11 | `hr-022` | `content_slide` | N | 0 | OMAR | — | 12 | 46 | 21 | `Draft` |
| 12 | `hr-023` | `flashcards` | N | 0 | OMAR | — | 13 | 39 | 17 | `Draft` |
| 13 | `hr-030` | `content_slide` | N | 0 | OMAR | — | 16 | 78 | 35 | `Draft` |
| 14 | `hr-031` | `decision_scenario` | Y | 15 | NOOR | Noor | 7 | 35 | 15 | `Draft` |
| 15 | `hr-032` | `drag_drop` | Y | 10 | OMAR | — | 12 | 19 | 8 | `Draft` |
| 16 | `hr-033` | `mcq` | Y | 5 | OMAR | — | 0 | 20 | 9 | `Draft` |
| 17 | `hr-040` | `content_slide` | N | 0 | OMAR | — | 15 | 63 | 28 | `Draft` |
| 18 | `hr-041` | `accordion` | N | 0 | OMAR | — | 14 | 91 | 42 | `Draft` |
| 19 | `hr-042` | `matching` | Y | 5 | OMAR | — | 13 | 14 | 6 | `Draft` |
| 20 | `hr-043` | `worked_example` | N | 0 | OMAR | Omar | 0 | 95 | 43 | `Draft` |
| 21 | `hr-044` | `decision_scenario` | Y | 15 | NOOR | Noor | 8 | 27 | 12 | `Draft` |
| 22 | `hr-045` | `adaptive_practice` | Y | 15 | OMAR | — | 12 | 25 | 11 | `Draft` |
| 23 | `hr-050` | `content_slide` | N | 0 | OMAR | — | 21 | 62 | 27 | `Draft` |
| 24 | `hr-051` | `worked_example` | N | 0 | OMAR | — | 0 | 65 | 29 | `Draft` |
| 25 | `hr-052` | `fill_blank` | Y | 10 | OMAR | — | 12 | 15 | 6 | `Draft` |
| 26 | `hr-053` | `worked_example` | N | 0 | OMAR | — | 0 | 79 | 36 | `Draft` |
| 27 | `hr-054` | `mcq` | Y | 10 | OMAR | — | 0 | 20 | 9 | `Draft` |
| 28 | `hr-060` | `matching` | Y | 10 | OMAR | — | 10 | 19 | 8 | `Draft` |
| 29 | `hr-061` | `simulation` | Y | 15 | OMAR | Omar | 14 | 49 | 21 | `Draft` |
| 30 | `hr-062` | `true_false` | Y | 5 | OMAR | — | 0 | 19 | 8 | `Draft` |
| 31 | `hr-070` | `content_slide` | N | 0 | OMAR | — | 15 | 57 | 25 | `Draft` |
| 32 | `hr-071` | `drag_drop` | Y | 10 | OMAR | — | 9 | 20 | 9 | `Draft` |
| 33 | `hr-080` | `content_slide` | N | 0 | OMAR | — | 21 | 52 | 24 | `Draft` |
| 34 | `hr-081` | `mcq` | Y | 5 | OMAR | — | 0 | 16 | 7 | `Draft` |
| 35 | `hr-090` | `results_breakdown` | N | 0 | OMAR | — | 11 | 28 | 12 | `Draft` |
| 36 | `hr-091` | `summary` | N | 0 | OMAR + NOOR | Omar + Noor | 21 | 62 | 28 | `Draft` |
| | **Totals** | | **15** | **145** | Omar 35 lines · Noor 4 lines | 8 of 36 screens | **366** | **1628** | **722 ≈ 12 min 2 s** | |

Narration words exclude the `OMAR:` / `NOOR:` labels; estimated seconds are words ÷ 140 wpm plus scripted pauses, including the `hr-061` tip line. `lint_narration_script` counts each label as a word, so its total is slightly higher (see [`lint-report.json`](lint-report.json)).

### Asset list (all screens)

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `hr-img-hero` | photo | not placed in v0.2 (was `hr-001`; Omar's pose took the right column) | own (consent pending **B6 / D5**) | Yes | optional — HR decision |
| `hr-img-values-icons` | SVG ×4 | `hr-010` | own (redrawn from slide 10 icon family) | n/a — decorative | to produce |
| `hr-img-7c-icons` | SVG ×7 | `hr-012` | own (redrawn from slide 10) | n/a — decorative | to produce |
| `hr-img-serve-icons` | SVG ×3 | `hr-014` | own | n/a — decorative | to produce |
| `hr-img-map` | SVG | `hr-021` | own | Yes | to produce |
| `hr-img-leaders` | photos ×4 | `hr-022` | local (consent on file — **B6**) | Yes | blocked on B6 |
| `hr-img-award-icons` | SVG ×2 | `hr-023` | own (redrawn from slides 17–18) | n/a — decorative | to produce |
| `hr-img-ethics-icons` | SVG ×4 | `hr-030` | own | n/a — decorative | to produce |
| `hr-img-ethics-meeting / -corridor / -desk` | illustrations ×3 | `hr-031` | ai-generated | Yes | to produce |
| `hr-img-help-icons` | SVG ×3 | `hr-040` | own | n/a — decorative | to produce |
| `hr-img-leavedesk` | illustration | `hr-044` | ai-generated | Yes | to produce |
| `hr-img-gosi-bar` | SVG | `hr-050` | own (authored) | Yes | to produce |
| `hr-img-oracle-1 … -5` | screenshots ×5 | `hr-061` | own (test account — **B8**) | Yes | blocked on B8 |
| `hr-img-idcard` | illustration | `hr-070` | ai-generated | Yes | to produce |
| `hr-img-benefits-wheel` | SVG | `hr-070` | own (authored) | Yes | to produce |
| `hr-img-dress-frontoffice / -medical / -backoffice` | illustrations ×3 | `hr-071` | ai-generated | Yes | to produce |
| `hr-img-exit-icons` | SVG ×4 | `hr-080` | own | n/a — decorative | to produce |
| `hr-pdf-quickref` | PDF | `hr-040`, `hr-091` | own (written by HR) | n/a — linked resource | to produce |
| `char-omar-welcome`, `-explaining`, `-listening`, `-thinking`, `-success`, `-avatar-neutral` | companion poses (shared programme set) | `hr-000`, `hr-001`, `hr-002`, `hr-043`, `hr-091`, `hr-061` | ai-generated programme masters — [`companions.md`](../../00_program/characters/companions.md) §3 (Canva media ids listed there) | Yes | generated; in `00_program/characters/assets/` (imported 2026-10-15) to `00_program/characters/assets/` |
| `char-noor-welcome`, `-avatar-neutral` | companion poses (shared programme set) | `hr-000`, `hr-031`, `hr-044` | ai-generated programme masters — companions.md §3 | Yes | generated; in `00_program/characters/assets/` (imported 2026-10-15) |
| `char-noor-avatar-happy`, `char-noor-avatar-concern` | companion avatars (shared programme set) | `hr-031`, `hr-091` | crop from `char-noor-success` / `char-noor-concern` (companions.md §3 “to make if needed”) | Yes | to make (programme asset, not module art) |
| `hr-aud-000 … hr-aud-091` | audio ×36 screen files (+1 feedback clip `hr-061` tip) from 39 recorded lines: Dr. Omar 35, Noor 4 | all narrated screens | two fixed companion voices, provider pending program **D10** | transcript = `narration_text` | to produce (v0.1 single-voice reference clips are superseded) |

### Open questions for the SME

| # | Screen id | Question | Phase 0 id | Blocks build? |
|---|---|---|---|---|
| 1 | `hr-000` | Does HR want the real CEO welcome video here instead of a still (phase-3 §1, program D10)? If yes, this becomes a `video` screen and the narration moves to the video transcript. | D10 | No |
| 2 | `hr-020` | **B5 / D3** — J3 and J4 branch names. The card deliberately shows the codes (J3, J4) and marks the names pending, because the codes are what staff use daily and both slides agree on them. | B5, D3 | No |
| 3 | `hr-021` | **B5 / D3** (J3, J4 names) · **B6 / D5** (branch photos — the plan allows photos inside the pin cards once rights and consents are confirmed; without them the cards are text-only, which is the default build). | B5, B6, D3, D5 | No |
| 4 | `hr-022` | **B6 / D5** — consent for the four portraits and names. Until it closes, ship the monogram-tile fallback and delete the name strings from the captions. | B6, D5 | No |
| 5 | `hr-023` | **B7** — the exact awarding body, year and wording for all five cards, and the JCI claim read from slide 18. The JCI claim is **excluded** from this card set until Comms confirms it in writing. | B7 | No |
| 6 | `hr-030` | **B14 / D8** — the 24-hour window must match the wording used in module 07. Until it closes, the strip carries an inline `<em>Pending B14 / D8.</em>` note. | B14, D8 | No |
| 7 | `hr-031` | **B14 / D8** — the 24-hour window appears in `n3b` and in the closing feedback. It must match module 07. | B14, D8 | No |
| 8 | `hr-040` | **B6 / D5** — the deck names individual HR staff and personal mailboxes (slide 30). The card ships with role mailboxes only. Swap the placeholder text once HR and the DPO close B6. | B6, D5 | No |
| 9 | `hr-041` | **B1** (sick-leave pay bands 31–90), **B2** (compassionate-leave wording for the death of a husband), **B9** (current-year carry-over), **B10** (scientific-leave wording on slide 40, which looks copied from the exam-leave slide), **B11** (Hajj leave service requirement). | B1, B10, B11, B2, B9 | No |
| 10 | `hr-042` | **B9** — confirm the entitlement table for the current year. If it changes, four strings change and nothing else. | B9 | No |
| 11 | `hr-043` | **B1** — the slide says “days 31–90: 25% deducted”. HR must confirm whether that means 75% of salary for days 31–90. The step text says exactly what the slide says and marks it pending; the narration deliberately does not state a percentage. | B1 | No |
| 12 | `hr-044` | **B10** — slide 40's sentence about academic exams looks copied from the exam-leave slide. If HR confirms a different purpose for scientific leave, re-word `n1` and its feedback. **B11** — confirm the two-year service rule and the 10–15 day range for Hajj leave. | B10, B11 | No |
| 13 | `hr-045` | **B9** — confirm `q1` and `q2` for the current year. **B2** — `q7`, `q8` and `q9` rest on the compassionate-leave table; confirm the day counts and the death-of-a-husband wording. | B2, B9 | No |
| 14 | `hr-050` | **B12** — confirm the 9.75 / 11.75 / 21.5 rates against current GOSI rates for new joiners. If they change, three numbers change here, on `hr-051`, on `hr-052`, and in the Quick Reference PDF. | B12 | No |
| 15 | `hr-051` | **B12** — rates. | B12 | No |
| 16 | `hr-052` | **B12** — if the rate changes, `hr-050`, `hr-051`, this screen's accepted answers and feedback, and the Quick Reference all change together. | B12 | No |
| 17 | `hr-053` | **B3** — the slide says overtime “depends on grade” but gives one formula. Until HR confirms, the card states the caveat in the intro and in the narration, and does not claim that every grade is eligible. | B3 | No |
| 18 | `hr-054` | **B3** — if HR confirms that eligibility grades differ, add the caveat to the stem rather than changing the arithmetic. | B3 | No |
| 19 | `hr-061` | **B8** — every screenshot must come from a test account with no real employee data. Until HRIS supplies them, this screen cannot be built; ship the module without it and add it in a minor version, or replace it with a five-step `sorting` screen (a plan change, because the points and the objective evidence both move). | B8 | Yes |
| 20 | `hr-062` | **B13** — confirm the 30-day suspension rule with HR. If it changes, the statement, both feedback strings and the Quick Reference change together. | B13 | No |
| 21 | `hr-070` | **B4** — confirm the lost-card fee. The card deliberately does **not** state the amount on screen; the amount goes in the Quick Reference and in a replacement note once HR confirms. | B4 | No |
| | *all other cards* | No open question recorded — the card's **Notes** section says “None”. | — | No |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| CBAHI | “see-bah-hee” | `hr-023` |
| Noor | “noor” (rhymes with *tour*) | `hr-000`, `hr-091` (and every `NOOR:` line label) |
| Omar | “OH-mar” | `hr-000` (and every `OMAR:` line label) |
| CEO | “C-E-O” | `hr-022` |
| CFO | “C-F-O” | `hr-022` |
| CMO | “C-M-O” | `hr-022` |
| COO | “C-O-O” | `hr-022` |
| D1 | “D-one” | `hr-021` |
| EOS | say “end of service” | `hr-080` |
| Eid | “eed” | `hr-041`, `hr-045` |
| GOSI | “GO-see” | `hr-044`, `hr-050` |
| HRMS | “H-R-M-S” | `hr-040` |
| Hajj | “hajj” | `hr-041` |
| IELTS | “eye-elts” | `hr-041`, `hr-044` |
| J1 | “J-one” | `hr-000`, `hr-021` |
| J2 | “J-two” | `hr-000`, `hr-021` |
| J3 | “J-three” | `hr-021` |
| J4 | “J-four” | `hr-021` |
| MCJ1 | “M-C-J-one” | `hr-020` |
| MCJ2 | “M-C-J-two” | `hr-020` |
| Mumaris | “mu-MAH-ris” | `hr-060`, `hr-062` |
| My Care | “my care” | `hr-012` |
| Oracle | “OR-uh-kul” | `hr-040`, `hr-061` |
| PRC | “P-R-C” | `hr-020`, `hr-021` |
| Qiwa | “KEE-wa” | `hr-060`, `hr-080` |
| R1 | “R-one” | `hr-021` |
| SAR | say “Saudi riyals” | `hr-051` |
| SCFHS | “S-C-F-H-S” | `hr-060`, `hr-062` |
| TOEFL | “toe-full” | `hr-041`, `hr-044` |

### Self-check

- [x] Every Phase 2 screen has a card, same ids and order (36 of 36)
- [x] Scored screens and total points match Phase 4 (15 scored, 145 points)
- [x] Narration total within ±15% of the Phase 3 estimate (722 s vs 780 s → 93%)
- [x] Every spoken line is prefixed `OMAR:` or `NOOR:`; Dr. Omar narrates every screen except the two Phase 3 Noor screens (`hr-031`, `hr-044`) and Noor's turns on `hr-000` and `hr-091`
- [x] Companions visible only on the 8 screens in the Phase 3 companion table (8 of 36, under one in three); never over a question — `hr-031`/`hr-044` use the L5 scenario avatar, `hr-061` shows Omar only with the end-of-simulation feedback
- [x] Two-voice screens (`hr-000`, `hr-091`) have 2 turns each and stay under 45 s; Omar's first-week story is used once, on `hr-001`; no other honest story is used in this module
- [x] Tip card (`hr-061`, 15 words) differs from the spoken tip line; shared `char-noor-*` / `char-omar-*` assets only — no module-specific character art or character AI prompts
- [x] `review-checklist.md` run on every card (including section H, brand, and section I, companions in narration)
- [x] No `<angle bracket>` guidance text left (only `<hr-…>` asset placeholders remain)
- [x] Every JSON block parses and validates against `core/project.py` models (36 of 36) and states `id`, `type`, `node_id`, `points` and `objective_ids`
- [x] `node_id`, `objective_ids` and `evidence_screen_ids` resolve; no dangling references
- [x] Hotspot and simulation regions use `rect`/`circle` with the right coordinate arity
- [x] No two adjacent screens share a type (stronger than the Phase 2 “no three in a row” rule)
- [x] Longest unscored run: 6 screens, `hr-014`→`hr-030`. Two of them need learner action (`hr-021` explore-all, `hr-023` flip), so the passive stretch is `hr-014` + `hr-020` + `hr-022` + `hr-030`. **Watch item for `lint_visual_plan`:** if it raises `passive_stretch`, apply the Phase 2 mitigation — move the `hr-030` ethics summary into the `intro_html` of `hr-031` and drop `hr-030` (a plan change). **v0.2 result:** `lint_visual_plan` raises no `passive_stretch` (0 errors, 0 warnings — [`lint-report.json`](lint-report.json)), so no plan change is needed.

**Carried forward to the next phase**

- Every `⚠ PENDING` marker resolves to a Phase 0 item id and is listed above.
- `hr-061` cannot be built until **B8** supplies test-account Oracle screenshots.
- Shipping audio waits for program **D10** (Noor and Dr. Omar voices) and the 30-second voice samples; the v0.1 clips in `audio/` are single-voice reference reads only.
- The `HR Quick Reference` PDF (`hr-pdf-quickref`) does not exist yet; HR writes it from confirmed policy.
