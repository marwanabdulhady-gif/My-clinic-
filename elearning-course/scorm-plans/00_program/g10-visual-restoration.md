# G10 — restore planned visuals to the review packs

**14 October 2026 · planning-reference fix implemented. Final assets remain pending.**

This implements the corrected inventory in [PR #37](https://github.com/marwanabdulhady-gif/My-clinic-/pull/37)
and [visual-and-motion-agent-brief.md](visual-and-motion-agent-brief.md). The selected scope is the
**full six-scene Code Red drill**, not the lean three-scene alternative. No additional named
characters, voices or required videos are introduced. PR #37's audited brief is now merged
and superseded PR #36 is closed. A merge does not constitute client approval of the assets.

## Restored references

| Module | Core screens | Restored visual handoff |
|---|---|---|
| 01 | `hs1-506`, `hs1-701`, `hs1-802` | My Clinic eyewash photo, treatment-room illustration, infusion-pump scene with editable inspection-label overlay |
| 02 | `hs2-030` | All six individually identified drill scenes, one per authored node |
| 02 | `hs2-040`, `hs2-051`, `hs2-064` | Client extinguisher photo, both chemical/biological kit photos, spill scene; register/NFPA clues retained on the escape-room screen |
| 08 | `ehr-010`, `ehr-011`, `ehr-020`, `ehr-031`, `ehr-032`, `ehr-040`, `ehr-041`, `ehr-050` | 31 unique test-environment shots; consultation form reused on the mandatory-field exploration |

Every planned Phase 3 visual on these modules' core screens now has its ID, brief, placement,
draft alt text and production gate in the visual plan/card and asset register. Build JSON notes
carry placeholder IDs and placement instructions; they are **not** final type-specific screen
schemas, measured hotspot regions or uploaded production asset IDs. No branches or answer keys
were invented to make the pending drill or EHR simulation look complete.

### Six-scene Code Red drill (`hs2-030`)

1. `hs2-img-drill-1` — consultation-room smoke / rescue.
2. `hs2-img-drill-2` — call point and phone / alarm.
3. `hs2-img-drill-3` — oxygen cylinder, alcohol rub and door / contain.
4. `hs2-img-drill-4` — small bin fire and spreading-fire state / extinguish or evacuate.
5. `hs2-img-drill-5` — stairwell and evacuation chair / evacuate.
6. `hs2-img-drill-6` — generic assembly point / wait for all-clear.

See [drill-scene-manifest.json](../02_health-and-safety-2/storyboard/drill-scene-manifest.json).
These are six planned base illustrations. The authored small-versus-spreading-fire decision
needs reviewed state layers; the manifest does not silently commission a seventh base scene.
Code/script wording is editable text; the Safety Manager must approve all six node treatments
and relevant D1/D2/B2/B8 decisions before images and final game targets are made.

### EHR captures

See [capture-manifest.json](../08_it-ehr-consultation/storyboard/capture-manifest.json):
**2 open/form + 5 diagnosis + 6 medication + 4 wizard + 3 summary + 5 SMS + 6 referral = 31**.
The form is reused by `ehr-011`, not counted twice. Up to four crops are reserved for legibility
review (~35), not extra workflow steps. No crop IDs or extra simulation nodes are invented.

All captures remain planned: DPO approval and EHR version are unset. Only an approved test
environment with fictional demographics, record numbers and phone may be captured. `IT.mp4`
and its frames are not reused. Instructions, examples, screen names, mandatory fields, SMS
functionality and referral timing retain their module 08 SME gates.

## Root-cause fixes / regression protection

- Phase 3 parser now accepts numeric screen prefixes (`hs1`, `hs2`) and `ehr-shot-*` rows.
- Grouped ranges and slash-separated asset IDs expand to individually trackable IDs.
- Compact shared-screen lists (`ehr-010, 011`, `hs2-060, 062, 063, 064`) resolve correctly.
- Visual-plan generation includes **all** mapped visuals, rather than breaking after the first;
  actual generated artwork is deduplicated rather than repeated as a second planned image.
- Review boards and the local preview show planned scene/capture slots without broken file links
  or pretending those images already exist.
- SCORM structure descriptions include the planned screenshots but exclude optional video
  assets whose screens are not in the core storyboard. This is still a planned structure, not a ZIP.
- Seven new G10 regression tests cover these failures and the six-scene/31-shot invariants.

## Reproduce the amended review pack

From the repository root (Word export/audit need `tools/requirements-docx.txt` in a venv):

```bash
python3 elearning-course/scorm-plans/tools/assemble_storyboard_docs.py \
  01_health-and-safety-1 02_health-and-safety-2 08_it-ehr-consultation
python3 elearning-course/scorm-plans/tools/lint_planning.py
python3 elearning-course/scorm-plans/tools/build_scorm_structure.py \
  01_health-and-safety-1 02_health-and-safety-2 08_it-ehr-consultation
python3 elearning-course/scorm-plans/tools/export_storyboard_docx.py \
  01_health-and-safety-1 02_health-and-safety-2 08_it-ehr-consultation
python3 elearning-course/scorm-plans/tools/audit_assets.py
python3 -m unittest discover -s elearning-course/scorm-plans/tools/tests -v
python3 elearning-course/scorm-plans/tools/generate_screens.py
node elearning-course/scorm-plans/tools/tests/test_scenario.cjs
```

Selective Word exports retain the full client-review index and kick-off link. Selective structure
exports retain the all-eight summary. Unaffected module storyboards and narration exports are
not regenerated for this correction. The affected three modules' narration/script/voice exports
are byte-for-byte unchanged by this pass.

## Validation and release boundary

- **15 Python tests pass** (8 existing + 7 G10).
- All eight planning packs: **0 errors / 0 warnings**; asset/link audit: **0 hard failures**.
- Baseline remains **207 screens, 95 scored activities, 26 experiences**; screen order/types,
  points, objectives and pass marks unchanged. No optional video screen is added.
- Browser smoke checks all 207 screens and visible six-scene/six-step capture slots, including
  shared-form placement; existing draft interactions and mobile/keyboard checks still pass.
- The three module Word review documents and programme overview were regenerated. Their
  asset descriptions remain planning instructions, not pictures or screenshot evidence.

## Next approval handoff prepared

The [asset approval handoff](asset-approval-handoff/README.md) and its response template now
cover **44 pending rows: 13 safety visuals (including all six drill scenes) and 31 EHR shots**.
The packet has not been sent; no reviewer names, signed decisions or approvals are recorded.
Generate it with `tools/prepare_asset_approval_handoff.py`. The generator refuses to overwrite
human responses. The course owner must route it to named Safety/Facilities/Biomedical and
EHR/DPO reviewers, then record their written decisions in Phase 0 before producing assets.

**Still needed:** client decisions, scene/photo production and permissions, Safety/EHR/DPO
review, approved character downloads, final audio, production game/simulation fields, asset
uploads/provenance, upstream lint/build, LMS testing and pilot. G10 is resolved only as a
missing-reference/documentation gap, not as an asset-production or launch-readiness gate.
