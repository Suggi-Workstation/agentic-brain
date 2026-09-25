---
name: pdf-extraction-updated-skill-retest
id: 20260925T102134Z
tier: report
status: draft
author: Neo
tags: [pdf, ocr, document-processing, skills, provenance, verification]
links:
  - governance/skills/pdf-extraction.md
  - research/reports/pdf-extraction-company-field-test.md
  - research/insights/pdf-extraction-tools.md
---

# Updated PDF Extraction Skill -- Fresh-Corpus Retest

## Executive Summary

**Does the updated skill work better? Its instructions are clearer and address the tested operational gaps; this is not a measured improvement in agent reliability or recognition accuracy.** Neo tested the revised shared skill on eight different official PDFs from Berkshire Hathaway, Toyota, Rio Tinto and JPMorgan Chase. The new originals contain 849 pages. Native extraction covered each document, selected-page checks covered a final matrix of 20 pages, and four complete conversions retained 141 sequential page markers. These are extraction-coverage measurements, not a certification of every financial cell. The corpus includes a historical annual report, modern statements, presentation tables and charts, and executive-compensation disclosures.

The revision addresses the first report's actionable instruction gaps. Its output-directory qualification matched both tested directory layouts. Page-number metadata correctly handled reordered API results. The explicit HTML fallback was useful for Berkshire's fragmented Markdown table, while the stronger directions on units, notes and JSON identify necessary checks beyond recovering readable numbers. Toyota and JPMorgan supplied important counterexamples: HTML did not repair every spanning header, and a footnote number still migrated into a compensation-total cell. Those limitations are consistent with the revised verification gate, not evidence that the patch was absent.

A separate fixed-control lane reused hash-identical first-run fixtures. Nintendo's default Markdown text, the four-page scan's extracted OCR text, and the successful cropped Nintendo OCR text were unchanged. The old currency-cell merge, partial chart recovery and exit-zero failure cases were reproduced. The installed tool versions also matched. Consequently, neither better accuracy nor faster engines can be attributed to the prose update.

**Recommendation: retain the updated skill for supervised research and preserve these cases as regression evidence; do not add a mandatory conversion chain.** Confidence is high in the observed command and output comparisons, moderate in general usability, and insufficient for a numerical reliability estimate. The same informed operator conducted both rounds; this was not a blinded agent A/B experiment. The shared skill, system packages and company research files were not modified.

## Research Question

The primary question is whether the updated procedure makes its intended task easier to perform correctly: retrieve a public company PDF, choose an appropriate available route, recover the required content, and recognize when the output is incomplete or structurally misleading. A falsifying result would include corrected instructions still pointing to the wrong output location, a documented fallback not running, missing requested pages being accepted as complete, or the procedure encouraging unverified financial use. The narrower recognition question is separate: did the same tools produce different or more correct output on identical inputs? Keeping these questions apart is necessary to answer Suggi's request without mistaking a documentation improvement for a model upgrade.

The baseline is [the first field-test report](pdf-extraction-company-field-test.md), ID `20260925T085319Z`. It tested Prosus, ASML, Nintendo and Citigroup and recommended focused instruction changes rather than a replacement toolkit. Morpheus subsequently committed the canonical update as `39d5c69ed865cb063cdffd1502dd8f72fdaa3356`. The present report extends the historical evidence; it does not replace the first run or revise its measurements. Its fresh documents deliberately come from different companies and include different disclosure formats. A second, explicitly labelled control lane repeats earlier failure cases so that changed document difficulty cannot explain away every result.

In scope are English-language financial statements and presentations, a proxy's compensation table, signs and decimals, differing period orders, multiple monetary scales, per-share units, footnotes, cross-page references, native-text layout failures, and synthetic scan OCR. Both command execution and actual generated content are examined. Out of scope are company valuation, exhaustive all-cell auditing, representative statistical accuracy, non-English OCR, handwriting, damaged historical photocopies, encryption, adversarial PDFs, fleet concurrency and production throughput. The older Berkshire PDF supplies a historical disclosure layout, not evidence about poor-quality scans.

A satisfactory outcome must identify what improved, what did not, and how the agent should respond to unresolved content. Successful conversion must remain distinct from correct financial interpretation. New documents broaden the evidence base, but cannot by themselves establish superiority over the old procedure. The test is useful even if its strongest result is unchanged raw output alongside better instructions for detecting and handling its limitations.

## Methodology

### Revision, environment and acquisition

Testing and retrieval occurred on September 25, 2026. The deployed skill was read before route selection and matched the canonical Brain file byte-for-byte. Its SHA-256 is `fd416844bf9d4e8417cf4ddd37a5613d425d030bb187fe5e5aaba3cd6cbdf4f4`; the first-run snapshot was `26a3afe6458e78dff1fa4235d6a2c93b08b0d0ad7e5b770293bc31ff7357a9c0`. The Git diff changes guidance, not the installed extraction executables. Version checks matched the baseline: Poppler 24.02.0, Tesseract 5.3.4, OCRmyPDF 17.12.1, PyMuPDF/PyMuPDF4LLM/Layout 1.28.2, pdfplumber 0.11.10, and Docling 2.130.0/Core 2.98.0. Tesseract still lists only `eng` and `osd`.

Official IR pages supplied the links. Rio's official results page linked its `cdn-rio.dataweavers.io` downloads. Unilever and Allianz were initial candidates, but their PDF endpoints returned HTTP 403, so no extraction result is claimed for them. Microsoft's annual download page offered Word documents rather than the desired annual PDF; it was not converted and relabelled as an original PDF. A mistaken Toyota IR path returned 404 before the correct page was found. An initial Berkshire HTML fetch was improperly decoded; HTTP-aware decompression recovered its links. A task helper also tried an unavailable `requests` import, then used installed curl without installing anything. These are acquisition/instrumentation issues, not failures of the PDF converters.

### Corpus and sampling

All page references below are physical, 1-based PDF positions. Source hashes establish that none of the eight originals duplicates the first corpus. Titles and sampled content were checked after download; PDF signatures and `pdfinfo` were verified before extraction.

| Document | Pages | Final selected-page matrix | Main challenge |
|---|---:|---|---|
| Berkshire 2025 annual report [4] | 154 | 94, 96, 92 | Fragmented text, shaded rows, share-class footnote |
| Berkshire 2002 annual report [5] | 78 | 29, 30 | Dotted leaders, historical share basis |
| Toyota FY2026 financial summary [6] | 31 | 13, 16, 2 | Spanning unit header; millions versus EPS yen |
| Toyota FY2026 results slides [7] | 32 | 6, 7 | Billions, qualifications and waterfall chart |
| Rio Tinto 2025 results release [8] | 48 | 27, 1, 44 | Cents versus dollars; cross-page APM definition |
| Rio Tinto 2025 results slides [9] | 30 | 13, 27 | Commodity columns, notes, negatives and percentages |
| JPMorgan 2025 annual report [10] | 364 | 197, 201, 254 | Signed bank income; million-dollar versus EPS units |
| JPMorgan 2026 proxy statement [11] | 112 | 69, 70 | Repeated names, note markers, compensation definitions |

The initial Rio page 26 was a contents page, not its income statement. Inspection caught the selection mistake, and page 27 was separately processed without overwriting the first result. Following the proxy's reference added page 62. Thus the final matrix contains 20 pages, while the complete API evidence covers 22 distinct source pages including the mistaken TOC and follow-up. The principal page from each original was visually inspected, with additional checks of Toyota's waterfall and the Rio/JPMorgan note pages. This is not an all-page visual review.

### Execution and comparison

Poppler `pdftotext -layout` processed all originals. PyMuPDF4LLM used the skill's selected-page API with `page_chunks=True` and `use_ocr=False`; returned chunks were mapped by `metadata.page_number`. Four pages also used `table_output="html"`. Whole-document CLI conversion covered both Toyota and both Rio documents with one worker, OCR disabled, headers/footers and page separators enabled. Logs and sequential markers were checked. Docling used the local offline standard pipeline, CPU, two threads, accurate tables, Markdown plus JSON, and one-page ranges. Additional cases addressed the corrected Rio statement and its presentation table. Default pdfplumber was exercised on four selected pages as a diagnostic, not as a required stage.

The fixed controls copied original PDFs, the original synthetic scan and the original successful Nintendo crop without changing their bytes. A fresh three-page scan control used 200-DPI renders of the new Berkshire, Toyota and JPMorgan principal pages. These are deliberately rasterized controls, not naturally scanned company originals. Scripts retain argument vectors, stdout, stderr, elapsed times and process RSS. The read-only audit script regenerates counts, hash checks and exact baseline comparisons. Manual semantic findings are separately recorded: no token-retention percentage is presented as financial correctness.

## Findings

### F1. The procedure's revised instructions are operationally useful

**Observation; high confidence for the exercised changes.** Both documented PyMuPDF4LLM output layouts were reproduced: a generic output directory creates a source-stem subdirectory, while an output directory already named after that stem avoids double nesting. Success logs were beside the outputs as described. The intentionally invalid list-valued CLI option still exited zero while recording `Status: error` and producing no Markdown. Requiring log success and requested content therefore rejects an actual misleading shell result, not a hypothetical one.

The reordered-page warning also mattered in the fresh corpus. Berkshire's requested 94,96,92 returned 92,94,96, and Toyota's 13,16,2 returned 2,13,16. Mapping by metadata preserved the association between a source page and its output. The original Nintendo control similarly returned 59,61,66 despite a 61,59,66 request. None of these results means that a page was lost; positional pairing would be the error.

| Revised guidance | Retest result | Limit |
|---|---|---|
| Qualify the output-directory basename rule | Both layouts located as documented | Does not assess content |
| Require log success and requested content | Rejected reproduced exit-zero conversion error | A success log alone still proves too little |
| Match API chunks by page metadata | Correctly handled old and new reordered requests | Does not validate table cells |
| Make HTML-table fallback explicit | Improved Berkshire table readability; retained Nintendo's demonstrated span | Did not fix Toyota's unit span or JPMorgan's migrated note |
| Retry missed OCR regions using best-source crop | Reproduced Nintendo's successful saved-crop output | The first run had already achieved this recovery |
| Follow JSON picture text and notes, then check the source | Recovered ASML JSON-only text and checked new financial definitions | Picture words are not complete chart data |

These are verified examples of instruction applicability. They are not a measured reduction in the error rate of previously untrained agents.

### F2. New tables confirm that fallback quality depends on the document

**Observation; high confidence on sampled rows.** Berkshire's 2025 source rendering is legible, but default Markdown fragments words and digits with repeated `<br>` breaks. Its HTML output restores useful strings such as total revenues `371,444`, although some stray characters remain. Docling produces the cleaner sampled table, retaining 2025 attributable earnings `66,968` million dollars and Class B EPS `31.04` dollars. This is a practical case for changing representation before, or selectively using, the heavier parser.[4]

The historical Berkshire page is comparatively straightforward. Native text and Markdown preserve sampled earnings and the footnote that defines the historical Class B basis as one-thirtieth of the Class A amount. That differs from the modern page's one-fifteen-hundredth wording. The document date and share basis must travel with the number; the older file's selectable text does not make it a natural scan benchmark.[5][4]

Toyota's statement provides the counterexample to treating HTML as a repair guarantee. Ordinary Markdown divides `Yen in millions` across columns, and HTML still emits separate `Yen in` and `millions` header cells rather than a spanning cell. Docling combines that heading with the two fiscal-year headers. All three routes still require the reader to respect the separate `Yen` row above EPS: `295.25` is not a million-yen amount. The sampled operating-income figure is `3,766,216` million yen in the statement but `3,766.2` billion yen in the presentation.[6][7]

JPMorgan's annual statement preserved sampled signs and periods, including investment securities losses `(57)` million dollars, total net revenue `182,447` million dollars and diluted EPS `20.02` dollars for 2025. That readable result supports the simple route on this page; it does not certify the entire annual report.[10]

### F3. A proxy exposes both extraction and interpretation hazards

**Observation; high confidence.** On physical proxy page 69, printed page 63, James Dimon's 2025 Summary Compensation Table total is `$40,632,724`. Footnote 6 attaches to his `$1,587,852` of all-other compensation. PyMuPDF4LLM instead emits `6 $40,632,724` in the total cell, in both Markdown and HTML. Docling leaves the total clean but creates an extra column for the note markers, with `5` from the header and `6` in that row. Neither output is a ready-to-use compensation schema.[11]

The page also explicitly refers to a different compensation table on printed page 56. Following that reference to physical page 62 gives `$43,000,000` for 2025 performance-year annual compensation, including `$36,500,000` of PSUs. The proxy explains that the performance-year table associates equity awards granted in the following year with that performance year, whereas the SEC table reports equity awards in the grant year and includes additional compensation components. The SCT mixes timing conventions: its 2025 equity awards reflect 2024 performance, but footnote 2 says cash incentives reflect the performance year shown and are awarded the following January. The entire SCT total must not be labelled prior-performance compensation. These are different definitions, not an arithmetic disagreement to repair.[11]

The updated source-and-notes instruction handles both hazards if followed literally: isolate the note marker, then identify which definition the requested figure requires. Merely recovering both numeric strings would leave the research question unresolved. This is a stronger test than checking whether a compensation number appears somewhere in the document.

### F4. Native text and JSON still do not guarantee complete tables or charts

**Observation; high confidence for the chosen pages.** Rio's slide 13 contains readable native characters and a multi-commodity table. PyMuPDF4LLM emits numerous picture-text fragments; switching its output to HTML does not construct the table. Docling extracts an Aluminium table but leaves much of Iron Ore, Copper and Lithium as linear text. The source picture is needed to bind Copper EBITDA `7.4` billion dollars to `114%` growth, and Lithium free cash flow `(1.5)` billion dollars to its correct column. The source's production, percentage and monetary units differ within the display.[9]

The first-run ASML control remains incomplete too. Docling's full-page OCR retains `Logic`, `51%`, `Memory` and `49%` inside JSON picture structures while its Markdown contains only the heading and image placeholders. The checked Taiwan/China label-value pairs are not completely recovered. The stronger JSON guidance makes those recoveries discoverable; it does not convert them into a complete chart.

Following Rio's page-1 APM reference to page 44 worked better as a research task than stopping at its headline table. Its disclosed free cash flow is `4,025` million dollars, with operating cash `16,832`, capex `(12,335)`, lease principal `(522)` and asset-sale proceeds `50`. Its definition explicitly includes the latter two items. The statement's EPS also carries cents, not a bare dollar amount. These context checks are useful even when the underlying digit extraction is correct.[8]

Default pdfplumber did not remove these concerns. Toyota returned no detected tables; JPMorgan's proxy output contained only a header row rather than its compensation grid. Rio's detected cells were not a complete commodity table and merged superscript note digits into production amounts: `0.9` with note 2 became `0.92`, while `3.4` with note 3 became `3.43`.[9] These are plausible-looking but incorrect numeric cells. Berkshire returned a large array, which was not treated as proof of usable structure. No general table correctness claim follows from nonempty arrays.

### F5. Fixed controls show unchanged recognition; fresh OCR adds breadth, not a win rate

**Observation; high confidence.** The following comparisons used newly executed commands and untouched first-run evidence, not only the previous report's narrative.

| Fixed input or failure case | New execution compared with first run |
|---|---|
| Nintendo selected-page default Markdown | Page texts identical |
| Four-page synthetic scan through OCRmyPDF/Poppler | Extracted text byte-identical, including the prior omitted rows and errors |
| Successful 300-DPI Nintendo crop through Tesseract PSM 6 | Text byte-identical |
| Nintendo Docling operating-profit cell | Still combines `360,117 2,264` into one currency cell |
| Nintendo HTML span | Demonstrated `colspan="2"` recovery remains available |
| ASML picture text | JSON-only partial recovery remains incomplete |
| Deliberately invalid CLI page list | Exit zero, log error, no usable Markdown |
| Deliberate OCR timeout | Exit zero, logged skip, no recovered text |

The fresh three-page synthetic scan became searchable without a timeout warning. Checked Berkshire EPS and earnings, Toyota operating income and EPS, and Dimon's compensation total survived. But JPMorgan's footnote `6` became a copyright symbol, and the independent reviewer found more serious errors outside those headline checks. Neo verified the original Barnum row in the rendered source and the corruption in `new-scan-after.txt:180`.[4][6][11]

| Jeremy Barnum SCT field | Original proxy page 69 | Synthetic-scan OCR |
|---|---|---|
| Year | `2024` | `504` |
| Salary, USD | `1,000,000` | `4,000,000` |
| Stock awards, USD | `8,550,000` | `8,850,000` |

The native Markdown and Docling outputs retain these source values. The scan has a real recognition error, not merely a different table representation.[11] This is not an exhaustive all-cell inspection, and the original PDF did not need OCR. A seemingly better selected-row result on these new pages cannot be compared numerically with the first run's 24-token probe. The unchanged old scan output establishes persistence of the tested behavior, not universal engine equivalence or correctness on unseen inputs.

### F6. Coverage is good; timing is only a bounded execution observation

**Observation; high confidence in measured counts, limited comparative meaning.** All eight originals yielded native text; each native output's page-break count matched `pdfinfo`. The four whole conversions recorded success and sequential markers covering 141 pages. The final selected-page matrix was present. These checks establish processing coverage, not complete text or correct figure relationships.

| Document | Whole-source Poppler seconds | Final selected API seconds | Whole-document CLI seconds |
|---|---:|---:|---:|
| Berkshire 2025 | 2.966 | 1.694 | Not run |
| Berkshire 2002 | 0.113 | 1.124 | Not run |
| Toyota summary | 0.118 | 1.331 | 12.038 |
| Toyota slides | 0.044 | 1.048 | 5.684 |
| Rio release | 0.096 | 1.560 | 10.112 |
| Rio slides | 0.064 | 1.289 | 7.739 |
| JPMorgan annual | 0.855 | 1.210 | Not run |
| JPMorgan proxy | 0.260 | 1.134 | Not run |

These columns do different work. Independent groups overlapped, and host load was not controlled. The meaningful new Docling statement/table invocations ranged from 11.461 to 19.887 seconds and 1.102 to 1.196 GiB maximum RSS; the accidentally selected TOC is excluded from that range. Each invocation loads a pipeline against a full source with one page requested. This is neither steady-state per-page throughput nor evidence that the skill update accelerated the engines.

## Discussion

The most important distinction is between a better operating procedure and a better recognizer. A written instruction can make an agent locate the right file, notice that a table header is misleading, inspect a JSON object that Markdown omitted, or refuse to treat an incomplete chart as data. It does not change the numerical recognition model simply by describing those checks more clearly. Here, the version checks and identical fixed-control output align with that distinction. The evidence supports adopting the clarified procedure without inventing a percentage gain in extraction accuracy.

The new corpus also challenges any attempt to turn the first report's useful fallback into a universal rule. Nintendo's spanning header benefited from HTML, and Berkshire's fragmented text became easier to read in HTML. Toyota's split unit header did not acquire a span, however, and JPMorgan's migrated footnote remained attached to the wrong numeric cell. Docling improved some tables while leaving a new Rio table incompletely structured. The correct response is not to rank one parser as always superior. It is to choose a route for the particular failure and check whether that failure actually disappeared.

There is no contradiction between saying that the revised procedure works and reporting unsuccessful extraction representations. Its own verification gate explicitly allows another route or an honestly unresolved gap. On Rio's slide, the image supplied checked source evidence even though no tested structured output was accepted as complete. On the compensation table, reading the source and related page resolved the requested definitions, while the raw table exports remained unsuitable for unattended ingestion. These are successful supervised research responses, not successful universal parsing.

Limitations remain important. Neo knew the first run's failures and proposed fixes, so this is an informed operator's application, not a blinded test of whether another agent would reliably obey every instruction. The fresh corpus was purposive and influenced by download accessibility. There was no systematic search for low-quality natural scans; the old Berkshire file supplies historical layout only. The tests do not cover every warning, character, note or page in the documents. They also do not establish cross-language readiness from English translations.

The combined evidence therefore reinforces the original deployment insight rather than superseding it: recover characters, preserve structure where possible, and independently check the meaning needed for the task. Improved instructions strengthen that separation. The remaining risk is silently reducing verification to an exit code, a digit search or the presence of a JSON cell.

## Conclusion

The updated shared skill works better as an operational guide: its corrected output paths, explicit metadata mapping, clearer HTML fallback and stronger context checks were exercised successfully. It remains a lean set of alternatives rather than an unnecessary sequence of converters. The fresh official corpus extended the first test beyond its original companies and included a historical report and proxy-specific compensation problem. The useful result is greater confidence in the procedure's applicability, accompanied by concrete examples of where its existing verification gate must still stop an automated correctness claim.

The fixed controls do not support an improvement in raw recognition. Several outputs were identical to the first run, including the scan errors and the successful crop recovery that already existed. The engine versions matched, and the repeated Docling currency merge and partial chart recovery persisted. These are expected limits of a guidance-only update, not grounds to declare the update ineffective. They establish what the update actually accomplished and prevent a misleading before-and-after accuracy story.

**The single recommendation is to keep the updated skill for supervised use and retain this compact set of positive and negative cases as regression evidence.** There is no demonstrated need for another installed converter or a mandatory multi-tool chain. An optional short clarification could mention HTML's usefulness for fragmented in-cell text as well as spanning headers, while retaining its existing requirement to verify the result. The new Toyota and proxy counterexamples should accompany Nintendo's positive HTML case if Morpheus adopts fixtures.

No new general governance gate is warranted: the current rule already rejects missing content and ambiguous columns. The structural improvement supplied by this task is reproducible evidence and explicit semantic counterexamples, not duplicated rules. Natural degraded scans, non-English documents and blinded testing with independent agents remain concrete future extensions. This report leaves the shared skill and the first report unchanged for Morpheus's review; it neither certifies unattended ingestion nor changes any investment conclusion.

## Reproduction and Evidence

### Evidence bundle and commands

The retained evidence root is `/home/hermes/.local/share/Trash/files/pdf-extraction-retest-20260925T100452Z/`. Downloads, outputs and task-only scripts were moved there together from Neo's scratch after the processes finished. This recoverable review hold is outside the 24-hour scratch pruner but remains subject to eventual manual Trash cleanup; it is not a permanent research repository. A complete file-hash inventory was checked across the move. Historical absolute paths in run logs describe the original execution location. The first-run root remains `/home/hermes/.local/share/Trash/files/pdf-extraction-review-20260925T083628Z/` and was read, not modified.

- `state.json`: retrieved URLs, hashes, sizes, page counts, acquisition failures and revision identity.
- `skill-under-test.md`, `versions.json`, `control-provenance.json`: pinned instructions, exact version comparisons and copied-fixture hashes.
- `selections.json`: corrected physical-page matrix; `semantic-checks.json`: manual sampled labels, values, units, periods and caveats.
- `record-run.py`, `exercise.py`, `followup.py`: task-only execution instrumentation; these were not installed as skills.
- `runs/<case>/result.json`, `stdout.txt`, `stderr.txt`, `resources.txt`: exact calls, measured cost and diagnostics.
- `audit-evidence.py`: read-only recomputation of source identities, coverage, fixed-control equality and execution metrics. Its output is saved as `audit-results.json`.
- Original PDFs, native text, generated Markdown/JSON and PNG source renders remain together. Raw downloaded material is not committed to Brain.

Run `python3 audit-evidence.py` from the retained bundle to regenerate the mechanical audit. It needs the stated first-run bundle for equality checks and does not certify semantic correctness. For conversion replay use a fresh task-owned root, copies or fresh downloads with matching hashes, and the scripts/manifests. The recorder refuses existing case directories. Run `exercise.py selected`, `exercise.py whole`, `exercise.py docling`, `exercise.py controls`, then `followup.py`. The originally recorded Rio TOC mistake remains visible: `exercise.py` retains its initial Docling page-26 invocation, while `followup.py` adds the actual page-27 statement. Extra reference-page and corrected API calls are recorded in their respective `result.json` files. This is an evidence bundle with replay instructions, not an idempotent packaged test suite.

### Source hashes

These hashes were calculated from the downloaded originals and checked against the first-run hashes for non-overlap.

| Original | SHA-256 |
|---|---|
| `berkshire-annual.pdf` | `777a62551d4542ce62671df66c218247a398ecb0e66aaa8a5410daeb49b67fbf` |
| `berkshire-historical.pdf` | `e150267a841c99f9c28e530df8aff08ef2c79aadb2717da76eb7dcb245f7a37a` |
| `toyota-summary.pdf` | `987edd45cd22d1b15f6b728d2e84e5c07ebd8fa8788c4b5e9a537e028b669c56` |
| `toyota-slides.pdf` | `4c5656574e1ed6abc30df41c5d673a231e35e5527b955aa461df9c272bb8e8df` |
| `rio-results.pdf` | `97576be0a19e61830f7444eb6f5f2b748cc08a2c58bfe4d99ae42f0c88a02650` |
| `rio-slides.pdf` | `677ab9536cc2d8e795bbaf48d14de1289dfc7ebb865bf09105ec0f07977fc12d` |
| `jpmorgan-annual.pdf` | `2a3ee9733eafd01e7667c5540fbd797c4cc688d14f00638a877f5623d1316d9d` |
| `jpmorgan-proxy.pdf` | `d44837c570a6a7268ecf975c8c9130e34af7ece307c8b8135da2072619f84a48` |

### Independent review

A separate-context, same-model-family evidence reviewer under `deleg_7780766f` returned **APPROVE WITH CORRECTIONS**. It independently checked source hashes, sizes and page counts; deployed/canonical/snapshot identity; versions; sequential whole-document markers; the corrected selection scope; and fixed-control results. It reviewed the saved evidence and provisional conclusions, not the final report draft: the draft-ready steering message arrived after that reviewer had finished. No final-prose approval or different-model-family review is claimed.

The material corrections are incorporated: no measured causal reliability improvement; no general accuracy claim from the new scan; precise mixed-component SCT timing; narrow Toyota/JPMorgan/Rio structure claims; and explicit fresh-path replay and coverage limits. Neo verified the added Barnum year/salary/stock-award errors against a source-image crop, the saved OCR row and native extraction. The read-only audit script was exercised again after evidence preservation. Review transcript: `/home/hermes/.hermes/profiles/neo/cache/delegation/live/deleg_7780766f/task-0.log`. The verdict and substantive findings are preserved here rather than depending solely on that runtime-managed transcript. The report remains `draft` in the formal pipeline pending Morpheus's owner review, not because test execution is incomplete.

## Cross-Links

- [First field-test report](pdf-extraction-company-field-test.md): historical baseline, preserved unchanged.
- [Updated canonical skill](../../governance/skills/pdf-extraction.md).
- [Deployment insight](../insights/pdf-extraction-tools.md): architecture confirmed, not superseded.
- [Review provenance](#independent-review).

## Sources

[4] https://berkshirehathaway.com/2025ar/2025ar.pdf -- Berkshire Hathaway 2025 annual report
[5] https://berkshirehathaway.com/2002ar/2002ar.pdf -- Berkshire Hathaway 2002 annual report
[6] https://global.toyota/pages/global_toyota/ir/financial-results/2026_4q_summary_en.pdf -- Toyota FY2026 financial summary
[7] https://global.toyota/pages/global_toyota/ir/financial-results/2026_4q_presentation_en.pdf -- Toyota FY2026 financial results presentation
[8] https://cdn-rio.dataweavers.io/-/media/content/documents/invest/financial-news-and-performance/results/2025/2025-annual-results.pdf?rev=1fe52cb440c34b42b7f1cd29197154ca -- Rio Tinto 2025 annual results release
[9] https://cdn-rio.dataweavers.io/-/media/content/documents/invest/financial-news-and-performance/results/2025/2025-annual-results-slides.pdf?rev=fb3fded98fe74c3e928b2744b0f2fcec -- Rio Tinto 2025 annual results slides
[10] https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/annualreport-2025.pdf -- JPMorgan Chase 2025 annual report
[11] https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/proxy-statement2026.pdf -- JPMorgan Chase 2026 proxy statement
