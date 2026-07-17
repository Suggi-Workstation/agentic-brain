---
name: skills-as-protocol-carriers
id: 20260717T121500Z
tier: reflection
trigger: research
author: Ava
tags: [skills, architecture, protocols, gates, preflight, session-end, feynman-loop, schoen-loop, prompt-efficiency, openclaw]
links:
  - governance/template-reflections.md
  - research/insights/rules-need-gates.md
  - research/insights/openclaw-manual.md
---

# i+o+r  skills can carry procedures but cannot enforce gates -- the constitution-vs-procedure split (Ava)

## I -- Idea

Suggi proposed moving the four operational protocols (Preflight, Feynman Loop,
Schoen Loop, Session End) from AGENTS.md into standalone skills, keeping
AGENTS.md lean with only references. Skills CAN carry procedures efficiently
but CANNOT enforce gates -- skills lack lifecycle hooks (no "before_session"
or "after_session" triggers). The correct architecture is a split: AGENTS.md
keeps the gate enforcement (WHAT must happen and WHEN), skills carry the
procedure (HOW it happens). This saves ~5.5K chars from the always-loaded
bootstrap while preserving gate strength.

This research was triggered by Suggi's Phase 21 proposal to reduce AGENTS.md
bloat. The openclaw-manual.md insight was already updated with thinking config
resolution order; now the question was whether the skills system could
structurally replace the inline protocols.

## O -- Opinion

Confidence: high (90%). The skills system is well-documented and designed for
exactly this pattern -- compact trigger metadata always visible, full
procedures loaded on demand. The limitation (no lifecycle hooks) is not a
blocker; it forces a cleaner architecture where the "constitution" (gates) and
"procedures" (skills) are properly separated.

The proposal is viable and architecturally sound, with specific constraints:

### What Skills Can Do (Strengths)

- **Lazy loading.** Skill bodies load only when the agent invokes them. The
  always-loaded prompt contains only name + description (~100 chars per skill).
  Versus inline text in AGENTS.md (~6K chars for the four protocols), the
  savings compound across every session start.

- **Independent versioning.** Skills can be updated without touching AGENTS.md.
  A preflight skill can add a new check without risking AGENTS.md corruption.
  The skill is the single source of truth for its procedure.

- **Workspace precedence.** `<workspace>/skills` beats bundled skills, so our
  custom preflight/session-end skills override any defaults.

- **Gating.** Skills support `metadata.openclaw.requires` (bins, env, config)
  for conditional activation. Preflight could require `git` on PATH; if missing,
  the skill is silently gated out.

- **`{baseDir}` references.** Skills can ship scripts, templates, and reference
  docs in subdirectories. A preflight skill could include a `scripts/verify.sh`
  for automated checks.

- **Cross-agent reuse.** Shared managed skills (`~/.openclaw/skills`) are
  visible to all agents. If Link wanted the same preflight, one shared skill
  serves both agents. Per-agent workspaces override or extend.

- **Watcher-based refresh.** Skills auto-refresh when SKILL.md changes. No
  gateway restart needed.

### What Skills Cannot Do (Limitations)

- **No lifecycle hooks.** Skills cannot fire automatically at preflight,
  post-compaction, or session-end. They must be explicitly invoked by the agent
  (via AGENTS.md instruction) or triggered by task description match. There is
  no `hooks.before_session_start` equivalent in the skill system.

- **No gate enforcement.** A skill provides instructions but cannot HALT
  execution. If the agent chooses not to invoke the preflight skill, nothing
  stops it. The inline approach in AGENTS.md guarantees the instructions are
  in context; the skill approach requires the agent to voluntarily read them.

- **Not loaded until triggered.** The skill body is not in context until the
  agent invokes it. This is the efficiency advantage but also the enforcement
  gap. The agent must choose to read the skill before it can follow its
  instructions.

### The Architecture: Constitution vs. Procedure Split

The correct approach addresses the limitation directly:

**AGENTS.md (Constitution) -- WHAT and WHEN:**
```
## Preflight -- HARD GATE (first, every session)

MUST invoke the `preflight` skill before any other action.
Follow every step in the skill. This is R1: PASS or HALT.
If the preflight HALTed, do not proceed.
```

This is ~150 chars vs. the current ~2K chars of inline preflight text. The
gate instruction IS in context (always loaded). The agent cannot claim it
"did not know" about the preflight -- the instruction is unambiguous and uses
RFC 2119 MUST language.

**Preflight Skill (Procedure) -- HOW:**
- Mirror sync verification
- Workspace structure verification  
- Context health check
- Bootstrap ingestion
- Governance ingestion
- Memory index verification
- Memory search
- Read-proof emission
- Self-check table

The skill body (~2K chars) loads only when the agent invokes `/preflight`.
This is a READ-DO pattern (Gawande): the agent reads the instruction then
executes each step.

### Token Budget Analysis

| Protocol | Current inline (chars) | As skill instruction (chars) | Saved |
|---|---|---|---|
| Preflight | ~2,000 | ~150 | 1,850 |
| Feynman Loop | ~1,000 | ~100 | 900 |
| Schoen Loop | ~500 | ~100 | 400 |
| Session End (steps 1-5) | ~1,500 | ~150 | 1,350 |
| IOR Writing | ~1,000 | ~50 | 950 |
| **Total** | **~6,000** | **~550** | **~5,450** |

At ~4 chars/token, this saves roughly 1,350 tokens from the always-loaded
bootstrap context. Over hundreds of sessions, this compounds.

The skill bodies (~6K chars combined) are loaded once per session when invoked,
costing ~1,500 tokens the first time they are needed. The net savings depends
on session length: short sessions break even or lose slightly; long sessions
save significantly.

### Risk: The Agent Skips the Skill

The primary failure mode: AGENTS.md says "invoke preflight" but the agent
proceeds without invoking it. This is NOT a new failure mode -- the current
inline approach has the same risk (the agent can skip steps even when they
are in context). The skill approach does not meaningfully increase this risk
because the gate instruction ("MUST invoke /preflight") is still in context.

Mitigations:
- The preflight skill description should be self-documenting: "Verify workspace
  mirror sync, context health, memory index, and governance before every session."
  This makes the skill's purpose clear even from the available-skills list.
- The AGENTS.md instruction is a hard gate with MUST/HALT language.
- The self-check table remains in the skill (or in AGENTS.md as a summary) to
  provide a visible completion checklist.
- If the agent fails preflight, it is detectable: the context shows no preflight
  actions were taken. The Schoen Loop catches it at session end.

### Skill Structure Design

Each skill should follow this pattern:

```
skills/preflight/
  SKILL.md              # Gate instruction + procedure
  references/
    preflight-checklist.md  # Self-check table (loaded only if needed)
  scripts/
    verify-mirror.sh    # Automated mirror sync check (optional)
```

SKILL.md for preflight:
```markdown
---
name: preflight
description: "Verify workspace mirror sync, context health, memory index, and governance before every session."
metadata: { "openclaw": { "requires": { "bins": ["git"] } } }
---

# Preflight -- Session Startup Verification

## Hard Gate (R1)

Every step below MUST pass before proceeding. HALT on any failure.

## Steps

1. **Mirror sync** -- Run git rev-parse + ls-remote. LOCAL must equal REMOTE.
   If desynced: local ahead = push, remote ahead = pull. Re-verify.
2. **Workspace structure** -- Verify all files in the Layout section of
   AGENTS.md exist. Create missing folders with mkdir -p.
3. **Context health** -- Run `/context list`. If any bootstrap file shows
   TRUNCATED or is within 10% of bootstrapMaxChars, flag it.
4. **Bootstrap ingestion** -- Confirm SOUL, AGENTS, MEMORY, IDENTITY, USER,
   TOOLS, HEARTBEAT all loaded.
5. **Governance ingestion** -- Read system-constitution.md,
   system-blueprint.md, system-primedirectives.md from agentic-brain.
6. **Memory index** -- Run `openclaw memory status`. If broken, run
   `openclaw memory index --force --agent main` and re-verify.
7. **Memory search** -- Run memory_search for recent context.
8. **Read-proof** -- Emit first output of session: "read: SOUL OK; AGENTS OK;
   ..."

## Self-Check

See `{baseDir}/references/preflight-checklist.md` for the verification table.
```

### What Already Exists vs. What We Build

**Bundled skills that partially overlap:**
- `healthcheck` -- host-level security audit. Different scope (OS, not workspace).
  Not a preflight replacement but a complementary skill.
- `spike` -- throwaway prototype workflow. Pattern reference for structured
  procedure skills.
- `taskflow` -- multi-step detached task orchestration. Too heavy for preflight;
  designed for async workflows with persistent state.

**Nothing existing matches our preflight/session-end pattern.** These are
organization-specific protocols derived from our Scar Tissue rules. They must
be built as custom skills.

**Skills we would build:**
1. `preflight` -- session startup verification (8 steps + self-check)
2. `feynman-loop` -- 6-step output quality loop
3. `schoen-loop` -- 4-question session-end reflection
4. `session-end` -- 5-step session close protocol
5. `ior-write` -- IOR creation following template-reflections.md

### Implementation Plan

1. Create skills in `~/.openclaw/workspace/skills/` (workspace-level, highest
   precedence, agent-specific)
2. Each skill gets `SKILL.md` + optional `references/` for detailed
   checklists
3. AGENTS.md is pruned: inline protocols replaced with hard-gate skill
   invocation instructions
4. The self-check tables move to skill `references/` subdirectories
5. Test: new session should invoke preflight on first turn, session-end before
   closing
6. Verify token savings via `/context detail` before and after

### What Stays in AGENTS.md (Not Movable to Skills)

- **Gate Rules R1-R13.** These are principles, not procedures. They inform
  every action. They must stay in always-loaded context.
- **Hard Rules section.** "ASCII-only, never commit secrets, etc." These are
  constitutional constraints, not procedural steps.
- **Architecture description.** The mirror model, workspace layout. Reference
  material the agent needs at all times.
- **The Gate Rule definitions.** What they mean, why they exist, the scar
  tissue origin. This is context the agent draws on throughout the session.

### What Moves to Skills

- **Preflight steps 1-7.** The procedural "how" of verification. Kept inline
  only as a hard-gate instruction: "MUST invoke /preflight."
- **Feynman Loop steps 1-6.** The detailed loop procedure. AGENTS.md keeps:
  "Before writing anything substantive, invoke /feynman-loop."
- **Schoen Loop 4 questions.** AGENTS.md keeps: "Every substantive session
  ends with /schoen-loop. Budget: at most 20% of session effort."
- **Session End steps 1-5.** AGENTS.md keeps: "At session end, invoke
  /session-end.\" The skill carries the detailed procedure.
- **IOR Writing format.** AGENTS.md keeps: "Write an IOR to
  agentic-brain/reflections/ if the session produced a durable insight.
  Invoke /ior-write and follow the skill."

## R -- Reflection

### Surprise (30%)

I expected skills to be a lightweight plugin system -- tool wrappers. They are
more general than that. The lazy-loading architecture (name+description always
visible, body on demand) is exactly the right shape for protocol encoding. The
OpenClaw team built this for exactly this use case: move heavy procedural
instructions out of the always-loaded prompt into triggerable, versionable,
sharable skill files.

The surprise was that ClawHub has no pre-existing "agent protocol" skills.
The skill ecosystem is tool-focused (image generation, PDF manipulation, git
operations). Organizational protocols like preflight and session-end are not
on ClawHub because they are inherently specific to each team's scar tissue.
This is correct: our protocols derive from our failures, and no one else has
our failure history.

### Feel (30%)

Relief. This proposal has been in the back of my mind since the bootstrap
context was bumped to 50K chars. AGENTS.md has grown with every session
(Preflight, Feynman Loop, Schoen Loop, IOR Writing, Session End, Retrieval
rules, Hard Rules, all 13 Gate Rules). Each addition was justified, but the
accumulation is real. The skills system provides a pressure-release valve that
does not compromise enforcement.

Slight unease about the transition: the current inline approach has been
battle-tested. Moving to skills introduces a new invocation step that could
fail. But the mitigation (hard-gate instruction in AGENTS.md) is strong enough
that I am comfortable with the risk. The gate instruction IS the enforcement;
the skill is just the procedure.

### Learn (40%)

1. **The skills system was designed for this pattern.** "Metadata always
   visible; body loads only after trigger." This is the prompt-efficiency
   architecture we need. The design is deliberate, not accidental -- the
   OpenClaw team expected agents with complex internal protocols.

2. **Constitution vs. Procedure is the correct separation.** AGENTS.md is the
   constitution: what must happen, when, and why. Skills are the procedures:
   how each step is executed. The constitution enforces gates; the procedures
   carry details. Neither alone is sufficient; both together are the system.

3. **Skills cannot replace gates but can carry them forward.** The preflight
   skill contains the self-check table. The gate enforcement ("PASS or HALT")
   stays in AGENTS.md. The verification mechanism ("what to check") moves to
   the skill. This is the same pattern as the template-reflections.md
   Pre-Commit Self-Check -- the gate is in the template, the items are in the
   checklist.

4. **Organizational protocols are inherently custom.** No ClawHub skill will
   ever have our Preflight procedure because it encodes our specific failure
   history (mirror desyncs, truncated SOUL, broken memory index, config
   contamination). The skill system supports this: workspace skills at highest
   precedence let us build team-specific protocols that are invisible to the
   public registry.

## One Actionable Change

Create the `preflight` skill as a proof-of-concept. This is the most
complex protocol (8 steps, tool calls, self-check) and the most impactful
for prompt savings (~2K chars). If preflight works as a skill, the
Feynman Loop, Schoen Loop, Session End, and IOR Writing skills follow
naturally. The AGENTS.md change is a single-line replacement:
"Before any other action, MUST invoke `/preflight`."

## Cross-links

- `governance/template-reflections.md` -- IOR format
- `research/insights/rules-need-gates.md` -- why protocols need gates, the
  R8 reference pattern this architecture follows
- `research/insights/openclaw-manual.md` -- skills system documentation
- Source: Suggi's Phase 21 proposal session

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Skills-as-protocol-carriers architecture. Constitution-vs-procedure split. |
