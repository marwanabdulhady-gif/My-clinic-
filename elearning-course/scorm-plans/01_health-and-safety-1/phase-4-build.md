# Phase 4 — Build (01 Facility Management & Safety)

Follow `../00_program/build-pipeline.md` §1. This page lists what is specific to this module.

## 1. Course settings

```json
{
  "title": "My Clinic — Facility Management & Safety",
  "description": "New-staff course on the eight CBAHI Facility Management & Safety plans, MOH emergency codes and ISO 45001 rights.",
  "scorm_version": "1.2",
  "language": "en",
  "theme": "<program theme tokens>",
  "theme_mode": "light",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 },
  "metadata": { "keywords": ["CBAHI", "FMS", "fire safety", "hazmat", "emergency codes"], "version": "1.0" }
}
```

## 2. Outline (section menu)

```json
"outline": [
  { "id": "hs1-s0", "kind": "section", "title": "Welcome" },
  { "id": "hs1-s1", "kind": "section", "title": "1 · The eight FMS plans",
    "objective": { "id": "hs1-o1", "description": "Name the eight FMS plans and match each to its purpose." } },
  { "id": "hs1-s2", "kind": "section", "title": "2 · Occupational Health & Safety",
    "objective": { "id": "hs1-o2", "description": "Apply AREC and the hierarchy of controls to a hazard." } },
  { "id": "hs1-s3", "kind": "section", "title": "3 · Emergency codes",
    "objective": { "id": "hs1-o3", "description": "Match MOH codes and follow the common response pattern." } },
  { "id": "hs1-s4", "kind": "section", "title": "4 · Fire safety",
    "objective": { "id": "hs1-o4", "description": "Respond with RACE and PASS; choose extinguisher and evacuation." } },
  { "id": "hs1-s5", "kind": "section", "title": "5 · Hazardous materials & waste",
    "objective": { "id": "hs1-o5", "description": "Read GHS/NFPA, decide on Code Orange, segregate waste." } },
  { "id": "hs1-s6", "kind": "section", "title": "6 · Security",
    "objective": { "id": "hs1-o6", "description": "Apply ID, visitor, contractor and premises rules." } },
  { "id": "hs1-s7", "kind": "section", "title": "7 · Utilities",
    "objective": { "id": "hs1-o7", "description": "Identify emergency power, shut-offs and HVAC rules." } },
  { "id": "hs1-s8", "kind": "section", "title": "8 · Medical equipment",
    "objective": { "id": "hs1-o8", "description": "Remove faulty equipment from use and report it." } },
  { "id": "hs1-s9", "kind": "section", "title": "9 · Radiation & laser",
    "objective": { "id": "hs1-o9", "description": "Apply ALARA, dose bands and laser classes." } },
  { "id": "hs1-s10", "kind": "section", "title": "Capstone & completion",
    "objective": { "id": "hs1-o10", "description": "Combine the plans in one connected emergency." } }
]
```

Each screen sets `node_id` to its section and `objective_ids` to the same objective when scored. `unlock_rule` stays `"free"`.

## 3. Points

| Screen | Pts | Screen | Pts | Screen | Pts |
|---|---|---|---|---|---|
| hs1-104 | 10 | hs1-405 | 10 | hs1-602 | 5 |
| hs1-204 | 10 | hs1-407 | 5 | hs1-702 | 5 |
| hs1-205 | 15 | hs1-408 | 5 | hs1-802 | 15 |
| hs1-302 | 10 | hs1-409 | 20 | hs1-803 | 5 |
| hs1-304 | 5 | hs1-502 | 10 | hs1-902 | 5 |
| hs1-402 | 5 | hs1-503 | 10 | hs1-905 | 5 |
| hs1-403 | 5 | hs1-504 | 5 | hs1-906 | 5 |
| | | hs1-507 | 15 | hs1-950 | 25 |
| | | hs1-508 | 10 | **Total** | **220** |

Pass = 80% of 220 = 176 points (with `score_scaling: true`, the LMS sees 0–100).

## 4. Spec snippets for the key interactions

Ids, text and structure are final; wording is subject to SME review.

**Sorting — RACE (`hs1-402`)**
```json
{ "type": "sorting", "id": "hs1-402", "title": "RACE: put the steps in order", "section": "4 · Fire safety",
  "node_id": "hs1-s4", "objective_ids": ["hs1-o4"], "points": 5,
  "prompt_html": "<p>You discover a fire. Put the response in the right order.</p>",
  "items": [
    { "id": "r", "text_html": "<strong>Rescue</strong> anyone in immediate danger" },
    { "id": "a", "text_html": "<strong>Alarm</strong> — pull station + call: code, location, your ID and name" },
    { "id": "c", "text_html": "<strong>Contain</strong> — remove O₂ and alcohol rub, close doors" },
    { "id": "e", "text_html": "<strong>Extinguish</strong> a small fire, or <strong>Evacuate</strong>" }
  ],
  "feedback": { "correct_html": "<p>Right. Smoke spreads faster than flame, so people and doors come first.</p>",
                "incorrect_html": "<p>Not quite. Rescue and contain come before extinguishing because smoke kills first.</p>" } }
```

**Decision scenario — Code Orange (`hs1-507`)** — node 1 of 3 shown
```json
{ "type": "decision_scenario", "id": "hs1-507", "title": "Spill or Code Orange?", "section": "5 · Hazardous materials & waste",
  "node_id": "hs1-s5", "objective_ids": ["hs1-o5"], "points": 15, "pass_score": 3,
  "intro_html": "<p>Three spills, three decisions. Use the rule you'd follow on shift.</p>",
  "nodes": [
    { "id": "n1", "prompt_html": "<p>A 200 mL bottle of alcohol hand rub falls and leaks in the corridor.</p>",
      "choices": [
        { "id": "a", "text_html": "Call the cleaning supervisor and warn people nearby", "score_delta": 1, "goto_node_id": "n2",
          "feedback_html": "<p>Correct. It is below the Code Orange threshold and not highly toxic. Keep people away until it is cleaned.</p>" },
        { "id": "b", "text_html": "Announce Code Orange", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Not needed here. Code Orange is for spills at or above the threshold, or highly toxic, reactive or explosive substances.</p>" }
      ] }
  ] }
```
*Threshold wording in feedback is filled from decision D1.*

**Hotspot explore — corridor (`hs1-404`)**
```json
{ "type": "hotspot", "id": "hs1-404", "title": "Find the fire safety equipment", "mode": "explore", "require_all": true,
  "image_asset_id": "<hs1-img-corridor>", "image_alt": "Clinic corridor with fire safety equipment.",
  "prompt_html": "<p>Open every item. Know where these are before you need them.</p>",
  "regions": [
    { "id": "callpoint", "shape": "rect", "coords": [812, 300, 70, 90],
      "label_html": "Call point", "feedback_html": "<p>Manual alarm. Pull it during the <strong>Alarm</strong> step of RACE.</p>" }
  ] }
```
*Coordinates are set after the illustration is final (natural pixel space). `rect`/`circle` only.*

**Capstone game (`hs1-950`)** — mechanics block
```json
{ "type": "game", "id": "hs1-950", "template": "case_sim", "points": 25, "pass_score": 2,
  "mechanics": {
    "score": { "id": "score", "start": 0 },
    "lives": { "id": "lives", "start": 3 },
    "hints": { "id": "hint", "hints": [ { "text": "People first, then the hazard.", "cost": 0 } ] }
  },
  "intro_html": "<p>One afternoon shift. Three things go wrong. Your decisions decide how it ends.</p>" }
```
*Node and choice structure (`content_html`, `choices[].to`, `on_choose`) follows `examples/games/lab-safety-game.en.json` in the edumints repo and `../00_program/storyboard-template/screen-type-guide.md`.*

## 5. Build order

1. `create_project` with §1 settings → `set_theme` → `set_tracking`.
2. Assets: SVGs first (`svg_to_asset`), then approved illustrations and photos (`add_asset`), then narration (`add_asset` + `normalize_audio_asset`). Keep the asset map in `build/asset-map.json`.
3. Screens section by section with `add_screen` (lets you `preview` each section). Use `build_from_spec` only for a full rebuild.
4. `lint_course` → fix errors (blocking) → document warnings.
5. `preview` desktop + narrow; walk every scenario branch.

## 6. Build-time risks

| Risk | Mitigation |
|---|---|
| Suspend data too large (54 screens, many interactions) | SCORM 2004; test resume after section 9 in SCORM Cloud. |
| Matching with images (`hs1-502`) may not support image-only left side | Use pictogram SVG inside `left_html` as `<img>` if the sanitizer allows asset references; otherwise use `drag_drop` with text names + a reference chart on the previous screen. Decide at build. |
| `mcq` multi-select support | If single-answer only, rewrite `hs1-702` as single best answer. |
