---
name: write-report
description: "Write a report: Executive Summary-Research-Methodology-Findings format with quality gates G1-G7, evaluation history, and cross-links. Use when asked to write a report, research a topic, investigate a question, or produce structured findings."
user-invocable: true
disable-model-invocation: false
---

# Report Writing

## What This Skill Does

Guides writing a research report to the agentic-brain. This skill holds the
PROCEDURE (clone, Feynman loop, write, verify, commit, push, discard).
The format SPECIFICATION and the compliance checklist live in
`brain:governance/template-reports.md` -- that file is the validator.
This skill references its Report Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when the task involves structured multi-step research that
produces findings, methodology, and conclusions: investigating a
topic, answering a research question, or synthesizing evidence across
sources. Reports require at least one independent evaluation.

Skip for:
- Single-source summaries (those are IORs or library topics)
- Research that doesn't need methodology documentation
- Quick fact-checking

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (clone, read template, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Template read before writing: `template-reports.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written ONLY to /tmp/brain-rpt/research/reports/ (NOT the workspace) (PASS / HALT)
- [ ] Template validator gate: `template-reports.md` Report Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if a report is warranted

A report is warranted when multi-step research produces structured
findings that will be evaluated by another agent. The report must
include methodology, negative results, and an evaluation history.

### 3. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-rpt && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-rpt
```

### 4. Read the format specification -- the validator

Read `brain:governance/template-reports.md` BEFORE writing. It defines
the Executive Summary-Research Question-Methodology-Findings-Discussion-
Conclusion format, frontmatter schema, and the complete Report Checklist.
That checklist is the format gate for this skill. Follow it exactly.

### 4b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the report file

Write ONLY to the agentic-brain. NEVER write reports to the workspace.

Path: `/tmp/brain-rpt/research/reports/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.

### 6. Commit and push

```bash
cd /tmp/brain-rpt
git add -A
git diff --cached --stat
git -c user.name="<AGENT>" -c user.email="<AGENT>@suggi-workspace.dev" \
  commit -m "report: <short-slug>"
git push origin main
```

Replace `<AGENT>` with your agent name (e.g. Link, Ava). If the push
fails, pull first, resolve, then push.

### 7. Discard the clone

```bash
cd /tmp && rm -rf brain-rpt
```

## Related

- `brain:governance/template-reports.md` -- format specification and compliance validator (Report Checklist, examples)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (reports require evaluation)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- `skills/write-reflection/SKILL.md` -- reflection writing (research produces IORs)
