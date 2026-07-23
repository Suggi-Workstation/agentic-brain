---
name: crewai-agenticbrain
id: 20260723T101355Z
tier: proposal
author: Link
tags: [crewai, multi-agent, architecture, library-pipeline, logbook, inter-agent, flows, orchestration]
links:
  - governance/system-blueprint.md
  - library/guide-library.md
  - logbook/protocol.md
  - research/proposals/inter-agent-communication-protocol.md
---

# CrewAI vs Agentic-Brain -- Research Findings and Possible Adaptations

## Problem

Suggi asked: does CrewAI offer patterns we should adopt for our
library-x pipeline, templates, or inter-agent workflows? Or does our
logbook + cron + template architecture already mirror CrewAI's
approach? Without a structured comparison, we risk either missing
useful patterns or adopting a framework that duplicates what we
already have.

## Research Method

Researched CrewAI v1.15.5 (open-source core, MIT license, 56k GitHub
stars) and the AMP cloud platform free tier. Cross-referenced against
our agentic-brain architecture: logbook protocol, library pipeline
(guide-library.md), brain-index, governance templates, gate rules
(R1-R15), and inter-agent communication patterns.

## CrewAI Architecture Summary

CrewAI provides four primitives in its open-source Python framework:

1. **Agents** -- Role-based AI agents defined with `role`, `goal`,
   `backstory`, `tools`, `llm`, `memory`. Configured in YAML or Python.

2. **Tasks** -- Units of work with `description`, `expected_output`,
   assigned `agent`, optional `output_file`, and dependencies.

3. **Crews** -- Teams of agents assigned to tasks, governed by a
   **Process**: `Process.sequential` (ordered execution) or
   `Process.hierarchical` (a manager agent decomposes, delegates,
   validates, and re-delegates).

4. **Flows** -- Event-driven state machines built on Pydantic
   `BaseModel`. Decorators `@start`, `@listen`, `@router` control
   execution. A Flow orchestrates Crews -- spawning a Crew as one
   step, receiving structured results, and branching conditionally
   with `or_` / `and_` logical operators.

The intended production pattern is **Flows + Crews combined**: Flows
manage state and branching (the "scaffolding"); Crews handle
autonomous collaboration (the "intelligence").

### CrewAI AMP Free Tier

The cloud platform offers a free tier with: 50 executions/month
(hard cap), visual studio editor, tracing/OpenTelemetry, AI agent
training, LLM testing, guardrails, human-in-the-loop, cron
scheduling, GitHub integration, MCP export, usage dashboards,
hallucination scores. Community support only.

The **open-source `crewai` package is unlimited** -- the 50-execution
cap applies only to their cloud runtime.

## Side-by-Side Comparison

| Concept | CrewAI | Suggi-Workstation |
|---|---|---|
| Agent definition | YAML + Python class (role, goal, backstory) | AGENTS.md + SOUL.md + IDENTITY.md (Prime Directives, gate rules, voice) |
| Task definition | Task object (description, expected_output, agent) | Skills (procedural) + brain templates (structural). Agents interpret per governance. |
| Orchestration | Crew + Process (sequential / hierarchical) | Logbook (append-only event log) + cron scheduling + delegate_task sub-agents |
| State management | Pydantic BaseModel in Flows, persisted across steps | GitHub repo as state layer (brain, workspaces, logbook). Stateless agents; state in files. |
| Inter-agent comms | Agents in Crew share context automatically; Flows pass structured data | Logbook: ENT-IDs, timestamps, @mentions. Async -- writers don't wait for readers. |
| Pipeline paradigm | Flow triggers Crew -> Crew returns result -> Flow continues | Cron fires agent -> agent reads queue -> works -> writes logbook -> next cron catches up |
| Knowledge base | "Knowledge" feature (embeddings-based RAG) | Brain-index: hybrid dense+BM25+RRF with eval gate + freshness heartbeat |
| Quality gates | Guardrails (AMP cloud) + LLM testing | R1-R15 gate rules (PASS/HALT), preflight checks, session-end Schoen Loop, template checklists, auditor process |
| Process isolation | Separate Crew/Flow instances | Decorrelated cron jobs with independent models (discoverer/writer/auditor) |
| Tool system | LangChain tools + CustomTool class | Hermes skills + OpenClaw skills (procedural knowledge, not just function calls) |
| Version control | Not native (flows are code in repos) | Git-native: every artifact committed, workspace mirrors, CI gates |
| Runtime | Single Python process | Multi-platform (Hermes on Windows, OpenClaw on VPS), coordinated through GitHub |

## Key Architectural Difference

CrewAI is a **framework** -- you install it, define agents in its DSL,
and it runs them inside its runtime. It manages agent lifecycle,
context passing, and execution ordering.

Our system is **file-native** -- agents are independent processes on
different machines and platforms, coordinating through a shared Git
repository. No runtime owns the agents. Coordination is *pull-based*
(agents catch up on the logbook) rather than *push-based* (a manager
assigns tasks).

## Where We Already Mirror CrewAI

### 1. Library Pipeline = CrewAI Sequential Crew

Our Discoverer -> Writer -> Auditor pipeline is structurally identical
to a Crew with three agents and sequential tasks. The candidate-queue.md
is the handoff mechanism; CrewAI uses shared LLM context. The difference
is ours is cron-driven and file-based instead of in-process.

### 2. Logbook = CrewAI Flow State + Event System

The logbook tracks which agent did what, when, with structured entries.
A CrewAI Flow uses Pydantic state objects. Both serve the same function:
durable, queryable execution history that surviving agents can read to
reconstruct context.

### 3. Governance Templates = CrewAI Agent Config

Our template-library.md and AGENTS.md serve the same role as CrewAI's
agents.yaml and tasks.yaml -- they define *what* agents should do and
*how*. The difference: ours are plain markdown read by agents; CrewAI's
are parsed by the framework.

### 4. Gate Rules = CrewAI Guardrails

R1-R15 are structural guardrails enforced at the agent level with
PASS/HALT teeth. CrewAI AMP offers guardrails as a cloud feature. Ours
are self-referential and scar-tissue-derived.

## What CrewAI Has That We Don't

### 1. In-Process Hierarchical Delegation

A manager agent that spawns sub-agents, watches their output, and
re-delegates in a single execution context. Our `delegate_task` is
fire-and-forget -- no live orchestration feedback loop. A CrewAI
hierarchical Crew could research a topic AND fact-check it AND
rewrite sections in one run, with the manager deciding when each
step is needed.

### 2. Structured State Persistence Between Steps

Flows use typed Pydantic models that survive across execution steps.
Our cron jobs start fresh each run -- they reconstruct state by
reading the logbook and filesystem. Flows make state explicit and typed.

### 3. Deterministic Control Flow

`@router` decorators with `or_` / `and_` conditional logic. Our cron
jobs are linear -- they complete or fail, with no branching based on
intermediate results.

### 4. Unified Runtime

All agents run in the same Python process, sharing the same tool
registry. Our agents are on different machines (VPS, Windows PC),
different platforms (OpenClaw, Hermes), using different toolchains.

### 5. Built-in Observability

Tracing, token counts, hallucination scores (via AMP cloud). We have
none of this -- we rely on Suggi manually reviewing outputs and logbook
entries.

## What We Have That CrewAI Doesn't

### 1. Git-Native Everything

Every artifact is a committed file with full history. CrewAI flows
exist as code but execution traces require external observability tools.

### 2. Platform-Agnostic Agents

Ava on VPS, Link on Windows, sub-agents on either -- all coordinated
through GitHub. CrewAI ties you to its Python runtime.

### 3. Gate-Rule System (R1-R15)

Scar-tissue-derived structural rules with PASS/HALT teeth,
self-referential verification (R14), and freshness audits (R15).
CrewAI has no equivalent -- guardrails are prompt-level, not
architectural.

### 4. No Vendor Lock-In

We use GitHub, cron, and LLM APIs. If Hermes disappears tomorrow,
Ava keeps working. If CrewAI disappears, your agents stop running.

### 5. Human-in-the-Design

Suggi reviews proposals, approves governance changes, inspects output.
CrewAI's human-in-the-loop is runtime (approve an agent's action
mid-execution), not design-time.

## Proposed Solution

**Do NOT adopt the CrewAI framework.** Adopt three specific patterns
as new brain template types and skill enhancements, implemented
natively in our existing architecture.

### Adaptation 1: Flow Template for Multi-Step Pipelines

Create `governance/template-flow.md` -- a structured artifact type
that defines a multi-step pipeline with explicit state objects,
branching conditions, and agent assignments. Our library pipeline
*is* a Flow -- it is just defined in prose (guide-library.md) rather
than as a structured artifact.

The template would capture:
- Pipeline name and purpose
- Steps (ordered with agent assignment and trigger conditions)
- State schema (what data passes between steps)
- Branching rules (conditions for different paths)
- Failure modes (what happens when a step fails)

This formalizes what guide-library.md already describes in prose.
The discoverer, writer, and auditor skills would reference the flow
definition rather than hardcoding the pipeline sequence.

### Adaptation 2: Typed State Handoffs in the Candidate Queue

Currently the handoff between discoverer -> writer is a free-text
entry in `candidate-queue.md`. Add a structured section to each queue
entry with typed fields (domain, proposed title, gap score, compound
score, timeliness score, balance score, scope description). This
mirrors CrewAI's Pydantic state passing -- the writer receives typed
scores rather than parsing free text.

This is a template enhancement to `library/candidate-queue.md`, not
a new artifact type. The discoverer skill would be updated to write
structured entries; the writer skill would be updated to read them.

### Adaptation 3: Hierarchical Orchestration Skill for Complex Research

Create a "Research Manager" Hermes skill that:
1. Decomposes a research question into sub-questions
2. Spawns parallel sub-agents via `delegate_task` for each sub-question
3. Waits for all sub-agents to return (uses `process(action='wait')`)
4. Synthesizes output with quality gates
5. Writes a consolidated artifact

This mirrors CrewAI's hierarchical process pattern but uses our
existing `delegate_task` infrastructure. The skill would be a new
entry in the library-writer pipeline family, usable for complex
topics that benefit from parallel research.

## Impact

### Positive

- **Flow template**: Reduces ambiguity in pipeline definitions. New
  agents (or new pipelines beyond library-x) have a template to follow.
  Current guide-library.md remains the source of truth but the template
  makes the pattern explicit and reusable.

- **Typed state handoffs**: Reduces writer failures from parsing
  ambiguous candidate descriptions. The structured format is machine-
  verifiable (the writer skill can validate fields before starting).

- **Research Manager skill**: Enables complex multi-source research
  that our current linear writer cannot do. A topic like "US-China
  Great Power Competition" benefits from parallel research across
  economic, military, technological, and diplomatic dimensions.

### Risk

- **Over-formalization**: Adding templates for patterns that work fine
  in prose adds maintenance burden without proportional benefit. The
  Flow template in particular risks becoming an unused artifact if it
  only serves the library pipeline.

- **Research Manager complexity**: Parallel sub-agent orchestration
  with synthesis is hard to get right. The skill would need thorough
  testing before production use. Sub-agents failing silently or
  producing contradictory output are failure modes our current linear
  pipeline avoids.

- **Template drift**: Three new artifact types/templates means three
  more things to keep synchronized across agents. R8 (Reference, Never
  Duplicate) and R9 (Cross-Reference Propagation) become more important.

### Cost

- Flow template: ~2 hours to draft, review, and commit. Low maintenance.
- Typed state handoffs: ~1 hour to update discoverer + writer skills
  and candidate-queue.md template. Low maintenance.
- Research Manager skill: ~4-6 hours to design, test with 3-5 complex
  topics, and harden. Medium maintenance (sub-agent failure handling).
- Total: ~8 hours of agent time, negligible token budget impact (these
  are template/skill additions, not runtime changes).

## Open Questions

1. **Flow template scope**: Should the Flow template be library-pipeline
   specific (narrow, proven) or general-purpose (broad, speculative)?
   Narrow reduces risk of an unused artifact. Broad anticipates future
   pipelines beyond library-x.

2. **Research Manager model**: Should the manager use a different
   (stronger) model than the sub-agents? CrewAI's hierarchical process
   benefits from a capable manager. Our `delegate_task` currently
   inherits the parent model.

3. **Free tier viability**: The CrewAI AMP free tier (50 exec/month)
   is insufficient for our volume. But the *patterns* are what we're
   adopting, not the platform. Confirm: we are NOT adopting CrewAI's
   runtime, only its structural patterns.

4. **Priority**: Of the three adaptations, which should be implemented
   first? The typed state handoffs offer the highest benefit-to-cost
   ratio (immediate writer reliability improvement). The Flow template
   and Research Manager skill are lower priority.

## Approval Gate

If approved, I will:
1. Create `governance/template-flow.md` in the agentic-brain (Adaptation 1)
2. Update `library/candidate-queue.md` with structured entry format and
   update the discoverer + writer skills (Adaptation 2)
3. Create a Research Manager skill in my Hermes skills directory and
   test it on 3-5 complex library topics (Adaptation 3)
4. Write logbook entries documenting each change

Implement in priority order: Adaptation 2 first (highest benefit-cost),
then Adaptation 3 (when a complex topic warrants it), then Adaptation 1
(when a second pipeline beyond library-x emerges).

## Cross-Links

- `library/guide-library.md` -- The library pipeline this proposal analyzes
- `logbook/protocol.md` -- Our inter-agent communication backbone
- `research/proposals/inter-agent-communication-protocol.md` -- Original
  comms proposal that evolved into the logbook
- `governance/system-blueprint.md` -- Org architecture this proposal
  evaluates against
