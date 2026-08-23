---
name: write-insight
description: "Write an insight: Insight-Evidence-Implications-Counter-evidence format with quality gates G1-G8, falsifiability, and cross-links. Use when asked to write an insight, capture a pattern, synthesize a finding, or distill a realization."
user-invocable: true
disable-model-invocation: false
---

# Insight Writing

## What This Skill Does

Guides writing an insight to the agentic-brain. This skill holds the
PROCEDURE (clone, Feynman loop, write, verify, commit, push, discard).
The format SPECIFICATION and the compliance checklist live in
`governance/template-insights.md` -- that file is the validator.
This skill references its Insight Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when the task involves capturing a cross-artifact pattern or
distilling a realization: multiple IORs, reports, or evaluations
point to the same conclusion. An insight is a one-sentence core
realization with evidence chain, implications, and falsifiability.

Skip for:
- Single-artifact observations (those are IORs or report findings)
- Unsourced opinions
- Patterns already documented in an existing insight

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (clone, read template, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Template read before writing: `template-insights.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written ONLY to /tmp/brain-ins/research/insights/ (NOT the workspace) (PASS / HALT)
- [ ] Template validator gate: `template-insights.md` Insight Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if an insight is warranted

An insight is warranted when a pattern emerges across multiple
artifacts that can be distilled into one quotable sentence. It must
be falsifiable (the counter-evidence section must state what would
prove it wrong).

### 3. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-ins && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-ins
```

### 4. Read the format specification -- the validator

Read `governance/template-insights.md` BEFORE writing. It defines
the Insight-Evidence-Implications-Counter-evidence format, frontmatter
schema, and the complete Insight Checklist. That checklist is the format
gate for this skill. Follow it exactly.

### 4b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the insight file

Write ONLY to the agentic-brain. NEVER write insights to the workspace.

Path: `/tmp/brain-ins/research/insights/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.

### 6. Commit and push

```bash
cd /tmp/brain-ins
git add -A
git diff --cached --stat
git -c user.name="<AGENT>" -c user.email="<AGENT>@suggi-workspace.dev" \
  commit -m "insight: <short-slug>"
git push origin main
```

Replace `<AGENT>` with your agent name (e.g. Link, Ava). If the push
fails, pull first, resolve, then push.

### 7. Discard the clone

```bash
cd /tmp && rm -rf brain-ins
```

## Related

- `governance/template-insights.md` -- format specification and compliance validator (Insight Checklist, examples)
- `skills/write-report/SKILL.md` -- report writing (reports produce insights)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (evaluations identify patterns)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
