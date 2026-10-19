# My Clinic induction: proposal vs storyboard and interactivity audit

> **Follow-up (2026-10-19):** §6 proposals are partly built as the unscored personalisation layer — see [`personalisation-and-interactivity-plan.md`](personalisation-and-interactivity-plan.md) §3 (done) and §5 (backlog). Package 04's missing results screen is fixed (`ops-089`).

Read-only audit, 2026-10-19. No repo files were changed.

**Sources read**
- Proposal: `elearning-course/proposal/MyClinic_Induction_eLearning_Proposal_e2026-MC01_Rev01.docx`, extracted with python-docx (paragraphs and all 13 tables).
- Per package 01–08: `phase-2-storyboard.md` and `build/course-spec.json` (the actual screen types), plus `build/build-report.json` (lint), `build/asset-map.json` and `phase-5-qa-and-delivery.md` (test-case rows).
- Programme level: `00_program/scorm-structure.md`, `scorm-base-audit.json`, `gamification-plan.md` and `scenario-design-plan.md`.
- Compiler: `/home/user/marwanabdulhady-gif/edumints-scorm-mcp` @ `4bbf459`, specifically `core/project.py`, `core/game_primitives.py`, `components/renderer.py`, `components/templates.py` and `docs/SCREEN_TYPES.md`.

---

## 1. What the proposal commits to (Rev01, 14-10-2026)

| Area | Commitment |
|---|---|
| Courses / packages | 6 courses, 8 SCORM packages (HSE ×2, HR, Ops, RCM ×2, Quality, EHR) |
| Screens / scored | ≈207 screens · 95 scored activities |
| Scenarios / games / sims | 26 (HSE 8, HR 4, Ops 1, RCM 4, Quality 2, EHR 7) |
| Seat time | ≈4 h. HSE 90 (P1 ~55 + P2 ~35), HR 45, Ops 15, RCM 45 (A ~25 + B ~20), Quality 25, EHR 25 |
| Narration | ≈60 min (table total 62), two voices (Noor, Dr. Omar), captions and transcripts. Synthetic English voice |
| Visuals | 96 diagrams, images and screens (HSE 26, HR 11, Ops 6, RCM 10 + 2 job aids, Quality 8, EHR 35 screenshots) |
| Test cases | 81 course-specific (26/12/8/16/9/10) plus a common checklist; SCORM Cloud and client LMS; pilot with 5–8 starters |
| Pass marks | HSE 80, HR 70, Ops 70, RCM 80, Quality 80, EHR 80. HSE: completion = all screens viewed + pass |
| Interactivity | "High": branching scenarios, games, escape room, guided software sims, drag-drop, sorting, adaptive practice, knowledge checks with feedback |
| Characters | Noor (senior nurse) and Dr. Omar (family physician) host every course |
| Language | English. Arabic optional, quoted separately. HSE emergency-code flashcards are bilingual EN/AR |
| Standards | SCORM 1.2 or 2004 4th ed.; completion, score, objective-level and question-level reporting; WCAG 2.2 AA; responsive HTML5 |
| Deliverables | Storyboards, narration (audio, captions, transcript), asset pack with provenance, QA report, job aids (HR Quick Ref, physician desk checklist, EBP summary, EHR quick card, bilingual code cards), QTI 2.1 export, LMS upload and admin guide, 30 days of defect fixes |
| Timeline | 9–10 weeks, kick-off within 1 week; storyboards at end of Phase 2 (weeks 3–4) |
| Price | USD 1,500 per course = USD 9,000 (50 / 30 / 20 %), excl. VAT, valid 15 days |

## 2. Programme reconciliation

| Item | Proposal | Storyboards + course-spec | Status |
|---|---|---|---|
| Packages | 8 | 8 course-spec.json, all SCORM 1.2 | Match |
| Screens | 207 | 54+26+36+13+21+15+22+20 = 207 | Match |
| Scored activities | 95 | 24+13+15+4+10+7+11+11 = 95 (925 pts) | Match |
| Scenarios/games/sims | 26 | 5+3+4+1+2+2+2+7 = 26 | Match |
| Narration | ≈60–62 min | 8,682 narration words ≈ 62 min at 140 wpm | Match |
| Test cases | 81 | 14+12+12+8+9+7+9+10 = 81 rows in phase-5 | Match |
| Storyboard ↔ build spec | — | Every screen id, type and point value in `phase-2-storyboard.md` equals `course-spec.json` (scripted diff: 0 differences) | Match |
| Job-aid PDFs | 5 | None in any package asset list. HR links `{{asset:hr-pdf-quickref}}`; RCM A/B and EHR say "pending production" | Gap (not produced yet) |
| QTI 2.1 export | yes | No QTI file in repo | Gap (not produced yet) |
| Bilingual code cards | yes | 0 Arabic characters in any spec; `hs2-020` fronts read "Arabic name: ⚠ Draft — pending D2" | Gap (blocked by D2) |
| Assets | 96 | 68 files present, 55 PENDING (EHR 31 of 35 pending the test-env capture) | In progress |
| Role personalisation | Not promised | None (no `variables`, `visible_if` or `points_var` in any spec) | Opportunity |

Minor inconsistency: `00_program/scorm-structure.md` §3 says the worst-case `suspend_data` for 01 is 749 bytes. `scorm-base-audit.json` reports 2,448 of 4,096 characters. Reconcile these before adding variables or exploration inputs, which also live in `suspend_data`.

## 3. Alignment per course

### Course 1 HSE (packages 01 + 02)

| Item | Proposal | Storyboard / spec | Status |
|---|---|---|---|
| Screens | ≈80 | 54 + 26 = 80 | Match |
| Scored | 37 | 24 + 13 | Match |
| Scenarios/games | 8 | hs1-205, 409, 507, 802, 950 + hs2-030, 052, 064 | Match |
| Seat time | ~55 + ~35 | PT55M + PT33M | Minor gap: P2 is 2 min short |
| Narration | 23 min | ≈16.5 + 6.6 min | Match |
| Test cases | 26 | 14 + 12 | Match |
| Pass / completion | 80%, viewed all + pass | 80, `viewed_all_and_passed` | Match |
| Explore 8 plans, corridor fire kit, utilities | yes | hs1-102 (8 regions), hs1-404 (9 regions; storyboard says 8), hs1-701 | Match (hs1-404 has 1 extra region) |
| Sort RACE, PASS, controls, spill kit | yes | hs1-402, 403, 204, hs2-053 | Match |
| Decision scenarios: cable, night fire, 3 spills, pump | yes | hs1-205, 409, 507 / hs2-052, 802 | Match |
| Code Red branching game | rescue → call script → contain → extinguish/evacuate → chair → assembly | hs2-030 nodes: rescue, alarm, contain, extinguish, evacuate, assembly, debrief | Match |
| Hazard hunt (6) + risk scoring | yes | hs2-011 (6 regions) + hs2-013 (+ worked example hs2-010) | Match (+ extra worked example) |
| Drag-drops: extinguishers, evac tools, waste, allowed/prohibited | yes | hs1-405 / hs2-041, hs2-031, hs1-508, hs2-070 | Match |
| Escape room | yes | hs2-064 (4 puzzles) | Match |
| Capstone "One shift, three plans" | yes | hs1-950 `game` case_sim | Match |
| Results by objective | yes | hs1-980, hs2-080 | Match |
| Bilingual code flashcards | yes | hs1-301 / hs2-020 English only, Arabic pending D2 | Gap |
| Completion checklist | yes | hs1-990 | Match |
| Diagrams ≈26 | yes | 4 + 9 assets pending | In progress |
| Extras | — | confidence polls hs1-002/981, image_compare hs2-051, NFPA quiz hs1-503, floor-plan labelling hs2-032 | Extra (inside counts) |
| Lint | — | `free_hints` hs1-950, hs2-030; `unbound_scored_question` hs2-031; text-only runs (hs1-204..304, hs1-405..502, hs2-052..070); thin objectives hs1-o1, o6, o7, o10, hs2-o2, o4, o7 | Risk |

### Course 2 HR (package 03)

| Item | Proposal | Storyboard / spec | Status |
|---|---|---|---|
| Screens / scored / scenarios | 36 / 15 / 4 | 36 / 15 / hr-031, 044, 045, 061 | Match |
| Seat / narration / tests | 45 min / 12 / 12 | PT45M / ≈11.9 / 12 | Match |
| Pass | 70% | 70 | Match |
| Icebreaker poll, values matching | yes | hr-002, hr-011 (6 pairs) | Match |
| Ethics conflict-of-interest scenario | yes | hr-031 (3 nodes) | Match |
| Rights vs responsibilities sort | yes | hr-032 drag_drop | Match |
| Leave desk (4 colleagues) | yes | hr-044 (4 nodes) | Match |
| Adaptive leave practice | yes | hr-045 elo, bank 12, max 6 | Match |
| GOSI (585) + overtime worked examples then practice | yes | hr-051/052, hr-053/054 | Match |
| Oracle leave simulation | yes | hr-061 (5 steps; test-account screens pending B8) | Match (assets pending) |
| Task→system matching, dress code by role | yes | hr-060, hr-071 | Match |
| HR Quick Reference PDF + survey link | yes | Linked in hr-091; PDF not produced | Gap (production) |
| Visual sets ≈11 | yes | 24 of 41 assets pending | In progress |
| Lint | — | Only `scored_over_objectives` (advisory); no thin objectives | OK |

### Course 3 Operations & My Care (package 04)

| Item | Proposal | Storyboard / spec | Status |
|---|---|---|---|
| Screens / scored / scenario | 13 / 4 / 1 | 13 / 4 / ops-031 | Match |
| Seat / narration / tests | 15 / 4 / 8 | PT15M / ≈4.5 / 8 | Match |
| Pass | 70% | 70 | Match |
| Clickable patient journey | yes | ops-002 hotspot explore | Match |
| Role-based org charts (no names) | yes | ops-011, ops-021 labeled_diagram display | Match |
| Sort 10 activity cards | yes | ops-030 (10 items) | Match |
| "Who do I call?" 4 requests | yes | ops-031 (4 nodes) | Match |
| "Results by objective" | yes | No `results_breakdown`; ends on ops-090 summary. LMS still gets `cmi.objectives` | Gap (on-screen only) |
| Thin objectives | — | ops-o1, ops-o3 | Risk |
| Interactivity | — | ops-000..ops-022 = 8 consecutive unscored screens before any check | Weak point |

### Course 4 RCM (packages 05 + 06)

| Item | Proposal | Storyboard / spec | Status |
|---|---|---|---|
| Screens / scored / scenarios | 36 / 17 / 4 | 21+15 / 10+7 / rcma-031, rcma-050, rcmb-052, rcmb-060 | Match |
| Seat | ~25 + ~20 | PT25M + PT20M | Match |
| Narration / tests | 11 / 16 | ≈6.4 + 4.8 / 9 + 7 | Match |
| Pass | 80% | 80 / 80 | Match |
| Weak vs strong note | yes | rcma-011 image_compare | Match |
| Sort clinical picture; symptom→diagnosis | yes | rcma-012, rcma-021 | Match |
| Sort uncovered ICD-10 | yes | rcma-023 | Match |
| Joint-pain scenario | yes | rcma-031 (2 nodes) | Match |
| "Fix the note", 3 notes | yes | rcma-050 (3 notes + debrief) | Match |
| Added vs amended; benefit→limit | yes | rcmb-010, rcmb-041 | Match |
| Rejection log classify + rework | yes | rcmb-051, rcmb-052 | Match |
| Adaptive "Covered or not?" 15 requests | yes | rcmb-060 bank 15, `max_items` 8 (a learner sees ≤8) | Match (wording nuance) |
| Desk checklist PDF, EBP summary PDF, QTI export | yes | All marked pending in summaries; none produced | Gap (production) |
| Lint | — | rcma `text_only_run` across 14 screens (rcma-012..rcma-050), `free_hints` rcma-050; thin rcma-o5, rcmb-o1 | Risk |

### Course 5 Clinical Governance (package 07)

| Item | Proposal | Storyboard / spec | Status |
|---|---|---|---|
| Screens / scored / scenarios | 22 / 11 / 2 | 22 / 11 / qsr-021, qsr-051 | Match |
| Seat / narration / tests | 25 / 7 / 9 | PT25M / ≈6.2 / 9 | Match |
| Pass | 80% | 80 | Match |
| Speak-up reflection | yes | qsr-002 poll | Match |
| S-P-O sort; FOCUS-PDCA order | yes | qsr-011, qsr-012 | Match |
| Explore 6 goals; "Which Mohammed?" | yes | qsr-020 (6 regions), qsr-021 | Match |
| Practice→goal; 5 moments | yes | qsr-022, qsr-023 | Match |
| Risk matrix worked example, scoring, response | yes | qsr-031, qsr-032, qsr-033 | Match |
| Iceberg 6 events; near-miss scenario | yes | qsr-041 (6), qsr-051 | Match |
| New narration from corrected transcript | yes | narration_text present; audio not built | In progress |
| Optional speak-up clip | optional | qsr-060 not in spec (by design) | Match |
| Lint | — | `text_only_run` qsr-041..qsr-051; thin qsr-o5 | Risk |

### Course 6 IT: EHR (package 08)

| Item | Proposal | Storyboard / spec | Status |
|---|---|---|---|
| Screens / scored / sims | 20 / 11 / 7 | 20 / 11 / ehr-010, 020, 031, 032, 040, 041, 050 | Match |
| Seat / narration / tests | 25 / 5 / 10 | PT25M / ≈5.2 / 10 | Match |
| Pass | 80% | 80 | Match |
| Mandatory-fields exploration | yes | ehr-011 hotspot explore | Match |
| Non-formulary and diagnosis-link questions | yes | ehr-033, ehr-034 | Match |
| Sort 9-step workflow | yes | ehr-051 | Match |
| Works with sound off; alt text | yes | 0 simulation steps missing `image_alt` | Match |
| ≈35 test-patient screenshots | yes | 31 of 35 PENDING (test environment) | In progress |
| EHR quick card PDF | yes | Marked pending in ehr-091 | Gap (production) |
| Lint | — | `too_many_list_items` ehr-042; thin ehr-o2, ehr-o5 | Risk |

## 4. Interactivity audit (actual types from `course-spec.json`)

Classes used below:
- **Passive**: title_slide, content_slide, summary, results_breakdown.
- **Display**: labeled_diagram with `mode: display`.
- **Formative**: unscored but clickable (hotspot explore, accordion, tabs, flashcards, timeline, poll, worked_example, image_compare).
- **Scored**: points > 0.

| Pkg | Screens | Type counts | Passive | +Display | Formative | Scored |
|---|---:|---|---:|---:|---:|---:|
| 01 | 54 | title 1, content 9, poll 2, hotspot 3, matching 5, flashcards 2, accordion 4, labeled_diagram 5, sorting 4, decision_scenario 4, drag_drop 2, tabs 3, mcq 5, true_false 2, game 1, results 1, summary 1 | 22% | 30% | 26% | 44% |
| 02 | 26 | title 1, content 4, worked_example 1, hotspot 2, mcq 3, fill_blank 1, flashcards 1, game 1, drag_drop 3, labeled_diagram 1, image_compare 1, decision_scenario 1, sorting 1, matching 1, escape_room 1, results 1, poll 1, summary 1 | 27% | 27% | 23% | 50% |
| 03 | 36 | title 1, content 8, poll 1, tabs 1, matching 3, accordion 2, mcq 4, timeline 1, hotspot 1, flashcards 1, decision_scenario 2, drag_drop 2, worked_example 3, adaptive 1, fill_blank 1, simulation 1, true_false 1, results 1, summary 1 | 31% | 31% | 28% | 42% |
| 04 | 13 | title 1, content 1, hotspot 1, accordion 2, labeled_diagram 2, flashcards 1, drag_drop 1, decision_scenario 1, mcq 1, matching 1, summary 1 | 23% | 38% | 31% | 31% |
| 05 | 21 | title 1, content 4, poll 1, tabs 1, image_compare 1, sorting 1, mcq 3, matching 1, worked_example 1, drag_drop 2, decision_scenario 1, true_false 1, game 1, results 1, summary 1 | 33% | 33% | 19% | 48% |
| 06 | 15 | title 1, content 2, drag_drop 2, tabs 2, mcq 1, accordion 1, true_false 1, matching 1, decision_scenario 1, adaptive 1, results 1, summary 1 | 33% | 33% | 20% | 47% |
| 07 | 22 | title 1, content 2, poll 2, labeled_diagram 2, drag_drop 2, sorting 3, hotspot 1, decision_scenario 2, matching 2, worked_example 1, fill_blank 1, true_false 1, results 1, summary 1 | 23% | 32% | 18% | 50% |
| 08 | 20 | title 1, content 4, timeline 1, simulation 7, hotspot 1, mcq 3, sorting 1, results 1, summary 1 | 35% | 35% | 10% | 55% |
| **All** | **207** | | **57 = 27.5%** | **65 = 31%** | **47 = 23%** | **95 = 46%** |

**Runs of 3 or more consecutive passive screens**
- Only one: **ehr-052 → ehr-090 → ehr-091**, a content slide followed by results and summary.
- No other module has three passive screens in a row, so the storyboards' own flow checks hold.

**Runs of 4 or more screens with nothing scored or checked** (this is where engagement actually drops)
- 01: hs1-000 → hs1-103 (6 screens)
- 02: hs2-000 → hs2-011 (4)
- 03: hr-000 → hr-010 (4), and hr-014 → hr-030 (6)
- 04: **ops-000 → ops-022 (8 of the module's 13 screens)**
- 05: rcma-000 → rcma-011 (5)
- 07: qsr-000 → qsr-010 (4)

**Visual-poverty runs** (compiler lint `text_only_run`)
- 01: hs1-103..202 (4), hs1-204..304 (7), hs1-405..502 (8), hs1-507..602 (4), hs1-904..950 (5)
- 02: hs2-052..070 (8)
- 05: rcma-012..050 (14)
- 07: qsr-041..051 (4)

**Verdict.** The courses are already fairly interactive: 46% of screens are scored and 73% need learner action. The weak spots are:
- the opening stretch of every module
- package 04's first two-thirds
- the end of package 08
- long text-only runs in 01 and 05
- no personalisation at all: every learner sees the same path, whatever their role.

## 5. What the compiler supports (edumints @ 4bbf459)

**Screen types (31, `core/project.py` `ScreenType`)**
`title_slide, content_slide, mcq, true_false, fill_blank, drag_drop, hotspot, branching, video, summary, accordion, tabs, flashcards, matching, sorting, timeline, lottie, simulation, decision_scenario, term_match_race, escape_room, labeled_diagram, data_chart, results_breakdown, poll, image_compare, game, adaptive_practice, worked_example, exploration, embed_html`.

There is **no** `click_reveal`, `show_if` or `conditional` type. Their equivalents:
- Click to reveal: `content_slide` with `reveal: "click"` (blocks appear one click at a time); `accordion`, `tabs` or `flashcards`.
- Hotspot exploration: `hotspot` with `mode: "explore"`, optional `require_all: true`, and regions `{id, shape: "rect"|"circle", coords, label_html, feedback_html}`. A `poly` shape fails the build.
- Read-only callouts: `labeled_diagram` with `mode: "display"`.

**Variables and conditions (course level plus `ScreenBase`, all screen types)**
- Course: `variables: [{name, type: "number"|"text"|"bool", default}]`; HUD options `points_var`, `levels: [{name, min_points}]`, `lives_var`, `max_lives`.
- Every screen: `visible_if: {var, cmp: "=="|"!="|">"|"<"|">="|"<=", value}` (one condition, no AND/OR); `on_enter: [VarAction]`; `on_correct` / `on_wrong: [VarAction]` on quiz types; `timer_sec`, `on_timeout`, `timeout_goto`.
- `VarAction = {var, op: "set"|"add", value}`.
- `branching` screen: `prompt_html`, `choices: [{id, text_html, goto_screen_id, set_vars: [VarAction]}]`, `default_goto`. The runtime `next()` is disabled on a branching screen, so the learner must choose.
- Text interpolation: `{{varname}}` in any rendered text node is replaced by `state.vars[varname]`. This only works when the course declares `variables`.
- Variables persist in `suspend_data` (`extra.a = state.vars`).
- Learner input replay: `exploration` with `input_kind: "text"|"choice"|"prediction"|"slider"`, `store_key` (unique, `[a-z0-9_-]`), `choices`, `min_value` / `max_value` / `step` / `unit`. It is unscored. Later screens echo the input with `<span data-exploration-ref="store_key">`, stored in `suspend_data` (`xp`, values cut at 500 characters).
- Formative quizzes: any quiz type with `points: 0` is treated as formative. It is outside the score, but it still writes `cmi.interactions`.

**Limits that matter for role personalisation**
1. `total_points` is computed at build time over **all** scored screens, visible or not. A role-gated screen must therefore be unscored (`points: 0`), or learners who skip it can never reach the full score. All scored activities stay common to every role.
2. Hidden screens do not block completion. `viewedAll()` accepts `state.reachedEnd`, which is set on reaching the last screen. The last screen (the summary) must therefore never carry `visible_if`.
3. `game` choices have `condition` and `GameAction var.set`, but on game-local variables (`ctx.vars = {}`). They cannot read the course `role`. `decision_scenario` has no conditions. Role-specific scenarios have to be separate unscored screens with `visible_if`.
4. Each package is its own SCO, so the role does not carry between packages. Either ask once per package (one `branching` screen each) or rely on LMS audience groups.
5. `gamification-plan.md` and `tools/audit_scorm_base.py` exclude leaderboards, ranking, streaks, **badges** and **countdowns/time limits**. Do not use `levels`, `timer_sec` or `term_match_race`. `points_var` shows a star counter that could be mistaken for the score; leave it off unless L&D approves.
6. `suspend_data` on SCORM 1.2 is capped at 4,096. Package 01 is already at 2,448 by the base audit. Keep text explorations short, and prefer choice or slider inputs.
7. Interpolated on-screen text (`{{role_label}}`) will not match pre-recorded narration. Keep variable text out of `narration_text`.

**Recommended role pattern**
Declare course `variables` `role` (text, default `"all"`) and `role_label`. Then:
- Insert one `branching` screen after the opening screens, with one choice per role, each with `set_vars` and `goto_screen_id` set to the next screen. Include a "show me everything" choice (`all`).
- Add short role-tip screens, `accordion` or `tabs` with `points: 0`, gated by `visible_if: {"var":"role","cmp":"==","value":"clinical"}`.
- Personalise shared screens with `{{role_label}}`.

## 6. Upgrade proposals per package

None of these change points, objectives or pass marks. The full machine-readable list is `interactivity-upgrades.json` (73 rows; 14 need an image, of which 2 are EHR screenshots to capture rather than generate).

**All packages**
- Add a role picker (`branching`): +1 screen per package.
- Add mission framing: section titles as "Mission n of N", `on_enter` add on a `missions` variable, and an echo on the results/summary screens, with no HUD.
- Turn polls into `exploration` where the answer should be replayed in the summary.

**Changes per package**
- **01 FMS:**
  - hs1-101 → exploration (prediction)
  - hs1-103 → flashcards
  - hs1-303 → formative true_false
  - hs1-410 → hotspot explore (new image)
  - hs1-501 → formative mcq
  - hs1-506 → exploration (eyewash, replayed in the hs1-990 checklist)
  - hs1-801 → hotspot explore (new image)
  - hs1-907 → flashcards
  - hs1-305 → hotspot explore (existing image)
  - role tips after hs1-410: "your part in a Code Red"
- **02 Safety Lab:**
  - hs2-001 → slider prediction, replayed at hs2-011
  - hs2-033 → hotspot explore on the hs2-032 plan
  - hs2-050 → formative true_false
  - hs2-060 → hotspot explore on a rendered register (new image)
  - hs2-081 poll → text exploration, replayed at hs2-090
  - role tips after hs2-030
- **03 HR:**
  - role picker using the hr-071 groups (front office / medical team / back office)
  - hr-014 and hr-022 → flashcards
  - hr-030 → exploration
  - hr-040 → click-reveal plus role help-desk variants
  - hr-050 → slider prediction
  - hr-070 → hotspot explore (new image)
  - hr-080 → timeline
  - role-specific dress-code tips after hr-071 (3 illustrations)
- **04 Ops:**
  - ops-001 → prediction, replayed at ops-031
  - ops-011 and ops-021 → hotspot explore on the existing charts
  - NEW formative mcq ops-012, which breaks the 8-screen run
  - role tips after ops-033
  - NEW ops-089 `results_breakdown`, which closes the proposal gap
- **05 RCM A:**
  - role picker: physician / dentist / RCM
  - rcma-002 poll → exploration, replayed at rcma-020 and rcma-040
  - rcma-020 and rcma-030 → flashcards (new images)
  - rcma-041 → formative true_false
  - role coding tips after rcma-023
  - small note-card SVGs to break the 14-screen text-only run
- **06 RCM B:**
  - rcmb-001 → slider prediction
  - rcmb-050 → hotspot explore on the rendered rejection log (new image)
  - role rework tips after rcmb-052
- **07 Quality:**
  - qsr-010 and qsr-040 → hotspot explore (existing images)
  - qsr-050 → timeline (new image)
  - role tips after qsr-023
  - qsr-091 → text exploration, replayed in qsr-092
- **08 EHR:**
  - role picker: physician / nurse
  - ehr-030 → hotspot explore on the order-search screenshot
  - ehr-042 → flashcards (also fixes the list lint)
  - ehr-052 → hotspot explore on the completion screenshot (breaks the only 3-passive run)
  - role tips after ehr-042

**Estimated effect (learner view).** Passive share falls from 27.5% to about 13% overall:
- 01: 22 → 7%
- 02: 27 → 11%
- 03: 31 → 13%
- 04: 23 → 18%
- 05: 33 → 17%
- 06: 33 → 18%
- 07: 23 → 17%
- 08: 35 → 18%

Each learner sees about 2 extra screens per package (4 in package 04). Build specs grow by roughly 30 screens in total because of the role variants.

**Change-control notes**
- New screens push the build count above the proposal's "≈207". Record them as unscored additions in the change log (a minor version, per `scorm-structure.md` §6), then rerun `tools/audit_scorm_base.py` and `build_scorm_structure.py`.
- Formative `points: 0` checks add `cmi.interactions` rows. Confirm with the client that LMS question-level reports can ignore them, or use `exploration` instead.
- Role-tip content and any role mapping (for example, who in the EHR places diagnoses, or dental ICD examples) need SME sign-off, as does any rule still blocked by an open item (D2, B4–B9).
