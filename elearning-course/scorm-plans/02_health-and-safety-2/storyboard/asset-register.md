# Visual and audio asset register

This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `hs2-img-storeroom` | [`assets/hs2-img-storeroom.png`](assets/hs2-img-storeroom.png) | illustration | ai-generated | Generated 2026-10-14 — Safety Manager must confirm the six-hotspot answer key before use. | Clinic store room with cables, high boxes, blocked exit, unlabelled bottle, spill by socket and a person on a wheeled chair. |
| `hs2-img-floorplan` | [`assets/hs2-img-floorplan.svg`](assets/hs2-img-floorplan.svg) | diagram | own | Generated native generic floor-plan SVG; never a real floor plan. | Generic evacuation floor plan with zones A to E. |
| `hs2-img-nfpa-230` | [`assets/hs2-img-nfpa-230.svg`](assets/hs2-img-nfpa-230.svg) | diagram | own | Generated native SVG. | NFPA diamond with health 2, flammability 3 and reactivity 0. |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note |
|---|---|---|---|---|---|
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.
- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.
- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.
- Keep diagrams as SVG/HTML where factual text needs revision after SME review.
