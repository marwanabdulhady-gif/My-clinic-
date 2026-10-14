# Phase 3 — Narration & assets (04 Operations & My Care)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## Companions in this module (Noor and Dr. Omar)

Character bible: [`../00_program/characters/companions.md`](../00_program/characters/companions.md). **Lead host: Omar** (narrates every narrated screen unless listed below). **Co-host: Noor**.

| Screen | Visible | Pose / asset | Placement (brand layout) | Speaks | What they do |
|---|---|---|---|---|---|
| ops-000 | Omar | `char-omar-welcome` | L1 half-body bottom-right | Omar | Welcome |
| ops-001 | Omar | `char-omar-explaining` | L3 right column | Omar | Three-desks story (companions.md §1) |
| ops-022 | Noor | `char-noor-avatar-neutral + tip card` | L3 tip card | Noor | Tip: when in doubt about an abbreviation, ask — everyone did once |
| ops-031 | Omar | `char-omar-avatar-neutral → -happy / -concern` | L5 avatar | Omar | "Who do I call?" host |
| ops-090 | Omar + Noor | `char-omar-success + char-noor-avatar-happy` | L6 | Omar + Noor | Two-voice close |

- Visible on 5 screens (about one in three or fewer). Not visible on question screens except as a feedback avatar.
- Spoken lines in scripts are prefixed `OMAR:` / `NOOR:`; two-voice screens are split into one segment per line (`part` = `omar-1`, `noor-1`, …) and joined into one audio file per screen (companions.md §5).
- Character images are the shared program assets `char-noor-*` / `char-omar-*` (companions.md §3); no module-specific character art.

## 1. Narration outline

| Screen | Speaker | Sec | Narration intent |
|---|---|---|---|
| ops-000 | Omar | 12 | In fifteen minutes you'll know where to send a patient's request. |
| ops-001 | Omar | 25 | Why routing matters; a patient who repeats their story loses trust. Omar's story: "I once sent the same patient to three desks in one morning. She never forgot it — and neither did I." |
| ops-002 | Omar | 20 | Walk the journey; notice where each team leads. |
| ops-010 | Omar | 40 | Operations runs the day: environment, KPIs, recovery on the spot. |
| ops-011 | Omar | 30 | Read the chart by roles; names are in the directory because they change. |
| ops-020 | Omar | 40 | My Care is the relationship after the visit: follow-ups, programmes, referrals. |
| ops-021 | Omar | 25 | My Care structure: managers, site leaders, coordinators, quality. |
| ops-022 | Noor | 15 | The abbreviations you'll hear on day one. |
| ops-030 / 032 / 033 | Omar | 8 each | Set up. |
| ops-031 | Omar | 15 | Set up four requests. |
| ops-090 | Omar + Noor | 20 | Right team, first time; use the directory for names. |

Estimated audio: ~5 minutes.

## 2. Lexicon used

PXO, FM (after B3), DMP, CHP, HHC, VIP, PR1 ("P-R-one"), J1–J4, KPI ("K-P-I"), TAT ("turnaround time").

## 3. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| ops-img-journey | SVG | ops-002 | 6-stage horizontal journey, icons, team colour tags + text labels | own | "Patient journey from booking to follow-up." |
| ops-img-ops-chart | SVG | ops-011 | Role-only Operations chart (from B1) | own | "Operations structure by role." |
| ops-img-mycare-chart | SVG | ops-021 | Role-only My Care chart (from B2) | own | "My Care structure by role." |
| ops-img-activities | SVG icons ×14 | ops-010, ops-020 | Line icons; slide 2/5 "sticky note" style **not** copied | own | decorative |
| ops-img-scenes-1..4 | illustrations | ops-031 | Reception, phone follow-up, insurance call, pharmacy queue | ai-generated | per scene |
| char-noor-* / char-omar-* | character set (program-wide) | see "Companions in this module" | Shared companion art: poses and avatars listed in companions.md §3 | ai-generated (masters approved first) | per pose, e.g. "Dr. Omar, the family physician, giving a tip." |
| ops-aud-* | audio | narrated screens | TTS | ai-generated | transcript |

No slide images are reused (they contain names).

## 4. Activity plans

| Activity | Objective | Rules | Success | Accessibility |
|---|---|---|---|---|
| ops-030 sort | ops-o1 | 10 cards, 2 targets | all correct for full points | keyboard pick-and-place |
| ops-031 routing | ops-o2 | 4 nodes, +1 per correct route | ≥ 3 | buttons |

## 5. Approval request

Director of Operations and My Care Manager approve both redrawn charts, all 10 sort cards and the four routing answers.
