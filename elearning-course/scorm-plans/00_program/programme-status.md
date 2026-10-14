# Programme status, gaps and next steps

![My Clinic logo](brand/logo-preview.png)

> Status as at **2026-10-14**. Checked against the files in this repository: every module folder, every storyboard pack, the review register and the proposal (`../../proposal/MyClinic_Induction_eLearning_Proposal_e2026-MC01_Rev00.docx`). This report records **production progress only**. No policy, clinical, payer or EHR content is approved yet.

---

## 1. Where every module stands

✅ done (draft ready for review) · 🟡 partly done · ⬜ not started · 🔒 waiting on My Clinic

| Module | Ph 0 source lock | Ph 1 action map | Ph 2a screen list | Ph 2b storyboard cards | Narration script + visual plan | Visual board + asset register | Companions in storyboard | Planning lint | Ph 3 voice and media | Ph 4 build | Ph 5 QA / LMS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 FMS | 🔒 B1–B10, D1 D2 D11 D14 | ✅ | ✅ 54 | ✅ v0.2 · 54 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 02 Safety Lab | 🔒 B1–B9, D1 D2 D11 D12 | ✅ | ✅ 26 | ✅ v0.2 · 26 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 03 Welcome On Board | 🔒 B1–B14, D3 D5 D8 | ✅ | ✅ 36 | ✅ v0.2 · 36 cards | ✅ | ✅ | ✅ Omar lead, Noor co-host | ✅ clean | 🟡 old single-voice reference clips only | ⬜ | ⬜ |
| 04 Who Does What | 🔒 B1–B7, D3 D5 D11 | ✅ | ✅ 13 | ✅ v0.2 · 13 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 05 RCM Part A | 🔒 B1–B10, D4 D11 | ✅ | ✅ 21 | ✅ v0.2 · 21 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 06 RCM Part B | 🔒 B1–B9, D4 D5 D11 | ✅ | ✅ 15 | ✅ v0.2 · 15 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 07 Clinical Governance | 🔒 B1–B11, D7–D10, NEW-01 | ✅ | ✅ 22 (+1 optional) | ✅ v0.2 · 22 cards | ✅ | ✅ (+3 native SVGs) | ✅ Noor lead, Omar co-host | ✅ clean | ⬜ | ⬜ | ⬜ |
| 08 EHR | 🔒 B1–B10, D6 D11 | ✅ | ✅ 20 (+1 optional) | ✅ v0.2 · 20 cards | ✅ | ✅ | ✅ | ✅ clean | 🔒 test-patient captures | ⬜ | ⬜ |

**Programme level**

| Item | Status |
|---|---|
| Plans in phases for all 8 packages (Phases 0–5) | ✅ |
| Brand identity, logo files, layouts L1–L6, screen mockups | ✅ draft · 🔒 Marketing confirmation (D11) |
| Companions Noor and Dr. Omar: bible, 8 poses each, avatars, placement rules | ✅ · ⬜ full-size transparent PNGs not yet downloaded from Canva into `characters/assets/` |
| Storyboard template, screen-type guide, examples, review checklist | ✅ |
| Client-review Word pack (all 8) + review register (37 build-detail questions) | ✅ v0.2 |
| **SCORM structure** (programme + per module) | ✅ new: [`scorm-structure.md`](scorm-structure.md) and `<module>/scorm-structure.md` |
| Proposal (6 courses, USD 9,000) | ✅ Rev01 (narration ~60 min, 26 scenarios, guide characters) · see §3 |
| Cross-module decisions D1–D14 | 🔒 all 14 open |
| Voices (D10), LMS + SCORM version (D9) | 🔒 open |
| Any SCORM project, build, package or LMS test | ⬜ none yet |

**In one line:** design is complete to storyboard level for all eight packages (207 core screens, 95 scored). Nothing can move to voice, media or build until My Clinic closes the Phase 0 items and D9–D11.

---

## 2. Gaps found in this check, and what to do

| # | Gap | Where | Fix | Who |
|---|---|---|---|---|
| G1 | ~~03 storyboard predates the companions.~~ **Done:** v0.2 with shared `char-*` art, `OMAR:`/`NOOR:` tags, two-voice split on `hr-000` and `hr-091`, full pack and clean lint. | `03_hr-employee-induction/storyboard/` | — | Done |
| G2 | ~~07 storyboard pack is incomplete.~~ **Done:** v0.2 with Omar on `qsr-031`, `qsr-040` and `qsr-092`, full pack, 3 native SVG diagrams and clean lint. SME to confirm: Noor beside the unscored poll on `qsr-002` (companions.md says no companion over a question), risk-matrix band names (B6), and the closing quote (B1). | `07_quality-safety-and-risk/storyboard/` | Confirm the three points in Phase 0 review | SMEs |
| G3 | **Shipping audio voice settings are generic.** Every `narration-script.json` has `voice_id: null`, `gender: null` and a generic persona, not the two companion voices.  Also, in 01, 02, 04, 05, 06 and 08 the TTS text started with the `NOOR:`/`OMAR:` label, so the voice would have read it aloud; **fixed** (label removed from `tts_text`, `speaker` field added). Still open: 7 screens in those packs have both voices in one segment (2 in 01, 2 in 02, 1 each in 04, 05, 06) and must be split into `noor-1`/`omar-1` parts, as 03 and 07 do. | all `storyboard/narration-script.json` and `audio-script-export.json` | After D10, set one voice block per companion and keep the `NOOR:` / `OMAR:` split (companions.md §5). | Course owner → agent |
| G4 | **Thin objective evidence.** 14 objectives are assessed by one scored screen only, so the LMS objective result depends on one answer. | see each `scorm-structure.md` §5 | Add a second short check where the objective matters for compliance (01 `hs1-o6`, `hs1-o7`; 07 `qsr-o5`; 08 `ehr-o2`), or accept at SME sign-off. Capstones (`hs1-o10`, `rcma-o5`) are fine as one big case. | SMEs + L&D |
| G5 | **37 scored screens still need SME build detail** (answers, feedback, replay rules, typed-answer variants). | [`storyboard-review-register.md`](storyboard-review-register.md) | Close row by row with the named SME, then update the cards. | SMEs + L&D |
| G6 | **Companion art not in the repo at full size.** Only preview JPGs exist; the proxy blocks Canva downloads. | `characters/` | Download the 18 files by media id (companions.md §3) as transparent PNGs into `characters/assets/`. | Marwan (Canva) |
| G7 | **Master timeline was out of step with the proposal** (8 weeks vs the proposal's 9–10 weeks). | `../README.md` §3 | Fixed in this pass: the README timeline now follows the proposal's phases. | Done |

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

---

## 5. What happens next (in order)

| Step | Action | Owner | Unblocks |
|---|---|---|---|
| 1 | Send the client-review Word pack and the review register to My Clinic; book the Phase 0 kick-off | L2S | everything |
| 2 | ~~Issue proposal Rev01 (§3 fixes)~~ ✅ done — send Rev01 with the storyboard pack as evidence | L2S | contract |
| 3 | ~~Retrofit 03 and complete 07 to v0.2 (G1, G2)~~ ✅ done; split the 7 two-voice segments (G3) | Storyboard agent | Phase 3 audio |
| 4 | Close D9 (LMS, SCORM version), D10 (voices), D11 (brand) | My Clinic L&D / Marketing | Phase 3 and 4 |
| 5 | Close module B-items and D1–D8, D12–D14 with named SMEs; update Phase 0 files and cards | SMEs | Phase 2 approval |
| 6 | Close the 37 register rows (G5); decide on thin objectives (G4) | SMEs + L&D | Phase 4 build fields |
| 7 | Download companion PNGs (G6); record and approve two 30-second voice samples | Marwan / course owner | Phase 3 |
| 8 | Module 08: test environment, test patient, 2-hour capture session, DPO review | IT + DPO | 08 build |
| 9 | Phase 3: produce narration audio (normalised), final images, captions; rerun `lint_narration_script` and `lint_authoring_plan(stage="planning")` | L2S | Phase 4 |
| 10 | Phase 4: `build_from_spec` per module following each `scorm-structure.md`; `lint_course`; preview | L2S | Phase 5 |
| 11 | Phase 5: `validate_package`, SCORM Cloud, LMS upload and test, pilot with 5–8 new starters, sign-off | L2S + My Clinic | launch |

Order of builds once unblocked (matches the learning path and the proposal staggering): **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.
