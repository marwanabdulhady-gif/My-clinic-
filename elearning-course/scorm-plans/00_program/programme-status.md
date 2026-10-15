# Programme status, gaps and next steps

![My Clinic logo](brand/logo-preview.png)

> Status as at **2026-10-15** (draft SCORM builds for all eight packages added; full-size companion art imported). Checked against the files in this repository: every module folder, every storyboard pack, the review register and the proposal (`../../proposal/MyClinic_Induction_eLearning_Proposal_e2026-MC01_Rev01.docx`). This report records **production progress only**. No policy, clinical, payer or EHR content is approved yet.

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
| SCORM packages | 🟡 **v0.1-draft for all eight** (2026-10-15): real edumints compiler, `lint_course` 0 errors, `validate_package` ok (structural; XSD offline). Pending decisions shown as `⚠ Draft — pending`, unmade media as PENDING cards, captions only. [`draft-builds.md`](draft-builds.md) |
| LMS / SCORM Cloud test | ⬜ not yet (D9 open) |

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
| G15 | **XSD validation not run** (schemas unreachable offline). | build environment | Run `validate_package` once with the IMS/ADL schemas (`SCORM_SCHEMA_DIR`), then SCORM Cloud. | L2S |
| G16 | **Schema limits** recorded in `screens.json` notes: no per-card feedback on drag/sort, no per-choice companion reaction, no media on mcq/matching/escape-room, one hint ladder per game. | edumints schema | Accept for v1.0 or request schema additions upstream; SMEs see the workaround wording at review. | L2S |
| G17 | **NFPA 704 diagrams were drawn wrong** (rotated quadrants, numbers on the wrong colours) in `hs1-img-nfpa-blank`, `hs1-img-nfpa-301w`, `hs2-img-nfpa-230`. | 01/02 storyboard assets | **Fixed** 2026-10-15: redrawn to the standard layout; the blank no longer prints the answers. | Done |

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
| SCORM version | "1.2 or 2004, to match the LMS" | 2004 for 01 and 03, 1.2 for the rest; D9 open | ✅ |
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

---

## 5. What happens next (in order)

| Step | Action | Owner | Unblocks |
|---|---|---|---|
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
| 9b | Rewrite the generic narration (G11) and fix `hs2-031` (G13) | Storyboard agent | voice work, Phase 2 sign-off |
| 10 | Phase 4: ~~draft builds~~ ✅ v0.1-draft for all eight (2026-10-15). Release builds: close decisions → update `screens.json`/storyboard → rerun `build_course_spec.py` + `edumints_build.py` → `draft_builds_report.py` | L2S | Phase 5 |
| 10b | Smoke-test the draft zips in SCORM Cloud now (launch, resume, scoring, completion) to catch LMS issues before D9 closes | L2S | C18 |
| 11 | Phase 5: `validate_package`, SCORM Cloud, LMS upload and test, pilot with 5–8 new starters, sign-off | L2S + My Clinic | launch |

Order of builds once unblocked (matches the learning path and the proposal staggering): **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.
