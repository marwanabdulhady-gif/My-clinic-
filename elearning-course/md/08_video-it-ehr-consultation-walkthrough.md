# Video — IT: EHR Consultation Workflow Walkthrough (Module Source)

> **Source file:** `google_drive/IT.mp4` *(not committed to git yet — it contains a non-test patient record; see README §3, item 18)*
> **Drive folder:** top level of the course folder
> **Size:** 35,459,607 bytes · **Duration:** 8 min 38 s · **Video:** 1920×912
> **Last modified in Drive:** 2026-10-07
> **Inspection method:**
> - **Audio check:** the audio track measures **−91 dB throughout** (silent). There is **no narration** in this video. All instructions come from **on-screen captions**.
> - **Visuals:** 104 screenshots sampled every 5 s. 69 are committed in `media/08_it-ehr-walkthrough/` (`tSSSSs.jpg`); 35 were withheld because they show personal identifiers. The 10-second chunk log is `CHUNKS_10s.md`. On-screen text was read with OCR (RapidOCR) and checked by hand.
> - **Patient data:** most of the video uses a test record ("Test Simplified Template Launch"). **However, about 1 minute (5:10–6:10) shows a second, non-test patient record** with name, date of birth, record numbers and a radiology report, and 7:10–7:20 and 8:30 show a phone number and an ID number. Those frames are withheld from the repo. Anonymise the recording before any external use.

---

## 1. What this source is

A **screen-recorded walkthrough of a consultation workflow in the clinic's electronic health record (EHR)** — from opening today's consultation list, through documenting history and diagnosis, ordering medications and labs, referrals, the consultation summary, patient education, and finalising the encounter.

It is a **silent screen recording with on-screen captions and overlay callouts** (e.g. "In order to complete a consultation, please be mindful that the below fields are mandatory prior to completing a patient's consultation"). It is useful as the basis for a **system-training module** for clinicians and front-line staff. It needs a **voice-over** (or on-screen text converted to a narration) before it can serve as a stand-alone course video.

### Learning objectives (derived)
By the end of the module, a clinician should be able to:
1. Open a patient's consultation from the day's list.
2. Complete the **mandatory fields** before finalising a consultation.
3. Add a **primary diagnosis** by ICD-10 code or name, and link orders to the diagnosis.
4. Place **medication, laboratory and other orders**, using the form wizard for packages.
5. Generate and print the **consultation summary**, send **educational material** by SMS, and make **referrals** and **follow-up** arrangements.

---

## 2. Timeline (screen-by-screen)

| Time | Screen | Captions and on-screen actions | What it teaches |
|---|---|---|---|
| 00:00 | **Today's consultation** list (left panel: patient card "Test Simplified Template Launch") | — | Starting point: the consultation queue for the day. Patient is selected from this list. |
| 00:30 | **Consultation form** — sections: Chief complaint, Duration of illness, History of present illness, Past medical history (allergy list, medication list), Physical examination, Plan of care. Top banner: "Record saved successfully." | Callout: *"In order to complete a consultation, please be mindful that the below fields are mandatory prior to completing a patient's consultation."* | The **mandatory fields** for a consultation. Save as you go. |
| 01:00 | **Add Diagnosis** dialog — search box (ICD-10 search); result list such as *Type 2 diabetes mellitus*, *Type 2 diabetes with hyperglycaemia*, *Type 2 diabetes with arthropathy*, *non-insulin-dependent diabetes with hyperglycaemia*, *Type 2 diabetes with kidney complications* | Caption: *"Diagnosis (Primary)*: you may search by ICD-10 code or by diagnostic name."* | Search diagnoses by **ICD-10 code** or by **name**; choose the **primary** diagnosis. |
| 01:30 | **Add Diagnosis — details** (Diagnosis name, Onset date, Chronicity, Mark as problem, Notes) | Callout: *"Click the star to mark an item as a favourite."* | Record the diagnosis details; mark common diagnoses as **favourites**. |
| 02:00 | **Order History** (tabs: Order list, Current items, All orders, Lab orders) with the **Diagnosis** panel and **Active medication** panel | Toast: *"Diagnosis successfully added."* | The diagnosis appears in the diagnosis list; orders are tracked in order history. |
| 02:30 | **Order search** (search by service, order set, package or order profile) | Callout: *"Search by service, lab, referral, package or order profile."* | How to find an order: search across services and packages. |
| 03:00 | **Form wizard** for a package ("Package details", "Collection/Order details", form steps 1 of 4) | Callout: *"The Form Wizard is used to review and modify package details before finalising the order."* | Review and modify a **package** before finalising. |
| 03:30 | **Medication order** form (route, dose, frequency, duration, start date, assessed diagnosis, administration location, "Attachments — drag & drop files here") | Callout: *"Type in the medicine name to complete the order."* Toast: *"Order added"*. | Medication ordering: type the drug name, complete the dose and route, link it to the **assessed diagnosis**. |
| 04:00 | **Order list** after adding items (new orders shown with "New" tags; diagnosis list E11 Type 2 diabetes, and other diagnoses) | — | Review the order list before signing. |
| 04:30 | **Medication order detail** (route, start date, end date, frequency, instructions to patient, notes to pharmacy, administration location) | — | Full medication order fields, including **instructions to the patient** and **pharmacy notes**. |
| 05:00 | **Lab result** (PDF viewer: Complete Blood Count (CBC) report with Haemoglobin, WBC, platelets, MCV, etc., reference ranges and "Verified by" block) | — | How a **lab result** appears in the record. |
| 05:30 | **Order and result toast** ("…successfully"); lab orders list | — | Confirmation of order/result actions. |
| 06:00 | **Topical patch order** (route: topical; frequency; duration; assessed diagnosis *Vitamin D deficiency anaemia*) | — | Medication for a topical route. |
| 06:30 | **Consultation summary** (sections: Lab orders with test name and comments; Special tests (e.g. ECG); Procedures; Referral orders with specialty, type and reason) | Button: *"Download and Print."* | The **consultation summary** — the record for the patient and the file. |
| 07:00 | **Send SMS educational material to patient** (Department name, ICD-10 code, Search, Send) | Title: *"Send SMS — educational material to patient"* | Send **educational material** matched to a condition by ICD-10 code. |
| 07:30 | **Consultation summary — patient & family education** (checklist: Infection control, Medication use, Disease/condition, Treatment, Health & lifestyle, Other) with the diagnoses table | Red banner: *"Ensure all mandatory fields are completed before finalising a patient's consultation."* | Complete **patient and family education** and check all mandatory fields. |
| 08:00 | **Referral and follow-up** (Specialty; Referral reason; Referral type = Internal; Follow-up toggle with interval/duration, Department drop-down ("Select department"; the option list is not legible in the frames), Scanned documents section) | — | Make an **internal referral**, set **follow-up**, and attach **scanned documents**. |

*Note on drug and lab names:* several item names in the medication and lab screens are small or partly obscured in the recording (for example the topical patch product name). Verify all product and test names on the live system before writing them into the course.

---

## 3. Process map (the workflow the video demonstrates)

1. **Open** the patient's consultation from today's list.
2. **Complete the consultation fields** — chief complaint, duration, history, past history, examination, plan of care. Mandatory fields must be complete.
3. **Add the diagnosis** — search by ICD-10 code or name; set the **primary** diagnosis; add details (onset, chronicity); optionally mark a favourite.
4. **Place orders** — search across services, labs, referrals and packages; use the **form wizard** for packages; for medications, type the drug name, then complete route, dose, frequency, duration, instructions and pharmacy notes; link each order to an **assessed diagnosis**.
5. **Review the order list** and the **active medication** list.
6. **Generate the consultation summary**, then **print or download** it.
7. **Patient education** — tick the education topics, send **SMS educational material** by ICD-10 code.
8. **Referrals and follow-up** — internal referral, reason, follow-up interval, department; attach documents.
9. **Finalise** — confirm all mandatory fields; the **Consultation complete** step closes the encounter.

---

## 4. Gaps, risks and editing notes

1. **No narration.** The video needs a voice-over, or the course should convert the captions into narration and step prompts.
2. **Patient identifiers on screen.** The main patient is a test record, but 5:10–6:10 shows a second patient's full record (name, DOB, IDs, radiology report) and 7:10–7:20 shows a phone number. Blur or re-record these sections before the video is used in the course or shared outside the team.
3. **Vendor and product names** are not named on screen beyond the clinic's branding; the course should refer to the "clinic EHR" unless the system name is confirmed.
4. **Clinical content on screen:** the diagnosis and medication examples (type 2 diabetes, anaemia, vitamin D) are examples — the course should not present them as clinical guidance. Add a clinical-disclaimer slide.
5. **Dense screens:** several frames are small. Re-record the critical steps at a larger zoom (or capture sub-clips) for the course.
6. **Accessibility:** captions are visual only. Add captions/subtitles and narration.
7. **Version control:** the screens reflect a specific build. Confirm the EHR version before publishing and re-record after any UI change.
8. **Interactive candidates:** "find the mandatory fields" click-through (00:30 and 07:30), ICD-10 search exercise (01:00), order-to-diagnosis linking drill (03:30–04:30), consultation-summary checklist (06:30–07:30), referral and follow-up set-up (08:00).

---

## 5. Detailed pass by minute (second review)

Full 10-second log: `media/08_it-ehr-walkthrough/CHUNKS_10s.md`. Windows 5:00–7:40 and 8:30–8:38 are **withheld** because they contain personal identifiers; they are summarised at workflow level only.

| Time | Phase | What happens on screen |
|---|---|---|
| 0:00–0:30 | Sign in and find the patient | Login with a test user account. The consultation list shows the day's patients, and the test patient is opened. |
| 0:30–1:10 | Consultation form | Save the basic information and chief complaint. The "Record saved successfully" message appears. The history, past medical history, physical examination and plan-of-care sections are completed. |
| 1:10–1:40 | Diagnosis | Search for the diagnosis by ICD-10 code or name. Select E11 (type 2 diabetes mellitus) and mark it as the primary problem. Open the consultation summary tab. |
| 1:40–4:50 | Orders | Open order entry and search by service, item, referral package or order profile. Orders covered: a CBC and TSH (labs), an ECG, a lornoxicam injection (IM/IV), a diclofenac sachet (added to favourites), vitamin D and a hair package (Form Wizard, step 1 of 6), Fevadol (non-formulary: approval needed), and Augmentin. Banners confirm each order ("Ordered successfully") and the screen notes that the order button must be pressed. |
| 4:50–5:00 | Order management | "Item deleted successfully" appears. The all-orders view lists past orders. |
| 5:00–6:20 | Withheld | Second patient's record: order history, lab results, radiology report and appointment. Workflow: review the history and allergies before ordering. |
| 6:20–6:40 | Order processing and summary | Processing status is shown. The consultation summary lists the diagnoses, lab orders, special tests and the medication list. |
| 6:40–7:00 | Summary and download | "Download and Print" is shown. The visit summary is reviewed. |
| 7:00–7:40 | Withheld | Visit-summary preview (patient fields) and an SMS screen. Workflow: send educational material by SMS, chosen by department and ICD-10 code (for example E11, with diabetes education leaflets). The phone number is not recorded here. |
| 7:40–8:20 | Education and referral | The "add patient and family educations" warning appears. The referral form has a speciality, referral type and appointment timing (next available, within a week, two weeks, a month). A referral to endocrinology (internal, 30 September 2024) is saved and listed. |
| 8:20–8:30 | Close the consultation | "Record saved successfully" and the sick-leave panel are shown. |
| 8:30–8:38 | Withheld | Sick-leave report. The screen shows that printing is disabled on this page. |

### Points to check before the course goes live
- The sequence and button names need checking on the live system (the version in the recording may differ).
- Medicine and lab names are small in several frames. Confirm them against the formulary before they go into quiz questions.
- Clinical examples (diabetes, anaemia, vitamin D) are illustrations only. Add a disclaimer slide.
