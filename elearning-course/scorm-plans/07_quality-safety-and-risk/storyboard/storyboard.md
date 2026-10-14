# Storyboard — 07 Clinical Governance: Quality, Patient Safety & Risk

![My Clinic logo](../../00_program/brand/logo-preview.png)

> Screen-by-screen storyboard for the 22 core screens in [`../phase-2-storyboard.md`](../phase-2-storyboard.md), in the same order and with the same ids. `qsr-060` is explicitly optional in Phase 2 and is deferred from the 22-screen / 95-point baseline; it remains an optional post-approval change, not a core screen.
> Written against [`../../00_program/storyboard-template/README.md`](../../00_program/storyboard-template/README.md), `brand-identity.md` and the character bible `companions.md`.

> **Review pack v0.2 · 2026-10-14.** v0.2 keeps the 22 hand-written v0.1 cards, ids, order, types,
> node ids and the 11 scored screens / 95 points unchanged, and adds the programme companions
> (Noor as lead host, Dr. Omar as co-host) exactly as the Phase 2 and Phase 3 companion tables place
> them, speaker-tagged narration, and the pack files below. It is a review artefact, **not an approved
> policy or production SCORM package**; every `⚠ PENDING` item stays open.

**Companion documents:** [`screen-visuals.html`](screen-visuals.html) ·
[`visual-plan.json`](visual-plan.json) · [`narration-script.json`](narration-script.json) ·
[`audio-script-export.json`](audio-script-export.json) · [`voice_talent.md`](voice_talent.md) ·
[`asset-register.md`](asset-register.md) · [`lint-report.json`](lint-report.json) ·
character bible [`companions.md`](../../00_program/characters/companions.md).

---

## A. Module header

| Field | Value |
|---|---|
| Module | 07 — My Clinic — Clinical Governance: Quality, Patient Safety & Risk |
| Module prefix | `qsr-` |
| Storyboard version | `v0.2` |
| Author | Arena agent, prepared for Quality / Risk / L&D review; v0.2 companion and pack pass |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review` (content depending on open Phase 0 decisions is explicitly pending) |
| SME reviewer (role) | Quality Director (SME lead); Patient Safety Officer / Risk Manager; Infection Control lead; Nursing Director; L&D human-listen reviewer |
| Audience | All clinical staff; recommended for all staff |
| Seat-time budget | ~25 minutes |
| SCORM / completion / pass mark | SCORM 1.2 · `viewed_all_and_passed` · passing score **80%** (76/95 points) |
| Scored screens / total points | 11 / 95 |
| Source file | `elearning-course/md/07_video-quality-safety-and-risk-orientation.md` (working transcript; 107 source frames in `elearning-course/media/07_quality-safety-risk/`) |
| Brand | My Clinic — [`00_program/brand/brand-identity.md`](../../00_program/brand/brand-identity.md) (read 2026-10-14) |
| Module colour | Caring purple `#652D8C` |
| Theme | `brand_to_theme(00_program/brand/brand-kit.json)` + `style-minimal`; module colour `#652D8C` as `secondary` |
| Phase 0 items still open | B1–B11; cross-module D7, D8, D9 and D10; new poll privacy item `NEW-01` |

### Objectives covered

| Objective id | Objective | Assessed by (screen ids) |
|---|---|---|
| `qsr-o1` | Classify quality measures as structure, process or outcome and order the FOCUS-PDCA cycle. | `qsr-011`, `qsr-012` |
| `qsr-o2` | Apply the six International Patient Safety Goals, including the two-identifier rule. | `qsr-021`, `qsr-022`, `qsr-023` |
| `qsr-o3` | Score a risk on the 5×5 matrix and choose an appropriate response. | `qsr-030`, `qsr-032`, `qsr-033` |
| `qsr-o4` | Distinguish critical incidents, adverse events and near misses within a just culture. | `qsr-041`, `qsr-042` |
| `qsr-o5` | Report an incident through the correct channel within 24 hours. | `qsr-051` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `qsr-sA` | A · Welcome | `qsr-000`–`qsr-002` |
| `qsr-sB` | B · The quality standard | `qsr-010`–`qsr-012` |
| `qsr-sC` | C · Patient safety goals | `qsr-020`–`qsr-023` |
| `qsr-sD` | D · Risk management | `qsr-030`–`qsr-033` |
| `qsr-sE` | E · Incidents | `qsr-040`–`qsr-042` |
| `qsr-sF` | F · Reporting | `qsr-050`–`qsr-051` |
| `qsr-sG` | G · Close | `qsr-090`–`qsr-092` |

### Companions in this module

Lead host **Noor** (senior staff nurse and patient-safety liaison) narrates every narrated screen; co-host
**Dr. Omar** (family physician) speaks only where he is visible. Art is the shared programme set
`char-noor-*` / `char-omar-*` ([`companions.md`](../../00_program/characters/companions.md) §3) — there is
no module-specific character art and no module character prompt.

| Screen | Visible | Pose / asset | Placement | Speaks |
|---|---|---|---|---|
| `qsr-000` | Noor | `char-noor-welcome` | L1 portrait card, bottom-right | Noor — welcome |
| `qsr-002` | Noor | `char-noor-listening` | L4 beside the poll (never over the options) | Noor — speak-up story |
| `qsr-021` | Noor | `char-noor-avatar-concern → -happy / -concern` | L5 scenario avatar | Noor — “Which Mohammed?” story |
| `qsr-031` | Dr. Omar | `char-omar-thinking` | L3 right column | Omar — risk-matrix worked example |
| `qsr-040` | Dr. Omar | `char-omar-avatar-neutral` + tip card | L3 tip card, bottom-left | Omar — iceberg and near-miss tip |
| `qsr-051` | Noor | `char-noor-avatar-neutral → -happy / -concern` | L5 scenario avatar | Noor — end-of-shift scenario |
| `qsr-092` | Noor + Dr. Omar | `char-noor-success` + `char-omar-avatar-happy` | L6 | Noor then Omar — two-voice close |

Visible on 7 of 22 screens (≈ 1 in 3). No companion appears on a scored question screen; on the
unscored `qsr-002` poll Noor stands beside the options as Phase 3 places her.

### Version history

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-10-14 | 22 hand-written cards; a module-only mentor character with its own AI prompts. |
| `v0.2` | 2026-10-14 | Shared companions applied per Phase 2/3; module character art and prompts removed; narration tagged `NOOR:` / `OMAR:` with Noor's two honest stories on `qsr-002` and `qsr-021`; Dr. Omar on `qsr-031`, `qsr-040`, `qsr-092`; pack files and native SVG diagrams added. |

### Shared build conventions

| Convention | Value |
|---|---|
| `section` / `node_id` | Use the exact section text and node id in the card and JSON. |
| Logo | Supplied PNG only, navy on light and white on navy; one per screen; size/position in each card. |
| Palette | Navy #003867 + module Caring purple #652D8C; magenta #9D3293 only for warnings/key numbers; feedback green/red always includes icon and words. |
| Typography | Montserrat per brand identity §3; no text below 14 px except footer/captions/compact label roles. |
| Watermark | Title, section opener and close only; never behind questions or body text. |
| Pending facts | No unresolved policy value is to be treated as approved; retain `⚠ PENDING B# / decision ID` until the owning SME closes it. |
| Narration | 140 wpm target; sentences ≤25 words; question screens are set-up only. Every spoken line starts `NOOR:` or `OMAR:` (Phase 3 Speaker column); `narration_text` is the script without markup, keeping the speaker names (“Noor: …”). |
| Audio placeholder | IDs use the pattern `qsr-aud-###`, one file per screen. The two-voice `qsr-092` is recorded as `noor-1` + `omar-1` and joined with 0.3 s silence (companions.md §5). Provider and voice ids remain pending D10. |
| Evidence links | Every scored screen sets `evidence_screen_ids` to a teaching screen, not itself. |
| Assessment density | 11 fixed scored screens across 5 objectives are intentional in this 25-minute compliance course; each question is explicitly objective-mapped, and repeated practice covers distinct skills rather than drawing from an exam pool. |
| Fictional data | Scenario names, record numbers and incident details are fictional training data only. |

### Proposed changes

No changes to the 22 core Phase 2 screens, their order, scored-screen count or Phase 4 points. The optional `qsr-060` director video remains deferred: D7 recommends not reusing the watermarked source, and Phase 4’s 22-screen / 95-point baseline does not include it. Add a new optional screen only after approval and a Phase 2/4 count update.

---

## B. Screen cards


### `qsr-000` — Clinical governance

**Status:** `Draft — ready for SME review` · **Section / node:** A · Welcome / `qsr-sA` · **Type:** `title_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Open: orient new clinical staff to the purpose of this module and its patient-safety focus. |
| Objective(s) | — |
| On-the-job action | — |
| Source | `elearning-course/md/07_video-quality-safety-and-risk-orientation.md`, source-video opening at 00:00 (title and welcome; narration wording remains subject to B1). |
| Depends on Phase 0 | None for the title; the spoken welcome is a new script, not a source quotation. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Clinical governance |
| Body / keywords | Subtitle: Quality, patient safety and risk · Module 07 · Caring |
| Word count (excl. title) | 9 |
| Instruction | n/a (title screen). |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L1 Title (see `../../00_program/brand/screen-mockups/01-title.png`) |
| Logo | `logo-horizontal-white.png`, 48 px tall, top-left (48 px from left, 40 px from top) |
| Visual concept | Official navy title gradient with the supplied white logo at upper left, a Caring-purple module chip and the title block on the left; Noor (`char-noor-welcome`) waves from a white rounded portrait card at bottom-right, with the large white petal watermark cropped behind it at the right edge; no photo and no generated logo. |
| edumints layout | n/a (`title_slide`) |
| Colours (palette names + hex) | bg navy gradient `#003867 → #3B6A97` · title white `#FFFFFF` · subtitle mist `#C0CED9` · module chip Caring purple `#652D8C` · no warning colour. |
| Typography (Montserrat) | Course title Montserrat Bold 700, 40 px; subtitle Montserrat Regular 400, 18–20 px; module chip Montserrat Bold 700, 12–14 px; footer 10–12 px. |
| Watermark | Supplied `mark-white.png`, 8–10% opacity, 520 px, cropped off the right edge. |
| Icons | None; only the supplied five-petal watermark. |
| Animation / reveal | Title fades up, followed by subtitle; no timed reveal is required for completion. |
| Companion | Noor · pose `char-noor-welcome` · placement L1: half-body in a white rounded portrait card (16 px radius, 4 px Caring-purple `#652D8C` top edge, “Noor · Senior staff nurse & patient-safety liaison” under the image), about 190 × 300 px, bottom-right · tip text n/a |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `brand-background-title-navy` | background | Supplied `00_program/brand/assets/background-title-navy.png`, official 16:9 navy title background. | own (official My Clinic brand asset) | Decorative navy gradient background. | Yes |
| `brand-logo-horizontal-white` | image | Supplied white logo lock-up, unchanged, 48 px tall at top-left. | own (official My Clinic brand asset) | My Clinic logo. | No |
| `brand-mark-white` | icon | Supplied white five-petal mark, 8–10% opacity, 520 px, cropped off right edge. | own (official My Clinic brand asset) | Decorative white petal watermark. | Yes |
| `char-noor-welcome` | character | Shared programme companion pose (preview: `00_program/characters/previews/char-noor-welcome.jpg`); half-body in a 190 × 300 px white portrait card, bottom-right. | ai-generated programme asset, Canva media `MAHX-pFaNMU`, made from the approved master (companions.md §3); no module prompt | Noor, the safety liaison, smiling and waving in welcome. | No |

#### 4. Interaction and scoring

n/a — title screen; no interaction and no score.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Warm, steady |
| Target seconds | 12 |
| Word count / est. seconds | 30 spoken words / ≈ 12.9 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Hello, I'm Noor, a senior nurse and patient-safety liaison. Welcome to clinical governance: how My Clinic protects patients every day. You'll link daily decisions to quality, safety, risk and reporting.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | No interaction; Continue is the player’s native keyboard-accessible control. |
| Not colour-only | Title, subtitle and module name are real HTML text; the mark is decorative only. |
| Captions / transcript | `narration_text` is present; no video. |
| Timing | Untimed; no auto-advance. |

#### 7. Build fields (edumints)

```json
{
  "type": "title_slide",
  "id": "qsr-000",
  "title": "Clinical governance",
  "subtitle": "Quality, patient safety and risk",
  "section": "A · Welcome",
  "node_id": "qsr-sA",
  "objective_ids": [],
  "points": 0,
  "background_asset_id": "<brand-background-title-navy>",
  "body_html": "<p class=\"course-chip\">MODULE 07 · CARING</p>",
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-000>",
  "notes": "Companion: Noor, char-noor-welcome, L1 portrait card bottom-right (alt: Noor, the safety liaison, smiling and waving in welcome.). Speaker: Noor.",
  "narration_text": "Noor: Hello, I'm Noor, a senior nurse and patient-safety liaison. Welcome to clinical governance: how My Clinic protects patients every day. You'll link daily decisions to quality, safety, risk and reporting."
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: Use the three supplied brand files as supplied. Do not place the course logo in an image model prompt; the optional source video is not used.


### `qsr-001` — The quality standard

**Status:** `Draft — ready for SME review` · **Section / node:** A · Welcome / `qsr-sA` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: introduce the expected quality standard before the learner practises how quality is measured. |
| Objective(s) | — (supports `qsr-o1`). |
| On-the-job action | A3 — describe how quality is measured and improved. |
| Source | Source video, 00:40 (quote card); the line is visible in the source frame but its exact quotation is ⚠ PENDING B1 (human listen). |
| Depends on Phase 0 | B1 (quote validation). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | The quality standard |
| Body / keywords | SECTION 1 OF 7 · “Doing the right things right — the first time, and every time.” ⚠ PENDING B1 |
| Word count (excl. title) | 17 |
| Instruction | n/a (section opener). |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L2 Section opener (see `../../00_program/brand/screen-mockups/02-section-opener.png`) |
| Logo | `logo-horizontal-navy.png`, 26 px tall, bottom-left (40 px from left, 28 px from bottom) |
| Visual concept | White section-opener stage with a 200 px official Caring value tile at left, “SECTION 1 OF 7” in small ambitious-dark text, the large navy headline and source quote in HTML, and a faint petal watermark cropped at the right. |
| edumints layout | `full_media` (`content_slide` section opener). |
| Colours (palette names + hex) | bg white `#FFFFFF` · title navy `#003867` · quote ink `#1F2A37` · section marker ambitious-dark `#006E78` (small label only) · Caring tile purple `#652D8C` with white icon · no warning accent beyond the pending marker in the draft. |
| Typography (Montserrat) | Section title Montserrat Bold 700, 40 px; section marker Montserrat Bold 700, 11–14 px; keywords/body Montserrat Regular 400, 16 px; footer 10–12 px. |
| Watermark | Supplied `mark-navy.png`, 6–8% opacity, 440 px, cropped off the right edge. |
| Icons | Supplied Caring value tile with its white line icon; tile is decorative and the word “Caring” is real text. |
| Animation / reveal | Quote fades in after the section marker; reduced-motion mode uses no movement. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `brand-value-tile-caring-purple` | image | Supplied `value-tile-caring-purple.png`, official square tile with white line icon; word “Caring” remains HTML text. | own (official My Clinic brand asset) | Decorative Caring value tile with white line icon. | Yes |
| `brand-mark-navy` | icon | Supplied five-petal watermark at 6–8% opacity, 440 px, cropped off right edge. | own (official My Clinic brand asset) | Decorative petal watermark. | Yes |

#### 4. Interaction and scoring

n/a — unscored section opener.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Calm, confident |
| Target seconds | 25 |
| Word count / est. seconds | 60 spoken words / ≈ 25.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Clinical governance connects the way a service is organised with the way care is delivered and the results patients experience. It asks teams to use reliable information, learn from problems and improve practice over time. Keep one question in mind: what helps the next patient receive safe, consistent care? The standard is a daily way of working, not a slogan.

New lexicon terms: None. The source quotation remains pending B1.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | No interaction; text is read in title → quote → footer order. |
| Not colour-only | The Caring tile is decorative; words carry the standard and the value name. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed; no auto-advance. |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "qsr-001",
  "title": "The quality standard",
  "section": "A · Welcome",
  "node_id": "qsr-sA",
  "objective_ids": [],
  "points": 0,
  "body_html": "<p class=\"section-marker\">SECTION 1 OF 7</p><blockquote>“Doing the right things right — the first time, and every time.” <strong>⚠ PENDING B1</strong></blockquote>",
  "media_asset_id": "<brand-value-tile-caring-purple>",
  "media_alt": "Decorative Caring value tile with a white line icon; the value name is text.",
  "layout": "full_media",
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-001>",
  "narration_text": "Noor: Clinical governance connects the way a service is organised with the way care is delivered and the results patients experience. It asks teams to use reliable information, learn from problems and improve practice over time. Keep one question in mind: what helps the next patient receive safe, consistent care? The standard is a daily way of working, not a slogan."
}
```

#### 8. Notes for SME and developer

- Open questions: B1: L&D and Quality must listen to the source and confirm the quotation before release; do not present the current quote as approved until then.
- Developer notes: Keep the quote as HTML text. Use the official Caring tile and watermark; no quote text is baked into an image.


### `qsr-002` — Speak up safely

**Status:** `Draft — ready for SME review` · **Section / node:** A · Welcome / `qsr-sA` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Reflect: make speaking up a normal topic without assessing or reporting the learner’s response. |
| Objective(s) | — (supports `qsr-o5`). |
| On-the-job action | A6 — report within the approved time and channel. |
| Source | Source-video closing theme at 08:35; reflection question from Phase 1 pedagogy and Phase 2 screen list. |
| Depends on Phase 0 | New open question `NEW-01` / D9: verify anonymous/non-persistent poll handling in the player and selected LMS before asking this question. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Speak up safely |
| Body / keywords | Have you ever noticed something unsafe at work and not said anything? · Anonymous response handling ⚠ PENDING NEW-01 |
| Word count (excl. title) | 17 |
| Instruction | Choose Yes, No or Not sure; you may continue without answering. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Three white response cards sit below a short reflection question in the left two-thirds; Noor (`char-noor-listening`, holding a tablet) stands in the right column beside the cards while she tells her speak-up story; an optional private reflection note appears after submission, with no score or progress penalty. |
| edumints layout | n/a (`poll`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | None; text-only choices keep attention on the reflection. |
| Animation / reveal | Cards fade up together; no timed movement. |
| Companion | Noor · pose `char-noor-listening` · placement L4: half-body about 300 px tall in the right column beside the poll, never over the response cards (unscored reflection, so there is no answer to give away) · tip text n/a |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `char-noor-listening` | character | Shared programme companion pose (preview: `00_program/characters/previews/char-noor-listening.jpg`); half-body about 300 px tall, right column beside the poll. | ai-generated programme asset, Canva media `MAHX-v3i0kY`, made from the approved master (companions.md §3); no module prompt | Noor, the safety liaison, holding a tablet and listening. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Options | `yes` Yes · `no` No · `unsure` Not sure |
| Correct answer(s) | n/a — reflection poll, unscored |
| Points | 0 |
| Reflection | “This reflection is not scored. Continue to the practice screens.” |
| Data handling | ⚠ PENDING NEW-01 / D9: do not enable until response storage and anonymity are verified. Free text is disabled.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Warm, honest, non-judgemental |
| Target seconds | 10 |
| Word count / est. seconds | 24 spoken words / ≈ 10.3 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Most of us have stayed quiet about something unsafe at least once. I have. Speaking up gets easier every time. Answer honestly, or pass.

Companion note: Noor's speak-up story (companions.md §1) is used once, here, before the unscored poll.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Native radio controls; Tab and arrow keys select; a labelled Continue control works without a mouse. |
| Not colour-only | Selection uses a radio indicator, border and text state, not purple alone. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed; answering is optional and must not block completion. |

#### 7. Build fields (edumints)

```json
{
  "type": "poll",
  "id": "qsr-002",
  "title": "Speak up safely",
  "section": "A · Welcome",
  "node_id": "qsr-sA",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>Have you ever noticed something unsafe at work and not said anything?</p><p><strong>Anonymous response handling ⚠ PENDING NEW-01</strong></p>",
  "options": [
    {
      "id": "yes",
      "text_html": "Yes"
    },
    {
      "id": "no",
      "text_html": "No"
    },
    {
      "id": "unsure",
      "text_html": "Not sure"
    }
  ],
  "multi": false,
  "allow_text": false,
  "reflection_html": "<p>This reflection is not scored. Continue to the practice screens.</p>",
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-002>",
  "notes": "Companion: Noor, char-noor-listening, right column beside the poll, never over the options (alt: Noor, the safety liaison, holding a tablet and listening.). Speaker: Noor.",
  "narration_text": "Noor: Most of us have stayed quiet about something unsafe at least once. I have. Speaking up gets easier every time. Answer honestly, or pass."
}
```

#### 8. Notes for SME and developer

- Open questions: NEW-01 / D9: verify the poll does not expose a response to managers or attach a named response to the learner record. If the tool cannot guarantee the intended privacy, replace the poll with a non-collecting reflection before production.
- Developer notes: The current Screen model has no explicit `anonymous` field. Keep the card blocked until the privacy/storage behaviour is confirmed; do not collect names or incident details.


### `qsr-010` — How quality is measured

**Status:** `Draft — ready for SME review` · **Section / node:** B · The quality standard / `qsr-sB` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: show the linked Structure → Process → Outcome model and introduce continuous improvement. |
| Objective(s) | — (teaches `qsr-o1`; assessed at `qsr-011` and `qsr-012`). |
| On-the-job action | A3 — describe how quality is measured and improved. |
| Source | Source video, 01:20 (Structure / Processes / Outcomes and valid, reliable data) and 02:00 (FOCUS-PDCA model). |
| Depends on Phase 0 | B1 for the narration transcript; B11 for exact FOCUS-PDCA step names. The three quality categories are in the source frame. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | How quality is measured |
| Body / keywords | Structure → Process → Outcome · Collect valid, reliable data · FOCUS-PDCA improvement cycle ⚠ PENDING B11 |
| Word count (excl. title) | 12 |
| Instruction | n/a (display diagram). |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Three linked blocks run left to right across a white stage; a small separate cycle badge connects measurement to improvement without obscuring the model. |
| edumints layout | n/a (`labeled_diagram`, `mode: "display"`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings My Clinic Navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · warning Responsible magenta `#9D3293` only for a pending policy warning. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None (never behind body content). |
| Icons | Three small own-SVG line icons: clinic/resources, team process, patient outcome; navy with a Caring-purple connector. |
| Animation / reveal | The three labels reveal left to right; the cycle badge appears last. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `qsr-img-spo` | svg | Own 1600×900 SVG draft ([`assets/qsr-img-spo.svg`](assets/qsr-img-spo.svg)): Structure → Processes → Outcomes blocks with arrows, a “valid, reliable data” bar and an improvement-cycle badge (step names pending B11); callout anchors match the build labels. | own | Diagram linking structure, processes and outcomes, with a separate improvement-cycle callout. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Diagram labels | `structure`: resources and setting · `process`: how work is performed · `outcome`: results for patients |
| Supporting statement | Collect valid, reliable data that reflects actual performance. |
| Correct answer(s) | n/a (static display) |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Clear, explanatory |
| Target seconds | 35 |
| Word count / est. seconds | 77 spoken words / ≈ 33 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Start with structure: the resources and setting available to provide care. Processes describe what the team does and how consistently it is done. Outcomes describe the results for patients. The three layers connect, but they answer different questions. Reliable, valid data helps a team understand actual performance rather than rely on impressions. The improvement cycle shown here connects measurement to action; confirm its approved step names before production. The arrow shows how measurement supports improvement over time.

New lexicon terms: None; do not speak the initials unless the pronunciation guide is applied.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | No interaction; the DOM follows Structure, Process, Outcome, then improvement-cycle callout. |
| Not colour-only | Each stage is named in text and ordered by position; arrows also show the relationship. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "labeled_diagram",
  "id": "qsr-010",
  "title": "How quality is measured",
  "section": "B · The quality standard",
  "node_id": "qsr-sB",
  "objective_ids": [],
  "points": 0,
  "image_asset_id": "<qsr-img-spo>",
  "image_alt": "Diagram linking structure, processes and outcomes, with a separate improvement-cycle callout.",
  "prompt_html": "<p>Collect valid, reliable data that reflects actual performance.</p><p>FOCUS-PDCA improvement cycle: exact step names ⚠ PENDING B11.</p>",
  "mode": "display",
  "labels": [
    {
      "id": "structure",
      "text": "Structure — resources and setting",
      "x": 300,
      "y": 540
    },
    {
      "id": "process",
      "text": "Process — how work is performed",
      "x": 800,
      "y": 540
    },
    {
      "id": "outcome",
      "text": "Outcome — results for patients",
      "x": 1300,
      "y": 540
    }
  ],
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-010>",
  "feedback": {
    "correct_html": "<p>The diagram links structure, processes and outcomes; use reliable data to understand performance.</p>",
    "incorrect_html": "<p>Review each labelled stage and the relationship shown by the arrows.</p>",
    "show_correct_answer": true
  },
  "narration_text": "Noor: Start with structure: the resources and setting available to provide care. Processes describe what the team does and how consistently it is done. Outcomes describe the results for patients. The three layers connect, but they answer different questions. Reliable, valid data helps a team understand actual performance rather than rely on impressions. The improvement cycle shown here connects measurement to action; confirm its approved step names before production. The arrow shows how measurement supports improvement over time."
}
```

#### 8. Notes for SME and developer

- Open questions: B11: Quality Director to confirm the organisation-approved FOCUS-PDCA step names. Keep the category labels tied to the source frame.
- Developer notes: The SVG must use real text labels/callouts, not AI-rendered text. Keep the FOCUS-PDCA callout visually separate from the S-P-O chain.


### `qsr-011` — Classify the measures

**Status:** `Draft — ready for SME review` · **Section / node:** B · The quality standard / `qsr-sB` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: distinguish structural resources, work processes and patient outcomes. |
| Objective(s) | `qsr-o1` — classify quality measures as structure, process or outcome. |
| On-the-job action | A3 — describe how quality is measured and improved. |
| Source | Source video, 01:20 for definitions; measure examples are Phase 2 practice items, not reported My Clinic data. |
| Depends on Phase 0 | B4 for the exact two-identifier practice wording used in one illustrative item; B10 for hand-hygiene wording. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Classify the measures |
| Body / keywords | Resources · Actions carried out · Patient results |
| Word count (excl. title) | 6 |
| Instruction | Place each illustrative measure in Structure, Process or Outcome, then check. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Seven compact measure cards sit above three equal labelled targets; the target order is fixed and keyboard placement is available. |
| edumints layout | n/a (`drag_drop`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | Three small own-family line icons for resource, action and result; navy outline, Caring-purple focus state. |
| Animation / reveal | None; all items are available immediately. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | `ratio` Nurse-to-patient ratio → Structure · `defib` Working defibrillator in every clinic → Structure · `identity` Percentage of patients checked with two identifiers → Process ⚠ PENDING B4 · `hygiene` Hand-hygiene compliance → Process ⚠ PENDING B10 · `falls` Patient falls per 1,000 visits → Outcome · `satisfaction` Patient satisfaction score → Outcome · `hba1c` HbA1c control in a diabetes programme → Outcome |
| Targets | `structure` Structure · `process` Process · `outcome` Outcome |
| Correct answer(s) | ratio/defib → Structure; identity/hygiene → Process; falls/satisfaction/HbA1c → Outcome |
| Points | 10 |
| Feedback — correct | Correct: resources are structure, actions are process, and patient results are outcomes. These examples are for practice, not local performance data. |
| Feedback — incorrect | Look at what each measure observes: available resources, a care activity, or a result for patients. Then classify it again. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 18 spoken words / ≈ 7.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Classify each measure as resources, actions or patient results. Apply the definitions from the previous screen before checking.

New lexicon terms: `HbA1c` → “H-B-A-one-C” (master lexicon); it appears in a measure label, not narration.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Use keyboard focus plus Space/Enter to pick an item and choose a labelled target; provide a non-drag alternative. |
| Not colour-only | Every target has a text heading and icon; correctness uses text and a symbol plus colour. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "drag_drop",
  "id": "qsr-011",
  "title": "Classify the measures",
  "section": "B · The quality standard",
  "node_id": "qsr-sB",
  "objective_ids": [
    "qsr-o1"
  ],
  "evidence_screen_ids": [
    "qsr-010"
  ],
  "points": 10,
  "prompt_html": "<p>Place each illustrative measure in Structure, Process or Outcome. These are practice examples, not My Clinic performance results.</p>",
  "items": [
    {
      "id": "ratio",
      "text_html": "Nurse-to-patient ratio",
      "correct_target_id": "structure"
    },
    {
      "id": "defib",
      "text_html": "Working defibrillator in every clinic",
      "correct_target_id": "structure"
    },
    {
      "id": "identity",
      "text_html": "Percentage of patients checked with two identifiers ⚠ PENDING B4",
      "correct_target_id": "process"
    },
    {
      "id": "hygiene",
      "text_html": "Hand-hygiene compliance ⚠ PENDING B10",
      "correct_target_id": "process"
    },
    {
      "id": "falls",
      "text_html": "Patient falls per 1,000 visits",
      "correct_target_id": "outcome"
    },
    {
      "id": "satisfaction",
      "text_html": "Patient satisfaction score",
      "correct_target_id": "outcome"
    },
    {
      "id": "hba1c",
      "text_html": "HbA1c control in a diabetes programme",
      "correct_target_id": "outcome"
    }
  ],
  "targets": [
    {
      "id": "structure",
      "label_html": "Structure — resources and setting"
    },
    {
      "id": "process",
      "label_html": "Process — actions carried out"
    },
    {
      "id": "outcome",
      "label_html": "Outcome — patient results"
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> Resources are structure, actions are process, and patient results are outcomes. These examples are practice items, not local performance data.</p>",
    "incorrect_html": "<p>Look at what each measure observes: available resources, a care activity, or a result for patients.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-011>",
  "narration_text": "Noor: Classify each measure as resources, actions or patient results. Apply the definitions from the previous screen before checking."
}
```

#### 8. Notes for SME and developer

- Open questions: B4 and B10: validate the two-identifier and hand-hygiene wording. The numeric examples are illustrative only and must not be presented as My Clinic results.
- Developer notes: The drop targets and instructions must expose keyboard pick-and-place controls; keep category meaning in text, not colour.


### `qsr-012` — FOCUS-PDCA: order the steps

**Status:** `Draft — ready for SME review` · **Section / node:** B · The quality standard / `qsr-sB` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: order the approved FOCUS-PDCA improvement-cycle steps. |
| Objective(s) | `qsr-o1` — order the FOCUS-PDCA cycle. |
| On-the-job action | A3 — describe how quality is measured and improved. |
| Source | Source video, 02:00 (FOCUS-PDCA model and sequence). |
| Depends on Phase 0 | B1 (transcript listen) and B11 (official step names). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | FOCUS-PDCA: order the steps |
| Body / keywords | Nine steps · One repeating cycle · Exact wording ⚠ PENDING B11 |
| Word count (excl. title) | 9 |
| Instruction | Arrange the steps in order, then check how the final step begins the next cycle. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Nine numbered text cards form one vertical sequence with a curved return arrow from Act to Find; numbering appears only after checking. |
| edumints layout | n/a (`sorting`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | No separate imagery; the return arrow is a simple own line element in navy. |
| Animation / reveal | None; position communicates sequence. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items (correct order) | `find` Find → `organise` Organise → `clarify` Clarify → `understand` Understand → `select` Select → `plan` Plan → `do` Do → `check` Check → `act` Act |
| Correct answer(s) | Find → Organise → Clarify → Understand → Select → Plan → Do → Check → Act |
| Points | 5 |
| Feedback — correct | Correct: FOCUS leads into Plan–Do–Check–Act, and the cycle continues rather than ending after one project. ⚠ PENDING B11: confirm the organisation’s approved words. |
| Feedback — incorrect | Rebuild the order from the confirmed FOCUS-PDCA model; treat improvement as a repeating cycle, not a one-off checklist. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 19 spoken words / ≈ 8.1 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Arrange the nine steps in order and show how the last begins the next cycle. Don't skip a step.

New lexicon terms: `FOCUS-PDCA` → “focus, P-D-C-A” (master lexicon).

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Sorting supports keyboard reordering; provide labelled move-up/move-down buttons. |
| Not colour-only | The sequence is represented by item position and explicit step names; the return arrow shows the cycle. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "sorting",
  "id": "qsr-012",
  "title": "FOCUS-PDCA: order the steps",
  "section": "B · The quality standard",
  "node_id": "qsr-sB",
  "objective_ids": [
    "qsr-o1"
  ],
  "evidence_screen_ids": [
    "qsr-010"
  ],
  "points": 5,
  "prompt_html": "<p>Arrange the FOCUS-PDCA steps in order. ⚠ PENDING B11: confirm exact labels before release.</p>",
  "items": [
    {
      "id": "find",
      "text_html": "Find ⚠ PENDING B11"
    },
    {
      "id": "organise",
      "text_html": "Organise ⚠ PENDING B11"
    },
    {
      "id": "clarify",
      "text_html": "Clarify ⚠ PENDING B11"
    },
    {
      "id": "understand",
      "text_html": "Understand ⚠ PENDING B11"
    },
    {
      "id": "select",
      "text_html": "Select ⚠ PENDING B11"
    },
    {
      "id": "plan",
      "text_html": "Plan ⚠ PENDING B11"
    },
    {
      "id": "do",
      "text_html": "Do ⚠ PENDING B11"
    },
    {
      "id": "check",
      "text_html": "Check ⚠ PENDING B11"
    },
    {
      "id": "act",
      "text_html": "Act ⚠ PENDING B11"
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> FOCUS leads into Plan–Do–Check–Act; improvement continues as a cycle. ⚠ PENDING B11: confirm exact approved terms.</p>",
    "incorrect_html": "<p>Rebuild the order from the organisation-approved FOCUS-PDCA model. Treat improvement as a repeating cycle.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-012>",
  "narration_text": "Noor: Arrange the nine steps in order and show how the last begins the next cycle. Don't skip a step."
}
```

#### 8. Notes for SME and developer

- Open questions: B11: Quality Director must confirm all nine step names and spelling; keep this item unapproved until confirmed.
- Developer notes: Do not imply that the sequence has been policy-approved while B11 is open. Include keyboard reordering.


### `qsr-020` — Six patient-safety goals

**Status:** `Draft — ready for SME review` · **Section / node:** C · Patient safety goals / `qsr-sC` · **Type:** `hotspot` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explore: connect each of the six patient-safety goals to its draft everyday practice. |
| Objective(s) | — (teaches `qsr-o2`; assessed at `qsr-021`–`qsr-023`). |
| On-the-job action | A2 — apply the six safety goals in daily work. |
| Source | Source video, 02:40–04:10 (six goals and described practices). |
| Depends on Phase 0 | B1, B3 (goal names/numbering), B4 (identifiers), B5 (falls band), B10 (hand-hygiene moments). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Six patient-safety goals |
| Body / keywords | Identification · Communication · High-alert medication · Safe procedures · Hand hygiene · Fall prevention ⚠ PENDING B3 |
| Word count (excl. title) | 12 |
| Instruction | Open all six goal panels and read the draft practice for each. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Six separate icon panels form a 3-by-2 grid; opening a panel reveals its practice in a nearby text card, and a counter tracks panels visited. |
| edumints layout | n/a (`hotspot`, `mode: "explore"`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings My Clinic Navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · warning Responsible magenta `#9D3293` only for a pending policy warning. Safety-specific colours appear only where the confirmed policy requires them; do not imply risk bands. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None (never behind body content). |
| Icons | Six own-SVG line icons in one family: identity card, speech bubble, medication vial, procedure checklist, clean hands, and fall-prevention symbol; navy outlines and Caring-purple highlights. |
| Animation / reveal | Unvisited panels receive a gentle outline; visited panels use a check icon and text label. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `qsr-img-pillars` | svg | Own 960×540 six-panel icon grid; no baked text; hotspots align with six panels; details remain HTML. | own | Six icon panels represent identification, communication, high-alert medicines, safe procedures, hand hygiene and fall prevention; panel names and practices are also text. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Mode | `explore`; `require_all: true`; unscored |
| Regions | `g1` Identification — two approved identifiers ⚠ PENDING B4 · `g2` Communication — verify verbal/telephone orders, critical results, structured handover ⚠ PENDING B3 · `g3` High-alert medications — standard process, red label and independent double-check ⚠ PENDING B3 · `g4` Safe procedures — checks, site marking, time-out/sign-out ⚠ PENDING B3 · `g5` Hand hygiene — five moments ⚠ PENDING B10 · `g6` Falls — band colour ⚠ PENDING B5 |
| Rough positions / coordinates | `g1` top-left, `g2` top-centre, `g3` top-right; `g4` bottom-left, `g5` bottom-centre, `g6` bottom-right. Draft `rect` coordinates use the planned 960×540 SVG and are **TBD after final SVG**. |
| Correct answer(s) | n/a — every region is a required explore panel |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Clear, practical |
| Target seconds | 30 |
| Word count / est. seconds | 75 spoken words / ≈ 32.1 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Patient safety is supported by six linked goals, not one reminder. Each goal names an area where teams can reduce avoidable risk. Open every pillar and read the practice paired with it. The exact wording, numbering and several details still need policy confirmation, so these descriptions are marked for review before release. Use the approved facility language once it is confirmed. The exercise is meant to help you connect a goal with a daily action.

New lexicon terms: None; say “International Patient Safety Goals” in full if needed.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Hotspot regions are keyboard-focusable buttons with accessible names; all panel descriptions appear in the DOM and can be opened with Enter/Space. |
| Not colour-only | Each panel has a number, icon and full text label; visited state includes a check and “opened” text. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed; require all six panels, not a timed visit. |

#### 7. Build fields (edumints)

```json
{
  "type": "hotspot",
  "id": "qsr-020",
  "title": "Six patient-safety goals",
  "section": "C · Patient safety goals",
  "node_id": "qsr-sC",
  "objective_ids": [],
  "image_asset_id": "<qsr-img-pillars>",
  "image_alt": "Six icon panels represent the six patient-safety goals; panel names and practices are also available as text.",
  "prompt_html": "<p>Open all six goals. Draft practice wording requires policy confirmation ⚠ PENDING B3.</p>",
  "mode": "explore",
  "require_all": true,
  "points": 0,
  "regions": [
    {
      "id": "g1",
      "shape": "rect",
      "coords": [
        0,
        0,
        320,
        270
      ],
      "label_html": "<strong>Goal 1 — Identification ⚠ PENDING B3</strong><p>Use two approved identifiers. Exact rule ⚠ PENDING B4.</p>",
      "feedback_html": "<p>Identification helps match care to the intended patient. Confirm the approved identifiers before release.</p>"
    },
    {
      "id": "g2",
      "shape": "rect",
      "coords": [
        320,
        0,
        640,
        270
      ],
      "label_html": "<strong>Goal 2 — Communication ⚠ PENDING B3</strong><p>Verify verbal/telephone orders, report critical results and use structured handover.</p>",
      "feedback_html": "<p>Communication practices reduce ambiguity at handover and when orders or results are shared.</p>"
    },
    {
      "id": "g3",
      "shape": "rect",
      "coords": [
        640,
        0,
        960,
        270
      ],
      "label_html": "<strong>Goal 3 — High-alert medicines ⚠ PENDING B3</strong><p>Draft mentions a red label and independent double-check.</p>",
      "feedback_html": "<p>Use the facility’s approved high-alert medication process; confirm details before production.</p>"
    },
    {
      "id": "g4",
      "shape": "rect",
      "coords": [
        0,
        270,
        320,
        540
      ],
      "label_html": "<strong>Goal 4 — Safe procedures ⚠ PENDING B3</strong><p>Draft practices include verification, site marking, time-out and sign-out.</p>",
      "feedback_html": "<p>Procedure safeguards must follow the current facility policy and approved terminology.</p>"
    },
    {
      "id": "g5",
      "shape": "rect",
      "coords": [
        320,
        270,
        640,
        540
      ],
      "label_html": "<strong>Goal 5 — Hand hygiene ⚠ PENDING B10</strong><p>Five moments: before patient contact, before a clean procedure, after body-fluid exposure risk, after patient contact, after surroundings.</p>",
      "feedback_html": "<p>Use the facility poster wording for each moment before release.</p>"
    },
    {
      "id": "g6",
      "shape": "rect",
      "coords": [
        640,
        270,
        960,
        540
      ],
      "label_html": "<strong>Goal 6 — Fall prevention ⚠ PENDING B5</strong><p>Draft source mentions a high-risk identifier band; confirm its colour and use.</p>",
      "feedback_html": "<p>Confirm the falls-policy identifier before naming or illustrating it.</p>"
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-020>",
  "feedback": {
    "correct_html": "<p>All six goal panels are open. Use the confirmed facility wording before release.</p>",
    "incorrect_html": "<p>Open the remaining goal panels to complete the exploration.</p>",
    "show_correct_answer": true
  },
  "narration_text": "Noor: Patient safety is supported by six linked goals, not one reminder. Each goal names an area where teams can reduce avoidable risk. Open every pillar and read the practice paired with it. The exact wording, numbering and several details still need policy confirmation, so these descriptions are marked for review before release. Use the approved facility language once it is confirmed. The exercise is meant to help you connect a goal with a daily action."
}
```

#### 8. Notes for SME and developer

- Open questions: B3–B5/B10: confirm goal wording, identifier rule, falls-band use/colour and the five moments. Keep the panels visibly marked pending until the relevant owner confirms them.
- Developer notes: SVG is 960×540; region coordinates are planned rectangles and must be rechecked against the approved final artwork. SVG contains icons only—no text, letters or numbers.


### `qsr-021` — Which patient?

**Status:** `Draft — ready for SME review` · **Section / node:** C · Patient safety goals / `qsr-sC` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: identify the intended patient when two records share a name and correct an unsafe shortcut. |
| Objective(s) | `qsr-o2` — apply patient-safety goals, including the two-identifier rule. |
| On-the-job action | A1 — identify every patient with the approved identifiers before care. |
| Source | Source video, 03:20 (Goal 1); Phase 2 scenario and Phase 4 node-1 snippet. All names and MRNs are fictional training data. |
| Depends on Phase 0 | B1 (source listen), B3 (Goal 1 wording), B4 (approved identifiers and same-name rule). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Which patient? |
| Body / keywords | Two fictional records share one full name. Verify before care. ⚠ PENDING B4 |
| Word count (excl. title) | 12 |
| Instruction | Choose what you would do at each decision point before the blood test proceeds. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario (see `../../00_program/brand/screen-mockups/05-scenario.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Noor's 56 px scenario avatar (purple ring, “Noor · Safety liaison”) sits above the situation; a text-free wristband illustration sits left of the three-node decision and two cards show the same name with different fictional record numbers; the avatar changes from concern on the intro to happy or concern after each choice. |
| edumints layout | n/a (`decision_scenario`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · header navy `#003867` · cards white `#FFFFFF` with line `#D9E1E8` · highlight Caring purple `#652D8C` · feedback success `#1E7B4F` / error `#B42318` with icons + words. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; situation Montserrat SemiBold 600, 17 px; choices/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (scenario screens have no watermark). |
| Icons | No extra icons beyond the shared line family; the wristband itself is a text-free illustration. |
| Animation / reveal | Situation card fades between nodes; choices remain still and keyboard focus is visible. |
| Companion | Noor · pose `char-noor-avatar-concern` on the intro → `char-noor-avatar-happy` after a best choice / `-avatar-concern` after an unsafe one · placement L5 scenario avatar, 56 px with a 3 px purple `#652D8C` ring and “Noor · Safety liaison” above the situation · tip text n/a |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `qsr-img-wristbands` | illustration | Two plain, unprinted patient wristbands side by side; no names or numbers inside image (fictional identifiers remain HTML text). | ai-generated | Two blank patient wristbands side by side; the fictional name and record numbers are provided as accessible HTML text. | No |
| `char-noor-avatar-concern` | character | Shared programme companion avatar, cropped to a circle; 56 px circular scenario avatar, purple ring, above the situation. | programme asset to make: crop from `char-noor-concern` (MAHX-hFE0aQ) (companions.md §3); no module prompt | Noor, the safety liaison, looking concerned. | No |
| `char-noor-avatar-happy` | character | Shared programme companion avatar, cropped to a circle; 56 px circular scenario avatar, purple ring, above the situation. | programme asset to make: crop from `char-noor-success` (MAHX-jiR90M) (companions.md §3); no module prompt | Noor, the safety liaison, smiling. | No |


**AI image prompt** (filled from `brand-identity.md` §6; `qsr-img-wristbands` only; no logo/text):

Asset `qsr-img-wristbands`:

```text
Flat vector illustration for a healthcare e-learning course, 16:9, two clean patient wristbands placed side by side on a pale clinical surface; both bands have blank, unprinted ID panels with no markings. Clean minimalist style, simple geometric shapes, thin navy (#003867) outlines, white and very light blue-grey (#F4F7FA, #C0CED9) surfaces, one highlight colour Caring purple (#652D8C), no magenta. Modern Saudi outpatient clinic context suggested only by the clean, bright surface, lots of white space, soft even lighting, no shadows or very soft flat shadows.
People: no people. Modest, culturally appropriate clothing for Saudi Arabia.
No text, no letters, no numbers, no logos, no signage words, no watermarks, no brand names.
Negative prompt: photorealism, 3D render, gradients, neon colours, clutter, extra medical devices, labels, printed marks, logos, text, dark or dramatic lighting, blood, injury, distorted hands, Western hospital stereotypes.
```

Companion art: shared programme poses only (`char-noor-*`, companions.md §3). No module-specific character prompt; never re-prompt Noor.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Intro | Two fictional patients named Mohammed Al-Harbi are waiting for blood tests. Fictional training record numbers: 100245 and 100871. |
| Nodes | `n1` confirm the patient before the draw · `n2` both names match · `n3` colleague suggests using age |
| Correct answer(s) | `n1-a`: full name + MRN compared with request ⚠ PENDING B4 · `n2-a`: use the additional identifier specified by policy (DOB or national ID) ⚠ PENDING B4 · `n3-a`: pause and re-verify using approved identifiers; age is not an identifier ⚠ PENDING B4 |
| Points / pass rule | 15 points · `pass_score: 2` of 3 best decisions |
| Per-choice feedback | Every option has explanatory `feedback_html`; correct feedback explains the two identifiers, wrong feedback explains why room/age/familiarity is unsafe. |
| Retry | Replay the scenario; do not inflate the recorded result across retries. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Serious, warm |
| Target seconds | 15 |
| Word count / est. seconds | 34 spoken words / ≈ 14.6 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: I once nearly drew blood from the wrong Mr Al-Harbi. The wristband stopped me. Now two fictional patients share one full name. Decide what you check, and what you do if both names match.

Companion note: Noor's honest story (companions.md §1) is used once, here; it sets up the scene and does not name the identifiers the learner must choose.

New lexicon terms: `MRN` → “medical record number”; say the term in full in narration.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Choices are keyboard-focusable buttons; Enter/Space selects. The same name and fictional numbers are included in accessible text, not only in the image. |
| Not colour-only | Each choice has text; feedback includes ✓/warning icon and “Correct” or explanatory words, not colour alone. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed; no countdown. |

#### 7. Build fields (edumints)

```json
{
  "type": "decision_scenario",
  "id": "qsr-021",
  "title": "Which patient?",
  "section": "C · Patient safety goals",
  "node_id": "qsr-sC",
  "objective_ids": [
    "qsr-o2"
  ],
  "evidence_screen_ids": [
    "qsr-020"
  ],
  "points": 15,
  "pass_score": 2,
  "intro_html": "<p>Two fictional patients named Mohammed Al-Harbi are waiting for blood tests. Fictional training record numbers: 100245 and 100871. Confirm identity before care continues.</p>",
  "start_node_id": "n1",
  "nodes": [
    {
      "id": "n1",
      "image_asset_id": "<qsr-img-wristbands>",
      "image_alt": "Two blank wristbands; fictional names and record numbers are shown as accessible HTML text.",
      "prompt_html": "<p>One patient is ready for a blood test. How do you confirm you have the right record?</p>",
      "choices": [
        {
          "id": "a",
          "text_html": "Ask the full name and compare the medical record number on the wristband with the request.",
          "score_delta": 1,
          "goto_node_id": "n2",
          "feedback_html": "<p><strong>Correct for the draft.</strong> The source plan names full name and medical record number. Confirm the facility rule before release. ⚠ PENDING B4</p>"
        },
        {
          "id": "b",
          "text_html": "Use the room number to choose the record.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>A room number is not one of the two identifiers named in the draft. Confirm the official rule. ⚠ PENDING B4</p>"
        },
        {
          "id": "c",
          "text_html": "Use the patient’s age.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>The source says age must not be used as an identifier. Confirm the facility’s approved wording. ⚠ PENDING B4</p>"
        }
      ]
    },
    {
      "id": "n2",
      "image_asset_id": "<qsr-img-wristbands>",
      "image_alt": "Two fictional wristbands share one name and show different fictional record numbers.",
      "prompt_html": "<p>The names match exactly. What should happen next?</p>",
      "choices": [
        {
          "id": "a",
          "text_html": "Pause and use the additional identifier specified by policy: date of birth or national ID. ⚠ PENDING B4",
          "score_delta": 1,
          "goto_node_id": "n3",
          "feedback_html": "<p>The Phase 2 draft names date of birth or national ID when names match. Use only the confirmed local rule. ⚠ PENDING B4</p>"
        },
        {
          "id": "b",
          "text_html": "Use age or room number as a tie-breaker.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Age and location are not safe tie-breakers. Follow the confirmed identifier policy. ⚠ PENDING B4</p>"
        },
        {
          "id": "c",
          "text_html": "Guess based on who looks familiar.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Familiarity does not verify identity. Stop and use the additional identifier allowed by policy. ⚠ PENDING B4</p>"
        }
      ]
    },
    {
      "id": "n3",
      "image_asset_id": "<qsr-img-wristbands>",
      "image_alt": "Two blank wristbands; the fictional name and record numbers are shown as accessible HTML text.",
      "prompt_html": "<p>A colleague says, “It’s the older one.” What do you do?</p>",
      "choices": [
        {
          "id": "a",
          "text_html": "Pause the draw, explain that age is not an identifier, and re-verify using approved identifiers. ⚠ PENDING B4",
          "score_delta": 1,
          "goto_node_id": null,
          "feedback_html": "<p><strong>Correct for the draft.</strong> Do not proceed on age or assumption; use the confirmed identifiers. ⚠ PENDING B4</p>"
        },
        {
          "id": "b",
          "text_html": "Proceed because the colleague knows the patient.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>Familiarity does not replace the identifier check. Pause and verify before care continues. ⚠ PENDING B4</p>"
        },
        {
          "id": "c",
          "text_html": "Ask another bystander to choose.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>A bystander cannot resolve an identity mismatch. Follow the approved identifier process. ⚠ PENDING B4</p>"
        }
      ]
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-021>",
  "feedback": {
    "correct_html": "<p>You have practised pausing and verifying identity. Use the confirmed identifiers and same-name rule.</p>",
    "incorrect_html": "<p>Revisit the approved identifier policy and the reasons each shortcut is unsafe.</p>",
    "show_correct_answer": true
  },
  "notes": "Companion: Noor L5 scenario avatar above the situation — char-noor-avatar-concern on intro, char-noor-avatar-happy / char-noor-avatar-concern after each choice. Speaker: Noor (honest story, companions.md §1).",
  "narration_text": "Noor: I once nearly drew blood from the wrong Mr Al-Harbi. The wristband stopped me. Now two fictional patients share one full name. Decide what you check, and what you do if both names match."
}
```

#### 8. Notes for SME and developer

- Open questions: B4: Nursing Director to confirm the two identifiers and third-identifier rule when names match. Confirm the source examples after B1. Fictional values must remain explicitly labelled as training data.
- Developer notes: Use `qsr-img-wristbands` on all three nodes (the Screen model allows one image per node) and render every name/MRN value as accessible HTML. Noor's avatar is L5 template chrome above the situation, not a node image: `char-noor-avatar-concern` on the intro, `-avatar-happy` after a best choice, `-avatar-concern` after an unsafe one. Her honest story is used only on this screen in the programme (companions.md §1). Companion art is the shared programme set — no module-specific character prompt.


### `qsr-022` — Practice meets goal

**Status:** `Draft — ready for SME review` · **Section / node:** C · Patient safety goals / `qsr-sC` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: connect common patient-safety practices to the goal they support. |
| Objective(s) | `qsr-o2` — apply the six patient-safety goals. |
| On-the-job action | A2 — apply the six safety goals in daily work. |
| Source | Source video, 03:20–04:10; Phase 2 practice pairs. |
| Depends on Phase 0 | B1, B3 (IPSG wording), B4 (identifiers), B5 (falls band). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Practice meets goal |
| Body / keywords | Match each daily practice to one goal. ⚠ PENDING B3–B5 |
| Word count (excl. title) | 10 |
| Instruction | Match each practice with the patient-safety goal it supports. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Six practice cards line up on the left and six goal labels on the right; long labels wrap without truncation. |
| edumints layout | n/a (`matching`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | None; keep every pair as text so the learner matches meaning rather than icon colour. |
| Animation / reveal | None. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Pairs | `p1` Full name + medical record number → Goal 1, Identification ⚠ PENDING B4 · `p2` Read back a telephone order → Goal 2, Communication ⚠ PENDING B3 · `p3` Red label + independent double-check → Goal 3, High-alert medications ⚠ PENDING B3 · `p4` Time-out before a procedure → Goal 4, Safe procedures ⚠ PENDING B3 · `p5` Clean hands before patient contact → Goal 5, Hand hygiene ⚠ PENDING B10 · `p6` Yellow band for a high-fall-risk patient → Goal 6, Fall prevention ⚠ PENDING B5 |
| Correct answer(s) | Each practice maps to its numbered goal above. |
| Points | 10 |
| Feedback — correct | Correct: each safe practice supports a specific goal. Confirm all goal wording with the facility policy before release. |
| Feedback — incorrect | Compare the purpose of each practice with the goal label; several details remain pending policy review. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 18 spoken words / ≈ 7.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Match each workplace practice with its patient-safety goal. Use each goal once, then check against the approved wording.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Each pair is operable with keyboard; provide labelled selects or keyboard matching, not pointer-only lines. |
| Not colour-only | Goal number and full name are written; match state uses line/border plus text. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "matching",
  "id": "qsr-022",
  "title": "Practice meets goal",
  "section": "C · Patient safety goals",
  "node_id": "qsr-sC",
  "objective_ids": [
    "qsr-o2"
  ],
  "evidence_screen_ids": [
    "qsr-020"
  ],
  "points": 10,
  "prompt_html": "<p>Match each practice with the patient-safety goal it supports. ⚠ PENDING B3–B5.</p>",
  "pairs": [
    {
      "id": "p1",
      "left_html": "Full name + medical record number ⚠ PENDING B4",
      "right_html": "Goal 1 — Identification ⚠ PENDING B3"
    },
    {
      "id": "p2",
      "left_html": "Read back a telephone order",
      "right_html": "Goal 2 — Communication ⚠ PENDING B3"
    },
    {
      "id": "p3",
      "left_html": "Red label + independent double-check ⚠ PENDING B3",
      "right_html": "Goal 3 — High-alert medications ⚠ PENDING B3"
    },
    {
      "id": "p4",
      "left_html": "Time-out before a procedure ⚠ PENDING B3",
      "right_html": "Goal 4 — Safe procedures ⚠ PENDING B3"
    },
    {
      "id": "p5",
      "left_html": "Clean hands before patient contact ⚠ PENDING B10",
      "right_html": "Goal 5 — Hand hygiene ⚠ PENDING B3"
    },
    {
      "id": "p6",
      "left_html": "Yellow band for high fall risk ⚠ PENDING B5",
      "right_html": "Goal 6 — Fall prevention ⚠ PENDING B3"
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> Each safe practice supports a specific goal. Confirm all wording with the current facility policy before release.</p>",
    "incorrect_html": "<p>Compare each practice with the purpose of the goal label. Several details remain pending policy review.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-022>",
  "narration_text": "Noor: Match each workplace practice with its patient-safety goal. Use each goal once, then check against the approved wording."
}
```

#### 8. Notes for SME and developer

- Open questions: B3–B5/B10: confirm goals, identifiers, falls-band colour and hand-hygiene practice. Keep each answer marked pending until confirmed.
- Developer notes: The matching screen is text-first; do not use colour as the only link between a practice and goal.


### `qsr-023` — Five moments

**Status:** `Draft — ready for SME review` · **Section / node:** C · Patient safety goals / `qsr-sC` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: order the five hand-hygiene moments around patient care. |
| Objective(s) | `qsr-o2` — apply the patient-safety goals. |
| On-the-job action | A2 — apply the six safety goals in daily work. |
| Source | Source video, 04:10; five-moment sequence transcribed in Phase 2. |
| Depends on Phase 0 | B1 (listen) and B10 (facility poster wording). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Five moments |
| Body / keywords | Order the hand-hygiene moments. ⚠ PENDING B10 |
| Word count (excl. title) | 6 |
| Instruction | Arrange the five moments in the order shown in the approved hand-hygiene guidance. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Five numbered cards form a loop around a simple patient-contact marker; each stage is a text label and the loop arrow is decorative. |
| edumints layout | n/a (`sorting`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | One small own line icon for clean hands; navy outline with Caring-purple focus state. |
| Animation / reveal | None. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items (correct order) | `m1` Before touching a patient → `m2` Before a clean/aseptic procedure → `m3` After body-fluid exposure risk → `m4` After touching a patient → `m5` After touching patient surroundings |
| Correct answer(s) | m1 → m2 → m3 → m4 → m5 |
| Points | 5 |
| Feedback — correct | Correct: the five moments cover before care, before an aseptic task, after exposure risk, after care and after the patient’s surroundings. ⚠ PENDING B10: verify poster wording. |
| Feedback — incorrect | Think about what happens before patient contact, before a procedure, and after contact or exposure; confirm the facility poster language. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 18 spoken words / ≈ 7.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Order the five hand-hygiene moments around patient contact and the care task; include every stage without skipping one.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Use keyboard move-up/move-down controls with spoken labels; no drag-only ordering. |
| Not colour-only | Text names each moment; the loop arrow and sequence numbers support, but do not replace, the labels. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "sorting",
  "id": "qsr-023",
  "title": "Five moments",
  "section": "C · Patient safety goals",
  "node_id": "qsr-sC",
  "objective_ids": [
    "qsr-o2"
  ],
  "evidence_screen_ids": [
    "qsr-020"
  ],
  "points": 5,
  "prompt_html": "<p>Arrange the five moments in the order shown in the approved hand-hygiene guidance. ⚠ PENDING B10.</p>",
  "items": [
    {
      "id": "m1",
      "text_html": "Before touching a patient ⚠ PENDING B10"
    },
    {
      "id": "m2",
      "text_html": "Before a clean/aseptic procedure ⚠ PENDING B10"
    },
    {
      "id": "m3",
      "text_html": "After body-fluid exposure risk ⚠ PENDING B10"
    },
    {
      "id": "m4",
      "text_html": "After touching a patient ⚠ PENDING B10"
    },
    {
      "id": "m5",
      "text_html": "After touching patient surroundings ⚠ PENDING B10"
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> The five moments cover before care, before an aseptic task, after exposure risk, after care and after the patient’s surroundings. Verify exact poster wording. ⚠ PENDING B10</p>",
    "incorrect_html": "<p>Think about before patient contact, before a procedure, and after contact or exposure. Confirm the facility poster wording.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-023>",
  "narration_text": "Noor: Order the five hand-hygiene moments around patient contact and the care task; include every stage without skipping one."
}
```

#### 8. Notes for SME and developer

- Open questions: B10: Infection Control lead confirms the five moments against the facility poster; no alternate wording is approved yet.
- Developer notes: Sequence order in the interaction must remain exactly as Phase 2 after B10 review.


### `qsr-030` — Risk-management lifecycle

**Status:** `Draft — ready for SME review` · **Section / node:** D · Risk management / `qsr-sD` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: sequence the risk-management lifecycle from identification to reporting. |
| Objective(s) | `qsr-o3` — score a risk and choose an appropriate response. |
| On-the-job action | A4 — score a risk and propose a response. |
| Source | Source video, 04:40 (Identify · Assess · Manage · Monitor · Report in the risk register). |
| Depends on Phase 0 | B1 for transcript wording; the lifecycle labels are visible in the source slide. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Risk-management lifecycle |
| Body / keywords | Identify · Assess · Manage · Monitor · Report |
| Word count (excl. title) | 5 |
| Instruction | Put the risk-management lifecycle in order. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Five labelled stage cards sit in one vertical column; a narrow number track appears only after the answer is checked. |
| edumints layout | n/a (`sorting`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | No separate image; numbered track and arrows are built from HTML/CSS. |
| Animation / reveal | None. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items (correct order) | `identify` Identify → `assess` Assess → `manage` Manage (controls) → `monitor` Monitor → `report` Report in the risk register |
| Correct answer(s) | Identify → Assess → Manage → Monitor → Report |
| Points | 5 |
| Feedback — correct | Correct: identify and assess the risk, put controls in place, monitor them, then report exposure in the risk register. |
| Feedback — incorrect | Monitoring only works after a risk has been assessed and managed; reporting records the exposure in the risk register. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Practical |
| Target seconds | 8 |
| Word count / est. seconds | 20 spoken words / ≈ 8.6 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Arrange the risk-management lifecycle from the first step through reporting, using the agreed labels. It's a sequence, not a score.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Keyboard move-up/move-down controls; each stage includes its complete text label. |
| Not colour-only | Stage names and ordered positions carry the sequence; no status is represented by colour alone. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "sorting",
  "id": "qsr-030",
  "title": "Risk-management lifecycle",
  "section": "D · Risk management",
  "node_id": "qsr-sD",
  "objective_ids": [
    "qsr-o3"
  ],
  "evidence_screen_ids": [
    "qsr-031"
  ],
  "points": 5,
  "prompt_html": "<p>Put the risk-management lifecycle in order.</p>",
  "items": [
    {
      "id": "identify",
      "text_html": "Identify"
    },
    {
      "id": "assess",
      "text_html": "Assess"
    },
    {
      "id": "manage",
      "text_html": "Manage — put controls in place"
    },
    {
      "id": "monitor",
      "text_html": "Monitor the controls"
    },
    {
      "id": "report",
      "text_html": "Report exposure in the risk register"
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> Identify and assess the risk, put controls in place, monitor them, then report exposure in the risk register.</p>",
    "incorrect_html": "<p>Monitoring follows assessment and management; reporting records exposure in the risk register.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-030>",
  "narration_text": "Noor: Arrange the risk-management lifecycle from the first step through reporting, using the agreed labels. It's a sequence, not a score."
}
```

#### 8. Notes for SME and developer

- Open questions: None beyond B1 source listen.
- Developer notes: qsr-031 revisits the lifecycle in a small instructional strip and acts as the course evidence screen for this practice.


### `qsr-031` — Score a risk

**Status:** `Draft — ready for SME review` · **Section / node:** D · Risk management / `qsr-sD` · **Type:** `worked_example` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: model impact × likelihood, then locate the result and choose a response without inventing local bands. |
| Objective(s) | — (teaches `qsr-o3`; assessed at `qsr-030`, `qsr-032` and `qsr-033`). |
| On-the-job action | A4 — score a risk and propose a response. |
| Source | Source video, 05:20 (impact × likelihood, 1–25) and 05:50–06:25 (response types); scenario inputs are illustrative teaching values. |
| Depends on Phase 0 | B1 (source listen), B6 (matrix bands/thresholds), B7 (risk-response wording). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Score a risk |
| Body / keywords | Hypothetical case · Impact 4 × likelihood 3 = 12 · Band ⚠ PENDING B6 · Responses: Reduce · Transfer · Accept · Avoid ⚠ PENDING B7 |
| Word count (excl. title) | 17 |
| Instruction | Follow the worked steps; consider a control in the reflection prompt. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | A white calculation ledger on the left reveals impact, likelihood and product step by step, with the draft 5×5 matrix (score in every cell, band names pending B6) at step 4; Dr. Omar (`char-omar-thinking`, hand at chin) stands half-body in the right column while he talks the example through. |
| edumints layout | n/a (`worked_example`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` for the score line · risk-band colours/labels ⚠ PENDING B6; no unconfirmed bands shown. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None (never behind body content). |
| Icons | Own 5×5 matrix SVG (labels and any colours only after B6); no AI-generated diagrams. |
| Animation / reveal | Reveal each worked step in order; the band remains a placeholder until policy confirmation. |
| Companion | Dr. Omar · pose `char-omar-thinking` · placement L3 right column, half-body 320–380 px tall; the worked steps stay in the left column · tip text n/a |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `qsr-img-matrix` | svg | Own 1600×900 SVG draft ([`assets/qsr-img-matrix.svg`](assets/qsr-img-matrix.svg)): 5×5 impact × likelihood grid with the score in every cell and a band-name slot in every cell reading “band ⚠ B6”; cells stay neutral (no band colours) until the Risk Manager supplies names, thresholds and colours; the 4 × 3 = 12 cell is outlined. | own | Risk matrix showing impact multiplied by likelihood on a 1-to-5 scale; exact band labels and colours are pending B6. | No |
| `char-omar-thinking` | character | Shared programme companion pose (preview: `00_program/characters/previews/char-omar-thinking.jpg`); half-body 320–380 px tall, right column. | ai-generated programme asset, Canva media `MAHX-jgu1Vk`, made from the approved master (companions.md §3); no module prompt | Dr. Omar, the family physician, with his hand at his chin, thinking through the risk score. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Hypothetical case | Expired stock found twice in a fictional clinic refrigerator; not a report of a real My Clinic event. |
| Steps | 1 Set impact to 4 (teaching input) · 2 Set likelihood to 3 (teaching input) · 3 Multiply 4 × 3 = 12 · 4 Look up band ⚠ PENDING B6 · 5 Compare Reduce · Transfer · Accept · Avoid; apply approved terms ⚠ PENDING B7 |
| Correct answer(s) | Numeric score = 12; local band and response terminology remain pending. |
| Points | 0 (worked example) |
| Self-explanation | What control could reduce the impact or likelihood in this hypothetical case? |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | Calm, explanatory, conversational |
| Target seconds | 40 |
| Word count / est. seconds | 102 spoken words / ≈ 43.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> OMAR: Let's score one together. It's a made-up case: expired items turn up twice this month in a clinic fridge. Impact first. A patient could get a vaccine that doesn't work, so we call impact four. It has already happened twice, so likelihood is three. Four times three gives twelve. Honestly, the number alone doesn't tell you what to do. The band for twelve comes from our corporate matrix, which Risk is still confirming. Then choose a response that lowers the risk, such as a weekly checklist with a second check. Treat those controls as teaching examples until Quality and Risk approve them.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | No scored action; work steps are readable in order and the self-explanation prompt can be skipped. |
| Not colour-only | Impact, likelihood and score are written as numbers and labels; matrix bands must use text as well as approved colour. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed; self-explanation has no timer. |

#### 7. Build fields (edumints)

```json
{
  "type": "worked_example",
  "id": "qsr-031",
  "title": "Score a risk",
  "section": "D · Risk management",
  "node_id": "qsr-sD",
  "objective_ids": [],
  "points": 0,
  "intro_html": "<p><strong>Hypothetical case only—not a My Clinic event.</strong> Expired stock is found twice in a fictional clinic refrigerator. Risk lifecycle: identify → assess → manage → monitor → report.</p>",
  "steps": [
    {
      "action_html": "Set impact to <strong>4</strong>.",
      "rationale_html": "For this hypothetical exercise, the possible consequence is a product that may not work as intended."
    },
    {
      "action_html": "Set likelihood to <strong>3</strong>.",
      "rationale_html": "This is a teaching input, not a measured local incident rate."
    },
    {
      "action_html": "Multiply: <strong>4 × 3 = 12</strong>.",
      "rationale_html": "The source defines the numeric score as impact multiplied by likelihood on a 1-to-5 scale."
    },
    {
      "action_html": "Look up score <strong>12</strong> on the corporate matrix.",
      "rationale_html": "Use the confirmed band name and threshold; do not infer them. ⚠ PENDING B6.",
      "artifact_asset_id": "<qsr-img-matrix>",
      "artifact_caption": "Corporate risk matrix; exact bands and colours pending B6."
    },
    {
      "action_html": "Compare the draft response labels: <strong>Reduce · Transfer · Accept · Avoid</strong>. ⚠ PENDING B7",
      "rationale_html": "Use only the response terms and approval conditions confirmed by the Risk Manager. ⚠ PENDING B7"
    }
  ],
  "fading": "partial",
  "self_explanation_prompt_html": "<p>What control could reduce impact or likelihood in this hypothetical case? This is an unscored reflection.</p>",
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-031>",
  "notes": "Companion: Dr. Omar, char-omar-thinking, L3 right column half-body (alt: Dr. Omar, the family physician, with his hand at his chin, thinking through the risk score.). Speaker: Omar.",
  "narration_text": "Omar: Let's score one together. It's a made-up case: expired items turn up twice this month in a clinic fridge. Impact first. A patient could get a vaccine that doesn't work, so we call impact four. It has already happened twice, so likelihood is three. Four times three gives twelve. Honestly, the number alone doesn't tell you what to do. The band for twelve comes from our corporate matrix, which Risk is still confirming. Then choose a response that lowers the risk, such as a weekly checklist with a second check. Treat those controls as teaching examples until Quality and Risk approve them."
}
```

#### 8. Notes for SME and developer

- Open questions: B6: Risk Manager supplies exact 1–25 matrix bands and colours. B7: Risk Manager confirms response names/conditions. The scenario and values are labelled hypothetical so they cannot be read as observed clinic data.
- Developer notes: Do not produce the final matrix, assign a band to score 12, or ship response guidance until B6/B7 close. Keep the SVG text selectable/readable and never rely on colour alone.


### `qsr-032` — Calculate the risk score

**Status:** `Draft — ready for SME review` · **Section / node:** D · Risk management / `qsr-sD` · **Type:** `fill_blank` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: multiply impact by likelihood and read the resulting band from the approved matrix. |
| Objective(s) | `qsr-o3` — score a risk on the 5×5 matrix. |
| On-the-job action | A4 — score a risk and propose a response. |
| Source | Source video, 05:20 (1–25 impact × likelihood); Phase 2 practice item. |
| Depends on Phase 0 | B6 — band names and score thresholds are open. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Calculate the risk score |
| Body / keywords | Impact 5 × likelihood 2 = ___ · Band: ___ ⚠ PENDING B6 |
| Word count (excl. title) | 7 |
| Instruction | Enter the numeric score and the matching band from the approved risk matrix. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | A large equation with two labelled blanks sits above a small matrix preview; the band field stays visibly blocked pending B6. |
| edumints layout | n/a (`fill_blank`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | No imagery; the multiplication sign and blank labels are text. |
| Animation / reveal | None. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | Impact 5 × likelihood 2 = score · risk band = band name |
| Correct answer(s) | Numeric: `10` (accept `10.0`); band: deliberately not authored until B6 closes. |
| Accepted variants | `score`: `10`, `10.0` · `band`: empty in draft and build-blocking until B6 confirms the approved label. |
| Points | 5 |
| Feedback — correct | 5 × 2 = 10. Read the band from the approved matrix. ⚠ PENDING B6. |
| Feedback — incorrect | Multiply impact by likelihood; do not guess the band. The approved range is pending B6. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 18 spoken words / ≈ 7.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Calculate the score from the impact and likelihood values, then use the confirmed matrix to supply its band.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Two explicitly labelled text inputs; accept keyboard entry and announce validation textually. |
| Not colour-only | The band must include its written label; no colour-only score field. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "fill_blank",
  "id": "qsr-032",
  "title": "Calculate the risk score",
  "section": "D · Risk management",
  "node_id": "qsr-sD",
  "objective_ids": [
    "qsr-o3"
  ],
  "evidence_screen_ids": [
    "qsr-031"
  ],
  "points": 5,
  "prompt_html": "<p>Impact 5 × likelihood 2 = <strong>[score]</strong>. Risk band = <strong>[band]</strong> ⚠ PENDING B6.</p>",
  "blanks": [
    {
      "id": "score",
      "accepted": [
        "10",
        "10.0"
      ]
    },
    {
      "id": "band",
      "accepted": []
    }
  ],
  "case_sensitive": false,
  "feedback": {
    "correct_html": "<p>5 × 2 = 10. Read the band from the approved matrix. ⚠ PENDING B6.</p>",
    "incorrect_html": "<p>Multiply impact by likelihood; do not guess the band. The approved range is pending B6.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-032>",
  "narration_text": "Noor: Calculate the score from the impact and likelihood values, then use the confirmed matrix to supply its band."
}
```

#### 8. Notes for SME and developer

- Open questions: B6 is build-blocking: the second blank has no accepted values until the Risk Manager supplies approved band labels and thresholds.
- Developer notes: Do not release with an empty accepted list; populate all approved band spelling variants after B6. Keep the first blank’s integer/decimal variants.


### `qsr-033` — Choose the risk response

**Status:** `Draft — ready for SME review` · **Section / node:** D · Risk management / `qsr-sD` · **Type:** `matching` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: distinguish the four proposed risk responses by the action they describe. |
| Objective(s) | `qsr-o3` — choose an appropriate risk response. |
| On-the-job action | A4 — score a risk and propose a response. |
| Source | Source video, 05:50–06:25; Phase 2 response examples. |
| Depends on Phase 0 | B7 — confirm approved terms and approval conditions. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Choose the risk response |
| Body / keywords | Reduce · Transfer · Accept · Avoid — wording ⚠ PENDING B7 |
| Word count (excl. title) | 7 |
| Instruction | Match each response with the action it describes. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Four response names appear in one column and four action cards in another; no response is distinguished by colour. |
| edumints layout | n/a (`matching`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | None; plain text keeps distinctions available to screen readers. |
| Animation / reveal | None. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Pairs | `reduce` Reduce → Add a second-check control to lower likelihood · `transfer` Transfer → Transfer financial exposure to an insurer · `accept` Accept → Leadership reviews and approves continued exposure · `avoid` Avoid → Do not start the risk-creating activity (all ⚠ PENDING B7) |
| Correct answer(s) | Each response maps to its action above. |
| Points | 10 |
| Feedback — correct | Correct: responses either control, transfer, formally accept or avoid exposure; confirm policy labels and conditions. |
| Feedback — incorrect | Re-read the action: lower exposure, pass it to a third party, approve living with it, or stop the activity. ⚠ PENDING B7 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 19 spoken words / ≈ 8.1 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Match each risk response with the action it describes. Use the policy-approved terms once confirmed, then check your reasoning.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Keyboard-accessible match controls; provide an alternative select list for each response. |
| Not colour-only | Each response and action is written in text; matching is not conveyed by hue. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "matching",
  "id": "qsr-033",
  "title": "Choose the risk response",
  "section": "D · Risk management",
  "node_id": "qsr-sD",
  "objective_ids": [
    "qsr-o3"
  ],
  "evidence_screen_ids": [
    "qsr-031"
  ],
  "points": 10,
  "prompt_html": "<p>Match each risk response with the action it describes. ⚠ PENDING B7.</p>",
  "pairs": [
    {
      "id": "reduce",
      "left_html": "Reduce / mitigate ⚠ PENDING B7",
      "right_html": "Add a second-check control to lower likelihood."
    },
    {
      "id": "transfer",
      "left_html": "Transfer ⚠ PENDING B7",
      "right_html": "Transfer financial exposure to an insurer."
    },
    {
      "id": "accept",
      "left_html": "Accept ⚠ PENDING B7",
      "right_html": "Leadership reviews and approves continued exposure."
    },
    {
      "id": "avoid",
      "left_html": "Avoid ⚠ PENDING B7",
      "right_html": "Do not start the risk-creating activity."
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> Responses control, transfer, formally accept or avoid exposure. Confirm policy labels and conditions. ⚠ PENDING B7</p>",
    "incorrect_html": "<p>Re-read each action: lower exposure, transfer it, approve living with it, or stop the activity.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-033>",
  "narration_text": "Noor: Match each risk response with the action it describes. Use the policy-approved terms once confirmed, then check your reasoning."
}
```

#### 8. Notes for SME and developer

- Open questions: B7: Risk Manager to confirm “reduce/mitigate”, transfer, accept/approval, and avoid terminology and conditions.
- Developer notes: Phase 2 uses “Reduce”; the source pass also says “mitigate”. Do not silently standardise until B7 closes.


### `qsr-040` — The safety iceberg

**Status:** `Draft — ready for SME review` · **Section / node:** E · Incidents / `qsr-sE` · **Type:** `labeled_diagram` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: show the source’s iceberg metaphor for event visibility and distinguish the draft event categories. |
| Objective(s) | — (teaches `qsr-o4`; assessed at `qsr-041` and `qsr-042`). |
| On-the-job action | A5 — classify an event correctly. |
| Source | Source video, 06:25–07:20 (iceberg, non-punitive culture, critical/sentinel wording). |
| Depends on Phase 0 | B1 (listen) and B8 (critical incident vs sentinel event, adverse event and near-miss definitions/examples). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | The safety iceberg |
| Body / keywords | Critical / sentinel event · Adverse event · Near miss — terms ⚠ PENDING B8 |
| Word count (excl. title) | 10 (+ 19-word tip card) |
| Instruction | n/a (display diagram). |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | A simple iceberg fills the right two-thirds with one labelled tip, one waterline layer and one larger submerged area, each category attached to both a label and a location; Omar's tip card (56 px avatar, teal ring, 4 px teal left edge, label “Omar's tip”) sits bottom-left, clear of the diagram labels. |
| edumints layout | n/a (`labeled_diagram`, `mode: "display"`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings navy `#003867` · body ink `#1F2A37` · Caring purple `#652D8C` for connector lines · all category names are text; category thresholds remain ⚠ PENDING B8. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None (never behind body content). |
| Icons | Own SVG iceberg silhouette with line callouts; no emoji or colour-only bands. |
| Animation / reveal | Labels reveal from top to bottom; respect reduced-motion preferences. |
| Companion | Dr. Omar · pose `char-omar-avatar-neutral` + tip card · placement L3 tip card bottom-left: 56 px avatar with a 3 px teal `#008C99` ring, white card max 360 px wide with a 4 px teal left edge, label “Omar's tip” · tip text (19 words, differs from the narration): “Caught it before it reached the patient? Report it anyway. It costs nothing and protects the next person.” |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `qsr-img-iceberg` | svg | Own 1600×900 SVG draft ([`assets/qsr-img-iceberg.svg`](assets/qsr-img-iceberg.svg)): iceberg with tip, below-waterline and deep layers, separate real-text callouts; terms pending B8; callout anchors match the build labels. | own | Iceberg with three labelled positions for critical or sentinel events, adverse events and near misses; exact terms are pending B8. | No |
| `char-omar-avatar-neutral` | character | Shared programme companion pose (preview: `00_program/characters/previews/char-omar-avatar-neutral.jpg`); 56 px circular avatar on the tip card, teal ring, bottom-left. | ai-generated programme asset, Canva media `MAHX-nPHDkA`, made from the approved master (companions.md §3); no module prompt | Dr. Omar, the family physician. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Layers | `critical` Tip — critical incident / sentinel event ⚠ PENDING B8 · `adverse` Below waterline — adverse event with harm ⚠ PENDING B8 · `near_miss` Submerged — failure caught before harm ⚠ PENDING B8 |
| Correct answer(s) | n/a (static display) |
| Points | 0 |
| Culture note | Source describes an open, non-punitive reporting culture; final terms and scope ⚠ PENDING B8. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | OMAR |
| Tone | Serious, reassuring |
| Target seconds | 35 |
| Word count / est. seconds | 69 spoken words / ≈ 29.6 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> OMAR: Picture an iceberg. At the tip are the most serious events, the ones everyone hears about. Just below the waterline are events that reach a patient and cause harm. The biggest part sits deep down: near misses, caught before any harm. Here's what helped me. I treat every near miss as a free lesson about a weak process. The exact terms and examples are still being confirmed by Risk.

Companion note: Tip-card text summarises; the spoken line explains (companions.md §4).

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | No interaction; labels and descriptions appear in reading order in HTML, not only on the SVG. |
| Not colour-only | Depth/position, category names and concise text describe each layer; colour is not required to distinguish categories. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "labeled_diagram",
  "id": "qsr-040",
  "title": "The safety iceberg",
  "section": "E · Incidents",
  "node_id": "qsr-sE",
  "objective_ids": [],
  "points": 0,
  "image_asset_id": "<qsr-img-iceberg>",
  "image_alt": "Iceberg with three labelled positions for critical or sentinel events, adverse events and near misses; exact terms are pending B8.",
  "prompt_html": "<p>Event names and definitions are draft pending incident-policy confirmation. ⚠ PENDING B8</p>",
  "mode": "display",
  "labels": [
    {
      "id": "critical",
      "text": "Critical incident / sentinel event ⚠ PENDING B8",
      "x": 560,
      "y": 215
    },
    {
      "id": "adverse",
      "text": "Adverse event — harm reached a person ⚠ PENDING B8",
      "x": 560,
      "y": 430
    },
    {
      "id": "near-miss",
      "text": "Near miss — caught before harm ⚠ PENDING B8",
      "x": 560,
      "y": 720
    }
  ],
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-040>",
  "feedback": {
    "correct_html": "<p>The diagram separates the draft event categories by position; final names and definitions remain pending B8.</p>",
    "incorrect_html": "<p>Review the three labelled layers and confirm their definitions with the policy owner.</p>",
    "show_correct_answer": true
  },
  "notes": "Companion: Dr. Omar tip card bottom-left — char-omar-avatar-neutral, label \"Omar's tip\": Caught it before it reached the patient? Report it anyway. It costs nothing and protects the next person. Speaker: Omar.",
  "narration_text": "Omar: Picture an iceberg. At the tip are the most serious events, the ones everyone hears about. Just below the waterline are events that reach a patient and cause harm. The biggest part sits deep down: near misses, caught before any harm. Here's what helped me. I treat every near miss as a free lesson about a weak process. The exact terms and examples are still being confirmed by Risk."
}
```

#### 8. Notes for SME and developer

- Open questions: B8: Risk Manager confirms event names, definitions, examples and whether “critical incident” or “sentinel event” is used. Do not ship either as a settled term before confirmation.
- Developer notes: Own SVG only. Use text labels and position as redundant cues; keep the iceberg metaphor visually neutral and non-graphic.


### `qsr-041` — Classify the event

**Status:** `Draft — ready for SME review` · **Section / node:** E · Incidents / `qsr-sE` · **Type:** `drag_drop` · **Scored:** Yes (10 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: distinguish draft critical/sentinel events, adverse events and near misses. |
| Objective(s) | `qsr-o4` — distinguish event classes within a just culture. |
| On-the-job action | A5 — classify an event correctly. |
| Source | Source video, 06:25–07:20; examples are Phase 2 practice cases. |
| Depends on Phase 0 | B1 and B8 — event definitions, terms, thresholds and examples. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Classify the event |
| Body / keywords | Critical / sentinel · Adverse · Near miss ⚠ PENDING B8 |
| Word count (excl. title) | 7 |
| Instruction | Classify each fictional event by what happened and whether harm reached a person. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Six short event cards sit above three labelled target columns; the full event text stays visible while moving. |
| edumints layout | n/a (`drag_drop`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | None; category targets use headings and text rather than coloured bands. |
| Animation / reveal | None. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | `wrong_site` Wrong-site procedure → Critical / sentinel ⚠ PENDING B8 · `abduction` Infant abduction → Critical / sentinel ⚠ PENDING B8 · `fall` Patient falls and needs stitches → Adverse ⚠ PENDING B8 · `rash` Wrong drug given; mild rash → Adverse ⚠ PENDING B8 · `caught_drug` Wrong drug prepared but caught before giving → Near miss ⚠ PENDING B8 · `sample` Lab sample has wrong name; caught at lab desk → Near miss ⚠ PENDING B8 |
| Targets | `critical` Critical / sentinel event · `adverse` Adverse event · `near_miss` Near miss |
| Points | 10 |
| Feedback — correct | Correct: classify by the event’s consequence and whether it was caught before reaching the person; final terms remain pending B8. |
| Feedback — incorrect | Ask what happened, whether harm reached a person, and whether the failure was caught in time. Confirm definitions with policy. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Serious, neutral |
| Target seconds | 8 |
| Word count / est. seconds | 20 spoken words / ≈ 8.6 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Classify each fictional event by what happened and whether harm reached the person. The labels remain subject to policy confirmation.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Keyboard pick-and-place targets; a select-list alternative is available for every item. |
| Not colour-only | Target names are written; feedback describes consequence and interception, not only a colour. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "drag_drop",
  "id": "qsr-041",
  "title": "Classify the event",
  "section": "E · Incidents",
  "node_id": "qsr-sE",
  "objective_ids": [
    "qsr-o4"
  ],
  "evidence_screen_ids": [
    "qsr-040"
  ],
  "points": 10,
  "prompt_html": "<p>Classify each fictional event by what happened and whether harm reached a person. ⚠ PENDING B8.</p>",
  "items": [
    {
      "id": "wrong_site",
      "text_html": "Wrong-site procedure ⚠ PENDING B8",
      "correct_target_id": "critical"
    },
    {
      "id": "abduction",
      "text_html": "Infant abduction ⚠ PENDING B8",
      "correct_target_id": "critical"
    },
    {
      "id": "fall",
      "text_html": "Patient falls and needs stitches ⚠ PENDING B8",
      "correct_target_id": "adverse"
    },
    {
      "id": "rash",
      "text_html": "Wrong drug given; mild rash ⚠ PENDING B8",
      "correct_target_id": "adverse"
    },
    {
      "id": "caught_drug",
      "text_html": "Wrong drug prepared but caught before giving ⚠ PENDING B8",
      "correct_target_id": "near_miss"
    },
    {
      "id": "sample",
      "text_html": "Lab sample has wrong name; caught at lab desk ⚠ PENDING B8",
      "correct_target_id": "near_miss"
    }
  ],
  "targets": [
    {
      "id": "critical",
      "label_html": "Critical / sentinel event ⚠ PENDING B8"
    },
    {
      "id": "adverse",
      "label_html": "Adverse event ⚠ PENDING B8"
    },
    {
      "id": "near_miss",
      "label_html": "Near miss ⚠ PENDING B8"
    }
  ],
  "feedback": {
    "correct_html": "<p><strong>Correct.</strong> Consider the event’s consequence and whether it was caught before reaching the person. Final definitions remain pending B8.</p>",
    "incorrect_html": "<p>Ask what happened, whether harm reached a person, and whether the failure was caught in time. Confirm the terms with policy.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-041>",
  "narration_text": "Noor: Classify each fictional event by what happened and whether harm reached the person. The labels remain subject to policy confirmation."
}
```

#### 8. Notes for SME and developer

- Open questions: B8 is build-blocking for the event labels and examples. Every scenario item is a fictional practice case, not a My Clinic incident.
- Developer notes: Check that the actual policy accepts each example under its target class. Keyboard and select-list alternatives are required.


### `qsr-042` — A just culture?

**Status:** `Draft — ready for SME review` · **Section / node:** E · Incidents / `qsr-sE` · **Type:** `true_false` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: recognise the source’s draft non-punitive reporting principle without promising immunity from policy. |
| Objective(s) | `qsr-o4` — distinguish event classes within a just culture. |
| On-the-job action | A6 — report within the approved time and channel without fear of blame. |
| Source | Source video, 06:25–07:00; source frames describe an open, non-punitive culture. |
| Depends on Phase 0 | B8 — confirm event policy wording and just-culture scope. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | A just culture? |
| Body / keywords | “If you report a near miss you caused, you will be disciplined.” ⚠ PENDING B8 |
| Word count (excl. title) | 14 |
| Instruction | Decide whether the statement matches the policy-approved reporting culture. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | One large statement sits above two equal True/False cards; neither option is preselected. |
| edumints layout | n/a (`true_false`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | Feedback uses a check or caution icon from the shared line family, with words. |
| Animation / reveal | Feedback banner appears after submission; no motion is required. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Statement | “If you report a near miss you caused, you will be disciplined.” ⚠ PENDING B8 |
| Correct answer | False in the Phase 2 draft; final just-culture wording is pending B8. |
| Points | 5 |
| Feedback — correct | Correct for the draft: the source describes an open, non-punitive culture and says reports are not used to criticise staff. Confirm limits and wording with policy. ⚠ PENDING B8 |
| Feedback — incorrect | The source’s draft message is non-punitive reporting; verify how the current policy defines accountability. ⚠ PENDING B8 |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Reassuring, careful |
| Target seconds | 8 |
| Word count / est. seconds | 19 spoken words / ≈ 8.1 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Consider the statement carefully. Decide whether it reflects the open, non-punitive culture described in the source, pending policy confirmation.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | True and False are native, labelled controls; both are reachable by keyboard. |
| Not colour-only | The statement and choices use words; answer feedback also includes an icon and explanation. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "true_false",
  "id": "qsr-042",
  "title": "A just culture?",
  "section": "E · Incidents",
  "node_id": "qsr-sE",
  "objective_ids": [
    "qsr-o4"
  ],
  "evidence_screen_ids": [
    "qsr-040"
  ],
  "points": 5,
  "prompt_html": "<p>If you report a near miss you caused, you will be disciplined. ⚠ PENDING B8</p>",
  "correct": false,
  "feedback": {
    "correct_html": "<p><strong>Correct for the draft.</strong> The source describes an open, non-punitive culture and says reports are not used to criticise staff. Confirm policy limits and wording. ⚠ PENDING B8</p>",
    "incorrect_html": "<p>The source’s draft message is non-punitive reporting. Verify how the current policy defines accountability. ⚠ PENDING B8</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-042>",
  "narration_text": "Noor: Consider the statement carefully. Decide whether it reflects the open, non-punitive culture described in the source, pending policy confirmation."
}
```

#### 8. Notes for SME and developer

- Open questions: B8: Risk Manager must confirm the just-culture policy and whether/how accountability is addressed. Avoid an absolute promise of immunity.
- Developer notes: Do not ship as a guarantee that an employee will never face discipline; align the exact item and feedback to approved policy.


### `qsr-050` — Report an event

**Status:** `Draft — ready for SME review` · **Section / node:** F · Reporting / `qsr-sF` · **Type:** `content_slide` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: identify reportable clinical and non-clinical examples, draft timing, reporting route and follow-up. |
| Objective(s) | — (teaches `qsr-o5`; assessed at `qsr-051`). |
| On-the-job action | A6 — report within the approved time and channel. |
| Source | Source video, 07:30–08:40; the reporting workflow frame at 08:00. |
| Depends on Phase 0 | B1, B9 (window, channel, severity escalation) and D8 (cross-module 24-hour consistency). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Report an event |
| Body / keywords | Report: clinical + non-clinical events · When: 24 hours ⚠ PENDING B9/D8 · Where: digital form or email ⚠ PENDING B9 · System review follows |
| Word count (excl. title) | 20 |
| Instruction | Read the draft workflow; use only the confirmed channel and timing at work. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L3 Content (see `../../00_program/brand/screen-mockups/03-content.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | Three white cards group reportable examples, when/where to submit, and what happens next; the 24-hour line is a magenta callout marked pending. |
| edumints layout | `text` (`content_slide` with three text blocks). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · reporting-rule callout Responsible magenta `#9D3293` with pending words. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; body Montserrat Regular 400, 16 px (14 px minimum); labels Montserrat Bold 700, 11–14 px; footer 10–12 px. |
| Watermark | None (never behind body content). |
| Icons | Three own line icons in navy: clinical care, facility/equipment, reporting workflow; icons supplement, not replace, the text. |
| Animation / reveal | Cards reveal in reading order; pending time/channel callouts remain visible. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

n/a — unscored content screen. The reporting rule and channel are pending policy approval.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Clear, practical |
| Target seconds | 35 |
| Word count / est. seconds | 75 spoken words / ≈ 32.1 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Reportable events include clinical concerns and problems affecting facilities, equipment, laboratories, fire safety or security. The source describes a digital report through the intranet or by email, followed by review, grading and escalation. The exact reporting channel and time limit require confirmation. The current draft shows a 24-hour window. Do not rely on it until the policy owner confirms it and aligns the wording with Module 03. Add factual details and immediate actions, not assumptions.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | No interaction; all three content blocks are read in a logical order. |
| Not colour-only | The “When” and “Where” callouts use explicit text and a ⚠ icon; red/magenta is not the only status cue. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "content_slide",
  "id": "qsr-050",
  "title": "Report an event",
  "section": "F · Reporting",
  "node_id": "qsr-sF",
  "objective_ids": [],
  "points": 0,
  "body_html": "",
  "layout": "text",
  "blocks": [
    {
      "html": "<p><strong>What to report</strong></p><p>Clinical: medication errors, falls. Non-clinical: system downtime, equipment failure, lab issues, fire hazards and security breaches.</p>"
    },
    {
      "html": "<p><strong>When</strong></p><p>Within 24 hours in the source draft. ⚠ PENDING B9 / D8</p>"
    },
    {
      "html": "<p><strong>Where and what follows</strong></p><p>Digital intranet form or email in the source draft. The system grades, escalates and analyses reports. Channel confirmation ⚠ PENDING B9.</p>"
    }
  ],
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-050>",
  "narration_text": "Noor: Reportable events include clinical concerns and problems affecting facilities, equipment, laboratories, fire safety or security. The source describes a digital report through the intranet or by email, followed by review, grading and escalation. The exact reporting channel and time limit require confirmation. The current draft shows a 24-hour window. Do not rely on it until the policy owner confirms it and aligns the wording with Module 03. Add factual details and immediate actions, not assumptions."
}
```

#### 8. Notes for SME and developer

- Open questions: B9 and D8: Risk Manager confirms current time window, channel name, severity escalation language and cross-module wording with module 03. Do not use a live URL until it is supplied.
- Developer notes: No source-video frames, watermark or original voice are reused (D7 recommendation). Build cards as real HTML text, not text baked into illustrations.


### `qsr-051` — End-of-shift near miss

**Status:** `Draft — ready for SME review` · **Section / node:** F · Reporting / `qsr-sF` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: decide whether, when and where to report a fictional near miss at the end of a tiring shift. |
| Objective(s) | `qsr-o5` — report an incident through the correct channel within the approved period. |
| On-the-job action | A6 — report within the approved time and channel without fear of blame. |
| Source | Source video, 07:30–08:40; Phase 2 end-of-shift scenario. The scenario is fictional. |
| Depends on Phase 0 | B1, B8 (near-miss classification), B9 (channel/window) and D8 (24-hour cross-module consistency). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | End-of-shift near miss |
| Body / keywords | Fictional near miss · Choose whether, when and where to report · ⚠ PENDING B8/B9/D8 |
| Word count (excl. title) | 14 |
| Instruction | Choose a safe next step at each node, then select a timing and channel. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L5 Scenario (see `../../00_program/brand/screen-mockups/05-scenario.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | A 19:00 end-of-shift situation card sits on the left with Noor's 56 px scenario avatar (purple ring, “Noor · Safety liaison”) above it; her avatar starts neutral and changes to happy or concern after each choice; each decision stays on the right in large buttons. |
| edumints layout | n/a (`decision_scenario`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · feedback success `#1E7B4F` / error `#B42318` with icon + explanatory words. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; situation Montserrat SemiBold 600, 17 px; choices/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (scenario screens have no watermark). |
| Icons | No extra icons; a clock label “19:00” is HTML text and not encoded in an image. |
| Animation / reveal | Node text fades between choices; provide a reduced-motion setting. |
| Companion | Noor · pose `char-noor-avatar-neutral` on the intro → `char-noor-avatar-happy` after a best choice / `-avatar-concern` after an unsafe one · placement L5 scenario avatar, 56 px with a 3 px purple `#652D8C` ring and “Noor · Safety liaison” above the situation · tip text n/a |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `char-noor-avatar-neutral` | character | Shared programme companion pose (preview: `00_program/characters/previews/char-noor-avatar-neutral.jpg`); 56 px circular scenario avatar, purple ring, above the situation. | ai-generated programme asset, Canva media `MAHX-n4HuyU`, made from the approved master (companions.md §3); no module prompt | Noor, the safety liaison. | No |
| `char-noor-avatar-happy` | character | Shared programme companion avatar, cropped to a circle; 56 px circular scenario avatar, purple ring, above the situation. | programme asset to make: crop from `char-noor-success` (MAHX-jiR90M) (companions.md §3); no module prompt | Noor, the safety liaison, smiling. | No |
| `char-noor-avatar-concern` | character | Shared programme companion avatar, cropped to a circle; 56 px circular scenario avatar, purple ring, above the situation. | programme asset to make: crop from `char-noor-concern` (MAHX-hFE0aQ) (companions.md §3); no module prompt | Noor, the safety liaison, looking concerned. | No |


No AI image prompt: this card uses only the shared programme companion avatars (`char-noor-*`, companions.md §3).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Intro | Fictional 19:00 shift-end scenario: earlier, you caught a colleague about to give insulin to the wrong patient. No one was harmed. |
| Nodes | `n1` report or not · `n2` timing · `n3` approved channel and factual description |
| Correct answer(s) | `n1-a` report the near miss ⚠ PENDING B8 · `n2-a` submit within the approved window (draft says within 24 hours) ⚠ PENDING B9/D8 · `n3-a` use the confirmed digital channel/email and record facts, not blame ⚠ PENDING B9 |
| Points / pass rule | 15 points · `pass_score: 3` of 3 best decisions (all best) |
| Per-choice feedback | Every choice explains why reporting, timing and channel matter; no blame language. |
| Retry | Replay without inflating the final score. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Serious, supportive |
| Target seconds | 15 |
| Word count / est. seconds | 38 spoken words / ≈ 16.3 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: A fictional near miss happened near the end of a tiring shift. No one was harmed, but the risk was real. Choose what to do next, then decide when and where the report belongs under the confirmed policy.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Three node choices use focusable buttons; no time limit, drag action or pointer-only control. |
| Not colour-only | Each choice and result has explanatory text and an icon; no status is conveyed by red/green alone. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "decision_scenario",
  "id": "qsr-051",
  "title": "End-of-shift near miss",
  "section": "F · Reporting",
  "node_id": "qsr-sF",
  "objective_ids": [
    "qsr-o5"
  ],
  "evidence_screen_ids": [
    "qsr-050"
  ],
  "points": 15,
  "pass_score": 3,
  "start_node_id": "n1",
  "intro_html": "<p>Fictional 19:00 shift-end scenario: earlier, you caught a colleague about to give insulin to the wrong patient. No one was harmed.</p>",
  "nodes": [
    {
      "id": "n1",
      "prompt_html": "<p>No patient was harmed. What should happen next?</p>",
      "choices": [
        {
          "id": "a",
          "text_html": "Report the near miss through the approved process. ⚠ PENDING B8",
          "score_delta": 1,
          "goto_node_id": "n2",
          "feedback_html": "<p><strong>Best choice in the draft.</strong> Reporting a near miss can reveal a weak process before harm occurs. Confirm the event policy. ⚠ PENDING B8</p>"
        },
        {
          "id": "b",
          "text_html": "Do not report because no harm occurred.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>The source describes reporting near misses; confirm the final definition and process with policy. ⚠ PENDING B8</p>"
        },
        {
          "id": "c",
          "text_html": "Wait to see whether the same problem happens again.",
          "score_delta": 0,
          "goto_node_id": "n2",
          "feedback_html": "<p>Waiting leaves the possible system weakness unreported. Use the confirmed process. ⚠ PENDING B8</p>"
        }
      ]
    },
    {
      "id": "n2",
      "prompt_html": "<p>When should you submit the report?</p>",
      "choices": [
        {
          "id": "a",
          "text_html": "Within the confirmed reporting window; the draft says within 24 hours. ⚠ PENDING B9/D8",
          "score_delta": 1,
          "goto_node_id": "n3",
          "feedback_html": "<p><strong>Best choice in the draft.</strong> The current draft says within 24 hours; use the final policy window once confirmed. ⚠ PENDING B9/D8</p>"
        },
        {
          "id": "b",
          "text_html": "Next week, when the shift is quieter.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>Delay may exceed the approved window. Submit within the confirmed time limit. ⚠ PENDING B9/D8</p>"
        },
        {
          "id": "c",
          "text_html": "Only if someone was harmed.",
          "score_delta": 0,
          "goto_node_id": "n3",
          "feedback_html": "<p>The draft includes near misses; confirm reportability in the current policy. ⚠ PENDING B8/B9</p>"
        }
      ]
    },
    {
      "id": "n3",
      "prompt_html": "<p>Which channel and description should you use?</p>",
      "choices": [
        {
          "id": "a",
          "text_html": "Use the confirmed digital channel or email and record factual details, not blame. ⚠ PENDING B9",
          "score_delta": 1,
          "goto_node_id": null,
          "feedback_html": "<p><strong>Best choice in the draft.</strong> Use the approved channel and record facts and immediate actions. Confirm the channel before release. ⚠ PENDING B9</p>"
        },
        {
          "id": "b",
          "text_html": "Tell one colleague only and leave no report.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>A private conversation does not replace the approved reporting process. ⚠ PENDING B9</p>"
        },
        {
          "id": "c",
          "text_html": "Write assumptions about the colleague’s intent.",
          "score_delta": 0,
          "goto_node_id": null,
          "feedback_html": "<p>Record observable facts and immediate actions, not assumptions or blame. Use the approved channel. ⚠ PENDING B9</p>"
        }
      ]
    }
  ],
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-051>",
  "feedback": {
    "correct_html": "<p>Review the confirmed reporting workflow and submit facts through the approved channel.</p>",
    "incorrect_html": "<p>Revisit the approved incident-reporting procedure and the current time window.</p>",
    "show_correct_answer": true
  },
  "notes": "Companion: Noor L5 scenario avatar above the situation — char-noor-avatar-neutral on intro, char-noor-avatar-happy / char-noor-avatar-concern after each choice. Speaker: Noor.",
  "narration_text": "Noor: A fictional near miss happened near the end of a tiring shift. No one was harmed, but the risk was real. Choose what to do next, then decide when and where the report belongs under the confirmed policy."
}
```

#### 8. Notes for SME and developer

- Open questions: B8/B9/D8: confirm near-miss reportability, the 24-hour window, official system/email channel and consistent wording with module 03 before release.
- Developer notes: All data and event details are fictional. Noor's avatar is L5 template chrome above the situation: `char-noor-avatar-neutral` on the intro, `-avatar-happy` after a best choice, `-avatar-concern` after an unsafe one; it never covers the choice buttons. The nodes carry no image; the 19:00 time and situation stay as HTML text. Companion art is the shared programme set — no module-specific character prompt.


### `qsr-090` — Your results

**Status:** `Draft — ready for SME review` · **Section / node:** G · Close / `qsr-sG` · **Type:** `results_breakdown` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close: show the learner’s score and performance by each of the five objectives. |
| Objective(s) | — (results screen for `qsr-o1`–`qsr-o5`). |
| On-the-job action | — |
| Source | `phase-1-action-map.md` §3 (objective register) and `phase-4-build.md` §3 (points/pass mark). |
| Depends on Phase 0 | None; objective advice text repeats pending-policy notes where relevant. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Your results |
| Body / keywords | Results by objective · Review any area below threshold |
| Word count (excl. title) | 8 |
| Instruction | Review your objective bars and any advice shown. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close (see `../../00_program/brand/screen-mockups/06-results.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header) |
| Visual concept | Five objective rows show a label, score bar and points earned; a navy score ring names PASSED or NOT YET in words. |
| edumints layout | n/a (`results_breakdown`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` · headings navy `#003867` · body ink `#1F2A37` · objective bars Caring purple `#652D8C` · weak result error `#B42318` with ⚠ and words. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; objective labels/body Montserrat Regular or Medium 400/500, 16 px; status chips Montserrat Bold 700, 12–14 px; footer 10–12 px. |
| Watermark | None on results; closing summary uses supplied `mark-navy.png` at 6–8% opacity, 440 px, cropped off the right edge. |
| Icons | A check icon for passed and warning icon for needs review; shared single-weight own line icons, never colour alone. |
| Animation / reveal | Bars grow from zero only when motion is allowed; reduce-motion shows final values immediately. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Sections | `qsr-o1`: qsr-011/qsr-012 · `qsr-o2`: qsr-021/qsr-022/qsr-023 · `qsr-o3`: qsr-030/qsr-032/qsr-033 · `qsr-o4`: qsr-041/qsr-042 · `qsr-o5`: qsr-051 |
| Weak threshold | 60% (edumints `results_breakdown` default; Quality SME may revise). |
| Pass mark | 80% overall = 76/95 points (`phase-4-build.md` §3). |
| Advice | Revisit the related explanation and approved policy before the next attempt; advice is objective-specific. |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Neutral, encouraging |
| Target seconds | 10 |
| Word count / est. seconds | 25 spoken words / ≈ 10.7 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Review your results by objective and notice where your choices were strongest. A lower result points to the topic to revisit before your next attempt.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Results are read in objective order; advice is in the same DOM order as its score row. |
| Not colour-only | PASSED / NOT YET and weak-objective wording accompany the ring, bars and status icons. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "results_breakdown",
  "id": "qsr-090",
  "title": "Your results",
  "section": "G · Close",
  "node_id": "qsr-sG",
  "objective_ids": [],
  "points": 0,
  "body_html": "<p>Passing score: 80% (76/95 points). Review the objective advice shown below.</p>",
  "sections": [
    {
      "title": "qsr-o1 · Quality measures and improvement cycle",
      "screen_ids": [
        "qsr-011",
        "qsr-012"
      ],
      "advice_html": "<p>Review the quality model and the confirmed improvement-cycle wording. ⚠ PENDING B11</p>"
    },
    {
      "title": "qsr-o2 · Patient-safety goals",
      "screen_ids": [
        "qsr-021",
        "qsr-022",
        "qsr-023"
      ],
      "advice_html": "<p>Review the approved identifier, goal and hand-hygiene guidance. ⚠ PENDING B3/B4/B5/B10</p>"
    },
    {
      "title": "qsr-o3 · Risk scoring and response",
      "screen_ids": [
        "qsr-030",
        "qsr-032",
        "qsr-033"
      ],
      "advice_html": "<p>Review the risk lifecycle, corporate matrix and approved response terms. ⚠ PENDING B6/B7</p>"
    },
    {
      "title": "qsr-o4 · Event classification and just culture",
      "screen_ids": [
        "qsr-041",
        "qsr-042"
      ],
      "advice_html": "<p>Review approved event definitions and reporting-culture wording. ⚠ PENDING B8</p>"
    },
    {
      "title": "qsr-o5 · Incident reporting",
      "screen_ids": [
        "qsr-051"
      ],
      "advice_html": "<p>Review the confirmed reporting window and channel. ⚠ PENDING B9/D8</p>"
    }
  ],
  "weak_threshold": 60,
  "show_total": true,
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-090>",
  "narration_text": "Noor: Review your results by objective and notice where your choices were strongest. A lower result points to the topic to revisit before your next attempt."
}
```

#### 8. Notes for SME and developer

- Open questions: None. The 60% objective-weak threshold is the screen-model default; confirm with the Quality SME if a different threshold is required.
- Developer notes: The overall pass mark remains 80% (76/95); objective-level advice is not a replacement for the package pass rule.


### `qsr-091` — Make a commitment

**Status:** `Draft — ready for SME review` · **Section / node:** G · Close / `qsr-sG` · **Type:** `poll` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Reflect: invite the learner to rehearse a sentence for a future safety concern; do not score it. |
| Objective(s) | — (supports `qsr-o5`). |
| On-the-job action | A6 — report within the approved time and channel. |
| Source | Phase 2 screen list; closing theme at 08:35. |
| Depends on Phase 0 | New open question `NEW-01` / D9: verify free-text storage/privacy before using an open response. |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Make a commitment |
| Body / keywords | What will you say the next time you notice something unsafe? |
| Word count (excl. title) | 11 |
| Instruction | Write a short sentence or continue without sharing. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L4 Question (see `../../00_program/brand/screen-mockups/04-question.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header), 2 px navy `#003867` rule |
| Visual concept | One open text field sits below the prompt; the screen shows a clear Skip option and a no-score note. |
| edumints layout | n/a (`poll`). |
| Colours (palette names + hex) | bg off-white `#F4F7FA` · cards white `#FFFFFF` with line `#D9E1E8` · stem navy `#003867` · body ink `#1F2A37` · highlight Caring purple `#652D8C` · correct `#1E7B4F` with ✓ + “Correct” · incorrect `#B42318` with an icon + words; never colour alone. |
| Typography (Montserrat) | Question label Montserrat Bold 700, 11–14 px; stem Montserrat SemiBold 600, 20–24 px; options/feedback Montserrat Regular or Medium 400/500, 16 px; footer 10–12 px. |
| Watermark | None (questions have no watermark). |
| Icons | None; text-only reflection. |
| Animation / reveal | Text field appears with no movement. |
| Companion | None — voice only (Noor narrates; no companion visible). |

**Imagery:** None for this interaction/content card; only the logo specified above is present.

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Prompt | “What will you say the next time you notice something unsafe?” |
| Response | Optional free text; no scored options. |
| Correct answer(s) | n/a — unscored commitment reflection |
| Points | 0 |
| Reflection | “Do not enter patient or staff identifying information. Storage/privacy behaviour ⚠ PENDING NEW-01 / D9.” |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR |
| Tone | Warm, practical |
| Target seconds | 8 |
| Word count / est. seconds | 19 spoken words / ≈ 8.1 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: Think of one calm sentence you could use if you noticed something unsafe. You may pass on sharing it.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Label the text field and Skip button; keyboard users can enter text or bypass the prompt. |
| Not colour-only | The prompt and Skip action are labelled in text; no visual distinction depends on colour. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed; response optional. |

#### 7. Build fields (edumints)

```json
{
  "type": "poll",
  "id": "qsr-091",
  "title": "Make a commitment",
  "section": "G · Close",
  "node_id": "qsr-sG",
  "objective_ids": [],
  "points": 0,
  "prompt_html": "<p>What will you say the next time you notice something unsafe?</p>",
  "options": [],
  "multi": false,
  "allow_text": true,
  "reflection_html": "<p>Do not enter patient or staff identifying information. Response storage/privacy behaviour is pending confirmation. ⚠ PENDING NEW-01 / D9.</p>",
  "reveal": "none",
  "narration_asset_id": "<qsr-aud-091>",
  "narration_text": "Noor: Think of one calm sentence you could use if you noticed something unsafe. You may pass on sharing it."
}
```

#### 8. Notes for SME and developer

- Open questions: NEW-01 / D9: verify whether a free-text poll is stored and whether it can be made non-persistent/anonymous. If privacy cannot be assured, replace with a non-collecting reflection prompt.
- Developer notes: Do not ask the learner to describe a real incident or name any person. Disable capture or confirm the required privacy controls before release.


### `qsr-092` — Ready to protect patients

**Status:** `Draft — ready for SME review` · **Section / node:** G · Close / `qsr-sG` · **Type:** `summary` · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Close: restate the practical skills, point to the approved policy and incident channel, and reinforce speaking up. |
| Objective(s) | — (closes `qsr-o1`–`qsr-o5`). |
| On-the-job action | — |
| Source | Source video closing at 08:35; links are placeholders pending approved policy locations. |
| Depends on Phase 0 | B1 (source phrase), B3 (IPSG policy link), B8 (event language), B9/D8 (incident-system link/window). |

#### 2. On-screen content

| Field | Value |
|---|---|
| Title | Ready to protect patients |
| Body / keywords | Measure quality · apply patient-safety goals · score risk and classify events · follow reporting workflow · approved links ⚠ PENDING B3/B9 |
| Word count (excl. title) | 18 |
| Instruction | Use the approved policy links and reporting channel after they are supplied. |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | L6 Results / close (see `../../00_program/brand/screen-mockups/06-results.png`) |
| Logo | `logo-horizontal-navy.png`, 30 px tall, header top-left (40 px from left, vertically centred in the 64 px header) |
| Visual concept | A four-item checklist sits beside two action cards for the approved incident system and IPSG policy; Noor (`char-noor-success`, thumbs up) stands half-body at the right with Dr. Omar's 56 px avatar (teal ring) beside his closing line; a faint petal watermark is cropped off the right edge behind Noor. |
| edumints layout | n/a (`summary`). |
| Colours (palette names + hex) | bg white `#FFFFFF` · headings navy `#003867` · body ink `#1F2A37` · Caring purple `#652D8C` for checklist ticks and action cards · magenta `#9D3293` only for pending rule callout. |
| Typography (Montserrat) | Screen title Montserrat Bold 700, 28–30 px; objective labels/body Montserrat Regular or Medium 400/500, 16 px; status chips Montserrat Bold 700, 12–14 px; footer 10–12 px. |
| Watermark | None on results; closing summary uses supplied `mark-navy.png` at 6–8% opacity, 440 px, cropped off the right edge. |
| Icons | Shared single-weight tick and link icons, navy/Caring purple, own SVG; each action card also has a text label. |
| Animation / reveal | Checklist ticks appear in order; action cards fade in last; reduced-motion displays all items at once. |
| Companion | Noor + Dr. Omar · poses `char-noor-success` + `char-omar-avatar-happy` · placement L6: Noor half-body 300–360 px at the right; Omar's 56 px avatar (3 px teal `#008C99` ring) beside his closing line · tip text n/a · two-voice close (2 turns, ≈ 19 s) |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `brand-mark-navy` | icon | Supplied five-petal watermark, 6–8% opacity, 440 px, cropped off right edge. | own (official My Clinic brand asset) | Decorative petal watermark. | Yes |
| `char-noor-success` | character | Shared programme companion pose (preview: `00_program/characters/previews/char-noor-success.jpg`); Noor half-body 300–360 px right; Omar 56 px avatar with teal ring. | ai-generated programme asset, Canva media `MAHX-jiR90M`, made from the approved master (companions.md §3); no module prompt | Noor, the safety liaison, smiling and giving a thumbs up. | No |
| `char-omar-avatar-happy` | character | Shared programme companion avatar, cropped to a circle; Noor half-body 300–360 px right; Omar 56 px avatar with teal ring. | programme asset to make: crop from `char-omar-success` (MAHX-llCU5M) (companions.md §3); no module prompt | Dr. Omar, the family physician, smiling. | No |

#### 4. Interaction and scoring

n/a — unscored summary screen.

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | NOOR / OMAR (two-voice close: `noor-1` → `omar-1`, joined with 0.3 s silence; 2 turns ≤ 45 s) |
| Tone | Warm, steady → Encouraging, firm |
| Target seconds | 20 (noor-1 13 · omar-1 7) |
| Word count / est. seconds | 43 spoken words / ≈ 18.4 s at 140 wpm (speaker tag excluded) |
| Cue targets | None |

> NOOR: You've practised measuring quality, checking identity, scoring risk and reporting what you notice. Some local details still await sign-off, so check the approved links before you rely on them.
>
> OMAR: And remember, you're the final layer of protection. When you see something, say something.

Companion note: “When you see something, say something” is the source-video line Phase 3 keeps as a quote; confirm it in the B1 listen before audio production.

New lexicon terms: None.

#### 6. Accessibility

| Field | Value |
|---|---|
| Keyboard | Summary and links follow one reading order; links are keyboard-accessible and visibly focused. |
| Not colour-only | Each checklist item and status is text plus an icon; action cards have full labels. |
| Captions / transcript | `narration_text` is present. |
| Timing | Untimed. |

#### 7. Build fields (edumints)

```json
{
  "type": "summary",
  "id": "qsr-092",
  "title": "Ready to protect patients",
  "section": "G · Close",
  "node_id": "qsr-sG",
  "objective_ids": [],
  "points": 0,
  "body_html": "<ul><li>Describe how quality is measured and improved.</li><li>Apply the approved patient-safety goals and verify identity.</li><li>Score a risk, choose an approved response and classify events.</li><li>Follow the confirmed incident-reporting workflow.</li></ul><p><strong>“When you see something, say something.” ⚠ PENDING B1</strong></p><p>Approved IPSG policy link ⚠ PENDING B3 · Approved incident-system link ⚠ PENDING B9.</p>",
  "show_score": true,
  "show_completion": true,
  "reveal": "auto",
  "narration_asset_id": "<qsr-aud-092>",
  "notes": "Companions: Noor char-noor-success half-body right + Dr. Omar char-omar-avatar-happy avatar. Two-voice close: noor-1 then omar-1, joined with 0.3 s silence into one file.",
  "narration_text": "Noor: You've practised measuring quality, checking identity, scoring risk and reporting what you notice. Some local details still await sign-off, so check the approved links before you rely on them. Omar: And remember, you're the final layer of protection. When you see something, say something."
}
```

#### 8. Notes for SME and developer

- Open questions: B1/B3/B8/B9/D8: confirm the closing phrase and replace the two generic policy destinations with approved URLs/locations. Do not invent links.
- Developer notes: Use the supplied navy logo in the header and mark-navy watermark only on this closing screen. Links remain placeholders until owners provide destinations.


---

## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | Speaker(s) | Companion visible | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---:|---|---|---:|---:|---:|---|
| 1 | `qsr-000` | `title_slide` | N | — | Noor | Noor | 9 | 30 | 12.9 | Draft |
| 2 | `qsr-001` | `content_slide` | N | — | Noor | — | 17 | 60 | 25.7 | Draft |
| 3 | `qsr-002` | `poll` | N | — | Noor | Noor | 17 | 24 | 10.3 | Draft |
| 4 | `qsr-010` | `labeled_diagram` | N | — | Noor | — | 12 | 77 | 33.0 | Draft |
| 5 | `qsr-011` | `drag_drop` | Y | 10 | Noor | — | 6 | 18 | 7.7 | Draft |
| 6 | `qsr-012` | `sorting` | Y | 5 | Noor | — | 9 | 19 | 8.1 | Draft |
| 7 | `qsr-020` | `hotspot` | N | — | Noor | — | 12 | 75 | 32.1 | Draft |
| 8 | `qsr-021` | `decision_scenario` | Y | 15 | Noor | Noor | 12 | 34 | 14.6 | Draft |
| 9 | `qsr-022` | `matching` | Y | 10 | Noor | — | 10 | 18 | 7.7 | Draft |
| 10 | `qsr-023` | `sorting` | Y | 5 | Noor | — | 6 | 18 | 7.7 | Draft |
| 11 | `qsr-030` | `sorting` | Y | 5 | Noor | — | 5 | 20 | 8.6 | Draft |
| 12 | `qsr-031` | `worked_example` | N | — | Omar | Dr. Omar | 17 | 102 | 43.7 | Draft |
| 13 | `qsr-032` | `fill_blank` | Y | 5 | Noor | — | 7 | 18 | 7.7 | Draft |
| 14 | `qsr-033` | `matching` | Y | 10 | Noor | — | 7 | 19 | 8.1 | Draft |
| 15 | `qsr-040` | `labeled_diagram` | N | — | Omar | Dr. Omar | 10 | 69 | 29.6 | Draft |
| 16 | `qsr-041` | `drag_drop` | Y | 10 | Noor | — | 7 | 20 | 8.6 | Draft |
| 17 | `qsr-042` | `true_false` | Y | 5 | Noor | — | 14 | 19 | 8.1 | Draft |
| 18 | `qsr-050` | `content_slide` | N | — | Noor | — | 20 | 75 | 32.1 | Draft |
| 19 | `qsr-051` | `decision_scenario` | Y | 15 | Noor | Noor | 14 | 38 | 16.3 | Draft |
| 20 | `qsr-090` | `results_breakdown` | N | — | Noor | — | 8 | 25 | 10.7 | Draft |
| 21 | `qsr-091` | `poll` | N | — | Noor | — | 11 | 19 | 8.1 | Draft |
| 22 | `qsr-092` | `summary` | N | — | Noor / Omar | Noor + Dr. Omar | 18 | 43 | 18.4 | Draft |
| | **Totals** | | **11 scored** | **95** | Noor 20 lines · Omar 3 lines | 7 screens | **248** | **840** | **359.8 s ≈ 6.0 min** | |

Narration words exclude the `NOOR:` / `OMAR:` tag. Phase 3 estimate ~7 minutes; scripted 6.0 minutes (-14 %, within ±15 %). Every segment is under 60 s; the two-voice close is 2 turns / ≈ 18.4 s.


### Asset list (all screens)

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `brand-background-title-navy` | background | `qsr-000` | own (official My Clinic brand asset) | Yes | Use supplied asset |
| `brand-logo-horizontal-white` | image | `qsr-000` | own (official My Clinic brand asset) | Yes | Use supplied asset |
| `brand-mark-white` | icon | `qsr-000` | own (official My Clinic brand asset) | Yes | Use supplied asset |
| `brand-value-tile-caring-purple` | image | `qsr-001` | own (official My Clinic brand asset) | Yes | Use supplied asset |
| `brand-mark-navy` | icon | `qsr-001`, `qsr-092` | own (official My Clinic brand asset) | Yes | Use supplied asset |
| `qsr-img-spo` | svg | `qsr-010` | own | Yes | Draft generated: [`assets/qsr-img-spo.svg`](assets/qsr-img-spo.svg) — review B11 badge wording |
| `qsr-img-pillars` | svg | `qsr-020` | own | Yes | To produce / review |
| `qsr-img-wristbands` | illustration | `qsr-021` | ai-generated | Yes | To produce / review |
| `qsr-img-matrix` | svg | `qsr-031`, `qsr-032` | own | Yes | Draft generated: [`assets/qsr-img-matrix.svg`](assets/qsr-img-matrix.svg) — scores final; band names/colours pending B6 |
| `qsr-img-iceberg` | svg | `qsr-040` | own | Yes | Draft generated: [`assets/qsr-img-iceberg.svg`](assets/qsr-img-iceberg.svg) — terms pending B8 |
| `char-noor-welcome` | character (programme) | `qsr-000` | ai-generated programme asset (Canva `MAHX-pFaNMU`) | Yes | Generated; download PNG with transparent background |
| `char-noor-listening` | character (programme) | `qsr-002` | ai-generated programme asset (Canva `MAHX-v3i0kY`) | Yes | Generated; download PNG with transparent background |
| `char-noor-avatar-neutral` | character (programme) | `qsr-051` | ai-generated programme asset (Canva `MAHX-n4HuyU`) | Yes | Generated |
| `char-noor-avatar-concern` | character (programme) | `qsr-021`, `qsr-051` | crop from `char-noor-concern` (Canva `MAHX-hFE0aQ`) | Yes | To make (companions.md §3) |
| `char-noor-avatar-happy` | character (programme) | `qsr-021`, `qsr-051` | crop from `char-noor-success` (Canva `MAHX-jiR90M`) | Yes | To make (companions.md §3) |
| `char-noor-success` | character (programme) | `qsr-092` | ai-generated programme asset (Canva `MAHX-jiR90M`) | Yes | Generated; download PNG with transparent background |
| `char-omar-thinking` | character (programme) | `qsr-031` | ai-generated programme asset (Canva `MAHX-jgu1Vk`) | Yes | Generated; download PNG with transparent background |
| `char-omar-avatar-neutral` | character (programme) | `qsr-040` | ai-generated programme asset (Canva `MAHX-nPHDkA`) | Yes | Generated |
| `char-omar-avatar-happy` | character (programme) | `qsr-092` | crop from `char-omar-success` (Canva `MAHX-llCU5M`) | Yes | To make (companions.md §3) |
| `qsr-aud-*` | audio | `qsr-000`, `qsr-001`, `qsr-002`, `qsr-010`, `qsr-011`, `qsr-012`, `qsr-020`, `qsr-021`, `qsr-022`, `qsr-023`, `qsr-030`, `qsr-031`, `qsr-032`, `qsr-033`, `qsr-040`, `qsr-041`, `qsr-042`, `qsr-050`, `qsr-051`, `qsr-090`, `qsr-091`, `qsr-092` | ai-generated / human voice (D10 pending): Noor + Dr. Omar | Transcript in every card | Narration scripted and speaker-tagged; `qsr-092` is two lines joined; provider/voice not approved |
| `qsr-vid-speakup` | video + WebVTT | `qsr-060 (optional, deferred)` | own (in-house recording only) | Transcript/captions required | Not in baseline; approval, recording and captions pending |


### Open questions for the SME

| # | Screen id | Question | Phase 0 id | Blocks build? |
|---|---|---|---|---|
| 1 | `qsr-001`, `qsr-092` | L&D/Quality: human-listen the whole source and confirm any quoted source phrase before release. | B1 | Yes for quotations/final narration approval |
| 2 | `qsr-060` optional | Quality Director: decide video licence route; recommended: do not ship the NotebookLM-watermarked source. Optional new in-house clip only. | B2 / D7 | No for 22-screen baseline; yes for optional video |
| 3 | `qsr-020`–`qsr-022` | Patient Safety Officer: confirm IPSG wording and numbering. | B3 | Yes |
| 4 | `qsr-020`–`qsr-022` | Nursing Director: confirm the two identifiers and same-name third-identifier rule. | B4 | Yes |
| 5 | `qsr-020`, `qsr-022` | Nursing Director: confirm the fall-risk band and its colour. | B5 | Yes |
| 6 | `qsr-031`, `qsr-032` | Risk Manager: provide official 1–25 matrix bands, thresholds and colours. | B6 | Yes |
| 7 | `qsr-031`, `qsr-033` | Risk Manager: confirm response terms and acceptance/approval conditions. | B7 | Yes |
| 8 | `qsr-040`–`qsr-042`, `qsr-051` | Risk Manager: settle critical incident vs sentinel event, adverse-event and near-miss definitions/examples, and just-culture wording. | B8 | Yes |
| 9 | `qsr-050`, `qsr-051` | Risk Manager: confirm reportable events, 24-hour window, digital channel/email and escalation terms. | B9 | Yes |
| 10 | `qsr-023` | Infection Control: verify the five moments against the facility poster. | B10 | Yes |
| 11 | `qsr-010`, `qsr-012` | Quality Director: confirm the FOCUS-PDCA step names and spelling. | B11 | Yes |
| 12 | `qsr-050`, `qsr-051` | Keep incident-report window consistent with Module 03 once policy is confirmed. | D8 | Yes |
| 13 | `qsr-002`, `qsr-091` | Verify poll storage, anonymity and non-persistence; no patient/staff details may be collected. | NEW-01 / D9 | Yes for these response controls |
| 14 | All narration | Confirm shared English voice provider, voice ID and commercial licence. | D10 | Yes for audio production; storyboard remains reviewable |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| Noor | “noor” (rhymes with *tour*) | `qsr-000` and every Noor line (speaker tag) |
| Omar | “OH-mar” | `qsr-031`, `qsr-040`, `qsr-092` (speaker tag) |

Both come from the master lexicon (`narration-and-lexicon.md` §4). The module also carries the master entries for `IPSG`, `FOCUS-PDCA`, `MRN`, plus Phase 3's `DOB`, `JCI`, `CBAHI` and `WHO`, in `narration-script.json`; none of these is spoken in the current script.

### Self-check

- [x] 22 core Phase 2 screens have cards in the same order; optional `qsr-060` is explicitly deferred rather than counted in the baseline.
- [x] Scored screens and total points match Phase 4: 11 screens / 95 points.
- [x] Narration total is within ±15% of the Phase 3 estimate; all segments are under 60 seconds and final timing report is below.
- [x] Review checklist applied to every card; open items are named at card level and in the SME table.
- [x] No invented clinical/policy facts are presented as final; all open policy dependencies are marked `⚠ PENDING`.
- [x] Brand fields are present on every card: L1–L6, supplied logo/position, palette/hex, Montserrat sizes, watermark, icons and prompts for every AI-generated asset.
- [x] v0.2: companions applied exactly per the Phase 2/3 tables (7 screens); shared `char-noor-*` / `char-omar-*` ids only; the v0.1 module-only mentor ids and character prompts are removed.
- [x] v0.2: every narration line is prefixed `NOOR:` or `OMAR:`; Dr. Omar speaks only on `qsr-031`, `qsr-040` and `qsr-092`; the two-voice close is 2 turns and under 45 s.
- [x] v0.2: Noor's honest stories are used once each, on `qsr-002` and `qsr-021` only; no companion appears over a question or gives away an answer.
- [x] v0.2: every JSON build block parses and carries `id`, `type`, `node_id`, `points` and `objective_ids`; `narration_text` matches the script without markup.
- [ ] Avatar crops `char-noor-avatar-concern`, `char-noor-avatar-happy`, `char-omar-avatar-happy` still to make (companions.md §3).
- [ ] D10 voice route and 30-second samples of both voices — **not yet**.
