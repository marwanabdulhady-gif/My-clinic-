# Review: the sibling project's AI Video Production Playbook

*Reviewed 2026-10-20. Source: Google Drive file `AI_VIDEO_PRODUCTION_PLAYBOOK.md` (id `1vJMIwyJHVHjdj5a1yOigMkJrrNnO3MnJ`, "Version 2") and its caption file `HSE_Induction_captions.srt` (id `1iiraMBoJiXIXTEqUzk3Q1ceuAeITGcys`). Compared with our [`video-tooling.md`](video-tooling.md), [`media-production-runbook.md`](media-production-runbook.md) §5 and [`media-video-plan.json`](media-video-plan.json).*

**How it was read.** The Drive tool returned the whole playbook in one result (379,705 characters, 7,127 lines, ending with the Appendix C table), so it was not cut off. One catch: the Drive text view escapes the Markdown (for example `\<\!-- FILE: template/package.json --\>`). The playbook's `extract_kit.py` (§4.1) looks for unescaped `<!-- FILE: … -->` markers, so it **will not work on that text**. To get the kit's 50 embedded files, download the raw `.md` (`download_file_content`) and run the extractor on that.

**What this file is.** It lists what we should take from the playbook, where the playbook disagrees with our plan, and a folder layout and agent procedure for our clips. Where the playbook says nothing about a topic, this review says so. It does not fill the gap with claims the playbook does not make. Nothing here changes a scored screen or a decision. Video work stays blocked until **D17** closes (AGENT-TASKS T7).

---

## 1. What the playbook covers (section map)

| § | Section | One line |
|---|---|---|
| 1 | Mission and non-negotiable rules | 14 golden rules: narration is the master clock, never paraphrase, never invent facts, cue every animation to a spoken phrase, no placeholders, verify before you claim, approve on paper first. |
| 2 | Pipeline at a glance | Phases P0–P10, each with its input, its output and a gate that must pass. Also gives typical run times on 2 vCPU / 2 GB. |
| 3 | Toolchain, repositories and licences | Tool table (Remotion 4.0.537, faster-whisper, imageio-ffmpeg, Inter, Piper/OpenAI/ElevenLabs/edge-tts/Gemini TTS, HyperFrames, Lucide). |
| 3.1 | Choosing the renderer | Remotion vs HyperFrames. Stays on Remotion unless the licence or the user rules it out, and says what carries over if you switch. |
| 4 | Bootstrap | `extract_kit.py`, the kit layout, new-project commands, machine sizing. |
| 5 | Phase 0: Intake | `data/BRIEF.md` contract (message/audience/action/proof), questions and defaults, routing by video type, formats per destination, fact ledger. |
| 6 | Phase 1: Script normalisation | `data/script.md` format `# SCENE n \| id \| Title`, verbatim rules, scene length, duration estimate. |
| 7 | Phase 2: Visual planning | `visual_plan.json` schema, the scene-planning method, the style bible, the storyboard approval gate, shot-plan tests. |
| 8 | Phase 3: Narration | Voice audition, one clip per scene, listening checks, master-track assembly with a fixed 1.8 s gap and two-pass loudness. |
| 9 | Phase 4: Transcription and timeline | faster-whisper `small.en`+, scene boundaries, script alignment, caption rules, exit codes, review flags. |
| 10 | Phase 5: Sound design | Synthesised original music bed and 7 SFX, ducking levels, sound rules. |
| 11 | Phase 6: Building scenes (Remotion) | Remotion rules, project architecture, scene workflow, cue-phrase rules, layout lessons, motion doctrine and the "premium look". |
| 12 | Phase 7: Visual QA loop | Still renders, sampling strategy, defect catalogue, draft render, motion audit, review sheets, "harsh director" scoring, human review rounds. |
| 13 | Phase 8: Final render | Render command, background running, memory, chunked muted render plus a separate audio mux. |
| 14 | Phase 9: Automated QA | `qa_check.py` checks and pass criteria (table quoted in §2.7 below). |
| 15 | Phase 10: Deliverables | Deliverable list and paths, short final message, mandatory retro. |
| 16 | Troubleshooting | 23 symptom → cause → fix rows (OOM, SIGPIPE, VAD dropouts, Arabic dots, cached images…). |
| 17 | Adapting the kit | Other languages, **Arabic/RTL rules (§17.1)**, vertical/60 fps/4K, other domains. |
| 18 | One-page agent checklist | P0–P10 tick list. |
| App. A | Kit source | All template files: config, Python pipeline scripts, Remotion core, scene registry, component library, doc templates (README, QA report, brief, facts, review log). |
| App. B | Worked example (HSE) | The 6:57, 10-scene, 945-word, 144-cue, 12,531-frame HSE induction: script, visual plan, 10 scene files. |
| App. C | Sources reviewed | What v2 took from HyperFrames, an Arabic motion-design guide, and the `motion-reel`, `arabic-motion-graphics`, `majed-*`, `famous-youtube-editor` and `we-viral-editing` skills. |

**Caption style seen in `captions.srt`.** There are 144 phrase-level cues, numbered from 1. Each cue holds one or two lines, broken at phrase boundaries. Lines are about 20–40 characters (for example `Health, Safety,` / `and Environment — or HSE —`), and most cues last about 1.3–5 s. The cue ends never overlap, and there is a small gap at sentence pauses. There are no speaker tags and no styling. The em dash is kept as in the script.

---

## 2. Practices worth adopting

### 2.1 Pre-production: script, approvals, scene manifest

- **Confirmed brief, written once.** `data/BRIEF.md` with frontmatter (`route`, `mode`, `message`, `audience`, `action`, `proof`, `destination`, `aspect`, `fps`, `language`, `voice`, `captions`, `music`, `sfx`, `brand`, `storyboard`), plus "Stated vs inferred" lists and one "integration check". The playbook's rule: "never execute an edited but unconfirmed brief." A phase that finds `BRIEF.md` "reads it and asks nothing".
- **Mode.** "Default to collaborative for anything longer than 60 s or anything client-facing." All our clips are client-facing, so we use collaborative mode.
- **Three approval gates** (rule 13): the confirmed brief, the storyboard board, and the stills/draft before the full render. "A note on a storyboard costs minutes; the same note on a video costs a render."
- **Fact ledger** `data/facts.md`: "One line per number, name, date, percentage, price, brand, colour code, classification or procedure that will appear on screen, with its source." There is a "Rejected or unverified" list "so nobody re-adds them by accident". "Never ask a model to 'add a compelling stat'." This matches our own rule 3. For us the sources are the storyboard or `kickoff-assumed-answers.md`, and the `⚠ Draft — pending` marker stays.
- **Script format** `data/script.md`: `# SCENE 1 | welcome | Welcome`, ids "unique and kebab-case", titles ≤ 40 characters, narration "verbatim", "one sentence per line". Use real punctuation and ` — ` for asides.
- **Scene length and duration.** "25–50 s of narration per scene (≈ 60–120 words)". Duration ≈ "words ÷ 150 × 60 s (EN), plus 1.8 s per scene gap". Our clips are 35–55 s (`target_sec`), so each clip will usually be **1–2 scenes**.
- **Visual plan contract** `data/visual_plan.json`. Each scene has `goal`, `visual`, `onScreenText`, `transitionIn`, `beats[]` (each with `cue` = "VERBATIM spoken phrase (2–5 words)" and an `action`), `sfx[]`, `mustShow` and `mustNotShow`, plus a project-level `criticalTerms` list. `build_timeline.py` checks every cue against the spoken words: "A missing SFX cue is a hard error; a missing beat cue is a warning."
- **Scene-planning method (§7.2).** Write the goal first. Give each beat one "visual verb" (*appear, build, connect, compare, transform, cross out, fill, flow, zoom-to-detail, resolve*). Group beats into 2–4 phases, with "One idea on screen at a time". Write on-screen text last: "headline ≤ 7 words, chip ≤ 4 words, body ≤ 12 words". Show procedures literally and concepts abstractly. List mustNotShow.
- **Shot-plan tests (§7.5), run on the plan before any code:** one-sentence, hook ("Something moves within the first second"), mute, phone ("Nothing that must be read below ~28 px on a 1080p 16:9 canvas"), event-gap ("under ~4 s for explainers"), no front-loading, "Write states, not feelings", and "Name the reference style instead of describing it".
- **Storyboard board.** `storyboard_board.py` builds one self-contained HTML page. The first pass is text only. Then comes a "sketch pass" with one posed still per scene in `renders/board/sNN_*.jpeg`. It ends with "open decisions as option lists, your recommendation first".

### 2.2 Audio: voice, loudness, music, SFX

- **Narration is frozen once approved.** "Once the master narration exists, never trim, time-stretch, speed up, re-order or regenerate it to fit visuals." "If the audio and script disagree, the audio wins for timing."
- **Pronunciation fixes go only in a TTS-side respelling map** (`PRON`, e.g. `{"PPE": "P P E"}`). The captions keep the script spelling. This fits our lexicon in `narration-and-lexicon.md`.
- **Audition two voices** on 30–45 real words and let the user choose by ear: "You cannot hear; the user can." Record provider, voice id, model and settings in `narration/tts_settings.json`. Training delivery is "~140–160 wpm".
- **One clip per scene**: `narration/scene01.mp3`, with an optional descriptive suffix (`scene01_welcome.mp3`). Long scenes are split as `scene03_part1.mp3`, `scene03_part2.mp3`, and these are joined with no gap.
- **Master track:** `python3 scripts/assemble_narration.py narration --gap 1.8 --lufs -16`. This puts a fixed 1.8 s silence between scenes ("don't go below 1.5 s"), a 0.3 s lead-in and a 0.6 s tail. It applies "one static, two-pass loudness gain" (`loudnorm=I=-16:TP=-1.5:LRA=11`, then `linear=true` with the measured values). It writes `data/narration_manifest.json` with the sha256 of the audio.
- **Music and SFX are synthesised originals** (`make_audio_assets.py`): a calm bed exactly as long as the narration, plus whoosh, tick, pop, chime, alert, drop and swell. "No third-party samples, so no licensing questions."
- **Ducking:** music at "~0.075 under speech, rising smoothly to ~0.15 in pauses, with a 3 s fade at the end". As a rule of thumb, the bed runs "−20 to −24 dB under speech".
- **SFX rules:** use 2–5 per scene at volume 0.08–0.22, each tied to a spoken phrase. "A sound only where something visible happens." `sfx_alert` is for real warnings only. "Nothing childish". "Approved sounds are frozen."
- **Mix targets:** the pause level is ≥ 6 dB below the speech level, the export loudness is within 1 LU of the narration, and the peak is < −1 dBFS.

### 2.3 Timing and sync

- **Narration as master clock.** Scene boundaries, beats, captions and SFX "are all derived from the recorded audio, never estimated".
- **Transcription:** faster-whisper with word timestamps, `beam_size=5`, `vad_filter=False`. VAD "drops speech it judges to be silence". Use `small.en` as the minimum. In testing, "`base.en` dropped a whole sentence and misplaced 14 words".
- **Scene boundaries:** if the manifest's sha256 matches the audio, they are the midpoints of the inserted gaps (exact). If not, they are the midpoints of the N−1 longest pauses (`silencedetect` −40 dB).
- **Alignment:** ASR words are aligned to script tokens with difflib. Timings come from the audio, and spelling and punctuation come from the script. `build_timeline.py` exit codes are `0` OK, `1` SFX cue not spoken, `2` ASR alignment problem ("never hand-edit timings"). Read `data/review_flags.md` every time.
- **Phrase-keyed cues that fail loudly.** `at("phrase")` "throws if a phrase is not spoken". Offsets: `at("phrase", -4)` when the visual should already be there as the word lands, `+6` for reactions, and `at("phrase", 0, "end")` to fire on the end of a phrase. When a phrase repeats, use a longer phrase or `cueSec(phrase, afterSec)`.
- **Transitions sit inside the inter-scene silence**: full-frame wipes, `TRANSITION_FRAMES = 26`, centred on the cut. QA fails if "any spoken word [falls] inside any wipe".

### 2.4 Visual design system

- **Colour roles over hex values.** "Keep the role when re-branding; change the hex." Warning and alert colours are reserved for real warnings and alerts (rule 7). "Warn with layout, not just colour", with an icon (⚠, ✕) as well.
- **Layout grid (1920×1080):** header band y 40–130, headline y 160–260, main stage y 260–880, caption band y 900–1040, safe margins x 96–1824.
- **Minimum sizes at 1080p:** icons that carry meaning ≥ 120 px, badges ≥ 160 px, body text ≥ 28 px, "any label the viewer must read ≥ 24 px". The phone review showed that 16–20 px sub-labels "are unreadable on a phone". Show "At most ~3 text elements visible at once in addition to the headline."
- **Motion grammar:** entrances use 12–20 frames ease-out, exits 10–14 frames. "Never scale up from 0. Start at 0.92–0.97". Stagger 30–80 ms per item. "No overshoot on big type." Hold text for reading time: "0.3 s per word, minimum 1.5 s". Use a "dramatic comma" of 0.3–0.75 s. "During safety-critical demonstrations the camera is static."
- **No idle freeze, no idle wobble.** Fill a long beat with one of five named routes: staged reveals, camera with intent, sequenced UI life, animated sequences, cursor-led action. "Sine-wave breathing, floating or glow pulses used to fill time read as 'the video is waiting'."
- **Banned by default:** "glow or bloom on text, bounce or elastic, gradient-filled text, the purple→blue 'AI' background, centred titles on gradients, text in the corners or frame borders… random particles… a pop sound on every element". "Premium = restraint."
- **"Cards that explain"** look best as UI panels (app window, checklist with ✓ rows, stat tiles). Design landscape-first on 16:9.
- **Ghost elements** were "the most common defect": give every element a defined exit. Objects must rest on something. Animate along paths that avoid text.
- **Reusable component library** (Remotion kit, `src/components/UI.tsx`): `Headline`, `Reveal`, `Chip`, `Card`, `RuleBanner`, `DrawPath`, `Callout`, `StrikeX`, `StepFlow`, `RiskMeter`, `ChapterHeader`, `ProgressRail`, plus `Icons.tsx` (60+ line icons), `Person.tsx` (flat-vector cast with PPE layers), `Environment.tsx` and `Transition.tsx` (six wipes). These components are React/Remotion code. For HyperFrames we copy the **ideas and names**, not the code (see §3).
- **Characters:** a fixed cast across scenes for continuity. "Expressions stay neutral or positive. Show correct behaviour and minimise depictions of wrong behaviour; when you must show it, keep it small and immediately cross it out."

### 2.5 Captions and accessibility

- Captions come "from the actual audio (word timings from ASR, spelling from the script)". Cues break "at sentence ends, pauses > 0.55 s, ASR segment ends, > 80 characters or > 6 s". Very short cues are merged, padding is "0.35 s without ever overlapping", and there are "Up to two balanced lines".
- Caption QA: "No overlaps or out-of-range cues; caption text vs ASR agreement ≥ 0.97."
- Keep key visuals out of the caption band (y > 900). This still matters for sidecar captions, because the player draws them over the bottom of the video.
- The playbook does **not** cover WebVTT, speaker voice tags, HTML transcripts, WCAG, photosensitive flashing limits, reduced-motion fallbacks or file-size budgets. Those come from our own plan (§3).

### 2.6 Rendering

- Render to `renders/`, **never `out/`**. A video rendered to `out/` "vanished from the user's files once already".
- Remotion: `npm run render` (H.264 CRF 18, AAC 320 kb/s, `--concurrency=2`, `--timeout=120000`). Run it in the background and filter progress with `grep --line-buffered`. Don't pipe stills through `tail`/`head` (SIGPIPE kills the render).
- For a fragile machine: render **muted** chunks, render the audio once, then concat and mux. "Joining chunks that each carry AAC audio with `-c copy` can leave small gaps at the joins, so don't."
- The final render refuses to run when a scene is unregistered (no placeholders in deliverables). A half-resolution `draft` is allowed.
- **HyperFrames path (§3.1):** "read the cue times from `src/data/timeline.json` into your composition's `data-start` attributes instead of `at()`, and run `npx hyperframes lint && npx hyperframes check` before every render." Everything except Phase 6 carries over. `qa_check.py`, `motion_check.py` and `review_sheets.py` "read any MP4".
- Export spec: "H.264 yuv420p + AAC 48 kHz with `+faststart`. Never produce odd sizes."

### 2.7 QA: exact checks and thresholds

`qa_check.py <mp4>` writes `data/qa_results.json` and review frames (4 per scene plus the final frame). It exits 1 if a hard check fails.

| Check | Command inside the script | Pass |
|---|---|---|
| Frame count | full decode, `-map 0:v:0 -f null -` | `== timeline.durationInFrames` |
| Duration | container vs narration | `\|Δ\| ≤ 0.1 s` |
| A/V sync | FFT cross-correlation of export audio vs `voiceover.mp3` at start / middle / end windows | lag 0 ± 25 ms **and** normalised correlation ≥ 0.9 |
| Black frames | `blackdetect=d=0.1:pix_th=0.05` | no segment ≥ 0.1 s |
| Freezes | `freezedetect=n=0.0005:d=6` | no frozen picture > 6 s |
| Peak | `volumedetect` | max < −1 dBFS |
| Voice dominance | `volumedetect` on the longest pause vs the longest speech run | pause ≤ speech − 6 dB |
| Captions | cue list | 0 overlaps, 0 out of range |
| Caption text | difflib ratio vs raw ASR words | ≥ 0.97 |
| Transitions | words vs wipe windows | no spoken word inside a wipe (also reports the tightest margin) |
| Loudness | `ebur128` on export and narration | **reported only**: the "within 1 LU" target is in §10 but is not in the pass list |
| Motion (advisory) | `motion_check.py`: 12 fps, 160×90 grey, a frame "moves" when the 99th-percentile change > 6 | explainer goal ≥ 35 % moving, holds ≤ 3 s (the HSE film measured 30.6 %, holds up to 4.0 s) |

Visual review on the **final file**: `review_sheets.py` makes `contact.jpg` (30 frames), `phone.jpg` (15 frames at 360 px) and `strip_<t>.jpg` (12 consecutive frames around a fast move). The reviewer then scores eight axes 1–10 in `REVIEW_LOG.md` (hook, phone readability, motion, variety, composition, brand/fact accuracy, sound sync, script rendering) and lists "three biggest problems with timestamps". Still sampling per scene: frame 0 and +15, each beat at cue +10, phase boundaries ±6, the last frame, and each transition midpoint. The §12.3 defect catalogue covers blank opening, collision, ghost element, path crossing text, floating object, too small, wrong colour role, invented content, caption overlap and transition gap. "Viewers may cache images by path": write each re-check to a new filename.

### 2.8 File and folder structure (playbook kit)

Per project: `data/` (brief, facts, script, plan, manifests, transcripts, captions, flags, QA results), `narration/`, `public/audio/`, `public/fonts/`, `src/` (`data/timeline.json`, `components/`, `scenes/`), `renders/` (`final_1080p.mp4`, `board/`, `review/`, `qa/`, `frames/`), `docs/` templates, `scripts/`. Its `.gitignore` is `node_modules`, `renders/frames`, `renders/*.png`. Deliverables are listed in §15. A filled `README.md`, `QA_REPORT.md` and `REVIEW_LOG.md` ship with the video.

### 2.9 Naming

`# SCENE n | kebab-id | Title`, `narration/sceneNN[_suffix].mp3` and `sceneNN_partK.mp3`, scene components `SceneNNName.tsx`, stills `renders/frames/fNNNNN.jpeg`, board stills `renders/board/sNN_*.jpeg`, sheets `renders/sheet_sNN.jpg`, final `renders/final_1080p.mp4`, SFX `sfx_<name>.wav`.

### 2.10 Agent instructions and prompts

- "Do it yourself; don't make the user do it". "Ask only what you cannot reasonably default, in one batch". "State every default you apply."
- Rule 10: "Every number in the QA report comes from a command you ran on the final file." When delivering, say "in two lines what you checked and what you did not check".
- Rule 14 and §12.7: "Every note is an instruction". Fix exactly that, in the user's words. Approved details go into `REVIEW_LOG.md → Frozen decisions`.
- "Harsh motion director, not a proud author" self-review, then "Self-audit: … list every motion that breaks this section, worst first, and fix them."
- Mandatory retro (§15.1): record "repeatable mistakes only, phrased as a rule the next agent can follow".
- "Sessions reset installed packages": re-run the installs on `ModuleNotFoundError`. Keep projects off a RAM-backed `/tmp`.

### 2.11 Licensing

- Remotion License: "free for individuals and companies with ≤ 3 employees; larger companies need a paid Company License… Tell the user."
- HyperFrames is Apache-2.0, "so no company-size limit".
- Each Piper voice "has its own licence". edge-tts is a GPL-3.0 tool on "an unofficial Microsoft endpoint, so confirm the terms before commercial use". OpenAI TTS: "disclose AI voice per OpenAI policy". ElevenLabs: "commercial rights depend on plan".
- Fonts are OFL. Music and SFX are synthesised by the kit, so they are original. Real foley may only come from libraries whose licence allows video use, with a `sfx/CREDITS.md`.
- The playbook does **not** state a licence for its own kit code. If we copy its scripts, the owner should confirm that this is allowed (it is the sibling project in the same Drive).

---

## 3. Gaps and conflicts against our current plan

| # | Topic | Playbook | Our plan | Recommendation |
|---|---|---|---|---|
| 1 | **Renderer** | Remotion by default. HyperFrames only if the licence or the user rules Remotion out. | HyperFrames first, Remotion as fallback (paid licence). | Keep HyperFrames. A clinic group has more than 3 employees, which is exactly the playbook's own switch condition (§3.1). Keep the playbook's pipeline and change only Phase 6. |
| 2 | **Fail-loudly cues in HyperFrames** | `at()` throws on a missing phrase. HyperFrames reads `data-start` from `timeline.json`. | Not specified. | Add a small resolver step that turns every cue phrase into a `data-start` value and **exits non-zero** when a phrase is not found. Without it, HyperFrames loses the playbook's main safety net. Not built yet. |
| 3 | **QA script is partly Remotion-bound** | `qa_check.py` reads `TRANSITION_FRAMES` from `src/components/Transition.tsx`. | — | Adapt it: read the wipe length from a constant in our composition or from `visual_plan.json`. Other inputs (`src/data/timeline.json`, `public/audio/voiceover.mp3`, `data/transcript_raw.json`) carry over. |
| 4 | **Loudness** | LMS target "−16 LUFS, peak < −1 dBTP". The HSE export **measured −19.7 LUFS** ("acceptable for an LMS, but aim nearer −16"). The narration is normalised with TP −1.5, so it may land "~1 LU short". | Narration −16 LUFS, −1 dBTP (runbook §4). `loudnorm=I=-16:TP=-1.5:LRA=11` (video-tooling). | Target −16 LUFS integrated on the **delivered** MP4, with a tolerance of ±1 LU and true peak ≤ −1 dBTP. Add it as a hard check: the playbook only reports loudness. Don't accept −19.7 as our norm. |
| 5 | **Captions** | Default "Both (burned-in on, SRT delivered)". | Sidecar **WebVTT** + HTML transcript. "keep the VTT as a sidecar file, not burned in, so learners can toggle it" (video-tooling). | Use sidecar VTT only for SCORM, with burn-in turned off. Convert the playbook's SRT cue list to VTT (the timings are the same), using our limits of ≤ 2 lines, ≤ 42 characters per line and 1–7 s. The playbook allows 80 characters per cue and 6 s, so ours are tighter. Keep the playbook's ≥ 0.97 agreement and no-overlap checks. Still keep content out of the bottom band. |
| 6 | **Two speakers** | One narrator. No speaker tags. The SRT has none. | Noor and Dr. Omar; VTT "with speaker voice tags" (runbook §4). | Make one scene per speaker turn and record the speaker per scene in `tts_settings.json`. Write `<v Noor>` / `<v Dr. Omar>` from that. Note: `assemble_narration.py` puts a fixed 1.8 s gap between scenes, which may feel slow in a dialogue. The playbook gives no dialogue guidance, so this is an **open question** for the first clip. Don't shorten the gap below 1.5 s if a transition sits there. |
| 7 | **Characters** | Draws a flat-vector `Person.tsx` cast with PPE layers. | Noor and Dr. Omar as supplied PNG poses from `characters/assets/`. They are never regenerated. Lip-sync by Rhubarb mouth swaps. | Use our PNGs only. The playbook's cast rules (continuity, neutral/positive expressions, show correct behaviour) still apply. Rhubarb is not in the playbook, so add it from video-tooling.md. |
| 8 | **Brand** | Neutral palette (navy `#10243A`, teal, mint, amber for caution, red for alerts), Inter font. | Navy `#003867`, value colours, one module colour, **magenta `#9D3293` for warnings and key numbers**, Montserrat, no gradients except the navy title gradient, "Never use colour alone" (brand-identity.md). | Map the roles: primary dark → navy `#003867`; primary accent → module colour; caution/alert → magenta plus an icon. Load Montserrat locally instead of Inter. Emergency-code colours appear only as small chips. Brand is still under D11 (draft). |
| 9 | **Output format and size** | 1920×1080, CRF 18, AAC 320 k, AAC 48 kHz. No size budget. | 1280×720 30 fps, AAC mono 96 k, ≤ 10 MB/min (fail the build above it). | Render a 1080p master as the playbook does, then encode the SCORM file with the video-tooling ffmpeg line (CRF 26, `-maxrate 1200k`, mono 96 k, `+faststart`). Run `qa_check.py` on the **SCORM file**, because the playbook reviews the final file. Add a size check. |
| 10 | **Accessibility** | No flash limit, no reduced-motion, no transcript, no WCAG. | "No more than 3 flashes per second; reduced-motion: poster frame + transcript". WCAG 2.2 AA. | Add three checks: a flash check (method to be chosen; the playbook gives none), a poster frame `<clip-id>-poster.jpg`, and an HTML transcript made from `script.md`. |
| 11 | **Music** | Subtle original bed on by default. | Not stated for clips. | Ask in the brief: the playbook itself says "Ask about music and SFX… some clients want voice only." If music is used, use only the playbook's synthesised bed. |
| 12 | **Voice provider** | Platform tool, OpenAI, ElevenLabs, Piper, edge-tts, Gemini. | D10: "External English neural TTS (one female, one male voice) for release 1". Kokoro via `hyperframes tts` (video-tooling). | Use the D10 provider once D10 closes. Don't use edge-tts for release files (unofficial endpoint). Record the engine in `tts_settings.json`. |
| 13 | **Arabic** | Full §17.1 rules: MSA for training, numerals decided in the brief, Arabic OFL fonts, RTL mirroring, px padding for dots, no letter-by-letter reveals, diacritised text for free TTS, multilingual ASR `small`/`medium` with `ar`. | "Arabic voices out of scope for R1" (D10 assumed answer). Kokoro has no Arabic. | Out of scope for R1. Keep §17.1 as the reference for any later Arabic version. Kokoro could not be used for it. |
| 14 | **Remotion licence** | "Tell the user." | Creators seat about $25/seat/month (video-tooling §3). | No change. If we ever fall back to Remotion, the owner buys the licence first. |
| 15 | **Placement in the course** | n/a | Clips add "new unscored video screen after …". | Adding a screen may touch screen order, which is protected by our rule 2. This must be settled under D17 before any build work. **Open question; not decided here.** |
| 16 | **Where files land** | `renders/final_1080p.mp4` in the project. | `target_file: "media/video/<id>.mp4"`, but no base folder is given. | **Resolved 2026-10-20:** work in `elearning-course/video/<clip-id>/`; `target_file` is now `<module>/storyboard/assets/<clip-id>.mp4`, relative to `scorm-plans/`, where the build looks for media. |

---

## 4. Recommended folder structure and naming

The layout keeps the playbook's paths inside each clip, so its scripts run with their default paths (`data/`, `narration/`, `public/audio/`, `src/data/timeline.json`, `renders/`).

```text
elearning-course/video/
├── _shared/                          shared once, versioned
│   ├── scripts/                      playbook kit scripts (renderer-independent) + our additions
│   │   ├── assemble_narration.py  transcribe.py  build_timeline.py  make_audio_assets.py
│   │   ├── qa_check.py (adapted, §3 row 3)  motion_check.py  review_sheets.py
│   │   ├── contact_sheet.py  storyboard_board.py
│   │   └── ours (written, tested): resolve_cues.py · srt_to_vtt.py · delivery_check.py (size + flash + loudness) · encode_scorm.sh
│   ├── brand/                        brand tokens CSS (navy #003867, module colours, magenta), Montserrat woff2 + OFL licence
│   ├── components/                   HyperFrames HTML/GSAP blocks: Headline, Chip, Card, RuleBanner, StepFlow,
│   │                                 RiskMeter, Callout, StrikeX, ProgressRail, Transition (same names as the kit)
│   └── docs/                         BRIEF / FACTS / QA_REPORT / README / REVIEW_LOG templates from the playbook
└── <clip-id>/                        e.g. prog-vid-welcome, qsr-vid-speakup (ids from media-video-plan.json)
    ├── package.json                  exact pinned HyperFrames version
    ├── data/
    │   ├── BRIEF.md  facts.md  script.md  visual_plan.json          ← written by the agent, approved
    │   ├── narration_manifest.json  transcript_raw.json  transcript_words.json
    │   ├── timeline_manifest.json/.md  review_flags.md  captions.srt  ← GENERATED, never hand-edited
    │   ├── <clip-id>.vtt  <clip-id>-transcript.html                   ← generated from the above
    │   └── qa_results.json
    ├── narration/   scene01_noor.mp3  scene02_omar.mp3 …  tts_settings.json   (_joined/ is temporary)
    ├── public/
    │   ├── audio/   voiceover.mp3  music_bed.mp3  sfx_*.wav
    │   ├── fonts/   Montserrat-*.woff2
    │   └── characters/   unmodified copies of the poses used, from 00_program/characters/assets/
    ├── src/         HyperFrames composition (index.html + scene files), src/data/timeline.json (generated)
    ├── renders/
    │   ├── board/   sNN_<scene-id>.jpeg  storyboard.html is in review/
    │   ├── frames/  fNNNNN.jpeg                       (gitignored)
    │   ├── qa/      review frames from qa_check.py    (gitignored)
    │   ├── review/  storyboard.html  contact.jpg  phone.jpg  strip_<t>.jpg
    │   ├── <clip-id>_master_1080p.mp4                 (full-quality master; gitignored)
    │   ├── <clip-id>.mp4                              (SCORM encode, the deliverable)
    │   └── <clip-id>-poster.jpg                       (reduced-motion poster)
    ├── REVIEW_LOG.md   QA_REPORT.md   README.md
    └── .gitignore      node_modules/  renders/frames/  renders/qa/  renders/*.png  renders/*_master_*.mp4  narration/_joined/
```

**Naming convention**

- **Clip id:** exactly as in `media-video-plan.json`, `<prefix>-vid-<slug>` (`prog`, `hs1`, `hs2`, `hr`, `ops`, `rcma`, `rcmb`, `qsr`, `ehr`). The folder name equals the clip id.
- **Scenes:** `# SCENE n | <kebab-id> | <Title ≤ 40 chars>` in `data/script.md`. The ids are reused as keys in `visual_plan.json` and in the composition.
- **Narration:** `narration/sceneNN_<speaker>.mp3`, where speaker is `noor` or `omar`. A scene split for TTS length must use `sceneNN_part1.mp3`, `sceneNN_part2.mp3` **with no speaker suffix**. The script's file pattern only accepts `_partK` directly before the extension, and any other suffix on two files of one scene is rejected ("several clips for scene"). In that case, record the speaker in `tts_settings.json`.
- **Stills and sheets:** `renders/frames/fNNNNN.jpeg` (absolute frame number). Sheets get a new name each round (`sheet_s02_r2.jpg`), because viewers cache by path.
- **Deliverables:** `<clip-id>.mp4`, `<clip-id>.vtt`, `<clip-id>-transcript.html`, `<clip-id>-poster.jpg`. These are copied to the job's `target_file` / `captions_file` after the owner approves (§3 row 16, resolved).
- **Branch:** one clip per branch, named after the task (AGENT-TASKS §1), e.g. `agent/t7-video-prog-vid-welcome`.

---

## 5. Agent procedure: one clip, end to end

The procedure is written for an agent that follows steps literally. **Stop and report** whenever a gate fails or something is unclear. Do not guess. `$V` = `elearning-course/video`, `$C` = `$V/<clip-id>`.

**Gate 0: may I start?**

1. Read `CLAUDE.md` and `elearning-course/AGENT-TASKS.md`. Confirm that T7 is no longer marked blocked and that **D17** is closed in `scorm-plans/00_program/decision-sheet.md`. If D17 is open, stop.
2. Pick the clip from `media-video-plan.json` (start with `prog-vid-welcome`, then `qsr-vid-speakup`). Note its `id`, `module`, `target_sec`, `script_outline`, `target_file`, `captions_file` and `acceptance`.
3. Check that the clip's own gate in `gate` is satisfied (e.g. `hs1-vid-why` waits for D2, `qsr-vid-speakup` for D8). If it is not, stop.
4. Confirm the two open questions in §3 (rows 15 and 16) have answers from the owner. If not, you may draft, but do not deliver to `target_file`.
5. `git fetch origin main && git checkout -b agent/t7-video-<clip-id> origin/main`.

**Phase 0: brief and facts**

6. `mkdir -p $C/{data,narration,public/audio,public/fonts,public/characters,src/data,renders/board,renders/review}`. Copy the templates from `$V/_shared/docs/`.
7. Fill `$C/data/BRIEF.md`: `route: narrated-explainer`, `mode: collaborative`, `destination: lms`, `aspect: 1920x1080` (master), `fps: 30`, `language: en`, `captions: srt-only` (delivered as VTT), `music:` and `sfx:` as the owner says, `brand: 00_program/brand/brand-identity.md`, `storyboard: yes`. Write the message, audience, action and proof lines. Use `proof: none` unless a sourced fact exists. Fill the "Stated vs inferred" lists and one integration check.
8. Fill `$C/data/facts.md`. Every name, number, step or label that will appear on screen gets a source: the module storyboard, or `kickoff-assumed-answers.md` with `⚠ Draft — pending`. Anything without a source goes under "Rejected or unverified".
9. **GATE A:** send the brief and facts to the owner and wait for an explicit OK. Do not continue on an edited but unconfirmed brief.

**Phase 1: script**

10. Write `$C/data/script.md` in `# SCENE n | id | Title` format. Use one scene per speaker turn, one sentence per line, and keep it within `target_sec` (words ÷ 150 × 60 + 1.8 s per gap). Use only approved wording. Never narrate a quiz answer.
11. **GATE B:** the script is approved by the owner or SME ("Script approved before any render").

**Phase 2: visual plan and storyboard**

12. Write `$C/data/visual_plan.json` (schema in playbook §7.1). Each scene needs goal, visual, onScreenText, beats with verbatim 2–5-word cues, sfx, mustShow and mustNotShow. Map the palette to our brand roles (§3 row 8). List the Noor or Dr. Omar pose file for each beat from `00_program/characters/assets/`.
13. Run the eight shot-plan tests (playbook §7.5) and write the result of each in `REVIEW_LOG.md`.
14. Run `python3 $V/_shared/scripts/storyboard_board.py` from inside `$C` to make `renders/review/storyboard.html`.
15. **GATE C:** the owner approves the board. Apply every note to the plan file itself and record approved details under "Frozen decisions".

**Phase 3: narration** (needs D10 closed)

16. Audition two voices per speaker on 30–45 words of this script. The owner picks by ear. Record provider, voice, model and settings in `narration/tts_settings.json`.
17. Generate one clip per scene: `narration/sceneNN_<speaker>.mp3`. Apply pronunciation fixes only in the TTS-side `PRON` map, using the lexicon in `narration-and-lexicon.md`.
18. Transcribe or listen to every clip. Check for truncation, skipped sentences and mispronounced terms. Regenerate only the faulty scene.
19. `python3 $V/_shared/scripts/assemble_narration.py narration --gap 1.8 --lufs -16`. Read the printed LUFS value.
20. **GATE D:** the owner approves the narration. From now on it is frozen: never trim, stretch or regenerate it.

**Phase 4: timeline**

21. `python3 $V/_shared/scripts/transcribe.py public/audio/voiceover.mp3 small.en en`. Use `medium.en` if exit 2 appears later.
22. `python3 $V/_shared/scripts/build_timeline.py`. It must exit `0`. On exit 1, fix the cue in `visual_plan.json`. On exit 2, re-transcribe with a larger model. Never hand-edit timings.
23. Read `data/review_flags.md`. Resolve each `wording` flag with the owner, or accept the audio and note it for the QA report.
24. Run `python3 $V/_shared/scripts/srt_to_vtt.py` to write `data/<clip-id>.vtt` with `<v Noor>` / `<v Dr. Omar>` tags from `tts_settings.json`, ≤ 2 lines and ≤ 42 characters per line.

**Phase 5: sound**

25. Only if the brief says music or SFX are on: `python3 $V/_shared/scripts/make_audio_assets.py`. Use 2–5 SFX per scene, each on a visible event.

**Phase 6: build (HyperFrames)**

26. Install the pinned HyperFrames version (`package.json`, Node ≥ 22). Load Montserrat and the brand CSS from `$V/_shared/brand/`. Copy the needed character PNGs unmodified into `public/characters/`.
27. Run `python3 $V/_shared/scripts/resolve_cues.py`. It must exit 0, which means every cue phrase in `data/cues.json` was found in `data/transcript_words.json`; it writes `src/data/cues.json`.
28. Build each scene from `$V/_shared/components/`. Keep content inside x 96–1824 and y 150–880, with the first element visible by frame +20. Give each element an explicit exit. Readable text must be ≥ 24 px (body ≥ 28 px). Use no banned effects (playbook §11.6).
29. Sketch pass: render one still per scene into `renders/board/sNN_<scene-id>.jpeg`, rebuild the board, and get a layout OK (**GATE E**).
30. `npx hyperframes lint && npx hyperframes check` must pass before every render.

**Phase 7: visual QA on stills and draft**

31. Render stills at frame 0 and +15, each cue +10, phase boundaries ±6, the last frame and transition midpoints. Make a contact sheet with a new filename each round.
32. Check every scene against the playbook §12.3 defect catalogue and our brand rules in `$V/_shared/brand/README.md` (one module colour, magenta for key warnings and numbers with an icon, logo PNG only on first/last scene, never colour alone). Facts on screen must be a subset of `facts.md`.
33. Render a half-resolution draft. **GATE F:** the owner reviews the draft. Fix each note exactly as written, and re-render only the affected seconds.

**Phase 8: render and encode**

34. Render the master to `renders/<clip-id>_master_1080p.mp4` (never `out/`). Run it in the background and confirm the file exists with its size.
35. Encode the SCORM file with `bash $V/_shared/scripts/encode_scorm.sh renders/<clip-id>_master_1080p.mp4 renders/<clip-id>.mp4` (it also normalises loudness). The equivalent command, without loudness:
    `ffmpeg -i renders/<clip-id>_master_1080p.mp4 -vf scale=1280:720 -c:v libx264 -profile:v high -pix_fmt yuv420p -preset slow -crf 26 -maxrate 1200k -bufsize 2400k -r 30 -g 60 -c:a aac -b:a 96k -ac 1 -movflags +faststart renders/<clip-id>.mp4`
36. Export the poster frame `renders/<clip-id>-poster.jpg` and write `data/<clip-id>-transcript.html` from `script.md`.

**Phase 9: automated QA (on `renders/<clip-id>.mp4`)**

37. `python3 $V/_shared/scripts/qa_check.py renders/<clip-id>.mp4` must print `PASS` for every line and exit 0. The lines are: frame count, |Δduration| ≤ 0.1 s, A/V lag ≤ 25 ms with correlation ≥ 0.9 at all windows, no black ≥ 0.1 s, no freeze > 6 s, peak < −1 dBFS, pause ≥ 6 dB below speech, captions without overlaps, caption agreement ≥ 0.97, and no word inside a wipe.
38. Our extra hard checks:
    - `python3 $V/_shared/scripts/delivery_check.py renders/<clip-id>.mp4 --vtt data/<clip-id>.vtt --json data/qa_delivery.json` prints `PASS` on every line: format, ≤ 10 MB per minute, −16 ± 1 LUFS, true peak ≤ −1 dBTP, ≤ 3 flashes per second (frame-to-frame mean-luma jumps ≥ 20 %, a screening guard, not a full Harding test), VTT present;
    - VTT text matches the narration word for word.
39. `python3 $V/_shared/scripts/motion_check.py renders/<clip-id>.mp4 --profile explainer` is advisory: record the moving % and the holds over 3 s.
40. `python3 $V/_shared/scripts/review_sheets.py renders/<clip-id>.mp4`. Open `contact.jpg`, `phone.jpg` and every `strip_*.jpg`. Score the eight axes in `REVIEW_LOG.md` and list the three biggest problems with timestamps. Fix them, re-render, and re-run steps 37–40.

**Phase 10: deliver**

41. Fill `QA_REPORT.md` and `README.md` with numbers taken only from the commands above.
42. After the owner approves, copy `<clip-id>.mp4` and `<clip-id>.vtt` to the job's `target_file` and `captions_file`. Then run the module rebuild and every gate in AGENT-TASKS §3, and look at the screen in `build/preview.html`.
43. Write the retro under "Errors log" in `REVIEW_LOG.md`: repeatable mistakes, each phrased as a rule.
44. Commit, push and open a pull request (never merge it). End with the AGENT-TASKS §5 report, including two lines on what was checked and what was not.

**Done (2026-10-20):** `resolve_cues.py`, `srt_to_vtt.py`, `delivery_check.py`, `encode_scorm.sh`, the `_shared/docs` templates and `video/README.md`. **Still needed before an agent can finish step 21:** the adapted `qa_check.py`, the HyperFrames component set, and the kit scripts extracted from the raw playbook file. Building these is a separate task. It is not covered by the playbook.
