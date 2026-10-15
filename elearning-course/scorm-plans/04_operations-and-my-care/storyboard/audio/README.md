# Narration production status — Module 04

The complete, screen-by-screen English script is in [`../narration-script.json`](../narration-script.json).
The recording table and TTS-ready text are in [`../voice_talent.md`](../voice_talent.md) and
[`../audio-script-export.json`](../audio-script-export.json).

## What is ready

- 14 screen segments, with lead/co-host prefixes, a timing estimate and a pronunciation lexicon.
- Estimated spoken runtime: **1.6 minutes** at 140 wpm. Interactive work adds the remainder of the module seat time.
- Captions/transcript text can be derived from each segment’s `narration_text` field.

## What is intentionally not yet produced

No shipping audio is generated in this draft. The shared voice decision (**D10**) remains open: the
programme needs two approved, fixed English voices (Noor and Dr. Omar), commercial-use permission,
and a short client-approved sample before a TTS provider or a human voice talent is booked. Once
approved, synthesise or record the `tts_text`, join planned two-voice turns with 0.3 seconds of
silence, normalise loudness, and update the Phase 4 asset map.

The scripts are review-ready; they are **not** evidence that a policy, clinical, EHR or payer fact is
approved. Keep every `⚠ PENDING` item in the cards until its Phase 0 owner closes it.
