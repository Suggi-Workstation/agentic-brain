---
name: pdf-extraction
description: "Use when reading, scraping or extracting PDFs and scans."
user-invocable: true
disable-model-invocation: false
---

# PDF Extraction and OCR

## When to Invoke

- Read, summarize, search, analyze or extract information from a PDF, whether
  it is a local file, attachment, download or public URL.
- Encounter PDF links or PDF responses while researching, scraping a website,
  following citations or retrieving documents; load before choosing how to read
  the PDF, not only after extraction fails.
- Read filings, annual reports, proxies, papers, manuals or other PDF documents,
  including when using `read_file` or web extraction to access their content.
- OCR scanned PDFs, screenshots or page images; repair unreadable text layers.
- Extract PDF tables, figures or layout; convert to Markdown, JSON or searchable
  PDF; verify page references and values against rendered pages.
- Investigate empty, partial, garbled or badly ordered PDF extraction, missing
  pages, lost footnotes or misaligned table columns.

Loading this skill does not require local conversion. If web extraction already
provides the required PDF content, verify coverage and use it. The local routes
below handle downloads and cases needing OCR, layout, tables or visual checks.
These tools are alternatives, not a mandatory sequence. Prefer native HTML or
spreadsheet cells when they already provide the required source data. Fetching
a PDF and extracting its contents are separate operations; these tools do not
bypass website access controls or replace general web-source discovery.

## Installed Tools

Commands run on the fleet VPS through `terminal`; no environment activation is
needed. These paths are not installations on a connected PC or laptop.

| Tool | Location | Purpose |
|---|---|---|
| Poppler | `/usr/bin/`: `pdfinfo`, `pdftotext`, `pdftoppm` | PDF metadata, existing text and page rendering; no OCR. |
| Tesseract | `/usr/bin/tesseract` | Recognize text in images; plain text, word coordinates or searchable PDF. |
| OCRmyPDF | `/opt/document-tools/ocr/bin/ocrmypdf` | Run Tesseract over PDF images and add a searchable text layer. |
| PyMuPDF4LLM | `/opt/document-tools/pdf/bin/python -m pymupdf4llm` | Convert PDF layout, text and tables to Markdown, JSON or plain text. |
| Docling | `/opt/document-tools/docling/bin/docling` | Model-based layout, reading order, OCR and table structure extraction. |
| pdfplumber | Import with `/opt/document-tools/pdf/bin/python` | Inspect text coordinates and extract or debug individual tables. |

Tesseract language data lives in `/usr/share/tesseract-ocr/5/tessdata/`.
Use `tesseract --list-langs` before selecting a language; `osd` detects orientation
and script, not a text language. Docling's layout and table models are local at
`/opt/document-tools/models/docling/`. Commands below process documents locally.

## Choose the Route

| Need | Use | Why |
|---|---|---|
| Identify a PDF or quickly read selectable text | Poppler | No model inference; preserves the existing characters. |
| Read a page visually, a chart, or a disputed value | Poppler rendering, then `vision_analyze` | Shows the original layout rather than a parser's interpretation. |
| OCR a screenshot, page image or cropped region | Tesseract | Direct image-to-text without a document-conversion pipeline. |
| Read image-only PDF pages or create a searchable PDF | OCRmyPDF | Adds OCR text while retaining the visible document. |
| Recover image text on pages that also contain native text | OCRmyPDF `--redo-ocr`, or Docling | `--skip-text` skips the whole page, including unread image regions. |
| Read ordinary digital PDFs as Markdown with page markers | PyMuPDF4LLM | Reconstructs reading order and tables from the text/layout. |
| Recover complex tables, columns or structure | Docling | Uses layout and table models; returns structured provenance. |
| Extract selected table cells or diagnose column boundaries | pdfplumber | Exposes coordinates, crops and configurable table detection. |

## Procedure

1. Identify the required pages and output: text, Markdown, structured tables,
   searchable PDF or rendered images. Run `pdfinfo` and inspect native text on
   representative/requested pages. Render suspicious or empty pages. A readable
   heading does not establish that an image-based table underneath was read.
2. Choose the least elaborate route that preserves the required content. Use the
   matching commands below; process selected pages when a full conversion is not
   needed. Do not run OCR over clean text merely to obtain Markdown.
3. Read the generated output with `read_file`; locate passages with
   `search_files`. Check tool warnings and actual content, not exit status alone.
   If coverage or structure fails, change route and compare with rendered pages.
4. Before using extracted figures, verify their row/column labels, signs,
   decimals, units, periods and footnotes against the source. Markdown is a
   reading format, not a verified financial dataset. Keep the source page with
   each material figure; PDF page position can differ from the printed label.

## Commands

Run these shell blocks with `terminal`. Replace the example absolute paths and
page numbers. `PDF` is the input file; `OUT` is the chosen output directory:

```bash
PDF="/absolute/path/report.pdf"
OUT="/absolute/path/output"
mkdir -p "$OUT"
```

### Poppler: inspect, extract or render

```bash
/usr/bin/pdfinfo "$PDF"
/usr/bin/pdftotext -layout -f 5 -l 7 "$PDF" "$OUT/pages-5-7.txt"
/usr/bin/pdftoppm -f 5 -l 5 -singlefile -r 200 -png "$PDF" "$OUT/page-5"
```

Page selection is 1-based and inclusive. `-layout` approximates physical text
spacing; it does not reconstruct table cells. Omit `-f` and `-l` for all pages.
The render creates `page-5.png`; open it with `vision_analyze`. Increase rendering
resolution for small text. An empty extraction may be a scan or a blank page;
render it before deciding. `pdfimages -list "$PDF"` lists embedded images, not
proof that those images contain unread text.

### Tesseract: image OCR

```bash
OMP_THREAD_LIMIT=2 /usr/bin/tesseract "$OUT/page-5.png" stdout -l eng --psm 3
OMP_THREAD_LIMIT=2 /usr/bin/tesseract "$OUT/page-5.png" "$OUT/page-5-words" -l eng --psm 3 tsv
```

Input is an image, not a PDF. `--psm 3` detects page layout; use `--psm 6` for an
already-cropped uniform text block, not an entire multi-column page. `tsv` writes
word boxes and confidence to `page-5-words.tsv`; confidence is not proof of
numeric correctness. Replace `tsv` with `hocr` for positioned HTML or `pdf` for
a searchable image PDF. Multiple installed languages use `-l eng+deu`.

### OCRmyPDF: searchable PDFs

For image-only pages, including files interleaving digital and scanned pages:

```bash
OMP_THREAD_LIMIT=2 /opt/document-tools/ocr/bin/ocrmypdf \
  --no-overwrite --skip-text --output-type pdf --optimize 0 \
  --jobs 2 --tesseract-timeout 120 -l eng \
  "$PDF" "$OUT/searchable.pdf"
```

Use a different output path from the input. This uses local PDFium rendering;
Ghostscript is not required for this ordinary-PDF route. Read the result with
Poppler or convert it with PyMuPDF4LLM using `--ocr-mode never`.

- Replace `--skip-text` with `--redo-ocr` to replace old invisible OCR and recover
  text in images while preserving visible native text on the same page.
- Add `--pages 5-7` to OCR only those 1-based pages. Other pages remain in the
  output; this does not create a page subset.
- Add `--rotate-pages` for sideways scans or `--deskew` for tilted lines only
  when needed. Rotation uses Tesseract's `osd` data.
- `--force-ocr` rasterizes visible text and vectors too. Use only for selected
  pages whose text layer cannot otherwise be recovered; recheck the result.
- `--sidecar` contains recognized OCR text, not all pre-existing digital text.
  Read the resulting PDF for complete text. Timeouts can leave pages without
  OCR even when an output PDF exists; check logs and page coverage.

### PyMuPDF4LLM: Markdown and layout JSON

For a digital PDF or an OCRmyPDF result with a usable text layer:

```bash
/opt/document-tools/pdf/bin/python -m pymupdf4llm "$PDF" \
  --out "$OUT" --workers 1 --backend md --ocr-mode never \
  --header --footer --opt page_separators=true
```

For `report.pdf`, output is `$OUT/report/report.md`, with `run-log.txt` in the
same subdirectory. Inspect that log: a batch can finish despite individual
conversion failures. Headers and footers are explicitly retained.

- Use `--backend json` for page numbers, boxes and table structure, or
  `--backend txt` for plain text. JSON uses `pages[].page_number` (1-based).
- For tables needing merged cells, add `--opt table_output=html` to Markdown
  output, then check header associations against the source.
- Optional selective OCR: replace `--ocr-mode never` with
  `--ocr-mode select-keep --ocr-func tesseract --ocr-lang eng --opt ocr_dpi=300`.
  Direct OCR can omit scanned table rows. Prefer OCRmyPDF or Docling for scanned
  tables and verify coverage; do not treat automatic OCR as a completeness check.

For selected pages, use the Python API rather than a list-valued CLI `--opt`:

```bash
/opt/document-tools/pdf/bin/python -c '
import json, sys, pymupdf4llm
pages = [int(n) - 1 for n in sys.argv[2:]]
chunks = pymupdf4llm.to_markdown(sys.argv[1], pages=pages, page_chunks=True, use_ocr=False)
print(json.dumps(chunks, indent=2))
' "$PDF" 5 6 7
```

Arguments are 1-based; the API list is 0-based. Each returned chunk has `text`,
`page_boxes` and `metadata.page_number` (1-based). CLI `--opt` does not parse
list values; a string such as `pages=[4,5,6]` fails inside the batch.

### Docling: complex layout and tables

```bash
HF_HUB_OFFLINE=1 OMP_NUM_THREADS=2 /opt/document-tools/docling/bin/docling convert "$PDF" \
  --from pdf --to md --to json --pipeline standard \
  --ocr-engine tesseract --ocr-lang eng --device cpu --num-threads 2 \
  --page-batch-size 1 --table-mode accurate \
  --artifacts-path /opt/document-tools/models/docling \
  --image-export-mode placeholder --abort-on-error --output "$OUT"
```

For `report.pdf`, output is `$OUT/report.md` and `$OUT/report.json`. Add
`--page-range 5-7` for a 1-based inclusive subset. Use `--no-ocr` for verified
clean digital pages. If selective OCR misses image text, use
`--ocr-mode full_page` on the affected page range and recheck it.

JSON carries `tables[].data.table_cells`, their row/column offsets and
`prov[].page_no`/bounding boxes. Markdown can omit headers or table-attached
footnotes even when JSON contains them. Inspect JSON `texts` for `footnote`,
`page_header` and `page_footer` labels; follow table `footnotes` references and
verify against the page. A successful conversion is not proof of complete text.
Keep the standard pipeline; VLM, remote services and additional enrichment
models are not part of this installed route.

### pdfplumber: selected tables and coordinates

Extract ruled tables from PDF page 5 as cell arrays:

```bash
/opt/document-tools/pdf/bin/python -c '
import json, sys, pdfplumber
with pdfplumber.open(sys.argv[1]) as doc:
    page = doc.pages[int(sys.argv[2]) - 1]
    print(json.dumps({"page": page.page_number, "tables": page.extract_tables()}, indent=2))
' "$PDF" 5
```

The Python page list is 0-based; the command argument and `page.page_number` are
1-based. `extract_tables()` returns all detected tables, not just the largest.

- For unruled aligned text, try `page.extract_tables({"vertical_strategy":
  "text", "horizontal_strategy": "text"})`; inspect for false columns.
- Isolate a table with `page.crop((x0, top, x1, bottom))`, then extract from the
  cropped page. Coordinates are PDF points measured from the top-left.
- Inspect `page.extract_words()` for word boxes. To see detected lines/cells,
  use `page.to_image(resolution=150).debug_tablefinder().save("table-debug.png")`
  inside the same Python context, with a chosen absolute output path.
- pdfplumber does not perform OCR. Use an OCRmyPDF result if the source is a
  scan, and expect OCR-positioned tables to need additional inspection.

## Verification

PASS: requested content is actually present, page references map to the source,
and material table values, labels, units and footnotes match the original.
HALT the completeness or correctness claim if pages/rows are missing, OCR timed
out or columns are ambiguous. Use another route or state the unresolved gap;
never fill missing cells by inference.
