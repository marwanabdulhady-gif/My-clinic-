# Visual and audio asset register

This register is the production hand-off for review. `Generated` means the file is in this repository; `planned` means it must still be approved or supplied. Every asset still needs the final `add_asset` provenance record during Phase 4.

## Generated in this review pack

| Asset id | File | Kind | Provenance | Status | Alt text |
|---|---|---|---|---|---|
| `ops-img-reception-scenario` | [`assets/ops-img-reception-scenario.png`](assets/ops-img-reception-scenario.png) | illustration | ai-generated | Generated 2026-10-14 — generic fictional scene; final routing remains subject to B7. | A patient talks to a patient-experience officer at a clinic reception desk. |
| `ops-img-journey` | [`assets/ops-img-journey.svg`](assets/ops-img-journey.svg) | diagram | own | Generated native SVG. | Patient journey from booking to follow-up. |
| `ops-img-ops-chart` | [`assets/ops-img-ops-chart.svg`](assets/ops-img-ops-chart.svg) | diagram | own | Generated role-only draft SVG; SME approval B1 required. | Draft Operations role structure. |
| `ops-img-mycare-chart` | [`assets/ops-img-mycare-chart.svg`](assets/ops-img-mycare-chart.svg) | diagram | own | Generated role-only draft SVG; SME approval B2 required. | Draft My Care role structure. |

## Planned assets from Phase 3

| Planned id | Kind | Screens | Brief | Source route | Alt text / accessibility note |
|---|---|---|---|---|---|
| `ops-img-journey` | SVG | ops-002 | 6-stage horizontal journey, icons, team colour tags + text labels | own | "Patient journey from booking to follow-up." |
| `ops-img-ops-chart` | SVG | ops-011 | Role-only Operations chart (from B1) | own | "Operations structure by role." |
| `ops-img-mycare-chart` | SVG | ops-021 | Role-only My Care chart (from B2) | own | "My Care structure by role." |
| `ops-img-activities` | SVG icons ×14 | ops-010, ops-020 | Line icons; slide 2/5 "sticky note" style not copied | own | decorative |
| `ops-img-scenes-1..4` | illustrations | ops-031 | Reception, phone follow-up, insurance call, pharmacy queue | ai-generated | per scene |
| `char-noor- / char-omar-` | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |

## Non-negotiable production rules

- Use the supplied My Clinic logo PNGs; never generate, redraw or bake the logo into an AI image.
- AI images contain no text, letters, numbers, brand names or patient/staff likenesses. Review every generated image before it becomes an interaction asset.
- Module 08 only uses newly captured screenshots from a test environment after DPO review. This repository contains no simulated production patient record.
- Keep diagrams as SVG/HTML where factual text needs revision after SME review.
