# Phase 4 — Build (06 RCM Part B)

Follow `../00_program/build-pipeline.md`.

## 1. Course settings

```json
{
  "title": "My Clinic — RCM Part B: New EBP Benefits & Claim-Rejection Analysis",
  "description": "The added and amended EBP benefits, their limits, and how to classify and rework rejected claims.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| rcmb-sA | What changed | rcmb-o1 |
| rcmb-sB | Benefits in practice | rcmb-o2 |
| rcmb-sC | Reading rejections | rcmb-o3 |
| rcmb-sD | Practice & close | rcmb-o2 |

## 3. Points

`rcmb-010` 10 · `rcmb-021` 5 · `rcmb-031` 5 · `rcmb-041` 10 · `rcmb-051` 15 · `rcmb-052` 15 · `rcmb-060` 20 · **Total 80**. Pass = 64.

## 4. Spec snippet — classify rejections (`rcmb-051`), 3 of 8 items

```json
{ "type": "drag_drop", "id": "rcmb-051", "title": "Why was it rejected?", "node_id": "rcmb-sC",
  "objective_ids": ["rcmb-o3"], "points": 15,
  "prompt_html": "<p>Sort each rejection comment by its cause.</p>",
  "items": [
    { "id": "i1", "text_html": "“Pain, unspecified”", "correct_target_id": "coding" },
    { "id": "i2", "text_html": "“Requires pre-authorisation as per policy”", "correct_target_id": "policy" },
    { "id": "i3", "text_html": "“Consultation within the free follow-up period”", "correct_target_id": "timing" }
  ],
  "targets": [
    { "id": "documentation", "label_html": "Documentation" },
    { "id": "coding", "label_html": "Coding" },
    { "id": "policy", "label_html": "Policy / pre-authorisation" },
    { "id": "timing", "label_html": "Timing / follow-up period" },
    { "id": "billing", "label_html": "Billing process" }
  ] }
```
*Category mapping is final only after B9.*

## 5. Build-time risks

| Risk | Mitigation |
|---|---|
| EBP changes again | All benefit text is HTML; keep `rcmb-pdf-ebp` versioned; minor version bump on change. |
| Learners treat the course as a coverage authority | Footer line on `rcmb-001`: "Always check the patient's policy and the current table of benefits." |
