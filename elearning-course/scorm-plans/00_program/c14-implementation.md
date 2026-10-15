# C14 implementation start — branded review tooling, modules 03 + 07

**14 October 2026 · implementation started, production exit gate blocked.**
References: [C14 issue #28](https://github.com/marwanabdulhady-gif/My-clinic-/issues/28),
[roadmap](next-phases-roadmap.md), [scenario design plan](scenario-design-plan.md),
[03 worksheet](course-templates/03-hr-employee-induction-production-worksheet.md),
[07 worksheet](course-templates/07-quality-safety-and-risk-production-worksheet.md).

PRs #33 and #34 are merged; their decision sheet and production handoff are now the
execution baseline. They did not close client decisions or authorise final assets.

## Implemented in this first preparatory slice

- Shared local screen renderer; supplied branding, exact screen IDs/order, transcripts,
  planned points/objectives/evidence, search/navigation and build-issue reporting.
- Modules 03 and 07 are the first detailed inputs. Other packages remain review briefs
  where their JSON is skeletal. The generator does not expand those briefs into policy.
- Decision scenarios `hr-031`, `hr-044`, `qsr-021`, `qsr-051`: one decision at a time;
  authored choice feedback; exact target transitions; locked choices to prevent repeated
  scoring; draft branch totals; explicit feedback-continue step; reset; keyboard controls.
- Pure scenario state separated from the DOM for exhaustive path tests. Missing target,
  feedback, score, cycles and unreachable nodes are rejected as unsupported/incomplete;
  no fallback answer, target or retry policy is invented.
- Pending clinical-policy wording is retained. The displayed outcome is not a learner
  pass, module score, client approval or an LMS report. Planned screen points remain untouched.
- Missing media remains labelled. Existing preview-resolution companions are placed from
  Phase 3 tables; the full-size companion art landed separately (G6 closed 2026-10-15,
  `00_program/characters/assets/`). No source-video
  patient data is copied; no final voices or generated video are produced.
- **Pre-kickoff drafting batch 1**: 58 current-content slides for 03/07, 61 actual browser
  captures and an eight-reference comparison gallery. Production worksheets/all six
  phase plans are required and reconciled; mockup geometry is compiled from HTML;
  licensed fonts are bundled. [Scope, evidence and next batches](draft-slide-production.md).

The shared preview is supporting infrastructure for C14, not completion of C14 or another
roadmap chunk. Usage and full coverage limits: [screen-generator.md](screen-generator.md).

## Local verification (not delivery QA)

- Repository Python gate: **27 tests pass**, including generator/template/layout/font and stale-capture checks.
- Node scenario gate: **189 exact authored paths across 4 scenarios pass**, plus state and
  malformed-graph tests.
- Browser smoke: **207 screens visited**; draft answer checks, scenario keyboard flow,
  policy markers, reset, navigation memory, search, 390px overflow and missing-resource checks.
- First-batch screenshot gate: **58 slides / 61 PNGs / 58 mobile checks**, local fonts,
  no browser errors or missing/external requests. Dense slides are full-height captures,
  not a claim of final 16:9 production pagination.
- Planning lint: all eight packages **0 errors / 0 warnings**.
- Asset/link audit: **0 hard failures**.

This does not constitute `lint_course`, SCORM validation, the 81-case delivery QA suite,
full accessibility testing, an LMS upload/resume test or a pilot.

## Next implementation order / gates

| Work | State | Required before production |
|---|---|---|
| Common branded review renderer | implemented | designer/client review, confirmed D11 |
| 03/07 decision-scenario playback | local draft implemented | SME approval of facts, keys and feedback |
| 03 adaptive practice `hr-045` | not implemented | upstream algorithm contract and approved rules |
| 03 Oracle simulation `hr-061` | structured review only | approved test captures and target alignment |
| 07 spatial interactions | structured review only | approved visuals and policy/matrix decisions |
| Companion placement | draft placements implemented from Phase 3, using review art | visual approval (C7 full-size artwork landed 2026-10-15) |
| Cue timing, final audio | not implemented | C6/D10 voices, C10 media |
| edumints project/spec, theme and tracking | not started | C10 completion, relevant Phase 0 closures, D9 |
| Server `lint_course` and preview | blocked | actual edumints build + reviewed media |
| SCORM export / actual LMS / pilot | not started | production exit gate and C18 |

C14 remains open. Do not mark a worksheet build/QA checkbox complete or close issue #28
based on these local tests. Next production handoff is C10 assets plus 03/07 SME decisions,
then upstream build/spec validation and the roadmap's production preview gate.
