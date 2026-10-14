# Phase 2 — Screen list (03 Welcome On Board)

> This is the **screen list**: one row per screen. It is the input to
> [`storyboard/storyboard.md`](storyboard/storyboard.md), which turns each row into a finished
> screen card (on-screen text, visuals and animation, interaction and scoring, full narration,
> accessibility, build JSON). **v0.1 of the storyboard is written and in SME review.**
> Do not add, remove or reorder rows without updating the storyboard in the same change.

Gate: `lint_visual_plan(plan, brand)`. ★ = scored. "Src" = slide in `HR.pptx`.

## A — Welcome

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-000 | `title_slide` | Open | "Welcome On Board" · "My Clinic & HR essentials" | — | | 2–3 |
| hr-001 | `content_slide` (full_media) | Purpose, mission, goal | *Purpose*: helping people live longer, healthier, happier lives · *Mission*: the world's most customer-centric healthcare company · *Goal*: outstanding patient experience + excellent clinical outcomes | — | | brand banner |
| hr-002 | `poll` (`allow_text`) | Icebreaker | "If you had one million Saudi riyals, where would you spend it?" options: Family · Travel · Learning · Giving back · Other (text) | Reflection: "Whatever you chose says something you care about. At My Clinic, we start from what people care about." | | 5 |

## B — Values & strategy

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-010 | `tabs` | Four values | Collaborative · Responsible · Ambitious · Caring — each tab: theme + 3–4 actions | — | | 9 |
| hr-011 ★ | `matching` | Values in action | 6 workplace actions ↔ value (e.g. "You admit a scheduling mistake to your manager and fix it" ↔ Responsible; "You ask a colleague from another department for their view" ↔ Collaborative; "You stay with an anxious patient until the nurse arrives" ↔ Caring; "You suggest a faster way to book follow-ups" ↔ Ambitious) | Feedback per pair | 10 | 9 |
| hr-012 | `accordion` | 7C strategy | Closer · Cure · Capabilities · Culture · Clinicians · Care · Cost — headline + 2 key points each | — | | 10 |
| hr-013 ★ | `mcq` | Pillar check | "My Care follow-up calls that build patient loyalty support which pillar?" → **Care** | Distractors: Closer, Culture, Cost — with why | 5 | 10 |
| hr-014 | `content_slide` | Who we serve | Patients & families (sick or healthy) · Community · Corporates & insurers | — | | 10 |

## C — Our clinic

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-020 | `timeline` | Our story | 2017 MCJ1 · 2018 new products · 2019 corporate check-up unit · 2021 MCJ2 · 2022 Dental (D1) · 2023 PRC · 2024 Riyadh (R1) · 2025 J3 · 2026 J4 (**names per D3**) | — | | 16 |
| hr-021 | `hotspot` (`explore`, `require_all`) | Branches | Simple map of Jeddah, Riyadh and Rabigh with pins: J1 North Jeddah · J2 East Jeddah · J3 · J4 · D1 · R1 · PRC | Each pin: type of clinic + year | | 14–15 |
| hr-022 | `content_slide` (blocks) | Leadership | Role cards: CEO · CMO · COO · CFO (photos and names **only with consent, B6**) | — | | 12–13 |
| hr-023 | `flashcards` | Awards | CBAHI accreditation (scores) · Best Clinical Patient Outcome 2019–20 · Best new clinic for customer service 2018 · Best New Premium Clinic 2018–19 · Most innovative corporate wellness initiative 2019 (**per B7**) | Flip | | 17–18 |

## D — Ethics & patients' rights

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-030 | `content_slide` | Code of ethics | Respect · Integrity · Accountability · Innovation & collaboration — one line each · "Ethical dilemma? Incident report within 24 hours + ethics team" | — | | 20–22 |
| hr-031 ★ | `decision_scenario` | Conflict of interest | You sit on a supplier evaluation; one bidder is your cousin's company. Node 1: say nothing / declare the conflict ✔ / step out quietly. Node 2: a colleague asks you to "help" a patient skip the queue for a gift → decline; if pressured, report. Node 3: unsure what's right → consult colleagues/committee, incident report within 24 h ✔ | Feedback explains Integrity and Accountability | 15 | 20–21 |
| hr-032 ★ | `drag_drop` | Rights vs responsibilities | Items: access to care regardless of race, gender or disability · informed consent · privacy · pain management · refuse treatment after understanding risks · ask for a patient advocate · give accurate health information · follow the treatment plan and attend appointments · respect other patients and staff → *Patient right* / *Patient responsibility* | Keyboard pick-and-place | 10 | 24–25 |
| hr-033 ★ | `mcq` | Apply | "A patient refuses a blood test after the doctor explains the risks." Best response → respect the refusal, make sure they understood, document it, inform the doctor | | 5 | 24 |

## E — Leave

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-040 | `content_slide` | Where to get help | HR help desk per business unit (role mailboxes, **B6**) · Request everything in Oracle · Full rules: *HR Quick Reference* PDF (resource) | — | | 30–31 |
| hr-041 | `accordion` | Leave types at a glance | Annual · Sick · Work injury · Maternity · Exam · Scientific · Hajj · Compassionate · Official holidays — one key rule each | — | | 32–43 |
| hr-042 ★ | `matching` | Annual entitlement | Grade ↔ working days: H–30, G–27, F & Consultant–25, A to E–22 | | 5 | 34 |
| hr-043 | `worked_example` | Sick-leave pay | Problem: 40 days of sick leave in a year with valid reports. Steps: days 1–30 full pay → days 31–40 at the reduced rate (**B1**) → reports from outside My Clinic need Staff Health Clinic approval. Self-explanation: "What changes if the report is from another hospital?" | Unscored | | 35 |
| hr-044 ★ | `decision_scenario` | **The leave desk** | You help four colleagues. (1) Lab technician wants scientific leave days for a conference → 2 days/year ✔. (2) Nurse wants exam leave for IELTS → not eligible ✔. (3) Pharmacist with 1 year's service asks for Hajj leave → not yet eligible (2 years) ✔. (4) Receptionist slipped on the way to work this morning → report to manager and HR today or tomorrow; work injury covers commuting ✔ | Each choice explains the rule; `pass_score` 3 | 15 | 36–41 |
| hr-045 ★ | `adaptive_practice` (`strategy: elo`) | Extra practice for those who need it | Bank of 12 single-answer items on leave rules (carry-over 5 days by end of March; physicians by end of June; maternity 12 weeks; start up to 4 weeks before; exam documents 2 weeks before; marriage 5 days; paternity 3 days; sibling bereavement 3 days; Eid holidays 4 days; Founding Day 22 Feb; National Day 23 Sep; scientific leave not carried over). `max_items` 6, `target_success` 0.7, `pass_ratio` 0.6 | Per-item feedback | 15 | 33–43 |

## F — Pay & social insurance

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-050 | `content_slide` | GOSI | What GOSI is · Saudi employees only · 9.75% employee + 11.75% company = 21.5% of basic + housing | — | | 44–45 |
| hr-051 | `worked_example` | GOSI example | (4,800 + 1,200) × 9.75% = **585 SAR** per month | Unscored | | 46 |
| hr-052 ★ | `fill_blank` | Practise | "Basic 6,000 + housing 1,500. Employee GOSI = ___ SAR" → accepted `731.25`, `731.25 SAR` | Feedback shows the working | 10 | 46 |
| hr-053 | `worked_example` | Overtime | Basic 6,000 ÷ (30 × 8) = 25 SAR/hour → regular OT × 1.5 = 37.50/hour → public holiday × 2 = 50/hour (**eligibility per B3**) | Unscored | | 48 |
| hr-054 ★ | `mcq` | Practise | "Basic 6,000. You work 4 overtime hours on a normal working day. Overtime pay?" → **150 SAR** (distractors 100, 200, 240) | Feedback shows the formula | 10 | 48 |

## G — Systems & licences

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-060 ★ | `matching` | Right system | Request annual leave ↔ Oracle · Employment certificate ↔ Oracle (HR service request) · Accept your contract ↔ Qiwa · Renew your professional licence ↔ Mumaris (SCFHS) · Employee guide & corporate discounts ↔ Intranet · Resign ↔ Oracle | | 10 | 47, 50–54, 59–60 |
| hr-061 ★ | `simulation` | Request leave in Oracle | 5 steps on test-account screenshots (**B8**): sign in → Time and Absences → Add Leaves → choose *Annual* + dates → Submit. Click regions on each screenshot; hints on each step | Feedback at end | 15 | 51 |
| hr-062 ★ | `true_false` | Licence rule | "If your licence will expire in less than 30 days without renewal, HR may suspend you from work." → **True** (**per B13**). Feedback: renew early; My Clinic pays the fee claim, not late penalties | | 5 | 49 |

## H — ID, benefits & dress code

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-070 | `content_slide` (blocks) | ID and benefits | ID card: lost → email HR, 100 SAR (**B4**); damaged → free replacement · Benefits wheel: health insurance · performance bonus · development · hybrid work · internal advancement · discounts | — | | 55, 57 |
| hr-071 ★ | `drag_drop` | Dress code | Items: uniform · scrubs and coat · business attire · minimal jewellery · professional shoes · no casual days → Front office / Medical team / Back office | Keyboard pick-and-place | 10 | 58 |

## I — Leaving & contracts

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-080 | `content_slide` | Contracts and resignation | Accept contract on Qiwa · Resign in Oracle · Notice: 2 months both ways · EOS + experience certificate within 15 days of last day | — | | 59–60 |
| hr-081 ★ | `mcq` | Apply | "You accept a new job starting in 3 weeks. What happens with your notice?" → you must serve the contractual 2 months unless agreed otherwise; submit in Oracle | | 5 | 59 |

## Close

| Id | Type | Purpose | On screen | Interaction / feedback | Pts | Src |
|---|---|---|---|---|---|---|
| hr-090 | `results_breakdown` | Results by objective | `hr-o1`…`hr-o6`, weak below 70% | — | | — |
| hr-091 | `summary` | Close | You can now: live the values · raise concerns · handle leave and pay questions · use Oracle, Qiwa, Mumaris · Links: *HR Quick Reference* PDF · Onboarding survey (URL) · Next: module 07 Clinical Governance | `show_score` | | 61–62 |

## Flow check

- Longest unscored run: `hr-020`→`hr-030` (5 screens). `hr-021` (explore) and `hr-023` (flip) need learner action, but if `lint_visual_plan` still raises `passive_stretch`, move the `hr-030` ethics summary into the `intro_html` of `hr-031` and drop `hr-030`.
- Two `worked_example` screens are each followed by a scored practice.
- No three same-type screens in a row.
