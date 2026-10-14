# My Clinic — E-Learning Course Source Pack

This folder turns the Google Drive course folder into one detailed Markdown file per source. The Markdown files are the basis for the e-learning course.

- **Source folder:** Google Drive `15HyVEiMlgNqjr2tQa1QjVxJ0v-TuFmgj` (subfolders: `HR`, `Health & Safety`, `RCM/RCM`, and top-level files)
- **Local copies of sources:** `../google_drive/` (flattened; original file names kept)
- **Markdown modules:** `md/`

## 1. Source → Markdown map

| # | Drive location | Source file | Markdown module | Pages / slides | Verification status |
|---|---|---|---|---|---|
| 01 | Health & Safety/ | `Health & Safety 1.pdf` | `md/01_health-and-safety-1_facility-management-and-safety.md` | 65 pages, 9 modules | Full text read; every page reviewed on contact sheets |
| 02 | Health & Safety/ | `Health & Safety 2.pdf` | `md/02_health-and-safety-2_safety-hazards-fire-and-chemicals.md` | 31 pages (mostly image-based) | Every page reviewed on contact sheets; slides 25 and 29 are blank or illegible in places |
| 03 | HR/ | `HR.pptx` | `md/03_hr-employee-induction.md` | 62 slides | All text read; unique images reviewed |
| 04 | top level | `Operations & My Care Structure.pptx` | `md/04_operations-and-my-care-structure.md` | 6 slides | All text read; org-chart reporting lines not in text layer |
| 05 | RCM/RCM/ | `How to optimize billing via coding , documentation.docx` | `md/05_rcm-billing-documentation-script.md` | Speaker script, 16 sections | Full text read (24 KB) |
| 06 | RCM/RCM/ | `how to optimize billing via coding ,, documentation  2026.pptx` | `md/06_rcm-billing-documentation-slides-2026.md` | 14 slides | Text plus all images reviewed; slide 6 and EBP figures approximate |
| 07 | top level | `Quality, Safety and Risk Orientation.mp4` | `md/07_video-quality-safety-and-risk-orientation.md` | 8 min 56 s, narrated | 107 screenshots every 5 s (`media/07_quality-safety-risk/`); 10 s chunk log with OCR and machine narration (`CHUNKS_10s.md`, low accuracy) |
| 08 | top level | `IT.mp4` | `md/08_video-it-ehr-consultation-walkthrough.md` | 8 min 38 s, silent | 104 screenshots every 5 s; 69 committed, 35 withheld (patient identifiers); 10 s chunk log in `CHUNKS_10s.md` |

A short list of Drive IDs is not recorded in these files because they were not all verified. The DOCX ID is `1RAeKs0Pm6Z4K8XfDbHU_Ha-Oza71V15m`.

## 2. Repository decisions

- **Quality video is committed** (`google_drive/Quality, Safety and Risk Orientation.mp4`, 39 MB, plain Git; Git LFS is not available in this sandbox). It contains no patient data.
- **IT video is not committed yet** (`google_drive/IT.mp4`, 35 MB, gitignored). It shows a non-test patient record (item 18). Commit it only after the recording is anonymised or the team accepts that risk.
- **Screenshots** are in `media/` (about 9 MB). 35 IT frames that show personal identifiers are withheld. The Quality frames have no identifiers.
- **Source IDs and sizes** are in `SOURCES.md`.
- **Other sources are committed** (about 17 MB in total) so the course team can trace each module to its source.

## 3. Conflicts and gaps to resolve before publishing

1. **Code Orange spill threshold.** H&S 1 (p.40) says a spill of **500 mL or more**, or a highly toxic/reactive/explosive substance, triggers Code Orange. H&S 2 (p.22) says a minor spill is **under 1 L** but also says a spill **over 500 mL** triggers Code Orange. Recommended single rule: ≥ 500 mL or hazardous substance → Code Orange.
2. **Emergency code naming and extensions.** H&S 2 uses placeholder extension "5555" for most codes. Code Silver and some other codes are named differently across the two H&S decks. Choose one code sheet.
3. **HR sick-leave wording.** The slide says days 31–90 have **25% deducted** (so 75% pay). Confirm the policy before publishing.
4. **HR compassionate leave.** "130 calendar day" for the death of a husband (Muslim female employee) looks like a typo or uses the standard waiting period. Confirm with HR.
5. **HR agenda.** Clinical Risk and Infection Control are on the agenda, but the deck has no slides for them. The agenda also shows "12:15 am" (likely pm).
6. **HR branch names.** The timeline lists Al Tahlia (2025) and Obhur (2026). The branch slides list Al Andalus (J3, 2025) and Abhor (J4, 2026).
7. **Regulator name.** The billing script says **"CCHI"**; the 2026 deck logo says **"Council of Health Insurance (CHI)"**. Standardise.
8. **Billing deck date.** The file name says 2026; the slides say **August 30, 2023**.
9. **Billing script garbled figures.** "Repeating Vitamin D too early not less than 118" and "Repeating HbA1c before 89 day" are not readable. Confirm the intervals.
10. **EBP counts.** The infographic says 18 added and 10 amended benefits, but shows 10 and 8 headline items. Confirm.
11. **Operations org chart.** The text layer gives labels, not reporting lines. Count labels (PXOs, FMs, Coords) are not clearly tied to units.
12. **Quality transcript.** The narration was recognised offline (CMU PocketSphinx, 10 s chunks, log in `CHUNKS_10s.md`) and has heavy ASR errors. I could not listen to the audio, so this needs a human listen before any quoted sentence is used in an assessment. Screenshots every 10 s are in `media/07_quality-safety-risk/`.
13. **IT video.** It has no narration (audio is silent). On-screen text was OCR'd and logged in 10-second windows in `media/08_it-ehr-walkthrough/CHUNKS_10s.md`. Plan a voice-over or narration script and check the clinical examples before publishing.
18. **Patient identifiers in the IT video.** Module 08 previously said no real patient data was shown. That was wrong. Around 5:10–6:10 the screen shows a second patient's full record (name, DOB, record numbers, radiology report); 7:10–7:20 and 8:30 show a phone number and an ID number. Those frames are withheld. Blur or re-record that section before the video is used or committed.
14. **Placeholders.** H&S 2 p.31 has empty contact boxes, and the cover pages of H&S 1 contain `[Facility Name]` and `[Month Year]`.
15. **Template origin.** H&S 2 PDF metadata says "First Clinic" with a different author. Confirm the branding.
16. **Branding watermark.** The Quality video frames show a NotebookLM watermark. Check the licence before reuse.
17. **Personal data.** The billing 2026 deck includes a claim-rejection log with claim numbers. Anonymise before sharing outside the team. The HR deck includes staff names and emails. Keep only what the course needs.

## 4. Suggested course structure

1. Orientation and HR policies (03)
2. Clinical governance and patient safety (07)
3. Health & Safety (01, 02)
4. Operations and My Care (04)
5. Clinical documentation and billing (05, 06)
6. EHR consultation workflow (08)

## 5. Method notes

- PDFs were read with PyMuPDF text extraction. Image-only pages were reviewed as contact sheets.
- The PPTX files were read with python-pptx, including grouped shapes, plus the embedded images.
- The DOCX was read with python-docx.
- Video audio was checked for speech (Quality has speech; IT is silent). Quality was transcribed with an offline recogniser in 10 s chunks. IT was reviewed by OCR of screenshots every 5 s and hand-checked; it has no narration.
