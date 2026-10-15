# Voice-over script — MC05-rcm-documentation-coding

Language: en · Pace: ~140 wpm · Two voices: **Dr. Omar** (lead host) and **Noor** (co-host) — [`companions.md`](../../00_program/characters/companions.md) §5.

## Voices

| Voice | Brief | Lines in this module | Provider / voice id |
|---|---|---|---|
| **Dr. Omar** (`OMAR:`) | Male, late 30s, friendly, confident and relaxed; international English with a light Gulf Arabic accent welcome; medium-low pitch; ~140 wpm | 20 | Pending program **D10** |
| **Noor** (`NOOR:`) | Female, early-to-mid 30s, warm, calm and clear; international English with a light Gulf Arabic accent welcome; smiling but not bubbly; ~140 wpm | 2 | Pending program **D10** |

Neither voice may be cloned from, or resemble, a real My Clinic employee. Record a 30-second sample of each voice reading a “meet your guide” line for approval before producing this module. Once D10 closes, record the provider and voice ids in `00_program/narration-and-lexicon.md` §1 and in `narration-script.json` → `voice`.

The speaker label (`OMAR:` / `NOOR:`) selects the voice and is **not** spoken; `tts_text` in [`audio-script-export.json`](audio-script-export.json) already has it removed and the lexicon applied. Two-voice screens are recorded as one file per `part` and joined with 0.3 s of silence (companions.md §5).

## Pronunciation guide

- **ALARA** → ah-LAR-ah
- **AREC** → A-R-E-C
- **BME** → Biomedical Engineering
- **BMI** → B-M-I
- **CBAHI** → see-bah-hee
- **CCHI** → C-C-H-I
- **CDI** → C-D-I
- **CHI** → C-H-I
- **EBP** → E-B-P
- **EHR** → E-H-R
- **ERT** → E-R-T
- **FMS** → F-M-S
- **GHS** → G-H-S
- **HAZMAT** → haz-mat
- **HPI** → history of present illness
- **ICD** → I-C-D
- **ICD-10** → I-C-D ten
- **KPI** → K-P-I
- **MOH** → M-O-H
- **NFPA** → N-F-P-A
- **OHS** → O-H-S
- **PASS** → pass
- **PPE** → P-P-E
- **PXO** → patient experience officer
- **RACE** → race
- **RCM** → R-C-M
- **RSO** → R-S-O
- **SAR** → Saudi riyals
- **SCORM** → scorm
- **SDS** → S-D-S
- **SMS** → S-M-S
- **TAT** → turnaround time

## Recording table

| # | Screen / part | Speaker | Tone | Script | Est. sec | File |
|---|---|---|---|---|---|---|
| 1 | `rcma-000` | omar | warm | OMAR: Welcome to RCM Part A: Documentation & Coding. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift. | 12.0 | `MC05-rcm-documentation-coding_rcma-000.mp3` |
| 2 | `rcma-001` | omar | calm, practical | OMAR: The reviewer only has your note. Good documentation protects the patient, you and the clinic. | 6.9 | `MC05-rcm-documentation-coding_rcma-001.mp3` |
| 3 | `rcma-002` | omar | reflective | OMAR: This reflection is not scored. Choose the response that helps you set one intention for your next shift. | 8.1 | `MC05-rcm-documentation-coding_rcma-002.mp3` |
| 4 | `rcma-010` | omar | calm, practical | OMAR: What always goes in, what never should. | 3.4 | `MC05-rcm-documentation-coding_rcma-010.mp3` |
| 5 | `rcma-011` | noor | calm, practical | NOOR: Same patient, same fluids. One note gets paid. | 3.9 | `MC05-rcm-documentation-coding_rcma-011.mp3` |
| 6 | `rcma-012` | omar | encouraging | OMAR: Put the steps in the order you would follow at work, then read the feedback. | 6.9 | `MC05-rcm-documentation-coding_rcma-012.mp3` |
| 7 | `rcma-013` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC05-rcm-documentation-coding_rcma-013.mp3` |
| 8 | `rcma-020` | omar | calm, practical | OMAR: Coding is clinical translation. Specific codes get accepted. | 3.9 | `MC05-rcm-documentation-coding_rcma-020.mp3` |
| 9 | `rcma-021` | omar | encouraging | OMAR: Match each item to the person or step that owns it, then read the feedback. | 6.9 | `MC05-rcm-documentation-coding_rcma-021.mp3` |
| 10 | `rcma-022` | omar | calm, practical | OMAR: Follow the example one step at a time, then identify why the next step makes sense. | 7.3 | `MC05-rcm-documentation-coding_rcma-022.mp3` |
| 11 | `rcma-023` | omar | encouraging | OMAR: Place each item where it belongs, then read the feedback. | 4.7 | `MC05-rcm-documentation-coding_rcma-023.mp3` |
| 12 | `rcma-030` | omar | calm, practical | OMAR: Defensive medicine feels safe but gets rejected. Follow work-up protocols, document deviations. | 5.6 | `MC05-rcm-documentation-coding_rcma-030.mp3` |
| 13 | `rcma-031` | omar | encouraging | OMAR: Play the situation through and decide, then read the feedback. | 4.7 | `MC05-rcm-documentation-coding_rcma-031.mp3` |
| 14 | `rcma-032` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC05-rcm-documentation-coding_rcma-032.mp3` |
| 15 | `rcma-033` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC05-rcm-documentation-coding_rcma-033.mp3` |
| 16 | `rcma-040` | omar | encouraging | OMAR: Let's check your earlier guess. Place each item where it belongs, then read the feedback. | 6.9 | `MC05-rcm-documentation-coding_rcma-040.mp3` |
| 17 | `rcma-041` | omar | calm, practical | OMAR: Coverage changes often. Part B covers what's new. | 3.9 | `MC05-rcm-documentation-coding_rcma-041.mp3` |
| 18 | `rcma-042` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC05-rcm-documentation-coding_rcma-042.mp3` |
| 19 | `rcma-050/omar-1` | omar | encouraging | OMAR: Three notes, your pen. Play the round, then read the feedback. | 5.1 | `MC05-rcm-documentation-coding_rcma-050_omar-1.mp3` |
| 20 | `rcma-050/noor-1` | noor | encouraging | NOOR: That is the habit we want from every new colleague. | 4.7 | `MC05-rcm-documentation-coding_rcma-050_noor-1.mp3` |
| 21 | `rcma-090` | omar | supportive | OMAR: Your results are organised by objective. Notice where you were confident, then revisit any section that needs another practical try. | 9.0 | `MC05-rcm-documentation-coding_rcma-090.mp3` |
| 22 | `rcma-091` | omar | confident | OMAR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you. | 15.4 | `MC05-rcm-documentation-coding_rcma-091.mp3` |
