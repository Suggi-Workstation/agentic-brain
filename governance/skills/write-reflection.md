---
name: write-reflection
description: "Write a reflection (reflection): Idea-Opinion-Reflection format with quality gates G1-G9, one actionable change, and cross-links. Use when asked to write a reflection, write a reflection, reflect on a topic, or capture a durable insight."
user-invocable: true
disable-model-invocation: false
---

# Reflection Writing

## What This Skill Does

Guides writing a reflection (reflection) to the agentic-brain. Procedure steps
cover the mechanics (clone, write, commit, discard). Format verification
checkboxes cover correctness (frontmatter, body structure, quality gates, output). For the
full format specification with examples and anti-patterns, read
`brain:governance/template-reflections.md`.

## When to Invoke

Invoke when the task involves writing or updating a reflection. An reflection is
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

- [ ] Procedure completed (clone, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Version History Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `template-reflections.md` Checklist: all items confirmed PASS (for new reflections)  (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Determine if a reflection is warranted

See "When to Invoke" above. If no durable insight emerged, skip reflection
writing entirely. Do not write a forced reflection to check a box.

### 2. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-reflection && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-reflection
```

### 3. Read the format specification

Read `brain:governance/template-reflections.md`. It defines the I/O/R
format, frontmatter schema, naming convention, quality gates (G1-G9),
and examples. Follow it exactly.

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

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to the template. HALT on any failure;
fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "reflection" (PASS / HALT)
- [ ] trigger: one of {session-end, error, surprise, milestone, decision, research, insight, self-knowledge} (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags (PASS / HALT)
- [ ] links: relative paths from brain root (e.g. governance/..., research/...). NOT the `brain:` prefix (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Section headers: `#` = title only, `##` = I/O/R sections, `###` = sub-sections within R (PASS / HALT)
- [ ] Title makes a claim (G1): something someone can agree or disagree with (PASS / HALT)
- [ ] `## I -- Idea`: one-sentence idea + context. Reader understands what triggered this (G2) (PASS / HALT)
- [ ] `## O -- Opinion`: clear position + confidence with percentage (high 85%+ / medium 60-85% / low below 60%) (G3) (PASS / HALT)
- [ ] `## R -- Reflection` with `### Surprise (30%)`, `### Feel (30%)`, `### Learn (40%)` (G4) (PASS / HALT)
- [ ] Surprise answers "I expected X, but Y happened" (PASS / HALT)
- [ ] One actionable change: concrete, structural, another agent could execute (G5) (PASS / HALT)
- [ ] Cross-links: at least 1 link to Library/insight/other reflection (G6) (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Title Makes a Claim): the title is something someone can agree or disagree with. Not "Notes on X" -- that is a draft (PASS / HALT)
- [ ] G2 (I Section Completeness): a reader with no context understands what triggered this (PASS / HALT)
- [ ] G3 (O Section Has a Spine): a clear position, not just description. Cites a confidence level (PASS / HALT)
- [ ] G4 (R Section Has a Surprise): if nothing surprised you, the reflection is incomplete (PASS / HALT)
- [ ] G5 (Actionable Change Is Concrete): not "be better" or "pay attention." Another agent could execute it from the description alone (PASS / HALT)
- [ ] G6 (Cross-links Exist): at least one link to a Library topic, insight, or another reflection. (PASS / HALT)
- [ ] G7 (Feynman Pre-write): Feynman pass completed BEFORE writing (blank page first) (PASS / HALT)
- [ ] G8 (Frontmatter Complete): all 7 fields present (name, id, tier, trigger, author, tags, links) (PASS / HALT)
- [ ] G9 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### Version History Sub-Checklist (ONLY if version-history table was added)

- [ ] Version-history table: present and correct (date + author + change rows) if file has version updates; omitted for single-version files (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: YYYY-MM-DD_author_slug.md (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-reflection/reflections/ (NOT workspace) (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing (blank page first) (G7) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G9) (PASS / HALT)

### 5. Commit and push

```bash
cd /tmp/brain-reflection
git add -A
git diff --cached --stat
git -c user.name="Ava" -c user.email="ava@suggi-workspace.dev" \
  commit -m "reflection: <short-slug>"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 6. Discard the clone

```bash
cd /tmp && rm -rf brain-reflection
```

## Related

- `brain:governance/template-reflections.md` -- full format, examples, anti-patterns, quality gates
- `skills/loop-feynman/SKILL.md` -- Feynman Loop (produces material for reflections)
- `skills/session-end/SKILL.md` -- session-end calls reflection writing when insight emerged

