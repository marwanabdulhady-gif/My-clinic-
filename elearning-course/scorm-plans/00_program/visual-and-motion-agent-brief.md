# Minimal visual scope and AI-agent brief

**For the course owner and external production agents · 14 October 2026**

## Recommendation on the cast

**Do not add more named, recurring characters.** Noor and Dr. Omar already cover all eight packages with approved, consistent designs and planned voice roles. A third speaking character would add another voice, continuity work, image generation, approvals and extra learner focus, without filling a clear gap in the current storyboard.

Keep the learner as the protagonist. Use a small set of **unnamed supporting roles** only when a scene needs them: a new colleague, a generic clinician, a front-office/operations colleague, and an adult patient/visitor. These are scene roles—not character IP. Do not create biographies, names, catchphrases, recurring outfits or AI voices for them. Show them at a distance or in simple flat-vector form. Use varied, modest, culturally appropriate clothing; no real patient/staff likenesses. For the wrong-patient wristband scene, use blank wristbands and put fictional identifiers into an editable layer only after SME/DPO approval.

Continue Noor and Omar according to [`characters/companions.md`](characters/companions.md): reuse the approved Canva master and poses, keep them on about one screen in three at most, and keep them off the interaction area while learners answer. **The 18 approved full-size images are downloads to obtain, not new character images to generate.**

## Visuals to make or approve

The course design is already mostly interactive. Do not turn every screen into a new illustration or video. Use the existing screen plans, interaction visuals and brand components as the baseline.

### Generate or produce next

1. **Download the 18 approved Noor/Omar PNGs from Canva** to `00_program/characters/assets/`. Use the existing media ids and transparent-PNG export directions in the character bible. These are approved artwork, not re-generation tasks. The interim avatar crops are for review only.
2. **Make 8 HR illustrations** from [`visual-generation-prompts.md`](visual-generation-prompts.md): three ethics context scenes for `hr-031`; the desk for `hr-044`; blank badge for `hr-070`; and three generic clothing examples for `hr-071`. Keep each image separate. HR/Marketing must confirm that the outfit illustrations do not assert dress rules beyond policy.
3. **Make up to 4 Operations context illustrations** for `ops-031`: reception, phone follow-up, insurance call and pharmacy queue. The existing `ops-img-reception-scenario.png` depicts the planned reception node and already has a storyboard prompt. First have the visual reviewer/SME confirm it fits; if approved, map it to the reception node and generate only the other 3 images. B7 must be closed before any image is paired with a definitive role-routing answer.
4. **Make 1 Clinical Governance wristband illustration** for `qsr-021`, with blank fields only. For the `qsr-020` six-goal visual, prefer six simple, editable SVG pictograms and add the approved words/labels in the course layer. Use the prompt-catalogue image version only if Quality approves it as a decorative, unlabelled visual.
5. **Capture HR Oracle visuals:** 5 screenshots are listed for `hr-061`. Capture only in an approved test account after B8 is cleared, and use empty/fake data. Do not generate or imitate Oracle screens with an image model.
6. **Capture EHR simulation visuals:** create a step-by-step capture manifest for the seven simulations after B2/D6 are cleared. The current register has not enumerated the exact number of screenshots each interaction step requires. Use the current test environment and fictional test patient, then obtain DPO approval. Never use the source `IT.mp4` or a real patient record.
7. **Finish authored graphics:** use editable SVG/HTML rather than an image model for labeled diagrams and data. The module asset registers describe the HR icon/map/award/benefit assets, Operations role/journey diagrams and icons, the 12 RCM Part B benefit icons, and Quality's process/risk/incident diagrams. Existing native SVG drafts should be updated only with SME-approved facts; do not redraw them as raster art.

The other existing visual files—HSE corridor, Safety Lab storeroom and Operations reception—are already generated. Get the relevant SME to review them before setting hotspot coordinates or finalizing answer feedback. Module 05's weak/strong note cards and reviewer graphic are already native SVGs. The guide [`visual-production-plan.md`](visual-production-plan.md) and the eight package asset registers remain the exact asset-id and placement sources.

**Minimum new scene-illustration count:** 12 AI-generated stills if the existing reception image is approved for reuse (8 HR + 3 further Operations scenes + 1 wristband); otherwise 13. There are 14 briefs in the current prompt catalogue because it also includes an optional Quality pictogram set; making that as editable SVG is the recommended minimal route. This count excludes the 18 approved companion downloads, test-account screenshots, editable SVG assets and icons. Keep the asset register's planned IDs intact until the reuse/alias mapping is approved.

## How many videos?

**Rev01 requires zero new standalone videos.** The storyboard and interactions carry the teaching. Video production beyond those screens is optional, not part of the agreed baseline.

For a small visual lift, I recommend **one optional 45–60 second motion-graphics clip** for the existing `qsr-060` “speak-up” slot, only if the Quality Director approves it under D7 and confirms the incident-reporting rule under D8. It should illustrate a generic near-miss reporting conversation without inventing an incident route, deadline, form or outcome. The approved narration script and exact reporting language must come first. If the approvals or an approved script are not ready, use **zero videos** and keep the native screens.

The other existing optional slot is `ehr-060`, a screen-recorded walkthrough. Skip it for the minimal version because the core course already has seven guided EHR simulations. If IT later confirms that learners need it, make it as a separately approved screen recording from the DPO-cleared fictional test-patient environment—not as generative video and not from `IT.mp4`. The two optional assets are already described in [`scorm-structure.md`](scorm-structure.md); adding one changes the screen/video package and needs a scope check.

Do not make an opening video for every package, repeated logo stings, or one clip per module. A light static title with the approved guide art and a small amount of motion on selected SVG assets is enough.

## Motion-graphics tool choice

For the proposed one short, brand-led clip, **use HyperFrames** if your agents are comfortable producing HTML/CSS/JavaScript. Its official documentation describes an agent-built, editable HTML video project and frame-by-frame deterministic rendering; its CLI supports local preview and MP4 rendering.[1] [2] This suits a short, repeatable motion piece assembled from the existing character PNGs, editable SVGs, brand type, and approved narration.

The current HyperFrames repository lists Node.js 22+ and FFmpeg as requirements. Its starter workflow is `npx hyperframes init mc-qsr060`, then `npx hyperframes preview` and `npx hyperframes render` from the project folder.[2] Keep the video project self-contained: copy in the approved PNGs/SVGs/audio and fonts, and do not rely on remote assets at render time.

Use **Remotion instead** if the agent team already works in React/TypeScript or expects to make many data-driven variants. Remotion defines a video as React-rendered frames with explicit width, height, duration-in-frames and fps, and its CLI renders a selected composition.[3] [4] Do not author the same clip in both systems. Pick one pipeline, check the current production license and renderer requirements, and retain editable source with the exported video.

## Instructions for the agents

### 1. Image agent — still assets only

```text
Project: My Clinic KSA (Saudi outpatient healthcare) e-learning. Read brand/brand-identity.md, characters/companions.md, visual-production-plan.md, visual-generation-prompts.md, and the target module storyboard card and asset-register row before you start.

Scope only the listed planned IDs. Produce 12 pending AI scene illustrations if the visual reviewer approves reuse of the existing Operations reception art (8 HR, 3 other Operations scenes, and 1 blank wristband); otherwise produce 13 by adding a new reception scene. The `qsr-img-pillars` item is preferably a clean set of six editable, unlabelled SVG pictograms, not an AI-rendered diagram. Do not regenerate the three existing HSE/Operations illustrations or any Noor/Omar character. The 18 approved character files are to be downloaded from Canva, not redesigned.

Follow the My Clinic flat-vector style and the asset-specific prompts. Use generic, anonymous, modestly dressed adults only; no named people, invented policies, patient/staff likenesses, text, logos, identifiers or screen UI. Do not add hazards, medicine or equipment beyond the asset brief. Keep diagrams, labels, numbers and exact facts editable as SVG/HTML. For every file return the requested asset ID, screen ID, source/editable file, PNG preview, actual prompt, generator/model, date and a short note of anything needing SME review. Do not mark an asset approved; only the named My Clinic SME can do that.
```

### 2. Audio agent — narration only

```text
Use only the package's current audio-script-export.json. Follow narration-production-plan.md and narration-and-lexicon.md. Speak the exact supplied TTS text; do not paraphrase, translate, add connective speech, read speaker labels or improvise a pronunciation. Keep Noor and Dr. Omar as two distinct fixed voices. If D10 is still open or a voice id is unapproved, stop and return a blocked-items list rather than choosing a voice. Generate one traceable segment per exported part, with the package/screen/part id in the filename and metadata. Return the provider/model, licensed voice id, text hash, duration, date and settings. Do not synthesize additional patient/colleague voices. Captions/transcripts must match the approved script exactly. Do not generate narration for the optional qsr-060 video until its script and D7/D8 approvals are recorded.
```

### 3. Motion-graphics agent — one optional video, not eight

```text
Create a source-editable HyperFrames project for the approved optional My Clinic asset qsr-060 only, if the owner provides a closed D7/D8 decision, approved storyboard copy, approved Noor art and approved audio. If any input is missing, do not invent or publish content; return a blocked-input list. Target 16:9, 1920×1080, 30 fps, 45–60 seconds, H.264 MP4 plus the editable HyperFrames source, exact transcript and WebVTT captions.

Use only supplied assets: approved Noor transparent PNGs, separately approved generic scenario illustrations, My Clinic's original logo PNG, Montserrat/brand palette, and the approved generated narration audio. Do not generate a new face/character, fake a patient chart, use real footage, use an image model to write text, copy NotebookLM/source-video frames, or add music that masks speech. No lip-sync is needed: use restrained 2D movement (slow position/scale, fades, line reveals and icon changes) on approved static assets. Keep one visual focus at a time; allow reading holds; keep captions and key content inside mobile-safe margins. Show no new policy, reporting route, deadline or answer beyond the exact signed-off script and course screen.

Supply a 5–7 beat timeline, source project, rendered preview and final MP4, captions, transcript, asset manifest, prompts, render settings, and a frame-based list of any concerns. Preview the opening, every stable text hold, each transition and the ending. Check the full clip for legibility, timing, character consistency, sound/caption sync and absence of patient data. Do not insert it into the SCORM package or mark it approved; the course owner and Quality Director review it first.
```

### Build and QA order

First close the policy, voice, brand and privacy approvals that affect an asset. Then obtain the already approved character files, generate only the 13 stills above, and capture software screenshots in approved test systems. Have SMEs review these inputs. Only after that should the optional video agent assemble the single short motion piece. Store prompts, source assets, generated files, licences and reviewer decisions in the project asset register; rerun the planning/asset checks before the SCORM build.

## Sources for the tool choice

[1]: https://hyperframes.heygen.com/introduction "HyperFrames official introduction"
[2]: https://github.com/heygen-com/hyperframes "HyperFrames source repository and README"
[3]: https://www.remotion.dev/docs/the-fundamentals "Remotion official fundamentals"
[4]: https://www.remotion.dev/docs/render "Remotion official render documentation"
