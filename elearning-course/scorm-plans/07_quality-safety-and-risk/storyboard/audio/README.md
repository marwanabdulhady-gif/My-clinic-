# Narration production status — Module 07

The screen-by-screen English script is in [`../narration-script.json`](../narration-script.json); the
recording table and TTS-ready text are in [`../voice_talent.md`](../voice_talent.md) and
[`../audio-script-export.json`](../audio-script-export.json).

## What is ready

- 23 segments on 22 narrated screens: 20 Noor lines and 3 Dr. Omar lines (`qsr-031`, `qsr-040`, `qsr-092` part `omar-1`).
- Estimated spoken runtime: **6.0 minutes** at 140 wpm (speaker tags excluded).
- Captions/transcript come from each screen's `narration_text`, which keeps the speaker names.

## What is not produced yet

No shipping audio exists. Decision **D10** (provider, voice ids, commercial licence) is open; approve a
30-second sample of each voice first. Then synthesise or record each segment's `tts_text`, join
`qsr-092` as `noor-1` + 0.3 s silence + `omar-1`, run `normalize_audio_asset` on every file, and
update the Phase 4 asset map. Keep every `⚠ PENDING` item open until its Phase 0 owner closes it.
