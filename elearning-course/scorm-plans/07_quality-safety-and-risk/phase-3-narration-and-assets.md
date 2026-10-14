# Phase 3 — Narration & assets (07 Clinical Governance)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 1. Narration source

Write **new** narration from the corrected transcript (Phase 0 B1) and the confirmed policies. Do not copy the video's sentences or voice. Keep the video's strongest lines as quotes where confirmed: "Doing the right things right, the first time and every time" and "When you see something, say something".

## 2. Narration outline

| Screen | Sec | Narration intent |
|---|---|---|
| qsr-000 | 12 | Welcome; this is how My Clinic protects patients every day. |
| qsr-001 | 25 | The standard: precision from the start, not "good enough". |
| qsr-002 | 10 | Invite an honest, anonymous answer. |
| qsr-010 | 35 | Quality is measured in three linked layers; good data shows real performance. |
| qsr-011 / 012 | 8 each | Set up. |
| qsr-020 | 30 | Six goals, each prevents a known type of harm; open each one. |
| qsr-021 | 15 | Set up two patients with the same name. Mentor: "I once nearly drew blood from the wrong Mr Al-Harbi. The wristband stopped me." |
| qsr-022 / 023 | 8 each | Set up. |
| qsr-030 | 8 | Set up. |
| qsr-031 | 40 | Talk through the fridge example: impact, likelihood, score, response. |
| qsr-032 / 033 | 8 each | Set up. |
| qsr-040 | 35 | The iceberg: what we see is the smallest part; near misses are free lessons. |
| qsr-041 / 042 | 8 each | Set up. |
| qsr-050 | 35 | What to report, by when, how; after you submit, the system takes over. |
| qsr-051 | 15 | Set up the end-of-shift scene. |
| qsr-090 | 10 | Read your results. |
| qsr-091 | 8 | Invite the commitment. |
| qsr-092 | 20 | You're the final layer of protection. |

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
| qsr-char-noor | character | qsr-021, 051 | Mentor: explaining, concern, success | ai-generated | per pose |
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
