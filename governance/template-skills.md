---
name: template-skills
id: 20260717T121600Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Ava
links:
  - governance/template-reflections.md
  - research/insights/rules-need-gates.md
  - research/insights/openclaw-manual.md
---

# Skill Template -- How We Write Agent Skills

A skill is a compact, triggerable workflow that lives in a directory
containing a `SKILL.md` file. Metadata (name, description, gating) is
always visible in the system prompt. The body loads only when the
agent invokes the skill. References, scripts, and assets load only
when needed.

## When to Create a Skill

Create a skill when:

- A procedure is used repeatedly across sessions (preflight, session-end).
- The procedure text exceeds ~500 chars -- moving it to a skill saves
  prompt overhead.
- The procedure benefits from independent versioning (not tied to AGENTS.md).
- The procedure could be shared across multiple agents.
- The procedure has its own scripts, templates, or reference materials.

Do NOT create a skill when:

- The content is constitutional (gate rules, principles, identity). These
  must stay in always-loaded bootstrap context.
- The content is a one-line instruction. A skill for "run `git status`" adds
  overhead with no benefit.
- The content is model-specific guidance that changes per provider. That
  belongs in model reference insights.
- The content is a checklist that is already defined in a governance template.
  Reference the template; do not duplicate it in a skill.

## The Constitution-vs-Procedure Rule

Skills carry procedures (HOW). AGENTS.md carries the constitution (WHAT,
WHEN, and HALT conditions). Never move gate enforcement into a skill.

**Correct:**
- AGENTS.md: "MUST invoke `/preflight` before any other action. R1: PASS or
  HALT. Do not proceed on HALT."
- Skill `preflight/SKILL.md`: The 8-step procedure, commands, and self-check
  table.

**Wrong:**
- Skill contains: "This skill must be run at session start." The skill cannot
  enforce this -- it has no lifecycle hooks. The enforcement must live in
  AGENTS.md.

Every skill depends on an AGENTS.md gate instruction. A skill without a
constitutional trigger is dead code.

## The Skill Loading Model

Skills load lazily. The system prompt receives only:

- **Name** (~20 chars)
- **Description** (~100 chars)
- **Location** (workspace, managed, bundled, plugin)

The full SKILL.md body loads when:
- The agent invokes the skill explicitly (`/skill-name`).
- The agent's current task description matches the skill's description
  (automatic trigger by the model).

This means the description is the skill's trigger surface. Write it to
maximize correct activation:

**Good description:** "Verify workspace mirror sync, context health, memory
index, and governance before every session."
-> Triggers on: preflight keywords, session startup, verification tasks.

**Bad description:** "A skill for running preflight checks."
-> Triggers on: nothing specific. Too generic.

## Global Formatting Rules

The entire GitHub org is plain 7-bit ASCII, lowercase, hyphen-delimited.
These rules are non-negotiable. CI enforces them.

- **ASCII-only:** Every character in every file is 7-bit ASCII (U+0000
  through U+007F). No emoji, no smart quotes, no Unicode dashes or
  arrows, no accented letters. The `ascii-guard.yml` CI gate fails the
  build on any violation.
- **Lowercase only:** All filenames, slugs, tags, domains, and folder
  names use lowercase exclusively. No CamelCase, no UPPERCASE, no
  mixed case.
- **Hyphens, not underscores:** Use hyphens (`-`) to separate words in
  filenames, slugs, and tags. Never use underscores (`_`).

## Frontmatter Schema

```yaml
---
name: <short-slug>                    # lowercase, kebab-case, unique. Skill name and slash-command.
description: "<one-line description>"  # quoted, one line, max 160 chars. The skill's trigger surface.
metadata:                              # optional, JSON5 object
  { "openclaw":
    {
      "requires": { ... },            # gating: bins, anyBins, env, config
      "primaryEnv": "<VAR_NAME>",     # primary env var for skills.entries.<name>.apiKey
      "emoji": "<X>",                 # macOS Skills UI icon
    }
  }
user-invocable: true                   # default true. Expose as slash command.
disable-model-invocation: false        # default false. When true, model cannot auto-trigger; only slash-command.
---
```

### Optional Frontmatter Keys

| Key | Type | Default | Purpose |
|---|---|---|---|
| `user-invocable` | boolean | `true` | Expose as user slash command `/skill-name` |
| `disable-model-invocation` | boolean | `false` | Prevent model from auto-triggering; only slash-command or AGENTS.md instruction |
| `command-dispatch` | `"tool"` | none | Route slash command directly to a tool, bypassing model |
| `command-tool` | string | none | Tool name for command-dispatch |
| `homepage` | string | none | URL shown in macOS Skills UI |

### Gating Fields (metadata.openclaw)

| Key | Type | Purpose |
|---|---|---|
| `requires.bins` | string[] | All binaries must exist on PATH |
| `requires.anyBins` | string[] | At least one binary must exist |
| `requires.env` | string[] | All env vars must exist |
| `requires.config` | string[] | Config paths must be truthy |
| `os` | string[] | Platform filter: `["darwin"]`, `["linux"]`, `["win32"]` |
| `always` | boolean | Skip all gates, always eligible |

## Frontmatter Rules

- `name` is a lowercase kebab-case slug, max 60 chars. Must be unique
  across all loaded skills. Also becomes the slash-command: `/name`.
- `description` is a quoted, one-line description, max 160 chars. This
  is the trigger surface seen by the model. Write it as a task-oriented
  instruction fragment that a model can match against the current task.
- `metadata` is a JSON5 object under the `"openclaw"` key. Use it for
  gating and UI metadata only. Do not use it for skill instructions.
- `user-invocable: false` hides the skill from slash-command discovery
  while keeping it available to the model. Use this for internal-only
  procedural skills that should be triggered by AGENTS.md, not by users.
- `disable-model-invocation: true` keeps the skill out of the system
  prompt entirely. It is only available via explicit slash-command.
  Use this for rarely-needed utility skills.
- **Combined:** `user-invocable: false` + `disable-model-invocation: false`
  (the default) is the correct setting for internal protocol skills
  (preflight, session-end, feynman-loop). The skill is visible in the
  available-skills list so AGENTS.md gate instructions can reference it
  efficiently, but users cannot accidentally trigger it as a slash command.
- `user-invocable: false` + `disable-model-invocation: true` makes the
  skill completely invisible -- no slash command, not in the prompt.
  The agent must use the `read` tool to manually load the SKILL.md file.
  Avoid this combination unless the skill must never be model-visible.

## Naming Convention

- **Skill folder:** The folder name is for organization only. The `name`
  frontmatter field is the canonical skill name. Keep folder and `name`
  aligned to avoid confusion.
- **File:** Always `SKILL.md` (uppercase, as required by OpenClaw).
- **Location:** Skills live in `<workspace>/skills/<skill-folder>/SKILL.md`.

## Directory Structure

```text
skill-folder/
  SKILL.md            # required: frontmatter + procedure body
  scripts/            # optional: deterministic shell helpers
  references/         # optional: docs loaded only when needed
  assets/             # optional: templates, output resources, media
```

Use `{baseDir}` in SKILL.md to reference paths relative to the skill
directory:

```markdown
Run the verification script: `{baseDir}/scripts/verify.sh`
See the checklist: `{baseDir}/references/checklist.md`
```

## Body Structure

### The Title

A level-1 heading that names the skill. Keep it short and match the
frontmatter `name`.

```markdown
# Preflight
```

### The Hard Gate (for Protocol Skills)

If the skill is triggered by an AGENTS.md gate instruction, restate
the gate at the top:

```markdown
## Hard Gate (R1)

This skill is invoked by AGENTS.md. Every step below MUST pass before
proceeding. HALT on any failure.
```

### The Procedure

Numbered or bulleted steps. Each step should be:
- Actionable: the agent knows exactly what command to run or what to check.
- Verifiable: the agent can tell if the step passed or failed.
- Non-overlapping: each step does one thing.

Use `{baseDir}` for references to scripts and checklists within the
skill directory. Prefer absolute paths for workspace and system paths.

```markdown
## Steps

1. **Mirror sync.** Run:
   ```
   LOCAL=$(git -C ~/.openclaw/workspace rev-parse HEAD)
   REMOTE=$(git ls-remote "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/workspace-ava.git" HEAD | awk '{print $1}')
   [ "$LOCAL" = "$REMOTE" ] && echo "SYNCED" || echo "DESYNCED"
   ```
   HALT if DESYNCED. Fix: local ahead = push; remote ahead = pull.
```

### The Self-Check

For procedures with verification steps, include either an inline
checklist or a reference to a checklist file:

## Self-Check

- [ ] Mirror sync verified (LOCAL = REMOTE)  (PASS / HALT)
- [ ] Workspace structure verified  (PASS / HALT)
- [ ] Context health checked  (PASS / HALT)
- [ ] Bootstrap ingested  (PASS / HALT)
- [ ] Governance ingested  (PASS / HALT)
- [ ] Memory index healthy  (PASS / HALT)
- [ ] memory_search run  (PASS / HALT)
- [ ] Read-proof emitted  (PASS / HALT)

### Cross-References

Link to the governance template that defines the pattern, the AGENTS.md
gate instruction that triggers this skill, and any related skills:

```markdown
## Related

- `governance/template-skills.md` -- skill construction rules
- AGENTS.md Preflight section -- the gate instruction that triggers this skill
- `skills/session-end/SKILL.md` -- session-end counterpart
```

## Quality Gates

Every skill passes these checks before being committed:

- **G1 -- Description Is a Trigger Surface:** The `description` field is a
  task-oriented instruction fragment. A model seeing it alongside a task
  description should correctly decide whether to invoke the skill.
- **G2 -- Has a Constitutional Trigger:** The skill is invoked by a hard-gate
  instruction in AGENTS.md (for protocol skills) or has a clear task-description
  match (for tool skills). No orphan skills.
- **G3 -- Procedure Is Actionable:** Every step can be executed from the
  description alone. No "think about X" or "consider Y" without a concrete
  action.
- **G4 -- Self-Check Exists:** If the procedure has verification steps, a
  checklist (inline or referenced) verifies each one.
- **G5 -- No Duplicate Governance:** The skill does not duplicate content
  from governance templates. It references them. R8 applies.
- **G6 -- Token Budget Conscious:** The description is under 160 chars.
  The body is as short as possible while remaining actionable. Remove
  content the base model already knows.
- **G7 -- Formatting Rules:** ASCII-only, lowercase slugs, hyphens not
  underscores. CI enforces ASCII via `ascii-guard.yml`.

## Anti-patterns

| Anti-pattern | Why It Fails | The Fix |
|---|---|---|
| Skill as constitution | "This skill must be run at session start." Cannot enforce. | Move enforcement to AGENTS.md. Skill carries procedure only. |
| Orphan skill | No AGENTS.md instruction, no task match. Never triggered. | Add gate instruction to AGENTS.md or improve description for task matching. |
| Description as summary | "A skill for doing X." Too generic for trigger matching. | Write as instruction fragment: "Verify X, check Y, and validate Z before proceeding." |
| Skill duplicates template | Skill contains checklist items from template-reflections.md. R8 violation. | Reference the template. Skill is procedure, template is format. |
| Skill without self-check | A 10-step procedure with no verification. Steps can be skipped silently. | Add inline checklist or `references/checklist.md`. |
| Skill with emoji in body | "Run the preflight checks :)" -- emoji is non-ASCII. | Remove all non-ASCII characters. ASCII-only mandate. |
| Over-granular skill | One skill per tiny procedure. 20 skills with 50 chars each. | Group related procedures. Aim for 5-10 skills total, each 1-3K chars. |
| Skill with hardcoded paths | `/home/suggi/workspace` instead of `~/.openclaw/workspace`. | Use `~` and env vars. Skills must work on other machines. |

## Example -- Minimal Valid Skill

---
name: example-skill
description: "Run a specific multi-step workflow with verification."
---

# Example Skill

## Hard Gate (R1)

Invoked by AGENTS.md. Every step MUST pass. HALT on failure.

## Steps

1. Run the check script: `{baseDir}/scripts/check.sh`
2. Verify output contains "OK".
3. If "OK", proceed. If "FAIL", HALT and report.

## Self-Check

- [ ] check.sh returned OK  (PASS / HALT)
- [ ] Output verified  (PASS / HALT)

## Related

- AGENTS.md -- the gate instruction that triggers this skill
- `governance/template-skills.md` -- skill construction rules

## The Skill Checklist

Pre-commit gate: every item below MUST be confirmed. The skill
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published skill.

- [ ] Frontmatter complete: name, description present; metadata.openclaw correct if used  (PASS / HALT)
- [ ] Frontmatter rules correct: name is kebab-case slug, description under 160 chars, quoted  (PASS / HALT)
- [ ] Description is a trigger surface (task-oriented instruction fragment)  (PASS / HALT)
- [ ] Skill has a constitutional trigger (AGENTS.md gate instruction or task-description match)  (PASS / HALT)
- [ ] Procedure steps are actionable (commands are copy-pasteable)  (PASS / HALT)
- [ ] Self-check exists if procedure has verification steps  (PASS / HALT)
- [ ] No duplicate governance content (references templates, does not inline them)  (PASS / HALT)
- [ ] Token budget: description under 160 chars, body lean  (PASS / HALT)
- [ ] {baseDir} used for internal references (not hardcoded relative paths)  (PASS / HALT)
- [ ] Folder name matches frontmatter name (or is clearly related)  (PASS / HALT)
- [ ] File is named SKILL.md (uppercase, as required)  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

---

*Written 2026-07-17 by Ava. Rules are scar tissue -- each one should trace
to a failure that proved it necessary. This template governs all skill
creation in the org.*
