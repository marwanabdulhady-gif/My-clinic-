# Programme status, gaps and next steps

![My Clinic logo](brand/logo-preview.png)

> Status as at **2026-10-19, second pass**: all 102 kick-off decisions have a researched working assumption ([`kickoff-assumed-answers.md`](kickoff-assumed-answers.md)), storyboards re-checked against Rev01 ([`storyboard-proposal-check.md`](storyboard-proposal-check.md)), role personalisation and extra interactivity added as an unscored layer in all eight packages ([`personalisation-and-interactivity-plan.md`](personalisation-and-interactivity-plan.md)), and media job lists for the image/audio/video agents ([`media-jobs-summary.md`](media-jobs-summary.md)). First pass the same day: Oracle Learning sample built and harness-tested; all packages SCORM 1.2; brand weave on every screen). Earlier: **2026-10-15** (draft SCORM builds for all eight packages added; full-size companion art imported). Checked against the files in this repository: every module folder, every storyboard pack, the review register and the proposal (`../../proposal/MyClinic_Induction_eLearning_Proposal_e2026-MC01_Rev01.docx`). This report records **production progress only**. No policy, clinical, payer or EHR content is approved yet.

---

## 1. Where every module stands

✅ done (draft ready for review) · 🟡 partly done · ⬜ not started · 🔒 waiting on My Clinic

| Module | Ph 0 source lock | Ph 1 action map | Ph 2a screen list | Ph 2b storyboard cards | Narration script + visual plan | Visual board + asset register | Companions in storyboard | Planning lint | Ph 3 voice and media | Ph 4 build | Ph 5 QA / LMS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 FMS | 🔒 B1–B10, D1 D2 D11 D14 | ✅ | ✅ 54 | ✅ v0.2 · 54 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | 🟡 v0.1-draft built · 0 lint errors · [2.3 MB](draft-builds.md) | ⬜ LMS test |
| 02 Safety Lab | 🔒 B1–B9, D1 D2 D11 D12 | ✅ | ✅ 26 | ✅ v0.2 · 26 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | 🟡 v0.1-draft built · 0 lint errors · [3.2 MB](draft-builds.md) | ⬜ LMS test |
| 03 Welcome On Board | 🔒 B1–B14, D3 D5 D8 | ✅ | ✅ 36 | ✅ v0.2 · 36 cards | ✅ | ✅ | ✅ Omar lead, Noor co-host | ✅ clean | 🟡 old single-voice reference clips only | 🟡 v0.1-draft built · 0 lint errors · [1.2 MB](draft-builds.md) | ⬜ LMS test |
| 04 Who Does What | 🔒 B1–B7, D3 D5 D11 | ✅ | ✅ 13 | ✅ v0.2 · 13 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | 🟡 v0.1-draft built · 0 lint errors · [2.5 MB](draft-builds.md) | ⬜ LMS test |
| 05 RCM Part A | 🔒 B1–B10, D4 D11 | ✅ | ✅ 21 | ✅ v0.2 · 21 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | 🟡 v0.1-draft built · 0 lint errors · [0.5 MB](draft-builds.md) | ⬜ LMS test |
| 06 RCM Part B | 🔒 B1–B9, D4 D5 D11 | ✅ | ✅ 15 | ✅ v0.2 · 15 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | 🟡 v0.1-draft built · 0 lint errors · [0.7 MB](draft-builds.md) | ⬜ LMS test |
| 07 Clinical Governance | 🔒 B1–B11, D7–D10, NEW-01 | ✅ | ✅ 22 (+1 optional) | ✅ v0.2 · 22 cards | ✅ | ✅ (+3 native SVGs) | ✅ Noor lead, Omar co-host | ✅ clean | ⬜ | 🟡 v0.1-draft built · 0 lint errors · [0.8 MB](draft-builds.md) | ⬜ LMS test |
| 08 EHR | 🔒 B1–B10, D6 D11 | ✅ | ✅ 20 (+1 optional) | ✅ v0.2 · 20 cards | ✅ | ✅ | ✅ | ✅ clean | 🔒 test-patient captures | 🟡 v0.1-draft built · 0 lint errors · [0.7 MB](draft-builds.md) | ⬜ LMS test |

**Programme level**

| Item | Status |
|---|---|
| Plans in phases for all 8 packages (Phases 0–5) | ✅ |
| Brand identity, logo files, layouts L1–L6, screen mockups | ✅ draft · 🔒 Marketing confirmation (D11) |
| Companions Noor and Dr. Omar: bible, 8 poses each, avatars, placement rules | ✅ full-size transparent PNGs imported into `characters/assets/` (2026-10-15) |
| Storyboard template, screen-type guide, examples, review checklist | ✅ |
| Client-review Word pack (all 8, branded header/footer) + review register (52 build-detail questions across all 8 packs) | ✅ v0.2 |
| **SCORM structure** (programme + per module) | ✅ new: [`scorm-structure.md`](scorm-structure.md) and `<module>/scorm-structure.md` |
| Proposal (6 courses, USD 9,000) | ✅ Rev01 (narration ~60 min, 26 scenarios, guide characters) · see §3 |
| Cross-module decisions D1–D14 | 🔒 all 14 open |
| Voices (D10), LMS + SCORM version (D9) | 🔒 open |
| Pre-kickoff current-content slide drafting | 🟡 [Batch 1: 03/07, 58 slides / 61 actual browser captures](draft-slide-production.md); required plans/templates and mockup geometry; later draft batches queued |
| SCORM packages | 🟡 **v0.1-draft for all eight** (2026-10-15): real edumints compiler, `lint_course` 0 errors, `validate_package` ok — manifest **XSD-validated** (0 errors, 0 warnings; [xsd-validation.md](xsd-validation.md)). Pending decisions shown as `⚠ Draft — pending`, unmade media as PENDING cards, captions only. [`draft-builds.md`](draft-builds.md) |
| LMS / SCORM Cloud test | 🟡 Oracle sample built and passed the local SCORM 1.2/2004 harness (resume, pass at 100%); [test guide](../00_sample-oracle-pilot/oracle-learning-test-guide.md) ready to send; real Oracle test pending |

**In one line:** all eight packages exist as compiled, validated **draft SCORM packages** (207 core screens, 95 scored) with the full-size companion art. They cannot become release builds until My Clinic closes the Phase 0 items and D9–D11, the narration is rewritten and voiced, and the pending media is produced. Pre-kickoff browser drafts use current content with those dependencies visibly pending; they do not close the production gates.

---

## 2. Gaps found in this check, and what to do

| # | Gap | Where | Fix | Who |
|---|---|---|---|---|
| G1 | ~~03 storyboard predates the companions.~~ **Done:** v0.2 with shared `char-*` art, `OMAR:`/`NOOR:` tags, two-voice split on `hr-000` and `hr-091`, full pack and clean lint. | `03_hr-employee-induction/storyboard/` | — | Done |
| G2 | ~~07 storyboard pack is incomplete.~~ **Done:** v0.2 with Omar on `qsr-031`, `qsr-040` and `qsr-092`, full pack, 3 native SVG diagrams and clean lint. SME to confirm: Noor beside the unscored poll on `qsr-002` (companions.md says no companion over a question), risk-matrix band names (B6), and the closing quote (B1). | `07_quality-safety-and-risk/storyboard/` | Confirm the three points in Phase 0 review | SMEs |
| G3 | ~~Two-voice screens were one recording, and TTS read the speaker label aloud.~~ **Done:** all eight packs now carry one segment per spoken line (`part` = `omar-1` / `noor-1`), `tts_text`/`ssml` without labels, one shared companion voice block, and one export schema (`tools/audio_export.py`, used by the generator and by `tools/normalise_narration.py` for 03/07). **Still open:** the voice ids themselves — `voice_id: null` until **D10** closes. | all `storyboard/narration-script.json` and `audio-script-export.json` | Close D10, then record provider + voice ids in `narration-and-lexicon.md` §1 and each `voice` block | Course owner → agent |
| G4 | **Thin objective evidence.** 14 objectives are assessed by one scored screen only, so the LMS objective result depends on one answer. | see each `scorm-structure.md` §5 | Add a second short check where the objective matters for compliance (01 `hs1-o6`, `hs1-o7`; 07 `qsr-o5`; 08 `ehr-o2`), or accept at SME sign-off. Capstones (`hs1-o10`, `rcma-o5`) are fine as one big case. | SMEs + L&D |
| G5 | **52 scored screens still need SME build detail** (answers, feedback, replay rules, typed-answer variants). The register now covers all eight packs, not six. | [`storyboard-review-register.md`](storyboard-review-register.md) | Close row by row with the named SME, then update the cards. | SMEs + L&D |
| G6 | ~~Companion art not in the repo at full size.~~ **Done:** the owner delivered the 18 full-size Canva originals on 2026-10-15 (verified 1:1 against the approved previews before renaming). `tools/import_companion_art.py` keyed their white backgrounds to transparency into `characters/assets/<asset id>.png` (originals kept in `characters/assets/originals/`) and replaced the interim avatar crops with full-size derived crops — now four, adding `char-omar-avatar-concern.png` for L4 feedback. | `characters/` | — | Done |
| G7 | **Master timeline was out of step with the proposal** (8 weeks vs the proposal's 9–10 weeks). | `../README.md` §3 | Fixed in this pass: the README timeline now follows the proposal's phases. | Done |
| G8 | **No repeatable evidence for assets, templates and logo placement.** Reviews relied on memory of what exists. | `00_program/` | Added `tools/audit_assets.py` → [`asset-template-audit.md`](asset-template-audit.md) + `asset-audit.json`: brand pixels/alpha, mockups vs L1–L6, companion coverage, referenced-vs-on-disk module assets, SVG validity, card template completeness, logo in every board/Word doc/Markdown cover, internal link resolution, TTS label leaks. Clean on 2026-10-14. | Done (rerun after changes) |
| G9 | **Planning lint could not be rerun locally** (the edumints MCP server is unreachable here), so `lint-report.json` files went stale after edits. | all `storyboard/lint-report.json` | Added `tools/lint_planning.py`, a deterministic local port of `lint_visual_plan` / `lint_narration_script` (upstream rev `4bbf4591`); all eight reports regenerated and clean. Each report says it is a local port and that the server lint must be rerun before Phase 4. | Done (rerun after changes) |
| G10 | **Planning-reference fix implemented; final media still pending.** Restored Phase 3 assets to the 01/02/08 cards, visual plans, asset registers and planned structures. Full **6-scene** Code Red drill and **31 unique EHR shots** now have individual placements, briefs, draft alt text and production gates. | `01_…/storyboard/`, `02_…/storyboard/`, `08_…/storyboard/` | See [`g10-visual-restoration.md`](g10-visual-restoration.md) and the drill/capture manifests. Safety/EHR/DPO approval, illustration/photo production and captures are still required. Corrected inventory remains 21–22 new stills, 4 client photos, 5 + 31 screenshots, 0 required videos. | Storyboard agent / Safety / IT / DPO |
| G11 | **Generic filler narration** on many question and simulation screens in the six generated packs (01, 02, 04, 05, 06, 08), e.g. "The next choice asks you to apply the rule…". It is now visible as captions in the draft packages. | `<module>/storyboard/narration-script.json` | Rewrite per screen (lead companion voice, situation set-up, never the answer), regenerate audio export, rebuild. Must be done before any voice work (D10). | Storyboard agent + L&D |
| G12 | **Explore hotspots broken in the edumints player** (`bindHotspot` returns before positioning regions in explore mode). Affects every clickable picture. | edumints-scorm-mcp `components/templates.py` | Worked around here (`build_course_spec.py` writes region positions as CSS). Fix upstream and remove the workaround. | L2S (edumints repo) |
| G13 | **Content gap `hs2-031`**: scored question on evacuation tools that no earlier screen teaches (`unbound_scored_question`). | `02_…` storyboard | Add a short teaching screen before it or move the question after the drill debrief; Safety SME to confirm. | Storyboard agent + Safety SME |
| G14 | **Two SCORM build routes.** `build_scorm_packages.py` (03/07 pilot, no lint, no skin) duplicates the canonical `build_course_spec.py` + `edumints_build.py`. | `tools/` | Marked superseded in `scorm-package-builds.md`; use only the canonical route. | Done (doc) |
| G15 | **XSD validation not run** (schemas unreachable offline). | build environment | **XSD run 2026-10-15: all eight manifests validate with 0 errors, 0 warnings** ([xsd-validation.md](xsd-validation.md)); rerun with the authentic SCORM 1.2 root schema before release, then SCORM Cloud. | Half done |
| G16 | **Schema limits** recorded in `screens.json` notes: no per-card feedback on drag/sort, no per-choice companion reaction, no media on mcq/matching/escape-room, one hint ladder per game. | edumints schema | Accept for v1.0 or request schema additions upstream; SMEs see the workaround wording at review. | L2S |
| G17 | **NFPA 704 diagrams were drawn wrong** (rotated quadrants, numbers on the wrong colours) in `hs1-img-nfpa-blank`, `hs1-img-nfpa-301w`, `hs2-img-nfpa-230`. | 01/02 storyboard assets | **Fixed** 2026-10-15: redrawn to the standard layout; the blank no longer prints the answers. | Done |
| G18 | **Percent shown Turkish-style** ("%75") on summary and results screens in the edumints player. | edumints `components/templates.py` | Patched at build time in every package (`edumints_build.py`, `player_patches: 2`); fix upstream with G12. | L2S (edumints repo) |
| G19 | **LMS target was unknown (D9).** My Clinic uses Oracle Applications Cloud → Oracle Learning, which documents SCORM 1.2 and 2004 Ed. 2–3 only. | all packages | **Applied:** all eight rebuilt as SCORM 1.2; sample package + test guide ready (`00_sample-oracle-pilot/`). Closes when My Clinic's LMS team returns the sample test. | L2S + My Clinic LMS admin |
| G20 | **Package 04 had no results-by-objective screen** although Rev01 promises it for every course. | `04_…` | **Fixed** in the personalisation layer: `ops-089` (unscored `results_breakdown`) before the close. | Done |
| G21 | **Job-aid links render broken markup** while the PDF does not exist (`hr-091` showed `" rel="noopener…`). | `build_course_spec.py` | **Fixed**: an `{{asset:…}}` link to a missing job aid becomes its text plus "⚠ Draft — pending". The five job-aid PDFs and the QTI 2.1 export (Rev01 deliverables) are still to make. | Done (render) · PDFs open |
| G22 | **Client decks contradict current public rules** in at least ten places (GOSI rate for post-July-2024 Saudis, radiation limit, laser classes, CCHI → CHI, EBP date, JCI/CBAHI claims, branch names, widow leave, 24-h incident rule, 2222 authority). | 01, 03, 05, 06, 07 | Raised first on the kick-off agenda ([`kickoff-assumed-answers.md`](kickoff-assumed-answers.md) "Where the research disagrees"). Drafts keep the "⚠ Draft — pending" markers until the owner decides. | My Clinic owners |
| G23 | **No Arabic yet.** Rev01 promises bilingual emergency-code cards (`hs1-301`, `hs2-020`); they are English only pending D2. | 01, 02 | Add the Arabic names once the facility code poster is supplied (D2); RTL plan in `brand-and-theme.md`. | L2S after D2 |
| G24 | **Resume-data figure disagrees**: `scorm-structure.md` says 749 bytes worst case for 01, `scorm-base-audit.json` 2,448. The personalisation layer adds ~100 bytes (two short variables + choice ids). | 01 | Measure on the built 01 package in the LMS harness and record one number; both are under the 4,096 SCORM 1.2 limit. | L2S |
| G25 | **Results screen shows "Total 100 %"** next to 0 % objectives when only some questions were answered (seen on `ops-089`, same player code as every results screen). | edumints player | Check in the harness with a full attempt; report upstream with G12/G18 if it persists. | L2S (edumints repo) |
| G26 | **First AI image batch (PR #53) needed fixes before use.** Of 108 new files, 35 are used (5 of them corrected), 2 were redrawn and 71 rejected. | 01–08 | **Done 2026-10-20:** fitted into the modules with hotspot maps for `hs1-410`, `hs1-701`, `qsr-020`; `hs2-img-drill-4` redrawn (was a duplicate assembly point; node 4 is Extinguish); `hs1-img-8plans` redrawn on the `hs1-102` grid; red emergency socket added to the treatment room; falls icon on the six-goal tile; chemical/biological kit colours swapped to match `hs2-051`; designer notes stripped from the SVGs; images re-encoded as JPEG (33 MB → 2.3 MB). Rejected: 36 placeholder "screenshots"/PDF cards (they hid real gates), 4 AI leader portraits (D5), 9 GHS sheets and unused SVGs with baked-in notes. **Canva round (2026-10-20):** drill 4 (Extinguish), the biological kit with its biohazard symbol and the extinguisher (pin, gauge, label, instructions panel, inspection tag) regenerated in Canva and fitted; `hs2-040` hotspots mapped. Still to do: SME review of every picture. | Done · SME review open |
| G27 | **Courses felt flat; simulations had no screens.** | all | **Done 2026-10-20:** gamification system on all eight (challenge brief, missions in the menu, XP and four ranks in the header, debrief; `tools/gamify.py`, D18); 36 training wireframes (`tools/build_wireframes.py`) make the Oracle and EHR simulations playable with distractors, each labelled "training wireframe — not the live system", until the test-environment captures arrive (jobs stay open); 8 Canva challenge illustrations fitted on the mission briefs (`<prefix>-img-challenge`). **0 placeholder cards left in any package.** | Done · captures and SME review open |
| G28 | **Portfolio upgrades and video production.** | all | **Done 2026-10-20:** the seven upgrades from `inspiration-portfolio-review.md` (outcome meter, Ask Noor / Ask Dr. Omar on 12 decisions, consequence-first feedback, 02 day-at-the-clinic timeline, revisit map on results, drag-to-store practice in 01/02, replies from the other side in 04/06). See `gamification-plan.md`. Video production restructured from the owner's playbook (`video-playbook-review.md`): `elearning-course/video/` with shared scripts (`resolve_cues.py`, `srt_to_vtt.py`, `delivery_check.py`, `encode_scorm.sh`, all tested), templates, brand tokens and a 44-step agent procedure; the clip delivery paths are fixed in `media-video-plan.json`. Still open: kit scripts from the raw playbook (`transcribe.py`, `build_timeline.py`, `qa_check.py`…), the HyperFrames components, the playbook kit licence, and D17. | Done · kit scripts and D17 open |
| G29 | **Own SCORM player; edumints retired (owner decision 2026-10-20).** The owner asked for screens that are not tied to edumints: compatible with Oracle only, minimal, interactive, animated, with no outline boxes around text. | all + sample | **Done 2026-10-20:** `tools/player/` (engine + design system, all 27 screen types, SCORM 1.2 for Oracle) and `tools/build_package.py` (zip, manifest, validation, `build-report.json`). `tools/check_packages.py` plays all nine in Chromium on a mock LMS (right → passed, wrong → failed, resume). Found and fixed on the way: overlapping hotspot markers (the whole object is now the click target), and drop boxes that picked up items. Open: `qsr-032` cannot be answered until B6 closes; module 08 scores 72 when every multiple choice is wrong, because its 7 simulations always complete (pass mark 80, so it still fails); the real Oracle tenant test (D9). | Done · D9 open |
| G30 | **Video production plan (owner, 2026-10-20).** Videos now, male voice, voice interactions, a visual and motion plan per scene. | 01–08 | **Done 2026-10-20:** `video/PRODUCTION-PLAN.md`, generated from `video/_shared/plan/clips.json` by `scaffold_clips.py`. It covers 9 clips and 43 scenes, Dr. Omar as the only voice, one unscored voice interaction per clip, and every motion cue checked against the spoken words. Drafts are in each `video/<clip-id>/data/`. AGENT-TASKS T7 is open. Owner questions: hs2 briefing placement (before hs2-030), the qsr-060 slot is missing, NPHIES is unsourced, HR timings are unsourced, and D17 value-add vs change request. Player support for interactive video (V0) is still to build. | Plan done · production open |

---

## 3. Proposal vs plans and storyboards

Checked every number in the proposal against the storyboard build blocks, narration scripts and Phase 5 test lists.

| Figure | Proposal | Plans / storyboards | Match |
|---|---|---|---|
| Courses / packages | 6 courses / 8 packages | 8 package folders; HSE = 01 + 02, RCM = 05 + 06 | ✅ |
| Screens | 80 · 36 · 13 · 36 · 22 · 20 = **207** | 54+26 · 36 · 13 · 21+15 · 22 · 20 = **207** | ✅ |
| Scored activities | 37 · 15 · 4 · 17 · 11 · 11 = **95** | 24+13 · 15 · 4 · 10+7 · 11 · 11 = **95** | ✅ |
| Pass marks | HSE 80 · HR 70 · Ops 70 · RCM 80 · Quality 80 · IT 80 | same in Phase 4 and storyboards | ✅ |
| Seat time | ~90 · 45 · 15 · 45 · 25 · 25 min (~4 h) | 55+33 · 45 · 15 · 25+20 · 25 · 25 | ✅ |
| Test cases | 26 · 12 · 8 · 16 · 9 · 10 = **81** | 14+12 · 12 · 8 · 9+7 · 9 · 10 = **81** | ✅ |
| Scenarios, games, simulations | Rev00: 27 → **Rev01: 8 · 4 · 1 · 4 · 2 · 7 = 26** | 5+3 · 4 · 1 · 2+2 · 2 · 7 = **26** | ✅ Rev01 |
| Narration | Rev00: 27 · 13 · 5 · 13 · 7 · 5 = ~70 min → **Rev01: 23 · 12 · 4 · 11 · 7 · 5 = 62 min** | 16.1+6.5 · 11.7 · 4.4 · 6.3+4.6 · 6.0 · 5.0 = **~61 min** | ✅ Rev01 |
| SCORM version | "1.2 or 2004, to match the LMS" | 1.2 for all eight (Oracle Learning); D9 open until the sample test | ✅ |
| EHR | new test-patient screenshots, original video not used | Phase 0 B2, D6; 7 simulations | ✅ |
| Phases and payment points | Phases 0–5, 9–10 weeks | same phase model in every folder | ✅ (README timeline now aligned) |
| Companions Noor and Dr. Omar, two voices | not in Rev00; **added in Rev01** | in every plan and all 8 storyboards | ✅ Rev01 |

**Verdict:** the proposal matches the plans on every number the client pays for (courses, packages, screens, scored activities, pass marks, test cases, seat time). Three corrections were needed; all three are made in **Rev01** (`../../proposal/MyClinic_Induction_eLearning_Proposal_e2026-MC01_Rev01.docx` / `.pdf`, revision sheet row 01). Rev00 is kept for the record:

1. **Narration:** say "about 60 minutes" (or "up to 70 minutes") instead of "about 70 minutes". The finished scripts total ~61 minutes; promising 70 creates a gap at delivery.
2. **Scenarios:** RCM has 4 scenarios, games and adaptive practice (2 in Part A, 2 in Part B), so the total is 26, not 27. Or add one scenario to RCM Part A to keep 27.
3. **Companions:** add one line under the approach and deliverables: two consistent guide characters (Noor and Dr. Omar) with two narration voices across all courses. It is a visible value-add that the client will see in every storyboard.

Also in Rev01: the proposal now says L2S has prepared full draft storyboards for all 207 screens, not "a storyboard outline".

---

## 4. Improvements made in this pass

1. **SCORM structure added.** [`scorm-structure.md`](scorm-structure.md) covers the LMS curriculum, zip contents, manifest (1.2 and 2004), outline → section → screen model, LMS data and versioning, all taken from the edumints packager. Each module now has `scorm-structure.md`: its package tree, manifest sketch, every section with every screen (type, points, objective, companion, narration), objective evidence and the tracking table.
2. **Generator, not hand-typing.** `tools/build_scorm_structure.py` rebuilds all eight structure files from the storyboards, so they cannot drift. It also flags thin objective evidence and untagged narration.
3. **Phase model updated.** The structure file is part of every module folder and the build pipeline (step 4c).
4. **README timeline aligned** with the proposal phases and weeks.
5. **Status board.** This file replaces guesswork with a module × phase grid.
6. **Two-voice audio fixed everywhere (G3).** One recording segment per spoken line in all eight packs; `tts_text` and `ssml` never contain the speaker label; one shared companion voice block and one export schema, implemented once in `tools/audio_export.py`.
7. **Narration padding de-duplicated.** Generated packs no longer repeat the same coaching sentence inside one screen (01, 02, 04, 05, 06, 08), and two-voice hand-offs vary by screen.
8. **Branded client Word pack.** Every rendering now carries the supplied client logo in the running header of each page, a module-colour cover band, a document-control table (`MC-SB-<nn> v0.2`) and live page numbering; all nine files regenerated from the current v0.2 storyboards.
9. **Interim companion avatars.** `tools/make_companion_avatars.py` derives the three missing avatar crops (`char-noor-avatar-happy/concern`, `char-omar-avatar-happy`) from approved poses and copies the two neutral avatars as transparent PNGs.
10. **Repeatable evidence.** `tools/audit_assets.py` (asset/template/logo/link audit) and `tools/lint_planning.py` (local port of the edumints planning lint) make the two quality gates rerunnable in this workspace; both are clean as at 2026-10-14.
11. **SME register completed.** The build-detail queue now covers all eight packs (52 screen-level questions, was 37 across six).
12. **One decision list instead of nine.** `tools/build_decision_sheet.py` merges the 14 programme decisions (D1–D14), every module B-item, `NEW-01`, the thin-objective choices (G4) and the module 07 poll check into [`decision-sheet.md`](decision-sheet.md) + CSV: **102 open rows**, each with an owner role, a due date and the exact file to write the answer back to. Rows disappear from the sheet as soon as they are closed in the source file, so the count is the live blocker count. [`kickoff-pack.md`](kickoff-pack.md) (`MC-KO-01 v0.1`, rendered to `kickoff-pack.docx`) adds the 90-minute run sheet, the attendee-role→decision map and the same-day write-back procedure.
13. **Agent-ready production handoffs.** Added a researched [`client-context.md`](client-context.md), character-aware [`visual-production-plan.md`](visual-production-plan.md), [`visual-generation-prompts.md`](visual-generation-prompts.md), [`visual-and-motion-agent-brief.md`](visual-and-motion-agent-brief.md), [`narration-production-plan.md`](narration-production-plan.md), [`scenario-design-plan.md`](scenario-design-plan.md) and [`gamification-plan.md`](gamification-plan.md). Added one prefilled production worksheet for each of the eight packages under [`course-templates/`](course-templates/), alongside the existing full storyboard template. The new [`plan-audit.md`](plan-audit.md) records the Rev01 cross-check, local gate results and remaining blockers. These handoffs do not close client decisions or authorize media generation.

14. **Kick-off answers researched (2026-10-19).** All 102 open decisions now carry a working assumption with confidence and sources (47 high, 35 medium, 20 low), merged into [`decision-sheet.md`](decision-sheet.md) / CSV as two new columns. Three new programme decisions D15–D17 (roles, extra screens, videos): **105 open rows**.
15. **Storyboards re-verified against Rev01** by script: 0 drift in ids, types or points across all 207 screens; every named activity present with the promised item counts ([`storyboard-proposal-check.md`](storyboard-proposal-check.md)).
16. **Personalisation and interactivity layer** (`tools/personalise.py`, `<module>/production/personalisation.json`): role picker, role tips, quick checks, predictions replayed at the close, flip-card conversions and the 04 results screen — all unscored, guarded so no point, objective or pass mark can change. All eight rebuilt: 0 lint errors, totals unchanged.
17. **Media job lists for agents** (`tools/build_media_jobs.py` → `<module>/production/media-jobs.json`, roll-up [`media-jobs-summary.md`](media-jobs-summary.md)): 22 AI stills (+1 staged), 39 own SVG/PDF, 44 photos/captures, 218 narration clips (156 still carry generator filler, G11 — rewrite with `tools/narration_rewrite.py`), 9 optional videos — each with prompt or script, target file, gate and acceptance checks. Procedure in [`media-production-runbook.md`](media-production-runbook.md).
18. **Hotspot maps** (`tools/map_hotspots.py`): boxes live beside each picture, a preview overlay checks them by eye, and new pictures can carry extra hotspots. Corridor (`hs1-404`) re-checked, a 9th hotspot added.
19. **Video tooling chosen**: HyperFrames primary, Remotion fallback (paid company licence), FFmpeg encode, WhisperX captions, Rhubarb lip-sync for Noor and Dr. Omar, dotLottie for in-player micro-animation ([`video-tooling.md`](video-tooling.md)).

---

## 5. What happens next (in order)

| Step | Action | Owner | Unblocks |
|---|---|---|---|
| 0 | At the kick-off, walk the ten contradictions first (G22), then confirm or correct the working assumptions row by row; confirm roles (D15), extra screens (D16) and videos (D17) | L2S + My Clinic | everything |
| 1 | Book the Phase 0 kick-off for **2026-10-19 (proposed)** and send [`kickoff-pack.docx`](kickoff-pack.docx) with the invite, plus the client-review Word pack, [`decision-sheet.csv`](decision-sheet.csv) and proposal Rev01 | L2S | everything |
| 1b | Write every kick-off outcome into the file named in its **Write back to** column the same day: **28 tier-1 rows by 2026-10-22**, D9/D10/D11 by 2026-10-26, the **71 tier-2 rows by 2026-10-30**; rerun `build_decision_sheet.py` + `export_kickoff_docx.py` after each write-back so closed rows drop out | My Clinic owners + L2S | C2–C9 |
| 2 | ~~Issue proposal Rev01 (§3 fixes)~~ ✅ done — send Rev01 with the storyboard pack as evidence | L2S | contract |
| 3 | ~~Retrofit 03 and complete 07 to v0.2 (G1, G2)~~ ✅ done; ~~split the 7 two-voice segments (G3)~~ ✅ done for all eight packs | Storyboard agent | Phase 3 audio |
| 3b | Work the chunked implementation queue in [`next-phases-roadmap.md`](next-phases-roadmap.md) (one PR per chunk) | L2S + agent | Phases 3–5 |
| 4 | Close D9 (LMS, SCORM version), D10 (voices), D11 (brand) — sheet tier 3, due 2026-10-26 | My Clinic L&D / Marketing | Phase 3 and 4 |
| 5 | Close module B-items and D1–D8, D12–D14 with named SMEs; update Phase 0 files and cards — sheet tier 1 (28 rows, due 2026-10-22) and tier 2 (71 rows, due 2026-10-30) | SMEs | Phase 2 approval |
| 6 | Close the 52 register rows (G5); decide the thin objectives (G4, one sheet row per module) | SMEs + L&D | Phase 4 build fields |
| 7 | ~~Download companion PNGs (G6)~~ ✅ done 2026-10-15 (`tools/import_companion_art.py`); record and approve two 30-second voice samples | Marwan / course owner | Phase 3 |
| 8 | Module 08: test environment, test patient, 2-hour capture session, DPO review | IT + DPO | 08 build |
| 9 | Phase 3: produce narration audio (normalised), final images, captions; rerun `lint_narration_script` and `lint_authoring_plan(stage="planning")` | L2S | Phase 4 |
| 9a | Media agents work `production/media-jobs.json` per [`media-production-runbook.md`](media-production-runbook.md); map hotspots on every new picture | Image / audio / video agents | Phase 3 |
| 9b | Rewrite the generic narration (G11) and fix `hs2-031` (G13) | Storyboard agent | voice work, Phase 2 sign-off |
| 10 | Phase 4: ~~draft builds~~ ✅ v0.1-draft for all eight (2026-10-15). Release builds: close decisions → update `screens.json`/storyboard → rerun `build_course_spec.py` + `build_package.py` → `check_packages.py` → `draft_builds_report.py` | L2S | Phase 5 |
| 10b | Smoke-test the draft zips in SCORM Cloud now (launch, resume, scoring, completion) to catch LMS issues before D9 closes. The XSD half is ✅ done 2026-10-15 ([xsd-validation.md](xsd-validation.md)) | L2S | C18 |
| 11 | Phase 5: `validate_package`, SCORM Cloud, LMS upload and test, pilot with 5–8 new starters, sign-off | L2S + My Clinic | launch |

Order of builds once unblocked (matches the learning path and the proposal staggering): **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.
