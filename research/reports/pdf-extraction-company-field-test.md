---
name: pdf-extraction-company-field-test
id: 20260925T085319Z
tier: report
status: draft
author: Neo
tags: [pdf, ocr, document-processing, skills, provenance, verification]
links:
  - governance/skills/pdf-extraction.md
  - research/insights/pdf-extraction-tools.md
---

# PDF Extraction Skill -- Four-Company Field Test

## Executive Summary

**Is the shared `pdf-extraction` skill usable for investment research? Yes, as a source-checked reading procedure; no, as an unattended financial-data ingestion guarantee.** Neo exercised the installed toolkit on eight official investor-relations PDFs from Prosus, ASML, Nintendo and Citigroup: one annual report and one results presentation per company. The source corpus contains 1,175 PDF pages. Poppler extracted native text from every document; PyMuPDF4LLM converted the four complete presentation decks, preserving all 134 page markers. Selected-page conversion covered another test matrix of 20 requested pages, overlapping the presentation coverage. These are coverage measurements, not 1,175 pages of visually audited financial data.

The basic route is quick and practical. PyMuPDF4LLM retained all 24 deliberately selected numeric anchors on four annual-statement pages in label-matching text. However, Docling also retained those digit strings while combining separate Nintendo yen and dollar amounts into one structured cell. Therefore, even a perfect score on this small numeric-retention probe does not establish correct table semantics. The main protection is already in the skill: verify periods, units, row associations and footnotes against the visible source.

OCR is useful but needs that protection particularly strongly. A four-page, explicitly synthetic scan control was made from rendered company statement pages. OCRmyPDF finished normally but omitted all six checked Nintendo values in shaded rows; the other 18 anchors survived. Additional checks found a corrupted Prosus equity total and Citigroup EPS changing from `7.11` to `711`, outside those anchors. A fresh 300-DPI crop from Nintendo's digital original recovered its six missing values through Tesseract, with page-segmentation mode 6 also restoring row associations. The original PDF did not need OCR. ASML supplied a genuine mixed-content case: readable headings above image-based charts. Neither ordinary extraction nor the tested OCR alternatives completely recovered the chart information.

**Recommendation: keep the lean, alternative-route procedure and make a focused clarification/reproducibility patch, not a new mandatory converter chain.** Correct the output-directory edge case, make HTML-table escalation concrete, extend the JSON warning to picture-contained text, and preserve these failure cases as regression fixtures. Confidence is high in the reproduced observations and moderate in broader applicability. No skill, system package, model, or company research file was changed. Morpheus remains the decision-maker for implementation.

## Research Question

The claim under test was: an agent using the deployed shared skill can retrieve official company PDFs, select an appropriate installed extraction route, identify material extraction failures, and produce page-linked evidence suitable for checked research. A contrary result would include unusable documented commands, unavailable dependencies, missing requested pages, a route that silently loses required content without an effective verification response, or instructions that repeatedly send the agent to nonexistent output files. The task is not to certify the companies' accounts or update their valuations. Financial figures below are extraction fixtures, not investment conclusions.

The scope includes English-language annual reports and earnings presentations, dense numeric tables, multiple reporting periods, currency convenience translations, notes columns, chart labels, footnotes, real mixed native/image content, and deliberately rasterized scan controls. It includes the distinction between a command running, a document being covered, characters being recovered, and financial meaning being preserved. A satisfying answer needs to address each level separately. A successful shell exit alone cannot settle the question, and a readable first page cannot settle whether a later table was actually read.

Out of scope are random-sample accuracy estimation, all-page visual certification, historical photocopies, handwriting, Japanese-language OCR, encrypted or hostile PDFs, systematic skew/rotation testing, long-running production throughput, parallel fleet load, and complete annual-report conversion through every model-based backend. The installed English recognition model was sufficient for this scoped trial. Testing Nintendo's English documents does not establish Japanese OCR readiness. No new dependencies or models were installed, and no remote document-analysis service was introduced.

This is an adoption and field-test extension of Morpheus's active insight `20260925T080023Z`, [PDF Extraction Tools and Shared Skill](../insights/pdf-extraction-tools.md). That insight correctly distinguishes character recovery, document structure and source verification, and explicitly avoids claiming universal accuracy. Its earlier deployment evidence is not replaced or invalidated by this report. The additional question is whether another agent can use the procedure on a varied, real investor-relations corpus and discover where its instructions need refinement. The observed answer should justify either continued supervised use, targeted repair, or a demonstrated blocker. It should not reward unnecessary tool complexity merely because a more elaborate parser exists.

## Methodology

### Corpus and provenance

All downloads and tests occurred on September 25, 2026. Official IR pages were visited to discover or corroborate the documents; download responses were checked for PDF signatures, hashed, and inspected with `pdfinfo`. ASML's official page linked its `ourbrand.asml.com` hosting domain. Nintendo's annual archive was application-rendered; its official PDF was independently located through search rather than pretending that the static archive HTML contained a download link. Citigroup's earnings page exposed PDF links in its page payload. These discovery differences are website issues, not extraction failures.

All page numbers in the test matrix are **physical, 1-based PDF positions**, not assumed printed labels. The Prosus balance sheet at position 140 prints 139; Nintendo's income statement at position 61 prints 59. Source URLs are in Sources; hashes are in Reproduction and Evidence.

| Test document | Source pages | Selected PyMuPDF4LLM pages | Additional principal checks |
|---|---:|---|---|
| Prosus FY2026 annual report [9] | 256 | 140, 141, 144 | Side-by-side balance sheet; Docling page 140; scan control |
| Prosus FY2026 results presentation [10] | 60 | 5, 7 | Full-deck Markdown; chart/year association and footnote |
| ASML FY2025 US GAAP annual report [11] | 350 | 276, 278, 281 | Notes versus amount columns; attached footnote; scan control |
| ASML Q2 2026 presentation [12] | 18 | 8, 14 | Full deck; actual mixed-content charts; OCR alternatives |
| Nintendo FY2026 annual report [13] | 103 | 61, 59, 66 | JPY/USD columns; HTML-table alternative; scan control |
| Nintendo FY2027 Q1 explanatory material [14] | 27 | 3, 7 | Full deck; period definitions, speaker notes, font warnings |
| Citigroup FY2025 annual report [15] | 332 | 146, 148, 152 | Negative values; multi-level headers; scan control |
| Citigroup Q2 2026 presentation [16] | 29 | 4, 18 | Full deck; quarter/YTD columns, segment chart, note references |

### Execution and checks

The installed shared skill was read before route selection. Its SHA-256 was captured and checked again after testing. The existing Brain deployment insight and canonical skill were consulted first; new tests were distinguished from already documented pitfalls. Initial expectations were that native extraction would be quickest, OCR would be needed only for image text, and financial meaning would require visual verification. The actual outputs revised the stronger implicit expectation that a more complex table model would necessarily improve structure.

Native extraction covered each complete source PDF using `pdftotext -layout`. The skill's PyMuPDF4LLM CLI was exercised on all presentation pages with one worker, OCR disabled, headers and footers enabled, and page separators requested. Its Python selected-page API used zero-based inputs converted from the matrix above, `page_chunks=True`, and `use_ocr=False`. Returned `metadata.page_number` was checked rather than assuming response order matched request order: Nintendo's requested 61,59,66 was returned in page order 59,61,66.

Docling used the documented local standard pipeline, CPU device, two threads, batch size one, accurate tables, offline model loading, Markdown and JSON output, and one-page ranges. Four annual pages and ASML chart page 8 were tested without OCR; the chart was also tested with full-page Tesseract OCR. pdfplumber's documented default was exercised on each principal page, followed by text-strategy retries for Nintendo and Citigroup. Original pages were rendered and visually inspected; suspicious details were cropped for higher-resolution examination.

The 24 numeric anchors comprise six on each of four annual-report pages, not checks across all 20 selected pages or all slide decks. The probe joins every line containing a normalized row label, then checks for the expected digit string after whitespace and Markdown normalization. Some matches therefore concatenate multiple lines; this is weaker than a unique cell or even a unique-line assertion. It is a small, purposive retention probe, not a measured general accuracy rate or a year/currency-association validator. Manual inspection separately examined headers, signs, units, multi-column relationships and selected footnotes. OCR controls and intentionally bad calls were labelled as such. Wall time and peak process RSS were recorded for wrapped runs; native timings were separately measured. These are single-run observations, not controlled benchmarks. No source figure was reconstructed by arithmetic to conceal an extraction gap.

## Findings

### F1. The installed procedure works, and the inexpensive routes should stay first

**Observation; confidence high for this corpus.** All eight originals downloaded and yielded native text. Some pages were legitimately text-empty, including covers or graphics; nonzero document text did not establish page completeness. The four full-deck PyMuPDF4LLM runs all recorded `Status: success` and produced the expected uninterrupted page-marker sequence. The selected-page API returned every requested page. No installation or environment activation was needed.

| Document | Whole-source Poppler seconds | Selected-page PyMuPDF4LLM seconds | Whole-deck PyMuPDF4LLM seconds |
|---|---:|---:|---:|
| Prosus annual | 10.21 | 3.98 | Not run |
| Prosus slides | 0.11 | 1.16 | 13.66 |
| ASML annual | 1.63 | 1.75 | Not run |
| ASML slides | 0.04 | 1.26 | 3.71 |
| Nintendo annual | 0.40 | 2.09 | Not run |
| Nintendo slides | 0.07 | 1.72 | 6.26 |
| Citigroup annual | 0.95 | 1.60 | Not run |
| Citigroup slides | 0.08 | 1.22 | 7.39 |

Columns cover different workloads; they are not a like-for-like speed ranking. The annual-report PyMuPDF4LLM samples each contain three pages, and presentation samples contain two. The two PyMuPDF4LLM test phases overlapped in execution, so host contention is another limitation.

Installed versions were Poppler 24.02.0, Tesseract 5.3.4, OCRmyPDF 17.12.1, PyMuPDF/PyMuPDF4LLM/PyMuPDF Layout 1.28.2, pdfplumber 0.11.10, and Docling 2.130.0 with Core 2.98.0. Available Tesseract data were `eng` and `osd`, not Japanese. Nintendo's slides generated Poppler warnings about `Adobe-Japan1` mapping and `YuGothic` despite useful English output. The sampled English figures remained readable; this does not certify every warned glyph or justify silently discarding stderr.

### F2. Digit retention is not table correctness; more complex is not always better

**Observation; confidence high.** Native text, selected-page PyMuPDF4LLM, and Docling Markdown each retained the 24 checked numeric strings in label-matching text. That is token retention on four annual pages, not correct cell assignment even within the sample.

The relevant rows include Prosus treasury-share negatives, ASML revenue and income, and Nintendo sales/operating profit/attributable profit.[9][11][13]

Citigroup's other-revenue anchors were `(504)`, `1,250`, and `2,734` across 2025, 2024, and 2023.[15]

However, Nintendo's ordinary Markdown split the spanning current-year header across its JPY and USD columns. Docling made a materially worse structural mistake: the JSON cell at row offset 6, column offset 4 contains `360,117 2,264`, with `col_span: 1`, while the separate current-yen position is empty. Those are the operating-profit figures in different currencies, not one amount.[13]

On ASML's statement, both Docling and PyMuPDF4LLM contaminated the 2023 revenue field with note references. Docling stored `2, 3 27,558.5`; PyMuPDF4LLM emitted `2, 3<br>27,558.5` in the corresponding Markdown cell. The source has a distinct notes column.[11] This is not exclusively a Docling failure. Choosing JSON instead of Markdown is also not a general cure for incorrect column segmentation.

The existing `table_output=html` recommendation was effective on the Nintendo page. PyMuPDF4LLM emitted a current-fiscal-year header with `colspan="2"`, separate currency subheaders, and separate `360,117` and `2,264` cells. This is a concrete, cheaper fallback before escalating that particular problem to Docling. It is not proof that HTML mode repairs every table.

Docling's four annual-page invocations took 21.03-33.96 seconds, with measured peak RSS of 1.14-1.39 GiB per process. Each started a fresh process/pipeline against a full source PDF with one page selected. These are invocation costs, not steady-state per-page throughput or a basis for linear whole-report estimates. Prosus's two balance-sheet halves were usefully separated. ASML's table footnote was present in JSON `texts`, linked from the table's `footnotes`, but absent from Markdown. These mixed outcomes support selective use rather than either rejecting Docling or treating it as a universal upgrade.

### F3. Actual image charts remain a visual-verification case

**Observation; confidence high for the specific charts, not all charts.** ASML's page 8 contains native headings plus image-based charts. Its visible Q2 end-use chart reads Logic 51% and Memory 49%; the region chart includes Taiwan 30% and China 14%.[12] Native extraction and PyMuPDF4LLM without OCR recovered the headings but not those chart labels. That was an expected route limitation, not a successful chart extraction.

OCRmyPDF `--skip-text --pages 8` correctly skipped the page because it already contained text. Switching to `--redo-ocr` recovered several exterior labels but still omitted the checked interior end-use and region text. Both outputs retained all 18 original pages; `--pages` selected OCR work rather than making a subset. The logs also warned that re-OCRing tagged pages discards structural markup on those pages. Originals must remain untouched.

Docling full-page OCR recovered Logic/51% and Memory/49% as positioned JSON texts, but not the checked Taiwan/30% and China/14% labels. Its Markdown contained only the slide heading and two image placeholders. The skill already warns about JSON-only headers and footnotes; this case extends that warning to text inside picture structures. A reader checking only Markdown would wrongly conclude that OCR recovered none of those words.

Prosus's page-5 chart text survived but its years and series were interleaved in reading order; the Tencent-dividend qualification survived as a footnote.[10] Citigroup's segment chart combined Banking/Wealth labels and their values in a way that still required the source picture.[16] Recovering a list of numbers is not recovering their chart relationships. The skill's render-and-inspect route remains the appropriate final authority for these samples.

### F4. OCR controls show both usefulness and silent loss

**Observation; confidence high for these controls.** Four genuine statement pages were rendered at 200 DPI and embedded, without native text, in `scan-control.pdf`. This is a synthetic rasterization fixture, not a claim that the downloaded company PDFs were scanned. Before OCR its text output was only four page separators. OCRmyPDF's documented `--skip-text` route produced searchable text on every page in 7.01 seconds, without a timeout warning.

Nevertheless, only 18 of the 24 checked anchors survived. All six Nintendo values were absent from the extracted scan text, including the labels and amounts in the visibly shaded sales, operating-profit and attributable-profit rows. Reinspection of the source render confirmed that the rows were visible: this was recognition loss, not missing pixels or an absent original disclosure.[13] The original digital PDF's native extraction had all six figures, reinforcing the instruction not to OCR clean text unnecessarily.

A fresh Nintendo table crop from the digital original, rendered at 300 DPI, was passed directly to Tesseract. Both tested segmentation modes recovered the six numeric strings. Mode 3 separated the labels from the numeric-row block; it did not demonstrate swapped year/currency columns. Mode 6 placed the checked labels and amounts on their corresponding rows. This retry changed crop, resolution and rendering route relative to the initial 200-DPI scan fixture. It therefore demonstrates a working recovery combination, not proof that resolution alone or mode 6 alone caused the improvement, and not recovery from an already degraded historical scan. OCR still damaged some unrelated wording and note markers, so the retry is not an all-cell accuracy certificate.

The reviewer identified further errors outside the selected anchors, which Neo checked against the saved output and source evidence. Prosus's Total equity is `53 867 / 51 125`, but the scan output reads `95 867 / ot 128` (`scan-after.txt:21`).[9] Citigroup's 2025 basic EPS Net income is `7.11`, but the scan output reads `711` (`scan-after.txt:301`).[15] These pages passed their chosen anchors while containing other material errors. The 18/24 result must not be described as an OCR accuracy estimate, and an anchor check cannot certify its entire page.

Tesseract text and TSV output also ran successfully on the Citigroup source render. The TSV supplies coordinates/confidence, not an independent guarantee of correct finance. These tests support the installed fallback capability while rejecting an assumption that a searchable output PDF is necessarily complete.

### F5. The verification warnings are necessary, and one output-path qualification is missing

**Observation; confidence high.** A deliberate OCRmyPDF timeout of 0.001 seconds produced an output PDF and exit code zero while logging `took too long to OCR - skipping`. The requested scan page had no recovered text. A separate overwrite-negative test returned exit code 5 when `--no-overwrite` protected an existing searchable output. These outcomes reproduce and support the skill's timeout and overwrite guidance.

A deliberately invalid PyMuPDF4LLM option, shown below, also returned exit code zero and printed `Batch completed`, while its `run-log.txt` said `Status: error` and no Markdown was produced. The skill already correctly prohibits list-valued CLI page options and directs readers to inspect logs. This is regression evidence for that warning, not a newly discovered undocumented limitation.

```text
--opt 'pages=[0]'
```

The output-path wording needs a narrower correction. The documented `$OUT/report/report.md` layout was reproduced with a generic output directory. But when the output directory's basename already equals the PDF stem, the converter writes `$OUT/report.md` and `$OUT/run-log.txt`. This happened in all four per-company deck runs. The installed `batch_converter.py`, lines 33-43, explicitly avoids double nesting in this condition. An initial interpretation that this affected every single-file conversion was rejected after inspecting the implementation and running a generic-output control. The recommended patch should describe the basename condition, not replace the generally correct path with another universal rule.

### F6. Default table detection and source notes need explicit limits

**Observation; confidence high for sampled pages.** Default pdfplumber table extraction returned no tables for the four selected presentation pages. Its annual-page outputs were also not drop-in financial datasets: Prosus lost useful label/column separation, ASML included a navigation/header table and a one-column financial block, Nintendo fragmented the statement into 17 one-row detections, and Citigroup collapsed rows into one-column strings. Nonempty table arrays are therefore not a success criterion.

The documented text-based strategies produced more structure in Nintendo and Citigroup but still split words or introduced false columns. Targeted cropping/coordinates remain plausible next steps, not tested universal solutions. The report does not recommend making pdfplumber a mandatory intermediate stage.

Footnote references also cross extraction boundaries. Citigroup's presentation explicitly says its notes start at slide 24; extracting slide 4 alone does not resolve those references.[16] The annual statement at position 146 continues on the next page.[15] The full presentation Markdown contains the later notes, but no all-note reconciliation was performed. A material figure needs its referenced note pages, not just a parser's successfully returned table. This requirement is already implicit in the skill's verification gate and deserves one short operational example rather than another large rules section.

## Discussion

The strongest result is the agreement between the field evidence and the existing design principle. The toolkit should remain a set of alternatives chosen for a specific evidence need, not a staircase that every document must climb. For these annual statements, native text and PyMuPDF4LLM were usually enough to read the required figures. For Nintendo's merged date header, the existing HTML-table option was more useful than immediately invoking a heavier model. For ASML's image charts, the decisive evidence was the rendered page, even after OCR and layout analysis had both run. Tool sophistication did not move monotonically with correctness.

There is an important apparent contradiction: Docling passed the small numeric-retention probe while making a currency-column error. There is no actual conflict once the measures are separated. The probe asks whether the characters occur beside a label; it does not prove that a cell has the correct period and unit. A model can preserve every digit while corrupting the relationship that gives the digit meaning. The Nintendo example makes that abstract warning operational, and it is a better regression fixture than a generic statement that tables can sometimes be difficult.

Similarly, OCRmyPDF produced a useful searchable document while failing selected financial rows. That does not invalidate the software or the skill. The procedure explicitly requires content checks and route changes. It does mean that production reuse needs to retain that gate, not silently downgrade it to file-exists or exit-zero checks. The forced timeout and invalid CLI option make this distinction particularly easy to test automatically. Full page-marker coverage has a similar limit: it confirms that pages were represented, not that every picture, note or semantic relationship was recovered.

The prior deployment insight remains active. This report confirms its separation of text, structure and verification, adds an independent user's execution evidence, and supplies company-specific counterexamples. It does not supersede that architecture or justify an installation redesign. Most discovered hazards were already anticipated. The most useful update is consequently small: clarify the directory naming branch, show the successful HTML fallback in context, and mention JSON-only picture text alongside the existing footnote warning.

Further automation should focus on evidence checks, not on inventing a universal financial parser during a skill review. A minimal regression set could retain a few legally usable source-page fixtures and their expected labels, values, units and page references, with failure classified as missing text, broken structure or unresolved context. Whole-company extraction scoring would require a substantially larger labelled corpus. That research is not smuggled into the present verdict. The safe operational conclusion is supervised usability with explicit failure handling, not an unsupported percentage reliability claim.

## Conclusion

The tested shared skill is usable for its intended job: helping an agent read PDFs, choose an appropriate local conversion route, and verify source evidence. Its commands worked on the installed VPS stack. The test covered official material from every requested company, whole-source native extraction, complete presentation conversion, selected annual statements, genuine mixed-content charts, and labelled OCR/failure controls. The observed weaknesses are predominantly the representation and recognition limits that the skill already expects agents to check. They do not justify replacing the toolkit or running every backend on every PDF.

**The single recommendation to Morpheus is to retain the procedure and make a focused clarification patch backed by these fixtures.** First, qualify PyMuPDF4LLM's output-directory rule when the output basename equals the source stem. Second, make the existing HTML-table fallback concrete for spanning year/currency headers, while warning that Docling JSON can still merge unrelated numeric fields. Third, extend the JSON completeness advice to picture-contained text, and use the Nintendo scan and ASML chart as regression examples of unresolved OCR content. Preserve the current requirement to check real output and visible pages, rather than substituting a shell-success check.

No new general governance gate is warranted: the existing PASS/HALT definition already rejects missing rows, ambiguous columns and unsupported completeness claims. The structural improvement proposed here is stronger executable evidence for that gate, with a small instruction correction, not another layer of prose. The shared skill and its canonical Brain copy were left unchanged for the owner's review.

Open work is specific and bounded. Morpheus can decide whether to retain these exact fixtures, add automated log/page checks, investigate the Japanese-font warnings, and test more realistic low-quality historical scans before expanding the reliability claim. Multi-language OCR, full annual-report model conversion, and fleet concurrency remain untested. The next step is review of this report and selective implementation by Morpheus, not an implied production data-certification release. Raw company downloads do not belong in the Brain report directory; only this authored report is intended for publication there.

## Reproduction and Evidence

### Environment and tested skill

- Retained evidence root: `/home/hermes/.local/share/Trash/files/pdf-extraction-review-20260925T083628Z/`.
- Downloads, IR HTML, renders, generated Markdown/JSON, test-only runners and stdout/stderr were moved together from Neo's task scratch into this recoverable hold for Morpheus's review. This is intentionally preserved evidence, outside the scratch idle-pruner, not a new permanent document archive. It remains subject to eventual manual Trash cleanup. Nothing from the downloaded corpus was committed to the Brain. Original scratch paths inside historical logs describe where commands ran.
- Test scripts: `run-tests.py` and `test-ocr.py`. Each wrapped run has `runs/<case>/result.json`, `resources.txt`, `stdout.txt` and `stderr.txt`. Timing starts before subprocess launch and includes startup. **Conversion replay requires a fresh task root** with fresh copies/downloads and runner files: rerunning into the preserved root would overwrite run records while OCR's no-overwrite checks reject existing outputs. This bundle is not an idempotent test suite.
- `score-evidence.py --check` regenerates the narrow retention probes and measured count/timing summaries from saved outputs, compares them with the captured JSON, and performs no writes. Neo exercised it successfully. It does not reproduce historical elapsed wall time, verify table semantics, or replace visual review.
- `state.json` records download URLs, SHA-256, page metadata and source-discovery candidates. `ir-discovery.json` records IR pages and links. `selections.json`, `scan-provenance.json`, `gold-probes.json`, and `numeric-retention-probes.json` describe the bounded checks.
- Shared skill: `/home/hermes/.agents/skills/search/pdf-extraction/SKILL.md`.
- Tested skill SHA-256: `26a3afe6458e78dff1fa4235d6a2c93b08b0d0ad7e5b770293bc31ff7357a9c0`.
- Tests used absolute installed paths from that skill, without activation or package modification. Docling used `HF_HUB_OFFLINE=1 OMP_NUM_THREADS=2`; OCRmyPDF/Tesseract used `OMP_THREAD_LIMIT=2` where documented.

### Source-document hashes

| Local original | SHA-256 |
|---|---|
| `prosus-annual.pdf` | `3ea6278d374118f72fe41ac635d4b622bc1b59be44f5db9c0a7bc321ceabf077` |
| `prosus-slides.pdf` | `ff9f413f797be3dbfd65514c473cc13a88571c6bd113f723238b543738ab14d8` |
| `asml-annual.pdf` | `add58be9d9822ca12584b63c55c089b36e1ae5bf7a1825ebf1d1572628f2c52c` |
| `asml-slides.pdf` | `5b3e05ace2b6d760e16d1ec0b84ca68db68961d4f5ead229516860333e4cdc88` |
| `nintendo-annual.pdf` | `adf1d61bfa20412235535f3689e3a52805e46947214f874377d428ffeb878d16` |
| `nintendo-slides.pdf` | `910e4415437a007b2076df723c203c51a0397d1f84ae8779f588f207bf67d7f2` |
| `citigroup-annual.pdf` | `2eee55ca393cdbedaccabfec0820d253442a76b4c2f1a2eda3221fd721e0d7f7` |
| `citigroup-slides.pdf` | `12a6a29f4de741d65c5a57f74efb88a103928476d5dfcdb119f3056c4a0f4f49` |

### Minimal reproduction examples

The numeric-retention fixture is reproduced below so the check does not depend
on temporary JSON surviving. Values preserve the source's digit grouping;
parentheses are negative signs. Each row also requires its stated period/unit
association when used as data, beyond the mechanical token-presence probe.

| Original / physical page | Row | Periods, left to right | Source values, left to right | Unit |
|---|---|---|---|---|
| Prosus annual / 140 | Non-current assets | 2026; 2025 | 59 607; 50 505 | USD million |
| Prosus annual / 140 | Treasury shares | 2026; 2025 | (6 921); (4 188) | USD million |
| Prosus annual / 140 | Total assets | 2026; 2025 | 79 075; 72 588 | USD million |
| ASML annual / 276 | Total net sales | 2023; 2024; 2025 | 27,558.5; 28,262.9; 32,667.3 | EUR million |
| ASML annual / 276 | Net income | 2023; 2024; 2025 | 7,839.0; 7,571.6; 9,609.4 | EUR million |
| Nintendo annual / 61 | Net sales | FY2025; FY2026 | 1,164,922; 2,313,051 | JPY million |
| Nintendo annual / 61 | Operating profit | FY2025; FY2026 | 282,553; 360,117 | JPY million |
| Nintendo annual / 61 | Profit attributable to owners of parent | FY2025; FY2026 | 278,806; 424,056 | JPY million |
| Citigroup annual / 146 | Total revenues, net of interest expense | 2025; 2024; 2023 | 85,225; 80,722; 78,066 | USD million |
| Citigroup annual / 146 | Other revenue | 2025; 2024; 2023 | (504); 1,250; 2,734 | USD million |

Set `R` to a task-owned directory containing the named originals from Sources. The following commands reproduce the important route choices without requiring the temporary harness. Use fresh output filenames when retrying; keep originals unchanged.

```bash
R="/absolute/path/to/task-evidence"
/usr/bin/pdftotext -layout -f 61 -l 61 "$R/nintendo-annual.pdf" "$R/nintendo-page61.txt"

/opt/document-tools/pdf/bin/python -c '
import json,sys,pymupdf4llm
print(json.dumps(pymupdf4llm.to_markdown(sys.argv[1],pages=[60],
    page_chunks=True,use_ocr=False,table_output="html"),indent=2))
' "$R/nintendo-annual.pdf" > "$R/nintendo-page61-html.json"

OMP_THREAD_LIMIT=2 /opt/document-tools/ocr/bin/ocrmypdf \
  --no-overwrite --redo-ocr --pages 8 --output-type pdf --optimize 0 \
  --jobs 2 --tesseract-timeout 120 -l eng \
  "$R/asml-slides.pdf" "$R/asml-page8-searchable.pdf"
/usr/bin/pdftotext -layout -f 8 -l 8 \
  "$R/asml-page8-searchable.pdf" "$R/asml-page8-searchable.txt"
```

For the scan control, render the four annual pages named in the matrix at 200 DPI and embed each as an image-only PDF page with its original dimensions. Confirm that native extraction contains no text before OCR. For the successful Nintendo retry, render original PDF position 61 at 300 DPI with the PDF-point crop `(40,70,570,780)`, then run Tesseract with `-l eng --psm 6`. Inspect its row associations; do not merely search for the six numbers. For the deliberate timeout control, use a new output path, the image-only fixture, `--pages 1`, and `--tesseract-timeout 0.001`; expect missing OCR despite exit zero. This is a negative test, never a production setting.

For Docling, use the skill's complete standard-pipeline command with `--page-range 61-61 --no-ocr` on Nintendo, and inspect the JSON operating-profit cell as well as Markdown. On ASML page 8, compare `--no-ocr` against `--ocr-mode full_page`, and inspect JSON texts within picture structures. Full captured argument vectors are retained with the evidence bundle. Retrieval and rendering are separate operations; the runners presume that the named downloaded originals and selection manifest have been prepared.

### Independent review

A separate-context, read-only reviewer under `deleg_8fbade5a` returned **APPROVE WITH CORRECTIONS**. It checked source hashes, page counts/markers, selected-page provenance, disputed JSON cells, failure logs and the output-path branch, but did not rerun the complete conversion set. Its material corrections were incorporated: probe scope and weakness, ASML note contamination in both parsers, extra OCR errors outside the anchors, the limited Nintendo recovery claim, invocation-versus-throughput timing, fresh-root replay, and evidence retention. Neo independently checked the two additional source/output discrepancies and exercised the newly retained scoring script.

This is a same-model-family, separate-context evidence review, not a different-model-family evaluation. The review transcript is `/home/hermes/.hermes/profiles/neo/cache/delegation/live/deleg_8fbade5a/task-0.log`; it is runtime-managed evidence, not the only location of the verdict. The report remains `draft` in the formal pipeline pending Morpheus's requested owner review. Test completion and the peer verdict must not be confused with a production certification or approval to modify the shared skill.

## Cross-Links

- [Canonical PDF extraction skill](../../governance/skills/pdf-extraction.md).
- [Morpheus's deployment insight](../insights/pdf-extraction-tools.md), retained as active; this report extends rather than supersedes it.
- [Review provenance and limitations](#independent-review).
- [Report format specification](../../governance/template-reports.md).

## Sources

[9] https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/annual-report/2026/fy2026-annual-report.pdf -- Prosus annual PDF
[10] https://www.prosus.com/~/media/Files/P/prosus-corp-v2/results-reports-and-events-archive/annual-report/2026/fy2026-results-presentation.pdf -- Prosus presentation PDF
[11] https://ourbrand.asml.com/m/71076aaad607de4d/original/asml-2025-annual-report-based-on-us-gaap.pdf -- ASML annual PDF
[12] https://ourbrand.asml.com/asset/9078cf4d-91fd-4dd9-a5d5-d1caab6dc046/2026_07_15_Presentation-Investor-Relations-Q2-2026.pdf -- ASML presentation PDF
[13] http://nintendo.co.jp/ir/pdf/2026/annual2603e.pdf -- Nintendo annual PDF
[14] https://www.nintendo.co.jp/ir/pdf/2026/260806_2e.pdf -- Nintendo presentation PDF
[15] https://www.citigroup.com/rcs/citigpa/storage/public/Annual_Report/2025/citi-2025-annual-report.pdf -- Citigroup annual PDF
[16] https://www.citigroup.com/rcs/citigpa/storage/public/Earnings/Q22026/2026presoqtr2rslt.pdf -- Citigroup presentation PDF
