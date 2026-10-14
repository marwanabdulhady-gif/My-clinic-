# Phase 3 — Narration & assets (03 Welcome On Board)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 0. Status: narration script drafted

The narration for all 36 screens is written and lives in
[`storyboard/storyboard.md`](storyboard/storyboard.md) (§5 of each card). The machine-readable
outputs below are generated from those cards, so the storyboard stays the single source of truth.

| File | What it is |
|---|---|
| [`storyboard/visual-plan.json`](storyboard/visual-plan.json) | `VisualPlan` — 36 screens with brand roles, layouts `L1`–`L6`, imagery, `on_screen_text`, `cue_targets`. `lint_visual_plan(plan, brand)` → **0 errors, 0 warnings**. |
| [`storyboard/narration-script.json`](storyboard/narration-script.json) | `NarrationScript` — 39 speaker-tagged segments for 36 screens (`part` = `omar` / `noor` / `omar-1` / `noor-1` / `omar-tip`) with `on_screen_text`, `target_sec` and tone, plus the module lexicon (incl. Noor, Omar). Input to `lint_narration_script`. |
| [`storyboard/audio-script-export.json`](storyboard/audio-script-export.json) | Output of `export_audio_script`: per line `tts_text` (lexicon applied, speaker label removed), `ssml`, `narration_text` (captions, speaker kept), `speaker`, per-line `filename`, per-screen `screen_file`, `est_sec` and estimated cue times. |
| [`storyboard/voice_talent.md`](storyboard/voice_talent.md) | Voice-over tables for the two voices (Dr. Omar, Noor) and the two-voice join instructions; provider pending D10. |
| [`storyboard/asset-register.md`](storyboard/asset-register.md) · [`storyboard/screen-visuals.html`](storyboard/screen-visuals.html) · [`storyboard/lint-report.json`](storyboard/lint-report.json) | v0.2 review-pack files: asset hand-off (shared companion assets, brand assets, planned module assets), branded screen review board with companion previews, and the planning lint report. |

`lint_visual_plan(plan, brand)` result: **0 errors, 0 warnings** (36 screens).
`lint_narration_script(script, plan)` result (v0.2): **0 errors, 0 warnings** (39 segments, 1,628 words excluding speaker labels, ≈ 12 min at 140 wpm; the lint's own estimate, which counts each label as a word, is 738 s ≈ 12.3 min).

**Reference audio (v0.1, superseded — single voice, made before the companions):** [`storyboard/audio/`](storyboard/audio/) — 10 clips, one per section, ~5 min,
generated from the `tts_text` of the export (lexicon applied, so it's a real test of the
pronunciations). See [`storyboard/audio/README.md`](storyboard/audio/README.md) for what to listen
for. Voice route is still open (program **D10**) — this is a reference read, not the shipping audio.

Planning-stage quality checks: `lint_visual_plan(plan, brand)` and `lint_narration_script(script, plan)` both pass with **0 errors, 0 warnings**. A draft authoring plan assembled from the storyboard, narration and visual plan was checked with `lint_authoring_plan(stage="planning")` → **0 errors, 0 warnings**; no persistent `authoring-plan.json` has been saved yet.

Still to do in this phase: the remaining 26 optional audio clips. Then stop for human approval before production.

## 1. Voice

This module is the learner's first contact with My Clinic. Option to use a **human voice** (or a short welcome video from the CEO/HR head, recorded in-house) for `hr-000`/`hr-001` only; TTS for the rest. Decide in Phase 0 (program D10).

**Reference voice (2026-10-14):** an English (GB) feminine voice, warm and coaching, ~140 wpm. Used only for the reference read in `storyboard/audio/`. It is **not** the production provider choice — that stays open until **D10** closes. When it closes, record the provider and voice id here, because the same voice must be used across all eight packages.

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Omar** (narrates every narrated screen unless listed below). **Co-host: Noor**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| hr-000 | Both | `char-duo-welcome` | L1 duo, bottom-right (mockup 07) | Omar + Noor | "Meet your guides": both introduce themselves (first course in the learning path) |
| hr-001 | Omar | `char-omar-explaining` | L3 right column, half-body | Omar | First-week story (companions.md §1) |
| hr-002 | Omar | `char-omar-listening` | L3 small, beside the poll | Omar | Invites the icebreaker |
| hr-031 | Noor | `char-noor-avatar-neutral → -concern / -happy` | L5 avatar | Noor | Ethics scenario host (as in the v0.1 storyboard) |
| hr-043 | Omar | `char-omar-thinking` | L3 right column | Omar | Talks through the sick-leave worked example |
| hr-044 | Noor | `char-noor-avatar-neutral` | L5 avatar | Noor | Leave-desk host (as in the v0.1 storyboard) |
| hr-061 | Omar | `char-omar-avatar-neutral + tip card` | L4 feedback avatar / tip after the simulation | Omar | Tip: check the request status before you book travel |
| hr-091 | Omar + Noor | `char-omar-success + char-noor-avatar-happy` | L6 | Omar + Noor | Two-voice close; Noor previews module 07 |

- Visible on 8 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `OMAR:` / `NOOR:`; two-voice screens are split into one segment per line (`part` = `omar-1`, `noor-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.
- **Done in storyboard v0.2 (2026-10-14):** every line in `storyboard/` is prefixed `OMAR:` / `NOOR:` per the table above (Dr. Omar 35 lines, Noor 4); the `hr-000` duo introduction and the `hr-091` two-voice close are split into `omar-1` / `noor-1` parts; Omar's first-week story is on `hr-001`; the `hr-061` tip has its own `omar-tip` line; the old module-only mentor art is replaced by the shared `char-noor-*` / `char-omar-*` asset ids; and `narration-script.json`, `audio-script-export.json`, `voice_talent.md`, `visual-plan.json`, `asset-register.md`, `screen-visuals.html` and `lint-report.json` were regenerated (lint 0 errors, 0 warnings). The v0.1 reference clips in `storyboard/audio/` are single-voice and superseded.

## 2. Narration outline

| Screen | Speaker | Sec | Narration intent |
|---|---|---|---|
| hr-000 | Omar + Noor | 15 | Warm welcome; what the next 45 minutes give you. |
| hr-001 | Omar | 35 | Why My Clinic exists, in plain words; a short honest line: "Everyone here remembers their own first week — and how much there was to take in." |
| hr-002 | Omar | 10 | Invite the icebreaker; no right answer. |
| hr-010 | Omar | 40 | Values are behaviours, not posters; one example for each. |
| hr-011 | Omar | 8 | Set up. |
| hr-012 | Omar | 45 | The 7Cs explain where the company is going; find the pillar your role touches most. |
| hr-013 | Omar | 8 | Set up. |
| hr-014 | Omar | 20 | Who we serve, including people who are healthy today. |
| hr-020 | Omar | 30 | From one clinic in 2017 to a network; what each step added. |
| hr-021 | Omar | 15 | Explore the branches; you'll hear their codes (J1, J2…) every day. |
| hr-022 | Omar | 20 | The leadership team and what each role looks after. |
| hr-023 | Omar | 15 | Recognition we're proud of — and that we have to keep earning. |
| hr-030 | Omar | 35 | The four ethics values; when in doubt, ask and report within 24 hours. |
| hr-031 | Noor | 15 | Set up the supplier evaluation. |
| hr-032 / 033 | Omar | 8 each | Set up. |
| hr-040 | Omar | 25 | Where help lives: your HR mailbox, Oracle, and the quick-reference PDF. |
| hr-041 | Omar | 40 | A quick tour of leave types; you'll practise the ones people ask about most. |
| hr-042 | Omar | 8 | Set up. |
| hr-043 | Omar | 40 | Talk through the sick-leave example step by step. |
| hr-044 | Noor | 15 | Set up the leave desk: four colleagues, four questions. |
| hr-045 | Omar | 10 | Set up adaptive practice: it stops early if you've got it. |
| hr-050 | Omar | 30 | What GOSI is and why the deduction protects you. |
| hr-051 | Omar | 30 | Work through 585 riyals aloud. |
| hr-052 | Omar | 8 | Set up. |
| hr-053 | Omar | 35 | Hourly rate first, then the multiplier. |
| hr-054 | Omar | 8 | Set up. |
| hr-060 | Omar | 10 | Set up: one system per task. |
| hr-061 | Omar | 15 | Set up the simulation. |
| hr-062 | Omar | 8 | Set up. |
| hr-070 | Omar | 25 | ID card care; the benefits you can use from day one. |
| hr-071 | Omar | 8 | Set up. |
| hr-080 | Omar | 25 | Contracts on Qiwa; if you ever leave, how to do it well. |
| hr-081 | Omar | 8 | Set up. |
| hr-090 | Omar | 12 | Read your results. |
| hr-091 | Omar + Noor | 25 | What you can now do; please complete the onboarding survey. |

Estimated audio: ~13 minutes.

## 3. Lexicon used

GOSI, SCFHS, Mumaris, Qiwa, HRMS, Oracle ("OR-uh-kul"), SAR, HHC, MCJ1 ("M-C-J-one"), MCJ2, PRC ("P-R-C"), J1–J4 ("J-one"…), D1, R1, EOS ("end of service"), IELTS ("eye-elts"), TOEFL ("toe-full"), CBAHI, JCI ("J-C-I").

## 4. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| hr-img-hero | photo | hr-001 | Real My Clinic team or clinic photo (consented) | own | "My Clinic team at the J1 reception." |
| hr-img-values-icons | SVG ×4 | hr-010 | Line icons for the four values | own | decorative |
| hr-img-7c-icons | SVG ×7 | hr-012 | Line icons (headset, syringe, gears, handshake, stethoscope, heart-hands, coins) redrawn from slide 10 | own | decorative |
| hr-img-map | SVG | hr-021 | Minimal map of western KSA and Riyadh with 7 pins | own | "Map of My Clinic branches in Jeddah, Rabigh and Riyadh." |
| hr-img-branches | photos ×7 | hr-021 (in region text) | Branch photos from slides 14–15 if rights confirmed | local (after Phase 0) | per branch |
| hr-img-leaders | photos ×4 | hr-022 | Consented portraits | local (consent on file) | "<name>, <role>." |
| hr-img-oracle-1..5 | screenshots | hr-061 | Test-account screenshots, 1920×1080, no real names (B8) | own | per step, e.g. "Oracle Time and Absences page." |
| hr-img-dress | illustrations ×3 | hr-071 feedback | Front office, medical team, back office outfits (replaces slide 58 art) | ai-generated | per role |
| hr-pdf-quickref | PDF | hr-040, hr-091 | **HR Quick Reference** (2 pages): leave tables, GOSI, overtime, contacts — written by HR from confirmed policy | own | n/a |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Noor, the safety liaison, explaining." |
| hr-aud-* | audio | narrated screens | TTS (or human for hr-000/001) | ai-generated / own | transcript |

## 5. Activity plans

| Activity | Objective | Rules | Success | Failure | Accessibility |
|---|---|---|---|---|---|
| hr-031 ethics | hr-o2 | 3 nodes | ≥ 2 best | replay | buttons |
| hr-044 leave desk | hr-o3 | 4 nodes, one per colleague | ≥ 3 | replay | buttons; rule text in feedback |
| hr-045 adaptive | hr-o3 | Elo, 12-item bank, max 6, stop when mastery reached | pass ratio 0.6 | items keep coming up to max | MCQ radio buttons |
| hr-061 Oracle sim | hr-o5 | 5 click steps, `rect` regions, hint per step | all steps | retry step | each step has a text instruction and alt text; offer a text-only "steps list" in feedback |

## 6. Approval request

HR approves: storyboard, all numbers against the verified facts register, the leave-desk and ethics scripts, the adaptive item bank (all 12 items + feedback), the Quick Reference PDF, and the Oracle screenshots (no real data). Comms approves leaders, awards and branch screens.
