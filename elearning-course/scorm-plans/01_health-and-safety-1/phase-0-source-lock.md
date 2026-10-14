# Phase 0 — Source lock (01 Facility Management & Safety)

**Goal:** every fact that will appear on a screen or in a question is confirmed by its owner before storyboarding is final.

## 1. Owners

| Role | Responsibility |
|---|---|
| Safety & Security Manager (SME lead) | Codes, fire, hazmat, security, utility; signs off the module |
| Biomedical Engineering lead | Section 8 (labels, PPM, out-of-service, oxygen network) |
| Radiation Safety Officer (RSO) | Section 9 (dose limits, investigation levels, OSL, laser classes) |
| Facilities / Engineering | Section 7 (emergency sockets colour, RO plant, shut-off valves) |
| Course owner (L&D) | Scope, seat time, LMS |

## 2. Blocking items

| # | Item | Source location | Needed decision | Owner | Status |
|---|---|---|---|---|---|
| B1 | Code Orange threshold | p.40 vs H&S 2 p.22 | See program decision **D1** | Safety Manager | Open |
| B2 | Code names and extension numbers (11 codes + 2 announcements) | pp.17–19 | See **D2**. Need the facility's code poster. | Safety Manager | Open |
| B3 | `[Facility Name]`, `[Month Year]` placeholders | p.1 | Facility name(s) to show; or "My Clinic" generic | L&D | Open |
| B4 | Radiation dose limits and bands (2 mSv / 3 months, 20 mSv / year; 1.25 / 1.25–3.75 / > 3.75 mSv) | p.59 | Confirm against current national regulation and facility policy; confirm whether the bands are per quarter | RSO | Open |
| B5 | Laser class table wording ("3" vs "3R" vs "3B") | p.61 | Confirm current IEC class names used at the facility | RSO | Open |
| B6 | Emergency (red) socket colour and generator timing ("within seconds") | p.46 | Confirm for each branch | Facilities | Open |
| B7 | Waste segregation bin colours | p.41 | The deck says colours vary; get the facility's bin colours so the drag-and-drop matches real bins | Infection Control / EHS | Open |
| B8 | Department Safety Liaison list | p.14 | Not needed on screen; learners are told to ask their supervisor. Confirm the wording. | Safety Manager | Open |
| B9 | Accreditation references (CBAHI chapter name, ISO 45001 rights) | pp.3, 15 | Confirm current CBAHI edition and wording | Quality / Accreditation | Open |
| B10 | Completion actions (acknowledgement form, evacuation route, numbers) | p.65 | How the acknowledgement is captured (see **D14**) | L&D | Open |

## 3. Non-blocking items (fix during Phase 2–3)

- The ISO 45001 rights text is duplicated in the PDF text layer (p.15). Use the single version in the source Markdown.
- Image reuse: 199 embedded images in the PDF. Confirm whether My Clinic owns them (PptxGenJS export suggests an in-house build). Until confirmed, plan **own SVG** replacements (see Phase 3 asset list).
- Course name: "Facility Management & Safety" — keep.

## 4. Verified facts register (fill as owners confirm)

| Fact used on screen | Value | Source | Confirmed by | Date |
|---|---|---|---|---|
| Code Blue extension | 2222 (national) | p.17–18 | | |
| Other code extensions | *pending D2* | | | |
| Code Orange trigger | *pending D1* | | | |
| Eyewash flush time | ≥ 15 minutes | p.39 | | |
| Sharps | never recap | p.41 | | |
| Evacuation | stairwells, never elevators | p.29 | | |
| Quarterly dose limit | *pending B4* | | | |
| Annual dose limit | *pending B4* | | | |
| Extinguisher agent ↔ fire table | p.27 | p.27 | | |
| Extinguisher classes A, B, C, D, K | p.28 | p.28 | | |

## 5. Exit criteria

- B1–B7 closed in writing; B9–B10 closed or explicitly deferred by the course owner.
- Verified facts register complete for every number used in a scored question.
