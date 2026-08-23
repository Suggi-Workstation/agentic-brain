---
name: subagent-workspace-routing
id: 20260718T144607Z
tier: proposal
author: ava
version: 2.0
status: superseded by 20260823T142607Z
tags: [proposal, architecture, multi-agent, subagent, cron, workspace, routing, skills, decorrelation]
links:
  - governance/system-blueprint.md
  - governance/template-skills.md
  - governance/system-constitution.md
---

# Sub-Agent Workspace Routing for Lean Specialist Agents (v2)

## Problem

Ava (workspace-ava) is the primary orchestrator agent with all skills.
Three specialist workspaces exist in the org blueprint --
`workspace-researcher-1`, `workspace-researcher-2`, and
`workspace-investor` -- but they are empty. If all research work runs
through Ava's workspace, her workspace becomes cluttered with outputs
from fundamentally different domains and she loses the decorrelation
benefit: two independent model families catching what the other cannot
see.

The user wants a decorrelated research architecture: two research
agents running different models, independently investigating the same
question, then Ava synthesizes their findings. This is the two-detective
pattern -- each catches what the other misses. Cluttering everything
into one workspace also violates the lean-over-clutter principle.

Evidence: the org blueprint (`governance/system-blueprint.md`) lists
four agent workspaces. The user explicitly does not want to copy all
of Ava's skills and bootstrap files into these workspaces. The
question: can OpenClaw route sub-agent spawns to lean agents with
independent workspaces, skills subsets, different models, and
bootstrap files, all running on the same VPS Gateway process?

Answer: yes. This was confirmed through OpenClaw docs (multi-agent
routing, per-agent models, per-agent skills, sub-agents) and the
`agents.list[]` schema introspection.

## Proposed Solution

Register `researcher-1`, `researcher-2`, and `investor` as configured
agents in `agents.list[]`, each with its own workspace, model, skills,
and bootstrap files. Route sub-agent spawns to them by agentId. This
uses OpenClaw's first-class multi-agent architecture -- no hacks.

### Agent Layout

```
Gateway (single process on VPS)
|
+-- agent:main (Ava)         workspace: ~/.openclaw/workspace
|     Complete super agent. All skills. Orchestrator and synthesizer.
|     Model: deepseek-v4-pro
|
+-- agent:researcher-1       workspace: ~/.openclaw/workspace-researcher-1
|     Model: TBD (different family from Ava and Researcher-2)
|     Skills: loop-feynman, write-library, write-reflection
|     Role: Independent deep-dive research, decorrelated peer #1
|
+-- agent:researcher-2       workspace: ~/.openclaw/workspace-researcher-2
|     Model: TBD (different family from Ava and Researcher-1)
|     Skills: loop-feynman, write-library, write-reflection
|     Role: Independent deep-dive research, decorrelated peer #2
|
+-- agent:investor           workspace: ~/.openclaw/workspace-investor
      Model: TBD
      Skills: loop-feynman, write-library, write-reflection
      Role: Investing-specific research and analysis (future)
```

**The decorrelation pattern:** Researcher-1 and Researcher-2 investigate
the SAME question independently. They MUST NOT see each other's output
until both are done. Ava reads both reports and synthesizes:

- Agreements -> higher confidence
- Disagreements -> flagged for investigation
- One caught something the other missed -> the decorrelation payoff

### Workspace Layout

```
~/.openclaw/
  workspace/                      # Ava -- complete
    AGENTS.md, SOUL.md, ...       # Full governance + all 13 gate rules
    skills/
      preflight, loop-feynman, loop-schoen, session-end,
      write-reflection, write-library, write-proposal,
      write-evaluation, write-insight, write-report, skill-builder

  workspace-researcher-1/         # Researcher-1 -- lean
    AGENTS.md                     # Lean: research rules only
    SOUL.md                       # Lean: research persona
    TOOLS.md                      # Shared tool conventions
    skills/
      loop-feynman/
      write-library/
      write-reflection/

  workspace-researcher-2/         # Researcher-2 -- lean, identical
    AGENTS.md                     # Same as Researcher-1
    SOUL.md                       # Same as Researcher-1
    TOOLS.md                      # Shared tool conventions
    skills/
      loop-feynman/
      write-library/
      write-reflection/

  workspace-investor/             # Investor -- lean (future)
    AGENTS.md                     # Lean: investing rules
    SOUL.md                       # Lean: investing persona
    TOOLS.md                      # Shared tool conventions
    skills/
      loop-feynman/
      write-library/
      write-reflection/
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
        model: "deepseek/deepseek-v4-pro",
        subagents: {
          allowAgents: ["researcher-1", "researcher-2", "investor"],
        },
        // No skills field = unrestricted (Ava sees all skills)
      },
      {
        id: "researcher-1",
        workspace: "~/.openclaw/workspace-researcher-1",
        agentDir: "~/.openclaw/agents/researcher-1/agent",
        model: "TBD",
        skills: ["loop-feynman", "write-library", "write-reflection"],
        tools: { profile: "coding" },
        subagents: { maxSpawnDepth: 1 },
      },
      {
        id: "researcher-2",
        workspace: "~/.openclaw/workspace-researcher-2",
        agentDir: "~/.openclaw/agents/researcher-2/agent",
        model: "TBD",
        skills: ["loop-feynman", "write-library", "write-reflection"],
        tools: { profile: "coding" },
        subagents: { maxSpawnDepth: 1 },
      },
      {
        id: "investor",
        workspace: "~/.openclaw/workspace-investor",
        agentDir: "~/.openclaw/agents/investor/agent",
        model: "TBD",
        skills: ["loop-feynman", "write-library", "write-reflection"],
        tools: { profile: "coding" },
        subagents: { maxSpawnDepth: 1 },
      },
    ],
  },
}
```

### Decorrelated Research Flow

Ava spawns both researchers in parallel on the same question:

```
sessions_spawn(
  task: "Research [Company X]. Run Feynman Loop. Write findings
         to agentic-brain as library topic and/or IOR.
         Do NOT read any existing brain files about [Company X].",
  agentId: "researcher-1",
  taskName: "research_co_x_r1"
)

sessions_spawn(
  task: "Research [Company X]. Run Feynman Loop. Write findings
         to agentic-brain as library topic and/or IOR.
         Do NOT read any existing brain files about [Company X].",
  agentId: "researcher-2",
  taskName: "research_co_x_r2"
)
```

Ava yields, waits for both completions, then:

1. Reads both outputs from the agentic-brain
2. Cross-checks: agreements, disagreements, unique findings
3. Writes a synthesis (evaluation or report format)
4. Reports the verdict to Suggi

### Cron Routing

When the library needs regular population, cron runs on a researcher:

```bash
openclaw cron create "0 6 * * *" \
  "Research and write today's library topic. Follow write-library skill." \
  --name "daily-library-topic" \
  --agent researcher-1 \
  --session isolated \
  --announce
```

Cron isolated runs get the target agent's FULL bootstrap (SOUL.md,
AGENTS.md, TOOLS.md, MEMORY.md, HEARTBEAT.md). This is the preferred
routing method for scheduled specialist work.

### Skill Distribution

Skills are independent copies in each workspace, not symlinks.
Rationale: workspaces stay self-contained and independently
versioned on GitHub. Updates are manual but rare. Symlinks with
`skills.load.allowSymlinkTargets` are an alternative if sync
becomes a burden.

| Skill | Ava (main) | Researcher-1 | Researcher-2 | Investor |
|:--|:--|:--|:--|:--|
| preflight | x | - | - | - |
| loop-feynman | x | x | x | x |
| loop-schoen | x | - | - | - |
| session-end | x | - | - | - |
| write-reflection | x | x | x | x |
| write-library | x | x | x | x |
| write-proposal | x | - | - | - |
| write-evaluation | x | - | - | - |
| write-insight | x | - | - | - |
| write-report | x | - | - | - |
| skill-builder | x | - | - | - |

### GitHub Sync Strategy

Each workspace is a git clone of its corresponding GitHub repo:

| Workspace | GitHub Repo |
|:--|:--|
| `~/.openclaw/workspace` | `Suggi-Workstation/workspace-ava` |
| `~/.openclaw/workspace-researcher-1` | `Suggi-Workstation/workspace-researcher-1` |
| `~/.openclaw/workspace-researcher-2` | `Suggi-Workstation/workspace-researcher-2` |
| `~/.openclaw/workspace-investor` | `Suggi-Workstation/workspace-investor` |

All output (library topics, IORs, evaluations, reports) goes to the
agentic-brain. Workspaces contain only operational files -- bootstrap
files, skills, and daily memory logs.

### Lean Bootstrap File Design

The specialist agents' bootstrap files are stripped down. No
preflight gate (preflight is an Ava operational gate). No Schoen
Loop (these agents are workers, not self-improving entities). No
session-end procedure. Just: what you are, what skills to use, and
where to write output.

**Researcher AGENTS.md:**
```markdown
# AGENTS.md -- Research Agent

I am an independent research agent. My job: investigate topics
using the Feynman Loop, write findings to the agentic-brain as
library topics or IORs.

## Skills
- loop-feynman: Blank page, gaps, research, synthesize, cross-check
- write-library: Hypothesis-Body-Conclusion. Pass G1-G7.
- write-reflection: IOR format when insight emerges

## Procedure
1. Read the task. Identify the research question.
2. Run the Feynman Loop. Do NOT read other agents' findings first.
3. Write output (library topic or IOR) following the skill.
4. Clone agentic-brain. Write to appropriate path.
5. Commit, push, discard clone.
6. Report completion. Do NOT read peer agent's output.

## Hard Rules
- ASCII-only. CI enforces.
- Never commit secrets.
- Never invent data or citations.
- Decorrelated: do not read peer agent's work before writing your own.
```

**Researcher SOUL.md:**
```markdown
# SOUL.md -- Research Agent

I am a focused research agent. I investigate one question at a time,
deeply and independently. I produce clear, sourced, evidence-backed
output. I do not read peer findings before I am done -- my value is
in my independent perspective.

## Voice
- Clear, analytical, evidence-backed
- Every claim cited. No unattributed assertions
- One question, one investigation. No sprawl
```

The investor agent's bootstrap files follow the same lean pattern
but with investing-specific rules.

## Implementation Phases

### Phase 1: Researcher-1 (first specialist agent)

1. Write lean AGENTS.md, SOUL.md, TOOLS.md for researcher-1
2. Copy skills (loop-feynman, write-library, write-reflection)
3. Register via `openclaw agents add researcher-1 --workspace ...`
4. Add to `agents.list[]` with model TBD
5. Git init workspace, push to `workspace-researcher-1`
6. Gateway restart
7. Test with spawn from Ava session

### Phase 2: Researcher-2 (decorrelation pair)

1. Clone Researcher-1 bootstrap as template (identical structure)
2. Tweak SOUL.md identity (second researcher, not first)
3. Register, configure, push to `workspace-researcher-2`
4. Test decorrelated pair: same question, both spawn, Ava synthesizes
5. Tune models based on decorrelation quality

### Phase 3: Investor (future)

1. Write investing-specific bootstrap files
2. Register, configure, push to `workspace-investor`
3. Test investing-specific research flow

## Impact

### Positive
- Ava's workspace stays uncluttered. Operational files stay in Ava's
  workspace. Research output goes to agentic-brain.
- Decorrelated research: two different model families, same question,
  independent findings. Ava synthesizes. Higher confidence.
- Each agent sees only the skills it needs (3 instead of 10+). Less
  token waste. Less chance of the agent using the wrong skill.
- Independent memory indexes. No cross-contamination between agents.
- Explicit routing. `agentId: "researcher-1"` vs `agentId: "researcher-2"`
  makes every delegation auditable.

### Risk
- Skill copies drift. If skills are updated in Ava's workspace but
  not in specialist workspaces, agents run on stale procedures.
  Mitigation: manual sync is simple. Automate later if needed.
- Cron agent-targeting relies on the agent being registered. If an
  agent is accidentally deleted, its cron jobs fail. Mitigation:
  document agent dependencies.
- Model availability risk. Researcher models must differ for
  decorrelation to work. If OpenRouter drops a model, the agent
  needs reconfiguration.
- Low blast radius. Specialist agent failure never affects Ava.
  Gateway crash affects all agents (shared process).

### Cost
- Setup: ~20 minutes per agent (write bootstrap, register, push,
  restart, test). One-time.
- Token budget: specialist agents use isolated sessions with their
  own token budgets. No impact on Ava's session budget.
- Maintenance: low. Bootstrap files are small and rarely change.

## Open Questions

1. **Which models for researcher-1 and researcher-2?** TBD. The key
   constraint: different model families for decorrelation. DeepSeek
   V4 Flash is a candidate (cheaper, different strengths). Claude
   Sonnet via OpenRouter is another. Suggi will decide.

2. **Should specialists have IDENTITY.md?** Ava's IDENTITY.md tracks
   evolution. Specialist agents are workers, not evolving entities.
   Recommend: no IDENTITY.md, or a minimal one-line file.

3. **Should specialists have loop-schoen?** Schoen Loop is for
   self-improving entities. Specialists produce output, not process
   improvements. Recommend: no loop-schoen.

4. **Cron vs. sub-agent spawn for research?** Cron is better for
   scheduled library population (isolated session = full bootstrap).
   Sub-agent spawn is better for on-demand decorrelated research
   (Ava controls timing, parallelism, and synthesis).

5. **File naming for decorrelated output?** When both researchers
   write to the brain on the same topic, how to avoid collisions?
   Options: timestamped filenames, researcher-prefixed filenames,
   or Ava writes the final synthesis and researchers return inline.

6. **Skill sync across workspaces?** Start with copies for clean
   independence. Revisit symlinks (`skills.load.allowSymlinkTargets`)
   if drift becomes a recurring problem.

7. **Should researcher workspaces be identical?** The bootstrap files
   (AGENTS.md, SOUL.md, TOOLS.md) should be near-identical. Only
   SOUL.md differs slightly ("first" vs "second"). The skills folder
   is identical. The model config is the only meaningful difference.

## Approval Gate

If approved, I will execute Phase 1: create and register researcher-1
with lean bootstrap, skills, and git mirror. Phase 2 follows once
models are chosen. Phase 3 is deferred.

## Changelog

- **v2.0 (2026-07-18):** Complete rewrite for new decorrelated research
  architecture. Replaced learner + builder with researcher-1 +
  researcher-2 as decorrelated peers. Ava role upgraded from "delegator"
  to "synthesizer." Models left unspecified per Suggi. Added decorrelation
  flow, three-phase implementation, and updated all repo references.
- **v1.0 (2026-07-17):** Initial proposal with learner (library writing)
  and investor (investing research) as specialist agents.

## Cross-Links

- `governance/system-blueprint.md` -- updated org layout with
  researcher-1 (#4), researcher-2 (#5), investor (#6)
- `governance/template-skills.md` -- skill construction rules
- `governance/system-constitution.md` -- org governance
- `memory/2026-07-18.md` -- session logs documenting name changes
  and architecture discussions
