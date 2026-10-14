# Plan audit — My Clinic induction programme

**Checked:** 14 October 2026 against proposal Rev01, the eight package folders, current storyboards/SCORM summaries, PR #33 and the available planning gates.

## Verdict

**The proposal and storyboard plan align on the principal quantities, but the programme is not production-ready.** The six commercial courses map to eight SCORM packages. Rev01's 207 screens, 95 scored activities, pass marks, approximately four hours of learner seat time, 81 test cases, 26 scenario/game/simulation experiences and about 60 minutes of two-voice narration reconcile with the current package plans. The scenario breakdown is 5+3+4+1+2+2+2+7 = 26 across the eight packages; the proposal groups that as 8+4+1+4+2+7 = 26 across six courses. The current programme status has the same cross-check in §3.

This is **scope/structure alignment**, not SME or client approval. No policy, clinical, payer, HR, EHR, brand or voice decision is approved merely because it appears in a storyboard or a generated recommendation.

## What is already in place

- All eight packages have Phase 0–5 plans, Phase 1 action maps, Phase 2 screen lists, complete draft storyboards, visual plans, narration scripts/exports, asset registers and Phase 5 test lists.
- The current storyboards cover 207 core screens and 95 scored activities. The build structure summary identifies 14 objectives with thin one-screen evidence; SMEs/L&D must add a second check where needed or accept the evidence limitation in writing.
- The universal storyboard template, screen-type guide, worked examples and review checklist already exist. Noor and Dr. Omar are specified in the character bible, per-package Phase 3 tables and storyboard visual references.
- The latest C1 change adds an open-decision sheet and kick-off pack to PR #33. The generated sheet has 102 open rows: 28 tier 1, 3 tier 3 and 71 tier 2. The pull request is **open** and has not been merged into `main` at the time checked.
- This pass adds a cited client-context brief, consolidated visual and narration production plans, an explicit scenario plan, a separate gamification plan, an asset prompt catalogue and one prefilled production worksheet per package.

## Test results

On the current project snapshot, `tools/lint_planning.py` reported 0 errors and 0 warnings in each of the eight packages. `tools/build_scorm_structure.py` regenerated the eight structures and summary. On PR #33, `tools/build_decision_sheet.py` generated 102 open rows with the expected 28/3/71 tier counts; `tools/export_kickoff_docx.py` generated the Word pack; and `tools/audit_assets.py` ended with `hard_failures=0` and `audit clean`.

The first PR #33 export attempt failed because `python-docx` was absent in this sandbox. After installing the repository's needed dependency in the test environment, the exporter succeeded. PR #33 currently shows no GitHub status checks in its status-check list, so the successful gates above were run locally and are not an automated GitHub CI result.

## What still prevents production or launch

- **The client has not closed the 102 Phase 0 decisions** in the open C1 decision sheet. These include safety thresholds/codes, HR/pay, payer/benefit and branch/organization facts, brand D11, LMS/SCORM D9 and voice D10.
- **The 52 scored-screen build-detail questions** remain in the SME register. The 14 thin objective-evidence flags also need a written decision.
- **Final audio is not complete.** Scripts and exports pass the local planning linter, but voice ids are null pending D10, sample voices need written approval, and final recorded/generated audio, normalization, captions and provenance remain to be produced.
- **Full-size companion art is not in the repository.** The 18 approved transparent assets are still to be downloaded from Canva. Interim avatar crops are not final assets.
- **Some illustration assets remain planned.** HR, Operations and Clinical Governance still have pending assets/prompt handoffs. The present prompt catalogue separates AI illustrations from diagrams that should be authored as SVG.
- **Module 08 must use DPO-approved fictional-patient test captures.** The committed source video contains patient identifiers and must not supply training media.
- **No SCORM build, package validation, SCORM Cloud/LMS test, learner pilot or launch sign-off has happened.** These remain phases 4–5, dependent on Phase 0 decisions and the D9 LMS setting.
- **Generated video is not in Rev01 scope.** The visual plan includes a clearly marked optional silent-loop prompt, but production must remain an optional enhancement until the owner approves scope and the client approves the content.

## Recommended next actions

1. Review and merge PR #33 through the normal repository review process; its documented local quality gates now pass.
2. Use the proposed kick-off pack to close the Phase 0 owner decisions and write every outcome back to its source file. Regenerate the decision sheet after each write-back.
3. Close the 52 SME rows and thin-objective evidence decisions; approve the visual character assets and final brand choices.
4. Close D10 and approve voice samples before asking audio agents to generate; use the exact JSON exports and do not authorize paraphrase.
5. Complete the prompted image assets and DPO-approved EHR screenshots; have the relevant SME review them before build.
6. Build, preview, validate and test each package on the agreed LMS/SCORM version, then pilot and record sign-off.
