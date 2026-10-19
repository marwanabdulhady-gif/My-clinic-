# Manifest XSD validation — all eight draft packages

> **2026-10-19:** 01 and 03 are now SCORM 1.2 (Oracle Learning target). Their 2004 results below are kept as the record; rerun the XSD check on the 1.2 builds with `SCORM_SCHEMA_DIR` (schema hosts are blocked in the cloud workspace).

![My Clinic logo](brand/logo-preview.png)

> Run **2026-10-15** against the committed `v0.1-draft` sources with the real compiler
> (`edumints-scorm-mcp` @ `4bbf459`, the revision pinned in [`build-pipeline.md`](build-pipeline.md) §6).
> This is the first half of **C22 / G15**: the `imsmanifest.xml` schema check. XSD validity is a
> **supporting** check — the gating proof of SCORM conformance is a SCORM Cloud round-trip and a real
> LMS (edumints `docs/CONFORMANCE.md`), which is still open.

## 1. Result

`validate_package` now runs the real XSD validation: the `schema_unavailable` warning that the
committed build reports carry is gone, and every package validates with **0 errors, 0 warnings**.

| Module | SCORM | `validate_package` | errors | warnings | `lint_course` errors | Package bytes |
|---|---|---|---|---:|---:|---:|---:|
| 01 | 2004 | ok | 0 | 0 | 0 | 2,367,661 |
| 02 | 1.2 | ok | 0 | 0 | 0 | 3,322,813 |
| 03 | 2004 | ok | 0 | 0 | 0 | 1,214,576 |
| 04 | 1.2 | ok | 0 | 0 | 0 | 2,513,779 |
| 05 | 1.2 | ok | 0 | 0 | 0 | 510,218 |
| 06 | 1.2 | ok | 0 | 0 | 0 | 701,178 |
| 07 | 1.2 | ok | 0 | 0 | 0 | 805,664 |
| 08 | 1.2 | ok | 0 | 0 | 0 | 699,025 |

Both SCORM versions are covered: the two 2004 packages (01, 03) and the six 1.2 packages. The rebuilt
zips differ from the committed ones only in the fresh project id inside `imsmanifest.xml` and the zip
entry timestamps — `index.html`, the runtime, the companion art and `preview.html` are byte-identical,
so the committed drafts still match their sources.

## 2. How the schemas were supplied

`validate_package` fetches the IMS/W3C schemas from `imsglobal.org` / `w3.org` on first use (only the
ADL files are vendored), which this build sandbox cannot reach. Setting **`SCORM_SCHEMA_DIR`** switches
the compiler to a fully offline schema directory with `12/` and `2004/` sub-directories and no network
access at all:

```bash
# <dir>/12/ and <dir>/2004/, each holding: driver_<ver>.xsd + adl/*.xsd (copied from the edumints
# checkout) + the IMS/W3C files, with absolute xml.xsd imports rewritten to the local xml.xsd
SCORM_SCHEMA_DIR=/path/to/scorm-schemas \
EDUMINTS_DIR=/path/to/edumints-scorm-mcp \
  .venv/bin/python elearning-course/scorm-plans/tools/edumints_build.py 01_health-and-safety-1
```

## 3. Schema provenance

Schema **files are not committed** (IMS/W3C licensing; see `.gitignore` and the compiler's own
policy). [`xsd-schema-provenance.json`](xsd-schema-provenance.json) records what was used: every file
with its source, byte count, sha256, and the sha256 the compiler expects.

- **17 files** (13 for 2004, 4 for 1.2) were taken from public mirrors and **16 of them are
  sha256-identical** to `runtime/schemas/ims_sources.json` — i.e. byte-for-byte the files the compiler
  fetches from IMS/W3C.
- **1 substitution:** the SCORM 1.2 Content-Packaging root schema (`imscp_rootv1p1p2.xsd`). No
  hash-exact mirror exists on GitHub among ~1,000 indexed copies, and `imsglobal.org` is unreachable
  here. The substitute is the same IMS CP 1.1.2 schema (the XML Spy revision, 14,905 bytes vs the
  13,601-byte file the compiler expects), it compiles cleanly with libxml2, and all four 1.2 manifests
  validate against it with 0 errors. **Re-run this check with the real file before a release build.**
- The ADL schemas (`adlcp`, `adlseq`, `adlnav`, plus the two driver XSDs) are copied byte-for-byte
  from the compiler checkout.

Caveat kept from the compiler's own notes: the SCORM 1.2 *1.2.1* LOM binding (`imsmd_rootv1p2p1.xsd`)
cannot be compiled by libxml2 (UPA violation) and is deliberately **not** used — both drivers bind the
1.2.4 LOM schema instead.

## 4. What this does and does not prove

| Proves | Does not prove |
|---|---|
| Every generated `imsmanifest.xml` is valid against the official SCORM 2004 / 1.2 schemas | That a real LMS imports, launches, resumes and scores the package |
| The manifest namespaces, resource/file references and sequencing metadata are structurally correct | Completion, pass/fail, `cmi.*` reporting or objective roll-up |
| The same compiler revision (`4bbf459`) that produced the drafts produces schema-valid output | Anything about the still-open Phase 0 decisions shown as `⚠ Draft — pending` |

Still open in C22: **SCORM Cloud smoke test** (import 1.2 and 2004, launch, resume, score, complete)
and a **release-build re-run** of this check with the authentic 1.2 root schema and XSD access.
