# Phase 2 — Storyboard (04 Operations & My Care)

Gate: `lint_visual_plan`. ★ = scored. "Src" = slide in `Operations & My Care Structure.pptx`.

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ops-000 | `title_slide` | Open | "Who Does What" · "Operations & My Care" | — | | 1, 4 |
| ops-001 | `content_slide` | Why it matters | "Right team, first time." · A patient shouldn't have to tell their story twice. | — | | — |
| ops-002 | `hotspot` (`explore`, `require_all`) | Patient journey | Horizontal journey: Book → Arrive & register → Consult → Lab / Radiology / Pharmacy → Leave → Follow-up. Each stage shows which team leads (Operations, My Care or both) | Open all 6 stages | | 2, 5 |
| ops-010 | `accordion` | Operations activities | 7 items from slide 2, each with one example ("Recovery: a patient waited 40 minutes; the PX officer apologises and fixes the next visit") | — | | 2 |
| ops-011 | `labeled_diagram` (`display`) | Operations structure | Redrawn **role-only** chart (B1): Director of Operations → PX & Operations Sr. Manager · Patient Access & PX Sr. Manager · Operations Sr. Manager → PX Managers → PXOs/FMs at sites J1–J4, PR1, VIP team, Check-Up Unit, In-Patient | Labels with one-line role description | | 3 |
| ops-020 | `accordion` | My Care activities | 7 items from slide 5, with DMP/CHP expanded (B3) | — | | 5 |
| ops-021 | `labeled_diagram` (`display`) | My Care structure | Redrawn role-only chart (B2): Director of Operations → Patient Access & PX Sr. Manager → My Care Manager → Onboarding leaders, site leaders (J1; J2–J4) → Coordinators; QA leader | — | | 6 |
| ops-022 | `flashcards` | Abbreviations | PXO · FM · Coord · DMP · CHP · HHC · PR1 · VIP team (B3) | Flip | | 3, 5 |
| ops-030 ★ | `drag_drop` | Sort the work | 10 cards → *Operations* / *My Care*: lab TAT KPI · clinic look and feel · on-spot complaint at reception · end-to-end journey · support a doctor's inquiry · monthly follow-up call · insurance medication follow-up · hypertension programme booking · telemedicine coordination · internal referral priority | Feedback on each card; overlap items explained | 15 | 2, 5 |
| ops-031 ★ | `decision_scenario` | **Who do I call?** | 4 nodes (routing per B7): (1) A patient at reception is upset that her lab result isn't ready → Operations / PX officer on site; (2) A diabetic patient asks who will remind him about his 3-month review → My Care; (3) A patient's insurer rejected his monthly medication → My Care insurance follow-up; (4) A doctor reports the pharmacy queue is causing delays every afternoon → Operations | Each choice explains the owner and the role | 20 | 2, 5 |
| ops-032 ★ | `mcq` | Escalation | "The PX officer can't resolve a complaint on the spot. Who is the next step?" → site Patient Experience Manager (per B1) | | 5 | 3 |
| ops-033 ★ | `matching` | Roles | PXO ↔ "patient experience on site" · My Care Coordinator ↔ "follow-ups and bookings" · My Care Onboarding Leader ↔ "enrols patients in My Care" · Operations Sr. Manager ↔ "daily operations" · QA Leader ↔ "quality of My Care calls/service" | | 10 | 3, 6 |
| ops-090 | `summary` | Close | Right team, first time · Link: live staff directory (intranet) · Next: module 05/06 (clinicians) or 08 (EHR) | `show_score` | | — |

## Flow check

- Passive run `ops-010`→`ops-022` = 5 screens (accordion, diagram, accordion, diagram, flashcards). If `passive_stretch` fires, move `ops-030` (sort) between `ops-011` and `ops-020`: learners sort Operations items first, then My Care items in a second `drag_drop`. Decide after lint.
