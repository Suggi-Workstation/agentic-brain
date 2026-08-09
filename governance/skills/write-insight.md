---
name: write-insight
description: "Write an insight: Insight-Evidence-Implications-Counter-evidence format with quality gates G1-G8, falsifiability, and cross-links. Use when asked to write an insight, capture a pattern, synthesize a finding, or distill a realization."
user-invocable: true
disable-model-invocation: false
---

# Insight Writing

## What This Skill Does

Guides writing an insight to the agentic-brain. This skill holds the
PROCEDURE (Feynman loop, read template, write, transfer, commit; the watcher pushes).
The format SPECIFICATION and the compliance checklist live in
`brain:governance/template-insights.md` -- that file is the validator.
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

- [ ] Procedure completed (read template, write, transfer, commit) (PASS / HALT)
- [ ] Template read before writing: `template-insights.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written to the VPS clone (`research/insights/`): directly by VPS agents, via SSH transfer by VPS-connected agents (PASS / HALT)
- [ ] Template validator gate: `template-insights.md` Insight Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed on VPS clone as hermes; watcher pushes within 1 min (AHEAD: 0 verified) (PASS / HALT)

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

### 3. Read the format specification -- the validator

Read `brain:governance/template-insights.md` BEFORE writing. It defines
the Insight-Evidence-Implications-Counter-evidence format, frontmatter
schema, and the complete Insight Checklist. That checklist is the format
gate for this skill. Follow it exactly.

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
`/srv/brain/agentic-brain/research/insights/<short-slug>.md` (your filesystem).

VPS-connected agents (remote machines, e.g. PC or laptop agents): write
locally (scratch), then transfer via the key door:

```bash
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /srv/brain/agentic-brain/research/insights/<short-slug>.md'
```

`<short-slug>`: kebab-case, max 60 chars, unique.
### 6. Commit on the VPS clone -- NO push

The watcher pushes within 1 min and reindexes. Verify after ~1 min:
`AHEAD: 0`, or a fresh push line in /srv/brain/logs/brain-pull.log.

VPS agents:

```bash
cd /srv/brain/agentic-brain && git add research/insights/<short-slug>.md && \
  git commit -m "insight: <short-slug>" && echo COMMITTED
```

VPS-connected agents:

```bash
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'su - hermes -c "cd /srv/brain/agentic-brain && git add research/insights/<short-slug>.md && git commit -m \"insight: <short-slug>\" && echo COMMITTED"'
```
## Related

- `brain:governance/template-insights.md` -- format specification and compliance validator (Insight Checklist, examples)
- `skills/write-report/SKILL.md` -- report writing (reports produce insights)
- `skills/write-evaluation/SKILL.md` -- evaluation writing (evaluations identify patterns)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
