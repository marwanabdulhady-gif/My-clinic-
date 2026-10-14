# Phase 1 — Action map & objectives (08 EHR Consultation)

## 1. Business goal

Every consultation is completed in the EHR on the day, with all mandatory fields, a specific primary diagnosis, and orders linked to that diagnosis. Measured by: incomplete-consultation reports, orders without a linked diagnosis, help-desk tickets from new clinicians, and (with RCM) rejections for diagnosis–order mismatch.

## 2. Action map

| # | On-the-job action | Why it goes wrong | Practice |
|---|---|---|---|
| A1 | Open the right patient's consultation from today's list | Rushed selection | Simulation |
| A2 | Complete the mandatory fields before finalising | Fields hidden in sections; finalise fails | Hotspot explore + MCQ |
| A3 | Add a specific primary diagnosis by ICD-10 search; use favourites | Symptom codes; slow searching | Simulation with typing |
| A4 | Place medication, lab and package orders linked to the assessed diagnosis | Orders not linked; non-formulary surprises | Medication and package simulations; MCQs |
| A5 | Print the summary, send SMS education, complete patient & family education | Steps skipped | Simulations |
| A6 | Make an internal referral and set follow-up | Wrong type or no follow-up | Simulation |

## 3. Learning objectives

| Id | Objective | Assessed by |
|---|---|---|
| `ehr-o1` | Open a consultation and complete the mandatory fields. | `ehr-010`, `ehr-012` |
| `ehr-o2` | Add a primary diagnosis using ICD-10 code or name search. | `ehr-020` |
| `ehr-o3` | Place medication, lab and package orders linked to the assessed diagnosis. | `ehr-031`, `ehr-032`, `ehr-033`, `ehr-034` |
| `ehr-o4` | Produce the consultation summary, send education by SMS, and make a referral with follow-up. | `ehr-040`, `ehr-041`, `ehr-050` |
| `ehr-o5` | Put the complete consultation workflow in the correct order. | `ehr-051` |

## 4. Seat-time budget

| Part | Screens | Minutes |
|---|---|---|
| Intro & workflow map | 3 | 3 |
| Open & document | 3 | 4 |
| Diagnosis | 1 | 3 |
| Orders | 5 | 7 |
| Summary & education | 3 | 4 |
| Referral & finish | 3 | 3 |
| Close | 2 | 1 |
| **Total** | **20** (+1 optional video) | **~25** |

## 5. Pedagogy notes

- **Show → try**: the whole workflow is shown once as a map, then each step is practised as a guided simulation with hints. No narration of every click; the instruction text carries it.
- The simulations are **practice on a test patient**, so mistakes are safe. Feedback explains the consequence in the real system (e.g. "the consultation can't be completed without a plan of care").
- Link to RCM (module 05) on the diagnosis and order screens: a linked, specific diagnosis is what gets claims approved.
