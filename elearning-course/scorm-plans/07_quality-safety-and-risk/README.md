# 07 — Clinical Governance: Quality, Patient Safety & Risk (SCORM plan)

![My Clinic logo](../00_program/brand/logo-preview.png)

| Item | Value |
|---|---|
| Source | `../../md/07_video-quality-safety-and-risk-orientation.md` (from `Quality, Safety and Risk Orientation.mp4`, 8 min 56 s, narrated; screenshots in `../../media/07_quality-safety-risk/`) |
| Package title | My Clinic — Clinical Governance: Quality, Patient Safety & Risk |
| Module prefix / ids | `qsr-` |
| Brand | My Clinic brand — [`brand-identity.md`](../00_program/brand/brand-identity.md); module colour **Caring purple #652D8C**; layouts L1–L6 |
| Audience | All clinical staff (and recommended for all staff) |
| Seat time | ~25 minutes |
| SCORM | 1.2 |
| Completion | `viewed_all_and_passed`, passing score **80** |
| Scored screens | 11, 95 points in total |
| Prerequisite | 03 Welcome On Board |

## Design idea in one paragraph

The source is a 9-minute narrated video (NotebookLM-style, watermarked) with five parts: the quality standard, the six International Patient Safety Goals, risk management, the incident iceberg, and incident reporting. The package is designed to rebuild the content natively with new visuals and narration, without reusing source frames or audio. Learners practise sorting Structure/Process/Outcome examples, ordering FOCUS-PDCA, identifying the right patient when two share a name, matching practices to the six goals, scoring a risk and choosing a response, classifying events, and reporting a near miss at the end of a shift. D7 remains open; the optional source-video reuse route is not included in the baseline. A new in-house "speak up" message is also optional and requires approval.

## Files

| Phase | File |
|---|---|
| 0 — Source lock | [phase-0-source-lock.md](phase-0-source-lock.md) |
| 1 — Action map & objectives | [phase-1-action-map.md](phase-1-action-map.md) |
| 2a — Screen list | [phase-2-storyboard.md](phase-2-storyboard.md) |
| 2b — Storyboard cards | [storyboard/storyboard.md](storyboard/storyboard.md) — **v0.1 drafted; 22 core screens, pending SME / Phase 0 review** |
| 3 — Narration & assets | [phase-3-narration-and-assets.md](phase-3-narration-and-assets.md) |
| 4 — Build | [phase-4-build.md](phase-4-build.md) |
| 5 — QA & delivery | [phase-5-qa-and-delivery.md](phase-5-qa-and-delivery.md) |

## Current status

**Storyboard v0.1 drafted for review**: 22 core cards in `storyboard/storyboard.md`, in Phase 2 order; 11 scored screens / 95 points; 857 narration words (≈ 6.1 minutes, within ±15% of the Phase 3 ~7-minute estimate). All 22 embedded screen JSON blocks validate against the edumints `core.project.Screen` model. Narration lints against the draft screen plan: **0 errors, 0 warnings**; transient visual-plan lint: **0 errors, 0 warnings**. `lint_course` reports one documented H3 advisory (`scored_over_objectives`): this is an intentional practice-rich 11-check design across five objectives, with every scored screen explicitly mapped; strict blockers: **0**. No `visual-plan.json` or audio export is committed yet; those follow policy confirmation and the SME approval gate. Optional `qsr-060` is deferred and excluded from the 22-screen / 95-point baseline.

**Still blocked on Phase 0 / program decisions**: B1 transcript listen; B3 IPSG wording; B4 identifiers; B5 falls band; B6 risk-matrix bands; B7 response terms; B8 incident definitions / just culture; B9 reporting window/channel; B10 hand-hygiene wording; B11 FOCUS-PDCA terms; D7 video route; D8 incident-reporting-window consistency; D9 LMS/privacy deployment context; D10 shared voice route; and new `NEW-01` poll-storage/privacy confirmation. Affected card copy is marked `⚠ PENDING` and must not be treated as approved policy.

**Technical integration note**: the inspected edumints `BrandVoice.formality` schema rejects the unchanged `brand-kit.json` value `conversational-professional` (it accepts `formal`, `neutral` or `conversational`). Visual lint used an in-memory `conversational` mapping only; resolve the adapter/schema mapping before calling `brand_to_theme` for a production build.
