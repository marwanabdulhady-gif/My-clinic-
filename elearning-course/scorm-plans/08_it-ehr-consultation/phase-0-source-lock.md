# Phase 0 — Source lock (08 EHR Consultation)

## 1. Owners

| Role | Responsibility |
|---|---|
| IT Applications / EHR lead (SME lead) | Workflow, screens, test environment; signs off |
| Medical Director or CMIO | Clinical examples and disclaimer |
| Pharmacy lead | Formulary / non-formulary examples |
| Data Protection Officer | PHI decision (D6), screenshot review |
| RCM lead | Diagnosis-to-order linking message (links to module 05) |

## 2. Blocking items

| # | Item | Source location | Needed decision | Owner | Status |
|---|---|---|---|---|---|
| B1 | **Patient identifiers in `IT.mp4`** (5:10–6:10 full record; 7:10–7:20 phone; 8:30 ID) | video | Program **D6**: the video and its frames are not used. Decide separately whether to remove the file from Git history and Drive sharing | IT + DPO | Open |
| B2 | Test environment + test patient ("Test Simplified Template Launch" or new) for **all** new screenshots | — | Provide test login, test patient with fictional demographics, and a capture session (1920×1080, browser zoom 125% for legibility) | EHR lead | Open |
| B3 | EHR product name and version | — | Name it or call it "the clinic EHR"; record the version so screenshots can be refreshed | EHR lead | Open |
| B4 | Mandatory fields before completing a consultation | 00:30, 07:30 | Exact list (chief complaint, duration, HPI, past history incl. allergies and medications, examination, plan of care, diagnosis, patient & family education?) | EHR lead | Open |
| B5 | Button and screen names (Today's consultation, Add Diagnosis, Order History, Form Wizard, Consultation Summary, Download and Print, Send SMS, Referral) | whole video | Confirm on the current build | EHR lead | Open |
| B6 | Medication and lab examples (lornoxicam, diclofenac, Fevadol non-formulary, Augmentin; CBC, TSH, ECG; vitamin D, "hair package") | 1:40–4:50 | Choose 2–3 neutral examples approved by Pharmacy; confirm which item needs non-formulary approval | Pharmacy + Medical Director | Open |
| B7 | Clinical disclaimer | — | Wording: "Clinical examples show how to use the system. They are not treatment guidance." | Medical Director | Open |
| B8 | SMS education: department list and ICD-10 linked leaflets | 7:00 | Confirm the feature exists in the current build and an E11 leaflet is available in test | EHR lead | Open |
| B9 | Referral timing options (next available, within a week, two weeks, a month) and internal vs external | 7:40–8:20 | Confirm | EHR lead | Open |
| B10 | Sick-leave panel (printing disabled) | 8:20–8:38 | In scope or not? Recommended: out of scope (separate job aid) | EHR lead | Open |

## 3. Verified facts register

| Fact | Value | Source | Confirmed by | Date |
|---|---|---|---|---|
| Diagnosis search | by ICD-10 code or by name | 01:00 caption | | |
| Favourites | click the star | 01:30 caption | | |
| Order search | by service, lab, referral, package or order profile | 02:30 caption | | |
| Form Wizard | review and modify package details before finalising | 03:00 caption | | |
| Mandatory fields | *pending B4* | | | |

## 4. Exit criteria

B1 decided; B2 capture session done; B3–B9 confirmed; B10 decided.
