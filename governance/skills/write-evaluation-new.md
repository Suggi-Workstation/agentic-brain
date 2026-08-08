---
name: write-evaluation-new
description: "Write an evaluation: Source-Criteria-Findings-Verdict format with quality gates G1-G8, decorrelation rule, and cross-links. Use when asked to evaluate, review, scrutinize, or perform independent review of an agent's work."
user-invocable: true
disable-model-invocation: false
---

# Evaluation Writing

## What This Skill Does

Guides writing an independent evaluation to the agentic-brain. This skill
holds the PROCEDURE (clone, Feynman loop, write, verify, commit, push,
discard). The format SPECIFICATION and the compliance checklist live in
`brain:governance/template-evaluations.md` -- that file is the validator.
This skill references its Evaluation Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when the task involves evaluating another agent's work: a
proposal, report, or insight needs independent scrutiny. The
decorrelation rule requires a different agent (or model family) than
the original author.

Skip for:
- Your own work (violates decorrelation rule)
- Work already evaluated with APPROVE verdict
- Minor formatting fixes

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (clone, read template, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Template read before writing: `template-evaluations.md` opened in step 4 and followed (PASS / HALT)
- [ ] File written ONLY to /tmp/brain-eval/research/evaluations/ (NOT the workspace) (PASS / HALT)
- [ ] Template validator gate: `template-evaluations.md` Evaluation Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if an evaluation is warranted

An evaluation is warranted when another agent has produced a proposal,
report, or insight that requires independent review. Confirm the
decorrelation rule: you are NOT the original author.

### 3. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-eval && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-eval
```

### 4. Read the format specification -- the validator

Read `brain:governance/template-evaluations.md` BEFORE writing. It defines
the Source-Criteria-Findings-Verdict format, frontmatter schema, and the
complete Evaluation Checklist. That checklist is the format gate for this
skill. Follow it exactly.

### 4b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the evaluation file

Write ONLY to the agentic-brain. NEVER write evaluations to the
workspace.

Path: `/tmp/brain-eval/research/evaluations/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.
Example: `ava-review-link-verification-paper.md`

### 6. Commit and push

```bash
cd /tmp/brain-eval
git add -A
git diff --cached --stat
git -c user.name="<AGENT>" -c user.email="<AGENT>@suggi-workspace.dev" \
  commit -m "evaluation: <short-slug>"
git push origin main
```

Replace `<AGENT>` with your agent name (e.g. Link, Ava). If the push
fails, pull first, resolve, then push.

### 7. Discard the clone

```bash
cd /tmp && rm -rf brain-eval
```

## Related

- `brain:governance/template-evaluations.md` -- format specification and compliance validator (Evaluation Checklist, examples)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (prerequisite for all artifact writing)
- `skills/write-report/SKILL.md` -- report writing (reports require evaluation)
