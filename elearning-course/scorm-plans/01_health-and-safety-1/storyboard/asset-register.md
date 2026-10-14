# Visual and audio asset register

This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `hs1-img-corridor` | [`assets/hs1-img-corridor.png`](assets/hs1-img-corridor.png) | illustration | ai-generated | Generated 2026-10-14 — SME visual check required before hotspot coordinates are set. | Clinic corridor showing a call point, extinguisher, fire blanket, sprinkler, evacuation chair and assembly sign. |
| `hs1-img-arec` | [`assets/hs1-img-arec.svg`](assets/hs1-img-arec.svg) | diagram | own | Generated native SVG. | AREC cycle: Anticipate, Recognise, Evaluate, Control. |
| `hs1-img-ert` | [`assets/hs1-img-ert.svg`](assets/hs1-img-ert.svg) | diagram | own | Generated native SVG. | Emergency Response Team roles around an Incident Commander. |
| `hs1-img-triangle` | [`assets/hs1-img-triangle.svg`](assets/hs1-img-triangle.svg) | diagram | own | Generated native SVG. | Fire triangle showing heat, fuel and oxygen. |
| `hs1-img-alara` | [`assets/hs1-img-alara.svg`](assets/hs1-img-alara.svg) | diagram | own | Generated native SVG. | ALARA diagram showing time, distance and shielding. |
| `hs1-img-nfpa-blank` | [`assets/hs1-img-nfpa-blank.svg`](assets/hs1-img-nfpa-blank.svg) | diagram | own | Generated native SVG. | Blank four-quadrant NFPA diamond. |
| `hs1-img-nfpa-301w` | [`assets/hs1-img-nfpa-301w.svg`](assets/hs1-img-nfpa-301w.svg) | diagram | own | Generated native SVG. | NFPA diamond with ratings 3, 0, 1 and W. |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note |
|---|---|---|---|---|---|
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |
| `hs1-aud-` | narration audio | all narrated screens | One MP3 per segment, file names from export_audio_script | ai-generated (TTS) | transcript = narration_text |

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.
- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.
- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.
- Keep diagrams as SVG/HTML where factual text needs revision after SME review.
