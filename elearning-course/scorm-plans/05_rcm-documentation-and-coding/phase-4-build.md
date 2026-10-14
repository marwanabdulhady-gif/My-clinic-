# Phase 4 — Build (05 RCM Part A)

Follow `../00_program/build-pipeline.md`.

## 1. Course settings

```json
{
  "title": "My Clinic — RCM Part A: Documentation & ICD-10 Coding That Gets Approved",
  "description": "Clinical documentation improvement for physicians: medical necessity, specific ICD-10 coding, avoiding defensive medicine and common rejection causes.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 80 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| rcma-sA | Why it matters | — |
| rcma-sB | Documentation strategy | rcma-o1 |
| rcma-sC | ICD-10 coding | rcma-o2 |
| rcma-sD | Defensive medicine & ordering | rcma-o3 |
| rcma-sE | Rejections & coverage | rcma-o4 |
| rcma-sF | Fix the note | rcma-o5 |

## 3. Points

`rcma-012` 10 · `rcma-013` 5 · `rcma-021` 10 · `rcma-023` 10 · `rcma-031` 15 · `rcma-032` 5 · `rcma-033` 5 · `rcma-040` 10 · `rcma-042` 5 · `rcma-050` 25 · **Total 100**. Pass = 80.

## 4. Spec snippets

**Matching (`rcma-021`)** — codes filled after B4
```json
{ "type": "matching", "id": "rcma-021", "title": "Don't stop at the symptom", "node_id": "rcma-sC",
  "objective_ids": ["rcma-o2"], "points": 10,
  "prompt_html": "<p>Match each presentation to the most specific supported diagnosis.</p>",
  "pairs": [
    { "id": "p1", "left_html": "Sore throat, fever, tonsillar exudate", "right_html": "J03 · Acute tonsillitis" },
    { "id": "p2", "left_html": "Headache, BP 168/102 on two readings", "right_html": "I10 · Essential hypertension" },
    { "id": "p3", "left_html": "Polyuria, HbA1c 8.1%", "right_html": "E11 · Type 2 diabetes mellitus" },
    { "id": "p4", "left_html": "Vomiting and diarrhoea for 2 days, dry mucosa", "right_html": "<code per B4> · Gastroenteritis" }
  ] }
```

**True/false (`rcma-033`)**
```json
{ "type": "true_false", "id": "rcma-033", "title": "Supplements", "node_id": "rcma-sD", "objective_ids": ["rcma-o3"], "points": 5,
  "prompt_html": "<p>A combined multivitamin “for general wellness”, with no documented deficiency, is likely to be rejected.</p>",
  "correct": true,
  "feedback": { "correct_html": "<p>Right. Supplements need a documented indication; combined supplements are treated as defensive medicine.</p>",
                "incorrect_html": "<p>It is likely to be rejected: there's no documented indication.</p>" } }
```

## 5. QTI export

Run `export_qti(project_id)` after the build so the RCM team can reuse the question items in other assessment tools.

## 6. Build-time risks

| Risk | Mitigation |
|---|---|
| Codes change with the payer's ICD-10 edition | Keep codes in screen text only (not images); update with `update_screen`. |
| Clinical vignettes read as treatment guidance | Add a one-line disclaimer on `rcma-001`: "Examples teach documentation, not treatment." |
