# Narration production plan — eight My Clinic packages

This document turns the current scripts and voice standards into a repeatable external-agent handoff. It supplements [`narration-and-lexicon.md`](narration-and-lexicon.md), the package `storyboard/narration-script.json`, `audio-script-export.json`, `voice_talent.md`, `phase-3-narration-and-assets.md` and the Phase 0 decision sheet. Do not rewrite source facts or resolve open decisions during audio production.

## Current state

All eight packages have a narration script and audio export file. The project planning lint reports zero narration errors and warnings across the packages. Script segments identify the speaker, part, text, tone and target duration; two-voice segments are separated so speaker labels are not read aloud. The proposal's Rev01 scope is about 60 minutes of narration in two consistent voices. The open D10 decision still blocks final provider/voice-id selection and production of approved final audio. Existing module 03 reference MP3s are older, single-voice samples; they are not the final two-voice production set.

**Do not confuse “script ready” with “audio complete.”** Shipping TTS/human audio, normalization, captions and final audio asset provenance are still Phase 3 work. No final voice ids should be invented.

## Voice direction

- **Noor (`noor`):** warm, calm and clear; female, early-to-mid 30s; international English; light Gulf Arabic accent is acceptable; around 140 words per minute. Senior staff nurse and patient-safety liaison. Leads packages 01, 02 and 07.
- **Dr. Omar (`omar`):** friendly, confident and relaxed; male, late 30s; international English; light Gulf Arabic accent is acceptable; medium-low pitch; around 140 words per minute. Family physician and onboarding champion. Leads 03, 04, 05, 06 and 08.
- Use one fixed, commercially licensed voice per character across all packages. The two voices must sound clearly distinct. Do not imitate, clone or use the voice of a real employee or source-video narrator.
- The lead host narrates each screen unless its Phase 3 companion table names the co-host. The co-host only speaks in explicitly planned moments. The voice must not expose an answer before the learner responds.

## Script-to-audio workflow

1. **Select only approved rows.** Start from a package's current `audio-script-export.json`; use its `screen_id`, `part`, speaker, exact exported `tts_text`/SSML, tone and target duration. Treat `narration-script.json` and source card as the text authority. Never paraphrase, add connective wording, translate, correct policy values or merge separate speaker parts.
2. **Resolve D10 first.** Record the provider, commercial-use licence status and immutable voice id in `narration-and-lexicon.md` and the package voice metadata. Obtain written approval of a 30-second sample for Noor and for Dr. Omar before bulk generation.
3. **Generate per segment.** File names must preserve package, screen and part identifiers from the export. Emit clean speech audio only; do not speak `NOOR:`, `OMAR:`, screen ids, metadata, stage directions, cue syntax, SSML tags or text shown on screen.
4. **Join planned multi-voice screens.** Keep the scripted order. Insert 0.3 seconds of silence between consecutive parts, then produce one screen-level audio asset where the build schema expects one. Do not combine unrelated screens. Keep original per-part files for traceability until the joined asset passes QA.
5. **Normalize and caption.** Apply the project's audio-normalization step to every final file. Generate captions/transcript from the approved script, preserve the speaker name in transcript/caption metadata, and do not rely on automatic speech recognition for the final text.
6. **Record provenance.** Store the exact input export, provider/model, voice id, generation date, normalization settings, final filename, duration, reviewer and licence/approval evidence in the package provenance record.

## Prompt for an external audio/TTS agent

```text
Produce audio for the My Clinic induction program using only the supplied audio-script-export.json rows. Do not edit, paraphrase, translate, supplement or reorder any spoken words. Generate each segment with its assigned approved speaker voice and preserve screen_id/part in the output filename and metadata. Speak only tts_text; never read speaker labels, screen text, ids, cues, pauses, JSON keys or SSML markup aloud. Use the client's approved fixed voice ids only; if voice id is null or approval is missing, stop and return a blocked-items list instead of choosing a voice. Target the script's stated tone, pace near 140 English words/minute, clear Gulf-region intelligibility and natural, unhurried delivery. Keep pauses marked in the script, but don't add theatrical emotion. Export clean WAV or high-quality MP3 per segment; also return provider/model, voice id, exact text hash, duration and generation date. Do not synthesize a voice resembling a real employee or source-video narrator. Do not generate captions from altered speech; captions must match the supplied approved script verbatim. Flag pronunciation uncertainty rather than changing terminology. Keep original segment files; any multi-part screen is joined in scripted order with 0.3 s silence after individual segments pass review. Do not claim policy, clinical or legal approval.
```

## Companion voice assignment

- Package 01: Noor lead; Omar on the planned infusion-pump scenario and specified guide moments.
- Package 02: Noor lead; Omar appears only in the planned drill/co-host moments.
- Package 03: Omar lead; Noor co-host. The welcome (`hr-000`) and close (`hr-091`) are two-voice exchanges; retain their separate parts.
- Package 04: Omar lead; Noor co-host for the planned tip/role moments.
- Packages 05–06: Omar lead; Noor in the planned hints/tips, not on every screen.
- Package 07: Noor lead; Omar co-host for the risk/near-miss moments named in Phase 3.
- Package 08: Omar lead; Noor on the planned patient-education tip only.

Exact screen-to-speaker/pose assignments live in each module's Phase 3 “Companions in this module” table. If the table and a script differ, stop the affected screen and resolve it in the project files before generation.

## Pronunciation and narration quality gate

- Follow the master lexicon in `narration-and-lexicon.md`. Use the module's script-local lexicon for its exact terms; do not infer local pronunciations for unresolved abbreviations.
- Speak for the ear: mostly short active sentences, one idea at a time, second person, present tense. The screen carries keywords; narration explains rather than reads the screen.
- Never say “click Next,” refer to “this slide,” narrate a screen label verbatim, give an answer on a question screen, shame a learner or dramatize a patient-safety event.
- Confirm pronunciation of My Clinic, Noor, Omar, CBAHI, MOH, ICD-10, payer/regulator names and local branch names with the approved lexicon/SME.
- Review a representative sample from each speaker and package. Listen for clipped words, robotic cadence, speaker swaps, extra speech, music masking, volume jumps and mispronunciation. Verify duration against the script target and package estimate.
- Compare every final transcript/caption to the approved narration text. Run `tools/lint_planning.py` before audio; use the server narration lint again before Phase 4 as required by the roadmap.

## Source-media cautions

- Package 07's source video narration has a low-accuracy transcript; do not quote or use it as a pronunciation reference. Use the approved course script and lexicon.
- Package 08's original IT video is silent and includes real patient identifiers in parts of the recording. Do not use it as image, video, audio or screen-capture source. The planned training uses approved fictional-patient test-environment captures only.
- Keep raw audio and AI generation files within the approved private project workspace. Do not upload client source media or scripts to an external provider unless its retention, privacy and commercial-use terms have been accepted by the project owner.

## Audio completion checklist

- [ ] D10 provider/voice ids and both 30-second voice samples approved in writing.
- [ ] All eight exports are current and pass local and server narration lint.
- [ ] Every segment's audio speaks the exact approved words; speaker labels are not spoken.
- [ ] Multi-part screens have correct voice order and 0.3-second gaps.
- [ ] Every audio file is normalized and duration/quality checked.
- [ ] Captions, transcript, provenance and final filenames match the export ids.
- [ ] SME approval is recorded for any disputed pronunciation or source-sensitive statement.
