---
name: pdf-extraction
description: "Use when reading, scraping or extracting PDFs and scans."
user-invocable: true
disable-model-invocation: false
---

# PDF Extraction and OCR

## When to Invoke

Use before reading, summarizing, searching or extracting PDFs from local files,
attachments or web links, including PDFs encountered during research or scraping.
Also use for scans/screenshots, OCR, tables/layout, conversion or incomplete text.
Existing web extraction, HTML or spreadsheet cells may suffice; verify them
rather than converting unnecessarily. The tools below are alternatives.

## Procedure

1. Define the needed pages, fields and output. Inspect `pdfinfo`, native text
   and a representative rendering. Classify each needed region as digital text,
   image text or mixed; a readable heading does not prove the table was read.
2. Choose the simplest matching use case below. Prefer native text to OCR.
   Process only needed pages unless the task requires the whole document.
3. Read outputs and warnings with `read_file` / `search_files`. For a failure,
   distinguish wrong characters from wrong structure, then change one relevant
   setting on the affected region. Preserve the original and baseline output.
4. Compare against the source using `vision_analyze`, cropping small text rather
   than trusting a downscaled page. Check every affected material field you will
   use, including previously correct fields. A repaired row does not validate
   its page. Reject regressions; use a local repair only with its own provenance.
5. Stop when the verification gate passes. If a suitable alternative still
   leaves ambiguity, report the gap; never infer missing digits or cells.

## Choose by Need or Failure

| Situation | Route or adjustment | Reason / limit |
|---|---|---|
| Selectable text; quick reading | Poppler `pdftotext -layout` | Copies existing characters; spacing is not a table schema. |
| Digital document needs Markdown | PyMuPDF4LLM with OCR disabled | Preserves native text while reconstructing layout. |
| Fragmented labels or spanning headers | Try `table_output="html"`; for an isolated row use a native clip | HTML can help spans but also merge notes into labels. Read headers separately. |
| Wrong or missing image characters | Tesseract; crop with a small margin and relevant labels | Render the best original at 300 DPI; compare 400 only if needed. Enlarging an old scan cannot restore detail. |
| Image layout differs | PSM 3: page; 6: uniform cropped block; 7: one line; 11: sparse labels | Never apply block mode blindly to columns. PSM 11 needs source/word boxes to restore associations. |
| Need a searchable scanned PDF | OCRmyPDF baseline; compare `--oversample 300`, then 400 only on failures | Higher resolution can fix one cell and corrupt another. Do not force oversampling on every scan. |
| Mixed text/images or bad old OCR | Replace `--skip-text` with `--redo-ocr`, or OCR only the image region | `--skip-text` skips an entire text-bearing page. Add `--rotate-pages` / `--deskew` only for observed rotation / tilt. |
| Columns collapsed or misplaced | pdfplumber crop and measured column boundaries | Read units/headers separately; check outer columns and graphical qualifiers. |
| Footnote digits joined to amounts | pdfplumber words with `extra_attrs=["size"]` and character coordinates | Separate by source size/position, never by stripping trailing digits. |
| Complex layout remains unresolved | Docling on affected pages | Check JSON provenance, not just Markdown; its documented OCR also uses Tesseract, not an independent engine. |

## Working Commands

Run via `terminal` on the fleet VPS. Replace paths and example page numbers;
use fresh output names for comparisons. `P` is the installed PDF Python:

```bash
PDF="/absolute/path/report.pdf"
OUT="/absolute/path/output"
P=/opt/document-tools/pdf/bin/python
mkdir -p "$OUT"
```

**Inspect / render.** Poppler pages are 1-based; omit the range for all text.
Crop options `-x -y -W -H` use pixels at the chosen DPI, not PDF points.

```bash
/usr/bin/pdfinfo "$PDF"
/usr/bin/pdftotext -layout -f 5 -l 5 "$PDF" "$OUT/page-5.txt"
/usr/bin/pdftoppm -f 5 -l 5 -singlefile -r 300 -png "$PDF" "$OUT/page-5"
```

**Markdown.** For the whole document:

```bash
"$P" -m pymupdf4llm "$PDF" --out "$OUT" --workers 1 --backend md \
  --ocr-mode never --header --footer --opt page_separators=true
```

Require `Status: success` in `run-log.txt` AND the requested content.
Output is `$OUT/report/report.md`, or `$OUT/report.md` when `OUT` is named
`report`. Add `--opt table_output=html` for HTML tables. Replace `--backend md`
with `--backend json` for structured layout or `--backend txt` for plain text;
JSON uses `pages[].page_number` (1-based). For selected pages:

```bash
"$P" -c 'import json,sys,pymupdf4llm; print(json.dumps(pymupdf4llm.to_markdown(sys.argv[1], pages=[int(n)-1 for n in sys.argv[2:]], page_chunks=True, use_ocr=False)))' "$PDF" 5 6
```

Match chunks by `metadata.page_number` (1-based), not return order.
Add `table_output="html"` inside the API call when needed; never pass page
lists through CLI `--opt`. Python page lists are 0-based.

**OCR.** Check `tesseract --list-langs`; use only installed text languages
(`osd` is orientation detection). For a rendered image, change PSM as above;
append `tsv` for word boxes, `hocr` for positioned HTML, or `pdf` for a searchable
image PDF. For files, replace `stdout` with an output basename; Tesseract adds
the extension. Use a file basename for PDF output, not binary terminal output.
Combine languages with `-l eng+deu` only if both are installed.
Confidence is not proof of correct numbers.

```bash
OMP_THREAD_LIMIT=2 /usr/bin/tesseract "$OUT/page-5.png" stdout -l eng --psm 3
OMP_THREAD_LIMIT=2 /opt/document-tools/ocr/bin/ocrmypdf \
  --no-overwrite --skip-text --output-type pdf --optimize 0 \
  --jobs 2 --tesseract-timeout 120 -l eng "$PDF" "$OUT/searchable.pdf"
```

Add `--pages 5-6` to limit OCR; other pages remain in the output. Read the
resulting PDF, not just a sidecar. Check for timeouts or unrecognized regions.
Do not rasterize clean text with `--force-ocr` as a routine fallback.

**Native rows / tables.** Use `"$P"` to import `pymupdf` or `pdfplumber` and
open the source path with `pymupdf.open(path)` or `pdfplumber.open(path)`.
For a 1-based `page_number`, select `doc[page_number-1]` or
`doc.pages[page_number-1]` respectively. Coordinates below are measured PDF
points from the top-left of this source:

- PyMuPDF: `page.get_text("text", clip=pymupdf.Rect(x0,y0,x1,y1), sort=True)`.
  Clip the row and its header/unit region separately; do not cut through text.
- pdfplumber: `body = page.crop((x0,top,x1,bottom))`; try
  `body.extract_tables()` for ruled tables, or `{"vertical_strategy":"text",
  "horizontal_strategy":"text"}` settings for unruled aligned text.
- If columns still merge, set `boundaries` to measured column-edge x positions:
  `body.extract_tables({"vertical_strategy":"explicit",
  "explicit_vertical_lines":boundaries,"horizontal_strategy":"text"})`.
  Inspect `body.debug_tablefinder(settings).edges` with that same settings
  dictionary if outer columns disappear:
  vertical boundaries must intersect horizontal edges. Never reuse another
  source's coordinates. Retain headers, units and graphical notes separately.
- For joined markers: `page.extract_words(extra_attrs=["size"])` and
  `page.chars` expose size and position; preserve the marker's note association.
- For a visual table diagnostic, use
  `body.to_image(resolution=300).debug_tablefinder(settings).save(output_png)`
  with the same settings dictionary and a chosen output path.
- pdfplumber does not OCR; use a searchable OCR derivative for scanned text,
  then verify its characters and table structure against the original.

**Complex layout.** Start without OCR for clean digital pages:

```bash
HF_HUB_OFFLINE=1 OMP_NUM_THREADS=2 /opt/document-tools/docling/bin/docling convert "$PDF" \
  --from pdf --to md --to json --pipeline standard --no-ocr \
  --ocr-engine tesseract --ocr-lang eng --device cpu --num-threads 2 \
  --page-batch-size 1 --table-mode accurate --page-range 5-6 \
  --artifacts-path /opt/document-tools/models/docling \
  --image-export-mode placeholder --abort-on-error --output "$OUT"
```

For image text, remove `--no-ocr`; use `--ocr-mode full_page` only if selective
OCR misses a needed region. Inspect JSON `tables`, `texts`, table `footnotes`
and picture `children`; `prov` maps content to source pages/boxes. Markdown
can omit these. Recovered chart words alone do not establish their associations.

## Verification -- PASS / HALT

PASS before using results: required pages/rows are present; each material value
matches its label, sign, decimal, unit, period and note in the source. Preserve
chart legends, graphical qualifiers and physical-page/printed-label mapping;
follow referenced notes/continuations. Verify all intended fields affected by
an adjustment, not just the repaired target. Then use the verified result.

HALT the correctness/completeness claim for missing content, timeouts, ambiguous
columns or unverified/regressing values. Try the matching alternative above or
state the unresolved gap. Neither exit zero, JSON nor a plausible total is proof.
