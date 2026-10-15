# Voice-over script — MC08-ehr-consultation

Language: en · Pace: ~140 wpm · Two voices: **Dr. Omar** (lead host) and **Noor** (co-host) — [`companions.md`](../../00_program/characters/companions.md) §5.

## Voices

| Voice | Brief | Lines in this module | Provider / voice id |
|---|---|---|---|
| **Dr. Omar** (`OMAR:`) | Male, late 30s, friendly, confident and relaxed; international English with a light Gulf Arabic accent welcome; medium-low pitch; ~140 wpm | 19 | Pending program **D10** |
| **Noor** (`NOOR:`) | Female, early-to-mid 30s, warm, calm and clear; international English with a light Gulf Arabic accent welcome; smiling but not bubbly; ~140 wpm | 1 | Pending program **D10** |

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
| 1 | `ehr-000` | omar | warm | OMAR: Welcome to EHR Consultation Workflow: Guided Simulation. You will practise decisions that help you act with confidence. You will leave with practical actions for your next shift. | 12.0 | `MC08-ehr-consultation_ehr-000.mp3` |
| 2 | `ehr-001` | omar | calm, practical | OMAR: Complete, specific, linked — on the day. Read the disclaimer. | 4.3 | `MC08-ehr-consultation_ehr-001.mp3` |
| 3 | `ehr-002` | omar | calm, practical | OMAR: The nine steps at a glance. | 3.0 | `MC08-ehr-consultation_ehr-002.mp3` |
| 4 | `ehr-010` | omar | encouraging | OMAR: Start from today's list. Work through the steps in order, then read the feedback. | 6.4 | `MC08-ehr-consultation_ehr-010.mp3` |
| 5 | `ehr-011` | omar | calm, practical | OMAR: The mandatory sections. Save as you go. | 3.4 | `MC08-ehr-consultation_ehr-011.mp3` |
| 6 | `ehr-012` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC08-ehr-consultation_ehr-012.mp3` |
| 7 | `ehr-020` | omar | encouraging | OMAR: Search by code or name. The primary diagnosis drives everything after it. My first week, I typed 'diabetes' and picked the first line. It wasn't the one I meant. Work through the steps in order, then read the feedback. | 17.1 | `MC08-ehr-consultation_ehr-020.mp3` |
| 8 | `ehr-030` | omar | calm, practical | OMAR: Five ways to find an order. The Form Wizard checks a package before you commit. | 6.9 | `MC08-ehr-consultation_ehr-030.mp3` |
| 9 | `ehr-031` | omar | encouraging | OMAR: Link every medication to the diagnosis you assessed. Work through the steps in order, then read the feedback. | 8.1 | `MC08-ehr-consultation_ehr-031.mp3` |
| 10 | `ehr-032` | omar | encouraging | OMAR: Review the package. Remove what you don't need. Work through the steps in order, then read the feedback. | 8.1 | `MC08-ehr-consultation_ehr-032.mp3` |
| 11 | `ehr-033` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC08-ehr-consultation_ehr-033.mp3` |
| 12 | `ehr-034` | omar | encouraging | OMAR: Decide as you would on shift, then read the feedback. | 4.7 | `MC08-ehr-consultation_ehr-034.mp3` |
| 13 | `ehr-040` | omar | encouraging | OMAR: The summary is the record the patient takes home. Work through the steps in order, then read the feedback. | 8.6 | `MC08-ehr-consultation_ehr-040.mp3` |
| 14 | `ehr-041` | omar | encouraging | OMAR: Education by SMS, matched to the diagnosis code. Work through the steps in order, then read the feedback. | 8.1 | `MC08-ehr-consultation_ehr-041.mp3` |
| 15 | `ehr-042` | noor | calm, practical | NOOR: Patient & family education is required before you finish. | 3.9 | `MC08-ehr-consultation_ehr-042.mp3` |
| 16 | `ehr-050` | omar | encouraging | OMAR: Internal referral and follow-up. Work through the steps in order, then read the feedback. | 6.4 | `MC08-ehr-consultation_ehr-050.mp3` |
| 17 | `ehr-051` | omar | encouraging | OMAR: Put the steps in the order you would follow at work, then read the feedback. | 6.9 | `MC08-ehr-consultation_ehr-051.mp3` |
| 18 | `ehr-052` | omar | calm, practical | OMAR: Completing the encounter. Where to get help. | 3.4 | `MC08-ehr-consultation_ehr-052.mp3` |
| 19 | `ehr-090` | omar | supportive | OMAR: Your results are organised by objective. Notice where you were confident, then revisit any section that needs another practical try. | 9.0 | `MC08-ehr-consultation_ehr-090.mp3` |
| 20 | `ehr-091` | omar | confident | OMAR: You can now use these key actions in your role. Keep the practical rule close, ask when you are unsure, and carry the next step into your shift. Take one clear next action with you. | 15.4 | `MC08-ehr-consultation_ehr-091.mp3` |
