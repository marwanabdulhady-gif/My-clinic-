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
| 03 Welcome On Board | 🔒 B1–B14, D3 D5 D8 | ✅ | ✅ 36 | ✅ v0.1 · 36 cards | ✅ (single voice) | 🟡 mockups only, no register | ⬜ **not retrofitted** | 🟡 not rerun | 🟡 reference audio (10 clips, not shipping voice) | ⬜ | ⬜ |
| 04 Who Does What | 🔒 B1–B7, D3 D5 D11 | ✅ | ✅ 13 | ✅ v0.2 · 13 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 05 RCM Part A | 🔒 B1–B10, D4 D11 | ✅ | ✅ 21 | ✅ v0.2 · 21 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 06 RCM Part B | 🔒 B1–B9, D4 D5 D11 | ✅ | ✅ 15 | ✅ v0.2 · 15 cards | ✅ | ✅ | ✅ | ✅ clean | ⬜ | ⬜ | ⬜ |
| 07 Clinical Governance | 🔒 B1–B11, D7–D10, NEW-01 | ✅ | ✅ 22 (+1 optional) | ✅ v0.1 · 22 cards | ⬜ **no JSON files** | ⬜ **no board, no register** | 🟡 Noor only, no speaker tags | ⬜ | ⬜ | ⬜ | ⬜ |
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
| Proposal (6 courses, USD 9,000) | ✅ Rev00 · see §3 for the check |
| Cross-module decisions D1–D14 | 🔒 all 14 open |
| Voices (D10), LMS + SCORM version (D9) | 🔒 open |
| Any SCORM project, build, package or LMS test | ⬜ none yet |

**In one line:** design is complete to storyboard level for all eight packages (207 core screens, 95 scored). Nothing can move to voice, media or build until My Clinic closes the Phase 0 items and D9–D11.

---

## 2. Gaps found in this check, and what to do

| # | Gap | Where | Fix | Who |
|---|---|---|---|---|
| G1 | **03 storyboard predates the companions.** It uses a module-only mentor (`mentor-noor` / `hr-char-noor`), has no Dr. Omar, and its narration has no `NOOR:` / `OMAR:` speaker tags. Phase 2 and Phase 3 say Omar leads with Noor as co-host. | `03_hr-employee-induction/storyboard/` | Retrofit to v0.2: swap `hr-char-noor` for the shared `char-noor-*` / `char-omar-*` set, apply the Phase 3 companion table, tag every narration line, regenerate `narration-script.json` and `audio-script-export.json`, add `asset-register.md`, `screen-visuals.html` and `lint-report.json`. | Storyboard agent |
| G2 | **07 storyboard pack is incomplete.** No `narration-script.json`, `visual-plan.json`, `voice_talent.md`, visual board, asset register or lint report. Uses module-only `qsr-char-noor`; Dr. Omar's screens (`qsr-031`, `qsr-040`, `qsr-092`) are not in the cards. | `07_quality-safety-and-risk/storyboard/` | Complete the pack to the same v0.2 standard as 01/02/04/05/06/08 and apply the Phase 3 companion table. | Storyboard agent |
| G3 | **Shipping audio voice settings are generic.** Every `narration-script.json` has `voice_id: null`, `gender: null` and a generic persona, not the two companion voices. | all `storyboard/narration-script.json` | After D10, set one voice block per companion and keep the `NOOR:` / `OMAR:` split (companions.md §5). | Course owner → agent |
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
| Scenarios, games, simulations | 8 · 4 · 1 · 5 · 2 · 7 = 27 | 5+3 · 4 · 1 · 2+2 · 2 · 7 = **26** | ⚠ RCM is 4, not 5 |
| Narration | 27 · 13 · 5 · 13 · 7 · 5 = **~70 min** | 16.1+6.5 · 11.5 · 4.4 · 6.3+4.6 · ~7 (Phase 3 estimate; no script file yet) · 5.0 = **~61 min** | ⚠ written scripts are ~9 min shorter |
| SCORM version | "1.2 or 2004, to match the LMS" | 2004 for 01 and 03, 1.2 for the rest; D9 open | ✅ |
| EHR | new test-patient screenshots, original video not used | Phase 0 B2, D6; 7 simulations | ✅ |
| Phases and payment points | Phases 0–5, 9–10 weeks | same phase model in every folder | ✅ (README timeline now aligned) |
| Companions Noor and Dr. Omar, two voices | **not mentioned** | in every plan, Phase 2/3 and 6 of 8 storyboards | ⚠ added after Rev00 |

**Verdict:** the proposal matches the plans on every number the client pays for (courses, packages, screens, scored activities, pass marks, test cases, seat time). Three things to correct in a **Rev01** before it goes to My Clinic:

1. **Narration:** say "about 60 minutes" (or "up to 70 minutes") instead of "about 70 minutes". The finished scripts total ~61 minutes; promising 70 creates a gap at delivery.
2. **Scenarios:** RCM has 4 scenarios, games and adaptive practice (2 in Part A, 2 in Part B), so the total is 26, not 27. Or add one scenario to RCM Part A to keep 27.
3. **Companions:** add one line under the approach and deliverables: two consistent guide characters (Noor and Dr. Omar) with two narration voices across all courses. It is a visible value-add that the client will see in every storyboard.

Optional for Rev01: the proposal says L2S prepared "a screen-by-screen storyboard outline". Full v0.2 storyboards now exist for all eight packages, so the proposal can say so.

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
| 2 | Issue proposal Rev01 (§3 fixes) with the storyboard pack as evidence | L2S | contract |
| 3 | Retrofit 03 and complete 07 to v0.2 (G1, G2) | Storyboard agent | Phase 2 sign-off for 03, 07 |
| 4 | Close D9 (LMS, SCORM version), D10 (voices), D11 (brand) | My Clinic L&D / Marketing | Phase 3 and 4 |
| 5 | Close module B-items and D1–D8, D12–D14 with named SMEs; update Phase 0 files and cards | SMEs | Phase 2 approval |
| 6 | Close the 37 register rows (G5); decide on thin objectives (G4) | SMEs + L&D | Phase 4 build fields |
| 7 | Download companion PNGs (G6); record and approve two 30-second voice samples | Marwan / course owner | Phase 3 |
| 8 | Module 08: test environment, test patient, 2-hour capture session, DPO review | IT + DPO | 08 build |
| 9 | Phase 3: produce narration audio (normalised), final images, captions; rerun `lint_narration_script` and `lint_authoring_plan(stage="planning")` | L2S | Phase 4 |
| 10 | Phase 4: `build_from_spec` per module following each `scorm-structure.md`; `lint_course`; preview | L2S | Phase 5 |
| 11 | Phase 5: `validate_package`, SCORM Cloud, LMS upload and test, pilot with 5–8 new starters, sign-off | L2S + My Clinic | launch |

Order of builds once unblocked (matches the learning path and the proposal staggering): **03 → 07 → 01 → 02 → 04 → 05 → 06 → 08**.
