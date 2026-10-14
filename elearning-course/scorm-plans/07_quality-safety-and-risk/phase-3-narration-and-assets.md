# Phase 3 — Narration & assets (07 Clinical Governance)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 1. Narration source

Write **new** narration from the corrected transcript (Phase 0 B1) and the confirmed policies. Do not copy the video's sentences or voice. Keep the video's strongest lines as quotes where confirmed: "Doing the right things right, the first time and every time" and "When you see something, say something".

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Noor** (narrates every narrated screen unless listed below). **Co-host: Dr. Omar**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| qsr-000 | Noor | `char-noor-welcome` | L1 half-body bottom-right | Noor | Welcome |
| qsr-002 | Noor | `char-noor-listening` | L4 beside the poll | Noor | Speak-up story before the anonymous poll (companions.md §1) |
| qsr-021 | Noor | `char-noor-avatar-concern → -happy` | L5 avatar | Noor | "Which Mohammed?" story and scenario |
| qsr-031 | Omar | `char-omar-thinking` | L3 right column | Omar | Talks through the risk-matrix worked example |
| qsr-040 | Omar | `char-omar-avatar-neutral + tip card` | L3 tip card | Omar | Tip: report the near miss — it is free learning |
| qsr-051 | Noor | `char-noor-avatar-neutral → -happy / -concern` | L5 avatar | Noor | End-of-shift reporting scenario |
| qsr-092 | Noor + Omar | `char-noor-success + char-omar-avatar-happy` | L6 | Noor + Omar | Two-voice close: "When you see something, say something." |

- Visible on 7 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `NOOR:` / `OMAR:`; two-voice screens are split into one segment per line (`part` = `noor-1`, `omar-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.

## 2. Narration outline

| Screen | Speaker | Sec | Narration intent |
|---|---|---|---|
| qsr-000 | Noor | 12 | Welcome; this is how My Clinic protects patients every day. |
| qsr-001 | Noor | 25 | The standard: precision from the start, not "good enough". |
| qsr-002 | Noor | 10 | Invite an honest, anonymous answer. |
| qsr-010 | Noor | 35 | Quality is measured in three linked layers; good data shows real performance. |
| qsr-011 / 012 | Noor | 8 each | Set up. |
| qsr-020 | Noor | 30 | Six goals, each prevents a known type of harm; open each one. |
| qsr-021 | Noor | 15 | Set up two patients with the same name. Noor's story: "I once nearly drew blood from the wrong Mr Al-Harbi. The wristband stopped me." |
| qsr-022 / 023 | Noor | 8 each | Set up. |
| qsr-030 | Noor | 8 | Set up. |
| qsr-031 | Omar | 40 | Talk through the fridge example: impact, likelihood, score, response. |
| qsr-032 / 033 | Noor | 8 each | Set up. |
| qsr-040 | Omar | 35 | The iceberg: what we see is the smallest part; near misses are free lessons. |
| qsr-041 / 042 | Noor | 8 each | Set up. |
| qsr-050 | Noor | 35 | What to report, by when, how; after you submit, the system takes over. |
| qsr-051 | Noor | 15 | Set up the end-of-shift scene. |
| qsr-090 | Noor | 10 | Read your results. |
| qsr-091 | Noor | 8 | Invite the commitment. |
| qsr-092 | Noor + Omar | 20 | You're the final layer of protection. |

Estimated audio: ~7 minutes.

## 3. Lexicon used

IPSG, FOCUS-PDCA, MRN, DOB ("date of birth"), JCI, CBAHI, WHO ("W-H-O").

## 4. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| qsr-img-quote | SVG/typography | qsr-001 | Quote on brand background, no imagery | own | n/a (text in HTML) |
| qsr-img-spo | SVG | qsr-010 | Three linked blocks | own | "Structure leads to processes, which lead to outcomes." |
| qsr-img-pillars | illustration | qsr-020 | Six pillars with numbered icons (ID band, speech bubble, red-label vial, surgical checklist, hands, yellow band) — **no NotebookLM frames reused** | ai-generated / own | "Six patient safety goals as six pillars." |
| qsr-img-wristbands | illustration | qsr-021 | Two wristbands with the same name, different MRN and DOB (fictional data) | ai-generated | "Two patient wristbands with the same name and different record numbers." |
| qsr-img-matrix | SVG | qsr-031, 032 | 5×5 matrix, band colours **and** band names in every cell (B6) | own | "Risk matrix: impact by likelihood, scores 1 to 25." |
| qsr-img-iceberg | SVG | qsr-040 | Iceberg with three labelled layers | own | "Iceberg: critical incidents at the tip, adverse events below, near misses at the base." |
| qsr-vid-speakup *(optional)* | video + VTT | qsr-060 | ≤ 60 s, recorded in-house, consent on file, captions | own | transcript |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Noor, the safety liaison, explaining." |
| qsr-aud-* | audio | narrated screens | TTS | ai-generated | transcript |

The 107 screenshots in `media/07_quality-safety-risk/` are **reference only** (layout ideas); none are packaged.

## 5. Activity plans

| Activity | Objective | Rules | Success | Accessibility |
|---|---|---|---|---|
| qsr-021 identification | qsr-o2 | 3 nodes | ≥ 2 best | buttons; wristband data repeated in text |
| qsr-051 end of shift | qsr-o5 | 3 nodes | all best | buttons |
| qsr-011 / 041 sorts | o1 / o4 | 7 / 6 items | all correct | keyboard |

## 6. Approval request

Quality Director and Patient Safety Officer approve the storyboard, the corrected narration, the matrix image and both scenarios. If `qsr-060` is used, approve the clip and captions.
