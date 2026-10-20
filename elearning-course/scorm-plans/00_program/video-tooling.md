# Programmatic motion-graphics video tooling for healthcare-induction e-learning

*Researched 2026-10-19. Star counts and releases come from the GitHub pages on that date, rounded. Licence terms change, so re-check before you buy.*

Project context: SCORM e-learning for healthcare induction. Brand navy `#003867`, Montserrat. Two illustrated characters, Noor and Dr. Omar, supplied as PNG poses. The videos are written by AI agents (Claude Code) working from code.

---

## 1. TL;DR recommendation

| Role | Pick | Why |
|---|---|---|
| **Primary composition and render** | **HeyGen HyperFrames** (Apache-2.0) | The source is plain HTML, CSS and GSAP. It is built for agents: 21 skills plus a Claude Code plugin. Rendering is deterministic (headless Chrome, then FFmpeg). There are no per-render fees and no headcount licence. Its CLI includes `tts` (local Kokoro) and `transcribe` (Whisper). Our HTML course and brand CSS can be reused as they are. |
| **Secondary / fallback** | **Remotion** (React, source-available) | The most mature ecosystem, with official `remotion-dev/skills`, `@remotion/captions`, Whisper.cpp captions, `@remotion/lottie` and Lambda. **It needs a paid Company Licence**, because a clinic group has more than 3 employees. That costs about $25 per seat per month for Creators. Choose it only if HyperFrames blocks you. |
| **Encode / package** | **FFmpeg** (LGPL/GPL) | The final H.264 + AAC encode, faststart, size control and loudness normalisation. |
| **Voice** | Kokoro-82M (local, Apache-2.0) via `hyperframes tts`. Use ElevenLabs or Azure Neural TTS if you need Arabic or premium voices. | Kokoro does **not** support Arabic. |
| **Captions (VTT)** | **WhisperX** (BSD-2) or `hyperframes transcribe`, then a small script to write WebVTT. **aeneas** only as a fallback. | When the script is known, align to the script text: you get exact wording and word timings. |
| **Character "talking"** | **Rhubarb Lip Sync** (MIT) for 2D mouth shapes, plus PNG pose swaps | It suits the illustrated Noor and Dr. Omar. Photoreal avatar models (HeyGen Avatar IV, MuseTalk, LivePortrait) are a poor fit for flat illustrations. |
| **In-player micro-animations** | **Lottie JSON / dotLottie** played by `@lottiefiles/dotlottie-web` (MIT), with `lottie-web` (MIT) as a fallback | Tiny vector files that can be themed. They run offline inside the SCORM zip. |

---

> **Update 2026-10-20 (owner's video playbook):** clips are now made in `elearning-course/video/<clip-id>/` (see [`../../video/README.md`](../../video/README.md)). The narration is the master clock: word timestamps come from the recording and animations wait for spoken phrases (`resolve_cues.py` fails loudly when a phrase is missing). The sidecar VTT script (`srt_to_vtt.py`) and the hard delivery checks (`delivery_check.py`: loudness, true peak, size, flashes, format) are written and tested. Comparison of the playbook against this plan: [`video-playbook-review.md`](video-playbook-review.md).

## 2. Comparison table

| Tool | Licence | Lang / authoring | Render pipeline | Output | Captions | Agent-friendliness | Stars (approx) | Last release / activity | SCORM fit |
|---|---|---|---|---|---|---|---|---|---|
| **HyperFrames** (`heygen-com/hyperframes`) | **Apache-2.0**, "no per-render fees or commercial-use thresholds" | HTML/CSS/JS, TypeScript tooling. Adapters for GSAP, CSS, Lottie, Three.js, Anime.js and WAAPI. | Headless Chrome (Puppeteer) seeks each frame, then FFmpeg encodes. Deterministic. Local, Docker, AWS Lambda, Cloud Run. | MP4. Transparent overlay is mentioned. | `transcribe` CLI (Whisper, word-level `transcript.json`). `embedded-captions` skill (WhisperX, **burned-in**). Sidecar VTT needs a small script. | **Excellent.** 21 skills (`/hyperframes` router, `hyperframes-cli`, `motion-graphics`, `faceless-explainer`, `slideshow`, `embedded-captions`, `remotion-to-hyperframes`…). Claude Code plugin. `lint`/`check`/`snapshot` QA commands. | ~67k | v0.8.175, **19 Oct 2026**. Very active, releases almost daily (still 0.x, so expect API churn). | **Excellent**: MP4 + VTT |
| **Remotion** (`remotion-dev/remotion`) | **Source-available "Remotion License"**. Free only for individuals, for-profits with **≤3 employees**, non-profits, and evaluation. Everyone else needs a **Company Licence**. | React / TypeScript | Bundles with Webpack/Rspack, renders frames in headless Chrome, then FFmpeg. Remotion Lambda / Cloud Run. | MP4 (H.264/H.265), WebM (VP8/9), ProRes, GIF, PNG sequence, audio-only | `@remotion/captions`, `@remotion/install-whisper-cpp` `toCaptions()`, `createTikTokStyleCaptions()`. Burned-in, but you can write VTT yourself. | **Excellent.** Official `remotion-dev/skills` (~5.4k★): `/remotion-best-practices`, `/remotion-captions`, `/remotion-render`… Includes AGENTS.md. | ~65k | v4.0.536, **16 Oct 2026** | Excellent technically, **but costs licence fees** |
| **Motion Canvas** (`motion-canvas/motion-canvas`) | MIT | TypeScript generator functions, Canvas2D | Browser editor exports an image sequence or uses the FFmpeg exporter plugin. Headless CLI rendering is weak. | MP4 (via ffmpeg plugin), PNG sequence | None built in | Moderate. It needs the editor UI to render, and has no agent skills. | ~19k | v3.17.2 (Dec 2024), 3.18 alpha (Feb 2025). **Slow.** | OK, but the render is awkward to automate |
| **Revideo** (now `midrender/revideo`, fork of Motion Canvas) | MIT | TypeScript (Motion Canvas API) | Headless browser `renderVideo()`, render API endpoint, Cloud Run example | MP4 | No first-party captions | Good API-first design, but uncertain momentum | ~4.1k | No GitHub releases listed. Repo moved org. **Maintenance risk.** | OK |
| **Manim (ManimCE)** (`ManimCommunity/manim`) | MIT | Python | Cairo or OpenGL renderer, then FFmpeg/PyAV | MP4, MOV, GIF, PNG, WebM | Plugin `manim-voiceover` (TTS + Whisper sync) | Good for code-gen of maths/diagrams. Poor for branded corporate/character work. | ~42k | v0.22.0 (Oct 2026) | Fine, but the wrong aesthetic |
| **Theatre.js** (`theatre-js/theatre`) | Core **Apache-2.0**, Studio editor **AGPL-3.0** | JS/TS | Runs in the browser. No video exporter; capture it via HyperFrames or Remotion. | (none natively) | none | Low. It is a visual keyframe editor for humans. | ~12.8k | Development "temporarily moved to a private repo" | Not needed |
| **Lottie / bodymovin + lottie-web** (`airbnb/lottie-web`) | MIT | JSON (exported from AE/bodymovin, LottieFiles Creator, Jitter, Figma plugins, or hand/agent-written) | Plays in the browser (SVG/Canvas/HTML renderers). It can also be rendered to MP4 inside HyperFrames or Remotion (`@remotion/lottie`). | `.json` | n/a (pair with an HTML transcript) | Good: an LLM can write or edit the JSON, but complex scenes are hard to write by hand | ~32k | Mature and slow-moving (many open issues) | **Excellent** for light in-player animation |
| **dotLottie** (`LottieFiles/dotlottie-web`) | MIT | `.lottie` (zipped JSON + assets) | Rust/WASM ThorVG core. Canvas2D/WebGL2/WebGPU. `<dotlottie-wc>` web component. | `.lottie`, `.json` | n/a | Good. Runtime **theming** (swap palette to `#003867`), state machines, markers. | ~0.9k | Active | **Excellent**: smaller files and theming |
| **Rive** (`rive-app/rive-wasm`) | Runtimes MIT. **The editor is proprietary SaaS.** | `.riv` binary | WASM runtime (canvas/WebGL) | `.riv`. The editor exports video on paid plans. | n/a | Low: the binary format can only be authored in the Rive editor | ~1k (wasm) | Active | Good runtime, but agents can't author for it |
| **Editly** (`mifi/editly`) | MIT | Node, JSON5 edit spec | FFmpeg + headless-gl + canvas/fabric | MP4, GIF | `subtitle` layer type (burned-in) | Good: a declarative JSON spec suits LLMs | ~5.5k | One maintainer, moderate activity | OK for slideshow-style videos. Limited motion design. |
| **FFmpeg** | LGPL-2.1+ (GPL with libx264) | CLI / C | The encoder itself | Everything | Burns in subs (`subtitles=`), muxes `mov_text`/WebVTT | Excellent (agents know it well) | (mirror) | 9.0.1 "Lei" (Aug 2026) reported | **Required** |
| **MoviePy** (`Zulko/moviepy`) | MIT | Python | Calls FFmpeg via imageio, with NumPy frames | MP4, GIF, etc. | `SubtitlesClip` (burned-in) | Good, but slow and v2 broke the v1 API | ~15k | v2.x | OK for simple assembly |
| **Shotstack** | **Proprietary SaaS** (SDKs are open) | JSON timeline via REST API | Cloud render | MP4, GIF, image | Caption/subtitle assets | Good (JSON API) | n/a | About $39/mo for 200 min (third-party figure, Sep 2026). Pay-as-you-go about $10 per 25 min. | Works, but adds vendor lock-in and data-residency questions |
| **Jitter** (jitter.video) | **Proprietary SaaS** | Web GUI | Cloud | MP4, GIF, **Lottie**, WebM/ProRes (Pro) | none | None (no public API found) | n/a | Free tier: 720p30 + Lottie export | Useful for **humans** to hand-design Lottie micro-animations |
| **Rhubarb Lip Sync** (`DanielSWolf/rhubarb-lip-sync`) | MIT | C++ CLI | Audio + optional script in, mouth-shape timeline out | TSV/XML/JSON (A–F, plus G/H/X shapes) | n/a | Excellent: JSON in, JSON out | ~2.7k | Stable | Drives mouth swaps on PNG characters |
| **OpenAI Whisper** (`openai/whisper`) | MIT (code + weights) | Python | Local ASR | txt/vtt/srt/tsv/json, `--word_timestamps True` | Writes **VTT** directly | Excellent | ~111k | Mature | Captions |
| **WhisperX** (`m-bain/whisperX`) | BSD-2-Clause | Python | Whisper + wav2vec2 forced alignment | srt/vtt/json, word-level | Accurate word timings | Excellent (`uvx whisperx`) | ~25k | Active | **Best caption timings** |
| **aeneas** (`readbeyond/aeneas`) | **AGPL-3.0** | Python/C | Forced alignment of known text to audio (TTS + DTW) | VTT, SRT, TTML, JSON, SMIL… | Sentence-level sync from the script | OK | ~2.9k | **Last release v1.7.3 (2017)**, Python 3.5-era | Legacy fallback only |
| **Kokoro-82M** (`hexgrad/kokoro`) | Apache-2.0 (code + weights) | Python/ONNX | Local TTS (used by `hyperframes tts`) | WAV | n/a | Excellent | ~9.5k | Active | EN/ES/FR/HI/IT/JA/PT/ZH. **No Arabic.** |

### AI video / avatar options (talking heads)

| Option | Licence / cost | Notes for Noor and Dr. Omar |
|---|---|---|
| **HeyGen API (Avatar IV / photo avatar)** | Commercial. About **$4/min at 1080p** via the API (third-party 2026 figures, $3–6 range). Separate API wallet. | Photoreal lip-sync. Results on flat illustrated PNGs are unreliable and may look off-brand. Also check healthcare-client consent and data-handling clauses. |
| **MuseTalk** (`TMElyralab/MuseTalk`, ~6.8k★) | MIT code and model, commercial use OK (test data is non-commercial) | Real-time lip-sync onto a video or image. Needs an NVIDIA GPU. Tuned for photoreal faces. |
| **LivePortrait** (`KwaiVGI/LivePortrait`, ~19k★) | Code MIT. **Check the InsightFace detector model licence (non-commercial) before commercial use.** | Portrait reenactment. Works on stylised faces only sometimes. Needs a GPU. |
| **SadTalker** (`OpenTalker/SadTalker`, ~14k★) | Apache-2.0 | CVPR 2023, now dated. |
| **Rhubarb + PNG mouth sprites** (recommended) | MIT, free, CPU | Ask the illustrator for 6–9 mouth shapes per character (or for each key pose). In the HTML, swap the mouth layer from Rhubarb's JSON. It matches the illustration style exactly. |

---

## 3. Remotion licence: exact current terms

From `remotion-dev/remotion/LICENSE.md`. The **Free Licence** covers:
- "an individual"
- "a for-profit organization with up to 3 employees"
- "a non-profit or not-for-profit organization"
- anyone "evaluating whether Remotion is a good fit, and are not yet using it in a commercial way"

Anyone else "is required to obtain a Company License". Pricing is at remotion.pro/license and remotion.dev/pricing. According to the pricing/terms pages, as summarised in search results in Oct 2026:
- **Remotion for Creators: $25 per seat per month.** No seat minimum, and no minimum spend when bought alone. A seat covers one person who writes Remotion code, **including through agentic tools such as Claude Code or Codex**.
- **Remotion for Automators: $0.01 per render, $100/month minimum.** This is for building video tools or apps. Developers on automation projects don't need a seat.
- **Enterprise:** from $500/month.

**For this project:** a healthcare provider with more than 3 staff needs at least 1 Creator seat (about $300/yr), or Automators if the renders are generated programmatically at scale. HyperFrames avoids this cost entirely.

---

## 4. Recommended pipeline

```
script.md (per scene: narration, on-screen text, character + pose, Lottie cue)
   │
   ├─1─► TTS ─────────────► scene-NN.wav
   │      hyperframes tts (Kokoro, local)  |  ElevenLabs / Azure Neural (Arabic, premium)
   │      → loudness-normalise: ffmpeg -af loudnorm=I=-16:TP=-1.5:LRA=11
   │
   ├─2─► Align / captions ─► words.json + scene-NN.vtt
   │      whisperx scene-NN.wav --output_format all   (or: hyperframes transcribe)
   │      → script `words2vtt` replaces ASR text with the *script* text (exact wording),
   │        cues ≤ 2 lines, ≤ 42 chars/line, 1–7 s, no orphan words
   │      (aeneas only if ASR fails on accents)
   │
   ├─3─► Lip-sync (optional) ► mouth-NN.json
   │      rhubarb -f json -d script.txt scene-NN.wav
   │
   ├─4─► Composition (HyperFrames)
   │      index.html per scene: brand.css (--navy:#003867; Montserrat self-hosted woff2),
   │      Noor / Dr. Omar PNG poses as <img> layers, GSAP timeline keyed to words.json,
   │      mouth sprite swaps from mouth-NN.json, Lottie icons via the Lottie adapter,
   │      <audio src="scene-NN.wav">. Agent uses /hyperframes + /motion-graphics skills,
   │      `hyperframes lint && hyperframes check --snapshots` for QA.
   │
   ├─5─► Render
   │      npx hyperframes render --quality delivery --output raw.mp4   (1920x1080 or 1280x720, 30fps)
   │
   └─6─► Final encode for SCORM (FFmpeg)
          ffmpeg -i raw.mp4 -c:v libx264 -profile:v high -pix_fmt yuv420p -preset slow \
                 -crf 26 -maxrate 1200k -bufsize 2400k -r 30 -g 60 \
                 -c:a aac -b:a 96k -ac 1 -movflags +faststart module-01.mp4
          → ship module-01.mp4 + module-01.vtt (<track kind="captions" srclang="en" default>)
```

**Size budget:** 10 MB/min is about 1.33 Mbps total. Spend about 1.1–1.2 Mbps on video and 96 kbps on mono AAC. Flat vector motion graphics usually reach **2–6 MB/min at 720p** with CRF 26–28, and 1080p fits under 10 MB/min with the `-maxrate` cap. Write a check that fails the build when `filesize / duration > 10 MB/min`. For lower bandwidth, also ship a 720p rendition.

**Accessibility:** keep the VTT as a sidecar file, not burned in, so learners can toggle it. Also ship an HTML transcript in the SCORM page (WCAG 2.2 AA). Burn in captions only for social cut-downs.

### Lottie route (in-player micro-animations)
- **Use it for** icon reveals (hand-hygiene steps, PPE, alarms), progress or "correct!" feedback, and character idle loops built from vector parts. Do **not** use it for narrated sequences; those go in MP4.
- **Author** in Jitter, LottieFiles Creator or After Effects + bodymovin (done by humans), or have the agent write or edit simple Lottie JSON (shapes, trims, transforms). Keep text as shapes, or make sure Montserrat is available.
- **Theme:** use dotLottie theming/slots for the navy `#003867` palette, so one asset serves several colourways.
- **Play:** bundle `@lottiefiles/dotlottie-web` (or `lottie-web` `lottie_light.min.js`, SVG renderer) **locally inside the SCORM zip**, with no CDN, because LMSs are often offline or sandboxed. Respect `prefers-reduced-motion`.
- **Budget:** each animation should be about 5–50 KB. Avoid embedded raster images in the Lottie.
- **Reuse:** the same Lottie can also play inside HyperFrames compositions, so the video and the in-player animation look consistent.

### Secondary-stack swap (if HyperFrames is blocked)
Remotion + `remotion-dev/skills` + `@remotion/install-whisper-cpp` (captions) + `@remotion/lottie`. Steps 1–3 and 6 stay the same; only step 4/5 changes. Budget for the Company Licence.

---

## 5. Risks and caveats
- **HyperFrames is 0.x and releases almost daily.** Pin the exact version in `package.json`, and keep the `hyperframes doctor` output in CI. It needs Node 22+ and FFmpeg.
- **Licences to note:** aeneas and the Theatre.js Studio are AGPL. Using them only as build-time tools is fine; don't ship them. libx264 is GPL; you are distributing outputs, not binaries, so that is fine.
- **Arabic voice:** Kokoro has none. Use Azure Neural TTS (ar-SA/ar-AE voices, word-boundary events) or ElevenLabs (timestamps endpoint). Check where patient-adjacent scripts are processed (data residency).
- **Avatar realism:** photoreal avatar tools are mismatched with illustrated characters. Pose swaps + Rhubarb are cheaper, deterministic and on-brand.
- The figures from third-party sources (Shotstack and HeyGen API pricing, FFmpeg version) should be confirmed on the vendor pages before you buy.

---

## 6. Sources
- HyperFrames repo/README: https://github.com/heygen-com/hyperframes · releases: https://github.com/heygen-com/hyperframes/releases · docs: https://hyperframes.heygen.com/introduction
- HyperFrames skills: https://github.com/heygen-com/hyperframes/tree/main/skills · embedded-captions SKILL.md: https://github.com/heygen-com/hyperframes/blob/main/skills/embedded-captions/SKILL.md · CLI skill: https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/SKILL.md
- HyperFrames coverage: https://themenonlab.blog/blog/heygen-hyperframes-video-as-code · https://claude.com/connectors/hyperframes-heygen · hyperframes-media skill (tts/transcribe, Kokoro): https://tessl.io/registry/skills/github/calesthio/OpenMontage/hyperframes-media
- Remotion repo: https://github.com/remotion-dev/remotion · releases: https://github.com/remotion-dev/remotion/releases · LICENSE: https://github.com/remotion-dev/remotion/blob/main/LICENSE.md · pricing: https://www.remotion.dev/docs/license/pricing , https://remotion.dev/pricing , https://www.remotion.pro/license , https://www.remotion.dev/blog/company-licenses
- Remotion skills: https://github.com/remotion-dev/skills · captions: https://www.remotion.dev/docs/captions/displaying , https://www.remotion.dev/docs/install-whisper-cpp/convert-to-captions
- Motion Canvas: https://github.com/motion-canvas/motion-canvas · https://github.com/motion-canvas/motion-canvas/releases
- Revideo: https://github.com/redotvideo/revideo (now midrender/revideo)
- Manim CE: https://github.com/ManimCommunity/manim · https://github.com/ManimCommunity/manim/releases
- Theatre.js: https://github.com/theatre-js/theatre
- lottie-web: https://github.com/airbnb/lottie-web · dotLottie web: https://github.com/LottieFiles/dotlottie-web
- Rive: https://github.com/rive-app/rive-wasm
- Editly: https://github.com/mifi/editly · MoviePy: https://github.com/Zulko/moviepy
- FFmpeg version: https://softantenna.com/softwares/6998-ffmpeg , https://isitpatched.com/ffmpeg
- Shotstack pricing: https://www.wireflow.ai/blog/shotstack-pricing , https://www.capterra.com/p/212383/Shotstack/
- Jitter pricing: https://www.jitter.video/pricing , https://lottiefiles.com/blog/design-guides-and-tips/best-motion-design-tools-ranked-by-use-case
- Whisper: https://github.com/openai/whisper · WhisperX: https://github.com/m-bain/whisperX · aeneas: https://github.com/readbeyond/aeneas
- Kokoro: https://github.com/hexgrad/kokoro · Rhubarb: https://github.com/DanielSWolf/rhubarb-lip-sync
- MuseTalk: https://github.com/TMElyralab/MuseTalk · LivePortrait: https://github.com/KwaiVGI/LivePortrait · SadTalker: https://sync.so/blog/what-is-sadtalker
- HeyGen pricing: https://www.arcade.software/post/heygen-pricing , https://diyai.io/ai-tools/video-generation/heygen-pricing/ , https://eesel.ai/blog/heygen-pricing
