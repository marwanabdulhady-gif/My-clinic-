# Phase 2 — Storyboard (06 RCM Part B)

Gate: `lint_visual_plan`. ★ = scored. "Src" = slide in the 2026 deck. All benefit wording is **subject to B3**.

## A — Intro

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-000 | `title_slide` | Open | "What's new in the EBP — and why claims get rejected" · "RCM Part B" · policy effective date (B1) | — | | 1 |
| rcmb-001 | `content_slide` | Frame | The EBP added new benefits and amended others · Coverage depends on the table of benefits and the documentation · Partial coverage ≠ full approval | — | | 3, 8 |

## B — Added vs amended

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-010 ★ | `drag_drop` | Sort the benefits | Cards: prevention exams · STDs · adult vaccination · home care for inpatients · temporary contraception · telemedicine · menopause/perimenopause cover · kidney transplant · diabetes programme → *Added*; mental health · optical · congenital anomalies · dental · dialysis limit · weight-loss surgery · OPD co-payment → *Amended* | Feedback per card | 10 | 8 |

## C — Prevention, vaccines, STDs

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-020 | `tabs` | What's covered | *Early exams*: mammogram · Pap smear · FIT/colonoscopy · dietary counselling (risk criteria, B7) · FBS/HbA1c · lipids · DEXA · *Adult vaccines*: Tdap · PCV13 · PPSV23 · influenza · *STDs*: treatment whatever the mode of infection (list) | — | | 9 |
| rcmb-021 ★ | `mcq` | Apply | "A 52-year-old with BMI 32 and high cholesterol asks for help with diet to lower her heart risk." → covered behavioural/dietary consultation; document BMI and risk factors (B7) | Distractors explain what's missing | 5 | 9 |

## D — Mental health

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-030 | `accordion` | Mental-health benefit | Included conditions (9) · Excluded: hypnosis, rehabilitation · Limit per policy period (B5) · Pre-authorisation for sub-limit services · Document: indication, link symptoms to a valid psychiatric diagnosis, justify referral | — | | 10; script |
| rcmb-031 ★ | `true_false` | Exclusion | "Hypnosis for alcohol use is covered under the mental-health benefit." → **False** | | 5 | 10 |

## E — Other added benefits

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-040 | `tabs` | Five benefits | Home care for inpatients (wound care, IV meds, catheter care) · Telemedicine (MOH-licensed centre, CHI rules) · Diabetes 360° programme (team + specialist visits) · Women's health (menopausal/perimenopausal hormone therapy) + family planning (hormonal contraceptives, IUD) · Kidney transplant (limit, B5) | — | | 11–12 |
| rcmb-041 ★ | `matching` | Key condition or limit | Mental health ↔ sub-limit per policy period + pre-auth · Kidney transplant ↔ up to the policy limit · Telemedicine ↔ MOH-licensed centre · Home care ↔ after an inpatient stay (wound/IV/catheter) · Family planning ↔ hormonal contraceptives and IUDs · Women's health ↔ menopausal hormone therapy | | 10 | 10–12 |

## F — The rejection log

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-050 | `content_slide` (blocks) | Read a log | Rebuilt HTML table, 8 rows, invented claim ids (B8): diagnosis · service · rejection comment. Comments drawn from slide 6: "pain, unspecified" · "fever" · "requires pre-authorisation as per policy" · "consultation within the free follow-up period" · "radiology: two views" · "no proof of billed service" · "duplicate billing" · "renal panel must include required tests" | — | | 6 |
| rcmb-051 ★ | `drag_drop` | Classify | The 8 comments → Documentation · Coding · Policy / pre-auth · Timing / follow-up period · Billing process (categories per B9) | Feedback explains the cause and the fix | 15 | 6 |
| rcmb-052 ★ | `decision_scenario` | Rework | Claim rejected: "Fever — non-specific diagnosis". Node 1: resubmit unchanged / bill again / review the note ✔. Node 2: the note shows fever 3 days, dysuria, positive urinalysis → add specific/provisional diagnosis and findings ✔ vs add a second random code. Node 3: resubmit with the supporting document ✔ vs new claim (duplicate) | Feedback ties back to Part A | 15 | 6; 05 |

## G — Practice

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-060 ★ | `adaptive_practice` (`strategy: elo`) | **Covered or not?** | Bank of 15 patient requests across all benefits (e.g. adult influenza vaccine; PCOS hormonal panel; telemedicine follow-up from an unlicensed app; IUD insertion; home IV antibiotics after discharge; bipolar disorder management; hypnosis; DEXA for a postmenopausal woman). `max_items` 8, `target_success` 0.7, `pass_ratio` 0.6 | Per-item feedback with the rule | 20 | 8–12 |

## Close

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| rcmb-090 | `results_breakdown` | Results | `rcmb-o1`…`o3` | — | | — |
| rcmb-091 | `summary` | Close | Know what's new · Document to the benefit's criteria · Check limits and pre-auth · Rework, don't resubmit · Link: EBP one-page summary (PDF) | `show_score` | | 14 |

## Flow check

`rcmb-040` (tabs) → `rcmb-041` (matching) → `rcmb-050` (content) → `rcmb-051`: no passive run over 2.
