---
name: write-insight
description: "Write an insight: Insight-Evidence-Implications-Counter-evidence format with quality gates G1-G8, falsifiability, and cross-links. Use when asked to write an insight, capture a pattern, synthesize a finding, or distill a realization."
user-invocable: true
disable-model-invocation: false
---

# Insight Writing

## What This Skill Does

Guides writing an insight to the agentic-brain. Procedure steps cover
the mechanics (clone, write, commit, discard). Format verification
checkboxes cover correctness (frontmatter, body structure, quality
gates, output). For the full format specification with examples, read
`brain:governance/template-insights.md`.

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

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Version History Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `template-insights.md` Checklist: all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Determine if an insight is warranted

An insight is warranted when a pattern emerges across multiple
artifacts that can be distilled into one quotable sentence. It must
be falsifiable (the counter-evidence section must state what would
prove it wrong).

### 2. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-ins && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-ins
```

### 3. Read the format specification

Read `brain:governance/template-insights.md`. It defines the
Insight-Evidence-Implications-Counter-evidence format, frontmatter
schema (7 fields including source), quality gates (G1-G8), and
examples. Follow it exactly.

### 3b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 4. Write the insight file

Write ONLY to the agentic-brain. NEVER write insights to the workspace.

Path: `/tmp/brain-ins/research/insights/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to the template. HALT on any failure;
fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "insight" (PASS / HALT)
- [ ] source: links to every originating IOR, report, or evaluation by id (G5) (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)
- [ ] links: relative paths from brain root (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] The Insight: one quotable sentence (G1). If it takes a paragraph, it is not yet an insight (PASS / HALT)
- [ ] Evidence: at least one source cited by id, chain of evidence complete (G2) (PASS / HALT)
- [ ] Implications: concrete ("changes X" or "informs decision Y"), not platitudes (G3) (PASS / HALT)
- [ ] Counter-evidence: states what would prove the insight wrong (G4). Cannot falsify = dogma (PASS / HALT)
- [ ] Version history: at minimum, a v1 row with date + author + change (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (One-sentence): core realization fits in one quoted line (PASS / HALT)
- [ ] G2 (Evidence Is Cited): at least one specific source cited by id. (PASS / HALT)
- [ ] G3 (Implications Are Concrete): concrete implications cited, so that another agent knows what to do differently (PASS / HALT)
- [ ] G4 (Falsifiable): counter-evidence explicitly states what would prove it wrong (PASS / HALT)
- [ ] G5 (Source Traceability): the source: field in frontmatter links to every originating IOR, report, or evaluation. (PASS / HALT)
- [ ] G6 (Cross-links Exist): source artifacts + related insights + affected governance linked (PASS / HALT)
- [ ] G7 (Frontmatter Complete): all 7 fields present (name, id, tier, source, author, tags, links) (PASS / HALT)
- [ ] G8 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### Version History Sub-Checklist (ONLY if version-history table was added)

- [ ] Version-history table: present and correct (date + author + change rows) if file has version updates; omitted for single-version files (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-ins/research/insights/ (NOT workspace) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G8) (PASS / HALT)

### 5. Commit and push

```bash
cd /tmp/brain-ins
git add -A
git diff --cached --stat
git -c user.name="Ava" -c user.email="ava@suggi-workspace.dev" \
  commit -m "insight: <short-slug>"
git push origin main

If the push fails, pull first, resolve, then push.
```

### 6. Discard the clone

```bash
cd /tmp && rm -rf brain-ins
```

## Related

- `brain:governance/template-insights.md` -- full format, examples, quality gates
- `skills/write-report/SKILL.md` -- report writing (reports produce insights)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (evaluations identify patterns)
