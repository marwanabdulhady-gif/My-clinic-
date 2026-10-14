# Narration standards and master lexicon (all modules)

Playbook topics: `narration`, `audio`, `characters` · Gates: `lint_narration_script`, `export_audio_script`

## 1. Voice route

| Route | Use for | Decision needed in Phase 0 |
|---|---|---|
| **External English TTS** (premium neural voice) → `add_asset` | Release 1 of all modules | Provider, voice id, licence for commercial training use |
| **Human voice talent** using `voice_talent.md` from `export_audio_script` | Optional for 03 (HR welcome) and 07 (Quality) if leadership wants a human voice | Budget, consent form |
| Server Piper TTS | **Not for release 1.** The Docker image ships a Turkish voice only | — |

Whatever the route: one voice for all eight packages, and `normalize_audio_asset` on every file so loudness matches.

Do **not** reuse the Quality video's narration voice. It may be synthetic and its consent status is unknown (module 07 source note 5).

## 2. Writing rules (from the playbook, applied)

1. Write for the ear: sentences of 25 words or fewer, contractions, one idea per sentence.
2. Talk to one person ("you"), present tense, active voice. Persona: an experienced colleague on your first week.
3. The screen shows keywords; the narration explains. Never read the screen word for word.
4. No interface talk ("click Next", "as you can see on this slide").
5. First screen of each module says why it matters on the job. Last screen says what you can now do.
6. Question screens: set up the situation and stop. Never narrate the answer. Feedback goes in the screen's feedback fields.
7. Pace: **140 words per minute** (English). Each segment under 60 seconds; split longer ones.
8. Human vulnerability where it fits: the mentor can admit a past mistake ("In my first month I nearly…"). Keep it short and real, never dramatic about patient harm.

## 3. Markup

- `[[cue:id]]` — intended reveal of a screen element (must exist in the screen's `cue_targets`). An estimate, not a guaranteed timing.
- `[[pause:1.0]]` — silence in seconds.

## 4. Master pronunciation lexicon

Every module copies the entries it uses into its `narration-script.json`. Add new acronyms here first.

| Term | Say it as | Modules |
|---|---|---|
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

## 5. Characters (optional, shared)

| Id | Role | Identity | Variants |
|---|---|---|---|
| `mentor-noor` | Coach / narrator persona | Fictional senior nurse and safety liaison, Saudi woman in her 30s, navy scrubs, plain navy hijab, plain ID badge with no logo or text, purple (#652D8C) lanyard, calm warm expression. Flat vector style from `brand/brand-identity.md` §6. | neutral, explaining, concern, success, hint |
| `newstarter-faisal` | Learner stand-in for scenarios | Fictional new staff member in business attire (front office) or scrubs (clinical scenes). | neutral, thinking, concern |

Rules: no real staff likeness; one approved master image before any variant; same face, clothes and proportions in every pose; alt text on each use. Characters appear on scenario screens only, never as decoration on every slide (minimalist rule).
