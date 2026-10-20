# Oracle Learning compatibility

![My Clinic logo](brand/logo-preview.png)

> Prepared **2026-10-19**. My Clinic runs **Oracle Applications Cloud** (the HR deck's self-service screens are Oracle Fusion: sign-in, *Time and Absences*, *Add Leaves*). The induction courses will therefore most likely be hosted in **Oracle Learning** (Fusion HCM). This file records what Oracle Learning accepts, what our packages send, the evidence we have, and the test My Clinic's LMS team runs with the sample package. Decision **D9** stays open until that test is done.

> **Update 2026-10-20: own player.** All nine packages now use our own SCORM 1.2 player (`tools/player/`), which replaces the edumints compiler and the scorm-again runtime. The zip root holds `imsmanifest.xml`, `index.html`, `course.js`, `player.js`, `player.css` and `assets/`. What it reports is in [`../tools/player/README.md`](../tools/player/README.md#what-oracle-receives-scorm-12). `tools/check_packages.py` plays every package on a mock SCORM 1.2 LMS:
> - all correct → `passed` 100 (07: 95, because `qsr-032` waits for B6);
> - all wrong → `failed`;
> - closed after 6 screens → relaunch on the same screen.
>
> This does **not** replace the real Oracle test (§4), which still closes D9. Rows below that mention edumints describe the old builds. The percent-format patch (G18) is no longer needed, because the player writes "75%".

## 1. What Oracle Learning accepts (published sources)

| Requirement | Oracle Learning | Our packages |
|---|---|---|
| Standard | SCORM **1.2** and SCORM **2004 Editions 2 and 3** (also AICC, HACP). 4th Edition is not in the documented list. | **SCORM 1.2 for all eight** (changed 2026-10-19; 01 and 03 were 2004 4th Ed.). 2004 build kept as an optional test. |
| Packaging | One `.zip`; `imsmanifest.xml` at the **root** of the zip (not in a sub-folder) | ✅ `imsmanifest.xml`, `index.html`, `runtime/`, `assets/` at the zip root |
| Size | 1 GB maximum | ✅ 0.5–3.3 MB per package (no audio yet; with narration still well under 50 MB) |
| Names | No spaces in the structure name | ✅ `MC_<NN>_<short>_v…_1.2.zip`, ids without spaces |
| Known community reports | 2004 4th Ed. package reported completion but success status "unknown"; blank page on launch; items stuck "processing" after upload | Avoided by using 1.2; launch and processing are covered in the sample test (§4) |

Sources: Oracle Fusion Talent Management documentation, *Add online content to your Oracle Learning resources* (24A) and *Managing the catalog resources* (20B); My Oracle Support Doc ID 2500837.1 *Supported SCORM and AICC standards*; Oracle Cloud Customer Connect thread *SCORM 2004 completion status vs success status (unknown) in Oracle Learning*. Oracle's sites were not reachable from the build workspace, so these were read through search results; **ask My Clinic IT to confirm the pod release and Doc ID 2500837.1** before release.

## 2. Why SCORM 1.2 for all eight

- **Documented support.** Every Oracle Learning release supports 1.2. The edumints compiler writes 2004 as **4th Edition**, which Oracle does not list.
- **The 1.2 size limit is not a risk.** SCORM 1.2 caps resume data (`cmi.suspend_data`) at 4,096 characters. The compiler's worst-case estimate for our largest module (01, 54 screens) is **749 bytes**; 03 is 373, 02 is 341, the sample 182. That was the only reason 01 and 03 were 2004.
- **What 1.2 reports to Oracle:** `cmi.core.lesson_status` (incomplete → passed/failed), `cmi.core.score.raw/min/max`, `cmi.objectives.n` (id, status, score), `cmi.interactions.n` (id, type, learner response, result, weighting, latency), `cmi.core.exit = suspend`, `cmi.suspend_data` and session time. Pass mark is in the manifest as `adlcp:masteryscore`.
- **What we lose vs 2004:** a separate `success_status` and scaled scores. Oracle shows passed/failed from `lesson_status`, so reporting is unchanged for My Clinic.

## 3. Evidence so far

| Check | Result | Where |
|---|---|---|
| Manifest XSD (official SCORM 1.2 / 2004 schemas) | 0 errors on all eight drafts (2026-10-15, same compiler) | [`xsd-validation.md`](xsd-validation.md) |
| `validate_package` structural | ok — all eight + sample, 1.2 and 2004 | each `build/build-report.json` |
| SCORM API round-trip (test LMS harness) | **1.2:** `LMSInitialize` → status `incomplete` → objectives registered → interaction `mcs-023` recorded (choice, correct, weighting 10) → score 17 → `exit=suspend` → **relaunch resumes on the same screen** (`cmi.core.entry=resume`). **2004:** same, plus `success_status=failed`, `score.scaled=0.17`. | [`../00_sample-oracle-pilot/build/lms-harness-results.json`](../00_sample-oracle-pilot/build/lms-harness-results.json), `tools/lms_harness/` |
| Real Oracle Learning launch | **Not yet** — needs My Clinic's Oracle tenant | §4 |

The harness proves the packages talk SCORM correctly. It does not prove Oracle's own behaviour (pop-up/launch window, how its reports map statuses). Only the sample test in My Clinic's Oracle tenant closes D9.

## 4. The sample test (send to My Clinic's LMS administrator)

Package: [`00_sample-oracle-pilot/build/MC_Sample_OracleLearning_1.2.zip`](../00_sample-oracle-pilot/build/MC_Sample_OracleLearning_1.2.zip) (8 minutes, 13 screens, 4 scored checks). Step-by-step guide and result sheet: [`../00_sample-oracle-pilot/oracle-learning-test-guide.md`](../00_sample-oracle-pilot/oracle-learning-test-guide.md).

## 5. Player fixes applied at build time (edumints 4bbf459)

| Issue | Effect | Workaround here | Upstream |
|---|---|---|---|
| Explore hotspots never positioned (G12) | All markers stack in one corner | CSS positions written by `build_course_spec.py` | Fix `bindHotspot` |
| Percent shown Turkish-style, e.g. "%75" (G18) | Score on the summary and results screens | `edumints_build.py` patches the two lines in each package's player (`player_patches: 2` in every report) | Format by language |
