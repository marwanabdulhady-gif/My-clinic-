# Sample course — Oracle Learning test guide

**For:** My Clinic LMS administrator (Oracle Learning) · **From:** Leap to Success (L2S) · **Time needed:** about 30 minutes

This sample is a short, real My Clinic course built with exactly the same tools as the eight induction courses. If it uploads, launches, tracks and resumes correctly in your Oracle Learning, the full courses will too.

## 1. Files

| File | Use |
|---|---|
| **`MC_Sample_OracleLearning_1.2.zip`** | **Upload this one.** SCORM 1.2 — the standard all Oracle Learning releases support. |

Do not unzip the files. Upload each zip as it is.

## 2. Upload and assign (Oracle Learning)

Menu names vary slightly by release; your Oracle Learning administrator guide has the exact path for your pod.

1. As a learning administrator, create a new **eLearning / online content** item (SCORM type) and upload `MC_Sample_OracleLearning_1.2.zip`.
2. Wait until processing finishes and the content shows as active. (If it stays "processing" for more than 30 minutes, note it in the result sheet.)
3. Add the content to a test **course and offering** (or a self-paced activity), then assign it to yourself and one test learner.
4. Leave the launch settings at their defaults first. If launch shows a blank page, try opening the content in a **new window** and allow pop-ups for your Oracle domain.

## 3. Test script (as the test learner)

| # | Do this | Expected | Result |
|---|---|---|---|
| 1 | Launch the course | Navy title screen with the My Clinic logo, Dr. Omar and Noor; a heartbeat line animates in | |
| 2 | Click **Next** to screen 3 | Wristband animation; captions button works | |
| 3 | On screen 5 choose *"Ask him to say his full name…"*, then *"Stop, explain kindly…"* | Feedback after each choice; Noor's avatar shown | |
| 4 | Go to screen 6, open all 8 items on the corridor | Numbered markers sit on each item | |
| 5 | **Close the course window halfway** (on screen 7) | Oracle shows the course **In progress** | |
| 6 | Relaunch | The course **opens on screen 7** (resume) | |
| 7 | Answer every check: screens 8, 9 and 11 | Feedback; drag, sort and choose work with mouse and keyboard | |
| 8 | Finish on screen 13 | Score shown as a percentage, e.g. **"100%"**, and "passed" | |
| 9 | Check the learner record in Oracle | Status **Completed / Passed**, score shown | |
| 10 | Repeat 1–9 on a phone browser | Layout fits the screen; touch works | |
| 11 | Optional: score below 80% on a fresh attempt | Status shows **Failed / not passed**, score shown | |

**What the course sends (SCORM 1.2):** status (`incomplete` → `passed` or `failed`), score 0–100, three topic objectives with their scores, one interaction record per question (answer and right/wrong), time in the course, and a bookmark for resume. Pass mark: 80%.

## 4. Please send back

- The result column above (✔ / ✘ and a note for any ✘).
- Screenshots of the learner record and, if available, the report showing score and objectives.
- Your Oracle Learning release (e.g. 25C), and whether content launches in the same window or a new one.
- Anything you had to change in the launch settings.

Questions: L2S project lead. This sample uses standard safety content (patient identification, fire response, hand hygiene) for testing only; it is not part of the approved induction content.
