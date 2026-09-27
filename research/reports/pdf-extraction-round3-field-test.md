---
name: pdf-extraction-round3-field-test
id: 20260927T133503Z
tier: report
status: final
author: Neo
tags: [pdf, ocr, document-processing, skills, provenance, verification]
links:
  - governance/skills/pdf-extraction.md
  - research/reports/pdf-extraction-company-field-test.md
  - research/reports/pdf-extraction-updated-skill-retest.md
  - research/insights/pdf-extraction-tools.md
---

# PDF Extraction: Third Company Field Test

## Executive Summary

**The latest skill provides useful, demonstrated local repairs on another company set and known failures, but no net OCR accuracy improvement has been established.** Some changed settings fix one row while damaging another. This round tested the precision-focused revision at `92174db48352a5613cfffeb52013be7299e114ba`, not the earlier wording-only update. Its new resolution, segmentation, native-region and coordinate recipes were exercised against actual files and their outputs. The evidence does not support unattended financial ingestion.

The fresh corpus comprises eight official PDFs from Siemens AG, Nestle, HSBC Holdings and Shell. They contain 1,133 source pages; a selected-page matrix covers 20 physical pages, while complete Markdown conversions cover 121 pages across one earnings release and three presentations. These are coverage counts, not correctness scores. Principal financial pages were rendered, selected values and associations checked, and more difficult regions inspected separately. The installed version outputs matched the preceding round.

The clearest trade-off is a controlled replay of the earlier JPMorgan proxy scan. The unchanged OCR command reproduced the previous output byte for byte. Adding only `--oversample 300` recovered Barnum's previously corrupted year, salary and stock-award amount, but introduced wrong salaries for Rohrbaugh and Pinto and a corrupted bonus for Erdoes elsewhere on the same page. Raising that setting to 400 made Barnum's year and salary wrong again. Separately, rendering the digital original at 300 or 400 DPI recovered his checked row; rendering it at 200 DPI reproduced its errors. These are different experiments: better rendering and enlarging an existing scan must not be conflated. The fresh scans also contain lost or malformed HSBC and Shell amounts beyond the headline figures.

The native-coordinate methods also produced useful results. Font-size-aware words separated Rio Tinto's footnotes from amounts that default extraction joined. On a fresh HSBC table, inspected explicit boundaries recovered a defined six-row body, including the outer labels and percentage column. An initial boundary attempt lost those outer columns, illustrating why a cleaner-looking array is not sufficient evidence of repair.

**Confidence is high in the retained, source-checked examples and limited outside them.** Keep the revised skill for supervised research. Prefer digital text, make targeted repairs, and accept only source-checked improvements rather than the largest image or most elaborate parser.

## Research Question

The falsifiable question is whether the newly documented settings and recovery routes can produce more faithful financial content than the previous defaults on defined inputs, while continuing to work on companies not used in either earlier field test. A positive answer requires an actual corrected character, amount, association or schema boundary. A successful command, an existing output file, a larger token count or a plausible financial total does not settle it.

The immediate motivation is Suggi's question about blurriness, recognition and tool quality. The second report, `20260925T102134Z`, distinguished image quality from character recognition and table interpretation but had not tested the proposed precision adjustments. The first report, `20260925T085319Z`, already showed that successful extraction could hide missing rows, note contamination and OCR errors. This round adds experiments; it does not retroactively upgrade either earlier result or replace its historical evidence.

In scope are the deployed skill, the already installed local tools, English-language official corporate PDFs, selected digital statements, presentations, a financial release and synthetic scans. Fresh companies test additional layouts. Earlier JPMorgan and Rio fixtures provide controlled regressions rather than additional independent companies. Within each controlled comparison, the input and other command settings are held fixed while the stated setting changes. Original digital rendering is a separate lane from resampling an already rasterized page.

Out of scope are investment recommendations, valuation, every figure across the full corpus, naturally aged or damaged scans, non-English OCR, remote document services, new model downloads and replacement engines. No claim is made about whether another OCR family would outperform Tesseract, or whether a less informed agent would choose these methods correctly without supervision. Independent review is an evidence check, not an independent-family engine benchmark.

A satisfying answer therefore includes both improvements and regressions, with provenance attached to each. It also distinguishes a repaired local region from a complete reusable financial schema. If a requested row is correct but a header is truncated, the overall extraction remains incomplete until the header is recovered. If a larger image fixes a stock award but corrupts the salary beside it, it cannot be called the better output. Those distinctions determine the recommendation below.

## Methodology

### Pin, sources and scope

The canonical skill and deployed `SKILL.md` matched at retrieval. Their SHA-256 was `a7567b3ac155240c0e9a3c72ff67c7eecba91c6943feb7627511aebbc1ebe067`; the complete snapshot and Git diff are retained. The update adds 300-DPI rendering, bounded comparison with 400 DPI, OCRmyPDF oversampling, region-specific segmentation, native row clips, explicit table boundaries and font-size-aware words. The tools are alternatives, not a mandatory production chain; the broader matrix here deliberately tests their behavior.

All fresh sources were downloaded on **2026-09-27 UTC** from official issuer sites. Download identities, URLs, hashes, byte sizes and `pdfinfo` page counts are in `state.json`. Their hashes are disjoint from both prior corpora. Discovery encountered a 403 for one Nestle HTML route, but the official PDFs downloaded successfully; this was a retrieval distinction, not a parser failure.

| Source | Pages | Selected physical pages | Role |
|---|---:|---|---|
| Siemens AG Report 2025[1] | 335 | 43, 45, 55 | Digital annual report |
| Siemens Q4 FY2025 earnings release[2] | 14 | 9, 8 | Quarter/year statement comparison |
| Nestle 2025 governance, compensation and financial statements[3] | 213 | 82, 86, 81 | Space-grouped amounts and mixed units |
| Nestle FY2025 roadshow presentation[4] | 34 | 32, 22 | Multilevel segment table and margin bridge |
| HSBC Holdings 2025 annual report[5] | 372 | 264, 266, 268 | Dense banking statements and notes |
| HSBC 2025 results presentation[6] | 51 | 26, 12 | Quarterly table, comparison baselines |
| Shell 2025 consolidated financial statements[7] | 92 | 16, 19, 35 | Annual-report section with different printed labels |
| Shell Q4/FY2025 results slides[8] | 22 | 6, 9 | Widely spaced values and picture-text output |

Poppler native extraction covered every source page. PyMuPDF4LLM API chunks covered the selected matrix and were matched by `metadata.page_number`, not request order. Four shorter documents underwent complete CLI conversion, with exact sequential markers and `Status: success` checked. HTML was tried on selected Siemens, Nestle, HSBC and Shell pages. Four principal statement pages underwent Docling standard-pipeline, accurate-table, no-OCR conversion using local models and two CPU threads. Both Markdown and available structured output remain in evidence; this is not an exhaustive audit of every JSON object.

Principal pages were rendered at 300 DPI. The four annual/financial statement pages were also rendered at 400 DPI and read with Tesseract PSM 3. A four-page image-only PDF made from their 300-DPI renders had an empty pre-OCR text layer; OCRmyPDF at `--oversample 300` produced searchable output. Such synthetic scans do not represent all real scanning defects. Visual verification used full-page context and selected crops, not downscaled whole-page images alone.

### Fixed comparisons and reproducibility

The earlier three-page, 200-DPI scan was copied byte-identically. OCRmyPDF used `--no-overwrite --skip-text --output-type pdf --optimize 0 --jobs 2 --tesseract-timeout 120 -l eng`, with either no oversampling argument, `--oversample 300`, or `--oversample 400`. Direct JPMorgan page-69 renders at 200, 300 and 400 DPI were a separate comparison using the same Tesseract PSM 3 settings. A single-row crop compared PSM 3 and 7; Shell's slide compared PSM 3 and 11. Rio's native word comparison changed only the font-size attribute request. HSBC boundary attempts and their diagnostic geometry were retained rather than overwritten.

Version outputs match round two: Poppler 24.02.0, Tesseract 5.3.4, OCRmyPDF 17.12.1, PyMuPDF/PyMuPDF4LLM/layout 1.28.2, pdfplumber 0.11.10 and Docling 2.130.0. The available OCR language data is English plus orientation detection. No software, model or language installation occurred. Version equality is not a claim that every internal model asset was independently compared with its historical counterpart.

`exercise.py` handles the main groups. Follow-ups are fully specified in each `runs/<case>/result.json` by argument vector and environment additions. Replay requires a fresh root and fresh output names; do not overwrite archived evidence. Run `python3 audit-evidence.py` for read-only checks of hashes, coverage, known failures, repaired table cells and version outputs. That audit is deliberately not an overall accuracy score.

## Findings

### 1. The new OCR default repairs one row but introduces errors in other rows

**Claim and confidence: high for the checked row, not for the whole proxy.** JPMorgan's source row for Jeremy Barnum in 2024 shows a salary of `1,000,000` and stock awards of `8,550,000`; source headers, row geometry and image crop distinguish these fields from the adjacent incentive column.[9]

| Same old rasterized scan; only oversampling varies | Year in checked row | Salary | Stock awards |
|---|---|---|---|
| Previous default, replayed | `504` | `4,000,000` | `8,850,000` |
| New default: 300 | `2024` | `1,000,000` | `8,550,000` |
| Comparison: 400 | `5554`, broken layout | `4,000,000` | `8,550,000` |

The previous-default text is byte-identical to round two's `new-scan-after.txt`. The 300 result introduces material numeric regressions, not merely extra punctuation. Source and baseline agree on the correct figures below; the 300-DPI oversampling output does not.[9]

| Other fields on the same page | Source and previous default | New 300-DPI oversampling output |
|---|---|---|
| Troy Rohrbaugh, 2025 salary | `1,000,000` | `4,000,000` |
| Daniel Pinto, 2024 salary | `1,500,000` | `4,500,000` |
| Mary Callahan Erdoes, 2024 bonus | `11,000,000` | Garbage prefix followed by `#1,000,000` |

These failures are retained at `old-scan-300.txt` lines 169, 186 and 166 respectively, alongside the earlier correct cells in `old-scan-default.txt`. The reviewer identified them beyond the initially targeted row; the parent verified both outputs and enlarged source crops. Thus the complete 300 output cannot replace the default wholesale on the strength of Barnum's repaired cells. No exhaustive, cell-level score was defined, so no net improvement is claimed. Whole-fixture durations were 5.171, 6.901 and 8.528 seconds respectively, including the three scanned pages rather than just the one row.

Fresh renders from the digital original produced a different result: 200 DPI reproduced the selected errors, while both 300 and 400 DPI recovered the checked sequence. The 300-DPI line crop returned the same correct sequence with PSM 3 and PSM 7. Thus this crop demonstrates that the new single-line route works, not that mode 7 improves on mode 3. Nor do these tests isolate a single physical cause such as optical blur: they establish effects of particular rendering/oversampling settings in these pipelines.

### 2. Font-size-aware native words separate real footnotes from amounts

**Claim and confidence: high for the inspected Rio production row.** On physical slide 13, the source presents copper production `0.9` with note 2 and aluminium production `3.4` with note 3.[10] Default pdfplumber words returned `0.92` and `3.43`. On the identical page, `extract_words(extra_attrs=["size"])` returned separate amount and marker words. The amount font size was 14.04 points; the markers were 9.36 points.

This is a demonstrated correction to token grouping using native information, not OCR or digit deletion. It supports the skill's added coordinate method. The source's units and note meanings still need reading: separating a marker does not establish which metric or scale an amount belongs to. The raw default and size-aware objects remain in `rio-footnote-words`; no edited source table is substituted for the evidence.

### 3. Explicit boundaries repair a fresh table, with an instructive failed first attempt

**Claim and confidence: high for the defined HSBC six-row body; no full-slide guarantee.** Physical slide 26 contains quarterly financial results from 4Q24 through 4Q25, followed by absolute and percentage comparisons with 4Q24.[6] Default pdfplumber extraction collapsed columns in the tested region. Explicit boundaries initially recovered the six middle numeric columns but silently omitted the outer label and percentage columns.

The recorded diagnostic explains the omission: horizontal text-derived edges spanned x=38.49754 to x=991.081012 points, while the proposed outer vertical boundaries were x=35 and x=995. Matching the outer boundaries to the measured horizontal extents recovered six rows by eight columns, including labels, signs, the dash and `>100%`. The 48 text cells match the source-checked body retained in `semantic-checks.json`. Header and currency were extracted separately. A graphical qualification is NOT recovered in that body: the source's red triangle marks the ordinary-shareholder-profit row as being on a reported FX basis. The source legend must accompany those values.[6] This is a text-body repair, not complete semantic recovery. The coordinates are source-specific, not a reusable preset.

This failure and recovery matter more than a simple pass. A partial table can look cleaner while losing fields. Here, source verification rejected it before publication. The proposed narrow refinement is to check outer-edge intersections and the first and last requested columns when using explicit vertical lines with text-derived horizontal lines. The original, failed and corrected outputs are all preserved.

### 4. Fresh documents still expose structural limits

**Claim and confidence: high for inspected examples; limited to those regions.** Native routes retained useful financial figures, but no fallback was uniformly superior:

- Siemens annual Markdown kept notes separate and retained the checked amounts, including 2025 revenue `78,914` million euros and basic net EPS `12.25` euros, but split the spanning words `Fiscal year`. HTML joined note numbers into labels. Docling restored the words but extended the fiscal-year heading over the Notes column.[1] The release separately requires distinguishing Q4 basic net EPS `2.07` from full-year `12.25`; matching the label alone would be insufficient.[2]
- Nestle annual Markdown retained checked sales `89 490` million CHF and net profit `9 033` million CHF but introduced detached letter fragments in some labels.[3] A native clip recovered `Financial expense`, note 5, `(1 826)` and `(1 843)`. A separate header clip was tightened after its first boundary cut through the adjacent sales label. The final header contains only the intended unit and years. The presentation's quarter groups and RIG/pricing/organic-growth columns remain essential context.[4]
- HSBC presentation HTML recovered the spanning comparison header but retained `<blank>` strings present in native extraction and not visibly displayed in the source rendering. Those are not invented OCR words. A source-measured native body clip avoided the spacer rows without blanket deletion of source text. The lower balance-sheet comparison switches to 3Q25, whereas the upper income comparison uses 4Q24.[6]
- Shell Markdown, HTML and Docling all attached the `$ million` heading to the 2023 column. The source applies the statement's scale to the financial amounts across years, while EPS is explicitly in dollars.[7] Switching parsers did not automatically repair that scope. The presentation's Q4/FY figures appeared in a picture-text fragment rather than a structured table; cash capital expenditure `6.0`/`20.9` and free cash flow `4.2`/`26.1` are billions and are not interchangeable metrics.[8]

The four fresh statement OCR comparisons retained the initially inspected headline figures at both 300 and 400 DPI. Review beyond those anchors found material failures in the new searchable scan. The source values below were verified from the digital pages and enlarged renders; they were not reconstructed arithmetically.[5][7]

| New synthetic scan, OCRmyPDF 300 | Source amount, USD millions | Actual `new-scan-300.txt` output | Line |
|---|---:|---|---:|
| HSBC, 2023 fee income | `15,616` | `on` | 204 |
| Shell, 2024 exploration | `2,411` | `2,All` | 301 |
| Shell, 2025 interest expense | `4,671` | `4,67]` | 304 |
| Shell, 2023 debt-instrument remeasurements | `41` | `Al` | 335 |
| Shell, 2023 cash-flow hedging gains | `71` | `7)` | 337 |

Direct Tesseract at 300 DPI retains HSBC's missing fee-income amount, but the Shell cells remain corrupted in both direct 300- and 400-DPI OCR, with slightly different bracket-like characters in some outputs. The common Tesseract engine does not make wrapper/rendering routes interchangeable. No single physical cause has been isolated.

Note coverage also regresses: Nestle's direct 400-DPI OCR drops note 4 from both other-operating-income and other-operating-expense rows, whereas 300 DPI retains it.[3] HSBC's superscript note marker 9 becomes a question mark, and Shell's `plc` becomes `ple` in a 400-DPI reading.[5][7] Correct headline amounts do not establish correct smaller amounts, note references or the rest of the page. The new scan remains an extraction aid, not verified financial data.

### 5. More elaborate routes did not establish universal superiority

**Claim and confidence: high for the recorded runs.** Shell slide 6 PSM 11 retained the inspected figures but split values and labels into separate text blocks. PSM 3 retained more convenient rowwise text. The sparse mode did not demonstrate a better association schema, and the single-line mode did not outperform the automatic mode on the checked crop. No replacement OCR engine was tested, so none can be ranked from this work.

The four complete conversions produced exactly 121 sequential page markers with successful run logs. That establishes requested page coverage, not complete chart or numeric correctness. Focused Docling invocations took 18.867-28.670 seconds and approximately 1.118-1.261 GiB maximum RSS. These are fresh, single-selected-page processes against full PDFs, not steady-state per-page throughput. All recorded commands exited successfully; known wrong outputs above show why that is not a correctness gate.

## Discussion

The third round changes the answer to a specific question left open by the second. Previously, the evidence supported clearer instructions and unchanged tested outputs. Now the changed settings and native recovery methods have demonstrably corrected selected failures, while the expanded review proves that other cells can regress at the same time. There is no contradiction: the earlier skill revision and this revision are different interventions, and the tests distinguish unchanged defaults from new recipes. Neither report establishes that the underlying engine was upgraded or that aggregate OCR accuracy improved.

The simplest explanatory model remains photographer, reader and bookkeeper. Rendering affects the picture; OCR recognizes characters; layout extraction assigns them to fields. The experiments support choosing a repair at the appropriate layer. Rio's incorrect `0.92` did not require a sharper picture: the source already supplied the amount and smaller marker separately. HSBC's incomplete array did not require stronger OCR: its missing outer fields came from table-edge geometry. The JPMorgan character errors, in contrast, responded to the resolution parameter, although not monotonically.

It would be tempting to conclude that blur caused the proxy errors. The evidence is less specific. Resampling can change character edges and segmentation behavior as well as apparent size. The 400-DPI oversampling regression, alongside successful fresh 400-DPI rendering, shows why original rendering and enlargement cannot be treated as interchangeable. The study identifies a useful setting, not a proven low-level recognition mechanism. It also does not imply that every scanned row improves at 300 DPI.

The fresh company set provides additional layout exposure rather than a population estimate. The selected pages were intentionally chosen to contain useful financial structure, and targeted follow-ups were guided by observed problems. This is appropriate for finding failure modes but unsuitable for estimating error rates or claiming better autonomous agent decisions. Independent evidence review reduces some oversight risk without supplying a blinded study or another OCR engine.

The practical implication is to retain digital text whenever it is usable, escalate locally and preserve associations. A setting must be checked across every affected field that will actually be used, not only the previously wrong target. The initial targeted checks would have understated the 300-DPI regression without the reviewer looking elsewhere on the page. HTML can join notes into labels; a table can lose outside columns or graphical qualifications; sparse OCR can preserve words while weakening order. Financial checks can raise warnings, but source rounding, mixed units and different performance definitions mean arithmetic must not silently rewrite a source value. A guarded escalation procedure is justified; blanket OCR, universally higher DPI and compulsory multi-tool chains are not.

## Conclusion

**The latest skill adds demonstrated recovery options and processes another varied company set, but it is not proven more accurate overall.** The useful change is not a new software installation. It is the combination of explicit resolution comparisons and concrete native-coordinate recovery methods. The fixed scan, native footnote and fresh table experiments show that these additions can repair meaningful errors; the same-page salary regressions and fresh-scan amount failures show why they cannot be accepted without verification.

The single recommendation is to **keep this revision as the supervised extraction procedure, with every affected material field checked before accepting a changed setting**. The inspected JPMorgan row justifies trying the new 300 setting, not accepting its entire output; both the 300 and 400 regressions rule out assuming that more pixels are better. Rio justifies using font and position information before altering digits. HSBC justifies checking the complete requested table boundary and retaining graphical qualifications. These are specific reasons to retain the revised recovery options, not a blanket assurance of correctness.

The remaining questions are concrete. Would these results persist on naturally scanned, skewed, faint or compressed reports? Does another OCR model improve those cases without new financial errors? Can a compact, source-verified regression set detect table-boundary omissions automatically without hardcoding document-specific geometry into a general skill? Can a separate operator choose the correct fallback without knowing the earlier failures? None of those questions is answered by this round.

The report and retained audit provide reusable evidence for further work. No new tools, installed helpers, shared-skill edits or governance changes were made. Table-edge failures, non-target salary regressions and fresh-scan amount failures are retained as explicit audit assertions. A new governance gate is not warranted because the current skill already requires verifying material values, columns and source associations; the test evidence now checks more of those failure dimensions. Further changes should be guided by measured failures, not a larger tool collection. The earlier reports remain valid historical records and are not silently superseded.

### Review and evidence retention

The separate-context evidence reviewer returned **APPROVE WITH CORRECTIONS** in delegation `deleg_3b9f3ba8`. The parent verified and incorporated the additional salary, bonus, fresh-scan amount, note-reference and graphical-qualification findings above. Review covered saved evidence and provisional conclusions; the draft handoff arrived after the reviewer had finished, so this is not an independent review of the final prose or a different-model-family benchmark. The reviewer reported no writes. The complete review transcript and a resolution record are retained with the evidence.

The finished evidence is preserved at `/home/hermes/.local/share/Trash/files/pdf-extraction-round3-20260927T132554Z/`, outside auto-pruned scratch, with recoverable-deletion metadata. File hashes were compared across the move, and the read-only audit and citation checks passed again at the preserved location. It includes sources, hashes, skill/version snapshots, selected text and images, command arguments, raw outputs, unsuccessful settings, `semantic-checks.json`, `review-resolution.json` and `audit-evidence.py`. Command records retain their original scratch paths as provenance; use a fresh namespace when replaying them. A copied ASML control was not exercised in this round; no result is claimed for it. Earlier evidence roots remain read-only. The pre-existing unrelated `scripts/__pycache__/library-publish.cpython-314.pyc` is outside task ownership and is left untouched.

### Fresh source SHA-256 manifest

| Fixture | SHA-256 |
|---|---|
| `siemens-annual` | `a702335f2c2d4f18d3ead4053df2fc3a9be3ad69b062bedd938f3b2551213b27` |
| `siemens-release` | `d126b271af80dc6e8e4078ea147408f18db6a65487ec593a9eb66df04fa60c37` |
| `nestle-financial` | `04f3599884c75233cd9ab888fe139280994129d0ed5489013353b3eb415acad3` |
| `nestle-slides` | `ee15e4f3e11564b1b00634c783403c9c30eb7ab86c4d72bba05cdc1ed6c835c3` |
| `hsbc-annual` | `94aab2f5c83d1060ee95d344f1915833869fe4502dc635e4ab9ca84f496ee94b` |
| `hsbc-slides` | `d10e9eb3ac6978d7bc67888cb90581e752ad644771a5247f85c2340676bda489` |
| `shell-financial` | `a97d13136097d9e8e303d3361c5194ec861cd08ca33f3e4b100a9c6fed5d0e34` |
| `shell-slides` | `93d42b854b97f7003124c0b70a2c66eb1c048d12e7a0f519bd7c4699c5f6fa32` |

## Sources

[1] https://www.siemens.com/applications/b09c49eb-3a14-73b3-9f71-e30e3c2dfdbd/assets/pdfs/en/Siemens_Report_FY2025.pdf - Siemens AG Report 2025
[2] https://assets.new.siemens.com/siemens/assets/api/uuid:3948cdd4-35e0-4c1d-8412-9aed4097b3d0/HQCOPR202511117277EN.pdf - Siemens AG Q4 FY2025 earnings release
[3] https://www.nestle.com/sites/default/files/2026-02/corp-governance-compensation-financial-statements-2025-en.pdf - Nestle 2025 governance compensation and financial statements
[4] https://www.nestle.com/sites/default/files/2026-02/full-year-results-roadshow-presentation-2025.pdf - Nestle full-year 2025 roadshow presentation
[5] https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2025/annual/pdfs/hsbc-holdings-plc/260225-annual-report-and-accounts-2025.pdf?download=1 - HSBC Holdings plc Annual Report and Accounts 2025
[6] https://www.hsbc.com/-/files/hsbc/investors/hsbc-results/2025/annual/pdfs/hsbc-holdings-plc/260225-annual-results-2025-presentation-to-investors-and-analysts.pdf - HSBC Holdings plc Annual Results 2025 presentation
[7] https://www.shell.com/investors/results-and-reporting/annual-report/_jcr_content/root/main/section_2113846431/link_list/links/item4.stream/1773292255440/bc68032ad3986f04e8401c7f1d4d20885e16c950/consolidated-financial-statements-ar25.pdf - Shell 2025 consolidated financial statements
[8] https://www.shell.com/content/experience-fragments/shell/corporate/quarterly/master/_jcr_content/root/tabs/tab_copy/text_copy_copy_94812_1352242202/links/item3.stream/1770256401893/3a6965abe56519e4b795a0087e21a00cc40204a1/q4-2025-slides.pdf - Shell fourth quarter and full year 2025 results slides
[9] https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/proxy-statement2026.pdf - jpmorgan-proxy fixed regression source
[10] https://cdn-rio.dataweavers.io/-/media/content/documents/invest/financial-news-and-performance/results/2025/2025-annual-results-slides.pdf?rev=fb3fded98fe74c3e928b2744b0f2fcec - rio-slides fixed regression source
