# Sample course for Oracle Learning (LMS compatibility pilot)

![My Clinic logo](../00_program/brand/logo-preview.png)

| Item | Value |
|---|---|
| Purpose | One small package My Clinic's LMS team can upload to **Oracle Learning** (Oracle Applications Cloud) to confirm launch, tracking and resume before the eight real packages arrive |
| Brand | My Clinic brand; module colour **Ambitious teal #008C99**; layouts L1–L6 |
| Built by | The same pipeline as the eight courses: `tools/build_sample.py` → `tools/build_package.py` (our own SCORM 1.2 player, `tools/player/`; edumints retired 2026-10-20) |
| Packages | `build/MC_Sample_OracleLearning_1.2.zip` (**upload this one first**) (the 2004 build was dropped with the edumints compiler: Oracle documents SCORM 1.2 support, and the player is 1.2 only) |
| Seat time | ~8 minutes · 13 screens · 4 scored checks · 60 points · pass 80% (48) |
| Content | Standard, low-risk practice: two patient identifiers, RACE/PASS fire response, WHO five moments for hand hygiene. Not reviewed by My Clinic SMEs; a sample, not a course |

## What is inside

| # | Screen | Interaction | Motion |
|---|---|---|---|
| 1 | `mcs-000` Welcome | Title with Dr. Omar and Noor | Heartbeat line draws in, pulse rings; guide cards slide up |
| 2 | `mcs-001` How this sample works | Content + Noor | Bullets reveal in sequence |
| 3 | `mcs-010` The right patient | Content + motion graphic | Wristband builds, two identifiers tick, room number crossed out |
| 4 | `mcs-011` Identifier or not? | Flip cards | Card flip |
| 5 | `mcs-012` ★ Two patients, one name | Branching scenario hosted by Noor (20 pts) | Avatar pop-in |
| 6 | `mcs-020` Find the fire equipment | Explore hotspot on the clinic corridor (8 items) | Markers, reveal |
| 7 | `mcs-021` If you find a fire: RACE | Motion graphic | RACE steps light up along a progress line; PASS appears |
| 8 | `mcs-022` ★ Put RACE in order | Sorting (10 pts) | — |
| 9 | `mcs-023` ★ Using the extinguisher | Multiple choice (10 pts) | — |
| 10 | `mcs-030` Five moments | Motion graphic | Patient zone grows; moments 1–5 appear in turn |
| 11 | `mcs-031` ★ Which moment is it? | Drag and drop (20 pts) | — |
| 12 | `mcs-090` Your results | Results by topic | — |
| 13 | `mcs-091` Close | Summary with score + Dr. Omar | — |

All motion respects the learner's *reduce motion* setting. Captions are on every screen; there is no voice in the sample (voices are decision D10).

## Oracle test

Follow [`oracle-learning-test-guide.md`](oracle-learning-test-guide.md). Rebuild: see the commands at the top of `tools/build_sample.py`.
