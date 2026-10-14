# Phase 2 — Storyboard (08 EHR Consultation)

Gate: `lint_visual_plan`. ★ = scored. "Src" = time in `IT.mp4` (for the **workflow reference only**; every screenshot is re-captured on a test patient, Phase 0 B2).

Simulation steps use `regions` (click) or `input_accepted` (type). Each step has `instruction_html`, `image_alt` and `hint_html`.

## Companions on screen (Noor and Dr. Omar)

Lead host **Dr. Omar**, co-host **Noor** — see [`../00_program/characters/companions.md`](../00_program/characters/companions.md). The companion is part of the visual design on these screens (full detail, poses and spoken lines in `phase-3-narration-and-assets.md`, "Companions in this module"):

| Screen | Companion | Placement |
|---|---|---|
| ehr-000 | Omar (`char-omar-welcome`) | L1 half-body bottom-right |
| ehr-001 | Omar (`char-omar-explaining`) | L3 right column |
| ehr-020 | Omar (`char-omar-avatar-neutral + tip card`) | L5 avatar above the simulation |
| ehr-042 | Noor (`char-noor-avatar-neutral + tip card`) | L3 tip card |
| ehr-050 | Omar (`char-omar-avatar-neutral`) | L5 avatar |
| ehr-091 | Omar (`char-omar-success`) | L6 right |

All other screens: no companion visible; the lead host's voice narrates.

## A — Intro & workflow map

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-000 | `title_slide` | Open | "EHR consultation workflow" · "Guided practice on a test patient" | — | | — |
| ehr-001 | `content_slide` | Why + disclaimer | Complete, linked, on the day · Disclaimer (B7) · "Everything here is a test patient." | — | | — |
| ehr-002 | `timeline` | Workflow map | 9 steps as events: 1 Open · 2 Document · 3 Diagnose · 4 Order · 5 Review orders · 6 Summary · 7 Educate · 8 Refer & follow up · 9 Complete | Click through | | process map |

## B — Open & document

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-010 ★ | `simulation` | Open the consultation | Step 1: today's consultation list → click the test patient. Step 2: open the consultation form | Hints name the panel | 5 | 00:00–00:30 |
| ehr-011 | `hotspot` (`explore`, `require_all`) | Mandatory fields | Consultation form screenshot; regions = each mandatory section (B4): chief complaint · duration · HPI · past history (allergies, medications) · examination · plan of care | Each region: what to write, "save as you go" | | 00:30 |
| ehr-012 ★ | `mcq` | Why it won't complete | "You press Complete and the system refuses. The form shows chief complaint, HPI and examination filled in." Most likely cause → plan of care (or another mandatory field per B4) is empty | | 5 | 07:30 banner |

## C — Diagnosis

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-020 ★ | `simulation` | Add the primary diagnosis | Step 1: click *Add Diagnosis*. Step 2: **type** `E11` (accepted: `E11`, `e11`, `type 2 diabetes`). Step 3: choose *Type 2 diabetes mellitus* from results. Step 4: mark as **primary** / problem; onset, chronicity. Step 5: click the star to add to favourites | Feedback: "Specific primary diagnosis = fewer rejections (module 05)." | 10 | 01:00–02:00 |

## D — Orders

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-030 | `content_slide` (text_media) | How to find an order | Search by service · lab · referral · package · order profile · Form Wizard reviews a package before you finalise | — | | 02:30–03:00 |
| ehr-031 ★ | `simulation` | Medication order | Step 1: open order search. Step 2: **type** the drug name (B6 example). Step 3: set route, dose, frequency, duration. Step 4: choose the **assessed diagnosis** (E11). Step 5: add instructions to the patient. Step 6: press *Order* | Feedback: "The order isn't placed until you press Order." | 15 | 03:30–04:30 |
| ehr-032 ★ | `simulation` | Lab package via Form Wizard | Step 1: search the package (B6). Step 2: Form Wizard step 1 — review items. Step 3: remove an item not needed. Step 4: finalise | | 10 | 03:00 |
| ehr-033 ★ | `mcq` | Non-formulary | "You order <non-formulary item, B6>. The system flags it. What does that mean?" → it needs approval before it can be dispensed; consider a formulary alternative | | 5 | 1:40–4:50 |
| ehr-034 ★ | `mcq` | Why link to a diagnosis | "Why must each order be linked to the assessed diagnosis?" → it shows medical necessity to the reviewer and keeps the record consistent; unlinked orders are a common rejection cause | Link to module 05 | 5 | 03:30 |

## E — Summary & education

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-040 ★ | `simulation` | Consultation summary | Step 1: open *Consultation Summary*. Step 2: check lab orders, special tests, referrals. Step 3: *Download and Print* | | 5 | 06:20–07:00 |
| ehr-041 ★ | `simulation` | SMS education | Step 1: open *Send SMS – educational material*. Step 2: choose department. Step 3: **type** `E11`. Step 4: select the leaflet. Step 5: *Send* (B8) | | 10 | 07:00 |
| ehr-042 | `content_slide` | Patient & family education | Checklist: infection control · medication use · disease/condition · treatment · health & lifestyle · other · "Required before finalising" | — | | 07:30 |

## F — Referral & finish

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-050 ★ | `simulation` | Internal referral + follow-up | Step 1: open referral. Step 2: specialty = Endocrinology. Step 3: **type** the reason (approved example phrase, e.g. "poorly controlled type 2 diabetes"; variants listed in `input_accepted`). Step 4: type = Internal; timing = within a month (B9). Step 5: follow-up toggle + interval. Step 6: Save | | 10 | 07:40–08:20 |
| ehr-051 ★ | `sorting` | The whole workflow | 9 steps from `ehr-002` in order | | 10 | process map |
| ehr-052 | `content_slide` | Complete the encounter | "Record saved successfully" → Complete · What happens if a field is missing · Where to get help (IT service desk) | — | | 08:20 |

## G — Optional reference video

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-060 *(optional)* | `video` | Full walkthrough | Re-recorded on the test patient, narrated, captioned (WebVTT), ≤ 8 min; `require_complete: false` | — | | whole video |

## Close

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| ehr-090 | `results_breakdown` | Results | `ehr-o1`…`o5` | — | | — |
| ehr-091 | `summary` | Close | Complete, specific, linked · Links: EHR quick-reference card (PDF), IT service desk | `show_score` | | — |

## Flow check

- Simulations alternate with MCQs/content; no three `simulation` screens in a row (`ehr-031`, `ehr-032` then `ehr-033` mcq; `ehr-040`, `ehr-041` then content).
