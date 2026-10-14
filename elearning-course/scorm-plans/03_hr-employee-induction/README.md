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
| SCORM | 2004 4th edition |
| Completion | `viewed_all_and_passed`, passing score **70** |
| Scored screens | 15, 145 points in total |
| Prerequisite | None — this is the first module in the learning path |

## Design idea in one paragraph

The HR deck is a full-day classroom induction: company story, values, the 7C strategy, leaders, branches, ethics, patients' rights, and a long run of HR policies. Most new starters don't need to memorise leave tables; they need to know **where the rule is, how to apply it to their own situation, and which system to use**. So the package keeps the "who we are" part short and warm (values, strategy, history, branches), turns ethics and patients' rights into short decisions, and turns HR policy into worked examples and a "leave desk" scenario where the learner handles colleagues' requests. Calculations (GOSI, overtime, sick-leave pay) are shown as worked examples and then practised once. The Oracle leave request becomes a guided click-through simulation. Policy details stay in a downloadable HR quick-reference PDF instead of on slides.

## Files

| Phase | File |
|---|---|
| 0 — Source lock | [phase-0-source-lock.md](phase-0-source-lock.md) |
| 1 — Action map & objectives | [phase-1-action-map.md](phase-1-action-map.md) |
| 2a — Screen list | [phase-2-storyboard.md](phase-2-storyboard.md) |
| 2b — Storyboard cards | [storyboard/storyboard.md](storyboard/storyboard.md) — **v0.1 drafted, in SME review** |
| 3 — Narration & assets | [phase-3-narration-and-assets.md](phase-3-narration-and-assets.md) |
| 4 — Build | [phase-4-build.md](phase-4-build.md) |
| 5 — QA & delivery | [phase-5-qa-and-delivery.md](phase-5-qa-and-delivery.md) |

## Current status

**Storyboard v0.1 drafted — in SME review.** All 36 screens have a finished card: on-screen wording, visual brief, animation/reveal, interaction and scoring with feedback, full narration script, accessibility notes, and the edumints JSON for each screen. Totals: 36 screens · 15 scored · 145 points · 366 on-screen words · 1,636 narration words (≈ 11 min 41 s of audio, inside the Phase 3 budget). Every JSON block validates against the server's `core/project.py` models.

**Still blocked on Phase 0**: HR policy confirmations (sick-leave pay B1, compassionate leave wording B2, ID-card penalty B4, overtime by grade B3, GOSI rates B12, SCFHS rule B13), branch names (B5/D3), personal-data policy (B6/D5), awards wording (B7), and the Oracle test account (B8 — this one blocks building `hr-061`).

**Narration done**: all 36 scripts written in the storyboard; `narration-script.json`,
`audio-script-export.json` and `voice_talent.md` generated from them. `lint_narration_script`
reports **0 errors, 0 warnings** (1,590 words, ~11 min 45 s of audio).

**Reference audio**: 10 clips, one per section (~5 min), in `storyboard/audio/` — enough to judge
the voice and the pacing. Voice route still open (program **D10**).

**Not yet started**: `visual-plan.json` (the Phase 2 exit gate), the remaining 26 audio clips, and
`lint_authoring_plan(stage="planning")`. Then the build (Phase 4).
