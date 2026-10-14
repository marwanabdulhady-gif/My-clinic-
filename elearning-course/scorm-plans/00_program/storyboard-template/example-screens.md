# Example screen cards (module 01)

Three finished cards showing the expected level of detail: an explain screen, a scored sort and a scored scenario. Copy this depth for every screen. Values marked `⚠ PENDING` show how to handle open Phase 0 items.

---

### `hs1-401` — The fire triangle

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `labeled_diagram` (display) · **Scored:** No

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Explain: why fire control works, and why RACE rescues and contains before extinguishing |
| Objective(s) | — (supports `hs1-o4`) |
| On-the-job action | A2 — respond to a fire using RACE and PASS |
| Source | `Health & Safety 1.pdf`, p.23 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | The fire triangle |
| Body / keywords | Heat · Fuel · Oxygen. Remove one side and the fire stops. **Smoke, not flame, is the leading cause of death.** |
| Word count (excl. title) | 19 |
| Instruction | n/a (display diagram) |

#### 3. Visual design

| Field | Value |
|---|---|
| Visual concept | Large equilateral triangle centred on a light background; each side labelled Heat, Fuel, Oxygen with a line icon; a grey smoke band drifts across the bottom with the warning text |
| Layout | n/a (labeled_diagram) |
| Colour roles | bg `light` · text `dark` · accent `accent` on the smoke warning only |
| Animation / reveal | Labels reveal in narration order: heat → fuel → oxygen → smoke |
| Character | None |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hs1-img-triangle` | svg | 960×540, triangle with three side labels as separate text, smoke band at the bottom; brand colours; no text baked in except side names | own | Fire triangle: heat, fuel and oxygen. Smoke spreads along the bottom. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items | Labels: `heat` (x 150, y 560) "Heat — ignition source" · `fuel` (x 850, y 560) "Fuel — anything that burns" · `oxygen` (x 500, y 120) "Oxygen — keeps it burning" · `smoke` (x 500, y 900) "Smoke kills first" |
| Correct answer(s) | n/a (display) |
| Points | 0 |

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Calm, clear |
| Target seconds | 30 |
| Word count / est. seconds | 74 words / ≈ 32 s |
| Cue targets | `heat`, `fuel`, `oxygen`, `smoke` |

> Every fire needs three things. [[cue:heat]] Heat to start it, [[cue:fuel]] something to burn, [[cue:oxygen]] and oxygen to keep it going. Take away any one of them and the fire stops. That's the idea behind every way we fight fire. [[pause:0.5]] [[cue:smoke]] But here's what catches people out. In a building, it's usually the smoke that kills, not the flames. Smoke moves faster than fire along corridors and through ducts. That's why RACE puts rescue and closing doors first.

New lexicon terms: None (RACE already in the master lexicon)

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | No interaction needed; labels readable in DOM order |
| Not colour-only | Every side is named in text; smoke warning is text plus icon |
| Captions / transcript | `narration_text` = script without markup |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "labeled_diagram", "id": "hs1-401", "title": "The fire triangle",
  "section": "4 · Fire safety", "node_id": "hs1-s4", "mode": "display",
  "image_asset_id": "<hs1-img-triangle>",
  "prompt_html": "<p>Heat · Fuel · Oxygen. Remove one side and the fire stops. <strong>Smoke, not flame, is the leading cause of death.</strong></p>",
  "labels": [
    { "id": "heat", "text": "Heat — ignition source", "x": 150, "y": 560 },
    { "id": "fuel", "text": "Fuel — anything that burns", "x": 850, "y": 560 },
    { "id": "oxygen", "text": "Oxygen — keeps it burning", "x": 500, "y": 120 },
    { "id": "smoke", "text": "Smoke kills first", "x": 500, "y": 900 }
  ]
}
```

#### 8. Notes for SME and developer

- Open questions: None
- Developer notes: adjust label x/y once the final SVG is drawn.

---

### `hs1-402` — RACE: put the steps in order

**Status:** `Draft — ready for SME review` · **Section / node:** 4 · Fire safety / `hs1-s4` · **Type:** `sorting` · **Scored:** Yes (5 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Check: recall the RACE order |
| Objective(s) | `hs1-o4` |
| On-the-job action | A2 |
| Source | `Health & Safety 1.pdf`, p.24; `Health & Safety 2.pdf`, pp.7–11 |
| Depends on Phase 0 | None |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | RACE: put the steps in order |
| Body / keywords | You discover a fire. Put the response in the right order. |
| Word count (excl. title) | 11 |
| Instruction | Drag the steps, or use the arrow keys, into the right order, then check. |

#### 3. Visual design

| Field | Value |
|---|---|
| Visual concept | Four white step cards stacked vertically, each with a bold first letter tile (R, A, C, E) hidden until checked, on a light background |
| Layout | n/a (sorting) |
| Colour roles | bg `light` · text `dark` · accent none |
| Animation / reveal | None |
| Character | None |

**Imagery:** None (text-only interaction).

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Items (correct order) | 1 `r` **Rescue** anyone in immediate danger · 2 `a` **Alarm** — pull the call point and call: code, location, your ID and name · 3 `c` **Contain** — remove O₂ cylinders and alcohol rub, close doors · 4 `e` **Extinguish** a small fire, or **Evacuate** |
| Correct answer(s) | r → a → c → e |
| Points | 5 |
| Feedback — correct | Right. Smoke spreads faster than flame, so people and doors come first. You only fight a fire that is small and contained. |
| Feedback — incorrect | Not quite. Rescue and contain come before extinguishing, because smoke kills first. Look at the order again. |
| Hint | n/a |
| Retry / lives | Unlimited retries; score counted once |

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Encouraging |
| Target seconds | 8 |
| Word count / est. seconds | 16 words / ≈ 7 s |
| Cue targets | None |

> You've just seen smoke coming from a room. Four things need to happen. In what order?

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Sorting supports keyboard reordering |
| Not colour-only | Order shown by position and numbers after checking |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "sorting", "id": "hs1-402", "title": "RACE: put the steps in order",
  "section": "4 · Fire safety", "node_id": "hs1-s4", "objective_ids": ["hs1-o4"], "points": 5,
  "prompt_html": "<p>You discover a fire. Put the response in the right order.</p>",
  "items": [
    { "id": "r", "text_html": "<strong>Rescue</strong> anyone in immediate danger" },
    { "id": "a", "text_html": "<strong>Alarm</strong> — pull the call point and call: code, location, your ID and name" },
    { "id": "c", "text_html": "<strong>Contain</strong> — remove O₂ cylinders and alcohol rub, close doors" },
    { "id": "e", "text_html": "<strong>Extinguish</strong> a small fire, or <strong>Evacuate</strong>" }
  ],
  "feedback": {
    "correct_html": "<p>Right. Smoke spreads faster than flame, so people and doors come first. You only fight a fire that is small and contained.</p>",
    "incorrect_html": "<p>Not quite. Rescue and contain come before extinguishing, because smoke kills first.</p>",
    "show_correct_answer": true
  }
}
```

#### 8. Notes for SME and developer

- Open questions: None
- Developer notes: none

---

### `hs1-507` — Spill or Code Orange?

**Status:** `Draft — ready for SME review` · **Section / node:** 5 · Hazardous materials & waste / `hs1-s5` · **Type:** `decision_scenario` · **Scored:** Yes (15 pts)

#### 1. Purpose

| Field | Value |
|---|---|
| Learning job | Practise: decide when a spill is Code Orange and follow the four response steps |
| Objective(s) | `hs1-o5` |
| On-the-job action | A6 — decide when a spill is Code Orange and respond |
| Source | `Health & Safety 1.pdf`, p.40; `Health & Safety 2.pdf`, p.22 |
| Depends on Phase 0 | **B1 / D1** (Code Orange threshold) |

#### 2. On-screen content

| Element | Text |
|---|---|
| Title | Spill or Code Orange? |
| Body / keywords | Three spills, three decisions. Use the rule you'd follow on shift. |
| Word count (excl. title) | 11 |
| Instruction | Choose what you would do for each spill. |

#### 3. Visual design

| Field | Value |
|---|---|
| Visual concept | One illustration per node: corridor with a small hand-rub bottle leaking; store room floor with a large tipped disinfectant container; lab bench with a small reagent bottle marked with the skull GHS pictogram |
| Layout | n/a (decision_scenario) |
| Colour roles | bg `surface` · text `dark` · accent none (feedback uses `success`/`error`) |
| Animation / reveal | None |
| Character | `mentor-noor` (concern) on the intro only |

**Imagery**

| Asset id | Kind | Description / brief | Source | Alt text | Decorative? |
|---|---|---|---|---|---|
| `hs1-img-spill-1` | illustration | Corridor floor, small puddle from a 200 mL hand-rub bottle; flat brand style | ai-generated | A small hand-rub bottle leaking in a corridor. | No |
| `hs1-img-spill-2` | illustration | Store room, large container of surface disinfectant on its side, wide spill | ai-generated | A large container of surface disinfectant spilled across a store-room floor. | No |
| `hs1-img-spill-3` | illustration | Lab bench, small reagent bottle with the GHS skull pictogram, a few drops spilled | ai-generated | A few drops spilled from a reagent bottle labelled with the acute toxicity pictogram. | No |

#### 4. Interaction and scoring

| Field | Value |
|---|---|
| Points | 15 |
| Pass rule | `pass_score` 3 (best choice on all three nodes) |
| Feedback — correct (end) | You applied the rule correctly: volume and hazard decide, not how messy it looks. |
| Feedback — incorrect (end) | Check the rule again: Code Orange is for large spills or any highly toxic, reactive or explosive substance. |
| Retry / lives | Replay allowed; score counted once |

| Node | Situation | Choice | Choice text | Score Δ | Goes to | Feedback (why) |
|---|---|---|---|---|---|---|
| n1 | A 200 mL bottle of alcohol hand rub falls and leaks in the corridor. | a | Warn people nearby and call the cleaning supervisor | +1 | n2 | Correct. It's below the Code Orange threshold ⚠ PENDING D1 and not highly toxic. Keep people away until it's cleaned. |
| | | b | Announce Code Orange | 0 | n2 | Not needed here. Code Orange is for spills at or above the threshold, or highly toxic, reactive or explosive substances. |
| n2 | A large container of surface disinfectant tips over; most of it is on the floor (well over 500 mL ⚠ PENDING D1). | a | Call the cleaning supervisor | 0 | n3 | A spill this size needs Code Orange. Isolate the area, warn others, then activate the code. |
| | | b | Isolate the area, warn others and activate Code Orange | +1 | n3 | Correct. Then put on the PPE the SDS specifies, contain it with the chemical spill kit, and report. |
| n3 | A few millilitres of a reagent marked with the skull pictogram spill on the lab bench. | a | Wipe it up with paper towels — it's tiny | 0 | — | The skull means acute toxicity. Any highly toxic substance triggers Code Orange, whatever the volume. |
| | | b | Activate Code Orange | +1 | — | Correct. Volume doesn't matter when the substance is highly toxic, reactive or explosive. |

#### 5. Narration

| Field | Value |
|---|---|
| Tone | Serious, calm |
| Target seconds | 15 |
| Word count / est. seconds | 28 words / ≈ 12 s |
| Cue targets | None |

> Spills happen every week in a clinic. Most are small. A few need the whole facility to respond. You'll see three. For each one, decide what you'd do.

New lexicon terms: None

#### 6. Accessibility

| Check | How this screen meets it |
|---|---|
| Keyboard | Choices are buttons |
| Not colour-only | Spill size and hazard stated in the prompt text; pictogram named in alt text |
| Captions / transcript | `narration_text` present |
| Timing | Untimed |

#### 7. Build fields (edumints)

```json
{
  "type": "decision_scenario", "id": "hs1-507", "title": "Spill or Code Orange?",
  "section": "5 · Hazardous materials & waste", "node_id": "hs1-s5",
  "objective_ids": ["hs1-o5"], "points": 15, "pass_score": 3, "start_node_id": "n1",
  "intro_html": "<p>Three spills, three decisions. Use the rule you'd follow on shift.</p>",
  "nodes": [
    { "id": "n1", "image_asset_id": "<hs1-img-spill-1>", "image_alt": "A small hand-rub bottle leaking in a corridor.",
      "prompt_html": "<p>A 200 mL bottle of alcohol hand rub falls and leaks in the corridor.</p>",
      "choices": [
        { "id": "a", "text_html": "Warn people nearby and call the cleaning supervisor", "score_delta": 1, "goto_node_id": "n2",
          "feedback_html": "<p>Correct. It's below the Code Orange threshold and not highly toxic. Keep people away until it's cleaned.</p>" },
        { "id": "b", "text_html": "Announce Code Orange", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Not needed here. Code Orange is for spills at or above the threshold, or highly toxic, reactive or explosive substances.</p>" } ] },
    { "id": "n2", "image_asset_id": "<hs1-img-spill-2>", "image_alt": "A large container of surface disinfectant spilled across a store-room floor.",
      "prompt_html": "<p>A large container of surface disinfectant tips over; most of it is on the floor.</p>",
      "choices": [
        { "id": "a", "text_html": "Call the cleaning supervisor", "score_delta": 0, "goto_node_id": "n3",
          "feedback_html": "<p>A spill this size needs Code Orange. Isolate the area, warn others, then activate the code.</p>" },
        { "id": "b", "text_html": "Isolate the area, warn others and activate Code Orange", "score_delta": 1, "goto_node_id": "n3",
          "feedback_html": "<p>Correct. Then put on the PPE the SDS specifies, contain it with the chemical spill kit, and report.</p>" } ] },
    { "id": "n3", "image_asset_id": "<hs1-img-spill-3>", "image_alt": "A few drops spilled from a reagent bottle labelled with the acute toxicity pictogram.",
      "prompt_html": "<p>A few millilitres of a reagent marked with the skull pictogram spill on the lab bench.</p>",
      "choices": [
        { "id": "a", "text_html": "Wipe it up with paper towels — it's tiny", "score_delta": 0, "goto_node_id": null,
          "feedback_html": "<p>The skull means acute toxicity. Any highly toxic substance triggers Code Orange, whatever the volume.</p>" },
        { "id": "b", "text_html": "Activate Code Orange", "score_delta": 1, "goto_node_id": null,
          "feedback_html": "<p>Correct. Volume doesn't matter when the substance is highly toxic, reactive or explosive.</p>" } ] }
  ],
  "feedback": {
    "correct_html": "<p>You applied the rule correctly: volume and hazard decide, not how messy it looks.</p>",
    "incorrect_html": "<p>Check the rule again: Code Orange is for large spills or any highly toxic, reactive or explosive substance.</p>"
  }
}
```

#### 8. Notes for SME and developer

- Open questions: Confirm the single Code Orange rule (D1). Recommended: ≥ 500 mL, or any highly toxic/reactive/explosive substance. The n1/n2 volumes and feedback change if the threshold changes.
- Developer notes: the same rule text must appear in `hs1-950` and module 02 (`hs2-050`, `hs2-052`, `hs2-064`).
