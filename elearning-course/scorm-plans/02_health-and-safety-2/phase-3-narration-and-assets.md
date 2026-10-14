# Phase 3 — Narration & assets (02 Safety in Practice)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Noor** (narrates every narrated screen unless listed below). **Co-host: Dr. Omar**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| hs2-000 | Noor | `char-noor-welcome` | L1 half-body bottom-right | Noor | Welcomes learners to the lab |
| hs2-011 | Noor | `char-noor-avatar-neutral + tip card` | L3 tip card | Noor | Blocked-exit story (companions.md §1) |
| hs2-030 | Noor + Omar | `char-noor-avatar (host); char-omar-avatar (node 2)` | L5 avatar | Noor + Omar | Code Red drill: Noor hosts; Omar is the colleague making the alarm call in node 2 |
| hs2-052 | Omar | `char-omar-avatar-neutral → -happy / -concern` | L5 avatar | Omar | Spill triage host |
| hs2-064 | Noor | `char-noor-tip (hints)` | L5 avatar beside hint text | Noor | Gives the escape-room hints |
| hs2-090 | Noor + Omar | `char-noor-success + char-omar-avatar-happy` | L6 | Noor + Omar | Two-voice close |

- Visible on 6 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `NOOR:` / `OMAR:`; two-voice screens are split into one segment per line (`part` = `noor-1`, `omar-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.

## 1. Narration outline

| Screen | Speaker | Sec | Narration intent |
|---|---|---|---|
| hs2-000 | Noor | 12 | This is a lab: you'll try things first and learn from the feedback. |
| hs2-001 | Noor | 20 | Safety is the habits that protect life, health and environment; today you practise them. |
| hs2-010 | Noor | 45 | Walk through the wet-floor example aloud; explain why likelihood and impact are scored separately. |
| hs2-011 | Noor | 15 | Set up the store room; there are six hazards; open them all. Noor's story: "I walked past a blocked exit for a week before I noticed it." |
| hs2-012 / 013 | Noor | 8 each | Set up. |
| hs2-020 | Noor | 25 | The poster on the wall is bilingual; learn both names; check your site's extensions. |
| hs2-030 | Noor + Omar | 20 | Set up the drill scene; there is no timer, but in real life seconds matter. |
| hs2-031 / 032 | Noor | 8 each | Set up. |
| hs2-033 | Noor | 25 | Inside vs outside assembly points; find your unit's plan today. |
| hs2-040 | Noor | 20 | Before you need it, know how to read the label and check the gauge. |
| hs2-041 | Noor | 8 | Set up. |
| hs2-050 | Noor | 25 | HAZMAT is chemical or biological; one clear rule decides Code Orange. |
| hs2-051 | Noor | 15 | Two kits, two colours, two jobs. |
| hs2-052 / 053 | Noor | 8 each | Set up. |
| hs2-060 | Noor | 35 | Read a register row left to right: what it is, why it's here, is the SDS on file, what the diamond says. |
| hs2-061 / 062 / 063 | Noor | 8 each | Set up. |
| hs2-064 | Noor | 15 | The store is locked; four checks open it; everything you need is in this module. |
| hs2-070 | Noor | 8 | Set up. |
| hs2-080 | Noor | 12 | Read your results. |
| hs2-081 | Noor | 8 | Invite one commitment. |
| hs2-090 | Noor + Omar | 20 | What you can now do; who to call. |

Estimated audio: ~8 minutes.

## 2. Lexicon used

HAZMAT ("haz-mat"), GHS, NFPA, SDS, PPE, RACE, PASS, CO₂, mL, EHS, BME ("Biomedical Engineering").

## 3. Asset manifest

**No image from `Health & Safety 2.pdf` is reused until D12/B3 is closed.**

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| hs2-img-storeroom | illustration | hs2-011 | Store room / office with exactly 6 hazards from the answer key, each clearly visible at stage size; no other accidental hazards | ai-generated (reviewed against key) | "Store room with several workplace hazards." |
| hs2-img-codes | SVG chips | hs2-020 | 12 cards, EN + AR text in HTML, colour chip SVG only | own | decorative chip |
| hs2-img-drill-1..6 | illustrations | hs2-030 | One scene per node: smoke in room; call point; O₂ cylinder + alcohol rub; small bin fire / spreading fire; stairwell with evacuation chair; assembly point | ai-generated (same style set) | per scene |
| hs2-img-floorplan | SVG | hs2-032 | Generic single-floor plan, Zones A–E, legend icons, "you are here" marker | own | "Generic evacuation floor plan with zones A to E." |
| hs2-img-extinguisher | photo | hs2-040 | My Clinic dry-powder extinguisher, label legible, 3:4 crop | own (permission) | "Dry-powder fire extinguisher with its label." |
| hs2-img-kit-chem / hs2-img-kit-bio | photos | hs2-051 | Real My Clinic kits, same angle and size | own | "Red chemical spill kit." / "Yellow biological spill kit." |
| hs2-img-register | HTML table | hs2-060, 062, 063, 064 | Rebuilt from the anonymised register (B5); real text, not a screenshot | own | n/a (HTML) |
| hs2-img-nfpa-230 | SVG | hs2-063, 064 | Diamond 2-3-0 | own | "NFPA diamond: health 2, flammability 3, reactivity 0." |
| hs2-img-ghs-1..9 | SVG | hs2-061 | Reuse module 01 assets `hs1-img-ghs-*` | own | names |
| hs2-img-spill-photo | illustration | hs2-064 | Spill with a measuring cue (e.g. a 1 L bottle on its side, more than half gone) | ai-generated | "Large disinfectant spill from a one-litre bottle." |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |
| hs2-aud-* | audio | narrated screens | TTS per segment | ai-generated | transcript |

## 4. Activity plans

| Activity | Objective | Rules | Success | Failure / retry | Accessibility |
|---|---|---|---|---|---|
| hs2-030 Code Red drill | hs2-o2 | 6 nodes; `score_delta` +1 per correct RACE choice; 2 lives; 1 hint per node; no timer | ≥ 5 of 6 | Lives at 0 → debrief → restart | Buttons; every scene has alt text; hints are text |
| hs2-064 escape room | hs2-o6 | 4 sequential puzzles, text answers with aliases, 3 lives, 1 hint each | all 4 solved | Lives at 0 → debrief → retry | Text input; all clues on screen as text (register in HTML, diamond numbers in alt text) |
| hs2-052 spill triage | hs2-o5 | 3 nodes | ≥ 3 correct | Replay | Buttons |

Escape-room puzzle answers must be **derivable from what is on screen** (playbook rule): the register and diamond are shown inside the puzzle prompt.

## 5. Approval request

Show: storyboard; the **store-room answer key + illustration**; all six drill scenes; escape-room puzzles, answers, hints and debrief; voice sample. Record in Phase 5 §4.
