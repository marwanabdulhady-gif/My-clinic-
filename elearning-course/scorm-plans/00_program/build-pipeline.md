# Build pipeline and SCORM settings (all modules)

This is the exact sequence Claude (the MCP client) follows for each package. Tool names are the edumints MCP tools listed in the server (`server.py`).

## 1. Tool sequence per module

| Step | Phase | Tool(s) | Output kept in the repo |
|---|---|---|---|
| 1 | 1 | `get_playbook('overview')`, `list_screen_types`, `list_themes` | — |
| 2 | 1 | `get_playbook('reference')`, `get_playbook('authoring')` | `authoring-plan.json` (draft) |
| 3 | 2 | `brand_to_theme(brand)` (once for the program) | `00_program/theme_tokens.json` |
| 4 | 2 | `lint_visual_plan(plan, brand)` | `visual-plan.json` + lint report |
| 5 | 3 | `lint_narration_script(script, plan)` → `export_audio_script(script)` | `narration-script.json`, `voice_talent.md` |
| 6 | 3 | `lint_authoring_plan(plan, stage="planning")` | lint report |
| 7 | 3 | **STOP — human approval** of storyboard, visuals, narration, activities | approval record in `phase-5-qa-and-delivery.md` |
| 8 | 4 | `lint_authoring_plan(plan, stage="production")` | lint report |
| 9 | 4 | `create_project` → `set_theme` → `set_tracking` | `project_id` |
| 10 | 4 | `svg_to_asset` (diagrams), `add_asset` (photos, audio, video, PDF), `normalize_audio_asset` (all narration) | asset map (`planned_id → asset_id`) |
| 11 | 4 | `add_screen` × N (or `build_from_spec(spec)` for the whole module) | `course-spec.json` |
| 12 | 4 | `lint_course(project_id)` → fix → `preview(project_id)` | lint report, preview notes |
| 13 | 5 | `lint_authoring_plan(plan, stage="delivery")` | lint report |
| 14 | 5 | `build_package(project_id)` → `validate_package` | SCORM zip (stored outside Git) |
| 15 | 5 | `export_qti(project_id)` (optional, for the question bank) | QTI 2.1 zip |

Planning files (`visual-plan.json`, `narration-script.json`, `authoring-plan.json`, `course-spec.json`) are saved in each module folder under `build/` when Phase 2–4 start. Built SCORM zips and media are **not** committed (size); store them in Drive with the version number.

## 2. Course-level settings (defaults)

| Setting | Value | Why |
|---|---|---|
| `language` | `"en"` | **Required.** The server default is `"tr"`. |
| `scorm_version` | `"2004"` for 01, 03 (long, many interactions); `"1.2"` for the others | SCORM 1.2 limits `suspend_data` to 4,096 characters; long modules risk losing resume state. Switch all to `"1.2"` only if the LMS cannot run 2004. **Confirm the LMS in Phase 0.** |
| `layout_mode` | `"stage"` (16:9, 960×540) | Matches the source decks; the player reflows on small screens. |
| `theme` | program theme tokens + `style-minimal` | See `brand-and-theme.md`. |
| `theme_mode` | `"light"` | |
| `tracking.completion_rule` | `"viewed_all_and_passed"` for compliance modules (01, 02, 07, 08); see each module's Phase 4 | Proves exposure *and* competence. |
| `tracking.passing_score` | 80 (compliance) / 70 (orientation) | Set per module. |
| `objectives` | one per Phase 1 objective, ids like `hs1-o1` | Feeds `cmi.objectives` for LMS reporting. |
| `outline` | one `section` node per storyboard section, `unlock_rule: "free"` | Section menu; avoid `sequential` for experienced re-takers. |
| `metadata` | title, description, keywords, version, owner | LOM metadata in the manifest. |
| `xapi` | off (release 1) | Turn on only if an LRS exists. |

Screen-level defaults:

- Every screen has a `section` matching the outline node and a `narration_text` when it has audio.
- Question screens: `lock_until_complete: false`.
- Scored screens carry `objective_ids` (so the LMS shows results per objective) and `points` (default weights in each Phase 4).
- Ids: `<module-prefix>-<section><nn>`, for example `hs1-402`. Ids are permanent once built; never reuse an id for a different screen.

## 3. Naming and versioning

- Project title: `My Clinic — <module title>`.
- Package file: `MC_<NN>_<short-name>_v<major>.<minor>_<scorm>.zip`, e.g. `MC_01_FMS_v1.0_2004.zip`.
- Version bump: **minor** for text/media fixes (LMS keeps learner records), **major** when scored screens or objectives change (re-import as a new activity in the LMS).

## 4. Known server limits to design around

From the edumints `docs/OPERATIONS-COURSE-ROADMAP.md` and playbook. The plans only use **supported** screen types.

| Limit | Effect on these plans |
|---|---|
| No `process_flow`, `hub` or `canvas_slide` screen | Processes use `sorting`, `timeline`, `worked_example`, `labeled_diagram` (display) or an authored SVG. |
| No final-exam pool, draw count or attempt limits | Each module has a **fixed** set of scored checks. Retakes are controlled in the LMS (attempt settings). |
| `lock_until_complete` does not reliably wait for audio to end | Do not rely on it for compliance. Completion = `viewed_all_and_passed`. |
| Cue markers are estimates, not measured timings | Keep blocks in narration order; check reveal timing in preview. |
| `poly` hotspot regions are rejected at build | Use `rect` or `circle` regions only. |
| Piper TTS in the Docker image has a Turkish voice only | English narration needs an external TTS or a human voice (see `narration-and-lexicon.md`). |
| `render_motion_video` max 60 s, 1920×1080 | Longer videos (module 08 walkthrough) are made outside the server and uploaded with `add_asset`. |
| Arabic player strings not localised | See `brand-and-theme.md` §6. |

## 5. Asset provenance (required)

Every image, audio and video file needs a provenance record. Allowed `source`: `ai-generated`, `cc0`, `public-domain`, `own`, `local`. Anything else is rejected.

```json
{ "asset": "img/hs1-ghs-pictograms.svg", "source": "own", "license": "My Clinic internal",
  "url": "", "author": "My Clinic course team", "retrieved_at": "2026-10-14", "license_url": "" }
```

- GHS pictograms are UN-published symbols; redraw as own SVG or use a CC0 set and record it.
- NFPA 704 diamond: draw your own generic diamond (the NFPA mark is a standard; do not copy a vendor's chart).
- Source-deck images (PDF/PPTX) are `local` **only after** Phase 0 confirms My Clinic owns them.
