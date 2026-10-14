# My Clinic — SME review and build-detail register

> **Review routing record · 2026-10-14.** This register consolidates screen-level authoring details
> that need review before Phase 4. It is not an approval log and does not turn an open source value
> into course policy. Record final policy/source decisions in each module’s Phase 0 file and in
> [`cross-module-decisions.md`](cross-module-decisions.md), then regenerate the affected pack.

## What this register checks

The register tests whether a **scored** Phase 2 row contains the source detail needed to make a
specific build object: an answer/route, feedback cue, any pass/replay rule, and typed-input variants
where the task asks the learner to type. A row not listed in the queue has source detail present;
it is still a **draft** awaiting SME confirmation.

| Scope | Count |
|---|---:|
| Scored review screens across the six new packs | 69 |
| Source-detail present in the Phase 2 brief | 32 |
| Screen-level build-detail review questions | 37 |

## Module triage

| Module | Scored screens | Source-detail present | Build-detail questions | Review artefacts |
|---|---:|---:|---:|---|
| 01 — Facility Management & Safety | 24 | 14 | 10 | [54 screen cards](../01_health-and-safety-1/storyboard/storyboard.md) · [visual board](../01_health-and-safety-1/storyboard/screen-visuals.html) |
| 02 — Safety in Practice: Hazard, Fire & Chemical Lab | 13 | 6 | 7 | [26 screen cards](../02_health-and-safety-2/storyboard/storyboard.md) · [visual board](../02_health-and-safety-2/storyboard/screen-visuals.html) |
| 04 — Who Does What: Operations & My Care | 4 | 1 | 3 | [13 screen cards](../04_operations-and-my-care/storyboard/storyboard.md) · [visual board](../04_operations-and-my-care/storyboard/screen-visuals.html) |
| 05 — RCM Part A: Documentation & ICD-10 Coding That Gets Approved | 10 | 6 | 4 | [21 screen cards](../05_rcm-documentation-and-coding/storyboard/storyboard.md) · [visual board](../05_rcm-documentation-and-coding/storyboard/screen-visuals.html) |
| 06 — RCM Part B: New EBP Benefits & Claim-Rejection Analysis | 7 | 3 | 4 | [15 screen cards](../06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md) · [visual board](../06_rcm-ebp-benefits-and-rejections/storyboard/screen-visuals.html) |
| 08 — EHR Consultation Workflow: Guided Simulation | 11 | 2 | 9 | [20 screen cards](../08_it-ehr-consultation/storyboard/storyboard.md) · [visual board](../08_it-ehr-consultation/storyboard/screen-visuals.html) |

## Screen-level build-detail queue

| Module | Screen | Type | Detail to close | Requested action | Source-lock reference | Review owner |
|---|---|---|---|---|---|---|
| 01 | [hs1-403](../01_health-and-safety-1/storyboard/storyboard.md#hs1-403) | `sorting` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-408](../01_health-and-safety-1/storyboard/storyboard.md#hs1-408) | `true_false` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-503](../01_health-and-safety-1/storyboard/storyboard.md#hs1-503) | `labeled_diagram` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-504](../01_health-and-safety-1/storyboard/storyboard.md#hs1-504) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-507](../01_health-and-safety-1/storyboard/storyboard.md#hs1-507) | `decision_scenario` | pass/replay rule | set pass score/lives and no-score-inflation replay behaviour | `D1` | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-702](../01_health-and-safety-1/storyboard/storyboard.md#hs1-702) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-802](../01_health-and-safety-1/storyboard/storyboard.md#hs1-802) | `decision_scenario` | correct/incorrect feedback copy, pass/replay rule | write source-cited correct and retry rationale; set pass score/lives and no-score-inflation replay behaviour | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-803](../01_health-and-safety-1/storyboard/storyboard.md#hs1-803) | `true_false` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-902](../01_health-and-safety-1/storyboard/storyboard.md#hs1-902) | `matching` | exact answer/route, correct/incorrect feedback copy | confirm the exact correct response and plausible distractors; write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 01 | [hs1-906](../01_health-and-safety-1/storyboard/storyboard.md#hs1-906) | `matching` | exact answer/route, correct/incorrect feedback copy | confirm the exact correct response and plausible distractors; write source-cited correct and retry rationale | `B5` | Safety Manager (lead); EHS; Facilities; Biomedical Engineering; RSO; Infection Control + L&D/authoring |
| 02 | [hs2-031](../02_health-and-safety-2/storyboard/storyboard.md#hs2-031) | `drag_drop` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 02 | [hs2-032](../02_health-and-safety-2/storyboard/storyboard.md#hs2-032) | `labeled_diagram` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 02 | [hs2-052](../02_health-and-safety-2/storyboard/storyboard.md#hs2-052) | `decision_scenario` | pass/replay rule | set pass score/lives and no-score-inflation replay behaviour | `D1` | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 02 | [hs2-053](../02_health-and-safety-2/storyboard/storyboard.md#hs2-053) | `sorting` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B4` | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 02 | [hs2-061](../02_health-and-safety-2/storyboard/storyboard.md#hs2-061) | `matching` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 02 | [hs2-062](../02_health-and-safety-2/storyboard/storyboard.md#hs2-062) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 02 | [hs2-063](../02_health-and-safety-2/storyboard/storyboard.md#hs2-063) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Safety Manager (lead); EHS; Facilities; Infection Control + L&D/authoring |
| 04 | [ops-031](../04_operations-and-my-care/storyboard/storyboard.md#ops-031) | `decision_scenario` | pass/replay rule | set pass score/lives and no-score-inflation replay behaviour | `B7` | Director of Operations (lead); My Care Manager; Patient Experience senior manager + L&D/authoring |
| 04 | [ops-032](../04_operations-and-my-care/storyboard/storyboard.md#ops-032) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B1` | Director of Operations (lead); My Care Manager; Patient Experience senior manager + L&D/authoring |
| 04 | [ops-033](../04_operations-and-my-care/storyboard/storyboard.md#ops-033) | `matching` | exact answer/route, correct/incorrect feedback copy | confirm the exact correct response and plausible distractors; write source-cited correct and retry rationale | See module Phase 0 and programme D11 | Director of Operations (lead); My Care Manager; Patient Experience senior manager + L&D/authoring |
| 05 | [rcma-021](../05_rcm-documentation-and-coding/storyboard/storyboard.md#rcma-021) | `matching` | exact answer/route | confirm the exact correct response and plausible distractors | `B4` | RCM lead (lead); Coding lead; Payer Relations; Medical Director + L&D/authoring |
| 05 | [rcma-031](../05_rcm-documentation-and-coding/storyboard/storyboard.md#rcma-031) | `decision_scenario` | pass/replay rule | set pass score/lives and no-score-inflation replay behaviour | `B10` | RCM lead (lead); Coding lead; Payer Relations; Medical Director + L&D/authoring |
| 05 | [rcma-032](../05_rcm-documentation-and-coding/storyboard/storyboard.md#rcma-032) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B3` | RCM lead (lead); Coding lead; Payer Relations; Medical Director + L&D/authoring |
| 05 | [rcma-033](../05_rcm-documentation-and-coding/storyboard/storyboard.md#rcma-033) | `true_false` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B8` | RCM lead (lead); Coding lead; Payer Relations; Medical Director + L&D/authoring |
| 06 | [rcmb-031](../06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md#rcmb-031) | `true_false` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | RCM lead (lead); Payer Relations; Coding lead; Data Protection Officer + L&D/authoring |
| 06 | [rcmb-041](../06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md#rcmb-041) | `matching` | exact answer/route, correct/incorrect feedback copy | confirm the exact correct response and plausible distractors; write source-cited correct and retry rationale | See module Phase 0 and programme D11 | RCM lead (lead); Payer Relations; Coding lead; Data Protection Officer + L&D/authoring |
| 06 | [rcmb-052](../06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md#rcmb-052) | `decision_scenario` | pass/replay rule | set pass score/lives and no-score-inflation replay behaviour | See module Phase 0 and programme D11 | RCM lead (lead); Payer Relations; Coding lead; Data Protection Officer + L&D/authoring |
| 06 | [rcmb-060](../06_rcm-ebp-benefits-and-rejections/storyboard/storyboard.md#rcmb-060) | `adaptive_practice` | exact answer/route | confirm the exact correct response and plausible distractors | See module Phase 0 and programme D11 | RCM lead (lead); Payer Relations; Coding lead; Data Protection Officer + L&D/authoring |
| 08 | [ehr-010](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-010) | `simulation` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-012](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-012) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B4` | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-031](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-031) | `simulation` | accepted typed-input variants | list case, unit and spelling variants for typed input | `B6` | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-032](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-032) | `simulation` | correct/incorrect feedback copy, accepted typed-input variants | write source-cited correct and retry rationale; list case, unit and spelling variants for typed input | `B6` | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-033](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-033) | `mcq` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B6` | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-040](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-040) | `simulation` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-041](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-041) | `simulation` | correct/incorrect feedback copy, accepted typed-input variants | write source-cited correct and retry rationale; list case, unit and spelling variants for typed input | `B8` | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-050](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-050) | `simulation` | correct/incorrect feedback copy | write source-cited correct and retry rationale | `B9` | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |
| 08 | [ehr-051](../08_it-ehr-consultation/storyboard/storyboard.md#ehr-051) | `sorting` | correct/incorrect feedback copy | write source-cited correct and retry rationale | See module Phase 0 and programme D11 | EHR Applications / EHR lead (lead); DPO; Medical Director; Pharmacy lead; RCM lead + L&D/authoring |

### How to close a row

1. The named domain SME confirms the controlled source detail and any associated Phase 0 decision.
2. L&D/authoring writes the concrete type-specific field(s): options/pairs, answer variants,
   feedback, branching paths, pass/replay rules or simulation regions.
3. Update the Phase 2/3/4 plan where appropriate, regenerate the review pack, rerun the visual
   and narration lint, and mark the row closed in the team’s tracker.
4. Do **not** infer a local threshold, payer rule, system label, extension number or clinical fact
   merely to clear this queue.

## Visual and privacy sign-off queue

| Module | Asset / screen | Check required | Review owner |
|---|---|---|---|
| 01 | `hs1-404` / `hs1-img-corridor.png` | Confirm all intended safety cues are factually depicted, then measure keyboard-reachable hotspot regions against the approved final image. | Safety Manager + Facilities |
| 02 | `hs2-011` / `hs2-img-storeroom.png` | Confirm all six hazards, especially the blocked exit and extinguisher cue, are visually unambiguous before scored hotspot coordinates are set. | Safety Manager + EHS |
| 04 | `ops-031` / `ops-img-reception-scenario.png` | Confirm neutral, fictional reception context and route any role/routing wording through the Operations SME; do not add personal data. | Director of Operations + DPO |
| 08 | All simulation captures | Capture only a test environment and fictional test patient. Verify every click region, label and typed-input variant after capture. | EHR Applications lead + DPO + Medical Director |

## Release boundary

- The six review packs are structurally complete and have clean visual-plan/narration lint reports.
- This register is a **pre-build review queue**. It does not approve policy content, final visual
  coordinates, shipping audio, test screenshots, SCORM packaging or LMS delivery.
- The CSV sibling, `storyboard-review-register.csv`, is provided for importing into an external
  tracker; `status` is intentionally initialised to **Open — review required before Phase 4**.
