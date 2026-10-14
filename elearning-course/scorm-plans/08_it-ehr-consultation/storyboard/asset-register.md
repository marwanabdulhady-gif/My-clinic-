# Visual and audio asset register

This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `ehr-capture-sheet` | [`assets/ehr-capture-sheet.svg`](assets/ehr-capture-sheet.svg) | diagram | own | Generated capture checklist only; not an EHR screenshot and not a substitute for B2 test-environment assets. | Checklist showing safe test-environment screenshot requirements. |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note |
|---|---|---|---|---|---|
| `ehr-pdf-quickref` | PDF | ehr-091 | 1-page EHR consultation quick-reference card | own | n/a |
| `ehr-vid-walkthrough (optional)` | MP4 + VTT | ehr-060 | Screen recording on test patient + voice-over; rendered outside the server (over the 60 s render_motion_video limit), uploaded with add_asset | own | transcript |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.
- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.
- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.
- Keep diagrams as SVG/HTML where factual text needs revision after SME review.
