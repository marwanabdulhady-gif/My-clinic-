# Gamification plan — learning-first practice and feedback

## Purpose

Use interaction and feedback to strengthen safe job performance, not to turn clinical induction into a competition. The Rev01 proposal and current SCORM structure commit to 95 scored activities across 207 screens and 26 scenario/game/simulation experiences. The six course groups are HSE, HR, Operations & My Care, RCM, Clinical Governance and IT/EHR; the eight packages are detailed in [`scenario-design-plan.md`](scenario-design-plan.md). Pass marks currently range from 70% to 80% by package, as set in Phase 4.

Do not introduce leaderboards, public ranking, time pressure, streaks, or badges as a new deliverable. Those are absent from the approved proposal and can distort safety-related behaviour. Course progress, score and objective tracking use SCORM and the agreed LMS settings once D9 is closed.

## Mechanics already planned

- **Decision scenarios and case simulations:** choices create a consequence and coaching feedback; scoring uses the existing per-choice rubric. Examples include RACE, spill triage, patient identification, rework and the HSE capstone.
- **Sequencing and guided exploration:** learners open hotspots, put steps in a safe order, or inspect required fields. Require the complete required set or show which step needs review. Keep textual equivalents for non-pointer access.
- **Escape-room and multi-step drills:** package 02's Code Red drill uses six decision nodes, two lives and one text hint per node, with no timer; its escape room uses four sequential puzzles, three lives and one hint per puzzle. Wrong choices lead to feedback/debrief and a retry, not a learner penalty outside the activity.
- **Case-simulation game:** package 01's capstone uses three lives and one hint per node, no timer, with success based on the best choices at two of three nodes. Package 05's “Fix the note” has three nodes, one hint per node, no lives and no timer; its pass score is two.
- **Adaptive practice:** HR leave-rule practice and RCM coverage practice use the existing item banks and documented target/pass ratios. Keep item wording, accepted answers and feedback under SME control.
- **Software simulations:** Oracle and EHR interactions use stepwise click/type tasks with hints and text instructions. Reset or retry at the step; the activity does not pretend to connect to production clinical systems.

The full activity rules, objective mapping, score fields and screen ids are in each package's Phase 3 activity table, Phase 2 storyboard and Phase 4 build plan. This plan does not change those settings.

## Feedback and scoring rules

Give feedback immediately after a choice, and explain why the choice is safe or what to reconsider. Preserve per-choice feedback for scenarios; avoid “wrong because wrong” messages. Do not reveal the answer in pre-choice narration, a visible companion reaction or a clue before the interaction. Hints should prompt the learner to use a rule, screen panel or sequence, not give the answer word-for-word.

Respect the current package pass marks and points. Do not normalize across packages or add points for speed. Where practice has lives, explain the rule and debrief before retry. Do not turn formative activities into course failure unless the relevant Phase 4 specification says they count toward the final pass. Preserve per-objective results and use the existing SCORM structure to transmit them; do not infer learner competence from completion alone.

## Accessibility and fairness

Every pointer action must have a keyboard alternative. Supply text instructions/steps for simulations, readable clue content for escape-room tasks, descriptive alt text for meaningful diagrams, and captions/transcripts for narration. No answer, status, risk band or score may be communicated by colour alone. Do not use sound-only or time-limited success cues. Make retries available according to the planned mechanic and never shame a learner for using a hint or retry.

For adaptive practice, retain the documented item-bank order/randomization and accepted input variants. Test that alternate accepted spellings and capitalization do not unfairly fail the learner. Track performance only at the agreed LMS level; do not add sensitive learner analytics or public ranking.

## Current design risks and decisions

The SCORM structure audit flags 14 objectives as having only one scored evidence screen. These are visible in `programme-status.md` §2/G4 and the generated per-package `scorm-structure.md` §5. SMEs and L&D must add a second check for objectives where compliance risk warrants it, or record written acceptance that one check is sufficient. Do not inflate the screen count or change pass marks without updating Rev01 and receiving approval.

The client must confirm LMS and SCORM version through D9 before build. Keep package-level settings as currently planned but treat them as conditional until D9 is closed. Review all open Phase 0 thresholds/codes and the 52 screen-level authoring questions before finalizing the answer keys, accepted responses and retry criteria.

## Gamification quality gate

Before build, for every scored interaction confirm: objective id and point value match Phase 4; correct and incorrect feedback are substantive; per-choice feedback exists for branching tasks; hints do not disclose answers; retries/lives/pass rules match Phase 3; keyboard and text-only alternatives work; color is not the sole cue; and the interaction does not use real patient or staff data. Run `lint_planning.py`, regenerate `scorm-structure.md`, close the relevant SME register row, and include the case in the 81-test QA plan. Package-level quiz/pass totals must reconcile with Rev01.

## Programme gamification system (owner decision D18, 2026-10-20)

The owner asked for a visible gamification layer across all eight courses. It is built by `tools/gamify.py` from [`gamification.json`](gamification.json) and changes nothing scored:

| Mechanic | What the learner sees | Rule |
|---|---|---|
| **Challenge** | A "Can you …?" hook on a mission-brief screen after the role picker (e.g. *Can you keep your clinic safe in your first week?*), with the course's challenge illustration | One per course; hooks in `gamification.json` |
| **Missions** | Every teaching section is "Mission n · <title>" in the menu | Welcome and close sections are not missions |
| **XP** | ★ n XP in the header | +10 per scored activity answered correctly, +5 per quick check, +2 per screen explored |
| **Ranks** | ◆ rank in the header, four per course (e.g. Newcomer → Safety Spotter → Safety Ally → Safety Champion) | Unlocked at 0 / 30 / 60 / 85 % of the course's maximum XP |
| **Debrief** | "You finished with n XP" on the closing screen | — |

Still excluded: leaderboards, public ranking, timers and speed bonuses, penalties outside the existing games, and anything that feeds XP into the score, the pass mark or the LMS record. XP lives only in the course variables (resume data, a few bytes). Revisiting a screen can add XP again; that is accepted because XP has no consequence. The earlier text in this plan that ruled out badges is superseded for ranks only, by D18.

### The seven portfolio upgrades (inspiration-portfolio-review.md, applied 2026-10-20)

All seven are built by `tools/gamify.py` (1–5, 7) or by the module layers (6). Nothing scored changes: no screen id, type, order, point or objective moved, and the totals are unchanged (220/145/145/50/100/80/95/90).

| # | Idea | What the learner sees | Where it lives |
|---|---|---|---|
| 1 | **Outcome meter** | A five-dot meter at the top, named for the course ("Clinic safety", "Patient trust", "Claim health", …). It starts at 3, goes up on each scored decision, game or simulation answered well, and down on each one answered badly. It is never the score. | `gamification.json` `meter`; player `lives_var: meter`, `max_lives: 5` |
| 2 | **Ask Noor / Ask Dr. Omar** | Before 12 key decisions: "Want a hint first?" → a short nudge from the companion (never the answer), or "I'm ready". | `gamification.json` `hints`; screens `<id>-ask`, `<id>-hint` (unscored, `visible_if hint == 1`) |
| 3 | **Consequence first** | Every decision-scenario reply starts with "✓ Better for the patient." or "⚠ Risk for the patient." (target per course), then the existing feedback. | `outcome_target` |
| 4 | **A day at the clinic** (02) | A 07:30 → 15:00 shift timeline after the brief, with each mission given a time. | `shift`, `shift_title`, `shift_notes` (02 only) |
| 5 | **Revisit map** | On the results screen, each weak area says which mission to reopen from the menu. | built from `evidence_screen_ids` |
| 6 | **Drag-to-store practice** (01, 02) | 01 `hs1-501s` "Put it where it belongs"; 02 `hs2-051s` "Which kit?". Both are unscored, and the storage rules are marked ⚠ Draft — pending 01/B7 and 02/B4. | `<module>/production/personalisation.json` |
| 7 | **Replies from the other side** (04, 06) | Before the feedback, the patient's, doctor's or payer's reaction in italics. | `gamification.json` `replies` (`ops-031`, `rcmb-052`). Module 08 has no branching scenario yet. |

Rules: hints and replies use only storyboard wording or ⚠-pending assumptions. The meter is shown with its name and in the module colour, turning red only when low. The meter and hint values are course variables, like XP.
