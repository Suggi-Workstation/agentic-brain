---
name: write-report
description: "Write a report: Executive Summary-Research-Methodology-Findings format with quality gates G1-G7, evaluation history, and cross-links. Use when asked to write a report, research a topic, investigate a question, or produce structured findings."
user-invocable: true
disable-model-invocation: false
---

# Report Writing

## What This Skill Does

Guides writing a research report to the agentic-brain. Procedure steps
cover the mechanics (clone, write, commit, discard). Format verification
checkboxes cover correctness (frontmatter, body structure, quality
gates, output). For the full format specification with examples, read
`brain:governance/template-reports.md`.

## When to Invoke

Invoke when the task involves structured multi-step research that
produces findings, methodology, and conclusions: investigating a
topic, answering a research question, or synthesizing evidence across
sources. Reports require at least one independent evaluation (G1).

Skip for:
- Single-source summaries (those are IORs or library topics)
- Research that doesn't need methodology documentation
- Quick fact-checking

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Version History Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `template-reports.md` Checklist: all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Determine if a report is warranted

A report is warranted when multi-step research produces structured
findings that will be evaluated by another agent. The report must
include methodology, negative results, and an evaluation history.

### 2. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-rpt && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-rpt
```

### 3. Read the format specification

Read `brain:governance/template-reports.md`. It defines the
Executive Summary-Research Question-Methodology-Findings-Discussion-
Conclusion format, frontmatter schema (6 fields), quality gates
(G1-G7), and examples. Follow it exactly.

### 3b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 4. Write the report file

Write ONLY to the agentic-brain. NEVER write reports to the workspace.

Path: `/tmp/brain-rpt/research/reports/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to the template. HALT on any failure;
fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "report" (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)
- [ ] links: relative paths from brain root (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Executive Summary: research question + answer + key evidence + confidence. Stands alone (G2) (PASS / HALT)
- [ ] Research Question: falsifiable, scoped (in/out clearly stated) (PASS / HALT)
- [ ] Methodology: reproducible, sources have retrieval dates, tools/parameters named, limitations stated (G3) (PASS / HALT)
- [ ] Findings: each with claim + evidence + confidence (PASS / HALT)
- [ ] Negative results: what was searched for and NOT found (G4) (PASS / HALT)
- [ ] Discussion: synthesizes findings, addresses surprises (PASS / HALT)
- [ ] Conclusion: restates question + answer + one recommendation + open questions (PASS / HALT)
- [ ] Evaluation History: at least one independent evaluation linked (APPROVE or APPROVE WITH CHANGES resolved) (G1) (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Independently Evaluated): at least one independent evaluation, verdict APPROVE or APPROVE WITH CHANGES (PASS / HALT)
- [ ] G2 (Executive Summary Stands Alone): a reader who only reads the executive summary gets the research question, the answer, the key evidence, and the confidence level (PASS / HALT)
- [ ] G3 (Methodology Is Reproducible): another agent could reproduce the research approach from the methodology section alone. Sources have retrieval dates. Tools and parameters are named (PASS / HALT)
- [ ] G4 (Negative Results Included): what was searched for and NOT found is documented alongside what was found (PASS / HALT)
- [ ] G5 (Cross-links): evaluations + related reports + referenced library topics linked (PASS / HALT)
- [ ] G6 (Frontmatter Complete): all 6 fields present (name, id, tier, author, tags, links) (PASS / HALT)
- [ ] G7 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### Version History Sub-Checklist (ONLY if version-history table was added)

- [ ] Version-history table: present and correct (date + author + change rows) if file has version updates; omitted for single-version files (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-rpt/research/reports/ (NOT workspace) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G7) (PASS / HALT)

### 5. Commit and push

```bash
cd /tmp/brain-rpt
git add -A
git diff --cached --stat
git -c user.name="Ava" -c user.email="ava@suggi-workspace.dev" \
  commit -m "report: <short-slug>"
git push origin main

If the push fails, pull first, resolve, then push.
```

### 6. Discard the clone

```bash
cd /tmp && rm -rf brain-rpt
```

## Related

- `brain:governance/template-reports.md` -- full format, examples, quality gates
- `skills/write-evaluation/SKILL.md` -- evaluation writing (reports require evaluation, G1)
- `skills/write-reflection/SKILL.md` -- reflection writing (research produces IORs)
