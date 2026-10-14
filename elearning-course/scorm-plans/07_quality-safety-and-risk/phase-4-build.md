# Phase 4 — Build (07 Clinical Governance)

Follow `../00_program/build-pipeline.md`.

## 1. Course settings

```json
{
  "title": "My Clinic — Clinical Governance: Quality, Patient Safety & Risk",
  "description": "Quality standard, the six International Patient Safety Goals, risk scoring, incident types and the 24-hour reporting rule.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| qsr-sA | Welcome | — |
| qsr-sB | The quality standard | qsr-o1 |
| qsr-sC | Six patient safety goals | qsr-o2 |
| qsr-sD | Risk management | qsr-o3 |
| qsr-sE | Incidents | qsr-o4 |
| qsr-sF | Reporting | qsr-o5 |
| qsr-sG | Close | — |

## 3. Points

`qsr-011` 10 · `qsr-012` 5 · `qsr-021` 15 · `qsr-022` 10 · `qsr-023` 5 · `qsr-030` 5 · `qsr-032` 5 · `qsr-033` 10 · `qsr-041` 10 · `qsr-042` 5 · `qsr-051` 15 · **Total 95**. Pass = 76.

## 4. Spec snippet — identification scenario (`qsr-021`), node 1

```json
{ "type": "decision_scenario", "id": "qsr-021", "title": "Which Mohammed?", "node_id": "qsr-sC",
  "objective_ids": ["qsr-o2"], "points": 15, "pass_score": 2,
  "intro_html": "<p>Two patients called Mohammed Al-Harbi are waiting for blood tests.</p>",
  "nodes": [
    { "id": "n1", "image_asset_id": "<qsr-img-wristbands>",
      "image_alt": "Two wristbands: same name; MRN 100245 and MRN 100871.",
      "prompt_html": "<p>One of them sits down in front of you. How do you confirm who he is?</p>",
      "choices": [
        { "id": "a", "text_html": "Ask his full name and check the MRN on his wristband against the request", "score_delta": 1, "goto_node_id": "n2",
          "feedback_html": "<p>Correct: the two approved identifiers.</p>" },
        { "id": "b", "text_html": "Check the room number on the request", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>A room or location is never an identifier. Patients move.</p>" },
        { "id": "c", "text_html": "Ask his age", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>Age must never be used as an identifier.</p>" }
      ] }
  ] }
```
*MRNs are fictional.*

## 5. Optional video

If `qsr-060` is approved: `add_asset` for the MP4, poster and WebVTT; set `video_asset_id`, `poster_asset_id`, `captions_asset_id`, `narration_text` (transcript). No separate narration audio on that screen.

## 6. Build-time risks

| Risk | Mitigation |
|---|---|
| Matrix colours fail contrast or colour-only meaning | Band names printed in each cell; check with `brand_to_theme` contrast and the high-contrast theme. |
| Terminology drifts from policy (critical vs sentinel) | Use the policy's terms everywhere, set in Phase 0 B8. |
