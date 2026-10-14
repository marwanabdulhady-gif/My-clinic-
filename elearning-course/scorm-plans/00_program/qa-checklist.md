# QA checklist and sign-off record (all modules)

Playbook topic: `quality` · Gates: `lint_course`, `lint_authoring_plan(stage="delivery")`, `validate_package`

Each module's `phase-5-qa-and-delivery.md` adds module-specific tests on top of this list. Status values: `pending`, `passed`, `failed`, `not_applicable` (with a reason). A status without evidence is not proof.

## 1. Content accuracy

- [ ] Every fact traces to a source page/slide listed in the storyboard's *Source* column.
- [ ] Every Phase 0 blocking item is resolved and the decision is reflected on screen.
- [ ] Numbers checked against the decision log (thresholds, days, percentages, limits, extensions).
- [ ] SME reviewed every scored question and its feedback.
- [ ] No placeholder text (`[Facility Name]`, `5555`, `TBD`) remains (`lint_course` + manual search).

## 2. Privacy and rights

- [ ] No patient identifiers in any screenshot, video frame, table or example.
- [ ] Claim numbers, staff names and emails removed or approved for internal use.
- [ ] Every asset has a provenance record with an allowed `source`.
- [ ] No third-party watermark (NotebookLM) in any asset.
- [ ] Staff photos used only with written consent.

## 3. Accessibility (WCAG 2.2 AA target)

- [ ] Alt text on every meaningful image; decorative images marked decorative.
- [ ] `narration_text` (captions/transcript) on every narrated screen.
- [ ] WebVTT captions on every video screen.
- [ ] Colour is never the only cue (emergency codes, NFPA diamond, risk matrix, waste bins).
- [ ] Every drag interaction is also usable by keyboard; timed activities can be extended or are untimed.
- [ ] Keyboard-only walk-through of the whole module (focus visible, logical order).
- [ ] Reduced-motion setting respected.
- [ ] Text readable at 360 px width (narrow preview).

## 4. Interaction and scoring

- [ ] Every scored screen has correct answers, feedback for right and wrong, and `objective_ids`.
- [ ] Every branch of every `decision_scenario`, `game` and `escape_room` walked: success, wrong answer, hint, lives exhausted, restart.
- [ ] Score cannot be inflated by replaying a screen.
- [ ] Results breakdown shows each section/objective.
- [ ] Passing score and completion rule match Phase 4.

## 5. Audio and video

- [ ] Real durations within ±15% of `est_sec`.
- [ ] First, middle and last file spot-listened: lexicon terms, clipped endings, loudness.
- [ ] Video controls and captions work in preview **and** in the LMS.

## 6. SCORM / LMS

- [ ] `validate_package` passes (manifest XSD).
- [ ] SCORM Cloud import: 0 parser warnings, launch, complete, pass, fail, resume mid-way.
- [ ] My Clinic LMS: import, launch on desktop and tablet, score + completion reported, resume works, re-attempt policy set.
- [ ] Interactions (question-level) visible in the LMS report.

## 7. Pilot

- [ ] 5–8 new starters from the target audience complete the module.
- [ ] Collect: time taken, score per objective, confusing screens, one improvement each.
- [ ] Fix list agreed and closed.

## 8. Sign-off record (copy into each module's Phase 5)

| Scope | Reviewer (role) | Revision | Date | Evidence | Decision |
|---|---|---|---|---|---|
| Storyboard & visuals | | | | | |
| Narration script | | | | | |
| Activities & scoring | | | | | |
| Built package (preview) | | | | | |
| LMS test | | | | | |
| Final release | | | | | |

Any change after sign-off resets the affected rows.
