# Narration standards and master lexicon (all modules)

Playbook topics: `narration`, `audio`, `characters` · Gates: `lint_narration_script`, `export_audio_script`

## 1. Voice route

| Route | Use for | Decision needed in Phase 0 |
|---|---|---|
| **External English TTS** (premium neural voice) → `add_asset` | Release 1 of all modules | Provider, voice id, licence for commercial training use |
| **Human voice talent** using `voice_talent.md` from `export_audio_script` | Optional for 03 (HR welcome) and 07 (Quality) if leadership wants a human voice | Budget, consent form |
| Server Piper TTS | **Not for release 1.** The Docker image ships a Turkish voice only | — |

Whatever the route: **two fixed voices for all eight packages**, one for each companion, and `normalize_audio_asset` on every file so loudness matches.

| Companion | Voice brief | Leads |
|---|---|---|
| **Noor** (`noor`) | Female, early-to-mid 30s, warm, calm, clear; international English, light Gulf Arabic accent welcome; ~140 wpm | 01, 02, 07 |
| **Dr. Omar** (`omar`) | Male, late 30s, friendly, confident, relaxed; international English, light Gulf Arabic accent welcome; medium-low pitch; ~140 wpm | 03, 04, 05, 06, 08 |

Provider and voice ids are recorded here when decision D10 is closed. Approve a 30-second sample of each voice before producing any module. Full rules: [`characters/companions.md`](characters/companions.md) §5.

Do **not** reuse the Quality video's narration voice. It may be synthetic and its consent status is unknown (module 07 source note 5).

## 2. Writing rules (from the playbook, applied)

1. Write for the ear: sentences of 25 words or fewer, contractions, one idea per sentence.
2. Talk to one person ("you"), present tense, active voice. Persona: an experienced colleague on your first week — in practice, the module's lead companion (Noor or Dr. Omar).
3. The screen shows keywords; the narration explains. Never read the screen word for word.
4. No interface talk ("click Next", "as you can see on this slide").
5. First screen of each module says why it matters on the job. Last screen says what you can now do.
6. Question screens: set up the situation and stop. Never narrate the answer. Feedback goes in the screen's feedback fields.
7. Pace: **140 words per minute** (English). Each segment under 60 seconds; split longer ones.
8. Human vulnerability where it fits: the companions (Noor, Dr. Omar) can admit a past mistake — see the honest stories in `characters/companions.md` §1 ("In my first month I nearly…"). Keep it short and real, never dramatic about patient harm.
9. **Never pad.** A screen's script is as long as its content needs to be; the Phase 3 `target_sec` is a planning estimate, not a quota. Sentences that only restate the prompt, the buttons or the next task are the G11 defect removed on 2026-10-15 — do not reintroduce them. Where a draft is materially under target it is listed in that module's [`storyboard/narration-gaps.md`](../01_health-and-safety-1/storyboard/narration-gaps.md) for authored prose (and SME confirmation) instead of filler.

## 3. Markup

- `[[cue:id]]` — intended reveal of a screen element (must exist in the screen's `cue_targets`). An estimate, not a guaranteed timing.
- `[[pause:1.0]]` — silence in seconds.

## 4. Master pronunciation lexicon

Every module copies the entries it uses into its `narration-script.json`. Add new acronyms here first.

| Term | Say it as | Modules |
|---|---|---|
| Noor | "noor" (rhymes with *tour*) | all |
| Omar | "OH-mar" | all |
| CBAHI | "see-bah-hee" (confirm local usage) | 01, 03 |
| MOH | "M-O-H" | 01, 02, 06 |
| ISO 45001 | "I-S-O forty-five thousand and one" | 01 |
| FMS | "F-M-S" | 01 |
| OHS | "O-H-S" | 01 |
| EHS | "E-H-S" | 01 |
| AREC | "A-R-E-C" | 01 |
| ERT | "E-R-T" | 01 |
| RRT | "R-R-T" | 01 |
| RACE | "race" | 01, 02 |
| PASS | "pass" | 01, 02 |
| CO₂ | "C-O-two" | 01, 02 |
| GHS | "G-H-S" | 01, 02 |
| NFPA | "N-F-P-A" | 01, 02 |
| SDS | "S-D-S" | 01, 02 |
| PPE | "P-P-E" | 01, 02 |
| PPM | "P-P-M" | 01 |
| UPS | "U-P-S" | 01 |
| HVAC | "H-vac" | 01 |
| RO | "R-O" | 01 |
| MRI | "M-R-I" | 01 |
| CT | "C-T" | 01 |
| ALARA | "ah-LAR-ah" | 01 |
| OSL | "O-S-L" | 01 |
| RSO | "R-S-O" | 01 |
| mSv | "millisieverts" | 01 |
| mL | "millilitres" | 01, 02 |
| GOSI | "GO-see" | 03 |
| SCFHS | "S-C-F-H-S" | 03 |
| Mumaris | "mu-MAH-ris" | 03 |
| Qiwa | "KEE-wa" | 03 |
| HRMS | "H-R-M-S" | 03 |
| SAR | "Saudi riyals" | 03, 05, 06 |
| HHC | "home health care" | 03, 04 |
| PXO | "patient experience officer" | 04 |
| FM | *expand after Phase 0 (not defined in source)* | 04 |
| DMP | *expand after Phase 0* | 04 |
| CHP | *expand after Phase 0* | 04 |
| VIP | "V-I-P" | 04 |
| RCM | "R-C-M" | 05, 06 |
| CDI | "C-D-I" | 05 |
| HPI | "history of present illness" | 05 |
| ICD-10 | "I-C-D ten" | 05, 06, 08 |
| CCHI / CHI | *one form only, decided in Phase 0* | 05, 06 |
| EBP | "E-B-P" | 06 |
| BMI | "B-M-I" | 05, 06 |
| HbA1c | "H-B-A-one-C" | 05, 08 |
| PCOS | "P-C-O-S" | 05 |
| FIT | "fit" | 06 |
| DEXA | "DEX-ah" | 06 |
| Tdap | "T-dap" | 06 |
| PCV13 / PPSV23 | "P-C-V thirteen" / "P-P-S-V twenty-three" | 06 |
| PTSD | "P-T-S-D" | 06 |
| IPSG | "I-P-S-G" | 07 |
| FOCUS-PDCA | "focus, P-D-C-A" | 07 |
| MRN | "medical record number" | 07, 08 |
| EHR | "E-H-R" | 08 |
| CBC | "C-B-C" | 08 |
| TSH | "T-S-H" | 08 |
| ECG | "E-C-G" | 08 |
| SMS | "S-M-S" | 08 |
| E11 | "E eleven" | 05, 08 |

ICD-10 codes are spoken letter-by-letter plus number, e.g. K52 → "K fifty-two".

## 5. Companion characters

Two fictional guides appear in every course: **Noor** (senior staff nurse and patient-safety liaison) and **Dr. Omar** (family physician and onboarding champion). Their identity, look, poses, assets, voices, speaking rules, honest stories and per-module plan are in **[`characters/companions.md`](characters/companions.md)**.

Script rules in short:
- The module's **lead host narrates** every narrated screen; the co-host speaks only where the module's Phase 3 companion table says so.
- Prefix every line `NOOR:` or `OMAR:`. Two-voice screens: one segment per line (`part` = `noor-1`, `omar-1`, …), joined into one audio file per screen with 0.3 s gaps, then normalised.
- `narration_text` keeps the speaker names for captions and transcripts.
- Lexicon: **Noor** → "noor" (rhymes with *tour*); **Omar** → "OH-mar".
