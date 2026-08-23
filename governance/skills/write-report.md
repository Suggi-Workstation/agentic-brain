---
name: write-report
description: "Write a report: Executive Summary-Research-Methodology-Findings format with quality gates G1-G7, evaluation gate, and cross-links. Use when asked to write a report, research a topic, investigate a question, or produce structured findings."
user-invocable: true
disable-model-invocation: false
---

# Report Writing

## What This Skill Does

Guides writing a research report to the agentic-brain. This skill holds the
PROCEDURE (Feynman loop, read template, write, transfer, commit; the watcher pushes).
The format SPECIFICATION and the compliance checklist live in
`governance/template-reports.md` -- that file is the validator.
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

- [ ] Procedure completed (read template, write, transfer, commit) (PASS / HALT)
- [ ] Template read before writing: `template-reports.md` opened in step 4 and followed (PASS / HALT)
- [ ] `research/README.md` read with the template before writing (PASS / HALT)
- [ ] Prior work queried via `query-brain-vps`; superseded / implemented / resolved artifacts got their `status:` updated (PASS / HALT)
- [ ] File written to the VPS clone (`research/reports/`): directly by VPS agents, via SSH transfer by VPS-connected agents (PASS / HALT)
- [ ] Template validator gate: `template-reports.md` Report Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed on VPS clone as hermes; watcher pushes within 1 min (AHEAD: 0 verified) (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if a report is warranted

A report is warranted when multi-step research produces structured
findings that will be evaluated by another agent. The report must
include methodology and negative results. The report itself
carries no evaluation section -- evaluations are separate
artifacts that link back.

Before writing, query prior work with the `query-brain-vps`
skill: existing proposals, reports, evaluations, and insights on
the topic. If this artifact supersedes, implements, or resolves an
earlier one, that artifact's `status:` field is updated in the same
session (see `research/README.md`).

### 3. Read the format specification and the pipeline map

Read `governance/template-reports.md` BEFORE writing. ALSO read
`agentic-brain:research/README.md` -- the pipeline map. It tells
you where this artifact sits in the flow and which earlier
artifacts' `status:` fields change when this one lands. It defines
the Executive Summary-Research Question-Methodology-Findings-Discussion-
Conclusion format, frontmatter schema, and the complete Report Checklist.
That checklist is the format gate for this skill. Follow it exactly.

### 4. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the artifact

Write ONLY to the agentic-brain. NEVER leave artifacts in the workspace.

VPS agents (running on the server, no SSH): write directly to
`/srv/brain/agentic-brain/research/reports/<short-slug>.md` (your filesystem).

VPS-connected agents (remote machines, e.g. PC or laptop agents): write
locally (scratch), then transfer via the key door:

```bash
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /srv/brain/agentic-brain/research/reports/<short-slug>.md'
```

`<short-slug>`: kebab-case, max 60 chars, unique.
### 6. Commit on the VPS clone -- NO push

The watcher pushes within 1 min and reindexes. Verify after ~1 min:
`AHEAD: 0`, or a fresh push line in /srv/brain/logs/brain-pull.log.

VPS agents:

```bash
cd /srv/brain/agentic-brain && git add research/reports/<short-slug>.md && \
  git commit -m "report: <short-slug>" && echo COMMITTED
```

VPS-connected agents:

```bash
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'su - hermes -c "cd /srv/brain/agentic-brain && git add research/reports/<short-slug>.md && git commit -m \"report: <short-slug>\" && echo COMMITTED"'
```
## Related

- `governance/template-reports.md` -- format specification and compliance validator (Report Checklist, examples)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (reports require evaluation)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- `skills/write-reflection/SKILL.md` -- reflection writing (research produces IORs)
