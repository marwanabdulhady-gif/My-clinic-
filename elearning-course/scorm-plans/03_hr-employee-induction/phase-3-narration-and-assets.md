# Phase 3 — Narration & assets (03 Welcome On Board)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 1. Voice

This module is the learner's first contact with My Clinic. Option to use a **human voice** (or a short welcome video from the CEO/HR head, recorded in-house) for `hr-000`/`hr-001` only; TTS for the rest. Decide in Phase 0 (program D10).

## 2. Narration outline

| Screen | Sec | Narration intent |
|---|---|---|
| hr-000 | 15 | Warm welcome; what the next 45 minutes give you. |
| hr-001 | 35 | Why My Clinic exists, in plain words; a short honest line: "Everyone here remembers their own first week — and how much there was to take in." |
| hr-002 | 10 | Invite the icebreaker; no right answer. |
| hr-010 | 40 | Values are behaviours, not posters; one example for each. |
| hr-011 | 8 | Set up. |
| hr-012 | 45 | The 7Cs explain where the company is going; find the pillar your role touches most. |
| hr-013 | 8 | Set up. |
| hr-014 | 20 | Who we serve, including people who are healthy today. |
| hr-020 | 30 | From one clinic in 2017 to a network; what each step added. |
| hr-021 | 15 | Explore the branches; you'll hear their codes (J1, J2…) every day. |
| hr-022 | 20 | The leadership team and what each role looks after. |
| hr-023 | 15 | Recognition we're proud of — and that we have to keep earning. |
| hr-030 | 35 | The four ethics values; when in doubt, ask and report within 24 hours. |
| hr-031 | 15 | Set up the supplier evaluation. |
| hr-032 / 033 | 8 each | Set up. |
| hr-040 | 25 | Where help lives: your HR mailbox, Oracle, and the quick-reference PDF. |
| hr-041 | 40 | A quick tour of leave types; you'll practise the ones people ask about most. |
| hr-042 | 8 | Set up. |
| hr-043 | 40 | Talk through the sick-leave example step by step. |
| hr-044 | 15 | Set up the leave desk: four colleagues, four questions. |
| hr-045 | 10 | Set up adaptive practice: it stops early if you've got it. |
| hr-050 | 30 | What GOSI is and why the deduction protects you. |
| hr-051 | 30 | Work through 585 riyals aloud. |
| hr-052 | 8 | Set up. |
| hr-053 | 35 | Hourly rate first, then the multiplier. |
| hr-054 | 8 | Set up. |
| hr-060 | 10 | Set up: one system per task. |
| hr-061 | 15 | Set up the simulation. |
| hr-062 | 8 | Set up. |
| hr-070 | 25 | ID card care; the benefits you can use from day one. |
| hr-071 | 8 | Set up. |
| hr-080 | 25 | Contracts on Qiwa; if you ever leave, how to do it well. |
| hr-081 | 8 | Set up. |
| hr-090 | 12 | Read your results. |
| hr-091 | 25 | What you can now do; please complete the onboarding survey. |

Estimated audio: ~13 minutes.

## 3. Lexicon used

GOSI, SCFHS, Mumaris, Qiwa, HRMS, Oracle ("OR-uh-kul"), SAR, HHC, MCJ1 ("M-C-J-one"), MCJ2, PRC ("P-R-C"), J1–J4 ("J-one"…), D1, R1, EOS ("end of service"), IELTS ("eye-elts"), TOEFL ("toe-full"), CBAHI, JCI ("J-C-I").

## 4. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| hr-img-hero | photo | hr-001 | Real My Clinic team or clinic photo (consented) | own | "My Clinic team at the J1 reception." |
| hr-img-values-icons | SVG ×4 | hr-010 | Line icons for the four values | own | decorative |
| hr-img-7c-icons | SVG ×7 | hr-012 | Line icons (headset, syringe, gears, handshake, stethoscope, heart-hands, coins) redrawn from slide 10 | own | decorative |
| hr-img-map | SVG | hr-021 | Minimal map of western KSA and Riyadh with 7 pins | own | "Map of My Clinic branches in Jeddah, Rabigh and Riyadh." |
| hr-img-branches | photos ×7 | hr-021 (in region text) | Branch photos from slides 14–15 if rights confirmed | local (after Phase 0) | per branch |
| hr-img-leaders | photos ×4 | hr-022 | Consented portraits | local (consent on file) | "<name>, <role>." |
| hr-img-oracle-1..5 | screenshots | hr-061 | Test-account screenshots, 1920×1080, no real names (B8) | own | per step, e.g. "Oracle Time and Absences page." |
| hr-img-dress | illustrations ×3 | hr-071 feedback | Front office, medical team, back office outfits (replaces slide 58 art) | ai-generated | per role |
| hr-pdf-quickref | PDF | hr-040, hr-091 | **HR Quick Reference** (2 pages): leave tables, GOSI, overtime, contacts — written by HR from confirmed policy | own | n/a |
| hr-char-noor | character | hr-031, hr-044 | Program mentor (explaining, concern) | ai-generated | per pose |
| hr-aud-* | audio | narrated screens | TTS (or human for hr-000/001) | ai-generated / own | transcript |

## 5. Activity plans

| Activity | Objective | Rules | Success | Failure | Accessibility |
|---|---|---|---|---|---|
| hr-031 ethics | hr-o2 | 3 nodes | ≥ 2 best | replay | buttons |
| hr-044 leave desk | hr-o3 | 4 nodes, one per colleague | ≥ 3 | replay | buttons; rule text in feedback |
| hr-045 adaptive | hr-o3 | Elo, 12-item bank, max 6, stop when mastery reached | pass ratio 0.6 | items keep coming up to max | MCQ radio buttons |
| hr-061 Oracle sim | hr-o5 | 5 click steps, `rect` regions, hint per step | all steps | retry step | each step has a text instruction and alt text; offer a text-only "steps list" in feedback |

## 6. Approval request

HR approves: storyboard, all numbers against the verified facts register, the leave-desk and ethics scripts, the adaptive item bank (all 12 items + feedback), the Quick Reference PDF, and the Oracle screenshots (no real data). Comms approves leaders, awards and branch screens.
