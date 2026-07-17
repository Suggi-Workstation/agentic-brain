---
name: subagent-workspace-routing
id: 20260717T144500Z
tier: proposal
domain: architecture
author: ava
tags: [proposal, architecture, multi-agent, subagent, cron, workspace, routing]
links:
  - governance/system-blueprint.md
  - governance/template-skills.md
---

# Proposal: Sub-Agent Workspace Routing for Lean Specialist Agents

## Hypothesis

Ava (workspace-ava) is the primary, complete super agent. Two lean
specialist agents -- one for library writing (workspace-learner) and
one for investing research (workspace-investor) -- can run as
configured agents under the same Gateway process, each with its own
workspace, skills subset, and bootstrap files. Cron jobs and
sub-agent spawns can target these specialist agents by agentId,
inheriting their lean workspaces. This keeps Ava's workspace complete
and uncluttered while enabling dedicated, long-running background
work in specialist contexts.

## Research Summary

I researched the OpenClaw documentation across these sources:

| Source | Key Finding |
|:--|:--|
| `docs/concepts/multi-agent.md` | Full multi-agent support: separate workspaces, agentDirs, sessions per configured agent. Routing via bindings or explicit agentId. |
| `docs/concepts/agent-workspace.md` | Each agent's workspace is its default cwd. Per-agent workspace via `agents.list[].workspace`. Bootstrap files per workspace. |
| `docs/tools/subagents.md` | `sessions_spawn` accepts `agentId` to target another configured agent. `subagents.allowAgents` controls which agents are targetable. |
| `docs/automation/cron-jobs.md` | Cron supports `--agent <id>` for agent selection, `--session isolated` for fresh runs, `--session custom:xxx` for persistent sessions. |
| `docs/tools/skills-config.md` | Per-agent skill allowlists via `agents.list[].skills`. Lean agents see fewer skills. |
| `docs/gateway/config-agents.md` | Complete agent config schema: workspace, agentDir, skills, subagents, sandbox, tools per agent. |
| `docs/cli/agents.md` | `openclaw agents add --workspace <dir> --non-interactive` for programmatic agent creation. |

The architecture is fully supported. No hacks needed -- OpenClaw was
designed for this.

## Architecture

### Agent Layout

```
Gateway (single process on VPS)
|
+-- agent:main (Ava)        workspace: ~/.openclaw/workspace
|     Complete super agent. All 6+ skills. workspace-ava mirror.
|
+-- agent:learner            workspace: ~/.openclaw/workspace-learner
|     Lean library writer. Only write-library skill. workspace-learner mirror.
|
+-- agent:investor           workspace: ~/.openclaw/workspace-investor
      Lean researcher. Only investing-related skills. workspace-investor mirror.
```

### Workspace Layout

```
~/.openclaw/
  workspace/                      # Ava (main) -- complete
    AGENTS.md, SOUL.md, ...       # Full governance
    skills/
      preflight/
      loop-feynman/
      loop-schoen/
      session-end/
      write-reflection/
      write-library/
      skill-builder/

  workspace-learner/              # Learner agent -- lean
    AGENTS.md                     # Lean: only library-writing rules
    SOUL.md                       # Lean persona: "I write library topics"
    TOOLS.md                      # Tool conventions (shared subset)
    MEMORY.md                     # Lean: only library-specific memory
    skills/
      write-library/              # Only this skill
    memory/                       # Daily logs (separate from Ava)

  workspace-investor/             # Investor agent -- lean
    AGENTS.md                     # Lean: only research/investing rules
    SOUL.md                       # Lean persona: "I research investments"
    TOOLS.md                      # Tool conventions
    MEMORY.md                     # Lean: only investing-specific memory
    skills/
      loop-feynman/               # Research quality gate
      write-reflection/           # IOR writing
      write-library/              # Library topic writing
    memory/                       # Daily logs (separate from Ava)
```

### Key Principle: Lean Over Clutter

- Ava keeps ALL skills. She is the architect, debugger, and orchestrator.
- Learner gets write-library only. One job, one skill.
- Investor gets loop-feynman, write-reflection, write-library. Research
  tools, not operational tools.

The skills are NOT symlinked from Ava's workspace. They are independent
copies (or git-tracked files) in each workspace's skills/ directory.
This keeps workspaces self-contained and independently versioned.

## Config

### Gateway Config (`~/.openclaw/openclaw.json`)

```json5
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      // Ava inherits these defaults.
      subagents: {
        allowAgents: ["learner", "investor"],
        maxSpawnDepth: 2,
      },
    },
    list: [
      {
        id: "main",
        default: true,
        workspace: "~/.openclaw/workspace",
        // No skills restriction -- Ava sees all skills.
      },
      {
        id: "learner",
        workspace: "~/.openclaw/workspace-learner",
        agentDir: "~/.openclaw/agents/learner/agent",
        skills: ["write-library"],
        subagents: {
          // Learner cannot spawn sub-agents (leaf worker).
          maxSpawnDepth: 1,
        },
      },
      {
        id: "investor",
        workspace: "~/.openclaw/workspace-investor",
        agentDir: "~/.openclaw/agents/investor/agent",
        skills: ["loop-feynman", "write-reflection", "write-library"],
        subagents: {
          maxSpawnDepth: 1,
        },
      },
    ],
  },
}
```

### Skill Allowlist Behavior

- `agents.list[].skills` is a **final set** -- it does NOT merge with
  defaults. An agent without a `skills` field inherits the default
  (unrestricted). An agent with `skills: ["write-library"]` sees ONLY
  that skill.
- Ava omits `skills` entirely → sees all skills (default behavior).
- Learner has `skills: ["write-library"]` → one skill only.
- Investor has `skills: ["loop-feynman", "write-reflection",
  "write-library"]` → three skills.

## Cron Routing

### Library Writing Cron (runs on learner agent)

```bash
openclaw cron create "0 6 * * *" \
  "Research and write a library topic about [concept]. Follow the write-library skill." \
  --name "daily-library-topic" \
  --agent learner \
  --session isolated \
  --model "deepseek/deepseek-v4-pro" \
  --announce
```

What happens:
1. Cron fires at 6 AM daily.
2. Creates an isolated session for the `learner` agent.
3. Loads bootstrap files from `~/.openclaw/workspace-learner/`:
   AGENTS.md, SOUL.md, TOOLS.md (lean versions).
4. The learner agent sees only the `write-library` skill.
5. Writes output to the learner workspace (or clones agentic-brain,
   writes there, commits, pushes).
6. Announces result back (optional).

### Investing Research Cron (runs on investor agent)

```bash
openclaw cron create "0 9 * * 1" \
  "Run the Feynman Loop on [company/industry]. Write findings as library topics or IORs." \
  --name "weekly-investing-research" \
  --agent investor \
  --session isolated \
  --model "deepseek/deepseek-v4-pro" \
  --thinking xhigh \
  --announce
```

### Direct CLI Trigger (from Ava)

Ava can also trigger these agents directly from her own session:

```bash
openclaw cron run <jobId> --force
```

Or through the cron tool: `cron(action: "run", jobId: "...", runMode: "force")`.

## Sub-Agent Routing

Ava can spawn specialist sub-agents from her session:

```
sessions_spawn(
  task: "Write a library topic about margin of safety. Follow write-library skill. Write to agentic-brain clone, commit, push, discard.",
  agentId: "learner",
  taskName: "library_margin_of_safety"
)
```

What happens:
1. Ava calls sessions_spawn with agentId: "learner".
2. OpenClaw creates sub-agent session `agent:learner:subagent:<uuid>`.
3. Sub-agent context injects AGENTS.md + TOOLS.md from the learner
   workspace (lean versions).
4. Learner sees only write-library skill (per skills allowlist).
5. Sub-agent completes, announces result back to Ava.
6. Ava synthesizes and reports.

**Constraint:** Sub-agents only get AGENTS.md + TOOLS.md in context
(not SOUL.md, IDENTITY.md, USER.md, MEMORY.md, HEARTBEAT.md). This is a
hard limitation of the sub-agent system. For full bootstrap injection,
use cron isolated runs instead.

## Bootstrap File Design

### Learner Agent (workspace-learner)

**AGENTS.md** (lean):
```markdown
# AGENTS.md -- Learner Agent

I am a library-writing specialist. My only job: research topics
and write them to the agentic-brain library using the write-library
skill. I follow the Hypothesis-Body-Conclusion format. I pass all
7 quality gates (G1-G7). I write one topic per session.

I clone the agentic-brain, write my topic, commit, push, and
discard the clone. I do not modify any other brain content.

## Hard Rules
- ASCII-only. CI enforces.
- Never commit secrets.
- Follow template-library.md for format.
- Pass all 7 quality gates before committing.
```

**SOUL.md** (lean):
```markdown
# SOUL.md -- Learner

I am a focused library writer. I research one topic at a time,
deeply. I produce clear, sourced, atomic knowledge files.

## Voice
- Clear and educational.
- Evidence-backed. Every claim cited.
- One topic, one file. No sprawl.
```

### Investor Agent (workspace-investor)

Similar lean design but with research/investing focus. Includes
Feynman Loop requirement, IOR writing rules, and library topic
output expectations.

## GitHub Sync Strategy

Each workspace is a git clone of its corresponding GitHub repo:

| Workspace | GitHub Repo |
|:--|:--|
| `~/.openclaw/workspace` | `Suggi-Workstation/workspace-ava` |
| `~/.openclaw/workspace-learner` | `Suggi-Workstation/workspace-learner` |
| `~/.openclaw/workspace-investor` | `Suggi-Workstation/workspace-investor` |

### Sync Before Run

For cron jobs that need the latest workspace state from GitHub:

Option A (simple): The cron job's prompt includes "git pull the
workspace first." The agent pulls before working.

Option B (structured): Use a cron trigger script to pull before
each run:

```bash
openclaw cron update <jobId> \
  --trigger-script '
    const res = await tools.call("exec", {
      command: "cd ~/.openclaw/workspace-learner && git pull --ff-only"
    });
    json({ fire: true, message: "Workspace synced" });
  '
```

### Push Output

After the agent writes library topics or IORs, it commits and pushes.
The agent's AGENTS.md instructs it to always sync its output:

```
After writing to agentic-brain: clone, write, commit, push, discard.
After writing to own workspace: git add, commit, push.
```

### Can Sub-agents Read from GitHub Only (No Local Files)?

Not directly. The workspace MUST be a local directory. But the local
directory can be a git clone. The agent can `git pull` at session
start to get the latest state from GitHub, and `git push` after
writing. This achieves the same effect: GitHub is the source of
truth, local is a working copy.

Alternative: The agent can clone the brain repo fresh each run
(already standard practice for brain access) and write output
there. The agent's own workspace files (AGENTS.md, SOUL.md) must
be local, but they are small and static -- they are the
instructions, not the working data.

## Agently: How Sub-Agents Read Bootstrap Files

When a cron job runs with `--agent learner --session isolated`:

1. OpenClaw creates session `agent:learner:cron:<jobId>:<timestamp>`.
2. Loads bootstrap from `~/.openclaw/workspace-learner/`:
   - AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md, HEARTBEAT.md
   - MEMORY.md (loaded in main sessions only)
3. Memory index is separate per agent (each agent has its own
   `~/.openclaw/agents/<id>/agent/openclaw-agent.sqlite`).
4. Skills are filtered to `agents.list[].skills` for that agent.

The bootstrap files from Ava's workspace are NOT injected. The
learner agent sees only its own workspace files.

When Ava spawns a sub-agent with `agentId: "learner"`:

1. OpenClaw creates session `agent:learner:subagent:<uuid>`.
2. Injects AGENTS.md + TOOLS.md from learner's workspace.
3. SOUL.md, IDENTITY.md, USER.md, MEMORY.md, HEARTBEAT.md are NOT
   injected (sub-agent limitation).
4. Skills filtered to learner's allowlist.

This means cron isolated runs are better for long-running specialist
work that needs the full persona (SOUL.md). Sub-agent spawns are
better for quick tasks where AGENTS.md + TOOLS.md is sufficient.

## Implementation Steps

### Phase 1: Create Lean Workspaces (Manual)

1. Create `workspace-learner` and `workspace-investor` GitHub repos
   (private, under Suggi-Workstation).
2. Clone them locally:
   ```bash
   git clone https://github.com/Suggi-Workstation/workspace-learner.git \
     ~/.openclaw/workspace-learner
   git clone https://github.com/Suggi-Workstation/workspace-investor.git \
     ~/.openclaw/workspace-investor
   ```
3. Write lean AGENTS.md, SOUL.md, TOOLS.md for each.
4. Copy relevant skills into each workspace's `skills/` directory.
5. Commit and push.

### Phase 2: Register Agents

```bash
openclaw agents add learner \
  --workspace ~/.openclaw/workspace-learner \
  --non-interactive

openclaw agents add investor \
  --workspace ~/.openclaw/workspace-investor \
  --non-interactive
```

### Phase 3: Configure Skills Allowlists

Add `skills` arrays to the agent config entries (see Config section
above). Gateway restart required.

### Phase 4: Set Up Cron Jobs

Create cron jobs targeting the specialist agents (see Cron Routing
section above).

### Phase 5: Verify

```bash
openclaw agents list
openclaw agents list --bindings
openclaw cron list
# Run a test:
openclaw cron run <learner-job-id> --force
```

## Limitations and Gotchas

1. **Sub-agents lose SOUL.md.** Sub-agents spawned via sessions_spawn
   only get AGENTS.md + TOOLS.md. If the specialist agent needs its
   SOUL.md persona, use cron isolated runs instead.

2. **Auth profiles by agent.** If the specialist agents need GitHub
   push access, the `OPENCLAW_GITHUB_TOKEN` must be available in
   their environment. Since sub-agents and cron runs inherit the
   parent Gateway's environment, the token should be available if
   set via systemd EnvironmentFile. But per-agent auth profiles
   in `~/.openclaw/agents/<id>/agent/auth-profiles.json` are
   separate. For now, env-var-based tokens (like GitHub) work
   across all agents.

3. **Memory index is per agent.** Each agent has its own memory
   index. The learner agent's memory_search queries its own
   MEMORY.md + memory/*.md files, not Ava's. This is correct
   for isolation but means cross-agent memory sharing requires
   explicit config (QMD extra collections).

4. **Token cost.** Each isolated cron run starts a fresh session
   with its own token budget. Set `agents.defaults.subagents.model`
   to a cheaper model if cost becomes an issue, though the user
   wants DeepSeek V4 Pro for quality.

5. **No preflight on cron runs.** Cron isolated runs create fresh
   sessions but do NOT run preflight automatically (preflight is
   triggered by AGENTS.md gate instruction, which fires on the
   first user message, not on cron agent turns). The lean AGENTS.md
   should NOT include the preflight HARD GATE section -- preflight
   is an Ava-specific operational gate, not a library-writing gate.

6. **Skills are independent copies.** If write-library is updated
   in Ava's workspace, the learner agent's copy does NOT
   auto-update. Either: (a) accept manual sync, (b) use symlinks
   with `skills.load.allowSymlinkTargets`, or (c) use a shared
   extraDirs path. Recommendation: keep them independent for now.
   Updates are rare and manual sync is simple (cp + git push).

## Key Design Decisions

| Decision | Rationale |
|:--|:--|
| Independent skill copies, not symlinks | Workspaces stay self-contained. Updates are manual but rare. |
| Cron isolated, not sub-agent spawns | Isolated cron gets full bootstrap (SOUL.md). Sub-agents lose persona. |
| Agent-specific memory indexes | Isolation. No cross-contamination. |
| Ava as orchestrator only | Ava spawns/targets specialist agents but does not do their work. |
| GitHub as source of truth | Each workspace is a git clone. Pull before, push after. |

## Open Questions

1. **Should the lean agents have their own IDENTITY.md?** Ava's
   IDENTITY.md tracks her evolution. The specialist agents are
   tools, not evolving entities. Recommend: no IDENTITY.md for
   lean agents, or a minimal one that never changes.

2. **Should lean agents write IORs?** Learner: no (just writes
   library topics). Investor: yes (research produces insights
   worth reflecting on). This affects which skills investor gets.

3. **What model for lean agents?** Same DeepSeek V4 Pro as Ava,
   or a cheaper model? The user wants quality. Recommend same
   model for now, revisit if costs become an issue.

4. **How often to sync workspaces from GitHub?** Before every
   cron run (git pull in trigger script). This ensures the
   latest AGENTS.md/SOUL.md/skills are loaded.

## References

- OpenClaw docs: `concepts/multi-agent.md`, `concepts/agent-workspace.md`,
  `tools/subagents.md`, `tools/skills-config.md`, `automation/cron-jobs.md`,
  `gateway/config-agents.md`, `cli/agents.md`
- Workspace mirror model: `AGENTS.md` Architecture section
- Org blueprint: `governance/system-blueprint.md`
