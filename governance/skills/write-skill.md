---
name: write-skill
description: "Design and construct new OpenClaw skills for reusable workflows, procedures, and protocols. Use when asked to create a skill, build a skill, design a skill, write a SKILL.md, or construct a reusable procedure."
user-invocable: true
disable-model-invocation: false
---

# Write Skill

## What This Skill Does

Guides designing and building a new OpenClaw skill. Procedure steps cover
the mechanics (decision flow, design, build, test). Format verification
checkboxes cover correctness (constitutional, frontmatter, body, output).
For the full skill specification with frontmatter schema, gating fields,
anti-patterns, and quality gates, read `brain:governance/template-skills.md`.

## When to Invoke

This skill is for designing and drafting a skill collaboratively BEFORE
submission. The deployment path depends on the change:

- **New skills or major redesigns:** submit the final draft through Skill
  Workshop for Suggi's review and approval. Workshop is the deployment
  gate -- it prevents unreviewed skills from going live.
- **Minor edits to existing skills:** use the `edit` tool directly on
  the SKILL.md file. No workshop needed for wording fixes, typo
  corrections, or small procedural tweaks.

Skip for:
- Questions about skill format (read `brain:governance/template-skills.md`)
- Trivial one-line instruction (inline in AGENTS.md, not a skill)

## Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (decision flow, spec read, create, build, test) (PASS / HALT)
- [ ] Design Decisions verification: all items confirmed PASS (PASS / HALT)
- [ ] Frontmatter verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure verification: all items confirmed PASS (PASS / HALT)
- [ ] Testing verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output verification: all items confirmed PASS (PASS / HALT)
- [ ] Template Skill Checklist: all items confirmed PASS (PASS / HALT)
- [ ] Skill committed and pushed (PASS / HALT)

## Procedure

### 1. Run the decision flow

Before building, confirm a skill is the right solution. HALT if any
check says "no skill needed."

- Constitutional content? (gate rules, identity, principles) -> stays
  in AGENTS.md. Do not skill.
- Under ~500 chars? -> inline, not a skill.
- One-off work? -> does not need a skill.
- Existing skill covers this? -> reuse, do not duplicate.
- Governance template defines the format? -> reference it, do not
  duplicate (R8, G5).

### 2. Read the skill specification

Read `brain:governance/template-skills.md`. It defines frontmatter
schema, body structure, naming convention, quality gates (G1-G8), and
the 14-item Skill Checklist.

### 2b. Know the ID rule (for write-X skills)

If the skill being built is a write-X skill, the builder MUST include
both a procedure step AND a Format Verification item for ID generation.
The procedure step runs `date -u +'%Y%m%dT%H%M%SZ'` and pastes the
exact output. The verification item checks the output and flags
human-rounded timestamps (ending in 000000Z). These are permanent,
unfixable errors -- the verification gate must catch them.
Never type an ID by hand.

### 3. Create the directory and design the frontmatter

Create the skill directory:

```bash
mkdir -p ~/.openclaw/workspace/skills/<skill-name>
```

Write the YAML frontmatter in `skills/<skill-name>/SKILL.md`. Follow
the schema from `brain:governance/template-skills.md`:

- `name`: lowercase kebab-case, matches folder name. Also the slash
  command: `/name`.
- `description`: task-oriented instruction fragment, under 160 chars,
  includes trigger phrases. This is the trigger surface -- the model
  matches it against the current task to decide whether to invoke.
- `user-invocable`: true for user skills (slash command), false for
  protocol skills (AGENTS.md triggered only).
- `disable-model-invocation`: false for normal skills (model can
  auto-trigger), true only for rarely-needed utilities.
- `metadata.openclaw.requires`: gating only on hard dependencies
  (bins, env vars, config). Do not gate on soft preferences.

Output destination: `~/.openclaw/workspace/skills/<skill-name>/SKILL.md`.

### 4. Build the SKILL.md body

Write the body sections in `~/.openclaw/workspace/skills/<skill-name>/SKILL.md`
following the hybrid pattern from template-skills.md. The standard
section order is:

1. `# Skill Name` -- level-1 heading matching frontmatter name.
2. `## Hard Gate (RX)` -- only for protocol skills. State which
   AGENTS.md instruction triggers this skill.
3. `## What This Skill Does` -- one paragraph. Reference any brain
   template that defines the format.
4. `## When to Invoke` -- trigger conditions + explicit skip conditions.
5. `## Self-Check -- HARD GATE` -- confirms all verification sections
   passed. References section names, not individual items.
6. `## Procedure` -- numbered steps. Each step: actionable
   (copy-pasteable command or checkable condition), verifiable (can
   tell pass/fail), non-overlapping (one thing per step).
7. `## Format Verification -- HARD GATE (before commit)` -- for
   write-X skills only: `- [ ]` checkboxes organized by category
   (Frontmatter, Body Structure, Quality Gates, Version History,
   File Output). Protocol skills may have a simpler verification
   section.
8. `## Related` -- links to brain template + related skills.

Progressive disclosure check: what stays in the SKILL.md body vs what
goes in `references/`? Detailed checklists, long code examples, and
supplementary documentation belong in `references/` loaded on demand.
The SKILL.md body stays lean -- procedure only. Reference the template;
never inline format specifications (G5).

Output destination: `~/.openclaw/workspace/skills/<skill-name>/SKILL.md`.

### 5. Test the skill

Run these checks from the skill directory:

```bash
cd ~/.openclaw/workspace/skills/<skill-name>
```

- **Load check:** `openclaw skills list | grep <name>` -- skill must
  appear in the list.
- **ASCII check:** `grep -Pn '[^\x00-\x7F]' SKILL.md` returns nothing.
  CI enforces this via `ascii-guard.yml`, but verify locally first.
- **Walk-through:** can the agent execute every step from SKILL.md
  alone? No missing commands, no ambiguous instructions.
- **Trigger test:** in a new session, test the description against
  multiple phrasings of the same task. Does the model consistently
  invoke the skill? If not, strengthen the description's trigger
  phrases.
- **Boundary test:** confirm skip conditions actually prevent
  invocation when they should. Test a case that SHOULD skip.

If the skill is a protocol skill (AGENTS.md triggered), also verify
step 6 was completed -- the AGENTS.md gate instruction exists and
references the skill by name.

### 6. Update AGENTS.md (protocol skills only)

If the skill is auto-triggered by AGENTS.md, add a `-- HARD GATE`
gate instruction referencing it. Without this, protocol skills are
orphaned. Skip for user-invocable skills -- description matching or
slash command is sufficient.

### 7. Write an IOR if a durable insight emerged

If building this skill surfaced a new pattern not yet in template-skills.md,
write an IOR. Propose updating the template if the insight is general.

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the template. HALT on any failure;
fix before committing.

### Design Decisions

- [ ] NOT constitutional content (gate rules, identity, hard rules stay in AGENTS.md) (PASS / HALT)
- [ ] Exceeds ~500 chars (one-liners stay inline) (PASS / HALT)
- [ ] Repeats across sessions (one-off work does not need a skill) (PASS / HALT)
- [ ] No duplicate: existing skill or template does not already cover this (PASS / HALT)

### Frontmatter

- [ ] name: lowercase kebab-case, matches folder name (PASS / HALT)
- [ ] description: task-oriented instruction fragment, under 160 chars, includes "Use when" trigger phrases (PASS / HALT)
- [ ] user-invocable: correctly set (true for user skills, false for protocol) (PASS / HALT)
- [ ] disable-model-invocation: correctly set (false for normal skills, true only for rarely-needed utilities) (PASS / HALT)

### Body Structure

- [ ] What This Skill Does: present, one paragraph, references template if one exists (PASS / HALT)
- [ ] When to Invoke: trigger conditions and skip conditions clearly stated (PASS / HALT)
- [ ] Procedure: every step actionable (copy-pasteable command or checkable condition) (PASS / HALT)
- [ ] Format Verification section present (for write-X skills): `- [ ]` checkboxes between "write" and "commit" organized by category (PASS / HALT)

### Testing

- [ ] Load check passed: `openclaw skills list | grep <name>` returns the skill (PASS / HALT)
- [ ] ASCII check passed: zero non-ASCII characters in SKILL.md (PASS / HALT)
- [ ] Walk-through passed: every procedure step executable from description alone (PASS / HALT)
- [ ] Trigger test passed: description matches trigger intent with varied phrasings; boundary test confirms skip conditions prevent invocation when they should (PASS / HALT)

### File Output

- [ ] G5 (No Duplicate Governance): no format definitions, quality gates, or checklists duplicated from brain template. Uses `brain:` references (PASS / HALT)
- [ ] Self-Check: `-- HARD GATE` header, confirms verification sections by name, does not duplicate individual items (PASS / HALT)
- [ ] Related: links to brain governance template + related skills (PASS / HALT)
- [ ] AGENTS.md updated with `-- HARD GATE` instruction (protocol skills only) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (PASS / HALT)
- [ ] Skill loads correctly: `openclaw skills list` shows it (PASS / HALT)
- [ ] All output destinations explicit (G8): every file-producing step states the exact path (PASS / HALT)

### Commit and push

```bash
cd ~/.openclaw/workspace
git add skills/<skill-name>/SKILL.md
git commit -m "skills/<skill-name>: <description>"
git push origin main
```

## Related

- `brain:governance/template-skills.md` -- full skill specification, frontmatter schema, quality gates G1-G8, 14-item Skill Checklist
- `skills/write-reflection/SKILL.md` -- example of hybrid format for write-X skills
- `skills/preflight/SKILL.md` -- example of a well-structured protocol skill
