# Phase 4 — Build (03 Welcome On Board)

Follow `../00_program/build-pipeline.md`. Module specifics below.

## 1. Course settings

```json
{
  "title": "My Clinic — Welcome On Board: My Clinic & HR Essentials",
  "description": "Induction for new employees: who we are, our values and strategy, ethics, patients' rights and essential HR policies.",
  "scorm_version": "1.2",
  "language": "en",
  "layout_mode": "stage",
  "tracking": { "completion_rule": "viewed_all_and_passed", "passing_score": 70 }
}
```

## 2. Outline

| Node id | Title | Objective |
|---|---|---|
| hr-sA | Welcome | — |
| hr-sB | Our values & strategy | hr-o1 |
| hr-sC | Our clinic | — |
| hr-sD | Ethics & patients' rights | hr-o2 |
| hr-sE | Your leave | hr-o3 |
| hr-sF | Pay & social insurance | hr-o4 |
| hr-sG | Systems & licences | hr-o5 |
| hr-sH | ID, benefits & dress code | hr-o6 |
| hr-sI | Contracts & leaving | hr-o6 |
| hr-sZ | Close | — |

## 3. Points

| Screen | Pts | Screen | Pts | Screen | Pts |
|---|---|---|---|---|---|
| hr-011 | 10 | hr-042 | 5 | hr-060 | 10 |
| hr-013 | 5 | hr-044 | 15 | hr-061 | 15 |
| hr-031 | 15 | hr-045 | 15 | hr-062 | 5 |
| hr-032 | 10 | hr-052 | 10 | hr-071 | 10 |
| hr-033 | 5 | hr-054 | 10 | hr-081 | 5 |
| | | | | **Total** | **145** |

Pass = 70% → 102 points.

## 4. Spec snippets

**Adaptive practice (`hr-045`)** — 2 of 12 items shown
```json
{ "type": "adaptive_practice", "id": "hr-045", "title": "Leave rules: quick practice", "node_id": "hr-sE",
  "objective_ids": ["hr-o3"], "points": 15, "max_items": 6, "target_success": 0.7, "pass_ratio": 0.6,
  "adaptive": { "strategy": "elo" },
  "prompt_html": "<p>Answer until the practice says you're ready. It stops early if you've got it.</p>",
  "items": [
    { "id": "q1", "difficulty": 0.3, "prompt_html": "<p>How many unused annual leave days can you carry over?</p>",
      "options": [ { "id": "a", "text_html": "Up to 5", "correct": true }, { "id": "b", "text_html": "Up to 10" }, { "id": "c", "text_html": "All of them" } ] },
    { "id": "q2", "difficulty": 0.6, "prompt_html": "<p>A consulting-room physician carries over leave. By when must it be used?</p>",
      "options": [ { "id": "a", "text_html": "End of March" }, { "id": "b", "text_html": "End of June", "correct": true }, { "id": "c", "text_html": "End of the year" } ] }
  ] }
```
*Item field names follow the `AdaptiveItem` schema at build time (MCQ format + `difficulty`).*

**Simulation (`hr-061`)** — step 3 of 5
```json
{ "image_asset_id": "<hr-img-oracle-3>", "image_alt": "Oracle Time and Absences page with an Add Leaves tile.",
  "instruction_html": "<p>Open the page where you add a new leave request.</p>",
  "regions": [ { "id": "add", "shape": "rect", "coords": [420, 310, 220, 140], "label_html": "Add Leaves" } ],
  "hint_html": "<p>Look for <em>Add Leaves</em> under Time and Absences.</p>" }
```

**Fill in the blank (`hr-052`)** — accepted answers `731.25`, `731.25 SAR`, `731.25 riyals`.

## 5. Resources

- `hr-pdf-quickref` uploaded with `add_asset` and linked from `hr-040` and `hr-091` (`<a>` link to the asset). Check in preview that the link opens/downloads; the edumints roadmap notes resource-link handling is limited, so test in the LMS as well.
- Onboarding survey: external URL link on `hr-091` (opens in a new tab).

## 6. Build-time risks

| Risk | Mitigation |
|---|---|
| Suspend data with adaptive practice + 15 scored screens | SCORM 2004. Test resume mid-`hr-045`. |
| Oracle UI changes after screenshots | Record the Oracle release in the asset notes; re-capture on change (Phase 5 trigger). |
| PDF link not resolving in the packaged course | Fallback: host the PDF on the intranet and link the URL. |
