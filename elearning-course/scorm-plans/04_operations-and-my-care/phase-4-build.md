# Phase 4 — Build (04 Operations & My Care)

Follow `../00_program/build-pipeline.md`.

## 1. Course settings

```json
{
  "title": "My Clinic — Who Does What: Operations & My Care",
  "description": "How Operations and My Care divide the patient journey, and where to route a patient's request.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| ops-s1 | The patient journey | — |
| ops-s2 | Operations | ops-o1 |
| ops-s3 | My Care | ops-o1, ops-o3 |
| ops-s4 | Practice: right team, first time | ops-o2 |

## 3. Points

`ops-030` 15 · `ops-031` 20 · `ops-032` 5 · `ops-033` 10 · **Total 50**. Pass = 35.

## 4. Spec snippet — routing scenario (`ops-031`), node 1

```json
{ "type": "decision_scenario", "id": "ops-031", "title": "Who do I call?", "node_id": "ops-s4",
  "objective_ids": ["ops-o2"], "points": 20, "pass_score": 3,
  "nodes": [
    { "id": "n1", "prompt_html": "<p>At reception, a patient is upset: her lab result promised for today isn't ready.</p>",
      "choices": [
        { "id": "a", "text_html": "Patient Experience Officer on site (Operations)", "score_delta": 1, "goto_node_id": "n2",
          "feedback_html": "<p>Yes. On-the-spot complaints and service recovery are Operations' job, led by the PX team.</p>" },
        { "id": "b", "text_html": "My Care coordinator", "score_delta": 0, "goto_node_id": "n2",
          "feedback_html": "<p>My Care follows patients up after the visit. A complaint in the clinic right now needs the on-site PX team.</p>" }
      ] }
  ] }
```

## 5. Build-time risks

| Risk | Mitigation |
|---|---|
| Org charts too dense at stage size | Max 12 boxes per chart; split into two diagrams if needed; check at 360 px. |
| Routing rules change | Keep routing answers in one place (this file + Phase 0 B7) for quick updates. |
