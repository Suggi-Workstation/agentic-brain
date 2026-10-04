---
name: write-reflection
description: "Use when writing or updating a reflection. IOR format per the reflection template."
user-invocable: true
disable-model-invocation: false
---

# Reflection Writing

## What This Skill Does

Guides writing a reflection (IOR) to the agentic-brain. This skill holds
the PROCEDURE (clone, Feynman loop, write, verify, commit, push, discard).
The format SPECIFICATION and the compliance checklist live in
`governance/template-reflections.md` -- that file is the validator.
This skill references its Reflection Checklist as the format gate and does
not restate its items (R8: reference, never duplicate).

## When to Invoke

Invoke when writing or updating a reflection.

## Final Self-Check -- HARD GATE

Confirm ALL items before committing.

- [ ] Procedure completed (clone, read template, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Template read before writing: `template-reflections.md` opened in step 3 and followed (PASS / HALT)
- [ ] File written ONLY to /tmp/brain-reflection/reflections/ (NOT the workspace) (PASS / HALT)
- [ ] Template validator gate: `template-reflections.md` Reflection Checklist -- all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Run the Feynman Loop

Before any research or writing, invoke the `loop-feynman` skill.
Complete every step. The blank page (Step 1) MUST precede any
source consultation (Step 3). See `skills/loop-feynman/SKILL.md`
for the full procedure and self-check.

### 2. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-reflection && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-reflection
```

### 3. Read the format specification -- the validator

Read `governance/template-reflections.md` BEFORE writing. It defines
the I/O/R format, frontmatter schema, naming convention, and the complete
Reflection Checklist. That checklist is the format gate for this skill.
Follow it exactly.

### 3b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 4. Write the reflection file

Write ONLY to the agentic-brain. NEVER write reflections to the workspace.

Path: `/tmp/brain-reflection/reflections/YYYY-MM-DD_author_slug.md`

- `YYYY-MM-DD`: local date of original publication. Never change on
  version updates.
- `author`: lowercase agent name (ava, link, zelda, luffy, suggi).
- `slug`: kebab-case title, max 60 chars.

### 5. Commit and push

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

### 6. Discard the clone

```bash
cd /tmp && rm -rf brain-reflection
```

## Related

- `governance/template-reflections.md` -- format specification and compliance validator (Reflection Checklist, examples, anti-patterns)
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (produces material for reflections)
- `skills/session-end/SKILL.md` -- session-end calls this skill
