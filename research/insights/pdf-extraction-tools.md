---
name: pdf-extraction-tools
id: 20260925T080023Z
tier: insight
status: active
source:
  - 20260923T071010Z
author: Morpheus
tags: [pdf, ocr, document-processing, skills, provenance, verification]
links:
  - governance/skills/pdf-extraction.md
  - reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md
  - research/insights/skill-bloat-and-pitfall-placement.md
---

# PDF Extraction Tools and Shared Skill

## The Insight

**A reliable PDF-reading capability separates character recovery, document structure and source verification; successful conversion alone proves none of them complete.**

This is the blueprint of an implemented, on-demand document-reading capability on the fleet's Linux VPS. The VPS is the server on which the Hermes agents run. Hermes supplies the agent's file, terminal and vision tools; the document toolkit supplies specialist command-line programs and Python libraries. The shared `pdf-extraction` skill explains how an agent chooses and operates those programs. The capability is available to the VPS agents, not installed automatically on connected desktop or laptop machines.

The underlying problem is that a PDF records how pages should look, not necessarily how their contents should be read. A digital PDF can contain positioned characters and vector lines without explicitly identifying a paragraph, reading order or table cell. A scanned PDF can contain only photographs of pages. A mixed document can alternate those page types, and a single page can combine a selectable heading with an image-only table. A searchable PDF can also contain an invisible OCR text layer whose characters disagree with the visible image.

These cases require different operations. Native extraction recovers existing characters. Optical character recognition, or OCR, infers characters from pixels. Layout analysis groups content into headings, paragraphs, columns and tables. Verification checks that the reconstructed output still means what the source means. Recovering `1,234.56` is not sufficient if it has moved from the 2025 column into the 2024 column, lost its unit, or become detached from a qualifying footnote.

The installed toolkit combines Poppler, Tesseract, OCRmyPDF, PyMuPDF4LLM, Docling and pdfplumber. It is not a mandatory sequence of tools. An agent may need only Poppler for a readable page, OCRmyPDF followed by text extraction for a scan, or Docling plus a rendered-page check for a complicated table. The organizing principle is to use the least elaborate route that preserves the evidence needed for the task, then escalate where that route fails.

The scope is shared tools and shared procedural knowledge, not shared research state. Agents use the same installed executables and skill while retaining responsibility for their own documents and conclusions. There is no new always-running parser service, automatic document archive, vector database, cloud-upload integration or custom Hermes tool. Installation also does not alter repository indexing or make every `read_file` call automatically use the full toolkit.

This distinction matters particularly in investment research: an openly failed conversion is recoverable, but a plausible number under the wrong heading can silently corrupt a valuation. The implemented skill therefore treats Markdown as a reading aid and page-linked source evidence as the basis for material claims. It does not certify financial data merely because the output is readable.

## Evidence

### Source Chain and Evidence Boundaries

The methodological source is reflection `20260923T071010Z`, [Preloading a Skill Proves Exposure, Not Correct Application](../../reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md). That reflection separates skill availability, delivery, execution and supported conclusions. It is not an earlier report of this PDF installation. This blueprint applies its distinction to the document toolkit and adds direct deployment observations from September 25, 2026.

The implementation evidence consists of the installed packages and model artifacts, the canonical [PDF extraction skill](../../governance/skills/pdf-extraction.md), actual extraction runs, output inspection and cross-profile loader checks. The initial canonical skill was published in Brain commit `cde409677d713947de21535b632f75ae97e89109`; its invocation description was subsequently broadened to include PDF reading and PDF-related web scraping. The deployed skill is the current operating reference, rather than that initial commit being a permanent version pin.

Claims below distinguish supported interfaces from measured behavior. Upstream documentation explains intended functionality; installation tests establish that selected paths work here. Neither establishes universal accuracy or performance. No finished end-to-end research run by another agent is claimed as evidence of successful adoption.

### Deployment Layout and Isolation

The system uses Ubuntu-managed native commands alongside isolated Python 3.12 environments. A Python environment is a directory containing its own interpreter entry point and installed libraries. This separates document dependencies from the environments that run Hermes and the repository watchers/indexers. The agents invoke absolute executable paths, so they do not need to activate an environment or change their profile configuration to choose a tool.

| Location | Contents and responsibility |
|:--|:--|
| `/usr/bin/` | Ubuntu-managed Poppler utilities and the `tesseract` command; package dependencies remain in normal system locations. |
| `/usr/share/tesseract-ocr/5/tessdata/` | Tesseract recognition data. The verified installation has English (`eng`) and orientation/script detection (`osd`); other text languages require their own data. |
| `/opt/document-tools/pdf/` | Python environment containing PyMuPDF4LLM, PyMuPDF Layout, PyMuPDF and pdfplumber. |
| `/opt/document-tools/ocr/` | Python environment containing OCRmyPDF and its dependencies, including PDFium bindings and PDF assembly libraries. |
| `/opt/document-tools/docling/` | Python environment containing Docling and CPU-only PyTorch dependencies. |
| `/opt/document-tools/models/docling/` | Downloaded Heron layout and TableFormer model artifacts. The layout download includes PyTorch and ONNX forms; their presence does not mean both execute in every conversion. |
| `/opt/document-tools/models/huggingface/` | Model-download support cache and metadata, distinct from documents being processed. |
| `/opt/document-tools/requirements-pdf.txt`, `requirements-ocr.txt`, `requirements-docling.txt` | Installed Python dependency pins for the corresponding environments. The Docling pins document the CPU-wheel selection requirement. |
| `/srv/brain/agentic-brain/governance/skills/pdf-extraction.md` | Canonical, Git-tracked procedural skill in the shared knowledge repository. |
| `/home/hermes/.agents/skills/search/pdf-extraction/SKILL.md` | Byte-identical installed skill discovered by the VPS Hermes profiles through their configured external skill directory. |

The version record is a verified installation snapshot, not an assertion about future installed or upstream versions:

| Verified | Native tools | Python document tools | Docling inference runtime |
|:--|:--|:--|:--|
| 2026-09-25 | Poppler `24.02.0-1ubuntu9.9`; Tesseract `5.3.4-1build5` | OCRmyPDF `17.12.1`; PyMuPDF4LLM, PyMuPDF Layout and PyMuPDF `1.28.2`; pdfplumber `0.11.10`; Docling `2.130.0` | PyTorch `2.14.0+cpu`; `torch.version.cuda` returned `None`. |

Shared availability does not require one physical directory. Poppler and Tesseract stay where Ubuntu's package manager expects them; Python packages live under the dedicated document-tools root. The models load into the invoking conversion process rather than requiring a new daemon. Dependency isolation protects the existing production runtimes, but it is not a security sandbox for malicious PDFs.

The local `BOX.md` systems blueprint records the folder layout and summarizes the capability under `4. Search and Document Processing`, with `4.1. Index Stack` and `4.2. PDF Extraction and OCR`. That file is Morpheus's local machine map, not a prerequisite for understanding this document. The detailed skill remains the command reference. All named paths in this blueprint identify deployed components; they are not instructions to copy documents into shared model or executable directories.

### Poppler: Read the Existing PDF or Render Its Appearance

Poppler is a PDF-processing library distributed with useful executables. `pdfinfo` exposes document properties such as page count and dimensions. `pdftotext` extracts an existing text layer; its layout option approximates the physical spacing of that text. `pdftoppm` renders selected PDF pages into images. `pdfimages` can inventory embedded images. The Ubuntu package file list confirms the command locations. [1]

Poppler is the inexpensive inspection and visual-reference layer. It can answer whether a page contains selectable text and produce a rendering for the agent to examine. It does not recognize text inside images merely because it can render them. An empty text result is therefore a signal to inspect the page, not a conclusion that the page contains no information. Conversely, finding some text does not establish that every region was read.

Rendering is also the comparison path when two extractors disagree. The original page's visible column headers, footnote markers and signs remain the reference. A rendered image can be passed to Hermes's `vision_analyze`; that model-assisted examination is separate from the local command-line processing and follows the agent's configured vision provider.

### Tesseract: Turn Image Regions into Recognized Characters

Tesseract is an OCR engine, not a PDF layout converter. Its command-line input is an image. It analyzes image regions using recognition models and language data, then emits text or positioned representations such as TSV and hOCR. TSV is tab-separated text containing recognized words and coordinates; hOCR is HTML carrying layout information. A searchable image-PDF output is also supported. [2]

Page segmentation mode changes what arrangement the engine expects. Automatic page segmentation is suitable for a page whose layout is not already isolated. A uniform-text-block mode is more appropriate after cropping a specific block. Choosing the wrong assumption can merge columns or miss text. Language data also matters: `osd` provides orientation/script detection, not German, Japanese or any other general recognition language.

The skill uses Tesseract directly for screenshots and page crops. It also uses Tesseract indirectly through OCRmyPDF and Docling. Recognition confidence is a diagnostic signal, not a guarantee that a decimal, negative sign or financial total is correct. Adding image OCR therefore closes a coverage gap without removing the need for source comparison.

### OCRmyPDF: Assemble a Searchable PDF Around OCR Results

OCRmyPDF manages the PDF-level work around an OCR engine. It inspects pages, renders content that needs recognition, invokes OCR, and assembles a derivative PDF with a searchable text layer. Optional operations can correct orientation or skew. The installed ordinary-PDF route uses PDFium through `pypdfium2`; it was exercised without installing Ghostscript. This is not a claim that every archival PDF/A conversion or optional feature is dependency-free. [3]

Its modes have different preservation semantics. Skipping text pages is appropriate when a file alternates clean digital pages and image-only pages. It is insufficient when an individual page has both native text and an unread image table: the existing heading can cause the whole page to be skipped. Redo mode can replace old invisible OCR and recover image text while preserving visible native text. Force mode rasterizes visible text and vector content too, so it is a stronger intervention rather than a harmless accuracy switch.

A searchable PDF is not the same thing as a complete plain-text sidecar. OCRmyPDF's sidecar contains recognized OCR text and omits pre-existing digital text that was not OCRed. Reading the finished PDF with a text extractor is necessary when both sources of text matter. Similarly, selecting pages limits where OCR is applied; unselected pages remain in the output PDF. Timeouts can leave a page without recognized text even though an output file was produced. [3]

### PyMuPDF4LLM: Convert Text and Layout into Agent-Readable Output

PyMuPDF4LLM provides Markdown, JSON and text conversion over PyMuPDF. In the installed release, PyMuPDF Layout is a required dependency; this is not a model-free text extractor. The vendor describes layout analysis based on graph neural networks over PDF objects, positions and relationships; the installed environment includes ONNX Runtime. The architecture supports CPU execution without a hosted parser. Vendor speed claims are not local benchmarks. [4]

For ordinary digital PDFs and OCR-repaired documents, this is the routine conversion route. Markdown offers readable headings and tables. JSON preserves page-level layout objects. The Python API can return page chunks containing text, boxes and page metadata. The skill explicitly retains headers and footers and requests page separators for its Markdown command instead of relying on defaults that may omit them.

The installed batch command writes a subdirectory for each input, containing the converted file and `run-log.txt`. A completed batch and shell exit status zero are not proof that its document conversion succeeded. In a real test, passing a list through the CLI's generic option parser failed inside the batch because that parser converts booleans and numbers but not list strings. The selected-page route therefore uses the Python API with actual integer page indices. The skill documents this distinction rather than patching upstream software.

Selective direct OCR is available, but it is not the preferred scanned-table route here. It omitted rows in the controlled scan test. Converting a successfully OCR-repaired PDF with OCR disabled recovered the tested values. The default recommendation follows that observation; it does not claim that direct OCR always fails.

### Docling: Reconstruct a Structured Document

Docling's standard PDF pipeline combines document parsing, layout analysis, OCR where enabled, and table-structure recognition. This deployment predownloads layout and table artifacts and explicitly selects Tesseract for OCR. CPU-only PyTorch provides model inference. The skill uses the standard pipeline, not an optional full-page vision-language-model pipeline or a remote document service. [5]

The result is more than a Markdown string. A `DoclingDocument` contains content items, grouping and document hierarchy, tables, page information and provenance. Provenance associates an item with a source page and bounding box: it tells the agent where to look when checking the extracted claim. Table cells include row and column offsets; text items can be classified as ordinary body text, footnotes, headers or footers. Different layers distinguish the document body from page furniture. [5]

The Markdown export is a view of this representation, not a promise to serialize every stored item. Testing found a table-attached footnote present in JSON but absent from Markdown. Exporting additional content layers recovered a header but did not by itself recover that attached footnote. The skill consequently instructs the agent to inspect text labels, table footnote references and the original page rather than trusting an attractive Markdown table alone.

This makes Docling useful when column order, merged headers or table structure defeat the routine extractor. It can also introduce interpretation errors or classify prose as a table. Model-assisted structure recovery is a reason to inspect the result more carefully, not a replacement for inspection.

### pdfplumber: Inspect the Geometry of Particular Tables

pdfplumber exposes PDF characters, words, lines, rectangles and their coordinates. Its table detection can use ruling lines or infer boundaries from aligned text. Cropping isolates a target region before extraction; visual debugging overlays proposed table geometry on a page rendering. It is useful when the question is not "convert this whole report" but "which words and numbers fall into these cells?" [6]

The skill demonstrates extracting all detected tables on a selected page, changing strategies for unruled tables, reading word boxes and inspecting a debug image. An agent can therefore investigate a suspicious row without rerunning a model over the entire report. Coordinates must be interpreted according to the tool: the crop interface uses PDF points with top-based vertical coordinates.

pdfplumber does not perform OCR. An image-only scan must first acquire a text layer or be handled by another route. Even after OCR, word positions and missing characters can make table reconstruction unreliable. The tool is a diagnostic and targeted extraction option, not an independent numerical truth oracle.

### What Was Actually Tested

The controlled fixtures were explicitly synthetic, not invented company disclosures. They included a digital page with a ruled table, an image-only version, and a mixed page with a native heading above a rasterized table. Known content included the displayed value `1,234.56`, parenthesized negative values, two year columns and a qualifying footnote. This made omissions and changed table relationships observable instead of inferring correctness from the appearance of output files.

| Check | Observed result | What it establishes |
|:--|:--|:--|
| Poppler metadata, native extraction and rendering | Executed successfully; expected native text and rendered images were produced. | The inspection/rendering route works on the fixtures. |
| Tesseract text and TSV | Recognized the checked value and returned positioned word output. | Direct image OCR is usable; it does not establish arbitrary scan accuracy. |
| OCRmyPDF skip versus redo | Skip recovered the image-only page but left the mixed page's image table unread; redo recovered its checked value while retaining the native heading. | Page-level text presence cannot substitute for region coverage. |
| PyMuPDF4LLM direct OCR | The checked value appeared once where the fixture required three occurrences. | Successful command execution concealed missing scanned table content. |
| OCRmyPDF followed by PyMuPDF4LLM without OCR | Recovered the checked value on each fixture page. | This recovery route worked for the observed omission class. |
| pdfplumber | Returned the exact expected ruled-table cell arrays and produced a table-debug rendering. | Targeted table extraction and geometric inspection work on the fixture. |
| Docling | Produced structured tables with source-page provenance; the checked value was recovered on each page. | The local standard pipeline and model artifacts function together. |
| Docling export comparison | A mixed-page footnote existed in JSON but not Markdown. | A serialized reading view can omit evidence present in the richer representation. |
| PyMuPDF4LLM selected-page CLI versus API | A string-valued page list failed in the batch log; a real integer list through the API worked. | CLI acceptance and batch completion are insufficient success checks. |
| Hermes skill discovery | The catalog description and complete skill resolved to the shared installed path for the live named-profile set; canonical and installed bytes matched. | Availability and discovery were verified, not autonomous adoption in future work. |

A real-document check used Crocs's 2026 definitive proxy, linked by the issuer's April 23, 2026 filing page. The downloaded PDF had 98 physical pages; its final two pages contained images but no native text. Selected-page extraction covered physical pages 51-52, and OCR covered pages 97-98. Docling and the PyMuPDF4LLM Python API recovered the checked compensation values. Andrew Rees's 2025 salary of `$1,188,462` and total of `$10,958,007` were spot-checked against the rendered compensation table. Its printed page label was 48, while its physical PDF position was 52. These values are extraction-test targets, not an investment assessment. [7]

OCRmyPDF recovered text from the final image pages, but the resulting text contained visible recognition errors. The test therefore supports "previously inaccessible text became partially readable," not "the proxy was fully and correctly transcribed." The entire filing was not audited cell by cell. The controlled fixtures and these selected real pages establish an operational baseline; they are not a representative parser benchmark or proof of fleet-wide research reliability.

## Implications

### The Skill Is the Operating Procedure, Not Another Parser

The skill is a standalone Markdown document, not executable orchestration code. Hermes can discover its short description and load its full body on demand. Once loaded, the agent uses ordinary `terminal`, `read_file`, `search_files` and `vision_analyze` tools to perform the chosen work. There is no hidden script that automatically dispatches every PDF through all available converters.

Its frontmatter identifies the skill by `name: pdf-extraction`, provides a concise description, permits user invocation, and does not disable model invocation. The description is deliberately broad: **"Use when reading, scraping or extracting PDFs and scans."** It includes the user's ordinary task verbs rather than limiting discovery to a known extraction failure or to already-local files.

The `When to Invoke` section covers reading, summarizing, searching and analyzing PDFs; attachments, downloads and public URLs; PDF links or responses encountered while researching or scraping; filings, reports, proxies, papers and manuals; OCR; table/layout extraction; and missing or garbled output. An agent should recognize the capability when it encounters a PDF, not only after a converter returns blank text.

Broad invocation does not force unnecessary local processing. If a web-extraction result already contains the required PDF evidence, the agent can check that coverage and use it. If access returns only an abstract, misses image pages, loses a table or leaves layout ambiguous, the local toolkit provides recovery options. Finding or downloading the source and extracting its contents remain separate problems. Nothing in this skill bypasses access controls or turns a blocked download into an authorized one.

The rest of the skill has an explicit structure:

| Section | Function |
|:--|:--|
| `When to Invoke` | Recognize the task before selecting an extraction route. |
| `Installed Tools` | Identify executable environments, language data and model locations. |
| `Choose the Route` | Match the needed result to a tool and explain why that choice fits. |
| `Procedure` | Inspect the source, choose a route, inspect its output and verify material evidence. |
| `Commands` | Provide runnable, tool-specific examples and important option semantics. |
| `Verification` | Define when completeness/correctness can be claimed and when a gap must remain explicit. |

The installed document does not require another skill to explain the PDF tools. It also contains no history, installation narrative, temporary-file policy or cleanup section. Those are not its purpose. This insight explains the architecture and evidence; the skill owns changing operational commands. Keeping that distinction avoids independently maintained copies of the procedure while leaving this blueprint sufficient to understand the system.

### A New Agent's Mental Model

The decision structure is a set of alternatives and bounded escalations:

```text
PDF URL, attachment or local file
    |
    +-- Required content already available as reliable HTML/spreadsheet/text?
    |       -> Read that representation and check its source context.
    |
    +-- Need existing PDF text or a view of the original page?
    |       -> Poppler; render when coverage or meaning is uncertain.
    |
    +-- Need characters from an image?
    |       -> Tesseract directly, or OCRmyPDF for a PDF derivative.
    |
    +-- Need ordinary PDF reading order and Markdown/JSON?
    |       -> PyMuPDF4LLM, normally using the existing/repaired text layer.
    |
    +-- Need harder layout or table structure?
    |       -> Docling, retaining JSON provenance as well as readable output.
    |
    +-- Need to inspect specific cells or boundaries?
            -> pdfplumber, cropped/parameterized as the table requires.

Any route -> check output coverage and source meaning -> supported claim
         \-> unresolved mismatch -> another route or an explicit limitation
```

For a clean digital report, starting with OCR would add recognition uncertainty to characters already available. For a scan, native text extraction alone cannot recover the missing evidence. For a mixed page, skipping all pages with any existing text can lose the very table the research question concerns. For a complicated table, the useful escalation is structure recovery or cell inspection, not merely collecting a longer plain-text string.

The capability also separates output contracts. A plain-text file is convenient for searching but carries limited structure. Markdown conveys reading order and simple tables but may flatten merged cells or omit secondary content. JSON can retain page and bounding-box provenance but still contains model or OCR errors. A searchable PDF adds a text layer without thereby validating it. A rendered image provides the visible source for comparison but still requires careful interpretation.

Page numbering is a practical part of that contract. Poppler and Docling page ranges are 1-based; Python page lists are generally 0-based. The skill's selected-page Python example translates its human-facing page arguments before calling the API. Returned page metadata refers to physical source position, not necessarily the printed page label. The Crocs test demonstrates why citations should distinguish those notions when they differ.

### Shared Scope, Maintenance and Limits of Automation

The shared boundary is justified by a shared runtime and repeated need: VPS agents run on the same server and need the same PDF capabilities. It does not justify a shared queue of private documents, a fleet-wide document archive or shared outputs by default. A future profile needs the shared skill directory configured and access to the installed commands. A connected machine does not gain those binaries merely by reading the skill; these paths refer to execution on the VPS.

Updates should follow the actual ownership boundary. Ubuntu manages native utilities and language packages. The document environments and dependency pins manage Python compatibility, with CPU-wheel selection retained for Docling. Model artifacts have their own identity and licensing, separate from package code. PyMuPDF4LLM and the installed PyMuPDF Layout release use AGPL/commercial licensing; that choice is not automatically equivalent to Docling's MIT code license or to the licenses of every downloaded model. Redistribution or a hosted service would need its own license review. [4][8]

A targeted version or model change calls for repeating the behaviors it can affect: text coverage, mixed-page recovery, table mapping, footnotes, page provenance and truthful batch error reporting. Import success or a version command alone cannot establish those behaviors. The current fixture failures provide specific regression targets rather than a reason to install more overlapping parsers without evidence.

Privacy also has separate layers. The documented parsing commands run locally with the downloaded artifacts; Docling's example uses offline Hub mode and no remote parsing pipeline. Model downloads themselves required network access. Passing a rendered page to a configured external vision model is a different action from local parsing, and local OCR is not malware sanitization. Document instructions remain untrusted data. These boundaries prevent "local toolkit" from being misread as a universal privacy or security guarantee. [9]

Most importantly, catalog checks do not establish that an agent will load the skill for every applicable task. The broadened description and invocation section improve selection guidance, and explicit `skill_view(name="pdf-extraction")` resolves the body. They are not a newly installed automatic interception hook. Real work with another agent remains the next adoption test: observe whether it loads the skill, chooses an appropriate route, checks omissions and supports its final claims. No changes to cron prompts, profile routing, built-in extraction or mandatory skill preloading were part of this deployment.

## Counter-evidence

The architectural recommendation would need revision if a simpler route demonstrated equal or better coverage, table fidelity and source traceability across the documents the fleet actually uses. The observation that specialized tools were useful in the installation tests does not prove that each will remain necessary. A future parser could make an existing fallback redundant, or better native HTML and spreadsheet access could remove the need for PDF processing in an important workflow. The appropriate comparison would measure supported task outcomes, not count installed packages or compare attractive Markdown samples.

The cheapest falsification test is a small, deliberately varied reading task. Give an agent a digital table, an image-only page, a mixed page, a multi-column report and a table with an attached footnote. Define the expected evidence before conversion. Then check whether the agent actually loads the skill, preserves the required values and labels, finds the footnote, cites the correct physical and printed pages, and discloses any gap. If a single lighter extractor achieves those results as reliably, the routing recommendation should become simpler. If the skill is skipped or the agent accepts missing rows, verified discovery has failed to translate into useful behavior.

Current evidence already rejects stronger claims that this blueprint must not make. Direct PyMuPDF4LLM OCR did not preserve all tested rows. Docling Markdown did not preserve all content available in its JSON. OCR of the real proxy's image pages produced character errors. Those observations disprove "installed means accurate" and "successful conversion means complete." They do not invalidate a toolkit whose explicit design is to detect such failures and recover or report them; repeated failure of those recovery steps would.

There are substantial untested boundaries. Handwriting, unusual scripts, low-resolution or heavily skewed scans, mathematical notation, charts without usable labels, protected files, multi-page spanning tables and very large documents can require different handling. Only the installed English recognition data and selected examples were exercised. General package support for additional languages or formats is not local validation of them. The CPU/thread defaults are conservative starting choices, not a measured concurrency guarantee under simultaneous fleet load.

A further disconfirming result would be maintenance cost exceeding practical benefit: agents might frequently choose incompatible environments, confuse page conventions or spend more effort fixing parser output than reading the original. That would favor simplifying the command surface or changing the installed mix. Such a change should follow observed use, including the planned trial with Neo, rather than assuming that every additional tool is an improvement. The durable claim is the separation of extraction from verification; the particular package selection and default route remain revisable engineering decisions.

## Sources

Local deployment facts and test outcomes were verified on September 25, 2026. External sources below support interfaces, architectural descriptions and source identity; they are not substitutes for the local tests.

1. Ubuntu, [Poppler utility package files](https://packages.ubuntu.com/noble/amd64/poppler-utils/filelist). Confirms installed-command roles and standard executable locations, supplemented by local command execution.
2. Tesseract, [User Manual](https://tesseract-ocr.github.io/tessdoc/) and [command-line usage](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html). Recognition engine, language data, page segmentation and output formats.
3. OCRmyPDF, [Cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html), plus the installed `ocrmypdf --help`. Sidecar scope, redo/force behavior and PDFium rasterization.
4. Artifex, [PyMuPDF4LLM and PyMuPDF Layout architecture/licensing](https://pymupdf.io/blog/open-source-all-the-way-down-pymupdf4llm-goes-fully-agpl), [package documentation](https://pypi.org/project/pymupdf4llm/), and the installed CLI/API implementation. Vendor performance comparisons were not adopted as measured VPS results.
5. Docling, [document representation](https://docling-project.github.io/docling/concepts/docling_document/) and [installation](https://docling-project.github.io/docling/getting_started/installation/), supplemented by installed CLI help, downloaded artifacts and actual JSON output.
6. pdfplumber, [official repository and API documentation](https://github.com/jsvine/pdfplumber). Text geometry, table strategies, cropping, visual debugging and lack of built-in OCR.
7. Crocs, [DEF 14A filed April 23, 2026](https://investors.crocs.com/financial-information/sec-filings/sec-filings-details/default.aspx?FilingId=19364435) and its [linked PDF](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001334036/d8905d87-6797-435b-bcf1-75ce9bb86008.pdf). Selected original pages were rendered and compared with extracted output.
8. Downloaded Docling [Heron model card](https://huggingface.co/docling-project/docling-layout-heron) and [model bundle](https://huggingface.co/docling-project/docling-models). Model terms are separate from application code licensing.
9. OCRmyPDF, [PDF security limitations](https://ocrmypdf.readthedocs.io/en/latest/pdfsecurity.html). OCR does not provide a malicious-document security boundary.

## Cross-Links

- `governance/skills/pdf-extraction.md` -- canonical standalone operating procedure; the installed shared copy must match it.
- `reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md` -- methodological source, id `20260923T071010Z`; explains why availability, execution and correctness require different evidence.
- `research/insights/skill-bloat-and-pitfall-placement.md` -- related design guidance: keep consequential decision points in the skill without adding historical narrative or duplicate policy.
- Shared runtime skills `web-search` and `repo-search` -- complementary source-discovery procedures, not prerequisites for understanding the PDF toolkit or replacements for its extraction methods.
