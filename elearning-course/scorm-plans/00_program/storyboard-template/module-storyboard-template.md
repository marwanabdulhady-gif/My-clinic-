# Storyboard — <NN> <Module title>

![My Clinic logo](../../00_program/brand/logo-preview.png)

> Copy this file to `<module folder>/storyboard/storyboard.md`. Replace everything in `<angle brackets>`. Repeat the **screen card** (section B) once per screen in `phase-2-storyboard.md`, in the same order.

---

## A. Module header

| Field | Value |
|---|---|
| Module | `<NN> — <full package title from README>` |
| Module prefix | `<hs1- / hs2- / hr- / ops- / rcma- / rcmb- / qsr- / ehr->` |
| Storyboard version | `v0.1` |
| Author | `<agent or person>` |
| Date | `<YYYY-MM-DD>` |
| Status | `Draft — ready for SME review` |
| SME reviewer (role) | `<from phase-0 Owners table>` |
| Audience | `<from README>` |
| Seat-time budget | `<from phase-1 §4>` |
| SCORM / completion / pass mark | `<from phase-4 §1>` |
| Scored screens / total points | `<count> / <points from phase-4 §3>` |
| Source file | `elearning-course/md/<file>.md` |
| Brand | My Clinic — `00_program/brand/brand-identity.md` (version/date read: `<date>`) |
| Module colour | `<name + hex from brand-identity.md §2, e.g. Ambitious teal #008C99>` |
| Theme | `brand_to_theme(00_program/brand/brand-kit.json)` + `style-minimal`; module colour as `secondary` |
| Phase 0 items still open | `<list ids, e.g. B1, B4, D1>` |

### Objectives covered

| Objective id | Objective | Assessed by (screen ids) |
|---|---|---|
| `<id>` | `<text from phase-1 §3>` | `<ids>` |

### Section outline

| Node id | Section title | Screens |
|---|---|---|
| `<node id from phase-4 §2>` | `<title>` | `<first id>–<last id>` |

### Proposed changes (optional)

`<Only if you think a screen should change. Keep the original card; explain the change and why here. Otherwise write "None".>`

---

## B. Screen card (repeat for every screen)

### `<screen id>` — `<screen title>`

**Status:** `Draft` · **Section / node:** `<section title>` / `<node id>` · **Type:** `<edumints type>` · **Scored:** `<Yes (n pts) / No>`

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | `<what this screen does: introduce / explain / explore / practise / check / close>` |
| Objective(s) | `<objective ids, or "—" if unscored>` |
| On-the-job action | `<A# from phase-1 action map, or "—">` |
| Source | `<file + page / slide / timestamp>` |
| Depends on Phase 0 | `<item ids, or "None">` |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | `<≤ 8 words>` |
| Body / keywords | `<keywords only; ≤ 25 words aim, 45 max>` |
| Word count (excl. title) | `<n>` |
| Instruction (interactive screens) | `<one sentence telling the learner what to do>` |

#### 3. Visual design

| Field | Value |
|---|---|
| Brand layout | `<L1 Title / L2 Section opener / L3 Content / L4 Question / L5 Scenario / L6 Results — see brand-identity.md §7>` |
| Logo | `<file + size + position from brand-identity.md §1, e.g. logo-horizontal-navy.png, 30 px, header top-left>` |
| Visual concept | `<≥ 6 words a designer can act on: subject, composition, what moves>` |
| edumints layout | `<text / text_media / media_text / full_media / n/a for interaction types>` |
| Colours (palette names + hex) | bg `<white #FFFFFF / off-white #F4F7FA / navy gradient>` · headings `<navy #003867>` · body `<ink #1F2A37>` · highlight `<module colour>` · warning `<magenta #9D3293 or none>` |
| Watermark | `<petal watermark (L1, L2, close only) / none>` |
| Icons | `<line icons used, colour, provenance>` |
| Animation / reveal | `<none / auto reveal in narration order / click reveal>` |
| Companion | `<None / Noor / Dr. Omar / both>` · pose asset `<char-noor-explaining, char-omar-avatar-happy…>` · placement `<half-body right / tip card bottom-left / scenario avatar / feedback avatar>` · tip text `<≤ 25 words or n/a>` — from the module's Phase 3 companion table |

**Imagery**

| Asset id | Kind | Description / brief | Source (provenance) | Alt text | Decorative? |
|---|---|---|---|---|---|
| `<from phase-3 asset manifest, or new id>` | `<svg / illustration / photo / screenshot / icon>` | `<what it shows, size, crop>` | `<own / ai-generated / cc0 / local>` | `<meaningful alt text>` | `<Yes/No>` |

**AI image prompt** (only for `ai-generated` assets — fill the template in `brand-identity.md` §6; delete if none):

```text
<filled prompt: scene, module colour hex, people (none / Noor or Dr. Omar from the approved master), "No text, no letters, no numbers, no logos…">
```

#### 4. Interaction and scoring

`<Fill the block for this screen's type from screen-type-guide.md. Delete the others.>`

| Field | Value |
|---|---|
| Items / options / nodes | `<full list, with ids>` |
| Correct answer(s) | `<exact>` |
| Accepted variants (typed answers) | `<list, or n/a>` |
| Points | `<from phase-4>` |
| Pass rule (scenarios / games) | `<e.g. pass_score 2>` |
| Feedback — correct | `<1–2 sentences: why it is right>` |
| Feedback — incorrect | `<1–2 sentences: what to reconsider; do not shame>` |
| Per-choice feedback (scenarios) | `<table below>` |
| Hint (if any) | `<text>` |
| Retry / lives | `<from phase-3 activity plan>` |

Scenario / game nodes (delete if not used):

| Node | Situation (prompt) | Choice id | Choice text | Score Δ | Goes to | Feedback (why) |
|---|---|---|---|---|---|---|
| `<n1>` | `<prompt>` | `<a>` | `<text>` | `<+1/0>` | `<n2>` | `<why>` |

#### 5. Narration

| Field | Value |
|---|---|
| Speaker(s) | `<NOOR / OMAR / both — lead host unless Phase 3 says otherwise>` |
| Tone | `<calm / warm / serious / encouraging>` |
| Target seconds | `<from phase-3>` |
| Word count / est. seconds | `<n words> / <n ÷ 140 × 60 s>` |
| Cue targets | `<element ids used in [[cue:id]], or none>` |

> `<Full narration script. Prefix every line NOOR: or OMAR:. Use [[cue:id]] and [[pause:1.0]] markup. Question screens: set up the situation only.>`

New lexicon terms: `<term → pronunciation, or "None">`

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | `<how it is completed without a mouse>` |
| Not colour-only | `<what text/shape/position carries the meaning>` |
| Captions / transcript | `<narration_text present / video VTT / n/a>` |
| Timing | `<untimed / timer can be extended / n/a>` |

#### 7. Build fields (edumints)

```json
{
  "type": "<type>",
  "id": "<screen id>",
  "title": "<title>",
  "section": "<section title>",
  "node_id": "<node id>",
  "objective_ids": [],
  "points": 0
}
```

`<Add the type-specific fields from screen-type-guide.md. Use planned asset ids in <angle brackets> where the server id is not known yet.>`

#### 8. Notes for SME and developer

- Open questions: `<list, each with Phase 0 id if it exists>`
- Developer notes: `<anything the builder must know, e.g. region coordinates set after the final image>`

---

## C. Module summary (fill after all cards)

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `<id>` | `<type>` | `<Y/N>` | `<n>` | `<n>` | `<n>` | `<n>` | `<Draft>` |
| | **Totals** | | `<n scored>` | `<total pts>` | | `<total words>` | `<total s ≈ min>` | |

### Asset list (all screens)

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `<id>` | `<kind>` | `<screen ids>` | `<provenance>` | `<Yes>` | `<to produce / exists>` |

### Open questions for the SME

| # | Screen id | Question | Phase 0 id | Blocks build? |
|---|---|---|---|---|
| 1 | `<id>` | `<question>` | `<B#/D#/new>` | `<Yes/No>` |

### Lexicon additions

| Term | Say it as | Screens |
|---|---|---|
| `<term>` | `<pronunciation>` | `<ids>` |

### Self-check

- [ ] Every Phase 2 screen has a card, same ids and order
- [ ] Scored screens and total points match Phase 4
- [ ] Narration total within ±15% of the Phase 3 estimate
- [ ] `review-checklist.md` run on every card (including section H, brand)
- [ ] No `<angle bracket>` text left
