# Phase 2 — Storyboard (05 RCM Part A)

Gate: `lint_visual_plan`. ★ = scored. "Src" = section of the speaker script.

## Companions on screen (Noor and Dr. Omar)

Lead host **Dr. Omar**, co-host **Noor** — see [`../00_program/characters/companions.md`](../00_program/characters/companions.md). The companion is part of the visual design on these screens (full detail, poses and spoken lines in `phase-3-narration-and-assets.md`, "Companions in this module"):

| Screen | Companion | Placement |
|---|---|---|
| rcma-000 | Omar (`char-omar-welcome`) | L1 half-body bottom-right |
| rcma-001 | Omar (`char-omar-explaining`) | L3 right column |
| rcma-011 | Noor (`char-noor-avatar-neutral + tip card`) | L3 tip card |
| rcma-031 | Omar (`char-omar-avatar-thinking → -happy / -concern`) | L5 avatar |
| rcma-050 | Omar + Noor (`char-omar-avatar (host); char-noor-tip (hints)`) | L5 |
| rcma-091 | Omar (`char-omar-success`) | L6 right |

All other screens: no companion visible; the lead host's voice narrates.

## A — Why it matters

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-000 | `title_slide` | Open | "Documentation & coding that gets approved" · "RCM Part A" | — | | Slide 1 |
| rcma-001 | `content_slide` (text_media) | The core idea | "The payer doesn't see your patient. The payer sees your note." · Clinical decision + documentation + coding = optimised payment | — | | Physician responsibility |
| rcma-002 | `poll` | Productive failure | "What do you think is the #1 cause of rejections at My Clinic?" (4 causes) | Reflection: "Hold that thought — we'll check it later." | | Common errors |

## B — Documentation strategy

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-010 | `tabs` | Always / Avoid | *Always*: chief complaint & HPI · relevant findings · link symptoms to the working diagnosis · labs/imaging when needed · *Avoid*: vague notes · diagnosis without support · copy-paste · "fatigue only", "body pain" | — | | Documentation strategy |
| rcma-011 | `image_compare` | Weak vs strong | Before: "Patient given IV fluids." · After: "Dehydration signs (HR 112, dry mucosa) — IV fluids started for stabilisation." Rendered as two note cards (SVG) | Slider; caption: same treatment, different outcome | | Medical necessity |
| rcma-012 ★ | `sorting` | The full clinical picture | Order: Chief complaint → HPI → relevant past history → clinical findings → assessment → plan with duration & follow-up | Feedback: "Good documentation tells a story, not just a diagnosis." | 10 | Full history |
| rcma-013 ★ | `mcq` | Medical necessity | "Which note best justifies a CBC?" options: "Routine CBC" / "Fatigue" / "Fatigue for 6 weeks, pallor, menorrhagia — rule out anaemia" ✔ / "Patient requested blood test" | Feedback explains what the reviewer asks: *why was this done?* | 5 | Medical necessity |

## C — ICD-10 coding

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-020 | `content_slide` | Coding is clinical translation | Primary = main condition treated · Secondary = complexity · Specific code = higher acceptance · #1 rejection cause: non-specific symptom coding | — | | ICD-10 core |
| rcma-021 ★ | `matching` | Symptom → supported diagnosis | Presentations ↔ codes (**final codes per B4**): "Vomiting + diarrhoea, 2 days, dehydration" ↔ gastroenteritis code · "Sore throat, fever, tonsillar exudate" ↔ J03 Acute tonsillitis · "Headache, BP 168/102 on two readings" ↔ I10 Hypertension · "Polyuria, HbA1c 8.1%" ↔ E11 Type 2 diabetes | Feedback: "Don't stop at the symptom." | 10 | ICD-10 core |
| rcma-022 | `worked_example` (`fading: partial`) | Provisional diagnosis | Fever 3 days + dysuria + suprapubic pain → urinalysis and culture ordered → document a **provisional** diagnosis linked to the findings → confirm or change when results return. Self-explanation: "Why is a provisional diagnosis better than 'fever' here?" | Unscored | | Golden tip; Professional diagnosis |
| rcma-023 ★ | `drag_drop` | Covered or not as primary? | Items: E66 Obesity (BMI 31) · L70 Acne · L66 Hair loss · L21 Seborrhoeic dermatitis · N97 Female infertility · General check-up · J03 Acute tonsillitis · E11 Type 2 diabetes · Obesity with BMI 42 referred for bariatric surgery (**B5**) → *Avoid as primary (uncovered)* / *Covered when clinically supported* | Feedback: "Link to a covered condition when it truly exists, or don't use it as the main diagnosis." | 10 | Uncovered codes |

## D — Defensive medicine & ordering

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-030 | `content_slide` | More tests ≠ better care | Follow initial work-up protocols · No supplements without indication · Repeat only at evidence-based intervals · If you deviate, **document why** | — | | Defensive medicine; Excessive ordering |
| rcma-031 ★ | `decision_scenario` | Joint-pain case | Node 1: 45-year-old with multi-joint pain, first visit, no history → order everything (CRP, ESR, anti-DNA, anti-Ro, anti-La) vs initial work-up (CRP, ESR) ✔. Node 2: same patient, rheumatoid arthritis already diagnosed by a rheumatologist elsewhere → document the history and the specialist diagnosis; the full panel is justified in one request ✔ | Feedback quotes the script's example (**B10**) | 15 | Defensive medicine |
| rcma-032 ★ | `mcq` | Timing | "Your diabetic patient's HbA1c was done 6 weeks ago. He asks for another." Best action → don't repeat yet unless there's a documented clinical reason; next test at the approved interval (**B3**) | | 5 | Excessive ordering |
| rcma-033 ★ | `true_false` | Supplements | "Prescribing a combined multivitamin 'for general wellness' with no documented deficiency is likely to be rejected." → **True** (**B8**) | | 5 | Defensive medicine |

## E — Rejections & coverage

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-040 ★ | `drag_drop` | Four causes | Rejection notes → causes: "No indication for the MRI" → missing justification · "Diagnosis: fever" → non-specific · "No examination findings recorded" → incomplete · "Antibiotic billed for a viral URTI code" → mismatch (+ 4 more) | Feedback reveals the poll answer from `rcma-002` | 10 | Common errors |
| rcma-041 | `content_slide` | Coverage changes | Benefits are added and amended often · Know what's covered, adapt documentation · "If you don't document it properly, it won't be covered — even if it's clinically correct." · Next: Part B covers the new EBP | — | | Updates; Physician responsibility |
| rcma-042 ★ | `mcq` | Coverage check | "Which hormonal assessment is likely to be approved?" → menopausal symptoms ✔ vs PCOS work-up (**B6**) | Feedback: the same service can be accepted or rejected depending on indication and documentation | 5 | Amended benefits |

## F — Capstone

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-050 ★ | `game` (`template: case_sim`) | **Fix the note** | 3 invented notes, one node each: (1) "Body pain. Vit D + B12 + multivitamin." → choose the best rewrite (findings, deficiency evidence, single indicated supplement, follow-up); (2) "Cough. Augmentin." → choose specific diagnosis + findings justifying antibiotic; (3) "Check-up. Full labs." → link to a covered condition or bill as appropriate. Score + 1 hint per node, no lives, no timer | Debrief: the 6-point checklist from the script's summary | 25 | To summarise |

## Close

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcma-090 | `results_breakdown` | Results | `rcma-o1`…`o5`, weak below 70% | — | | — |
| rcma-091 | `summary` | Checklist to keep | ✔ Be specific; avoid uncovered codes and combined supplements · ✔ Full data + plan with duration and outcome · ✔ Justify every service with a specific code; provisional diagnosis if needed · ✔ Think like a clinician *and* a reviewer · ✔ If you skip a protocol, document why · ✔ Clear, strong, defensible. Next: Part B | `show_score` | | To summarise |

## Flow check

- No passive run longer than 2. No three same-type screens in a row.
- Every part has a scored screen.
