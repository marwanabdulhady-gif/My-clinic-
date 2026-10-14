# Narration audio — 03 Welcome On Board

Reference narration for the module, generated so the course team can hear the voice and judge
pacing before committing to a TTS provider or booking voice talent.

**This is a reference read, not the shipping audio.** The plan's voice route is still open
(program decision **D10**): external English TTS for release 1, or a human voice for the welcome
screens (phase-3 §1). Whatever is chosen, one voice is used across all eight packages and every
file goes through `normalize_audio_asset` so loudness matches.

## Voice used for this reference

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

**Not yet generated:** the other 26 screens. Those are mostly short question set-ups (6–15 s each).
Say the word and I'll produce them in the next run.

## How these were generated

Each clip is the `tts_text` from
[`../audio-script-export.json`](../audio-script-export.json), i.e. the narration **with the
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

The full module is 1,590 words ≈ **705 s (11 min 45 s)** at 140 wpm, against the Phase 3 estimate
of 13 minutes — 91%, inside the ±15% tolerance. `lint_narration_script` reports **0 errors, 0
warnings**, so no segment runs past 60 s and every screen is within 15% of its own target.

## Note on the repo convention

`00_program/build-pipeline.md` says built media is not committed. These 10 clips total
**1.3 MB**, which is small enough to version alongside the script, and having them in the PR lets
reviewers hear the narration without leaving GitHub. If the course team would rather keep media out
of Git, add `elearning-course/scorm-plans/*/storyboard/audio/` to `.gitignore` and store the files
in Drive with the version number.
