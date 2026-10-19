# Media production runbook — for the image, audio and video agents

![My Clinic logo](brand/logo-preview.png)

This is the working procedure for any agent (or person) that makes the pictures, narration and videos for the eight packages. The job lists are generated, so nobody has to work out what is missing:

```bash
python3 elearning-course/scorm-plans/tools/build_media_jobs.py     # writes <module>/production/media-jobs.json
```

The roll-up is in [`media-jobs-summary.md`](media-jobs-summary.md). Each job carries its route, target file, size, prompt or script, the screens that use it, the hotspot regions it must show, the gate that blocks it, and its acceptance checks. **An agent picks a job whose gate is closed, makes the file at `target_file`, records provenance, and re-runs the build.** Nothing else in the storyboard is edited by a media agent.

---

## 1. The loop (every job)

1. **Pick** a job with `status: "todo"` from `<module>/production/media-jobs.json`. Skip it if its `gate` names an open decision in [`decision-sheet.md`](decision-sheet.md). Assumed answers ([`kickoff-assumed-answers.md`](kickoff-assumed-answers.md)) are enough for a *draft*, not for a release file.
2. **Make** the file exactly at `target_file`, in the format the job asks for.
3. **Check** it against the job's `acceptance` list, and look at it on the built screen. Hotspot pictures also go through §3.
4. **Record** provenance in the job (`made_by`, `tool`, `model`, `date`, `prompt_used`) and set `status` to `"review"`. Only the SME or the course owner sets `"approved"`.
5. **Rebuild** the module (§6). A file at `target_file` replaces the PENDING card automatically.

## 2. Images

| Route | What it means | Who makes it |
|---|---|---|
| `ai-image` | Flat vector illustration from the job's `prompt` (the approved prompt plus the shared style suffix from [`visual-generation-prompts.md`](visual-generation-prompts.md)) | Image agent |
| `own-svg` | Diagram, icon set or pictogram drawn as SVG; labels stay in HTML, never in pixels | Diagram agent |
| `own-pdf` | Job aid from the brand template | Document agent |
| `client-photo` / `client-photo-or-role-tile` | Photographed by My Clinic with permission; if not supplied, a role tile or an `ai-image` substitute, recorded as a substitution | My Clinic / image agent |
| `capture` | Screenshot from an approved **test** environment (Oracle, EHR). Never generated, never from `IT.mp4` | My Clinic IT with L2S |

Rules that apply to every generated picture: 1920 × 1080 master (shown at 960 × 540), PNG, no text, numbers, logos or identifiers in the pixels, no real likenesses, Noor and Dr. Omar are never regenerated (use `characters/assets/`), unnamed supporting people only ([`visual-and-motion-agent-brief.md`](visual-and-motion-agent-brief.md)).

## 3. Hotspots on generated pictures — and adding more

A hotspot box is only right for the picture it was drawn on, so boxes live in a **map file** next to the picture, not in the storyboard:

```bash
python3 tools/map_hotspots.py init    01_health-and-safety-1 hs1-img-corridor   # map from the current screen
python3 tools/map_hotspots.py preview 01_health-and-safety-1                    # overlay page to check by eye
```

- After generating a picture, open `production/hotspots/<asset-id>.json`, set one pixel box per region (`[x, y, w, h]` on the picture's own size), fill `mapped_by`, and check `production/hotspots/preview.html`: every box must sit on its object. An agent with vision can draft the boxes; a person signs `checked_by`.
- **More hotspots:** when the new picture shows more useful things, add them under `add_regions` with a label and feedback. They go live on explore and unscored screens at the next build. On a **scored** find-the-hazard screen they change the answer key, so they wait for `"sme_approved": true`.
- Every hotspot job in `media-jobs.json` lists the regions the picture **must** show; the image prompt is not accepted until each one is visible, separate and at least 48 px at 960 × 540.
- Worked example: `01_health-and-safety-1/production/hotspots/hs1-img-corridor.json` (eight boxes checked, one new region — the stairwell exit — proposed for SME confirmation).

## 4. Audio (narration)

- One clip per segment, file name `<prefix>-aud-<screen>.mp3`, MP3 44.1 kHz mono 96 kbps, −16 LUFS integrated, −1 dBTP, 300 ms head and tail.
- Voices: Noor and Dr. Omar only, from the D10 provider; the voice description is in each job. Neither voice may be cloned from, or sound like, a real employee.
- **Do not voice a job with `status: "blocked-rewrite"`** (156 of 218 on 2026-10-19; every segment in 01, 02, 04, 05, 06 and 08). Rewrite them with `tools/narration_rewrite.py` (export → fill `new_text` → apply → check); step by step in [`../../AGENT-TASKS.md`](../../AGENT-TASKS.md) T1. Its script still carries generic filler lines (listed in `filler_lines`) added by the storyboard assembler to reach the target length (gap G11). Rewrite from the source first, keep it under `target_sec`, never narrate the answer.
- Captions: WebVTT made from the final audio by forced alignment (e.g. `whisperx` or `aeneas`), with speaker voice tags. The caption text must match `narration_text` on the screen word for word.
- Pronunciation: the lexicon in `storyboard/voice_talent.md` and [`narration-and-lexicon.md`](narration-and-lexicon.md).

## 5. Video (motion graphics)

The approved baseline (Rev01) needs **no** video. The optional motion-graphics clips are planned in [`media-video-plan.json`](media-video-plan.json) and the tool choice is in [`video-tooling.md`](video-tooling.md). Each clip is a change request or a free value-add, decided by the owner (decision D17 in [`personalisation-and-interactivity-plan.md`](personalisation-and-interactivity-plan.md)). Every clip: approved script first, Noor/Dr. Omar art from `characters/assets/`, brand palette and Montserrat, MP4 H.264, 1280 × 720 or 1920 × 1080, ≤ 10 MB per minute, a WebVTT caption file and a text transcript, no flashing above 3 per second.

## 6. Rebuild and check

```bash
python3 tools/build_course_spec.py <module>          # picks up new files + hotspot maps
EDUMINTS_DIR=… /tmp/claude-0/edu-venv/bin/python tools/edumints_build.py <module>
python3 tools/build_media_jobs.py                    # job statuses refresh from the files on disk
```

Open `<module>/build/preview.html` and look at every screen the job lists. Then the normal gates: `lint_planning.py`, `audit_assets.py`, the test suite.
