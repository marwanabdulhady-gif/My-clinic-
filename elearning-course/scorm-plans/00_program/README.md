# 00_program — programme files by phase

![My Clinic logo](brand/logo-preview.png)

Everything that applies to **all eight packages**, grouped by the phase it belongs to. Module-specific files live in each `0N_…/` folder (see [`../../PROJECT-MAP.md`](../../PROJECT-MAP.md)).

## Status and plan

| File | What it is |
|---|---|
| [`programme-status.md`](programme-status.md) | Module × phase grid, gaps G1–G25, ordered next steps |
| [`next-phases-roadmap.md`](next-phases-roadmap.md) | Remaining work cut into PR-sized chunks C0–C28 |
| [`plan-audit.md`](plan-audit.md) | Proposal-to-plan cross-check and gate results |
| [`client-context.md`](client-context.md) | Public context on My Clinic KSA and approval cautions |

## Phase 0 — Source lock and decisions

| File | What it is |
|---|---|
| [`cross-module-decisions.md`](cross-module-decisions.md) | D1–D17 programme decisions |
| [`decision-sheet.md`](decision-sheet.md) · [`decision-sheet.csv`](decision-sheet.csv) | Every open decision (D-items + module B-items) with owner, due date, write-back target |
| [`kickoff-pack.md`](kickoff-pack.md) · [`kickoff-pack.docx`](kickoff-pack.docx) | Kick-off meeting pack MC-KO-01 v0.3 |
| [`kickoff-assumed-answers.md`](kickoff-assumed-answers.md) · [`.csv`](kickoff-assumed-answers.csv) · [`kickoff-research-notes.md`](kickoff-research-notes.md) | Researched working assumption for every open decision, the ten deck contradictions, sources |

## Phase 1–2 — Action map, storyboards and review

| File | What it is |
|---|---|
| [`storyboard-template/`](storyboard-template/) | Storyboard template, screen-type guide, worked examples, review checklist |
| [`course-templates/`](course-templates/) | One prefilled production worksheet per package |
| [`storyboard-production-board.md`](storyboard-production-board.md) · [`.html`](storyboard-production-board.html) | Storyboard pack status board |
| [`storyboard-review-register.md`](storyboard-review-register.md) · [`.csv`](storyboard-review-register.csv) | Screen-level SME build-detail questions |
| [`scenario-design-plan.md`](scenario-design-plan.md) · [`gamification-plan.md`](gamification-plan.md) | Scenario inventory, game mechanics, scoring, retries |
| [`storyboard-proposal-check.md`](storyboard-proposal-check.md) | Storyboards vs proposal Rev01, interactivity audit, compiler capabilities |
| [`inspiration-portfolio-review.md`](inspiration-portfolio-review.md) | Instructional-design portfolio review: patterns and 15 ranked upgrades for the courses; the top seven are applied (see `gamification-plan.md`) |
| [`personalisation-and-interactivity-plan.md`](personalisation-and-interactivity-plan.md) · [`roles.json`](roles.json) · [`interactivity-upgrades.json`](interactivity-upgrades.json) | Who the induction is for, role paths, the unscored personalisation layer, backlog |
| [`draft-slide-production.md`](draft-slide-production.md) · [`draft-slide-phases.json`](draft-slide-phases.json) · [`screen-generator.md`](screen-generator.md) | Pre-kick-off browser slide drafts (review renderer) |

## Brand, characters and visuals (Phases 2–3)

| File | What it is |
|---|---|
| [`brand/`](brand/) | Brand identity, logo files, fonts, `edumints-skin.css` (player skin incl. the brand weave) |
| [`brand-and-theme.md`](brand-and-theme.md) | Theme decision, Arabic/RTL plan |
| [`characters/`](characters/) | Noor and Dr. Omar: bible, full-size art, avatars |
| [`visual-production-plan.md`](visual-production-plan.md) · [`visual-generation-prompts.md`](visual-generation-prompts.md) | Visual hand-off and image prompts |
| [`visual-and-motion-agent-brief.md`](visual-and-motion-agent-brief.md) | Minimum asset inventory, video decision, agent instructions |
| [`media-production-runbook.md`](media-production-runbook.md) · [`media-jobs-summary.md`](media-jobs-summary.md) | How image/audio/video agents work the generated job lists; hotspot maps |
| [`video-tooling.md`](video-tooling.md) · [`media-video-plan.json`](media-video-plan.json) | Motion-graphics tools (HyperFrames, Remotion …) and the optional clip plan |
| [`video-playbook-review.md`](video-playbook-review.md) · [`../../video/README.md`](../../video/README.md) | Owner's video playbook vs our plan; where clips are made, names, QA scripts, 44-step agent procedure |
| [`motion-and-animation-spec.md`](motion-and-animation-spec.md) · [`motion-spec-summary.json`](motion-spec-summary.json) | Structured motion spec per screen |
| [`g10-visual-restoration.md`](g10-visual-restoration.md) · [`asset-approval-handoff/`](asset-approval-handoff/) | Restored planned visuals and the SME approval hand-off |
| [`asset-template-audit.md`](asset-template-audit.md) · [`asset-audit.json`](asset-audit.json) | Asset, template, logo and link audit |

## Phase 3 — Narration

| File | What it is |
|---|---|
| [`narration-and-lexicon.md`](narration-and-lexicon.md) | Voices, writing rules, pronunciation lexicon |
| [`narration-production-plan.md`](narration-production-plan.md) | Audio production workflow and audio-agent hand-off |

## Phase 4 — SCORM structure and build

| File | What it is |
|---|---|
| [`scorm-structure.md`](scorm-structure.md) · [`scorm-structure-summary.json`](scorm-structure-summary.json) | How the packages are structured (LMS, zip, manifest, outline, tracking) |
| [`scorm-base-audit.md`](scorm-base-audit.md) · [`scorm-base-audit.json`](scorm-base-audit.json) | Structure gate: screens, scored items, scenarios, objectives |
| [`build-pipeline.md`](build-pipeline.md) | Tool sequence, settings, local edumints compile (§6) |
| [`draft-builds.md`](draft-builds.md) | Current draft packages: results per module |
| [`c14-implementation.md`](c14-implementation.md) | 03 + 07 build chunk notes |
| [`scorm-package-builds.md`](scorm-package-builds.md) · [`scorm-package-builds.json`](scorm-package-builds.json) | First 03/07 pilot build (superseded route, kept as record) |

## Phase 5 — QA, LMS and delivery

| File | What it is |
|---|---|
| [`oracle-learning-compatibility.md`](oracle-learning-compatibility.md) | Oracle Learning requirements, SCORM 1.2 decision, evidence |
| [`xsd-validation.md`](xsd-validation.md) · [`xsd-schema-provenance.json`](xsd-schema-provenance.json) | Manifest XSD validation results |
| [`qa-checklist.md`](qa-checklist.md) | Common QA checklist and sign-off record |
| [`../00_sample-oracle-pilot/`](../00_sample-oracle-pilot/) | Sample package and Oracle test guide |
