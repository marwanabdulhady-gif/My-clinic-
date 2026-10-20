# Videos: where they are made and how

This folder is where the optional motion-graphics clips are **made**. The clips themselves are planned in [`../scorm-plans/00_program/media-video-plan.json`](../scorm-plans/00_program/media-video-plan.json). The tool choice is in [`video-tooling.md`](../scorm-plans/00_program/video-tooling.md). The full step-by-step agent procedure is [`video-playbook-review.md` §5](../scorm-plans/00_program/video-playbook-review.md#5-agent-procedure-one-clip-end-to-end).

> ⛔ **Do not start a clip until decision D17 is closed** in `scorm-plans/00_program/decision-sheet.md`. Narration also needs D10. See AGENT-TASKS.md T7.

## The one rule that keeps videos in sync

**The recorded narration is the master clock.** Write the script, record it, and freeze it. Then get the word timestamps from the recording and hang every animation on a **spoken phrase**, never on a typed number of seconds. If a phrase is not in the recording, the build fails loudly (`resolve_cues.py`, exit 1). Never stretch or trim the voice to fit the pictures.

## Folders

```text
video/
├── README.md                this file
├── .gitignore               keeps frames, masters and node_modules out of git
├── _shared/
│   ├── scripts/             tools every clip uses (run from inside the clip folder)
│   ├── brand/               tokens.css + where to copy fonts and characters from
│   ├── components/          HyperFrames blocks (to build: Headline, Chip, Card, RuleBanner, StepFlow, …)
│   └── docs/                templates: BRIEF, facts, script, REVIEW_LOG, QA_REPORT, CLIP_README
└── <clip-id>/               one folder per clip, named exactly as the id in media-video-plan.json
    ├── data/                BRIEF.md facts.md script.md visual_plan.json  (+ generated timing files)
    ├── narration/           sceneNN_noor.mp3 / sceneNN_omar.mp3, tts_settings.json
    ├── public/              audio/ fonts/ characters/ (unmodified copies)
    ├── src/                 HyperFrames composition; src/data/cues.json is GENERATED
    ├── renders/             board/ review/ <clip-id>.mp4 <clip-id>-poster.jpg  (frames/ qa/ masters gitignored)
    └── REVIEW_LOG.md  QA_REPORT.md  README.md
```

Start a clip like this:

```bash
C=elearning-course/video/<clip-id>
mkdir -p $C/{data,narration,public/audio,public/fonts,public/characters,src/data,renders/board,renders/review}
cp elearning-course/video/_shared/docs/{BRIEF,facts,script}.md $C/data/
cp elearning-course/video/_shared/docs/{REVIEW_LOG,QA_REPORT}.md $C/
cp elearning-course/video/_shared/docs/CLIP_README.md $C/README.md
```

## Names

| Thing | Name |
|---|---|
| clip folder | `<prefix>-vid-<slug>`, e.g. `prog-vid-welcome`, `qsr-vid-speakup` |
| scene heading in `script.md` | `# SCENE n \| kebab-id \| Title (≤ 40 chars)` |
| narration file | `narration/sceneNN_noor.mp3` or `sceneNN_omar.mp3` |
| cue key | `sceneNN-<what-appears>` in `data/cues.json`, value = the 2–5 spoken words it waits for |
| deliverables | `<clip-id>.mp4` · `<clip-id>.vtt` · `<clip-id>-transcript.html` · `<clip-id>-poster.jpg` |
| branch | `agent/t7-video-<clip-id>` |

## Scripts in `_shared/scripts/` (all tested)

| Script | What it does | Pass = |
|---|---|---|
| `resolve_cues.py` | Turns `data/cues.json` (cue → spoken phrase) into times from `data/transcript_words.json`. Writes `src/data/cues.json`. | exit 0. Exit 1 lists every phrase that is not in the recording. |
| `srt_to_vtt.py data/captions.srt data/<clip-id>.vtt` | Makes the WebVTT caption file with `<v Noor>` / `<v Dr. Omar>` speaker tags from `data/narration_manifest.json`. | exit 0 (fails on overlapping or empty cues) |
| `encode_scorm.sh <master> renders/<clip-id>.mp4` | 1080p master → 720p H.264, mono AAC 96k, loudness normalised to −16 LUFS / −1.5 dBTP, faststart | file written |
| `delivery_check.py renders/<clip-id>.mp4 --vtt data/<clip-id>.vtt` | **Hard checks:** H.264 yuv420p · 1280×720 or 1920×1080 · 30 fps · AAC · ≤ 10 MB/min · −16 ± 1 LUFS · true peak ≤ −1 dBTP · ≤ 3 flashes per second · VTT present | every line `PASS`, exit 0 |

Still to add, from the playbook kit (the raw playbook in the owner's Drive folder): `assemble_narration.py`, `transcribe.py` (faster-whisper word timestamps), `build_timeline.py`, `qa_check.py` (A/V sync, black, freeze, caption agreement), `motion_check.py`, `review_sheets.py`, `storyboard_board.py`. Until they are in `_shared/scripts/`, an agent stops at procedure step 21 and reports.

## Standards (every clip)

- Speakers: Noor and Dr. Omar only. Art comes from `scorm-plans/00_program/characters/assets/` and is never generated.
- Brand: follow [`_shared/brand/README.md`](_shared/brand/README.md): navy `#003867`, Montserrat, **one** module colour as the highlight, magenta for key warnings and key numbers (with an icon and words), and never colour alone. Use the navy logo PNG on light backgrounds and the white one on navy, on the first and last scenes only.
- Text: ≥ 24 px (body ≥ 28 px at 1080p), inside the safe area in `tokens.css`. Facts on screen must be a subset of `data/facts.md`.
- Sound: −16 ± 1 LUFS integrated, true peak ≤ −1 dBTP. Music off unless the owner asks.
- Accessibility: a separate VTT file (never burned-in), an HTML transcript, a poster frame for reduced motion, and no more than 3 flashes per second.
- Delivery: MP4 H.264 1280×720 30 fps, ≤ 10 MB per minute. Copy to the clip's `target_file` / `captions_file` (relative to `scorm-plans/`, in the module's `storyboard/assets/`) only after the owner approves.
- Licence: HyperFrames is open source. Remotion needs a paid company licence above 3 employees, so it is only a fallback.

## The gates (stop at each one and wait for an explicit OK)

A brief + facts → B script → C storyboard board → D narration (frozen) → E layout stills → F half-res draft → delivery checks green → owner approval → copy to `target_file`, rebuild the module, and run every AGENT-TASKS §3 check.
