---
name: write-reflection-new
description: "Write a reflection (IOR): Idea-Opinion-Reflection format with quality gates G1-G9, one actionable change, and cross-links. Use when asked to write a reflection, reflect on a topic, or capture a durable insight."
user-invocable: true
disable-model-invocation: false
---

# Reflection Writing

> DRAFT REVISION (2026-08-08) -- proposed update to `write-reflection.md`.
> This file is for comparison only; NOT canonical until Suggi approves.
> Changes: procedure-only skill (research-backed: skills = HOW, templates =
> WHAT); format compliance restatements removed; template's Reflection
> Checklist is the single format gate; execution-only checks retained.

## What This Skill Does

Guides writing a reflection (IOR) to the agentic-brain. This skill holds
the PROCEDURE (clone, Feynman loop, write, verify, commit, push, discard).
The format SPECIFICATION and the compliance checklist live in
`brain:governance/template-reflections.md` -- that file is the validator.
This skill references its Reflection Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when the task involves writing or updating a reflection. A reflection is
warranted when a session produces a durable insight:

- The Feynman Loop revealed a gap you did not know you had.
- An error revealed a failure class not yet gated against.
- Research produced a conclusion that contradicts or extends existing
  brain knowledge.
- A structural change was made that other agents should know about.

Skip when the session produced only logs (memory/YYYY-MM-DD.md), status
updates, or insights already captured in an existing reflection (update the
existing one instead -- see template versioning rules).

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, read template, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Execution Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Template validator gate: `template-reflections.md` Reflection Checklist -- all 15 items confirmed PASS (covers frontmatter schema/rules, id generation, I/O/R structure, Schoen budget, version-history position, cross-links, filename, ASCII, G1-G9) (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete all 6 steps. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Determine if a reflection is warranted

See "When to Invoke" above. If no durable insight emerged, skip reflection
writing entirely. Do not write a forced reflection to check a box.

### 3. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-reflection && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-reflection
```

### 4. Read the format specification -- the validator

Read `brain:governance/template-reflections.md` BEFORE writing. It defines
the I/O/R format, frontmatter schema, naming convention, and the 15-item
Reflection Checklist (quality gates G1-G9 included). That checklist is the
format gate for this skill. Follow it exactly.

### 4b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 5. Write the reflection file

Write ONLY to the agentic-brain. NEVER write reflections to the workspace.

Path: `/tmp/brain-reflection/reflections/YYYY-MM-DD_author_slug.md`

- `YYYY-MM-DD`: local date of original publication. Never change on
  version updates.
- `author`: lowercase agent name (ava, link, zelda, luffy, suggi).
- `slug`: kebab-case title, max 60 chars.

## Execution Sub-Checklist -- HARD GATE (before commit)

Verify every item below. These are EXECUTION checks -- they confirm the
procedure was followed, not the artifact's format. Format compliance is
gated by the template's Reflection Checklist (Final Self-Check item 3).
HALT on any failure; fix before committing.

- [ ] Template read before writing: `template-reflections.md` opened in step 4 and followed (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] File written ONLY to /tmp/brain-reflection/reflections/ (NOT the workspace) (PASS / HALT)

### 6. Commit and push

```bash
cd /tmp/brain-reflection
git add -A
git diff --cached --stat
git -c user.name="<AGENT>" -c user.email="<AGENT>@suggi-workspace.dev" \
  commit -m "reflection: <short-slug>"
git push origin main
```

Replace `<AGENT>` with your agent name (e.g. Link, Ava). If the push
fails, pull first, resolve, then push.

### 7. Discard the clone

```bash
cd /tmp && rm -rf brain-reflection
```

## Related

- `brain:governance/template-reflections.md` -- format specification and compliance validator (Reflection Checklist, G1-G9, examples, anti-patterns)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (produces material for reflections)
- `skills/session-end/SKILL.md` -- session-end calls reflection writing when insight emerged
