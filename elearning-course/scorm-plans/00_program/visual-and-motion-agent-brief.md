# Minimal visual scope and AI-agent brief

**For the course owner and external production agents · 14 October 2026**

## Recommendation on the cast

**Do not add more named, recurring characters.** Noor and Dr. Omar already cover all eight packages with approved, consistent designs and planned voice roles. A third speaking character would add another voice, continuity work, image generation, approvals and extra learner focus, without filling a clear gap in the current storyboard.

Keep the learner as the protagonist. Use a small set of **unnamed supporting roles** only when a scene needs them: a new colleague, a generic clinician, a front-office/operations colleague, and an adult patient/visitor. These are scene roles—not character IP. Do not create biographies, names, catchphrases, recurring outfits or AI voices for them. Show them at a distance or in simple flat-vector form. Use varied, modest, culturally appropriate clothing; no real patient/staff likenesses. For the wrong-patient wristband scene, use blank wristbands and put fictional identifiers into an editable layer only after SME/DPO approval.

Continue Noor and Omar according to [`characters/companions.md`](characters/companions.md): reuse the approved Canva master and poses, keep them on about one screen in three at most, and keep them off the interaction area while learners answer. **The 18 full-size images already exist in Canva: they are downloads to obtain, not new character images to generate.** They are our approved design; My Clinic approves the two masters at the Phase 3 gate.

## Visuals to make or approve

The course design is already mostly interactive. Do not turn every screen into a new illustration or video. Use the existing screen plans, interaction visuals and brand components as the baseline.

> **Audit correction (14 October 2026).** The first version of this brief counted only the scene images that the v0.2 storyboard cards reference (12/13). The Phase 3 asset manifests, and proposal Rev01, also need **9 HSE scene images**, **4 client safety photos** and **31 EHR screenshots**, which the generated v0.2 cards for 01, 02 and 08 left out (gap G10 in `programme-status.md`). Rev01 sells HSE "≈26 diagrams and illustrations (… scenario scenes)", "clickable illustrations" of a corridor **and a treatment room**, and "≈35 new screenshots" for EHR. The table below is the corrected minimum that still delivers Rev01.

**G10 implementation update:** the planned visual references have now been restored to modules 01, 02 and 08. The owner selected the **full six-scene drill**. See [g10-visual-restoration.md](g10-visual-restoration.md) for the manifests, regression tests and remaining production gates. No images or screenshots were produced or approved in that fix.

### Minimum asset inventory (delivers Rev01, nothing more)

| # | Asset | Ids | Screens | Route | Count | Gate before making it |
|---|---|---|---|---|---:|---|
| 1 | Companion art (Noor, Dr. Omar) | `char-noor-*`, `char-omar-*` (companions.md §3) | all modules | **Download** from Canva as transparent PNG; no regeneration | 18 | Client approves the two masters at the Phase 3 gate (companions.md §2). The cloud workspace cannot reach Canva downloads: the course owner downloads them. |
| 2 | Avatar crops | `char-noor-avatar-happy`, `-concern`, `char-omar-avatar-happy` | 03, 07, others | Crop from the downloaded poses with `tools/make_companion_avatars.py` | 3 | Row 1 done |
| 3 | HR scene stills | `hr-img-ethics-meeting`, `-corridor`, `-desk`, `hr-img-leavedesk`, `hr-img-idcard`, `hr-img-dress-frontoffice`, `-medical`, `-backoffice` | hr-031, 044, 070, 071 | AI still | 8 | Dress-code images: HR confirms they assert no rule beyond policy |
| 4 | Operations scenes | `ops-img-scenes-2..4` (+ `-1` = existing reception image) | ops-031 | AI still | 3 (4 if reception is rejected) | B7 routing answers closed |
| 5 | Wristband | `qsr-img-wristbands` | qsr-021 | AI still, **blank fields**; identifiers in an editable layer | 1 | 07 B3 (identification goal wording); DPO approves any identifier layer |
| 6 | Six-goal pictograms | `qsr-img-pillars` | qsr-020 | **Editable SVG**, labels in HTML | 1 set | 07 B3 (IPSG wording) and B5 (falls band) |
| 7 | HSE 01 scene stills | `hs1-img-treatment-room`, `hs1-img-pump-label` | hs1-701 (hotspot), hs1-802 (scored scenario) | AI still; pump label dates as an editable overlay | 2 | Facilities / Biomedical confirm items and the label rule |
| 8 | HSE 02 drill scenes | `hs2-img-drill-1..6` | hs2-030 (scored Code Red game, the module's centre) | AI still, one per node | 6 | D1/D2 code names; Safety Manager signs the node list |
| 9 | HSE 02 spill | `hs2-img-spill-photo` | hs2-064 | AI still with a clear volume cue | 1 | D1 Code Orange threshold (the image must match it) |
| 10 | Client safety photos | `hs1-img-eyewash`, `hs2-img-extinguisher`, `hs2-img-kit-chem`, `hs2-img-kit-bio` | hs1-506, hs2-040, hs2-051 | **Photographed by My Clinic** (Rev01: "MY CLINIC provides photos where needed") | 4 | Permission recorded; if not supplied, fall back to an AI still and record the substitution |
| 11 | Leadership row | `hr-img-leaders-ceo/-cmo/-coo/-cfo` | hr-022 | Client photos with consent, **or role tiles** with no faces | 4 or 0 | D5 / B6 decision |
| 12 | Oracle screenshots | `hr-img-oracle-1..5` | hr-061 | Capture in an approved test account, empty or fake data | 5 | B8 |
| 13 | EHR screenshots | `ehr-shot-list`, `-form`, `-dx-1..5`, `-order-1..6`, `-wizard-1..4`, `-summary-1..3`, `-sms-1..5`, `-ref-1..6` | ehr-010 to ehr-050 | Capture in the DPO-approved test environment, fictional patient, 1920×1080 at 125% | 31 (+ up to 4 crops = Rev01's "≈35") | B2/D6; DPO reviews every file |
| 14 | Authored SVG/HTML | HR icons, map, award, benefits wheel, GOSI bar; Ops journey, charts, 14 icons; RCM-B 12 icons; 07 quote, S-P-O, matrix, iceberg; 05 notes; 01/02 diagrams | various | Own SVG/HTML, never an image model | — | Update only with SME-approved facts |
| 15 | Job aids (Rev01 deliverables) | `hr-pdf-quickref`, `rcma-pdf-checklist`, `rcmb-pdf-ebp`, `ehr-pdf-quickref`, emergency-code cards | summary screens | Own PDF from the brand template | 5 | Facts closed in Phase 0 |
| 16 | Existing scenes to **review, not regenerate** | `hs1-img-corridor`, `hs2-img-storeroom`, `ops-img-reception-scenario` | hs1-404, hs2-011, ops-031 | SME review, then set hotspot coordinates | 3 | Answer keys signed |

**New AI-generated stills: 21** if the reception image is approved for reuse (8 HR + 3 Ops + 1 wristband + 2 HSE-01 + 7 HSE-02), otherwise **22**. That is the minimum that keeps every scored scenario and every Rev01 promise illustrated.

**Leaner option, needs SME sign-off:** the Code Red drill can run on **3** scenes instead of 6 (smoke in the room · call point and phone · stairwell and assembly point), with the other nodes shown as text cards. That gives **18 / 19** stills. Do not cut the treatment room (Rev01 names it) or the pump label (it carries a scored decision).

Supporting people in every scene follow the cast rule above: unnamed, non-speaking, modestly dressed, generic flat vector, no likenesses.

## How many videos?

**Rev01 requires zero new standalone videos.** Rev01 lists the EHR walkthrough video only as an *optional service, quoted on request*, and does not mention a Quality clip at all. The storyboard and interactions carry the teaching. Video production beyond those screens is optional, not part of the agreed baseline.

For a small visual lift, I recommend **one optional 45–60 second motion-graphics clip** for the existing `qsr-060` “speak-up” slot, only if the Quality Director approves it under D7 and confirms the incident-reporting rule under D8. It should illustrate a generic near-miss reporting conversation without inventing an incident route, deadline, form or outcome. The approved narration script and exact reporting language must come first. If the approvals or an approved script are not ready, use **zero videos** and keep the native screens. Because `qsr-060` is outside the 22-screen / 95-point baseline and outside Rev01, decide first whether it is a free value-add or a change request; either way it adds one unscored screen and a video asset to package 07.

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

Scope only the listed planned IDs. Produce the pending AI scene illustrations in the "Minimum asset inventory" table: 21 if the visual reviewer approves reuse of the existing Operations reception art (8 HR, 3 other Operations scenes, 1 blank wristband, 2 module-01 scenes, 6 Code Red drill scenes and 1 spill scene), otherwise 22. Make each one only after its gate in that table is closed. If the SME approves the leaner drill option, make 3 drill scenes instead of 6. The `qsr-img-pillars` item is preferably a clean set of six editable, unlabelled SVG pictograms, not an AI-rendered diagram. Do not regenerate the three existing HSE/Operations illustrations or any Noor/Omar character. Do not make client photos, Oracle screens or EHR screens with an image model. The 18 approved character files are to be downloaded from Canva, not redesigned.

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

First close the policy, voice, brand and privacy approvals that affect an asset. Then obtain the character files (once the client approves the masters), generate only the 21–22 stills above (18–19 with the leaner drill option), collect the four client safety photos, and capture software screenshots in approved test systems. Have SMEs review these inputs. Only after that should the optional video agent assemble the single short motion piece. Store prompts, source assets, generated files, licences and reviewer decisions in the project asset register; rerun the planning/asset checks before the SCORM build.

## Sources for the tool choice

[1]: https://hyperframes.heygen.com/introduction "HyperFrames official introduction"
[2]: https://github.com/heygen-com/hyperframes "HyperFrames source repository and README"
[3]: https://www.remotion.dev/docs/the-fundamentals "Remotion official fundamentals"
[4]: https://www.remotion.dev/docs/render "Remotion official render documentation"
