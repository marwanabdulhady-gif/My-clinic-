# Phase 3 — Narration & assets (01 Facility Management & Safety)

Gates: `lint_narration_script(script, plan)` → `export_audio_script(script)` → `lint_authoring_plan(plan, stage="planning")` → **STOP for approval**.

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Noor** (narrates every narrated screen unless listed below). **Co-host: Dr. Omar**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| hs1-000 | Noor | `char-noor-welcome` | L1 half-body bottom-right | Noor | Welcomes learners and introduces herself |
| hs1-001 | Noor | `char-noor-explaining` | L3 right column, half-body | Noor | Call-point story (companions.md §1) |
| hs1-205 | Noor | `char-noor-avatar-neutral → -happy / -concern` | L5 avatar above situation | Noor | Sets up the corridor scene; reacts to choices |
| hs1-206 | Omar | `char-omar-avatar-neutral + tip card` | L3 tip card bottom-left | Omar | Tip: a doctor can stop unsafe work too — "I have, and nobody blamed me." |
| hs1-301 | Noor | `char-noor-avatar-neutral + tip card` | L3 tip card | Noor | Tip: save your site's extensions in your phone today |
| hs1-409 | Noor | `char-noor-avatar-neutral → -happy / -concern` | L5 avatar | Noor | Night-shift fire scenario host |
| hs1-506 | Omar | `char-omar-avatar-neutral + tip card` | L3 tip card | Omar | Tip: set a timer; keep flushing for 15 minutes |
| hs1-507 | Noor | `char-noor-avatar-concern (intro)` | L5 avatar | Noor | Spill scenario host |
| hs1-802 | Omar | `char-omar-avatar-neutral → -happy / -concern` | L5 avatar | Omar | Omar hosts the overdue infusion-pump scenario (he uses pumps daily) |
| hs1-950 | Noor + Omar | `char-noor-explaining; char-omar-avatar in node 3` | L5 | Noor + Omar | Capstone: Noor hosts, Omar appears when the suction unit is found |
| hs1-980 | Noor | `char-noor-success` | L6 right, half-body | Noor | Reads results with the learner |
| hs1-990 | Noor + Omar | `char-noor-success + char-omar-avatar-happy` | L6 | Noor + Omar | Two-voice close: Noor sums up, Omar hands over to the next course |

- Visible on 12 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `NOOR:` / `OMAR:`; two-voice screens are split into one segment per line (`part` = `noor-1`, `omar-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.

## 1. Narration outline (per screen)

Target ~140 wpm. "Sec" = target seconds. Question screens get a short set-up only; the answer is never narrated.

| Screen | Speaker | Sec | Narration intent (the script expands this; it must not read the screen) |
|---|---|---|---|
| hs1-000 | Noor | 15 | Welcome. Safety here is everyone's job; in the next hour you'll learn what to do in the first minutes of an emergency. |
| hs1-001 | Noor | 30 | Why: CBAHI surveyors ask staff, not just managers. Noor's story: "On my first day I didn't know where the nearest call point was." |
| hs1-002 | Noor | 8 | Set up the confidence check. |
| hs1-101 | Noor | 35 | The chapter is a survey requirement, a shared responsibility, and one connected system. |
| hs1-102 | Noor | 25 | Invite exploration: each plan protects a different physical risk; open all eight. |
| hs1-103 | Noor | 20 | Plans and codes are two views of the same system: give one example of each. |
| hs1-104 | Noor | 8 | Set up the match. |
| hs1-201 | Noor | 25 | Risk is likelihood plus severity; a hazard is the thing, risk is the chance it hurts someone. |
| hs1-202 | Noor | 30 | Why a near miss is the most valuable report: it is free learning. |
| hs1-203 | Noor | 30 | AREC as a habit before every task, not a form. |
| hs1-204 | Noor | 10 | Set up: start at the top. |
| hs1-205 | Noor | 15 | Set the corridor scene; stop before choices. |
| hs1-206 | Omar | 30 | You can stop unsafe work without fear; if you're unsure, ask your supervisor who your liaison is. |
| hs1-301 | Noor | 30 | Codes are announced overhead; learn the meaning, then your site's extension. Code Blue is 2222 everywhere. |
| hs1-302 | Noor | 8 | Set up. |
| hs1-303 | Noor | 25 | Evacuation and End of Disaster are announcements, not colours; only stand down on the official all-clear. |
| hs1-304 | Noor | 8 | Set up. |
| hs1-305 | Noor | 20 | The ERT is five teams; you are part of the response even if you're not on it. |
| hs1-401 | Noor | 30 | Remove one side of the triangle and the fire stops; smoke kills first, which is why RACE rescues and contains before extinguishing. |
| hs1-402/403 | Noor | 8 each | Set up. |
| hs1-404 | Noor | 20 | Walk the corridor; know where these are before you need them. |
| hs1-405 | Noor | 10 | Set up: wrong class can make a fire worse. |
| hs1-406 | Noor | 35 | Horizontal first; vertical by stairs; full evacuation only for the worst events. |
| hs1-407/408 | Noor | 8 each | Set up. |
| hs1-409 | Noor | 15 | Set the night-shift scene. |
| hs1-410 | Noor | 25 | Prevention rules exist because each item started a real fire somewhere. |
| hs1-501 | Noor | 25 | Chemicals come in one door only — procurement — and never without a label and an SDS. |
| hs1-502/503/504 | Noor | 8 each | Set up. |
| hs1-505 | Noor | 30 | Storage, transport and handling all follow the SDS. |
| hs1-506 | Omar | 25 | Find your nearest eyewash today; 15 minutes feels long — don't stop early. |
| hs1-507 | Noor | 15 | Set up three spills. |
| hs1-508 | Noor | 10 | Set up; never recap. |
| hs1-601 | Noor | 30 | Your badge identifies you; everyone without one in a restricted area is your concern. |
| hs1-602 | Noor | 8 | Set up. |
| hs1-701 | Noor | 25 | Red sockets are on generator power; know your shut-off valves; isolation-room vents protect everyone. |
| hs1-702 | Noor | 8 | Set up. |
| hs1-801 | Noor | 25 | Labels tell you if a device is safe to use today. |
| hs1-802 | Omar | 12 | Set the busy-ward scene. |
| hs1-803 | Noor | 8 | Set up. |
| hs1-901 | Noor | 35 | Ionising vs non-ionising; the MRI magnet is always on. |
| hs1-902 | Noor | 8 | Set up. |
| hs1-903 | Noor | 25 | Time, distance, shielding — three levers you control. |
| hs1-904 | Noor | 25 | Wear your badge; the RSO is your contact. |
| hs1-905/906 | Noor | 8 each | Set up. |
| hs1-907 | Noor | 25 | Laser eye injuries often don't hurt at first — that's why protection is not optional. |
| hs1-950 | Noor + Omar | 20 | Set up the shift: three plans, one afternoon. |
| hs1-980 | Noor | 15 | Read your results; revisit any section below 70%. |
| hs1-981 | Noor | 8 | Compare with the start. |
| hs1-990 | Noor + Omar | 30 | What you can now do; four actions to finish this week. |

Estimated narration total: ~19 minutes of audio inside ~55 minutes of seat time.

## 2. Lexicon used

From `../00_program/narration-and-lexicon.md`: CBAHI, MOH, ISO 45001, FMS, OHS, EHS, AREC, ERT, RRT, RACE, PASS, CO₂, GHS, NFPA, SDS, PPE, PPM, UPS, HVAC, RO, MRI, CT, ALARA, OSL, RSO, mSv, mL.

## 3. Asset manifest

All diagrams are authored SVG (`svg_to_asset`); real text in HTML wherever possible. Source = provenance `source` value.

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| hs1-img-8plans | SVG icon grid | hs1-102 | 4×2 grid, one line icon per plan, label under each; hotspot rects per tile | own | "Eight Facility Management and Safety plans shown as icons." |
| hs1-img-arec | SVG cycle | hs1-203 | 4-stage circular arrow, brand colours | own | "AREC cycle: Anticipate, Recognise, Evaluate, Control." |
| hs1-img-ert | SVG diagram | hs1-305 | Incident Commander centre, 5 team nodes | own | "Emergency Response Team: Safety, Security, Nursing, Facility, Operation." |
| hs1-img-triangle | SVG | hs1-401 | Fire triangle with three labelled sides | own | "Fire triangle: heat, fuel and oxygen." |
| hs1-img-corridor | illustration | hs1-404 | Clinic corridor with 8 identifiable equipment items; each item ≥ 48 px at stage size | ai-generated (reviewed) or own | "Clinic corridor with fire safety equipment." |
| hs1-img-ghs-1..9 | SVG pictograms | hs1-502 | 9 GHS pictograms redrawn (red diamond, black symbol) | own / public-domain (UN GHS) | name of each pictogram |
| hs1-img-nfpa-blank | SVG | hs1-503 | Generic NFPA 704 diamond, quadrants without labels | own | "Empty NFPA hazard diamond with four quadrants." |
| hs1-img-nfpa-301w | SVG | hs1-504 | Diamond with 3/0/1/W | own | "NFPA diamond: health 3, flammability 0, reactivity 1, special W." |
| hs1-img-eyewash | photo | hs1-506 | Own photo of a My Clinic eyewash/shower unit | own (with permission) | "Combined eyewash and emergency shower station." |
| hs1-img-treatment-room | illustration | hs1-701 | Room with sockets, UPS monitor, extension, valve, vent | ai-generated (reviewed) | "Treatment room showing sockets, a valve and an air vent." |
| hs1-img-pump-label | illustration | hs1-802 | Infusion pump with an overdue inspection label (fictional dates) | ai-generated (reviewed) | "Infusion pump with an overdue inspection label." |
| hs1-img-alara | SVG | hs1-903 | Source icon with time/distance/shield labels | own | "ALARA: time, distance, shielding." |
| hs1-img-codes-chips | SVG set | hs1-301 | 11 colour chips with code names printed | own | (decorative — name is in text) |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |
| hs1-aud-* | narration audio | all narrated screens | One MP3 per segment, file names from `export_audio_script` | ai-generated (TTS) | transcript = `narration_text` |

**Rights check:** if the 199 PDF images are confirmed as My Clinic-owned (Phase 0), the GHS chart and code poster can be used as `local` instead of being redrawn.

## 4. Activity plans (for `lint_authoring_plan`)

| Activity | Objective | Rules | Success | Failure / retry | Keyboard alternative |
|---|---|---|---|---|---|
| hs1-205 corridor | hs1-o2 | 3 nodes, each choice has `score_delta` +1 for the best choice, 0 otherwise | ≥ 2 | Replay allowed; score counted once | Choices are buttons |
| hs1-409 night fire | hs1-o4 | 4 nodes, branching on "fire grows" | ≥ 3 | Replay | Buttons |
| hs1-507 spills | hs1-o5 | 3 cases + steps | ≥ 3 of 4 | Replay | Buttons |
| hs1-802 pump | hs1-o8 | 4 nodes | ≥ 3 | Replay | Buttons |
| hs1-950 capstone game | hs1-o10 | `case_sim`, score, 3 lives, 1 hint per node, no timer; rule: `when wrong if lives==0 then goto debrief` | `pass_score` 2 (best choice on 2 of 3 nodes) | Lives exhausted → debrief → retry | All nodes are choice buttons; hints are text |
| Drag-and-drop (405, 508) | o4, o5 | each item one target | all correct for full points (partial scoring if supported) | Retry | Keyboard pick-and-place supported by the player |

## 5. Approval request (end of Phase 3)

Show the SME and course owner, as tables (not raw JSON):
1. The storyboard (Phase 2) with any changes since review.
2. `voice_talent.md` from `export_audio_script` + one sample audio file.
3. Approved companion masters (Noor, Dr. Omar) + one scenario illustration.
4. The four scenario scripts (choices + feedback text).

Record the approval in Phase 5 §4. No audio or illustration production until approved.
