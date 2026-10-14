# 08 — EHR Consultation Workflow: Guided Simulation (SCORM plan)

![My Clinic logo](../00_program/brand/logo-preview.png)

| Item | Value |
|---|---|
| Source | `../../md/08_video-it-ehr-consultation-walkthrough.md` (from `IT.mp4`, 8 min 38 s, **silent**, contains patient identifiers) |
| Package title | My Clinic — EHR Consultation Workflow: Guided Simulation |
| Module prefix / ids | `ehr-` |
| Brand | My Clinic brand — [`brand-identity.md`](../00_program/brand/brand-identity.md); module colour **Dark teal #006E78**; layouts L1–L6 |
| Audience | Physicians and clinical staff who document consultations in the clinic EHR |
| Seat time | ~25 minutes |
| SCORM | 1.2 |
| Completion | `viewed_all_and_passed`, passing score **80** |
| Scored screens | 11, 90 points in total |
| Prerequisite | 05 RCM Part A (recommended: links diagnosis and orders to coding) |

## Design idea in one paragraph

The source is a silent screen recording of a full consultation in the clinic EHR, with captions and callouts — and about a minute of a **real patient's record**. It cannot be used as is. The package is planned around **new screenshots captured on a test patient in a test environment**, turned into guided `simulation` screens: open the consultation, find the mandatory fields, add the primary diagnosis by ICD-10 search, place a medication order linked to the diagnosis, order a lab package through the form wizard, print the summary, send SMS education, make an internal referral with follow-up, and finally put the whole workflow in order. A narrated, captioned walkthrough video can be re-recorded later as an optional reference.

## Files

| Phase | File |
|---|---|
| 0 — Source lock | [phase-0-source-lock.md](phase-0-source-lock.md) |
| 1 — Action map & objectives | [phase-1-action-map.md](phase-1-action-map.md) |
| 2 — Storyboard | [phase-2-storyboard.md](phase-2-storyboard.md) |
| 3 — Narration & assets | [phase-3-narration-and-assets.md](phase-3-narration-and-assets.md) |
| 4 — Build | [phase-4-build.md](phase-4-build.md) |
| 5 — QA & delivery | [phase-5-qa-and-delivery.md](phase-5-qa-and-delivery.md) |

## Current status

**Blocked on Phase 0**: test environment and test patient for new screenshots (D6), EHR version and button names, formulary names, clinical disclaimer approval. **Do not use `IT.mp4` or its frames in any deliverable.**
