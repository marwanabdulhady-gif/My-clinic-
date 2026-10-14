# Scenario design plan — six courses, eight SCORM packages

## Purpose and proposal fit

The Rev01 proposal commits to **26 scenario, game and guided-simulation experiences** across six customer-facing courses. The repository's proposal/status reconciliation maps those to eight production packages as **5 + 3 + 4 + 1 + 2 + 2 + 2 + 7 = 26**. Grouped for the proposal, that is HSE (01+02) **8**, HR (03) **4**, Operations (04) **1**, RCM (05+06) **4**, Clinical Governance (07) **2**, and IT/EHR (08) **7**. This reconciles with the Rev01 proposal and current programme status. The exact screen ids and step counts below are controlled by each package's Phase 2/3 files.

## Scenario principles

Use short, credible workplace situations that require the learner to choose an action, inspect a screen or complete a safe sequence. Each activity must assess an action from the module's Phase 1 action map and must use only facts in its source or a closed Phase 0 decision. Put the consequence and coaching in per-choice feedback. Never use a real incident as a case unless client approval and privacy review are explicit; the existing storyboards mark cases fictional where relevant.

Show one decision at a time when the decision has a safety consequence. Keep the situation text concise and readable. Avoid punitive countdowns, shame, patient-harm spectacle, real staff names and unapproved department-routing rules. Use fictional identities/data. A scene image is atmosphere; it cannot carry the answer or replace the text instruction.

Noor and Dr. Omar are story guides, not authority for policy. Use the approved pose and speaker specified in the package's Phase 3 companion table. Their reactions can reflect safe/unsafe outcomes without ridicule or exaggeration. The active question remains character-free as directed by `characters/companions.md`.

## Experience map

- **HSE — packages 01 and 02, total 8.** Package 01's five experiences are `hs1-205` (AREC/controls/rights), `hs1-409` (RACE fire response), `hs1-507` (Code Orange decision), `hs1-802` (overdue infusion-pump reporting) and `hs1-950` (mixed “One shift, three plans” capstone). Package 02's three experiences are `hs2-030` (Code Red `case_sim` game), `hs2-052` (spill triage) and `hs2-064` (escape-room game). Noor leads safety cases; Dr. Omar appears only where Phase 3 specifies. Emergency codes, spill thresholds and response language remain blocked by open client decisions.
- **HR — package 03, total 4.** The four experiences are `hr-031` (conflict-of-interest decision scenario), `hr-044` (four-colleague leave-desk scenario), `hr-045` (adaptive leave-rule practice) and `hr-061` (Oracle annual-leave simulation on a test account). Omar leads; Noor co-hosts planned ethics/leave moments. HR policy values and Oracle capture require SME approval.
- **Operations & My Care — package 04, total 1.** `ops-031` is the scored role-routing decision scenario with four routing nodes. `ops-002` is an exploration of the patient journey that supports the course but is not counted as a second scenario in the proposal. Dr. Omar leads; Noor appears only at planned guide moments. B7 controls unapproved role ownership and routing.
- **RCM — packages 05 and 06, total 4.** Package 05 has `rcma-031` (joint-pain documentation/coding decision scenario) and `rcma-050` (“Fix the note” case-simulation game). Package 06 has `rcmb-052` (claim rework scenario) and `rcmb-060` (“Covered or not?” adaptive practice). Dr. Omar hosts the cases/game; Noor's hints appear only where Phase 3 specifies. Payer rules, claim examples and benefits counts require SME confirmation.
- **Clinical Governance — package 07, total 2.** `qsr-021` covers patient-identification decisions; `qsr-051` covers end-of-shift near-miss reporting. Both are fictional cases. Noor leads; Dr. Omar co-hosts selected risk/near-miss content. Matrix bands, incident labels, response routes and wording require Quality owner review.
- **IT/EHR — package 08, total 7.** Seven guided simulations cover opening a consultation (`ehr-010`), diagnosis (`ehr-020`), medication order (`ehr-031`), lab package (`ehr-032`), consultation summary (`ehr-040`), SMS education (`ehr-041`) and referral/follow-up (`ehr-050`). Dr. Omar leads, with Noor on the planned patient-education tip. Use only approved test-environment screenshots and a fictional patient; no source-video frame containing real patient data.

The package counts above follow the explicit Rev01 reconciliation in `programme-status.md` §3. If a storyboard's activity is reclassified, update the package count, `scorm-structure-summary.json`, proposal cross-check and this plan together.

## Per-scenario authoring record

Every scenario card should include: screen id and source; action/objective assessed; fictional learner situation; exact decision points and choices; best/unsafe choice; score delta; feedback per choice; hint/retry/lives rule; exit/pass rule; narrator and guide pose; scene asset/alt text; dependencies on Phase 0; keyboard and screen-reader alternatives; SME owner and written approval date. For simulations, add the test screenshot/version, each click/type target, accepted input variants, reset behavior and test-patient approval record.

## Review and release gates

1. Keep the six-course totals and eight-package mapping consistent: 26 experiences overall. The current totals match Rev01.
2. Close relevant Phase 0 items in writing before turning a pending rule into a choice or feedback. C1's generated decision sheet is the owner queue, not an approval.
3. Close the 52 SME/build-detail register rows and the thin-objective choices. Confirm that each learning objective has adequate evidence or record the SME's acceptance of a single scored check.
4. Have the accountable SME review every scenario's facts, answer key, feedback and consequences. Safety/clinical examples require Safety/Quality/clinical review; HR items require HR review; claim/payer examples require RCM review; EHR simulations require IT and DPO review.
5. Test every branch, reset and retry with keyboard-only use, captions, text alternatives and non-colour cues. Retain a trace from source statement to screen choice and feedback.

A scenario design can be ready for review while still being unapproved. Do not treat an internally drafted answer or a character's spoken line as client policy.
