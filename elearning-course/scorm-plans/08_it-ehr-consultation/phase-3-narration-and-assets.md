# Phase 3 — Narration & assets (08 EHR Consultation)

Gates: `lint_narration_script` → `export_audio_script` → `lint_authoring_plan(stage="planning")` → **STOP for approval**.

## 1. Narration approach

The source video is silent. Narration is **light**: a short spoken intro on each simulation screen (why this step matters), then the learner follows on-screen instructions. Simulations have `lock_until_complete: false`. Every instruction is in text, so the module works with sound off.

## 2. Narration outline

| Screen | Sec | Narration intent |
|---|---|---|
| ehr-000 | 12 | You'll practise a full consultation on a test patient; mistakes are safe here. |
| ehr-001 | 25 | Complete, specific, linked — on the day. Read the disclaimer. |
| ehr-002 | 30 | The nine steps at a glance. |
| ehr-010 | 10 | Start from today's list. |
| ehr-011 | 25 | The mandatory sections; save as you go. |
| ehr-012 | 8 | Set up. |
| ehr-020 | 20 | Search by code or name; the primary diagnosis drives everything after it. Mentor: "My first week, I typed 'diabetes' and picked the first line. It wasn't the one I meant." |
| ehr-030 | 25 | Five ways to find an order; the Form Wizard checks a package before you commit. |
| ehr-031 | 15 | Link every medication to the diagnosis you assessed. |
| ehr-032 | 10 | Review the package; remove what you don't need. |
| ehr-033 / 034 | 8 each | Set up. |
| ehr-040 | 10 | The summary is the record the patient takes home. |
| ehr-041 | 12 | Education by SMS, matched to the diagnosis code. |
| ehr-042 | 20 | Patient & family education is required before you finish. |
| ehr-050 | 15 | Internal referral and follow-up. |
| ehr-051 | 8 | Set up. |
| ehr-052 | 20 | Completing the encounter; where to get help. |
| ehr-090 | 10 | Read your results. |
| ehr-091 | 15 | Close. |

Estimated audio: ~5 minutes.

## 3. Lexicon used

EHR, ICD-10, E11, HPI, CBC, TSH, ECG, SMS, IM/IV ("I-M, I-V"), drug names approved in B6 (with pronunciation).

## 4. Asset manifest

| Planned id | Kind | Screens | Brief | Source | Alt text (draft) |
|---|---|---|---|---|---|
| ehr-shot-list | screenshot | ehr-010 | Today's consultation list, test patient only, 1920×1080 at 125% zoom | own (test env) | "Today's consultation list with one test patient." |
| ehr-shot-form | screenshot | ehr-010, 011 | Consultation form with all sections visible (may need 2 crops) | own | "Consultation form showing mandatory sections." |
| ehr-shot-dx-1..5 | screenshots | ehr-020 | Add Diagnosis dialog: empty, typed E11, results, details, star | own | per step |
| ehr-shot-order-1..6 | screenshots | ehr-031 | Order search → medication form states | own | per step |
| ehr-shot-wizard-1..4 | screenshots | ehr-032 | Form Wizard steps | own | per step |
| ehr-shot-summary-1..3 | screenshots | ehr-040 | Summary sections, Download and Print | own | per step |
| ehr-shot-sms-1..5 | screenshots | ehr-041 | SMS education screen states; **phone field shows a fictional number** | own | per step |
| ehr-shot-ref-1..6 | screenshots | ehr-050 | Referral and follow-up | own | per step |
| ehr-pdf-quickref | PDF | ehr-091 | 1-page EHR consultation quick-reference card | own | n/a |
| ehr-vid-walkthrough *(optional)* | MP4 + VTT | ehr-060 | Screen recording on test patient + voice-over; rendered outside the server (over the 60 s `render_motion_video` limit), uploaded with `add_asset` | own | transcript |
| ehr-aud-* | audio | narrated screens | TTS | ai-generated | transcript |

**Screenshot rules:** test environment only; fictional names, MRNs, phone and ID numbers; DPO reviews every image before upload; record the EHR version in each asset's notes. `media/08_it-ehr-walkthrough/` frames are **reference only**.

## 5. Activity plans

| Activity | Objective | Rules | Success | Accessibility |
|---|---|---|---|---|
| Simulations (010, 020, 031, 032, 040, 041, 050) | o1–o4 | Each step: click region (`rect`) or type (`input_accepted`); hint after a wrong attempt | All steps completed | Each step has a text instruction; regions reachable by keyboard; screenshots have alt text; a text "steps list" appears in the feedback |
| ehr-051 sorting | o5 | 9 items | correct order | keyboard |

## 6. Approval request

EHR lead approves every screenshot, instruction and region; DPO approves that no real data appears; Medical Director approves clinical examples and the disclaimer; Pharmacy approves drug names.
