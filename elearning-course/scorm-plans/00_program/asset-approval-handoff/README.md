# G10 asset approval handoff — full six-scene drill

**Prepared for review, not sent. Nothing here grants production approval.**

This packet is the next step after [G10 reference restoration](../g10-visual-restoration.md).
It covers **44 asset records: 13 safety visuals (including all six Code Red scenes) and 31
unique EHR screenshots**. It is not a new 44-image commission: the safety set includes four
client photos; EHR files are test-environment captures. The overall brief still calls for
21/22 new still illustrations across the programme, five Oracle captures and zero required videos.

## Send / review sequence

1. Course owner names the accountable Safety Manager, Facilities/Biomedical reviewer, EHR
   lead and DPO using the [decision sheet](../decision-sheet.md). Do not infer names or email
   addresses. Use the [kick-off pack](../kickoff-pack.md) to close the facts below.
2. Send Safety the six scene briefs in
   [drill-scene-manifest.json](../../02_health-and-safety-2/storyboard/drill-scene-manifest.json),
   the [module 02 cards](../../02_health-and-safety-2/storyboard/storyboard.md) and its Word
   review document. Ask for a written decision per node before scene production.
3. Send Facilities/Biomedical the [module 01 cards](../../01_health-and-safety-1/storyboard/storyboard.md)
   for treatment-room targets and the editable pump-label example. Request permissioned
   client photos of the eyewash, extinguisher and both spill kits.
4. Send IT/DPO the [31-shot capture manifest](../../08_it-ehr-consultation/storyboard/capture-manifest.json)
   and [module 08 cards](../../08_it-ehr-consultation/storyboard/storyboard.md). Request the
   approved test environment and a completely fictional patient; do not request credentials
   in this CSV, in chat or in Git. IT supplies access through its normal secure process.
5. Reviewers return a copy of `response-template.csv`, with name, date, a signed decision or
   a link to its signed record, and corrections. Store actual responses separately from
   generated templates, and write approved facts back to Phase 0 before building assets.

## Approval questions that must close

### Safety / Facilities / Biomedical

- D1 / module 02 B1: confirm the spill threshold. The spill-volume cue must match the approved
  rule; a draft bottle illustration must not decide the threshold.
- D2 / module 02 B2: confirm code wording and branch extensions. Call scripts stay editable
  HTML; image generation must not bake in text, phone numbers or code labels.
- Sign all six authored drill nodes (rescue, alarm, contain, extinguish/evacuate, stairs/chair,
  assembly/all-clear), including safe actions, scene targets and the trained-only distinction.
- Module 02 B8: confirm generic versus branch-specific assembly-point treatment.
- Module 01 B6: confirm emergency sockets, utilities and target items in the treatment room.
- Biomedical: confirm the overdue-label example and escalation rule. Use fictional label dates
  in an editable overlay; never let an image model invent an inspection date or label.
- For client photos, record ownership/permission and verify equipment against the current site.
  Kit procedure remains blocked by module 02 B4; photography does not approve the procedure.

### IT / EHR / DPO

- B2 / D6: approve the test environment and fictional demographics before capture. Source
  `IT.mp4` and patient-bearing frames are never substitutes.
- B3/B5: record EHR version and confirm labels. Capture at 1920×1080 and 125% browser zoom.
- B4/B6/B8/B9: confirm mandatory fields, approved examples, SMS feature/leaflets, and referral
  wording/timing. Medication or lab examples show system use, not prescribing guidance.
- Use a test-only SMS destination; do not send to a real patient. Confirm safe test execution
  for Order, Send and Save actions with IT before running them.
- DPO reviews **every captured file**, including crops, for names, IDs, record numbers, phones,
  notifications and browser chrome. Review current pixels, not just the fictional patient setup.
- Reuse the consultation-form shot on ehr-011. Up to four legibility crops may be needed, but
  they are not extra workflow steps and still require per-file review.

## Evidence and release rules

`status`, names, dates and signed decisions are intentionally blank/unapproved in the prepared
packet. There are no captured images, generated scenes or signed client approvals attached.
Do not use a row's existence, a tool result or a merge as approval.

Before any asset ships: close its decisions in Phase 0; obtain reviewer sign-off; record source,
license/permission, author, date and approved file reference in provenance; then upload through
Phase 4. Coordinates, hit regions, simulation input aliases and game logic need separate review
against the final visual. Asset approval does not complete the SCORM/LMS/pilot gate.

**Cast:** Noor and Dr. Omar only as named guides; any scene extras are unnamed and non-speaking.
No new character design, voice or video generation is authorised by this packet.

## Response tracker index

Briefs, alt text and gates are in `response-template.csv` and `request.json`. All rows begin
`Pending — not submitted`. This generator refuses to overwrite human responses in the template.

| Asset | Core screens | Planned placement | Reviewer role |
|---|---|---|---|
| `hs1-img-eyewash` | hs1-506 | Screen visual; production placement reviewed by the SME. | Facilities + Safety/EHS |
| `hs1-img-treatment-room` | hs1-701 | Screen visual; production placement reviewed by the SME. | Facilities + Safety/EHS |
| `hs1-img-pump-label` | hs1-802 | Screen visual; production placement reviewed by the SME. | Biomedical Engineering + Facilities |
| `hs2-img-drill-1` | hs2-030 | Node 1 · Rescue | Safety Manager + EHS |
| `hs2-img-drill-2` | hs2-030 | Node 2 · Alarm | Safety Manager + EHS |
| `hs2-img-drill-3` | hs2-030 | Node 3 · Contain | Safety Manager + EHS |
| `hs2-img-drill-4` | hs2-030 | Node 4 · Extinguish or evacuate | Safety Manager + EHS |
| `hs2-img-drill-5` | hs2-030 | Node 5 · Evacuate | Safety Manager + EHS |
| `hs2-img-drill-6` | hs2-030 | Node 6 · Assembly point | Safety Manager + EHS |
| `hs2-img-extinguisher` | hs2-040 | Screen visual; production placement reviewed by the SME. | Safety Manager + EHS |
| `hs2-img-kit-chem` | hs2-051 | Left comparison image | Safety Manager + EHS |
| `hs2-img-kit-bio` | hs2-051 | Right comparison image | Safety Manager + EHS |
| `hs2-img-spill-photo` | hs2-064 | Screen visual; production placement reviewed by the SME. | Safety Manager + EHS |
| `ehr-shot-list` | ehr-010 | ehr-010 step 1 · consultation list | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-form` | ehr-010, ehr-011 | ehr-010 step 2; reused on ehr-011 for mandatory-field exploration | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-dx-1` | ehr-020 | Step 1 · Add Diagnosis dialog | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-dx-2` | ehr-020 | Step 2 · Diagnosis search with draft E11 input | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-dx-3` | ehr-020 | Step 3 · Diagnosis results | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-dx-4` | ehr-020 | Step 4 · Primary diagnosis details, onset and chronicity | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-dx-5` | ehr-020 | Step 5 · Diagnosis favourites star | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-order-1` | ehr-031 | Step 1 · Order search | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-order-2` | ehr-031 | Step 2 · Drug-name search using the approved B6 example | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-order-3` | ehr-031 | Step 3 · Medication route, dose, frequency and duration fields | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-order-4` | ehr-031 | Step 4 · Assessed-diagnosis selection | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-order-5` | ehr-031 | Step 5 · Patient-instructions fields | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-order-6` | ehr-031 | Step 6 · Order submission control | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-wizard-1` | ehr-032 | Step 1 · Package search using the approved B6 example | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-wizard-2` | ehr-032 | Step 2 · Form Wizard item review | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-wizard-3` | ehr-032 | Step 3 · Form Wizard item removal | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-wizard-4` | ehr-032 | Step 4 · Form Wizard finalisation | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-summary-1` | ehr-040 | Step 1 · Consultation Summary entry | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-summary-2` | ehr-040 | Step 2 · Lab orders, special tests and referrals in summary | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-summary-3` | ehr-040 | Step 3 · Download and Print control | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-sms-1` | ehr-041 | Step 1 · Send SMS educational-material entry | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-sms-2` | ehr-041 | Step 2 · SMS department selection | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-sms-3` | ehr-041 | Step 3 · SMS diagnosis-code search | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-sms-4` | ehr-041 | Step 4 · SMS leaflet selection | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-sms-5` | ehr-041 | Step 5 · SMS Send control | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-ref-1` | ehr-050 | Step 1 · Referral entry | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-ref-2` | ehr-050 | Step 2 · Referral specialty selection | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-ref-3` | ehr-050 | Step 3 · Referral-reason field | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-ref-4` | ehr-050 | Step 4 · Referral type and timing fields | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-ref-5` | ehr-050 | Step 5 · Follow-up toggle and interval | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |
| `ehr-shot-ref-6` | ehr-050 | Step 6 · Referral Save control | EHR lead + DPO; Pharmacy/Medical Director for examples as applicable |

## Regenerate

```bash
python3 elearning-course/scorm-plans/tools/prepare_asset_approval_handoff.py
```

The packet is deterministic from Phase 3 manifests. If returned responses were entered in the
template, archive them separately before regeneration. Never erase reviewer evidence to make
the tool pass. No email is sent by the tool.
