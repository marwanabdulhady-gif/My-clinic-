# Phase 4 — Build (02 Safety in Practice)

Follow `../00_program/build-pipeline.md`. Module specifics below.

## 1. Course settings

```json
{
  "title": "My Clinic — Safety in Practice: Hazard, Fire & Chemical Lab",
  "description": "Hands-on practice: hazard spotting, Code Red drill, evacuation tools, extinguishers, spills and the chemical register.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| hs2-sA | A · Spot the hazard | hs2-o1 |
| hs2-sB | B · Code Red drill | hs2-o2 |
| hs2-sC | C · Evacuation | hs2-o3 |
| hs2-sD | D · Extinguishers | hs2-o4 |
| hs2-sE | E · Spills | hs2-o5 |
| hs2-sF | F · Labels & register | hs2-o6 |
| hs2-sG | G · Regulations & close | hs2-o7 |

`unlock_rule: "free"`.

## 3. Points

| Screen | Pts | Screen | Pts |
|---|---|---|---|
| hs2-012 | 5 | hs2-053 | 10 |
| hs2-013 | 5 | hs2-061 | 10 |
| hs2-030 | 25 | hs2-062 | 10 |
| hs2-031 | 10 | hs2-063 | 5 |
| hs2-032 | 10 | hs2-064 | 20 |
| hs2-041 | 10 | hs2-070 | 10 |
| hs2-052 | 15 | **Total** | **145** |

Pass = 80% → 116 points.

## 4. Spec snippets

**Fill in the blank (`hs2-013`)**
```json
{ "type": "fill_blank", "id": "hs2-013", "title": "Score the risk", "node_id": "hs2-sA",
  "objective_ids": ["hs2-o1"], "points": 5,
  "prompt_html": "<p>Likelihood <strong>2</strong>, impact <strong>5</strong>. Risk score = {{blank}}</p>",
  "answers": ["10"] }
```
*Field names for blanks follow the `fill_blank` schema from `list_screen_types` at build time.*

**Escape room (`hs2-064`)**
```json
{ "type": "escape_room", "id": "hs2-064", "title": "Chemical store lockout", "node_id": "hs2-sF",
  "objective_ids": ["hs2-o6"], "points": 20, "lives": 3,
  "intro_html": "<p>The chemical store is locked. Four safety checks open it. Everything you need is on screen.</p>",
  "puzzles": [
    { "id": "p1", "prompt_html": "<p>The solvent's NFPA diamond reads 2 (blue), 3 (red), 0 (yellow). What is its <strong>health</strong> rating?</p>",
      "accepted": ["2", "two"], "hint_html": "<p>Health is the blue quadrant.</p>" },
    { "id": "p2", "prompt_html": "<p>Which register row has no SDS on file? Enter the row number.</p>",
      "accepted": ["4"], "hint_html": "<p>Look at the SDS column for a ✘.</p>" },
    { "id": "p3", "prompt_html": "<p>A colleague is splashed in the eye. How many minutes, at least, do you flush?</p>",
      "accepted": ["15", "15 minutes", "fifteen"], "hint_html": "<p>Longer than feels comfortable.</p>" },
    { "id": "p4", "prompt_html": "<p>Most of a one-litre bottle of disinfectant has spilled. Which code do you call?</p>",
      "accepted": ["orange", "code orange"], "hint_html": "<p>Check the volume against the threshold.</p>" }
  ] }
```
*Puzzle 4 wording follows D1.*

**Drag and drop (`hs2-031`)**
```json
{ "type": "drag_drop", "id": "hs2-031", "title": "Choose the evacuation tool", "node_id": "hs2-sC",
  "objective_ids": ["hs2-o3"], "points": 10,
  "prompt_html": "<p>Match each patient to the tool you'd use.</p>",
  "items": [
    { "id": "i1", "text_html": "Bedbound adult, 2nd floor", "correct_target_id": "mattress" },
    { "id": "i2", "text_html": "Adult who can't walk, stairs needed", "correct_target_id": "chair" },
    { "id": "i3", "text_html": "Newborn in the nursery", "correct_target_id": "newborn" },
    { "id": "i4", "text_html": "Infant carried by a staff member", "correct_target_id": "apron" }
  ],
  "targets": [
    { "id": "mattress", "label_html": "Evacuation mattress" },
    { "id": "chair", "label_html": "Evacuation chair" },
    { "id": "newborn", "label_html": "Newborn evacuation chair" },
    { "id": "apron", "label_html": "Baby mover / apron" }
  ] }
```

## 5. Build order

1. Reuse module 01 GHS SVGs (copy the asset files; asset ids are per project).
2. Build Part B (`hs2-030`) first and preview it end to end; it carries most of the score.
3. Then the remaining parts in order; `lint_course`; `preview`.

## 6. Build-time risks

| Risk | Mitigation |
|---|---|
| Store-room illustration shows extra, unintended hazards | Review against the key; regenerate or edit until only the 6 are visible. |
| `image_compare` needs two images of the same size | Shoot both kits on the same background and crop identically. |
| Learners skip module 01 | Set the LMS prerequisite; the first screen says the lab assumes module 01. |
