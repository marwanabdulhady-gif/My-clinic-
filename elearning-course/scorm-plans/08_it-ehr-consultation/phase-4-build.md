# Phase 4 — Build (08 EHR Consultation)

Follow `../00_program/build-pipeline.md`.

## 1. Course settings

```json
{
  "title": "My Clinic — EHR Consultation Workflow: Guided Simulation",
  "description": "Guided practice on a test patient: mandatory fields, ICD-10 diagnosis, linked orders, summary, SMS education, referral and follow-up.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| ehr-sA | The workflow | — |
| ehr-sB | Open & document | ehr-o1 |
| ehr-sC | Diagnosis | ehr-o2 |
| ehr-sD | Orders | ehr-o3 |
| ehr-sE | Summary & education | ehr-o4 |
| ehr-sF | Referral & finish | ehr-o4, ehr-o5 |

## 3. Points

`ehr-010` 5 · `ehr-012` 5 · `ehr-020` 10 · `ehr-031` 15 · `ehr-032` 10 · `ehr-033` 5 · `ehr-034` 5 · `ehr-040` 5 · `ehr-041` 10 · `ehr-050` 10 · `ehr-051` 10 · **Total 90**. Pass = 72.

## 4. Spec snippet — diagnosis simulation (`ehr-020`), steps 2–3

```json
{ "type": "simulation", "id": "ehr-020", "title": "Add the primary diagnosis", "node_id": "ehr-sC",
  "objective_ids": ["ehr-o2"], "points": 10,
  "prompt_html": "<p>Add type 2 diabetes as the primary diagnosis for the test patient.</p>",
  "steps": [
    { "image_asset_id": "<ehr-shot-dx-2>", "image_alt": "Add Diagnosis dialog with an empty search box.",
      "instruction_html": "<p>Search for the diagnosis by its ICD-10 code.</p>",
      "input_accepted": ["E11", "e11", "type 2 diabetes"], "input_label": "Search diagnosis",
      "hint_html": "<p>Type 2 diabetes mellitus is <strong>E11</strong>.</p>" },
    { "image_asset_id": "<ehr-shot-dx-3>", "image_alt": "Search results listing type 2 diabetes diagnoses.",
      "instruction_html": "<p>Choose <em>Type 2 diabetes mellitus</em>.</p>",
      "regions": [ { "id": "t2dm", "shape": "rect", "coords": [180, 420, 620, 44], "label_html": "Type 2 diabetes mellitus" } ],
      "hint_html": "<p>Pick the general E11 entry unless the notes support a complication.</p>" }
  ] }
```
*Region coordinates are measured on the final screenshots (natural pixels).*

## 5. Optional video

If `ehr-060` is approved: record on the test patient, add voice-over from the Phase 3 script, export MP4 + real time-synced WebVTT, `add_asset` both, attach to a `video` screen with `narration_text` = transcript.

## 6. Build-time risks

| Risk | Mitigation |
|---|---|
| Screenshots too small at stage size | Capture at 125% zoom; crop to the working area; one action per step. |
| EHR UI update | Record version; Phase 5 trigger to re-capture; keep region coordinates in `build/regions.json`. |
| Any real identifier slips into a screenshot | DPO check before `add_asset`; T1 in Phase 5 repeats the check on the built package. |
