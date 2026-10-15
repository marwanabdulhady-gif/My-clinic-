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
| Draft SCORM (v0.1) | [`build/MC_07_ClinicalGov_v0.1-draft_1.2.zip`](build/MC_07_ClinicalGov_v0.1-draft_1.2.zip) · [`preview.html`](build/preview.html) · `lint_course` 0 errors · `validate_package` ok (structural) · [`draft-builds.md`](../00_program/draft-builds.md) |

## Design idea in one paragraph

The source is a 9-minute narrated video (NotebookLM-style, watermarked) with five parts: the quality standard, the six International Patient Safety Goals, risk management, the incident iceberg, and incident reporting. The package is designed to rebuild the content natively with new visuals and narration, without reusing source frames or audio. Learners practise sorting Structure/Process/Outcome examples, ordering FOCUS-PDCA, identifying the right patient when two share a name, matching practices to the six goals, scoring a risk and choosing a response, classifying events, and reporting a near miss at the end of a shift. D7 remains open; the optional source-video reuse route is not included in the baseline. A new in-house "speak up" message is also optional and requires approval.

## Files

| Phase | File |
|---|---|
| 0 — Source lock | [phase-0-source-lock.md](phase-0-source-lock.md) |
| 1 — Action map & objectives | [phase-1-action-map.md](phase-1-action-map.md) |
| 2a — Screen list | [phase-2-storyboard.md](phase-2-storyboard.md) |
| 2b — Storyboard pack | [storyboard/storyboard.md](storyboard/storyboard.md) — **v0.2; 22 core screens, pending SME / Phase 0 review** · [visual board](storyboard/screen-visuals.html) · [narration script](storyboard/narration-script.json) · [voice talent](storyboard/voice_talent.md) · [asset register](storyboard/asset-register.md) · [lint report](storyboard/lint-report.json) |
| 3 — Narration & assets | [phase-3-narration-and-assets.md](phase-3-narration-and-assets.md) |
| 4 — Build | [phase-4-build.md](phase-4-build.md) |
| 5 — QA & delivery | [phase-5-qa-and-delivery.md](phase-5-qa-and-delivery.md) |

## Current status

**Storyboard v0.2 ready for SME review** (2026-10-14): the 22 hand-written v0.1 cards are kept (same ids, order, types, node ids; 11 scored screens / 95 points) and now use the programme companions exactly as Phase 2/3 place them — lead host **Noor** (visible on `qsr-000`, `qsr-002`, `qsr-021`, `qsr-051`, `qsr-092`) and co-host **Dr. Omar** (`qsr-031` risk example, `qsr-040` iceberg tip, `qsr-092` two-voice close), with the shared `char-noor-*` / `char-omar-*` art only. Narration is speaker-tagged: 23 lines (20 Noor, 3 Omar) on 22 screens, 840 words ≈ 6.0 minutes at 140 wpm (Phase 3 estimate ~7 min). The pack adds `visual-plan.json`, `narration-script.json`, `audio-script-export.json`, `voice_talent.md`, `screen-visuals.html`, `asset-register.md`, `lint-report.json` and draft native SVGs for `qsr-img-spo`, `qsr-img-matrix` (bands pending B6) and `qsr-img-iceberg` (terms pending B8). Server lint (edumints `core.playbook` @ 4bbf459): visual plan **0 errors / 0 warnings**, narration **0 / 0**; all 22 build blocks validate against `core.project.Screen`. Still to make: avatar crops `char-noor-avatar-concern`, `char-noor-avatar-happy`, `char-omar-avatar-happy`. Optional `qsr-060` stays deferred.

**Still blocked on Phase 0 / program decisions**: B1 transcript listen; B3 IPSG wording; B4 identifiers; B5 falls band; B6 risk-matrix bands; B7 response terms; B8 incident definitions / just culture; B9 reporting window/channel; B10 hand-hygiene wording; B11 FOCUS-PDCA terms; D7 video route; D8 incident-reporting-window consistency; D9 LMS/privacy deployment context; D10 shared voice route; and new `NEW-01` poll-storage/privacy confirmation. Affected card copy is marked `⚠ PENDING` and must not be treated as approved policy.

**Technical integration note**: the inspected edumints `BrandVoice.formality` schema rejects the unchanged `brand-kit.json` value `conversational-professional` (it accepts `formal`, `neutral` or `conversational`). The v0.2 lint uses the programme adapter `00_program/brand/brand-kit.edumints.json` (formality `conversational`) and leaves the official `brand-kit.json` unchanged; resolve the adapter/schema mapping before calling `brand_to_theme` for a production build.
