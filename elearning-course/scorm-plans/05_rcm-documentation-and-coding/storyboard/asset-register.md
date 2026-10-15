# Visual and audio asset register

This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `rcma-img-note-weak` | [`assets/rcma-img-note-weak.svg`](assets/rcma-img-note-weak.svg) | diagram | own | Generated native SVG using fictional teaching text. | Weak generic clinical note stating only that IV fluids were given. |
| `rcma-img-note-strong` | [`assets/rcma-img-note-strong.svg`](assets/rcma-img-note-strong.svg) | diagram | own | Generated native SVG using fictional teaching text. | Stronger generic clinical note linking dehydration signs to IV fluids. |
| `rcma-img-reviewer` | [`assets/rcma-img-reviewer.svg`](assets/rcma-img-reviewer.svg) | diagram | own | Generated native SVG. | A reviewer sees a written note rather than the patient encounter. |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note | Placement | Production gate |
|---|---|---|---|---|---|---|---|
| `rcma-img-note-weak` | SVG note cards | rcma-011 | Two identical-size EHR-style note cards (generic, no vendor UI), weak vs strong text | own | "Weak note: patient given IV fluids." / "Strong note: dehydration signs, IV fluids for stabilisation." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `-strong` | SVG note cards | rcma-011 | Two identical-size EHR-style note cards (generic, no vendor UI), weak vs strong text | own | "Weak note: patient given IV fluids." / "Strong note: dehydration signs, IV fluids for stabilisation." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcma-img-reviewer` | SVG | rcma-001 | Minimal illustration: note on one side, reviewer with only the paper on the other | own | "A reviewer sees only the written note." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcma-img-notes-1` | HTML | rcma-050 | Invented notes in HTML (real text) | own | n/a | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcma-img-notes-2` | HTML | rcma-050 | Invented notes in HTML (real text) | own | n/a | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcma-img-notes-3` | HTML | rcma-050 | Invented notes in HTML (real text) | own | n/a | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcma-pdf-checklist` | PDF | rcma-091 | One-page "Clear, strong, defensible" desk checklist | own | n/a | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `char-noor-*` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `char-omar-*` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.
- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.
- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.
- Keep diagrams as SVG/HTML where factual text needs revision after SME review.
