# Visual and audio asset register

This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `rcmb-img-benefit-icons` | [`assets/rcmb-img-benefit-icons.svg`](assets/rcmb-img-benefit-icons.svg) | icon | own | Generated native icon sheet; labels remain HTML in the course. | A set of generic line icons for health benefits. |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note | Placement | Production gate |
|---|---|---|---|---|---|---|---|
| `rcmb-img-benefit-icons` | SVG ×12 | rcmb-010, 020, 040 | Line icons per benefit | own | decorative | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcmb-tbl-log` | HTML table | rcmb-050, 051 | Rebuilt rejection rows (B8); invented ids CLM-0001…; no names, dates or providers | own | n/a | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `rcmb-pdf-ebp` | PDF | rcmb-091 | One-page EBP summary from the official document (B3), approved by payer relations | own | n/a | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `char-noor-*` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |
| `char-omar-*` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." | Screen visual; production placement reviewed by the SME. | PENDING relevant Phase 0 and SME visual approval; provenance recorded before production. |

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.
- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.
- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.
- Keep diagrams as SVG/HTML where factual text needs revision after SME review.
