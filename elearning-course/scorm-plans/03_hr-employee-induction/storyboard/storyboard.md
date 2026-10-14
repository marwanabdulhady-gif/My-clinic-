# Storyboard — 03 Welcome On Board: My Clinic & HR Essentials

> Screen-by-screen storyboard for module 03. One card per screen listed in
> [`../phase-2-storyboard.md`](../phase-2-storyboard.md), same ids, same order.
> Written against [`../../00_program/storyboard-template/README.md`](../../00_program/storyboard-template/README.md).

---

## A. Module header

| Field | Value |
|---|---|
| Module | 03 — My Clinic — Welcome On Board: My Clinic & HR Essentials |
| Module prefix | `hr-` |
| Storyboard version | `v0.1` |
| Author | Arena agent (storyboarding run 1), for HR + Comms review |
| Date | 2026-10-14 |
| Status | `Draft — ready for SME review` |
| SME reviewer (role) | HR Business Partner / Head of Human Capital (SME lead); Corporate Communications for screens `hr-020`–`hr-023` |
| Audience | All new employees (clinical and non-clinical), day 1–3 |
| Seat-time budget | ~46 minutes (phase-1 §4: A 3 · B 6 · C 5 · D 6 · E 10 · F 6 · G 5 · H 2 · I 2 · Close 1) |
| SCORM / completion / pass mark | SCORM 2004 4th ed · `viewed_all_and_passed` · passing score **70** (= 102 of 145 points) |
| Scored screens / total points | 15 / 145 |
| Source file | `elearning-course/md/03_hr-employee-induction.md` (from `HR.pptx`, 62 slides, *Confidential*) |
| Phase 0 items still open | B1, B2, B3, B4, B5/D3, B6/D5, B7, B8, B9, B10, B11, B12, B13, B14/D8 |

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
| `narration_text` | Every card with a narration script carries `narration_text` = the script with `[[cue:…]]` / `[[pause:…]]` markup removed, for captions and the transcript. |
| `narration_asset_id` | `<hr-aud-XXX>` — assigned in Phase 3/4 from `export_audio_script`. |
| `evidence_screen_ids` | Set on every scored screen to the screen that teaches the rule (K1 evidence link, `core/antislop.py` E1). |
| Asset id placeholders | Written as `<hr-img-…>` / `<hr-aud-…>` / `<hr-pdf-…>` until `add_asset` returns a real id. |

### Proposed changes

| # | Screen | Change proposed | Why | Keep original? |
|---|---|---|---|---|
| 1 | `hr-044`, node 1 | Frame the lab-technician request as a request that **already has the MD's pre-approval**, and make the tested rule *“2 days a year for technicians, never carried over”* (slides 39–40). | Phase 2 words it as “scientific leave for a conference”. The source says scientific leave is for academic exams (slide 40) and that supporting documents need the MD's pre-approval. The reframe keeps the item answerable from the source and still tests the 2-day allowance. | Yes — the original card is written; the reframe is inside it and flagged for HR. |
| 2 | `hr-071`, item `it6` | Keep the wording **“No casual days”** for back office and make front office **“Uniform for every shift”**, with per-item feedback that names the difference. | The source uses *“no casual days”* for back office (slide 58) and *“no casual attire”* for front office. Two near-identical strings would make one placement ambiguous. | Yes — flagged in the card's SME notes. |

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
| Visual concept | Full-bleed My Clinic clinic photo, softly blurred, with a `primary` colour wash; title block left-aligned on the lower third, generous white space above |
| Layout | n/a (`title_slide`) |
| Colour roles | bg `primary` · text `on_primary` · accent none |
| Animation / reveal | Title fades up, then the subtitle 0.4 s later |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-hero` | photo | 1920×1080, real My Clinic reception or team photo, consented or replaced with an own-brand illustration | own (consent pending B6/D5) | Decorative background: the My Clinic reception area. | Yes |

#### 4. Interaction and scoring

n/a — title slide, no interaction and no score.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Warm |
| Target seconds | 15 |
| Word count / est. seconds | 31 words / ≈ 13.3 s |
| Cue targets | None |

> Welcome to My Clinic. Over the next forty-five minutes you'll meet who we are, and the HR rules you'll actually use in your first month. Nothing here is a memory test.

New lexicon terms: None

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
  "background_asset_id": "<hr-img-hero>",
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<hr-aud-000>",
  "narration_text": "Welcome to My Clinic. Over the next forty-five minutes you'll meet who we are, and the HR rules you'll actually use in your first month. Nothing here is a memory test."
}
```

#### 8. Notes for SME and developer

- Open questions: Does HR want the real CEO welcome video here instead of a still (phase-3 §1, program D10)? If yes, this becomes a `video` screen and the narration moves to the video transcript.
- Developer notes: `hr-img-hero` must not show identifiable staff or patients until B6/D5 is closed. Until then use the program's generic clinic illustration and mark the asset `provisional`.

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
| Visual concept | Three stacked statement blocks on an off-white field, each with a small line icon (heart, globe-and-heart, shield-check); the purpose block is largest and sits alone at the top |
| Layout | `full_media` with the hero photo behind a 60% `light` scrim, text blocks left-aligned over it |
| Colour roles | bg `light` · text `dark` · accent none |
| Animation / reveal | Blocks reveal in narration order: purpose → mission → goal |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-hero` | photo | Reused from `hr-000`, darker crop, scrim applied in the theme, not baked in | own | Decorative background: the My Clinic reception area. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Warm, calm |
| Target seconds | 35 |
| Word count / est. seconds | 85 words / ≈ 37.6 s |
| Cue targets | `purpose`, `mission`, `goal` |

> [[cue:purpose]] Our purpose is simple to say and hard to do: we help people live longer, healthier, happier lives. That includes people who are well today and come in for a check-up. [[pause:0.4]] [[cue:mission]] Our mission is to be the world's most customer-centric healthcare company. Customer-centric isn't a slogan — it's why a receptionist, a nurse and an analyst all get asked the same question: did this help the patient? [[pause:0.4]] [[cue:goal]] Our goal follows from that: outstanding patient experience, alongside excellent clinical outcomes. [[pause:0.4]] Everyone here remembers their own first week.

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
  "layout": "full_media",
  "media_asset_id": "<hr-img-hero>",
  "media_alt": "Decorative background: the My Clinic reception area.",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Purpose</strong> — helping people live longer, healthier, happier lives</p><p><strong>Mission</strong> — the world's most customer-centric healthcare company</p><p><strong>Goal</strong> — outstanding patient experience + excellent clinical outcomes</p>",
  "narration_asset_id": "<hr-aud-001>",
  "narration_text": "Our purpose is simple to say and hard to do: we help people live longer, healthier, happier lives. That includes people who are well today and come in for a check-up. Our mission is to be the world's most customer-centric healthcare company. Customer-centric isn't a slogan — it's why a receptionist, a nurse and an analyst all get asked the same question: did this help the patient? Our goal follows from that: outstanding patient experience, alongside excellent clinical outcomes. Everyone here remembers their own first week."
}
```

#### 8. Notes for SME and developer

- Open questions: None. The three statements are verbatim from the brand banner in the deck.
- Developer notes: `blocks` reveal as one unit. The three statements are therefore separate `<p>` elements in `body_html`, not `blocks`, so they reveal one by one.

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
| Visual concept | Five large tappable option cards in a single row on small screens, two rows on wide; each card has a line icon above a one-word label; a free-text box slides in under the row labelled “Other” |
| Layout | n/a (`poll`) |
| Colour roles | bg `surface` · text `dark` · accent on the selected card only |
| Animation / reveal | Cards fade up in sequence over 0.6 s; the reflection panel fades in after submitting |
| Character | None |

**Imagery:** None (icon set is part of the shared line-icon family, not a per-screen asset).

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
| Tone | Warm, light |
| Target seconds | 10 |
| Word count / est. seconds | 23 words / ≈ 9.9 s |
| Cue targets | None |

> Before we start: if you had one million Saudi riyals, where would you spend it? There's no right answer. Pick whatever is closest.

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
  "prompt_html": "<p>If you had one million Saudi riyals, where would you spend it?</p>",
  "options": [
    { "id": "a", "text_html": "Family" },
    { "id": "b", "text_html": "Travel" },
    { "id": "c", "text_html": "Learning" },
    { "id": "d", "text_html": "Giving back" },
    { "id": "e", "text_html": "Other" }
  ],
  "multi": false,
  "allow_text": true,
  "reflection_html": "<p>Whatever you chose says something you care about. At My Clinic, we start from what people care about — including yours.</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-002>",
  "narration_text": "Before we start: if you had one million Saudi riyals, where would you spend it? There's no right answer. Pick whatever is closest."
}
```

#### 8. Notes for SME and developer

- Open questions: None.
- Developer notes: the poll must never block Continue — `poll` is unscored and participation-only.

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
| Visual concept | Four horizontal tab labels across the top with one line icon each; the active panel shows the theme line in large type and the actions as a plain bulleted list with no bullets, one per row |
| Layout | n/a (`tabs`) |
| Colour roles | bg `light` · text `dark` · accent underlines the active tab only (1 of 4 = 25% of the tab strip, well under the 10% screen-area rule) |
| Animation / reveal | Panel content fades up on each tab change |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-values-icons` | SVG ×4 | Line icons: two figures (Collaborative), shield-check (Responsible), chevron-up (Ambitious), heart-in-hand (Caring). Redrawn from slide 10's icon family in brand colours. | own | Decorative — each tab is labelled in text. | Yes |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | 4 tabs: `collaborative`, `responsible`, `ambitious`, `caring` |
| Correct answer(s) | n/a |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Warm, direct |
| Target seconds | 40 |
| Word count / est. seconds | 81 words / ≈ 36.7 s |
| Cue targets | `intro`, `collab`, `resp`, `amb`, `care` |

> [[cue:intro]] Every clinic has values on a wall. Ours only matter if you can see them in what people do. [[pause:0.4]] [[cue:collab]] Collaborative: we act together, treat everyone with respect, and stay transparent. [[pause:0.4]] [[cue:resp]] Responsible: own your decisions, make things happen, and hold each other to the same standard. [[pause:0.4]] [[cue:amb]] Ambitious: go above and beyond, and challenge the status quo when it stops serving patients. [[pause:0.4]] [[cue:care]] Caring: act with empathy, because everyone matters. [[pause:0.4]] As you go on, think which of these you already do without being asked.

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
  "prompt_html": "<p>Values are behaviours. Open each one and look for something you already do.</p>",
  "tabs": [
    { "label": "Collaborative",
      "body_html": "<p><strong>Unites diverse</strong></p><p>Act together · Treat everyone with respect · Be transparent · Embrace diverse perspectives · Deliver outstanding results</p>",
      "image_asset_id": "<hr-img-values-icons-collab>", "image_alt": "Decorative icon." },
    { "label": "Responsible",
      "body_html": "<p><strong>Creating a culture of accountability</strong></p><p>Own our decisions and actions · Make things happen · Demonstrate high professional standards · Hold yourself and each other accountable</p>",
      "image_asset_id": "<hr-img-values-icons-resp>", "image_alt": "Decorative icon." },
    { "label": "Ambitious",
      "body_html": "<p><strong>Set new standards</strong></p><p>Go above and beyond · Make new possibilities happen · Challenge the status quo · Become industry shapers · Deliver outstanding results</p>",
      "image_asset_id": "<hr-img-values-icons-amb>", "image_alt": "Decorative icon." },
    { "label": "Caring",
      "body_html": "<p><strong>Putting empathy first</strong></p><p>Act with empathy · Everyone matters · Love our customers · Deliver with quality</p>",
      "image_asset_id": "<hr-img-values-icons-care>", "image_alt": "Decorative icon." }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-010>",
  "narration_text": "Every clinic has values on a wall. Ours only matter if you can see them in what people do. Collaborative: we act together, treat everyone with respect, and stay transparent. Responsible: own your decisions, make things happen, and hold each other to the same standard. Ambitious: go above and beyond, and challenge the status quo when it stops serving patients. Caring: act with empathy, because everyone matters. As you go on, think which of these you already do without being asked."
}
```

#### 8. Notes for SME and developer

- Open questions: None. All eight action phrases are verbatim from slide 9.
- Developer notes: the four icons are one asset family (`hr-img-values-icons`) uploaded as four assets; the build ids above use the `-collab` / `-resp` suffix convention from phase-3 §4.

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
| Visual concept | Two columns: six plain white action cards on the left, four value tiles on the right; a drawn connector line follows the learner's pointer while a card is selected |
| Layout | n/a (`matching`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt; `success` / `error` only in the result state |
| Animation / reveal | None |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 6.9 s |
| Cue targets | None |

> Here are six things people did this week. Match each one to the value behind it.

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
  "objective_ids": ["hr-o1"],
  "points": 10,
  "evidence_screen_ids": ["hr-010"],
  "prompt_html": "<p>Six things people did this week. Match each one to the value behind it.</p>",
  "pairs": [
    { "id": "p1", "left_html": "You admit a scheduling mistake to your manager and fix it.", "right_html": "Responsible" },
    { "id": "p2", "left_html": "You ask a colleague in another department for their view before you decide.", "right_html": "Collaborative" },
    { "id": "p3", "left_html": "You stay with an anxious patient until the nurse arrives.", "right_html": "Caring" },
    { "id": "p4", "left_html": "You suggest a faster way to book follow-up appointments.", "right_html": "Ambitious" },
    { "id": "p5", "left_html": "You share the reason for a delay with the team instead of staying quiet.", "right_html": "Collaborative" },
    { "id": "p6", "left_html": "You check your own work against the professional standard before you sign it off.", "right_html": "Responsible" }
  ],
  "feedback": {
    "correct_html": "<p>Right. Notice that Responsible and Collaborative each appear twice: the values overlap in real work, and one action can show more than one.</p>",
    "incorrect_html": "<p>Not all six. Read each action again and ask what the person was actually choosing to do — own it, involve others, reach further, or care for someone.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-011>",
  "narration_text": "Here are six things people did this week. Match each one to the value behind it."
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
| Visual concept | Seven collapsed rows in a single column, each with a line icon, the pillar name in caps and a chevron; expanding a row reveals the headline line and the key points as a wrapped keyword row |
| Layout | n/a (`accordion`) |
| Colour roles | bg `light` · text `dark` · accent on the chevron of the open panel only |
| Animation / reveal | Panel body expands with a 200 ms height transition |
| Character | None |

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
| Tone | Calm, clear |
| Target seconds | 45 |
| Word count / est. seconds | 99 words / ≈ 45.6 s |
| Cue targets | `intro`, `closer`, `cure`, `cap`, `culture`, `clin`, `care`, `cost` |

> [[cue:intro]] Strategy feels like someone else's job until you find your own work inside it. Here are the seven pillars. [[pause:0.4]] [[cue:closer]] Closer: convenient access — clinics, community clinics and home health care, digital services, telemedicine. [[pause:0.4]] [[cue:cure]] Cure: the best Saudi doctors, clinical outcomes, centres of excellence, prevention and wellbeing. [[pause:0.4]] [[cue:cap]] Capabilities: a repeatable model for running and growing clinics, with real governance. [[pause:0.4]] [[cue:culture]] Culture: our mission and values, servant leadership, a culture of excellence. [[pause:0.4]] [[cue:clin]] Clinicians: a caring environment, competitive benefits, room to grow. [[pause:0.4]] [[cue:care]] Care: seamless experience, empathy, loyalty built through My Care. [[pause:0.4]] [[cue:cost]] Cost: competitive cost to serve. [[pause:0.4]] Whichever one you picked, that's your line in.

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
  "prompt_html": "<p>Seven pillars. Open the ones your role touches — you're not expected to memorise all seven.</p>",
  "items": [
    { "title": "Closer", "body_html": "<p><strong>Convenient &amp; easy access</strong></p><p>Convenient physical access · Community clinics &amp; HHC · Digital access &amp; services · Call centre &amp; telemedicine</p>", "image_asset_id": "<hr-img-7c-closer>", "image_alt": "Decorative icon." },
    { "title": "Cure", "body_html": "<p><strong>Tackle the biggest healthcare challenge</strong></p><p>The best Saudi doctors · Focus on clinical outcomes · Centres of excellence · Prevention &amp; wellbeing</p>", "image_asset_id": "<hr-img-7c-cure>", "image_alt": "Decorative icon." },
    { "title": "Capabilities", "body_html": "<p><strong>A repeatable business model</strong></p><p>Repeatable operations &amp; expansion · Robust governance &amp; compliance · Peopleware, software, hardware · Competitive cost to serve</p>", "image_asset_id": "<hr-img-7c-capabilities>", "image_alt": "Decorative icon." },
    { "title": "Culture", "body_html": "<p><strong>The way we do things around here</strong></p><p>Mission, values &amp; beliefs · Servant leadership · A culture of excellence</p>", "image_asset_id": "<hr-img-7c-culture>", "image_alt": "Decorative icon." },
    { "title": "Clinicians", "body_html": "<p><strong>An attractive doctor value proposition</strong></p><p>Caring environment · Competitive benefits · Growth &amp; development</p>", "image_asset_id": "<hr-img-7c-clinicians>", "image_alt": "Decorative icon." },
    { "title": "Care", "body_html": "<p><strong>A legendary service &amp; care</strong></p><p>Seamless experience · Empathy &amp; compassion · Loyalty through My Care · Service &amp; advocacy mindset</p>", "image_asset_id": "<hr-img-7c-care>", "image_alt": "Decorative icon." },
    { "title": "Cost", "body_html": "<p><strong>Competitive cost to serve</strong></p><p>Revenue-cycle management · Operational efficiency · Overhead management</p>", "image_asset_id": "<hr-img-7c-cost>", "image_alt": "Decorative icon." }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-012>",
  "narration_text": "Strategy feels like someone else's job until you find your own work inside it. Here are the seven pillars. Closer: convenient access — clinics, community clinics and home health care, digital services, telemedicine. Cure: the best Saudi doctors, clinical outcomes, centres of excellence, prevention and wellbeing. Capabilities: a repeatable model for running and growing clinics, with real governance. Culture: our mission and values, servant leadership, a culture of excellence. Clinicians: a caring environment, competitive benefits, room to grow. Care: seamless experience, empathy, loyalty built through My Care. Cost: competitive cost to serve. Whichever one you picked, that's your line in."
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
| Visual concept | Stem in large type at the top; four plain option rows beneath, each a radio control plus a single sentence; no imagery, so the decision is the only thing on screen |
| Layout | n/a (`mcq`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 6.9 s |
| Cue targets | None |

> One to try. My Care follow-up calls build patient loyalty. Which pillar do they belong to?

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
  "objective_ids": ["hr-o1"],
  "points": 5,
  "evidence_screen_ids": ["hr-012"],
  "prompt_html": "<p>My Care follow-up calls that build patient loyalty support which pillar?</p>",
  "options": [
    { "id": "a", "text_html": "Care", "correct": true,
      "feedback_html": "<p>Care. My Care follow-up calls are named in the Care pillar under “build loyalty through My Care”. Loyalty is a service and relationship outcome, not an access outcome.</p>" },
    { "id": "b", "text_html": "Closer",
      "feedback_html": "<p>Closer covers <em>access</em>: physical, community and home health care, digital services, and the call centre and telemedicine. A phone call is access; a follow-up call that builds loyalty is Care.</p>" },
    { "id": "c", "text_html": "Culture",
      "feedback_html": "<p>Culture is mission, values and servant leadership. It shapes how we behave, not this service.</p>" },
    { "id": "d", "text_html": "Cost",
      "feedback_html": "<p>Cost is about cost to serve: revenue cycle, efficiency and overhead. Loyalty work sits on the service side.</p>" }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Care. My Care follow-up calls are named in the Care pillar under “build loyalty through My Care”. Loyalty is a service and relationship outcome, not an access outcome.</p>",
    "incorrect_html": "<p>Not quite. Closer is about <em>access</em> — physical, community, digital and telemedicine. Culture is mission, values and leadership. Cost is efficiency. The pillar that names My Care and loyalty is Care.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-013>",
  "narration_text": "One to try. My Care follow-up calls build patient loyalty. Which pillar do they belong to?"
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
| Visual concept | Three equal cards side by side, each with one line icon above a short label and a one-line caption; the first card is annotated “sick or healthy” in a smaller line |
| Layout | `text` |
| Colour roles | bg `light` · text `dark` · accent none |
| Animation / reveal | Cards fade up left to right in narration order |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-serve-icons` | SVG ×3 | Line icons: family group, community ring, briefcase-and-shield | own | Decorative — each card is labelled in text. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Warm |
| Target seconds | 20 |
| Word count / est. seconds | 44 words / ≈ 19.6 s |
| Cue targets | `patients`, `community`, `corporates` |

> [[cue:patients]] Who do we serve? First, patients and their families — sick or healthy. Many of the people who walk in today are well, and we want them to stay that way. [[pause:0.4]] [[cue:community]] Second, the community around each clinic. [[pause:0.3]] [[cue:corporates]] Third, corporates and insurers. Three groups, one standard.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Patients &amp; families</strong> — sick or healthy</p><p><strong>Community</strong></p><p><strong>Corporates &amp; insurers</strong></p>",
  "narration_asset_id": "<hr-aud-014>",
  "narration_text": "Who do we serve? First, patients and their families — sick or healthy. Many of the people who walk in today are well, and we want them to stay that way. Second, the community around each clinic. Third, corporates and insurers. Three groups, one standard."
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
| Visual concept | A single horizontal axis with nine year nodes; the active node lifts and its caption card slides in beneath the axis; a thin progress line fills as the learner moves along |
| Layout | n/a (`timeline`) |
| Colour roles | bg `light` · text `dark` · accent on the progress line and active node only |
| Animation / reveal | Nodes appear in year order as the narration advances |
| Character | None |

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
| Tone | Warm, plain |
| Target seconds | 30 |
| Word count / est. seconds | 72 words / ≈ 32.1 s |
| Cue targets | `e2017`, `e2019`, `e2023`, `e2024`, `e2025` |

> We opened our first clinic in North Jeddah in 2017. [[cue:e2017]] [[pause:0.3]] In 2019 we started the employment check-up unit, [[cue:e2019]] our first corporate service. [[pause:0.3]] Then came East Jeddah, the dental centre, and Petro-Rabigh in 2023, [[cue:e2023]] our first clinic inside a corporate community. [[pause:0.3]] Riyadh followed in 2024, [[cue:e2024]] a flagship to put the brand on the map. [[pause:0.3]] The last two years added our first community clinics. [[cue:e2025]] Nine years, nine steps, one idea: bring good care closer.

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
  "prompt_html": "<p>From one clinic in Jeddah to a network across the west and Riyadh.</p>",
  "events": [
    { "date": "2017", "title": "MCJ1 opens", "body_html": "<p>Our first full-service outpatient clinic, in North Jeddah.</p>" },
    { "date": "2018", "title": "New products", "body_html": "<p>New products launched, widening what one clinic could offer.</p>" },
    { "date": "2019", "title": "Corporate check-ups", "body_html": "<p>The employment check-up unit starts — our first corporate service line.</p>" },
    { "date": "2021", "title": "MCJ2 opens", "body_html": "<p>Our second full-service outpatient clinic, in East Jeddah.</p>" },
    { "date": "2022", "title": "Dental centre", "body_html": "<p>My Clinic Dental (D1) opens in Jeddah.</p>" },
    { "date": "2023", "title": "Petro-Rabigh", "body_html": "<p>PRC opens — our first clinic inside a corporate community.</p>" },
    { "date": "2024", "title": "Riyadh", "body_html": "<p>R1 opens: a flagship clinic in Riyadh to establish the brand.</p>" },
    { "date": "2025", "title": "J3 opens", "body_html": "<p>Our first community clinic in Jeddah. <em>Name pending decision B5 / D3.</em></p>" },
    { "date": "2026", "title": "J4 opens", "body_html": "<p>Our second community clinic in Jeddah. <em>Name pending decision B5 / D3.</em></p>" }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-020>",
  "narration_text": "We opened our first clinic in North Jeddah in 2017. In 2019 we started the employment check-up unit, our first corporate service. Then came East Jeddah, the dental centre, and Petro-Rabigh in 2023, our first clinic inside a corporate community. Riyadh followed in 2024, a flagship to put the brand on the map. The last two years added our first community clinics. Nine years, nine steps, one idea: bring good care closer."
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
| Visual concept | Minimal outline map of western Saudi Arabia with an inset for Riyadh; seven numbered pins; each pin opens a small card with the code, the branch type, the city and the year; a counter shows “3 of 7” |
| Layout | n/a (`hotspot`) |
| Colour roles | bg `light` · text `dark` · accent on unvisited pins only (they dim to neutral once opened) |
| Animation / reveal | Pins pulse gently until opened, then settle |
| Character | None |

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
| Tone | Warm, practical |
| Target seconds | 15 |
| Word count / est. seconds | 31 words / ≈ 13.3 s |
| Cue targets | None |

> You'll hear these codes every day, so it's worth knowing what they mean. Open all seven pins. J one, J two, D one, J three, J four, P-R-C and R one.

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
  "image_asset_id": "<hr-img-map>",
  "image_alt": "Map of My Clinic sites: five in Jeddah, one in Petro-Rabigh, one in Riyadh.",
  "mode": "explore",
  "require_all": true,
  "prompt_html": "<p>Seven sites. You'll hear these codes every day — open each pin.</p>",
  "regions": [
    { "id": "j1", "shape": "rect", "coords": [300, 150, 90, 60], "label_html": "J1 — North Jeddah",
      "feedback_html": "<p>Our first full-service outpatient clinic. Opened 2017.</p>" },
    { "id": "j2", "shape": "rect", "coords": [430, 190, 90, 60], "label_html": "J2 — East Jeddah",
      "feedback_html": "<p>Our second full-service outpatient clinic. Opened 2021.</p>" },
    { "id": "d1", "shape": "rect", "coords": [350, 250, 90, 60], "label_html": "D1 — Dental Centre",
      "feedback_html": "<p>Our dental centre in Jeddah. Opened 2022.</p>" },
    { "id": "j3", "shape": "rect", "coords": [280, 300, 90, 60], "label_html": "J3 — community clinic",
      "feedback_html": "<p>Our first community clinic in Jeddah. Opened 2025. Name pending decision B5 / D3.</p>" },
    { "id": "j4", "shape": "rect", "coords": [300, 380, 90, 60], "label_html": "J4 — community clinic",
      "feedback_html": "<p>Our second community clinic in Jeddah. Opened 2026. Name pending decision B5 / D3.</p>" },
    { "id": "prc", "shape": "circle", "coords": [250, 470, 32], "label_html": "PRC — Petro-Rabigh",
      "feedback_html": "<p>Our clinic in Petro-Rabigh. Opened 2023.</p>" },
    { "id": "r1", "shape": "circle", "coords": [980, 300, 32], "label_html": "R1 — Riyadh",
      "feedback_html": "<p>Our first clinic in Riyadh — a flagship. Opened 2024.</p>" }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-021>",
  "narration_text": "You'll hear these codes every day, so it's worth knowing what they mean. Open all seven pins. J one, J two, D one, J three, J four, P-R-C and R one."
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
| Visual concept | Four portrait cards in one row; each is a soft-cornered square with the role printed under it and a one-line “looks after” caption; no names until consent is recorded |
| Layout | `text` (blocks: caption, image, caption, image …) |
| Colour roles | bg `light` · text `dark` · accent none |
| Animation / reveal | Cards fade up left to right in narration order |
| Character | None |

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
| Tone | Warm, factual |
| Target seconds | 20 |
| Word count / est. seconds | 46 words / ≈ 20.8 s |
| Cue targets | `ceo`, `cmo`, `coo`, `cfo` |

> [[cue:ceo]] Four people lead the company. The CEO sets the direction. [[pause:0.4]] [[cue:cmo]] The CMO owns clinical standards — questions about how we practise medicine land here. [[pause:0.4]] [[cue:coo]] The COO runs the clinics day to day. [[pause:0.3]] [[cue:cfo]] The CFO looks after the money. You'll see their decisions in how your clinic runs.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "blocks": [
    { "html": "<p>Chief Executive Officer — sets the direction and answers to the board.</p>" },
    { "asset_id": "<hr-img-leaders-ceo>", "caption": "Abdullah Alghamdi, Chief Executive Officer. Portrait pending consent B6." },
    { "html": "<p>Chief Medical Officer — owns clinical standards and outcomes.</p>" },
    { "asset_id": "<hr-img-leaders-cmo>", "caption": "Dr Ahmed Al Zahrani, Chief Medical Officer. Portrait pending consent B6." },
    { "html": "<p>Chief Operating Officer — runs the clinics day to day.</p>" },
    { "asset_id": "<hr-img-leaders-coo>", "caption": "Hesham Abdulwahab, Chief Operating Officer. Portrait pending consent B6." },
    { "html": "<p>Chief Finance Officer — looks after the money that makes it possible.</p>" },
    { "asset_id": "<hr-img-leaders-cfo>", "caption": "Richard Thompson, Chief Finance Officer. Portrait pending consent B6." }
  ],
  "narration_asset_id": "<hr-aud-022>",
  "narration_text": "Four people lead the company. The CEO sets the direction. The CMO owns clinical standards — questions about how we practise medicine land here. The COO runs the clinics day to day. The CFO looks after the money. You'll see their decisions in how your clinic runs."
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
| Visual concept | Five cards in a shallow fan across the middle of the stage; flipping one rotates it on its vertical axis to reveal the back; the flipped card stays face-up and slides to the back of the fan |
| Layout | n/a (`flashcards`) |
| Colour roles | bg `light` · text `dark` · accent on the flip control only |
| Animation / reveal | 300 ms vertical-axis flip, respects `prefers-reduced-motion` by cross-fading instead |
| Character | None |

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
| Tone | Warm, honest |
| Target seconds | 15 |
| Word count / est. seconds | 39 words / ≈ 16.7 s |
| Cue targets | None |

> We're proud of these, so flip them. And hold one thought alongside them. Accreditation is measured, not given. Every score here expires, and the next survey team will look at what we did this year, not at these cards.

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
  "prompt_html": "<p>Flip each card. Accreditation is measured, not given — and it has to be earned again.</p>",
  "cards": [
    { "front_html": "CBAHI accreditation",
      "back_html": "Accredited by CBAHI, the Central Board for Accreditation of Healthcare Institutions. MCJ1 scored 98.67 in 2022 and MCJ2 scored 100 in 2023. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-star>", "front_alt": "Decorative icon." },
    { "front_html": "Best Clinical Patient Outcome",
      "back_html": "Best Clinical Patient Outcome, 2019–2020. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-trophy>", "front_alt": "Decorative icon." },
    { "front_html": "Best new clinic for customer service",
      "back_html": "Best new clinic for customer service, 2018. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-star>", "front_alt": "Decorative icon." },
    { "front_html": "Best New Premium Clinic",
      "back_html": "Best New Premium Clinic, 2018–19. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-trophy>", "front_alt": "Decorative icon." },
    { "front_html": "Most innovative corporate wellness initiative",
      "back_html": "Most innovative corporate wellness initiative in Saudi Arabia, 2019. <em>Pending B7.</em>",
      "front_asset_id": "<hr-img-award-star>", "front_alt": "Decorative icon." }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-023>",
  "narration_text": "We're proud of these, so flip them. And hold one thought alongside them. Accreditation is measured, not given. Every score here expires, and the next survey team will look at what we did this year, not at these cards."
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
| Visual concept | Four value blocks in a 2×2 grid with one line icon each; a single full-width warning strip below the grid carries the 24-hour rule, set in `dark` on an `accent`-tinted panel, with an exclamation icon so the meaning is not carried by colour |
| Layout | `text` |
| Colour roles | bg `light` · text `dark` · accent on the bottom strip only (one strip, well under 10%) |
| Animation / reveal | Grid blocks fade up one by one, then the strip slides up last |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-ethics-icons` | SVG ×4 | Line icons: two people with a heart (Respect), open hand with a tick (Integrity), clipboard with a check (Accountability), lightbulb with a link (Innovation and collaboration) | own | Decorative — each value is labelled in text. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Serious, warm |
| Target seconds | 35 |
| Word count / est. seconds | 78 words / ≈ 35.1 s |
| Cue targets | `respect`, `integrity`, `accountability`, `innovation`, `report` |

> [[cue:respect]] Four values sit under everything. Respect — the rights, privacy and dignity of patients, families and colleagues. [[pause:0.4]] [[cue:integrity]] Integrity — be transparent, and disclose any conflict of interest. [[pause:0.4]] [[cue:accountability]] Accountability — a culture where people report safety concerns instead of staying quiet. [[pause:0.4]] [[cue:innovation]] Innovation and collaboration — research and community work that improves outcomes. [[pause:0.5]] [[cue:report]] And the rule you'll use: faced with an ethical dilemma, complete an incident report within twenty-four hours and bring in the ethics team. You're never expected to work it out alone.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Respect</strong> — uphold the rights, privacy and dignity of patients, families and colleagues.</p><p><strong>Integrity</strong> — transparent practice; disclose any potential conflict of interest.</p><p><strong>Accountability</strong> — a culture that encourages reporting safety concerns and adherence to policy.</p><p><strong>Innovation &amp; collaboration</strong> — support research and community engagement to improve quality and outcomes.</p><p><strong>Ethical dilemma? Incident report within 24 hours + ethics team.</strong> <em>Pending B14 / D8.</em></p>",
  "narration_asset_id": "<hr-aud-030>",
  "narration_text": "Four values sit under everything. Respect — the rights, privacy and dignity of patients, families and colleagues. Integrity — be transparent, and disclose any conflict of interest. Accountability — a culture where people report safety concerns instead of staying quiet. Innovation and collaboration — research and community work that improves outcomes. And the rule you'll use: faced with an ethical dilemma, complete an incident report within twenty-four hours and bring in the ethics team. You're never expected to work it out alone."
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
| Visual concept | A flat-illustration band across the top that changes with the node — a meeting room, then a corridor, then a quiet desk; the situation text sits on a white card below it and the choices are full-width buttons under that |
| Layout | n/a (`decision_scenario`) |
| Colour roles | bg `surface` · text `dark` · accent none during the decision; `success` / `error` tints in the outcome line only |
| Animation / reveal | The situation card fades up on each node change |
| Character | `mentor-noor`, pose `explaining` on node 1, `concern` on node 2, `neutral` on node 3. Uses the program master character (`narration-and-lexicon.md` §5); phase-3 §4 lists the module-local id `hr-char-noor` for the same asset. |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-ethics-meeting` | illustration | Flat meeting-room scene: table, four chairs, a laptop and a document; two brand colours | ai-generated | “A small meeting room where a supplier evaluation is being discussed.” | No |
| `hr-img-ethics-corridor` | illustration | Flat corridor scene: reception desk and a queue of two patients | ai-generated | “A clinic corridor with a reception desk and two patients waiting.” | No |
| `hr-img-ethics-desk` | illustration | Flat desk scene: laptop showing a blank report form, a cup, a notebook | ai-generated | “A desk with a laptop open on an incident report form.” | No |
| `hr-char-noor` / `mentor-noor` | character | Program mentor, three poses | ai-generated | “Noor, a senior nurse and safety liaison, speaking.” | No |

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
| Tone | Serious, calm |
| Target seconds | 15 |
| Word count / est. seconds | 35 words / ≈ 15.0 s |
| Cue targets | None |

> Three moments now, and nobody is watching. First: you're on a panel evaluating suppliers for a clinic fit-out, and one bidder is your cousin's company. The evaluation starts in an hour. What do you do?

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
  "objective_ids": ["hr-o2"],
  "points": 15,
  "evidence_screen_ids": ["hr-030"],
  "pass_score": 3,
  "start_node_id": "n1",
  "intro_html": "<p>Three moments, three decisions. Nobody is watching.</p>",
  "nodes": [
    { "id": "n1",
      "prompt_html": "<p>You're on a panel evaluating three suppliers for a clinic fit-out. One bidder is your cousin's company. The evaluation starts in an hour.</p>",
      "image_asset_id": "<hr-img-ethics-meeting>",
      "image_alt": "A small meeting room where a supplier evaluation is being discussed.",
      "choices": [
        { "id": "n1a", "text_html": "Say nothing — you can score their bid fairly.", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Even a fair score looks compromised. Integrity means disclosing a potential conflict of interest before the work starts, in procurement as much as in recruitment.</p>" },
        { "id": "n1b", "text_html": "Declare the conflict in writing to the panel chair and step back from scoring that bid.", "score_delta": 1, "goto_node_id": "n2",
          "feedback_html": "<p>Right. You disclose the potential conflict and remove yourself from the decision. Nobody has to guess afterwards, including you.</p>" },
        { "id": "n1c", "text_html": "Step out of the meeting quietly and say nothing.", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Leaving is better than scoring, but silence doesn't help: the panel still doesn't know why, and the conflict stays undocumented. Declare it, then step back.</p>" }
      ] },
    { "id": "n2",
      "prompt_html": "<p>A colleague from another department asks you to “help” a patient skip the queue, and offers you a gift.</p>",
      "image_asset_id": "<hr-img-ethics-corridor>",
      "image_alt": "A clinic corridor with a reception desk and two patients waiting.",
      "choices": [
        { "id": "n2a", "text_html": "Decline, and explain that access to care is not something we trade.", "score_delta": 1, "goto_node_id": "n3",
          "feedback_html": "<p>Right. Fair access is part of Respect — every patient in that queue is waiting for the same reason. A gift makes it a transaction.</p>" },
        { "id": "n2b", "text_html": "Do it once, then return the gift.", "score_delta": 0, "goto_node_id": "n3",
          "feedback_html": "<p>Returning the gift afterwards doesn't undo it. Someone else waited longer because of a favour, and the gift makes it a transaction.</p>" },
        { "id": "n2c", "text_html": "Ask the patient to wait outside and slot them in when it's quiet.", "score_delta": 0, "goto_node_id": "n3",
          "feedback_html": "<p>Quiet or not, that patient is still moving ahead of people who waited. Decline, and say why.</p>" }
      ] },
    { "id": "n3",
      "prompt_html": "<p>A week later you're not sure whether something you saw counts as an ethical issue. Nobody else has raised it.</p>",
      "image_asset_id": "<hr-img-ethics-desk>",
      "image_alt": "A desk with a laptop open on an incident report form.",
      "choices": [
        { "id": "n3a", "text_html": "Wait until you're certain before involving anyone.", "score_delta": 0, "goto_node_id": null,
          "feedback_html": "<p>Waiting is the common mistake. The policy doesn't ask you to be certain; it asks you to act on the dilemma you have.</p>" },
        { "id": "n3b", "text_html": "Raise it with a colleague or the committee, and complete an incident report within 24 hours so the ethics team can advise.", "score_delta": 1, "goto_node_id": null,
          "feedback_html": "<p>Right. Consult colleagues for anything beyond your expertise, and complete an incident report within twenty-four hours so the ethics team can guide you. That's Accountability working.</p>" },
        { "id": "n3c", "text_html": "Mention it informally to your line manager and leave it there.", "score_delta": 0, "goto_node_id": null,
          "feedback_html": "<p>A quiet word is a start, but it leaves no record and no route to advice. Report it within twenty-four hours and bring the ethics team in.</p>" }
      ] }
  ],
  "feedback": {
    "correct_html": "<p>Three out of three. You declared the conflict, you held the line on queue-jumping, and you used the reporting route instead of guessing. That is Integrity and Accountability as behaviour, not as a poster.</p>",
    "incorrect_html": "<p>Below three. The pattern to hold on to: disclose a conflict early, never trade access for a favour, and when you genuinely don't know, report it within twenty-four hours and ask the ethics team.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-031>",
  "narration_text": "Three moments now, and nobody is watching. First: you're on a panel evaluating suppliers for a clinic fit-out, and one bidder is your cousin's company. The evaluation starts in an hour. What do you do?"
}
```

#### 8. Notes for SME and developer

- Open questions: **B14 / D8** — the 24-hour window appears in `n3b` and in the closing feedback. It must match module 07.
- Developer notes: the last node's choices carry `goto_node_id: null`, which ends the scenario. `pass_score` 3 is reachable only by `n1b` → `n2a` → `n3b`. Replay resets the running score; the LMS keeps the first recorded attempt's points.

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
| Visual concept | Two tall drop zones side by side with plain headings and one line icon each; nine draggable chips sit in a wrap row below; a placed chip shows a 1 px border and a small position number |
| Layout | n/a (`drag_drop`) |
| Colour roles | bg `surface` · text `dark` · accent on the drop-zone hover outline only |
| Animation / reveal | Chips settle with a 120 ms spring when dropped |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 19 words / ≈ 8.1 s |
| Cue targets | None |

> Nine statements from reception. Sort each: is it what the patient can expect, or what we ask of them?

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
  "objective_ids": ["hr-o2"],
  "points": 10,
  "evidence_screen_ids": ["hr-030"],
  "prompt_html": "<p>Nine statements from the notice in reception. Sort them into the right column.</p>",
  "targets": [
    { "id": "right", "label_html": "Patient right" },
    { "id": "resp", "label_html": "Patient responsibility" }
  ],
  "items": [
    { "id": "it1", "text_html": "Access to care regardless of race, gender or disability", "correct_target_id": "right" },
    { "id": "it2", "text_html": "Information and informed consent before treatment", "correct_target_id": "right" },
    { "id": "it3", "text_html": "Privacy and confidentiality", "correct_target_id": "right" },
    { "id": "it4", "text_html": "Pain management", "correct_target_id": "right" },
    { "id": "it5", "text_html": "Refuse treatment after understanding the risks", "correct_target_id": "right" },
    { "id": "it6", "text_html": "Ask for a patient advocacy representative", "correct_target_id": "right" },
    { "id": "it7", "text_html": "Give accurate health information", "correct_target_id": "resp" },
    { "id": "it8", "text_html": "Follow the treatment plan and attend appointments", "correct_target_id": "resp" },
    { "id": "it9", "text_html": "Respect other patients and staff", "correct_target_id": "resp" }
  ],
  "feedback": {
    "correct_html": "<p>Right. Six rights and three responsibilities. The full notice is posted in the reception area if you ever need to point someone to it.</p>",
    "incorrect_html": "<p>Not quite. A right is what the patient can expect from us. A responsibility is what we ask of them so that we can look after them safely. Look again at the three that ask the patient to <em>do</em> something.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-032>",
  "narration_text": "Nine statements from reception. Sort each: is it what the patient can expect, or what we ask of them?"
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
| Visual concept | Stem in large type; four plain option rows; no imagery, so the decision carries the screen |
| Layout | n/a (`mcq`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Calm |
| Target seconds | 8 |
| Word count / est. seconds | 20 words / ≈ 8.6 s |
| Cue targets | None |

> Last one here. A patient refuses a blood test after the doctor has explained the risks. What do you do?

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
  "objective_ids": ["hr-o2"],
  "points": 5,
  "evidence_screen_ids": ["hr-032"],
  "prompt_html": "<p>A patient refuses a blood test after the doctor has explained the risks. What is the right response?</p>",
  "options": [
    { "id": "a", "text_html": "Respect the refusal, check she understood the risks, document it, and tell the doctor", "correct": true,
      "feedback_html": "<p>Right. Refusal of treatment is a patient right once the risks are understood. Your job is to check understanding, document the refusal, and inform the doctor.</p>" },
    { "id": "b", "text_html": "Ask the clinic manager to persuade her to agree",
      "feedback_html": "<p>Bringing in a manager to talk her round turns a right into pressure. She can refuse once she understands the risks.</p>" },
    { "id": "c", "text_html": "Take the sample anyway, because the doctor ordered it",
      "feedback_html": "<p>Proceeding against a competent patient's refusal is not consent. Stop and escalate to the doctor instead.</p>" },
    { "id": "d", "text_html": "Ask a family member to consent instead",
      "feedback_html": "<p>A family member cannot replace her consent. Only she can decide, once she understands the risks.</p>" }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Right. Refusal of treatment is a patient right once the risks are understood. Your job is to check understanding, document the refusal, and inform the doctor.</p>",
    "incorrect_html": "<p>Not that one. A competent patient can refuse after the risks have been explained. Persuasion, proceeding anyway, or substituting a family member's consent all override a right.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-033>",
  "narration_text": "Last one here. A patient refuses a blood test after the doctor has explained the risks. What do you do?"
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
| Visual concept | Three cards in a row, each with a line icon and a short label; the third card carries a download affordance and a small PDF glyph; beneath them a single line states the rule “if it's a request, it goes through Oracle” |
| Layout | `text` |
| Colour roles | bg `light` · text `dark` · accent on the third card's download affordance only |
| Animation / reveal | Cards fade up left to right |
| Character | None |

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
| Tone | Practical, warm |
| Target seconds | 25 |
| Word count / est. seconds | 63 words / ≈ 27.8 s |
| Cue targets | `desk`, `oracle`, `pdf` |

> [[cue:desk]] Where help lives. First, your HR help desk — one per business unit, so you'll talk to people who know your clinic. [[pause:0.4]] [[cue:oracle]] Second, Oracle. If it's a request, it goes through Oracle. That's the only way it has a record. [[pause:0.4]] [[cue:pdf]] Third, the HR Quick Reference: two pages with every leave table and the pay rules. Download it now. You don't need to memorise this.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Your HR help desk</strong> — one per business unit. <em>Role mailbox addresses pending B6 / D5.</em></p><p><strong>Request everything in Oracle.</strong> If it's a request, it needs a record.</p><p><strong>Full rules:</strong> <a href=\"{{asset:hr-pdf-quickref}}\">HR Quick Reference (PDF, 2 pages)</a></p>",
  "narration_asset_id": "<hr-aud-040>",
  "narration_text": "Where help lives. First, your HR help desk — one per business unit, so you'll talk to people who know your clinic. Second, Oracle. If it's a request, it goes through Oracle. That's the only way it has a record. Third, the HR Quick Reference: two pages with every leave table and the pay rules. Download it now. You don't need to memorise this."
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
| Visual concept | Nine collapsed rows, each with a two-letter code chip on the left (AN, SK, WI, MA, EX, SC, HJ, CO, OH), the leave name, and a chevron; expanding shows one sentence of plain text plus a single “watch out” line where a rule trips people up |
| Layout | n/a (`accordion`) |
| Colour roles | bg `light` · text `dark` · accent on the chevron of the open panel only |
| Animation / reveal | 200 ms height transition on expand |
| Character | None |

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
| Tone | Practical |
| Target seconds | 40 |
| Word count / est. seconds | 91 words / ≈ 42.0 s |
| Cue targets | `intro`, `annual`, `sick`, `injury`, `maternity`, `exam`, `scientific`, `hajj`, `compass`, `holidays` |

> [[cue:intro]] Nine types. Open the ones you need. [[pause:0.3]] [[cue:annual]] Annual: after probation, five days carried over, used by end of March. [[pause:0.3]] [[cue:sick]] Sick: valid report needed. First thirty days paid in full. [[pause:0.3]] [[cue:injury]] Work injury covers commuting, and has a same-day or next-day deadline. [[pause:0.3]] [[cue:maternity]] Maternity: twelve weeks, starting up to four weeks early. [[pause:0.3]] [[cue:exam]] Exam leave: academic exams only, documents two weeks ahead. [[pause:0.3]] [[cue:scientific]] Scientific: by profession, and can't be carried over. [[pause:0.3]] [[cue:hajj]] Hajj: two years' service and a permit. [[pause:0.3]] [[cue:compass]] Compassionate: marriage, paternity, bereavement. [[pause:0.3]] [[cue:holidays]] Then Eid, Founding Day, National Day. [[pause:0.3]] We'll practise the four people ask about most.

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
  "prompt_html": "<p>Nine types. Open the one you need — the full tables are in the Quick Reference.</p>",
  "items": [
    { "title": "Annual", "body_html": "<p>After probation, with your line manager's approval. Carry over up to 5 days; use them by end of March (consulting-room physicians: end of June). <em>Pending B9.</em></p>" },
    { "title": "Sick", "body_html": "<p>Tell your line manager. Valid medical report required. First 30 days full pay; days 31–90 <em>pending B1</em>; days 91–120 unpaid.</p>" },
    { "title": "Work injury", "body_html": "<p>Covers work hours and commuting. <strong>Report to your line manager and HR the same day or the next day.</strong></p>" },
    { "title": "Maternity", "body_html": "<p>12 weeks. You may start up to 4 weeks before the expected delivery date.</p>" },
    { "title": "Exam", "body_html": "<p>Paid, for <strong>academic</strong> exams only. Actual exam days only. Documents at least 2 weeks in advance. IELTS, TOEFL and similar are not eligible.</p>" },
    { "title": "Scientific", "body_html": "<p>Paid days per profession each year, for academic exams. Needs the MD's pre-approval. <strong>Cannot be carried over.</strong> <em>Pending B10.</em></p>" },
    { "title": "Hajj", "body_html": "<p>Muslim employees with two full years of service. 10–15 days including Eid. Hajj permit copy required. <em>Pending B11.</em></p>" },
    { "title": "Compassionate", "body_html": "<p>Marriage 5 days · paternity 3 · immediate relative 5 · sibling 3 · death of a husband <em>pending B2</em>.</p>" },
    { "title": "Official holidays", "body_html": "<p>Eid al-Fitr 4 days · Eid al-Adha 4 days · Founding Day 22 February · National Day 23 September.</p>" }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-041>",
  "narration_text": "Nine types. Open the ones you need. Annual: after probation, five days carried over, used by end of March. Sick: valid report needed. First thirty days paid in full. Work injury covers commuting, and has a same-day or next-day deadline. Maternity: twelve weeks, starting up to four weeks early. Exam leave: academic exams only, documents two weeks ahead. Scientific: by profession, and can't be carried over. Hajj: two years' service and a permit. Compassionate: marriage, paternity, bereavement. Then Eid, Founding Day, National Day. We'll practise the four people ask about most."
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
| Visual concept | Two columns: four grade tiles on the left (H, G, F and Consultant, A to E) and four number tiles on the right (30, 27, 25, 22); a connector line follows the selection |
| Layout | n/a (`matching`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 14 words / ≈ 6.0 s |
| Cue targets | None |

> Four grades, four entitlements. Match each grade to its annual leave, in working days.

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
  "objective_ids": ["hr-o3"],
  "points": 5,
  "evidence_screen_ids": ["hr-041"],
  "prompt_html": "<p>Four grades, four entitlements. Match each grade to its annual leave, in working days. <em>Entitlement pending B9.</em></p>",
  "pairs": [
    { "id": "p1", "left_html": "Grade H", "right_html": "30 working days" },
    { "id": "p2", "left_html": "Grade G", "right_html": "27 working days" },
    { "id": "p3", "left_html": "Grade F and Consultant", "right_html": "25 working days" },
    { "id": "p4", "left_html": "Grades A to E", "right_html": "22 working days" }
  ],
  "feedback": {
    "correct_html": "<p>Right. Entitlement rises with grade: 30, 27, 25 and 22 working days. Your contract and the Quick Reference both show your own grade.</p>",
    "incorrect_html": "<p>Not quite. The entitlement rises with grade, from 22 working days at grades A to E up to 30 at grade H. Match them again.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-042>",
  "narration_text": "Four grades, four entitlements. Match each grade to its annual leave, in working days."
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
| Visual concept | A five-row vertical ledger on a white card: each row has a day band on the left, the action in the middle and a “Why?” control on the right; revealing a row slides its rationale panel open beneath the action |
| Layout | n/a (`worked_example`) |
| Colour roles | bg `light` · text `dark` · accent on the “Why?” control only |
| Animation / reveal | `fading: "partial"` — actions are visible, rationales sit behind a per-step reveal control |
| Character | None |

**Imagery:** None (the ledger is CSS; no artefact screenshots are needed).

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
| Tone | Calm, precise |
| Target seconds | 40 |
| Word count / est. seconds | 95 words / ≈ 43.2 s |
| Cue targets | `s1`, `s2`, `s3`, `s4`, `s5` |

> One example, properly. A colleague is off sick forty days in a year, with valid reports. [[cue:s1]] First, she tells her line manager — that's first, not last. [[pause:0.4]] [[cue:s2]] The first thirty days are paid in full. [[pause:0.4]] [[cue:s3]] Ten days fall into the next band, and that's where pay drops. [[pause:0.4]] Note the detail people miss: it's the total in the year that sets the band, not one spell. [[pause:0.5]] [[cue:s4]] Beyond ninety days it's unpaid. [[pause:0.4]] [[cue:s5]] And if the report is from outside My Clinic, the Staff Health Clinic must approve it. [[pause:0.4]] Now: what changes if her report comes from another hospital?

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
  "fading": "partial",
  "intro_html": "<p>A colleague is off sick for 40 days in one year, with valid medical reports from My Clinic. How is the pay worked out?</p>",
  "steps": [
    { "action_html": "<p><strong>Days 1–30</strong> — tell your line manager you are unwell.</p>",
      "rationale_html": "<p>Notification is the first requirement. Sick leave is accepted only with a valid medical report, and your manager needs to know today, not at the end of it.</p>" },
    { "action_html": "<p><strong>Days 1–30</strong> — full salary.</p>",
      "rationale_html": "<p>The first thirty days of valid sick leave in a year are paid in full.</p>" },
    { "action_html": "<p><strong>Days 31–40</strong> — reduced pay. <em>Per the slide as written: 25% deducted, so 75% of salary. Pending B1.</em></p>",
      "rationale_html": "<p>The second band cuts pay by a quarter. Continuous and separated periods count the same way, so the band follows the total days in the year, not one absence.</p>" },
    { "action_html": "<p><strong>Days 91–120</strong> — unpaid.</p>",
      "rationale_html": "<p>The bands run 1–30, 31–90 and 91–120. Forty days never reaches this band, but it's the ceiling you should know.</p>" },
    { "action_html": "<p>Check the report: from outside My Clinic, it needs <strong>Staff Health Clinic approval</strong>.</p>",
      "rationale_html": "<p>Reports from My Clinic are accepted as they are. Anything from another provider has to be approved, or the leave isn't valid.</p>" }
  ],
  "self_explanation_prompt_html": "<p>What changes if the medical report comes from another hospital?</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-043>",
  "narration_text": "One example, properly. A colleague is off sick forty days in a year, with valid reports. First, she tells her line manager — that's first, not last. The first thirty days are paid in full. Ten days fall into the next band, and that's where pay drops. Note the detail people miss: it's the total in the year that sets the band, not one spell. Beyond ninety days it's unpaid. And if the report is from outside My Clinic, the Staff Health Clinic must approve it. Now: what changes if her report comes from another hospital?"
}
```

#### 8. Notes for SME and developer

- Open questions: **B1** — the slide says “days 31–90: 25% deducted”. HR must confirm whether that means 75% of salary for days 31–90. The step text says exactly what the slide says and marks it pending; the narration deliberately does not state a percentage.
- Developer notes: `worked_example` carries no `points`. Do not score this screen.

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
| Visual concept | A flat service-desk illustration band at the top that stays constant; below it a single request card with the colleague's first name, role and question, then full-width choice buttons; a “3 of 4 answered” counter sits in the corner |
| Layout | n/a (`decision_scenario`) |
| Colour roles | bg `surface` · text `dark` · accent none during the decision |
| Animation / reveal | Request card fades up on each node change |
| Character | `mentor-noor`, pose `explaining` on node 1 and `neutral` on nodes 2–4 |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-leavedesk` | illustration | Flat office-desk scene: a desk, a laptop, a small plant, two chairs; brand colours, white background | ai-generated | “An HR service desk with a laptop and two chairs.” | No |
| `hr-char-noor` / `mentor-noor` | character | Program mentor, poses `explaining` and `neutral` | ai-generated | “Noor, a senior nurse and safety liaison, at the leave desk.” | No |

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
| Tone | Practical, warm |
| Target seconds | 15 |
| Word count / est. seconds | 27 words / ≈ 11.6 s |
| Cue targets | None |

> Now you're on the other side of the desk. Four colleagues, four questions. First: Yousuf, a lab technician, wants scientific leave and already has the MD's pre-approval.

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
  "objective_ids": ["hr-o3"],
  "points": 15,
  "evidence_screen_ids": ["hr-041"],
  "pass_score": 3,
  "start_node_id": "n1",
  "intro_html": "<p>Four colleagues, four questions. You're the one they've asked.</p>",
  "nodes": [
    { "id": "n1",
      "prompt_html": "<p><strong>Yousuf</strong> is a lab technician. He asks for two days of scientific leave, and he already has the MD's pre-approval for his documents. How many days can he take this year?</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        { "id": "n1a", "text_html": "Two days — that's the technician allowance, and unused days can't be carried over.", "score_delta": 1, "goto_node_id": "n2",
          "feedback_html": "<p>Right. Scientific leave is 2 days a year for lab and radiology technicians, 3 for nurses, 4 for pharmacists, 5 for other physicians and dentists, and 7 for consultants. It also can't be carried over.</p>" },
        { "id": "n1b", "text_html": "Seven days — that's the allowance.", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Seven days is the consultants' allowance. Technicians get two. The allowance follows the profession, not the request.</p>" },
        { "id": "n1c", "text_html": "None — scientific leave is only for consultants and physicians.", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Not so. Every profession in the table has an allowance; technicians have the smallest, at two days a year.</p>" },
        { "id": "n1d", "text_html": "Two days now, and he can carry the rest into next year.", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>The days are right, the carry-over isn't. Scientific leave cannot be carried over — unused days are lost.</p>" }
      ] },
    { "id": "n2",
      "prompt_html": "<p><strong>Amal</strong> is a nurse. She asks for exam leave to sit IELTS next month, and she has her documents ready.</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        { "id": "n2a", "text_html": "Refuse: IELTS is not an academic examination, and it's named as not eligible.", "score_delta": 1, "goto_node_id": "n3",
          "feedback_html": "<p>Right. Exam leave is paid leave for academic examinations only, and IELTS, TOEFL and Microsoft certifications are named as not eligible. Having the documents ready doesn't change eligibility.</p>" },
        { "id": "n2b", "text_html": "Approve it — she has her documents in on time.", "score_delta": 0, "goto_node_id": "n3",
          "feedback_html": "<p>Documents matter, but eligibility comes first. IELTS is not an academic examination and is named as not eligible.</p>" },
        { "id": "n2c", "text_html": "Approve half the exam days as a goodwill gesture.", "score_delta": 0, "goto_node_id": "n3",
          "feedback_html": "<p>Well meant, but the rule is about the type of exam, not the number of days. IELTS is not eligible, so there are no days to approve.</p>" }
      ] },
    { "id": "n3",
      "prompt_html": "<p><strong>Reem</strong> is a pharmacist with one full year of service. She asks for Hajj leave and has her Hajj permit ready.</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        { "id": "n3a", "text_html": "Not yet — Hajj leave needs two full years of continuous service.", "score_delta": 1, "goto_node_id": "n4",
          "feedback_html": "<p>Right. Two full years of continuous service is the eligibility rule, and one year doesn't meet it. The permit is needed, but it doesn't shorten the service requirement.</p>" },
        { "id": "n3b", "text_html": "Yes — one year of service is enough.", "score_delta": 0, "goto_node_id": "n4",
          "feedback_html": "<p>It isn't. Hajj leave is for Muslim employees with two full years of continuous service.</p>" },
        { "id": "n3c", "text_html": "Yes, now that she has the Hajj permit.", "score_delta": 0, "goto_node_id": "n4",
          "feedback_html": "<p>The permit is a requirement, not a substitute. Without two full years of service she isn't eligible, permit or not.</p>" }
      ] },
    { "id": "n4",
      "prompt_html": "<p><strong>Sara</strong> is a receptionist. She slipped on the way into work this morning and her ankle is painful. What does she need to do?</p>",
      "image_asset_id": "<hr-img-leavedesk>",
      "image_alt": "An HR service desk with a laptop and two chairs.",
      "choices": [
        { "id": "n4a", "text_html": "Tell her line manager and HR today or tomorrow — commuting is covered as a work injury.", "score_delta": 1, "goto_node_id": null,
          "feedback_html": "<p>Right. Work injury covers commuting as well as work hours, and the deadline is the same day or the following day. HR then reports the case to GOSI.</p>" },
        { "id": "n4b", "text_html": "Wait and see whether she needs time off before reporting it.", "score_delta": 0, "goto_node_id": null,
          "feedback_html": "<p>Waiting is the mistake this rule exists to prevent. The report has to go to her line manager and HR the same day or the next day, whether or not she ends up taking time off.</p>" },
        { "id": "n4c", "text_html": "Tell her commuting accidents aren't covered.", "score_delta": 0, "goto_node_id": null,
          "feedback_html": "<p>They are. Work injury applies during work hours and while commuting to and from work, for Saudi and expatriate employees alike.</p>" }
      ] }
  ],
  "feedback": {
    "correct_html": "<p>Three or four. You checked eligibility before you answered, which is the whole job at this desk: type of leave, who qualifies, and what document is missing.</p>",
    "incorrect_html": "<p>Fewer than three. The habit to build is to check three things every time — the type of leave, the eligibility rule, and the document. Two of these four turned on eligibility, not on paperwork.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-044>",
  "narration_text": "Now you're on the other side of the desk. Four colleagues, four questions. First: Yousuf, a lab technician, wants scientific leave and already has the MD's pre-approval."
}
```

#### 8. Notes for SME and developer

- Open questions: **B10** — slide 40's sentence about academic exams looks copied from the exam-leave slide. If HR confirms a different purpose for scientific leave, re-word `n1` and its feedback. **B11** — confirm the two-year service rule and the 10–15 day range for Hajj leave.
- Developer notes: `pass_score` 3 with four nodes means one wrong answer is tolerated. `n1` deliberately has four choices; the others have three. All four `n1` choices go to `n2`, so no path is short.

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
| Visual concept | One question at a time, centred, with three option rows; a thin progress strip at the top fills as items are answered and a small “est. 3 more” hint appears once the estimator has enough data |
| Layout | n/a (`adaptive_practice`) |
| Colour roles | bg `surface` · text `dark` · accent on the progress strip only |
| Animation / reveal | Question cross-fades between items |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 10 |
| Word count / est. seconds | 25 words / ≈ 10.7 s |
| Cue targets | None |

> A short practice set now. It adapts: if you're getting these, it will finish early. If you're not, it'll keep going for a few more.

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
  "objective_ids": ["hr-o3"],
  "points": 15,
  "evidence_screen_ids": ["hr-041"],
  "max_items": 6,
  "target_success": 0.7,
  "pass_ratio": 0.6,
  "adaptive": { "strategy": "elo" },
  "prompt_html": "<p>Answer until the practice says you're ready. It stops early if you've got it.</p>",
  "items": [
    { "id": "q1", "difficulty": 0.25, "prompt_html": "<p>How many unused annual leave days can you carry over?</p>",
      "options": [ { "id": "a", "text_html": "Up to 5", "correct": true }, { "id": "b", "text_html": "Up to 10" }, { "id": "c", "text_html": "All of them" } ],
      "explain_html": "<p>Carry-over is capped at 5 days. Anything above that is lost at the end of the carry-over window.</p>",
      "scaffold_html": "<p>The cap is a small number — single digits.</p>" },
    { "id": "q2", "difficulty": 0.35, "prompt_html": "<p>Carried-over annual leave must be used by when?</p>",
      "options": [ { "id": "a", "text_html": "End of March", "correct": true }, { "id": "b", "text_html": "End of June" }, { "id": "c", "text_html": "End of the year" } ],
      "explain_html": "<p>Carried-over leave has to be used by the end of March of the following year.</p>",
      "scaffold_html": "<p>It's the end of a spring month.</p>" },
    { "id": "q3", "difficulty": 0.65, "prompt_html": "<p>A consulting-room physician carries over leave. By when must it be used?</p>",
      "options": [ { "id": "a", "text_html": "End of March" }, { "id": "b", "text_html": "End of June", "correct": true }, { "id": "c", "text_html": "End of the year" } ],
      "explain_html": "<p>Consulting-room physicians have a later deadline: the end of June.</p>",
      "scaffold_html": "<p>This group gets three months more than everyone else.</p>" },
    { "id": "q4", "difficulty": 0.3, "prompt_html": "<p>How long is maternity leave?</p>",
      "options": [ { "id": "a", "text_html": "12 weeks", "correct": true }, { "id": "b", "text_html": "10 weeks" }, { "id": "c", "text_html": "8 weeks" } ],
      "explain_html": "<p>Maternity leave is 12 weeks.</p>",
      "scaffold_html": "<p>It's measured in weeks, not months — and it's the longest of the three options.</p>" },
    { "id": "q5", "difficulty": 0.6, "prompt_html": "<p>How early can maternity leave start?</p>",
      "options": [ { "id": "a", "text_html": "Up to 2 weeks before the due date" }, { "id": "b", "text_html": "Up to 4 weeks before the due date", "correct": true }, { "id": "c", "text_html": "On the due date only" } ],
      "explain_html": "<p>You may start up to 4 weeks before the expected delivery date.</p>",
      "scaffold_html": "<p>The allowance is measured in weeks before the due date.</p>" },
    { "id": "q6", "difficulty": 0.5, "prompt_html": "<p>Exam leave documents must be submitted how far in advance?</p>",
      "options": [ { "id": "a", "text_html": "At least 2 weeks", "correct": true }, { "id": "b", "text_html": "At least 1 week" }, { "id": "c", "text_html": "On the day of the exam" } ],
      "explain_html": "<p>Documents — the exam schedule and course schedule, plus a result transcript afterwards — must go in at least two weeks in advance.</p>",
      "scaffold_html": "<p>Think in weeks, and it's more than one.</p>" },
    { "id": "q7", "difficulty": 0.25, "prompt_html": "<p>How many days of leave for your own marriage?</p>",
      "options": [ { "id": "a", "text_html": "5 calendar days", "correct": true }, { "id": "b", "text_html": "3 days" }, { "id": "c", "text_html": "10 days" } ],
      "explain_html": "<p>Marriage leave is 5 calendar days.</p>",
      "scaffold_html": "<p>Marriage attracts the same number of days as bereavement of an immediate relative.</p>" },
    { "id": "q8", "difficulty": 0.3, "prompt_html": "<p>How many days of paternity leave?</p>",
      "options": [ { "id": "a", "text_html": "3 days", "correct": true }, { "id": "b", "text_html": "5 days" }, { "id": "c", "text_html": "7 days" } ],
      "explain_html": "<p>Paternity leave is 3 days.</p>",
      "scaffold_html": "<p>It's the same number as bereavement of a sibling.</p>" },
    { "id": "q9", "difficulty": 0.45, "prompt_html": "<p>Bereavement leave for the death of a sibling?</p>",
      "options": [ { "id": "a", "text_html": "3 calendar days", "correct": true }, { "id": "b", "text_html": "5 calendar days" }, { "id": "c", "text_html": "10 calendar days" } ],
      "explain_html": "<p>Death of a sibling is 3 calendar days. Death of an immediate relative — spouse, parent or child — is 5.</p>",
      "scaffold_html": "<p>Immediate relatives attract more days than siblings.</p>" },
    { "id": "q10", "difficulty": 0.2, "prompt_html": "<p>How many days is each Eid holiday?</p>",
      "options": [ { "id": "a", "text_html": "4 days each", "correct": true }, { "id": "b", "text_html": "3 days each" }, { "id": "c", "text_html": "5 days each" } ],
      "explain_html": "<p>Eid al-Fitr and Eid al-Adha are each 4 days.</p>",
      "scaffold_html": "<p>Both Eids are the same length.</p>" },
    { "id": "q11", "difficulty": 0.4, "prompt_html": "<p>When is Founding Day?</p>",
      "options": [ { "id": "a", "text_html": "22 February", "correct": true }, { "id": "b", "text_html": "23 September" }, { "id": "c", "text_html": "1 January" } ],
      "explain_html": "<p>Founding Day is 22 February. National Day is 23 September — the two are easy to swap.</p>",
      "scaffold_html": "<p>It's a February date, and the other national holiday falls in September.</p>" },
    { "id": "q12", "difficulty": 0.55, "prompt_html": "<p>Can unused scientific leave be carried over?</p>",
      "options": [ { "id": "a", "text_html": "No, never", "correct": true }, { "id": "b", "text_html": "Yes, up to 5 days" }, { "id": "c", "text_html": "Yes, with the MD's approval" } ],
      "explain_html": "<p>Scientific leave cannot be carried over. It also needs the MD's pre-approval, but approval doesn't create a carry-over.</p>",
      "scaffold_html": "<p>Approval and carry-over are two different rules; only one of them is mentioned in the source.</p>" }
  ],
  "feedback": {
    "correct_html": "<p>You've got the leave numbers. Carry-over, maternity, compassionate and the holidays are the four people ask about most — they're all in the Quick Reference.</p>",
    "incorrect_html": "<p>Leave numbers are worth a second look in the HR Quick Reference. The ones people mix up are the carry-over deadline, Founding Day versus National Day, and sibling versus immediate-relative bereavement.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-045>",
  "narration_text": "A short practice set now. It adapts: if you're getting these, it will finish early. If you're not, it'll keep going for a few more."
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
| Visual concept | A horizontal stacked bar split 9.75 / 11.75 across the full width, labelled “you” and “My Clinic” under each segment and “21.5% total” above; beneath it a single line naming what the contribution buys |
| Layout | `text` |
| Colour roles | bg `light` · text `dark` · accent on the “you” segment only (the number that appears on the payslip) |
| Animation / reveal | Bar grows from zero, then the two segment labels fade in, then the total |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-gosi-bar` | SVG | 960×200 authored SVG stacked bar, two segments; percentages as real text, not baked in | own | “GOSI contribution: the employee pays 9.75%, My Clinic pays 11.75%, a total of 21.5%.” | No |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Calm, practical |
| Target seconds | 30 |
| Word count / est. seconds | 62 words / ≈ 27.4 s |
| Cue targets | `what`, `who`, `split` |

> [[cue:what]] GOSI is the General Organization for Social Insurance — the government body for social protection in Saudi Arabia. [[pause:0.4]] [[cue:who]] It applies to Saudi employees, until retirement at sixty. [[pause:0.4]] [[cue:split]] The split matters: you pay nine point seven five per cent of basic plus housing. My Clinic pays eleven point seven five. So the real contribution is twenty-one point five, and most of it isn't yours.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>GOSI</strong> — General Organization for Social Insurance.</p><p>Saudi employees only, until retirement at 60.</p><p>9.75% you + 11.75% My Clinic = <strong>21.5%</strong> of basic + housing. <em>Rates pending B12.</em></p>",
  "media_asset_id": "<hr-img-gosi-bar>",
  "media_alt": "GOSI contribution: the employee pays 9.75%, My Clinic pays 11.75%, a total of 21.5%.",
  "narration_asset_id": "<hr-aud-050>",
  "narration_text": "GOSI is the General Organization for Social Insurance — the government body for social protection in Saudi Arabia. It applies to Saudi employees, until retirement at sixty. The split matters: you pay nine point seven five per cent of basic plus housing. My Clinic pays eleven point seven five. So the real contribution is twenty-one point five, and most of it isn't yours."
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
| Visual concept | A three-row calculation ledger: each row shows one line of arithmetic in large mono-ish numerals with a “Why?” control to the right; the final row is boxed and carries the answer in the accent colour plus a SAR label |
| Layout | n/a (`worked_example`) |
| Colour roles | bg `light` · text `dark` · accent on the final answer row only |
| Animation / reveal | `fading: "partial"` — the arithmetic is visible, the rationale is behind a per-step control |
| Character | None |

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
| Tone | Calm, precise |
| Target seconds | 30 |
| Word count / est. seconds | 65 words / ≈ 28.7 s |
| Cue targets | `s1`, `s2`, `s3` |

> Let's do one together. Basic four thousand eight hundred, housing one thousand two hundred. [[cue:s1]] Add them — GOSI is charged on basic plus housing, so six thousand. [[pause:0.4]] [[cue:s2]] Apply your rate, nine point seven five per cent. The company's rate never touches your payslip. [[pause:0.4]] [[cue:s3]] Six thousand times nought point nought nine seven five is five hundred and eighty-five riyals a month. That's the line to look for.

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
  "fading": "partial",
  "intro_html": "<p>Basic 4,800 + housing 1,200. What is the monthly GOSI deduction from your salary? <em>Rates pending B12.</em></p>",
  "steps": [
    { "action_html": "<p>Add basic and housing: 4,800 + 1,200 = <strong>6,000</strong>.</p>",
      "rationale_html": "<p>GOSI is charged on basic salary <strong>plus housing allowance</strong>, not on basic alone and not on total pay with allowances and bonuses.</p>" },
    { "action_html": "<p>Apply the employee rate: 6,000 × <strong>9.75%</strong>.</p>",
      "rationale_html": "<p>Only your share is deducted from your salary. The company's 11.75% is paid on top and never appears as a deduction on your payslip.</p>" },
    { "action_html": "<p>Result: <strong>585 SAR</strong> deducted each month.</p>",
      "rationale_html": "<p>6,000 × 0.0975 = 585. This is the line you'll see on your payslip.</p>" }
  ],
  "self_explanation_prompt_html": "<p>Which part of the salary is the percentage applied to?</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-051>",
  "narration_text": "Let's do one together. Basic four thousand eight hundred, housing one thousand two hundred. Add them — GOSI is charged on basic plus housing, so six thousand. Apply your rate, nine point seven five per cent. The company's rate never touches your payslip. Six thousand times nought point nought nine seven five is five hundred and eighty-five riyals a month. That's the line to look for."
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
| Visual concept | A large centred equation with a single inline input at the blank; beneath it a small muted line reminding the learner of the two inputs, and nothing else — no imagery to distract from the arithmetic |
| Layout | n/a (`fill_blank`) |
| Colour roles | bg `surface` · text `dark` · accent on the input's focus ring only |
| Animation / reveal | None |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 15 words / ≈ 6.4 s |
| Cue targets | None |

> Your turn. Basic six thousand, housing one thousand five hundred. What's your monthly GOSI deduction?

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
  "objective_ids": ["hr-o4"],
  "points": 10,
  "evidence_screen_ids": ["hr-051"],
  "case_sensitive": false,
  "prompt_html": "<p>Basic 6,000 + housing 1,500. Your monthly GOSI deduction = ___ SAR. <em>Rates pending B12.</em></p>",
  "blanks": [
    { "id": "b1", "accepted": ["731.25", "731.25 SAR", "731.25 SR", "731.25 riyals", "731.25 Saudi riyals", "731", "731 SAR"] }
  ],
  "feedback": {
    "correct_html": "<p>Right. Basic 6,000 + housing 1,500 = 7,500, and 7,500 × 9.75% = <strong>731.25 SAR</strong> a month.</p>",
    "incorrect_html": "<p>Not quite. Add basic and housing first — that's 7,500 — then take 9.75% of that, not of the basic alone.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-052>",
  "narration_text": "Your turn. Basic six thousand, housing one thousand five hundred. What's your monthly GOSI deduction?"
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
| Visual concept | A three-row ledger like `hr-051`, but the third row forks into two stacked results — “normal day ×1.5” and “public holiday ×2” — so the learner sees one rate and two multipliers |
| Layout | n/a (`worked_example`) |
| Colour roles | bg `light` · text `dark` · accent on the two result figures only |
| Animation / reveal | `fading: "partial"` |
| Character | None |

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
| Tone | Calm, precise |
| Target seconds | 35 |
| Word count / est. seconds | 79 words / ≈ 35.5 s |
| Cue targets | `s1`, `s2`, `s3`, `elig` |

> [[cue:elig]] One caveat before the numbers: whether you're eligible for overtime at all depends on your grade. Check that first. [[pause:0.4]] [[cue:s1]] Now the arithmetic. Basic six thousand. Divide by thirty days times eight hours — two hundred and forty hours — and you get twenty-five riyals an hour. [[pause:0.4]] [[cue:s2]] On a normal working day, multiply by one and a half. That's thirty-seven riyals fifty. [[pause:0.4]] [[cue:s3]] On a public holiday, multiply by two. Fifty riyals an hour. [[pause:0.4]] Same hourly rate both times. Only the multiplier moves.

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
  "fading": "partial",
  "intro_html": "<p>Basic 6,000. What is your overtime rate on a normal working day, and on a public holiday? <em>Eligibility by grade pending B3.</em></p>",
  "steps": [
    { "action_html": "<p>Hourly rate: 6,000 ÷ (30 × 8) = 6,000 ÷ 240 = <strong>25 SAR/hour</strong>.</p>",
      "rationale_html": "<p>The formula uses a 30-day month at 8 hours a day, so 240 hours. Everything else in the calculation hangs off this one number.</p>" },
    { "action_html": "<p>Normal working day: 25 × 1.5 = <strong>37.50 SAR/hour</strong>.</p>",
      "rationale_html": "<p>Overtime on a normal working day is paid at time and a half.</p>" },
    { "action_html": "<p>Public holiday: 25 × 2 = <strong>50 SAR/hour</strong>.</p>",
      "rationale_html": "<p>Overtime on a public holiday is paid at double time. Note it's the same hourly rate — only the multiplier changes.</p>" }
  ],
  "self_explanation_prompt_html": "<p>Why is the hourly rate worked out from 240 hours, not 208?</p>",
  "reveal": "none",
  "narration_asset_id": "<hr-aud-053>",
  "narration_text": "One caveat before the numbers: whether you're eligible for overtime at all depends on your grade. Check that first. Now the arithmetic. Basic six thousand. Divide by thirty days times eight hours — two hundred and forty hours — and you get twenty-five riyals an hour. On a normal working day, multiply by one and a half. That's thirty-seven riyals fifty. On a public holiday, multiply by two. Fifty riyals an hour. Same hourly rate both times. Only the multiplier moves."
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
| Visual concept | Stem in large type; four plain option rows, each a single amount; no imagery, so the arithmetic carries the screen |
| Layout | n/a (`mcq`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 20 words / ≈ 8.6 s |
| Cue targets | None |

> One for you. Basic six thousand. You work four overtime hours on a normal working day. What's the overtime pay?

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
  "objective_ids": ["hr-o4"],
  "points": 10,
  "evidence_screen_ids": ["hr-053"],
  "prompt_html": "<p>Basic 6,000. You work 4 overtime hours on a normal working day. What is the overtime pay?</p>",
  "options": [
    { "id": "a", "text_html": "150 SAR", "correct": true,
      "feedback_html": "<p>Right. Hourly rate is 6,000 ÷ 240 = 25, then 25 × 1.5 × 4 hours = 150 SAR.</p>" },
    { "id": "b", "text_html": "100 SAR",
      "feedback_html": "<p>That's 25 × 4. You've worked out the plain hourly pay and left out the time-and-a-half multiplier.</p>" },
    { "id": "c", "text_html": "200 SAR",
      "feedback_html": "<p>That's 25 × 2 × 4. Double time is for a public holiday, not a normal working day.</p>" },
    { "id": "d", "text_html": "240 SAR",
      "feedback_html": "<p>That doesn't come from the formula. Go back to the hourly rate first: 6,000 ÷ 240.</p>" }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Right. Hourly rate is 6,000 ÷ 240 = 25, then 25 × 1.5 × 4 hours = 150 SAR.</p>",
    "incorrect_html": "<p>Not quite. Build it in three moves: 6,000 ÷ 240 = 25 an hour, × 1.5 for a normal day, × 4 hours.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-054>",
  "narration_text": "One for you. Basic six thousand. You work four overtime hours on a normal working day. What's the overtime pay?"
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
| Visual concept | Two columns: six task cards on the left, four system tiles on the right, each system tile carrying a small monogram (O, Q, M, I); a connector line follows the selection |
| Layout | n/a (`matching`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Practical |
| Target seconds | 10 |
| Word count / est. seconds | 19 words / ≈ 8.1 s |
| Cue targets | None |

> Six tasks, four systems. Match each one to where it actually happens. Most of them are the same system.

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
  "objective_ids": ["hr-o5"],
  "points": 10,
  "evidence_screen_ids": ["hr-040"],
  "prompt_html": "<p>Six tasks, four systems. Match each task to where it happens.</p>",
  "pairs": [
    { "id": "p1", "left_html": "Request annual leave", "right_html": "Oracle" },
    { "id": "p2", "left_html": "Ask for an employment certificate", "right_html": "Oracle" },
    { "id": "p3", "left_html": "Accept your employment contract", "right_html": "Qiwa" },
    { "id": "p4", "left_html": "Renew your professional licence", "right_html": "Mumaris (SCFHS)" },
    { "id": "p5", "left_html": "Read the employee guide and corporate discounts", "right_html": "Intranet" },
    { "id": "p6", "left_html": "Resign", "right_html": "Oracle" }
  ],
  "feedback": {
    "correct_html": "<p>Right. Three of the six run through Oracle, because they're all requests that need a record. Contracts are accepted on Qiwa, licences are renewed on Mumaris, and the guide lives on the intranet.</p>",
    "incorrect_html": "<p>Not all six. Ask yourself which of these are <em>requests</em> — those go through Oracle. The contract and the licence are external platforms, and the guide is just reading.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-060>",
  "narration_text": "Six tasks, four systems. Match each one to where it actually happens. Most of them are the same system."
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
| Visual concept | A browser-chrome frame holding a full-width screenshot; a numbered instruction bar sits directly above the frame; the correct region is not outlined until the learner asks for a hint, at which point a dashed rectangle appears around it |
| Layout | n/a (`simulation`) |
| Colour roles | bg `surface` · text `dark` · accent on the hint rectangle only |
| Animation / reveal | The next screenshot cross-fades in on a correct click |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-oracle-1` | screenshot | Oracle Applications Cloud sign-in page, test account, 1920×1080 | own (test account — B8) | “Oracle sign-in page with empty username and password fields and a Sign In button.” | No |
| `hr-img-oracle-2` | screenshot | Oracle home with the Time and Absences tile | own (test account — B8) | “Oracle home page with a Time and Absences tile in the quick actions area.” | No |
| `hr-img-oracle-3` | screenshot | Time and Absences hub with the Add Leaves tile | own (test account — B8) | “Oracle Time and Absences page with an Add Leaves tile.” | No |
| `hr-img-oracle-4` | screenshot | Add Leaves form with the leave-type drop-down open, showing Annual, Bereavement, Marriage, Scientific, Sick, Study | own (test account — B8) | “Oracle Add Leaves form with the leave-type drop-down open.” | No |
| `hr-img-oracle-5` | screenshot | Add Leaves form filled, with a Submit button | own (test account — B8) | “Oracle Add Leaves form with dates entered and a Submit button.” | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Steps | See the table below. All five are click steps with `rect` regions. |
| Correct answer(s) | One region per step, `correct: true` |
| Points | 15 |
| Feedback — correct | That's the whole flow: sign in, Time and Absences, Add Leaves, choose the leave type and dates, submit. Your manager approves it in the same system, so you can see where it's got to. |
| Feedback — incorrect | Not every step. The route is always the same: sign in, then Time and Absences, then Add Leaves. The last two steps are the form itself. |
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
| Tone | Practical, calm |
| Target seconds | 15 |
| Word count / est. seconds | 27 words / ≈ 11.6 s |
| Cue targets | None |

> Let's do it once for real, on a test account. Book yourself a week of annual leave. Five steps, and I'll tell you what to look for.

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
  "objective_ids": ["hr-o5"],
  "points": 15,
  "evidence_screen_ids": ["hr-060"],
  "prompt_html": "<p>Five steps. These screenshots come from a test account, so nothing here is real.</p>",
  "steps": [
    { "image_asset_id": "<hr-img-oracle-1>",
      "image_alt": "Oracle sign-in page with empty username and password fields and a Sign In button.",
      "instruction_html": "<p>Sign in to Oracle.</p>",
      "regions": [ { "id": "signin", "shape": "rect", "coords": [1180, 620, 180, 56], "correct": true, "label_html": "Sign In" } ],
      "hint_html": "<p>Use the <em>Sign In</em> button under the password field.</p>" },
    { "image_asset_id": "<hr-img-oracle-2>",
      "image_alt": "Oracle home page with a Time and Absences tile in the quick actions area.",
      "instruction_html": "<p>Open the area where you manage your time and leave.</p>",
      "regions": [ { "id": "timeabs", "shape": "rect", "coords": [260, 300, 320, 200], "correct": true, "label_html": "Time and Absences" } ],
      "hint_html": "<p>Look for <em>Time and Absences</em> in the quick actions.</p>" },
    { "image_asset_id": "<hr-img-oracle-3>",
      "image_alt": "Oracle Time and Absences page with an Add Leaves tile.",
      "instruction_html": "<p>Open the page where you add a new leave request.</p>",
      "regions": [ { "id": "addleaves", "shape": "rect", "coords": [420, 310, 220, 140], "correct": true, "label_html": "Add Leaves" } ],
      "hint_html": "<p>Look for <em>Add Leaves</em> under Time and Absences.</p>" },
    { "image_asset_id": "<hr-img-oracle-4>",
      "image_alt": "Oracle Add Leaves form with the leave-type drop-down open.",
      "instruction_html": "<p>Choose <em>Annual</em> from the leave-type list.</p>",
      "regions": [ { "id": "leavetype", "shape": "rect", "coords": [300, 260, 420, 60], "correct": true, "label_html": "Leave type" } ],
      "hint_html": "<p>The leave type is a drop-down near the top of the form.</p>" },
    { "image_asset_id": "<hr-img-oracle-5>",
      "image_alt": "Oracle Add Leaves form with dates entered and a Submit button.",
      "instruction_html": "<p>Send the request.</p>",
      "regions": [ { "id": "submit", "shape": "rect", "coords": [1500, 900, 180, 56], "correct": true, "label_html": "Submit" } ],
      "hint_html": "<p><em>Submit</em> sits at the bottom of the form.</p>" }
  ],
  "feedback": {
    "correct_html": "<p>That's the whole flow: sign in, Time and Absences, Add Leaves, choose the leave type and dates, submit. Your manager approves it in the same system, so you can see where it's got to.</p>",
    "incorrect_html": "<p>Not every step. The route is always the same: sign in, then Time and Absences, then Add Leaves. The last two steps are the form itself.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-061>",
  "narration_text": "Let's do it once for real, on a test account. Book yourself a week of annual leave. Five steps, and I'll tell you what to look for."
}
```

#### 8. Notes for SME and developer

- Open questions: **B8** — every screenshot must come from a test account with no real employee data. Until HRIS supplies them, this screen cannot be built; ship the module without it and add it in a minor version, or replace it with a five-step `sorting` screen (a plan change, because the points and the objective evidence both move).
- Developer notes: `coords` for `rect` are `[x, y, w, h]` in the image's natural pixels. All five sets above are **provisional** against 1920×1080 screenshots and must be re-measured after the final captures. Record the Oracle release in the asset notes and re-capture when the UI changes (phase-5 trigger).

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
| Visual concept | The statement in large type centred, with two wide side-by-side buttons beneath labelled True and False; no imagery, so the judgement carries the screen |
| Layout | n/a (`true_false`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Serious |
| Target seconds | 8 |
| Word count / est. seconds | 19 words / ≈ 8.1 s |
| Cue targets | None |

> True or false: if your licence expires in under thirty days without renewal, HR may suspend you from work.

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
  "objective_ids": ["hr-o5"],
  "points": 5,
  "evidence_screen_ids": ["hr-060"],
  "prompt_html": "<p>If your professional licence will expire in less than 30 days without renewal, HR may suspend you from work. <em>Pending B13.</em></p>",
  "correct": true,
  "feedback": {
    "correct_html": "<p>True. With fewer than 30 days to expiry and no renewal, HR may suspend you. Renew early on Mumaris: My Clinic covers the expense claim, but it does not pay penalties for late renewal.</p>",
    "incorrect_html": "<p>It's true. My Clinic may suspend you if your licence has under 30 days left and hasn't been renewed. Renew on Mumaris well before that — the company pays the fee claim, not the late penalties.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-062>",
  "narration_text": "True or false: if your licence expires in under thirty days without renewal, HR may suspend you from work."
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
| Visual concept | A two-card row: the left card shows an ID badge with a small warning line about lost cards; the right card is a six-segment benefits wheel, each segment labelled with a one- or two-word benefit and a line icon |
| Layout | `text` (blocks: image, caption, image, caption) |
| Colour roles | bg `light` · text `dark` · accent on the lost-card warning line only |
| Animation / reveal | Left card fades up, then the wheel segments fill in sequence |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-idcard` | illustration | Flat ID badge on a lanyard, first name only, no real logo until approved | ai-generated | “A My Clinic staff ID badge on a lanyard.” | No |
| `hr-img-benefits-wheel` | SVG | 600×600 six-segment wheel: health insurance, performance bonus, development, hybrid work, internal advancement, discounts; labels as real text | own | “Benefits wheel: health insurance, annual performance bonuses, employee development, hybrid work, internal advancement and discounts.” | No |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Practical, warm |
| Target seconds | 25 |
| Word count / est. seconds | 57 words / ≈ 25.2 s |
| Cue targets | `id`, `lost`, `wheel` |

> [[cue:id]] Two quick things. Your ID card: wear it where it can be seen. [[pause:0.4]] [[cue:lost]] Lose it, and you email HR — there's a replacement fee. Damage it, and it's replaced free. [[pause:0.4]] [[cue:wheel]] Second, what you can use from day one: health insurance, performance bonuses, development, the hybrid work policy, internal advancement and discounts. Look at the ones you'd actually use.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "blocks": [
    { "html": "<p><strong>Lost card</strong> — email HR. Replacement fee <em>pending B4</em>.</p><p><strong>Damaged card</strong> — replaced free of charge.</p>" },
    { "asset_id": "<hr-img-idcard>", "caption": "A My Clinic staff ID badge on a lanyard." },
    { "html": "<p><strong>Benefits from day one:</strong> health insurance · annual performance bonuses · employee development · hybrid work policy · internal advancement · discounts.</p>" },
    { "asset_id": "<hr-img-benefits-wheel>", "caption": "Benefits wheel: health insurance, annual performance bonuses, employee development, hybrid work, internal advancement and discounts." }
  ],
  "narration_asset_id": "<hr-aud-070>",
  "narration_text": "Two quick things. Your ID card: wear it where it can be seen. Lose it, and you email HR — there's a replacement fee. Damage it, and it's replaced free. Second, what you can use from day one: health insurance, performance bonuses, development, the hybrid work policy, internal advancement and discounts. Look at the ones you'd actually use."
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
| Visual concept | Three drop zones in a row, each headed by a small flat figure illustration showing the outfit; six draggable chips sit in a wrap row beneath; a placed chip shows a border and an index number |
| Layout | n/a (`drag_drop`) |
| Colour roles | bg `surface` · text `dark` · accent on the drop-zone hover outline only |
| Animation / reveal | Chips settle with a 120 ms spring when dropped |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-dress-frontoffice` | illustration | Flat figure in a clinic uniform, standing, neutral background | ai-generated | “A front-office colleague in the clinic uniform.” | No |
| `hr-img-dress-medical` | illustration | Flat figure in scrubs and a coat, with a stethoscope | ai-generated | “A clinical colleague in scrubs and a coat.” | No |
| `hr-img-dress-backoffice` | illustration | Flat figure in business attire | ai-generated | “A back-office colleague in business attire.” | No |

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
| Tone | Practical |
| Target seconds | 8 |
| Word count / est. seconds | 20 words / ≈ 8.6 s |
| Cue targets | None |

> Six dress-code rules, three groups. Put each one where it applies — and pay attention to the one about casual days.

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
  "objective_ids": ["hr-o6"],
  "points": 10,
  "evidence_screen_ids": ["hr-070"],
  "prompt_html": "<p>Six rules, three groups. Place each rule where it applies.</p>",
  "targets": [
    { "id": "front", "label_html": "Front office" },
    { "id": "medical", "label_html": "Medical team" },
    { "id": "back", "label_html": "Back office" }
  ],
  "items": [
    { "id": "it1", "text_html": "Uniform for every shift", "correct_target_id": "front" },
    { "id": "it2", "text_html": "Scrubs and coat", "correct_target_id": "medical" },
    { "id": "it3", "text_html": "Business attire", "correct_target_id": "back" },
    { "id": "it4", "text_html": "Minimal jewellery", "correct_target_id": "medical" },
    { "id": "it5", "text_html": "Professional shoes", "correct_target_id": "medical" },
    { "id": "it6", "text_html": "No casual days", "correct_target_id": "back" }
  ],
  "feedback": {
    "correct_html": "<p>Right. Front office wears the clinic uniform. The medical team wears scrubs and a coat with professional shoes and minimal jewellery. Back office is business attire, with no casual days.</p>",
    "incorrect_html": "<p>Not all six. Three of them belong to the medical team, two to back office and one to front office. The one people mix up is “no casual days” — that's the back-office wording; front office says “no casual attire”.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-071>",
  "narration_text": "Six dress-code rules, three groups. Put each one where it applies — and pay attention to the one about casual days."
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
| Visual concept | A short horizontal four-step strip — Qiwa, Oracle, two months, 15 days — with an arrow between each; each step carries a one-line caption beneath it and a small line icon above |
| Layout | `text` |
| Colour roles | bg `light` · text `dark` · accent on the “2 months” figure only |
| Animation / reveal | Steps fade in left to right in narration order |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-img-exit-icons` | SVG ×4 | Line icons: document-signature (Qiwa), screen-and-form (Oracle), calendar (notice period), envelope-with-certificate (EOS) | own | Decorative — each step is labelled in text. | Yes |

#### 4. Interaction and scoring

n/a — unscored content screen.

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Calm, matter-of-fact |
| Target seconds | 25 |
| Word count / est. seconds | 52 words / ≈ 23.5 s |
| Cue targets | `qiwa`, `oracle`, `notice`, `eos` |

> [[cue:qiwa]] Two ends of one story. Starting: you accept your contract on Qiwa, the Ministry of Human Resources platform. [[pause:0.4]] [[cue:oracle]] Leaving: a resignation is a request, so it goes through Oracle. [[pause:0.4]] [[cue:notice]] Notice is two months, and it runs both ways. [[pause:0.4]] [[cue:eos]] End-of-service benefits and your experience certificate follow within fifteen days of your last day.

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
  "layout": "text",
  "animation": "fade-up",
  "reveal": "auto",
  "body_html": "<p><strong>Accept your contract</strong> on Qiwa.</p><p><strong>Resign</strong> in Oracle.</p><p><strong>Notice: 2 months</strong>, honoured by both parties.</p><p><strong>EOS + experience certificate</strong> within 15 days of your last working day.</p>",
  "narration_asset_id": "<hr-aud-080>",
  "narration_text": "Two ends of one story. Starting: you accept your contract on Qiwa, the Ministry of Human Resources platform. Leaving: a resignation is a request, so it goes through Oracle. Notice is two months, and it runs both ways. End-of-service benefits and your experience certificate follow within fifteen days of your last day."
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
| Visual concept | Stem in large type; four plain option rows; no imagery, so the decision carries the screen |
| Layout | n/a (`mcq`) |
| Colour roles | bg `surface` · text `dark` · accent none during the attempt |
| Animation / reveal | None |
| Character | None |

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
| Tone | Calm |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 6.9 s |
| Cue targets | None |

> Last scenario. You've accepted a new job starting in three weeks. What happens with your notice?

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
  "objective_ids": ["hr-o6"],
  "points": 5,
  "evidence_screen_ids": ["hr-080"],
  "prompt_html": "<p>You accept a new job starting in 3 weeks. What happens with your notice?</p>",
  "options": [
    { "id": "a", "text_html": "You must serve the contractual 2 months unless My Clinic agrees otherwise; submit the resignation in Oracle", "correct": true,
      "feedback_html": "<p>Right. The notice period is two months and it binds both sides, unless My Clinic agrees to something different. And a resignation is a request, so it goes in through Oracle.</p>" },
    { "id": "b", "text_html": "You can leave in 3 weeks — a new job overrides the notice period",
      "feedback_html": "<p>A new job doesn't override the contract. The two months stands unless My Clinic agrees to shorten it.</p>" },
    { "id": "c", "text_html": "Email your manager; Oracle is only for leave requests",
      "feedback_html": "<p>Oracle isn't only for leave. Resignation, letters and certificates are all service requests, and they need a record.</p>" },
    { "id": "d", "text_html": "Give one month: notice is shorter for grades A to E",
      "feedback_html": "<p>The notice period in your contract isn't set by grade in this policy. Assume two months unless your contract says otherwise.</p>" }
  ],
  "multi_select": false,
  "feedback": {
    "correct_html": "<p>Right. The notice period is two months and it binds both sides, unless My Clinic agrees to something different. And a resignation is a request, so it goes in through Oracle.</p>",
    "incorrect_html": "<p>Not that one. The contractual notice is two months, and it binds both sides. You can always ask HR whether they'll agree to less, but you can't assume it.</p>",
    "show_correct_answer": true
  },
  "reveal": "none",
  "narration_asset_id": "<hr-aud-081>",
  "narration_text": "Last scenario. You've accepted a new job starting in three weeks. What happens with your notice?"
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
| Visual concept | Six rows, each with the objective name, a thin bar showing the percentage, and the points earned over points available; any row below the threshold expands to show one line of advice beneath it |
| Layout | n/a (`results_breakdown`) |
| Colour roles | bg `surface` · text `dark` · accent on the advice rows only |
| Animation / reveal | Rows fade up in sequence; bars grow from zero |
| Character | None |

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
| Tone | Encouraging |
| Target seconds | 12 |
| Word count / est. seconds | 28 words / ≈ 12.0 s |
| Cue targets | None |

> Here's where you landed, objective by objective. Anything under seventy per cent has a note beside it. It's a list of where to look next, not a verdict.

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
  "body_html": "<p>One row per objective. Anything below 70% comes with a suggestion.</p>",
  "weak_threshold": 70,
  "show_total": true,
  "sections": [
    { "title": "Values & strategy", "screen_ids": ["hr-011", "hr-013"],
      "advice_html": "<p>Revisit the four values and the 7C pillars. The one to remember: Care is where My Care and patient loyalty sit.</p>" },
    { "title": "Ethics & patients' rights", "screen_ids": ["hr-031", "hr-032", "hr-033"],
      "advice_html": "<p>Disclose conflicts early, never trade access to care, and when you're unsure, report within 24 hours. A right is what the patient can expect; a responsibility is what we ask of them.</p>" },
    { "title": "Leave", "screen_ids": ["hr-042", "hr-044", "hr-045"],
      "advice_html": "<p>Check three things on every request: the type of leave, the eligibility rule, and the document. The tables are in the HR Quick Reference.</p>" },
    { "title": "Pay & social insurance", "screen_ids": ["hr-052", "hr-054"],
      "advice_html": "<p>GOSI is basic plus housing × 9.75%. Overtime is basic ÷ 240, then × 1.5, or × 2 on a public holiday.</p>" },
    { "title": "Systems & licences", "screen_ids": ["hr-060", "hr-061", "hr-062"],
      "advice_html": "<p>Requests go through Oracle. Contracts on Qiwa, licences on Mumaris, guides on the intranet. Renew your licence well before it expires.</p>" },
    { "title": "ID, dress code & contracts", "screen_ids": ["hr-071", "hr-081"],
      "advice_html": "<p>Front office wears the uniform, the medical team wears scrubs and a coat, back office is business attire. Notice is two months both ways.</p>" }
  ],
  "reveal": "none",
  "narration_asset_id": "<hr-aud-090>",
  "narration_text": "Here's where you landed, objective by objective. Anything under seventy per cent has a note beside it. It's a list of where to look next, not a verdict."
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
| Visual concept | A five-item checklist on the left, each with a small tick glyph; on the right two stacked action cards — one for the HR Quick Reference download, one for the onboarding survey — and a single line naming the next module |
| Layout | n/a (`summary`) |
| Colour roles | bg `light` · text `dark` · accent on the two action cards only |
| Animation / reveal | Checklist ticks in one by one, then the action cards fade up |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hr-pdf-quickref` | PDF | Same asset as `hr-040` | own | n/a | n/a |

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
| Tone | Warm |
| Target seconds | 25 |
| Word count / est. seconds | 61 words / ≈ 27.0 s |
| Cue targets | `list`, `pdf`, `survey`, `next` |

> [[cue:list]] That's the induction. You can now live the values, raise a concern the right way, and answer the leave and pay questions. You'll also know which system to use. [[pause:0.3]] [[cue:pdf]] Download the HR Quick Reference. [[pause:0.3]] [[cue:survey]] Please complete the onboarding survey — two minutes, and it shapes how we run this day. [[pause:0.3]] [[cue:next]] Next: clinical governance, quality, patient safety and risk. Welcome to My Clinic.

New lexicon terms: None

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
  "show_score": true,
  "show_completion": true,
  "body_html": "<p><strong>You can now:</strong> live the values · raise a concern the right way · answer leave and pay questions · use Oracle, Qiwa and Mumaris · keep your licence valid.</p><p><strong>Keep this:</strong> <a href=\"{{asset:hr-pdf-quickref}}\">HR Quick Reference (PDF, 2 pages)</a></p><p><strong>Please do:</strong> <a href=\"{{survey_url}}\" target=\"_blank\" rel=\"noopener\">the onboarding survey (2 minutes)</a></p><p><strong>Next:</strong> module 07 — Clinical Governance: Quality, Patient Safety &amp; Risk.</p>",
  "animation": "fade-up",
  "reveal": "auto",
  "narration_asset_id": "<hr-aud-091>",
  "narration_text": "That's the induction. You can now live the values, raise a concern the right way, and answer the leave and pay questions. You'll also know which system to use. Download the HR Quick Reference. Please complete the onboarding survey — two minutes, and it shapes how we run this day. Next: clinical governance, quality, patient safety and risk. Welcome to My Clinic."
}
```

#### 8. Notes for SME and developer

- Open questions: None on content. HR must supply the live onboarding-survey URL before build; until then use `{{survey_url}}` as a placeholder and confirm in preview that the link opens in a new tab.
- Developer notes: `{{asset:hr-pdf-quickref}}` is replaced with the real asset URL after `add_asset`. Test both links in preview **and** in the LMS.

---

## C. Module summary

### Screen register

| # | Screen id | Type | Scored | Pts | On-screen words | Narration words | Est. sec | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | `hr-000` | `title_slide` | N | 0 | 0 | 31 | 13 | `Draft` |
| 2 | `hr-001` | `content_slide` | N | 0 | 24 | 85 | 36 | `Draft` |
| 3 | `hr-002` | `poll` | N | 0 | 12 | 23 | 10 | `Draft` |
| 4 | `hr-010` | `tabs` | N | 0 | 14 | 81 | 35 | `Draft` |
| 5 | `hr-011` | `matching` | Y | 10 | 12 | 22 | 9 | `Draft` |
| 6 | `hr-012` | `accordion` | N | 0 | 15 | 99 | 42 | `Draft` |
| 7 | `hr-013` | `mcq` | Y | 5 | 0 | 16 | 7 | `Draft` |
| 8 | `hr-014` | `content_slide` | N | 0 | 10 | 44 | 19 | `Draft` |
| 9 | `hr-020` | `timeline` | N | 0 | 12 | 72 | 31 | `Draft` |
| 10 | `hr-021` | `hotspot` | N | 0 | 11 | 31 | 13 | `Draft` |
| 11 | `hr-022` | `content_slide` | N | 0 | 12 | 46 | 20 | `Draft` |
| 12 | `hr-023` | `flashcards` | N | 0 | 13 | 39 | 17 | `Draft` |
| 13 | `hr-030` | `content_slide` | N | 0 | 16 | 78 | 33 | `Draft` |
| 14 | `hr-031` | `decision_scenario` | Y | 15 | 7 | 35 | 15 | `Draft` |
| 15 | `hr-032` | `drag_drop` | Y | 10 | 12 | 26 | 11 | `Draft` |
| 16 | `hr-033` | `mcq` | Y | 5 | 0 | 22 | 9 | `Draft` |
| 17 | `hr-040` | `content_slide` | N | 0 | 15 | 66 | 28 | `Draft` |
| 18 | `hr-041` | `accordion` | N | 0 | 14 | 105 | 45 | `Draft` |
| 19 | `hr-042` | `matching` | Y | 5 | 13 | 14 | 6 | `Draft` |
| 20 | `hr-043` | `worked_example` | N | 0 | 0 | 95 | 41 | `Draft` |
| 21 | `hr-044` | `decision_scenario` | Y | 15 | 8 | 27 | 12 | `Draft` |
| 22 | `hr-045` | `adaptive_practice` | Y | 15 | 12 | 25 | 11 | `Draft` |
| 23 | `hr-050` | `content_slide` | N | 0 | 21 | 62 | 27 | `Draft` |
| 24 | `hr-051` | `worked_example` | N | 0 | 0 | 65 | 28 | `Draft` |
| 25 | `hr-052` | `fill_blank` | Y | 10 | 12 | 15 | 6 | `Draft` |
| 26 | `hr-053` | `worked_example` | N | 0 | 0 | 79 | 34 | `Draft` |
| 27 | `hr-054` | `mcq` | Y | 10 | 0 | 20 | 9 | `Draft` |
| 28 | `hr-060` | `matching` | Y | 10 | 10 | 19 | 8 | `Draft` |
| 29 | `hr-061` | `simulation` | Y | 15 | 14 | 27 | 12 | `Draft` |
| 30 | `hr-062` | `true_false` | Y | 5 | 0 | 22 | 9 | `Draft` |
| 31 | `hr-070` | `content_slide` | N | 0 | 15 | 57 | 24 | `Draft` |
| 32 | `hr-071` | `drag_drop` | Y | 10 | 9 | 20 | 9 | `Draft` |
| 33 | `hr-080` | `content_slide` | N | 0 | 21 | 52 | 22 | `Draft` |
| 34 | `hr-081` | `mcq` | Y | 5 | 0 | 16 | 7 | `Draft` |
| 35 | `hr-090` | `results_breakdown` | N | 0 | 11 | 33 | 14 | `Draft` |
| 36 | `hr-091` | `summary` | N | 0 | 21 | 67 | 29 | `Draft` |
| | **Totals** | | **15** | **145** | **366** | **1590** | **705.1 ≈ 11 min 45 s** | |

### Asset list (all screens)

| Asset id | Kind | Used on | Source | Alt text written? | Status |
|---|---|---|---|---|---|
| `hr-img-hero` | photo | `hr-000`, `hr-001` | own (consent pending **B6 / D5**) | Yes | to produce |
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
| `mentor-noor / hr-char-noor` | character ×3 poses | `hr-031`, `hr-044` | ai-generated (program master) | Yes | to produce |
| `hr-aud-000 … hr-aud-091` | audio ×36 | all narrated screens | TTS or human (program **D10**) | transcript = `narration_text` | to produce |

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
| J1 | “J-one” | `hr-021` |
| J2 | “J-two” | `hr-021` |
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
- [x] Narration total within ±15% of the Phase 3 estimate (701 s vs 780 s → 90%)
- [x] `review-checklist.md` run on every card
- [x] No `<angle bracket>` guidance text left (only `<hr-…>` asset placeholders remain)
- [x] Every JSON block parses and validates against `core/project.py` models (36 of 36)
- [x] `node_id`, `objective_ids` and `evidence_screen_ids` resolve; no dangling references
- [x] Hotspot and simulation regions use `rect`/`circle` with the right coordinate arity
- [x] No two adjacent screens share a type (stronger than the Phase 2 “no three in a row” rule)
- [ ] Longest unscored run: 6 screens, `hr-014`→`hr-030`. Two of them need learner action (`hr-021` explore-all, `hr-023` flip), so the passive stretch is `hr-014` + `hr-020` + `hr-022` + `hr-030`. **Watch item for `lint_visual_plan`:** if it raises `passive_stretch`, apply the Phase 2 mitigation — move the `hr-030` ethics summary into the `intro_html` of `hr-031` and drop `hr-030` (a plan change).

**Carried forward to the next phase**

- Every `⚠ PENDING` marker resolves to a Phase 0 item id and is listed above.
- `hr-061` cannot be built until **B8** supplies test-account Oracle screenshots.
- The `HR Quick Reference` PDF (`hr-pdf-quickref`) does not exist yet; HR writes it from confirmed policy.
