> **Retired 2026-10-20.** This harness tested the old edumints packages. Use `tools/check_packages.py`, which plays the new packages on a mock SCORM 1.2 LMS.

# Local SCORM API harness

A minimal stand-in LMS for checking what a package sends before it goes to Oracle Learning or SCORM Cloud. `harness.html` exposes both the SCORM 1.2 `API` and the SCORM 2004 `API_1484_11`, logs every call and keeps the CMI data in `sessionStorage` so a relaunch can test resume.

It is evidence that the package speaks SCORM correctly; it is **not** an LMS conformance test. The real gate is the Oracle sample test (`00_sample-oracle-pilot/oracle-learning-test-guide.md`).

```bash
cd /some/empty/dir
cp <repo>/elearning-course/scorm-plans/tools/lms_harness/* .
mkdir s12 s2004
(cd s12   && unzip -q <repo>/elearning-course/scorm-plans/00_sample-oracle-pilot/build/MC_Sample_OracleLearning_1.2.zip)
(cd s2004 && unzip -q <repo>/elearning-course/scorm-plans/00_sample-oracle-pilot/build/MC_Sample_OracleLearning_2004.zip)
python3 -m http.server 8765 --bind 127.0.0.1 &      # must be http: browsers block file:// frames from the parent API
NODE_PATH=$(npm root -g) node resume_test.js 1.2       # answer one question, leave, relaunch → resume check
NODE_PATH=$(npm root -g) node walkthrough_test.js 2004 # visit every screen → final status
NODE_PATH=$(npm root -g) node pass_test.js 1.2        # answer everything correctly → passed, 100%
```

The two scripts are written for the sample (they answer `mcs-023`); change the screen id to test another package.
