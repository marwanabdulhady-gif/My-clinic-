# 03 — Welcome On Board: My Clinic & HR Essentials (SCORM plan)

![My Clinic logo](../00_program/brand/logo-preview.png)

| Item | Value |
|---|---|
| Source | `../../md/03_hr-employee-induction.md` (from `HR.pptx`, 62 slides, marked *Confidential*) |
| Package title | My Clinic — Welcome On Board: My Clinic & HR Essentials |
| Module prefix / ids | `hr-` |
| Brand | My Clinic brand — [`brand-identity.md`](../00_program/brand/brand-identity.md); module colour **Caring purple #652D8C**; layouts L1–L6 |
| Audience | All new employees (clinical and non-clinical), day 1–3 |
| Seat time | ~45 minutes |
| SCORM | 1.2 (Oracle Learning target; worst-case resume data 749/373 bytes of the 4,096 limit — see `00_program/oracle-learning-compatibility.md`) |
| Completion | `viewed_all_and_passed`, passing score **70** |
| Scored screens | 15, 145 points in total |
| Prerequisite | None — this is the first module in the learning path |
| Draft SCORM (v0.1) | [`build/MC_03_WelcomeOnBoard_v0.1-draft_1.2.zip`](build/MC_03_WelcomeOnBoard_v0.1-draft_1.2.zip) · [`preview.html`](build/preview.html) · `lint_course` 0 errors · `validate_package` ok (structural) · [`draft-builds.md`](../00_program/draft-builds.md) |

## Design idea in one paragraph

The HR deck is a full-day classroom induction: company story, values, the 7C strategy, leaders, branches, ethics, patients' rights, and a long run of HR policies. Most new starters don't need to memorise leave tables; they need to know **where the rule is, how to apply it to their own situation, and which system to use**. So the package keeps the "who we are" part short and warm (values, strategy, history, branches), turns ethics and patients' rights into short decisions, and turns HR policy into worked examples and a "leave desk" scenario where the learner handles colleagues' requests. Calculations (GOSI, overtime, sick-leave pay) are shown as worked examples and then practised once. The Oracle leave request becomes a guided click-through simulation. Policy details stay in a downloadable HR quick-reference PDF instead of on slides.

## Files

| Phase | File |
|---|---|
| 0 — Source lock | [phase-0-source-lock.md](phase-0-source-lock.md) |
| 1 — Action map & objectives | [phase-1-action-map.md](phase-1-action-map.md) |
| 2a — Screen list | [phase-2-storyboard.md](phase-2-storyboard.md) |
| 2b — Storyboard cards | [storyboard/storyboard.md](storyboard/storyboard.md) — **v0.2 (brand identity + companions Dr. Omar and Noor), ready for SME review** · [asset register](storyboard/asset-register.md) · [screen review board](storyboard/screen-visuals.html) · [lint report](storyboard/lint-report.json) |
| 2b — Visual plan (JSON) | [storyboard/visual-plan.json](storyboard/visual-plan.json) — **`lint_visual_plan` clean (0 errors, 0 warnings)** |
| 3 — Narration & assets | [phase-3-narration-and-assets.md](phase-3-narration-and-assets.md) |
| 4 — Build | [phase-4-build.md](phase-4-build.md) |
| 5 — QA & delivery | [phase-5-qa-and-delivery.md](phase-5-qa-and-delivery.md) |

## Current status

**Storyboard v0.2 (2026-10-14) — ready for SME review.** v0.2 retrofits the course companions: lead host Dr. Omar narrates (`OMAR:`), co-host Noor hosts the ethics scenario and the leave desk and shares the welcome and the close (`NOOR:`); companions are visible on 8 of 36 screens using only the shared `char-omar-*` / `char-noor-*` assets. v0.1 summary below, with v0.2 numbers where they changed. All 36 screens have a finished card in [`storyboard/storyboard.md`](storyboard/storyboard.md) with the full My Clinic brand identity applied (`L1`–`L6` layouts, logo specs, Caring purple `#652D8C`, petal watermarks, line icons, AI image prompts): on-screen wording, visual brief, animation/reveal, interaction and scoring with feedback, full narration script, accessibility notes, and the edumints JSON for each screen. Totals: 36 screens · 15 scored · 145 points · 366 on-screen words · 1,628 narration words in v0.2 (≈ 12 min of audio, inside the Phase 3 budget). Every JSON block validates against the server's `core/project.py` models.

**Visual plan done**: [`storyboard/visual-plan.json`](storyboard/visual-plan.json) generated from the storyboard and validated with `lint_visual_plan(plan, brand)` → **0 errors, 0 warnings**.

**Technical integration note**: the inspected edumints `BrandVoice.formality` schema accepts `formal`, `neutral` or `conversational`, while the unchanged official `brand-kit.json` says `conversational-professional`. Linting used an in-memory `conversational` mapping only; no brand-kit value was changed. Resolve the adapter/schema mapping before calling `brand_to_theme` in the production build.

**Still blocked on Phase 0**: HR policy confirmations (sick-leave pay B1, compassionate leave wording B2, ID-card penalty B4, overtime by grade B3, GOSI rates B12, SCFHS rule B13), branch names (B5/D3), personal-data policy (B6/D5), awards wording (B7), and the Oracle test account (B8 — this one blocks building `hr-061`).

**Narration done (v0.2)**: all 36 screens scripted in 39 speaker-tagged lines (Dr. Omar 35, Noor 4); `narration-script.json`,
`audio-script-export.json` and `voice_talent.md` regenerated from them. `lint_narration_script(script, plan)`
reports **0 errors, 0 warnings** (1,628 words, ≈ 12 min of audio). `lint_visual_plan` also reports 0 / 0.

**Reference audio**: 10 v0.1 clips in `storyboard/audio/` — single-voice reference reads made before the companions, now **superseded**; not the Noor / Dr. Omar voices. Voice route still open (program **D10**).

**Authoring-plan quality gate**: a planning-stage draft assembled from the storyboard, narration and visual plan was checked with `lint_authoring_plan(stage="planning")` → **0 errors, 0 warnings**. The draft is not persisted as `authoring-plan.json` yet; save it when Phase 3 resumes after SME review.

**Not yet started**: shipping audio in the two companion voices (after D10 and the voice samples). Then proceed to the human approval gate and the build (Phase 4).
