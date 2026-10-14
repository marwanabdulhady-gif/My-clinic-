# Phase 2 — Storyboard (01 Facility Management & Safety)

Gate: `lint_visual_plan(plan, brand)`. On-screen text stays under 25 words where possible (hard limit 45). "Pts" = points for scored screens. "Src" = page in `Health & Safety 1.pdf`.

Screen types used: only the 31 supported edumints types. Rows marked ★ are scored.

## Section 0 — Welcome

| Id | Type | Purpose | On screen (keywords) | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-000 | `title_slide` | Open the course | "Facility Management & Safety" · "Your first-week safety essentials" | — | | p.1 |
| hs1-001 | `content_slide` (text_media) | Why it matters; how the course works | 3 icons: *Protect patients · Protect you · Pass the CBAHI survey*; "9 short sections · resume any time" | — | | pp.1, 3 |
| hs1-002 | `poll` | Unscored confidence check (baseline) | "How confident are you to act in a fire right now?" 1–4 | Reflection text: "We'll come back to this at the end." | | — |

## Section 1 — CBAHI FMS chapter overview

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-101 | `content_slide` | Why the chapter exists | *Survey requirement · Everyone's responsibility · One connected system* | — | | p.3 |
| hs1-102 | `hotspot` (`mode: explore`, `require_all: true`) | Explore the eight plans | Icon grid of 8 plans (own SVG). Each region opens: purpose + 4 main functions | All 8 regions must be opened | | pp.4–8 |
| hs1-103 | `content_slide` | Plans ↔ codes link | "A fire is a Code Red. A chemical spill is a Code Orange." | — | | p.3 |
| hs1-104 ★ | `matching` | Check plans | 8 pairs: plan ↔ purpose (one sentence each) | Per-pair feedback; correct set shown after submit | 10 | pp.5–8 |

## Section 2 — Occupational Health & Safety

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-201 | `flashcards` | Four core terms | Health · Safety · Hazard · Risk (front term, back definition + example) | Flip | | p.10 |
| hs1-202 | `accordion` | Incident types | Near miss · First aid · Medical treatment · Lost time · Fatality. Near miss tagged "most valuable to report" | Open each | | p.11 |
| hs1-203 | `labeled_diagram` (`mode: display`) | AREC cycle | Circular SVG: Anticipate → Recognise → Evaluate → Control | 4 labels with short text | | p.12 |
| hs1-204 ★ | `sorting` | Hierarchy of controls | Order most → least effective: Elimination, Substitution, Engineering, Administrative, PPE | Feedback: "PPE is the last line of defence, not the first." | 10 | p.13 |
| hs1-205 ★ | `decision_scenario` | Apply AREC + controls + rights | Corridor with a trailing cable across a walkway near a patient waiting area (illustration). 3 nodes: (1) what do you do first; (2) which control is strongest (re-route cable / cover / sign / warn); (3) supervisor says "leave it, we're busy" → use your right to stop unsafe work, contact your Safety Liaison | Each choice has a *why* feedback; `pass_score` 2 of 3 best choices | 15 | pp.12–15 |
| hs1-206 | `accordion` | Who to contact + your rights | Department Safety Liaison (ask your supervisor on day 1) · Right to stop unsafe work · Right to be consulted · Right to training | — | | pp.14–15 |

## Section 3 — Disaster management

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-301 | `flashcards` | Learn the codes | 11 cards: front = code name + colour chip (bilingual EN/AR), back = meaning + extension (**pending D2**) | Flip | | pp.17–18 |
| hs1-302 ★ | `matching` | Check codes | 8 pairs (randomised): Red–Fire, Orange–Hazmat spill, White–Violent situation, Black–Bomb threat, Pink–Child/infant abduction, Blue–Cardiac arrest, Yellow–External disaster, Brown–Utility failure | Feedback per pair | 10 | pp.17–18 |
| hs1-303 | `content_slide` | Two announcements | *Hospital Evacuation* (go to assembly point) · *End of Disaster* (stand down only on this signal) | — | | p.19 |
| hs1-304 ★ | `sorting` | Common response pattern | Recognise → Activate → Respond → Stand down | Feedback reinforces "wait for the official all-clear" | 5 | p.20 |
| hs1-305 | `labeled_diagram` (`display`) | Who responds | ERT diagram: Safety · Security · Nursing · Facility · Operation around an Incident Commander | — | | p.21 |

## Section 4 — Fire safety

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-401 | `labeled_diagram` (`display`) | Fire triangle + smoke | Triangle: Heat · Fuel · Oxygen. Callout: "Smoke, not flame, is the leading cause of death." | — | | p.23 |
| hs1-402 ★ | `sorting` | RACE | Rescue → Alarm → Contain → Extinguish/Evacuate | Feedback explains why rescue and contain come before extinguishing | 5 | p.24 |
| hs1-403 ★ | `sorting` | PASS | Pull → Aim (low, at the base) → Squeeze → Sweep | | 5 | p.24 |
| hs1-404 | `hotspot` (`explore`, `require_all`) | Find the equipment | Clinic corridor illustration with 8 regions: smoke detector, heat detector, call point, extinguisher, fire blanket, sprinkler, evacuation chair, assembly-point sign | Each region: what it is + when you use it | | pp.25–26 |
| hs1-405 ★ | `drag_drop` | Extinguisher classes | Items: "Burning paper bin", "Petrol leak", "Smoking photocopier", "Magnesium shavings", "Pantry pan fire" → targets Class A / B / C / D / K | Keyboard-operable; feedback: "Check the label before you pull the pin." | 10 | pp.27–28 |
| hs1-406 | `tabs` | Evacuation types | Horizontal (first response, same floor) · Vertical (stairwells, never elevators) · Full (whole building, assembly point) | — | | p.29 |
| hs1-407 ★ | `mcq` | Choose the evacuation | "Smoke in Room 3; fire doors at the end of the corridor; patients on the same floor are not in danger yet. First move?" → Horizontal to the next compartment | Wrong options explain why (elevator, full evacuation too early) | 5 | p.29 |
| hs1-408 ★ | `true_false` | Oxygen myth | "Oxygen is flammable." → **False**: oxidiser, intensifies fire | | 5 | p.31 |
| hs1-409 ★ | `decision_scenario` | Put RACE into action | Night shift: smoke from a waste bin in a patient room. Nodes: (1) first action (rescue patient); (2) the call — what to say (code, location, ID & name); (3) contain (remove O₂ cylinder and alcohol rub, close door); (4) fire grows past the bin → evacuate horizontally | Each node has consequences; `pass_score` 3 of 4 | 20 | pp.23–31 |
| hs1-410 | `content_slide` | Fire prevention | 7 icons: candles · unauthorised welding · extensions · heaters/boilers · smoking & vaping · unauthorised microwaves · uncontrolled flammables | — | | p.30 |

## Section 5 — Hazardous materials & waste

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-501 | `content_slide` | Ordering & inventory | Approved procurement only · On the inventory with SDS · **Never accept an unlabelled container** | — | | p.33 |
| hs1-502 ★ | `matching` | GHS pictograms | 9 pairs: pictogram (own SVG via `left_html` image or name) ↔ hazard | Feedback per pair | 10 | p.34 |
| hs1-503 ★ | `labeled_diagram` (`quiz`) | NFPA diamond parts | Place 4 labels: Health (blue) · Flammability (red) · Reactivity (yellow) · Special (white) | Colour + position + text label (not colour alone) | 10 | pp.35–36 |
| hs1-504 ★ | `mcq` | Read a diamond | Diamond shows Health 3 · Flammability 0 · Reactivity 1 · Special W. "What does this tell you before opening?" → serious health hazard; do not use water | | 5 | p.36 |
| hs1-505 | `accordion` | Store, handle, transport | Storage per SDS · Designated carts & routes · PPE per SDS · Flammable cabinet (double-walled, self-latching) · SDS at point of use | — | | pp.37–38 |
| hs1-506 | `content_slide` (text_media) | Eyewash and showers | "Find your nearest one **today**." "Flush ≥ 15 minutes." Photo of a unit (own) | — | | p.39 |
| hs1-507 ★ | `decision_scenario` | Code Orange decision | 3 short cases: (a) small spill of hand rub; (b) a spill over the threshold of surface disinfectant; (c) a few mL of a highly toxic reagent → Code Orange? + 4 response steps (isolate & warn → PPE per SDS → contain with right kit → report) | Rule shown in feedback (**text depends on D1**) | 15 | p.40 |
| hs1-508 ★ | `drag_drop` | Waste segregation | Items: used needle, blood-soaked dressing, paper towel (clean), scalpel blade, gloves with body fluid, food wrapper → General / Infectious / Sharps | Feedback: "Never recap." Bin colours **per B7** shown as text + colour | 10 | p.41 |

## Section 6 — Security

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-601 | `tabs` | Security rules | *People*: ID always · contractor permits · visitor badges · *Premises*: CCTV · lost & found → Security · designated parking · no smoking anywhere | — | | pp.43–44 |
| hs1-602 ★ | `mcq` | Apply | "A man without a badge is in the staff-only medication room and says he is a contractor." Best action → politely ask for permit/badge; if none, call Security; do not leave him alone | Wrong options explain risks | 5 | p.43 |

## Section 7 — Utility

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-701 | `hotspot` (`explore`, `require_all`) | Utility walk-around | Treatment-room illustration: red emergency socket (**per B6**), standard socket, UPS-backed monitor, unauthorised extension (crossed), water shut-off valve, HVAC vent in isolation room | Region text: what it is, what you do | | pp.46–47 |
| hs1-702 ★ | `mcq` (multi-correct if supported, else single) | Apply | "The isolation room is cold. A visitor asks you to close the vent." → Never disable isolation-room vents; report to Maintenance | | 5 | p.47 |

## Section 8 — Biomedical

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-801 | `content_slide` | Labels, PPM, tagging | Inspection label (date + status) · PPM schedule · "Out of Service" tag | — | | p.49 |
| hs1-802 ★ | `decision_scenario` | Spot it, report it | An infusion pump's label is 2 months overdue; the ward is busy. Nodes: use or not → tag out of service → who to notify (Biomedical Engineering) → colleague suggests moving a pump from another room (never relocate without BME) | | 15 | pp.49–52 |
| hs1-803 ★ | `true_false` | Oxygen cylinders | "Store cylinders upright and secured, with full and empty clearly separated." → True | | 5 | p.51 |

## Section 9 — Radiation & laser safety

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-901 | `tabs` | Ionising vs non-ionising | *Ionising*: X-ray, CT → dosimeters, shielding · *Non-ionising*: MRI, ultrasound, laser · *MRI*: magnet always on, screening every time · *X-ray rooms*: lead apron, stand behind the shield | — | | pp.54–55 |
| hs1-902 ★ | `matching` | Protection principles | Justification · Optimisation · Limitation ↔ definitions | | 5 | p.56 |
| hs1-903 | `labeled_diagram` (`display`) | ALARA | Time · Distance · Shielding around a source icon | — | | p.57 |
| hs1-904 | `accordion` | Staying accountable | OSL dosimeter · Lead apron · RSO is your contact | — | | p.58 |
| hs1-905 ★ | `mcq` | Dose bands | "A quarterly OSL reading shows 2.0 mSv. What happens?" → Notification level: you are informed and monitored (**values pending B4**) | Feedback shows the 3 bands table | 5 | p.59 |
| hs1-906 ★ | `matching` | Laser classes | 1/1M · 2/2M · 3R · 3B · 4 ↔ hazard (**wording per B5**) | | 5 | p.61 |
| hs1-907 | `content_slide` | Laser hazards & measures | Eyes (often no pain) · Skin burns · High voltage → Eye protection · Beam management · Control reflections · Training | — | | pp.62–64 |

## Capstone and close

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hs1-950 ★ | `game` (`template: case_sim`) | "One shift, three plans" | Mixed case: (1) during a busy clinic a cleaner knocks over a large bottle of disinfectant next to an oxygen cylinder → Code Orange or not (D1), move O₂ away; (2) an alarm sounds → which code is announced for smoke; RACE choice; (3) afterwards you notice the suction unit's label is expired → tag and report. Mechanics: score + 3 lives + 1 hint per node; no timer | Debrief node lists which plan each decision belonged to | 25 | pp.3, 24, 40, 49 |
| hs1-980 | `results_breakdown` | Show strengths by section | Sections = objectives `hs1-o1`…`hs1-o10`; `weak_threshold` 70 | "Revisit" links to weak sections | | — |
| hs1-981 | `poll` | Confidence re-check | Same question as `hs1-002` | Reflection: compare with start | | — |
| hs1-990 | `summary` | Completion actions | ✔ Locate your evacuation route and assembly point · ✔ Save emergency numbers · ✔ Find your nearest eyewash · ✔ Ask your supervisor who your Safety Liaison is · ✔ Sign the acknowledgement (D14) · Contact: Safety & Security Manager | `show_score: true` | | p.65 |

## Flow check against lint rules

- No three screens of the same type in a row (checked: sorting `hs1-402`/`403` are followed by hotspot).
- No more than four passive screens in a row (longest passive run: `hs1-301`→`303` = 2 before a scored screen; section 9 `hs1-903`/`904` = 2).
- Every section has at least one scored screen.
- Accent background used only on the capstone title node.
