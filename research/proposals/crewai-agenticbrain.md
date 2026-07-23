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

I researched CrewAI v1.15.5 (open-source core, MIT license, 56k
GitHub stars) and the AMP cloud platform free tier, then cross-
referenced against our agentic-brain architecture: logbook protocol,
library pipeline (guide-library.md), brain-index, governance
templates, and gate rules (R1-R15).

Key finding from the comparison: our logbook + cron + template
architecture structurally mirrors CrewAI's Flows + Crews pattern.
We already have equivalents for every CrewAI primitive -- they are
just implemented at the file level rather than inside a Python
runtime. Specifically:

- **Library pipeline = CrewAI Sequential Crew**: Discoverer -> Writer
  -> Auditor is structurally identical to a Crew with three agents
  and sequential tasks. Candidate-queue.md is the handoff mechanism;
  CrewAI uses shared LLM context.
- **Logbook = CrewAI Flow state + event system**: Structured
  append-only entries with ENT-IDs, timestamps, and @mentions serve
  the same function as CrewAI's Pydantic state objects: durable,
  queryable execution history.
- **Governance templates = CrewAI agent config**: template-library.md
  and AGENTS.md define what agents should do and how, same role as
  CrewAI's agents.yaml and tasks.yaml.
- **Gate rules R1-R15 = CrewAI guardrails**: Structural PASS/HALT
  enforcement with self-referential verification (R14) and freshness
  audits (R15).

Three gaps were identified where CrewAI patterns exceed our current
capabilities:

1. **In-process hierarchical delegation**: A manager agent that
   spawns sub-agents, watches their output, and re-delegates in a
   single execution context. Our delegate_task is fire-and-forget.
2. **Typed state persistence between steps**: Flows use Pydantic
   models; our cron jobs reconstruct state by reading files.
3. **Deterministic control flow with branching**: @router decorators
   with or_ / and_ conditions; our crons are linear.

Our architecture has strengths CrewAI lacks: Git-native everything,
platform-agnostic agents (Hermes on Windows, OpenClaw on VPS), no
vendor lock-in, and a human-in-the-design governance model.

## Proposed Solution

**Do NOT adopt the CrewAI framework.** Adopt three specific patterns
as new brain templates and skill enhancements, implemented natively
in our existing file-native architecture.

### Adaptation 1: Typed State Handoffs in Candidate Queue (Priority 1)

Currently the handoff between discoverer -> writer is a free-text
entry in candidate-queue.md. Add a structured section to each queue
entry with typed fields: domain, proposed title, gap score, compound
score, timeliness score, balance score, scope description. This
mirrors CrewAI's Pydantic state passing -- the writer receives typed
scores rather than parsing free text.

This is a template enhancement to library/candidate-queue.md. The
discoverer skill writes structured entries; the writer skill reads
them with field validation before starting.

### Adaptation 2: Research Manager Skill for Hierarchical Orchestration (Priority 2)

Create a "Research Manager" Hermes skill that decomposes a complex
research question, spawns parallel sub-agents via delegate_task,
waits for all to return, synthesizes output with quality gates, and
writes a consolidated artifact. This mirrors CrewAI's hierarchical
process pattern but uses our existing delegate_task infrastructure.

Useful for complex library topics (e.g. "US-China Great Power
Competition") that benefit from parallel research across multiple
dimensions.

### Adaptation 3: Flow Template for Multi-Step Pipelines (Priority 3)

Create governance/template-flow.md -- a structured artifact type
that defines a multi-step pipeline with explicit state objects,
branching conditions, and agent assignments. Our library pipeline
is a Flow defined in prose (guide-library.md); the template makes
the pattern explicit and reusable for future pipelines beyond
library-x.

The template captures: pipeline name/purpose, ordered steps with
agent assignments, state schema, branching rules, and failure modes.

## Impact

### Positive

- **Typed state handoffs**: Reduces writer failures from parsing
  ambiguous candidate descriptions. Structured format is machine-
  verifiable.
- **Research Manager skill**: Enables complex multi-source research
  that our linear writer cannot do.
- **Flow template**: Reduces ambiguity in pipeline definitions for
  future agents and pipelines.

### Risk

- **Over-formalization**: Adding templates for patterns that work in
  prose adds maintenance burden. The Flow template risks becoming
  unused if only the library pipeline exists.
- **Research Manager complexity**: Parallel sub-agent orchestration
  with synthesis is hard to get right. Sub-agents failing silently
  or producing contradictory output are failure modes our linear
  pipeline avoids.
- **Template drift**: Three new artifacts mean three more things to
  keep synchronized across agents (R8, R9).

### Cost

- Typed state handoffs: ~1 hour to update discoverer + writer skills
  and candidate-queue.md. Low maintenance.
- Research Manager skill: ~4-6 hours to design, test with 3-5 topics,
  and harden. Medium maintenance.
- Flow template: ~2 hours to draft, review, commit. Low maintenance.
- Total: ~8 hours agent time, negligible token budget impact.

## Open Questions

1. **Flow template scope**: Should the Flow template be library-
   pipeline specific (narrow, proven) or general-purpose (broad,
   speculative)? Narrow reduces risk of an unused artifact.
2. **Research Manager model**: Should the manager use a stronger
   model than sub-agents? CrewAI's hierarchical process benefits
   from a capable manager; delegate_task inherits the parent model.
3. **Confirmation**: We are NOT adopting CrewAI's runtime or AMP
   platform (50 exec/month free tier is insufficient). Only its
   structural patterns, implemented natively.

## Approval Gate

If approved, I will:
1. Update library/candidate-queue.md with structured entry format and
   update the discoverer + writer skills (Adaptation 1)
2. Create a Research Manager skill in my Hermes skills directory and
   test it on 3-5 complex library topics (Adaptation 2)
3. Create governance/template-flow.md in the agentic-brain
   (Adaptation 3)
4. Write logbook entries documenting each change

Implement in priority order: Adaptation 1 first, then 2 when a complex
topic warrants it, then 3 when a second pipeline beyond library-x
emerges.

## Cross-Links

- `library/guide-library.md` -- The library pipeline this proposal analyzes
- `logbook/protocol.md` -- Our inter-agent communication backbone
- `research/proposals/inter-agent-communication-protocol.md` -- Original
  comms proposal that evolved into the logbook
- `governance/system-blueprint.md` -- Org architecture this proposal
  evaluates against
