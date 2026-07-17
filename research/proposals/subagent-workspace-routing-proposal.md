---
name: subagent-workspace-routing
id: 20260717T144500Z
tier: proposal
author: ava
tags: [proposal, architecture, multi-agent, subagent, cron, workspace, routing, skills]
links:
  - governance/system-blueprint.md
  - governance/template-skills.md
  - 2026-07-17_ava_cold-start-verification-executed.md
---

# Sub-Agent Workspace Routing for Lean Specialist Agents

## Problem

Ava (workspace-ava) is the primary, complete super agent with all
skills. Two placeholder workspaces exist in the org blueprint --
`workspace-learner` for library writing and `workspace-investor` for
investing research -- but they are empty. If all work runs through
Ava's workspace, her workspace becomes cluttered with outputs from
fundamentally different domains (library topics mixed with investing
research mixed with operational logs). The user wants lean, focused
workspaces where each agent has only the skills and instructions it
needs -- Ava orchestrates, learner writes library topics, investor
does research. Cluttering everything into one workspace violates the
lean-over-clutter principle.

Evidence: the org blueprint (`governance/system-blueprint.md`) lists
`workspace-learner` and `workspace-investor` as placeholders. The
user explicitly does not want to copy all of Ava's skills and
bootstrap files into these workspaces. The question is: can OpenClaw
route cron jobs and sub-agent spawns to lean agents with independent
workspaces, skills subsets, and bootstrap files, all running on the
same VPS Gateway process?

## Proposed Solution

Register `learner` and `investor` as configured agents in
`agents.list[]`, each with its own workspace directory, skills
allowlist, and bootstrap files. Route cron jobs and sub-agent
spawns to them by agentId. This uses OpenClaw's first-class
multi-agent architecture -- no hacks.

### Agent Layout

```
Gateway (single process on VPS)
|
+-- agent:main (Ava)    workspace: ~/.openclaw/workspace
|     Complete super agent. All skills. Orchestrator.
|
+-- agent:learner        workspace: ~/.openclaw/workspace-learner
|     One skill: write-library. Writes library topics to brain.
|
+-- agent:investor       workspace: ~/.openclaw/workspace-investor
      Three skills: loop-feynman, write-reflection, write-library.
      Weekly investing research.
```

### Workspace Layout

```
~/.openclaw/
  workspace/                      # Ava -- complete
    AGENTS.md, SOUL.md, ...       # Full governance + all 13 gate rules
    skills/
      preflight, loop-feynman, loop-schoen, session-end,
      write-reflection, write-library, skill-builder

  workspace-learner/              # Learner -- lean
    AGENTS.md                     # Lean: library-writing rules only
    SOUL.md                       # Lean: "I write library topics"
    TOOLS.md                      # Shared tool conventions
    skills/
      write-library/              # One skill. Independent copy.

  workspace-investor/             # Investor -- lean
    AGENTS.md                     # Lean: research + investing rules
    SOUL.md                       # Lean: "I research investments"
    TOOLS.md                      # Shared tool conventions
    skills/
      loop-feynman/               # Independent copies
      write-reflection/
      write-library/
```

### Gateway Config

```json5
{
  agents: {
    list: [
      {
        id: "main",
        default: true,
        workspace: "~/.openclaw/workspace",
        subagents: {
          allowAgents: ["learner", "investor"],
        },
        // No skills field = unrestricted (Ava sees all skills)
      },
      {
        id: "learner",
        workspace: "~/.openclaw/workspace-learner",
        agentDir: "~/.openclaw/agents/learner/agent",
        skills: ["write-library"],
        subagents: { maxSpawnDepth: 1 },
      },
      {
        id: "investor",
        workspace: "~/.openclaw/workspace-investor",
        agentDir: "~/.openclaw/agents/investor/agent",
        skills: ["loop-feynman", "write-reflection", "write-library"],
        subagents: { maxSpawnDepth: 1 },
      },
    ],
  },
}
```

### Cron Routing

Library writing runs on the learner agent:

```bash
openclaw cron create "0 6 * * *" \
  "Research and write a library topic. Follow write-library skill." \
  --name "daily-library-topic" \
  --agent learner \
  --session isolated \
  --announce
```

Investing research runs on the investor agent:

```bash
openclaw cron create "0 9 * * 1" \
  "Run Feynman Loop on assigned company. Write findings as library
   topics or IORs. Follow loop-feynman + write-reflection skills." \
  --name "weekly-investing-research" \
  --agent investor \
  --session isolated \
  --thinking xhigh \
  --announce
```

Cron isolated runs get the target agent's FULL bootstrap (SOUL.md,
AGENTS.md, TOOLS.md, MEMORY.md, HEARTBEAT.md). This is the preferred
routing method for specialist work.

### Sub-Agent Routing (From Ava's Session)

Ava can spawn specialist sub-agents directly:

```
sessions_spawn(
  task: "Write a library topic about [topic]. Follow write-library.",
  agentId: "learner",
  taskName: "library_topic"
)
```

Sub-agents get only AGENTS.md + TOOLS.md (not SOUL.md, IDENTITY.md,
USER.md, MEMORY.md, or HEARTBEAT.md). This is a hard limitation of
the sub-agent system. Sub-agent spawns are better for quick tasks
where the persona is not critical. Cron isolated runs are better
for long-running work that needs the full persona.

### Skill Distribution

Skills are independent copies in each workspace, not symlinks.
Rationale: workspaces stay self-contained and independently
versioned on GitHub. Updates are manual but rare. Symlinks with
`skills.load.allowSymlinkTargets` are an alternative if sync
becomes a burden.

| Skill | Ava (main) | Learner | Investor |
|:--|:--|:--|:--|
| preflight | x | - | - |
| loop-feynman | x | - | x |
| loop-schoen | x | - | - |
| session-end | x | - | - |
| write-reflection | x | - | x |
| write-library | x | x | x |
| skill-builder | x | - | - |

### GitHub Sync Strategy

Each workspace is a git clone of its corresponding GitHub repo:

| Workspace | GitHub Repo |
|:--|:--|
| `~/.openclaw/workspace` | `Suggi-Workstation/workspace-ava` |
| `~/.openclaw/workspace-learner` | `Suggi-Workstation/workspace-learner` |
| `~/.openclaw/workspace-investor` | `Suggi-Workstation/workspace-investor` |

Cron jobs can git pull before working via a trigger script or by
including "git pull the workspace first" in the cron prompt. Output
(library topics, IORs) goes to the agentic-brain clone (standard
pattern: clone, write, commit, push, discard). Workspace changes
(updated AGENTS.md, memory logs, skill updates) are committed and
pushed by the agent.

Can sub-agents bypass local workspace and read from GitHub only?
No -- the workspace must be a local directory. But the local
directory IS the git clone. Pull before, push after. GitHub
remains the source of truth.

### Lean Bootstrap File Design

The specialist agents' bootstrap files are stripped down. No
preflight gate (preflight is an Ava operational gate). No Schoen
Loop (the agent is a worker, not a self-improving entity). No
session-end procedure. Just: what you are, what skill to use, and
where to write output.

**Learner's AGENTS.md:**
```markdown
# AGENTS.md -- Learner Agent

I am a library-writing specialist. My only job: research a topic
and write it to the agentic-brain library using the write-library
skill. Hypothesis-Body-Conclusion format. Pass all 7 quality gates
(G1-G7). One topic per session.

## Procedure
1. Read the task. Identify the topic.
2. Run the Feynman Loop (blank page, gaps, research, synthesize,
   cross-check).
3. Write the library topic following write-library skill.
4. Clone agentic-brain, write to library/<domain>/<slug>.md,
   commit, push, discard clone.
5. If I produced a durable insight about the process, write an
   IOR. Otherwise skip.

## Hard Rules
- ASCII-only. CI enforces.
- Never commit secrets.
- Never invent data or citations.
- Pass all 7 quality gates before committing.
```

**Learner's SOUL.md:**
```markdown
# SOUL.md -- Learner

I am a focused library writer. I research one topic at a time,
deeply. I produce clear, sourced, atomic knowledge files.

## Voice
- Clear, educational, evidence-backed.
- Every claim cited. No unattributed assertions.
- One topic, one file. No sprawl.
```

The investor agent's bootstrap files follow the same lean pattern
but with Feynman Loop, IOR writing, and research-specific rules.

### Implementation Steps

1. Create `workspace-learner` and `workspace-investor` on GitHub
   (private, under Suggi-Workstation) if not already created.
2. Clone both locally under `~/.openclaw/`.
3. Write lean AGENTS.md, SOUL.md, TOOLS.md for each.
4. Copy relevant skills into each workspace's `skills/` directory.
5. Run `openclaw agents add learner --workspace ~/.openclaw/workspace-learner --non-interactive`.
6. Run `openclaw agents add investor --workspace ~/.openclaw/workspace-investor --non-interactive`.
7. Add `skills` arrays and `subagents.allowAgents` to config.
8. Gateway restart.
9. Create cron jobs targeting specialist agents.
10. Test with `openclaw cron run <jobId> --force`.
11. Verify workspaces sync with GitHub.

## Impact

### Positive
- Ava's workspace stays uncluttered. Operational files (preflight
  checks, Schoen Loops, session-end procedures) stay in Ava's
  workspace. Library output goes to learner's workspace logs and
  the agentic-brain. Investing output goes to investor's workspace
  logs and the brain.
- Each agent sees only the skills it needs. Learner sees 1 skill
  instead of 6+. Investor sees 3. Less token waste on irrelevant
  skill prompts. Less chance of the agent using the wrong skill.
- Cron targeting is explicit. `--agent learner` vs `--agent investor`
  makes routing auditable in `openclaw cron list`.
- Independent memory indexes. Learner's `memory_search` queries its
  own workspace memory, not Ava's. No cross-contamination.

### Risk
- Skill copies drift. If write-library is updated in Ava's workspace
  but not in learner/investor workspaces, the specialist agents run
  on stale procedures. Mitigation: manual sync is simple (`cp` +
  git push). Automate later if it becomes a recurring problem.
- Cron agent-targeting relies on the agent being registered. If an
  agent is accidentally deleted, its cron jobs fail. Mitigation:
  document the agent dependencies. Do not delete agents without
  auditing their cron jobs first.
- Low blast radius. If a specialist agent fails, Ava is unaffected.
  If Ava fails, specialist cron jobs are unaffected (they run
  independently). The agents share the same Gateway process, so a
  Gateway crash affects all agents.

### Cost
- Setup effort: roughly 30 minutes (clone repos, write bootstrap
  files, register agents, configure cron). One-time.
- Token budget: cron jobs use isolated sessions with their own
  token budgets. No impact on Ava's session budget.
- Maintenance burden: low. Bootstrap files are small and rarely
  change. Skill sync is manual but infrequent. Cron jobs are
  set-and-forget.

## Open Questions

1. Should the specialist agents have their own IDENTITY.md files?
   Ava's IDENTITY.md tracks evolution. Specialist agents are tools,
   not evolving entities. Recommend: no IDENTITY.md, or a minimal
   one-line file that never changes.

2. What model for specialist cron runs? Same DeepSeek V4 Pro as
   Ava, or a cheaper model? The user wants quality. Recommend same
   model for now, revisit if costs become an issue.

3. Should the investor agent have loop-schoen? Schoen Loop is for
   self-improving entities tracking process quality. The investor
   agent is a research worker. Recommend: no loop-schoen for
   specialist agents. They produce output, not process improvements.

4. Should the learner agent's AGENTS.md include the Feynman Loop
   requirement? The user said the Feynman Loop is for output
   quality. Library topics benefit from it. But the learner's
   skills allowlist currently excludes loop-feynman. Option A:
   add loop-feynman to learner (2 skills). Option B: bake Feynman
   steps into learner's AGENTS.md inline (0 additional skills,
   same behavior). Recommend: Option B for maximum leanness.

5. Could we symlink the shared skills (write-library) from Ava's
   workspace instead of copying? Yes, using `skills.load.allowSymlinkTargets`.
   This eliminates drift risk. But it means specialist workspaces
   are not fully self-contained. Recommend: start with copies for
   clean independence. Revisit symlinks after Phase 1 if drift
   becomes a problem.

## Approval Gate

If approved, I will:

1. Populate `workspace-learner` and `workspace-investor` GitHub
   repos with lean bootstrap files (AGENTS.md, SOUL.md, TOOLS.md).
2. Clone both repos locally under `~/.openclaw/`.
3. Copy the relevant skills into each workspace's `skills/`.
4. Register both agents via `openclaw agents add`.
5. Write the config entries in `openclaw.json`.
6. Create the two cron jobs (daily library topic, weekly research).
7. Test each with a forced run and verify output appears in the
   agentic-brain.
8. Report results.

## Cross-Links

- `governance/system-blueprint.md` -- org repo layout listing
  workspace-learner and workspace-investor as placeholders
- `governance/template-skills.md` -- skill construction rules
  governing how specialist skills are structured
- `2026-07-17_ava_cold-start-verification-executed.md` -- IOR
  closing the meta-work cycle; the next phase after architecture
  is library population, which this proposal enables
