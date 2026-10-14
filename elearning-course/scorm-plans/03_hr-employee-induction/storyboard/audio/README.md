# Narration audio — 03 Welcome On Board

> **Superseded reference reads — not the companion voices.** These 10 clips were made from the
> v0.1 single-narrator script, before the course companions existed. Storyboard **v0.2**
> (2026-10-14) splits the narration between **Dr. Omar** (lead host, 35 lines) and **Noor**
> (co-host, 4 lines) — see [`../narration-script.json`](../narration-script.json),
> [`../voice_talent.md`](../voice_talent.md) and
> [`../../../00_program/characters/companions.md`](../../../00_program/characters/companions.md) §5.
> The clips are kept only as a pacing and pronunciation reference. **Do not ship them**, and do not
> treat their voice as Noor's or Dr. Omar's: the two companion voices are still open under program
> decision **D10**, and each needs an approved 30-second sample before production.

What changed since these clips were made: every line now has a speaker (`OMAR:` / `NOOR:`);
`hr-000` and `hr-091` are two-voice screens (Omar then Noor, joined with 0.3 s silence);
`hr-001` ends with Omar's first-week story; `hr-031` and `hr-044` are Noor's; `hr-061` has an extra
Omar tip line played with the end-of-simulation feedback. The `hr-001` and `hr-091` clips below
therefore no longer match the script.

## Voice used for this reference (v0.1, superseded)

| Field | Value |
|---|---|
| Voice id (this session) | `voice-00` |
| Language / accent | English (GB) |
| Persona | An experienced colleague coaching a new team member on their first week |
| Pace | ~140 wpm (the module's stated pace) |
| Provider | Arena TTS — **not** the production provider |

## What's here

10 clips, one per section, ~5 minutes of audio in total. They were picked to give a full tour of
the module's voice rather than just the longest scripts.

| File | Screen | Section | Est. sec |
|---|---|---|---|
| `MC03-welcome-on-board_hr-001.mp3` | `hr-001` | A · Welcome | 37.6 |
| `MC03-welcome-on-board_hr-012.mp3` | `hr-012` | B · Values & strategy | 45.6 |
| `MC03-welcome-on-board_hr-020.mp3` | `hr-020` | C · Our clinic | 32.1 |
| `MC03-welcome-on-board_hr-030.mp3` | `hr-030` | D · Ethics & patients' rights | 35.1 |
| `MC03-welcome-on-board_hr-041.mp3` | `hr-041` | E · Your leave | 42.0 |
| `MC03-welcome-on-board_hr-051.mp3` | `hr-051` | F · Pay & social insurance | 28.7 |
| `MC03-welcome-on-board_hr-061.mp3` | `hr-061` | G · Systems & licences | 11.6 |
| `MC03-welcome-on-board_hr-070.mp3` | `hr-070` | H · ID, benefits & dress code | 25.2 |
| `MC03-welcome-on-board_hr-080.mp3` | `hr-080` | I · Contracts & leaving | 23.5 |
| `MC03-welcome-on-board_hr-091.mp3` | `hr-091` | Z · Close | 27.0 |

**Not generated, and not planned in this voice:** the other 26 screens. Shipping audio for all 36 screens is produced in the two companion voices once D10 closes.

## How these were generated

Each clip is the `tts_text` from the **v0.1** version of
[`../audio-script-export.json`](../audio-script-export.json) (since replaced by the v0.2 two-voice export), i.e. the narration **with the
pronunciation lexicon applied**. That's deliberate: it's the text that would actually be sent to a
TTS provider, so listening is a real test of the lexicon.

**Listen for these** — they're the entries most likely to read badly, and fixing them is a
one-line change to the `lexicon` block in
[`../narration-script.json`](../narration-script.json):

| Term | Written as | Appears in |
|---|---|---|
| GOSI | `GO-see` | `hr-051` |
| HR | `H-R` | `hr-070`, `hr-091` |
| ID | `I-D` | `hr-070` |
| Qiwa | `KEE-wa` | `hr-080` |
| Oracle | `OR-uh-kul` | `hr-080` |

If any of them comes out as “H dash R” or similar, change the entry to a spelled-out form
(for example `"HR": "aitch ar"`) and regenerate.

## Pacing

v0.1 (these clips): 1,590 words ≈ 705 s. v0.2 script: 1,628 words (speaker labels excluded) ≈ 722 s
(12 min) at 140 wpm against the Phase 3 estimate of 13 minutes — inside the ±15% tolerance.
`lint_narration_script` on the v0.2 script reports **0 errors, 0 warnings**
([`../lint-report.json`](../lint-report.json)).

## Note on the repo convention

`00_program/build-pipeline.md` says built media is not committed. These 10 clips total
**1.3 MB**, which is small enough to version alongside the script, and having them in the PR lets
reviewers hear the narration without leaving GitHub. If the course team would rather keep media out
of Git, add `elearning-course/scorm-plans/*/storyboard/audio/` to `.gitignore` and store the files
in Drive with the version number.
