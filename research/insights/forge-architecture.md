---
name: forge-architecture
id: 20260811T172352Z
tier: insight
source:
  - 20260801T000008Z
author: Link
tags: [forge, agent-architecture, autonomous-agent, research-pipeline, state-persistence, maker-checker, self-learning, provenance]
links:
  - research/insights/harness-engineering.md
  - research/insights/loop-engineering.md
  - research/insights/agent-evolution.md
  - research/insights/context-engineering.md
  - governance/system-constitution.md
---

# The Forge Architecture: A Resumable Research Agent Is a Filesystem With a Pipeline, Not a Model in a Loop

## The Insight

A durable, self-learning research agent is not a model running a loop; it is a shared filesystem with a gated six-stage pipeline, a maker-checker verification boundary, and a resumable state layer that outlives every context window.

## Evidence

The agentic forge (repo `Suggi-Workstation/agentic-forge`, protocol id `20260801T000008Z`, deployed to `/srv/forge/agentic-forge` on suggi-vps, owned `root:agents` like the brain) implements a six-stage pipeline: IDEA -> RESEARCH -> EVALUATE -> PROPOSE -> VALIDATE -> INSIGHT. Every stage produces an immutable artifact with a `parent` field forming a full provenance chain from insight back to origin idea. Every stage transition is a binary gate: PASS advances, HALT pivots or buries in `graveyard/` with a post-mortem. Seven skills drive it: forge-ideate, forge-research, forge-evaluate, forge-propose, forge-validate, forge-insight, forge-verify.

Two design properties make this architecture sound rather than merely elaborate:

1. **State lives outside the context window.** The agent is amnesiac between sessions; the filesystem is not. Artifacts, provenance chains, and git history carry the work forward. This matches the consensus of long-running agent engineering (Addy Osmani's long-running agents analysis, Anthropic's long-running Claude work, the Ralph loop pattern): finite context is the first wall every long-running agent hits, and the answer is checkpointed external state, not a bigger window.

2. **The evaluator is separated from the generator.** forge-verify orchestrates a maker-checker gate: an independent reviewer with a different model and zero shared context reads the artifact cold and renders APPROVE, FLAG, or REJECT. Anthropic's harness research identifies self-grading as a primary failure mode; separate-evaluator verification is the countermeasure. The forge has this built in, which places it ahead of most published agent-loop designs.

The gap analysis against the same body of research identified one structural weakness: the forge lacks an explicit state layer. The protocol instructs the loop to "read the active pipeline state" but defines no file that holds that state. The Ralph loop and Memory Bank patterns all converge on three files outside the artifact pipeline: a status file (where am I, what is next), a journal (chronological lab notes), and a learnings file (rolling operational rulebook). Without them, a crash or context reset strands the agent mid-pipeline with no way to resume.

## Implications

1. **Build Neo as a filesystem-first agent.** His operational core is the forge loop: read ANCHOR.md, read the active pipeline state, advance one stage, write the artifact, pass forge-verify, commit, push. His AGENTS.md defines the loop contract; the forge repo holds the work product; his workspace stays lean.

2. **Add the three-file state layer to the forge.** `forge/STATUS.md` (current pipeline position, active artifact, next action), `forge/JOURNAL.md` (append-only chronological lab notes), `forge/LEARNINGS.md` (operational lessons about how research is done, distinct from `forge/insights/` which holds domain principles). Session bookends: read all three at loop start (boot injection), update them at loop end (checkpoint).

3. **ANCHOR.md stays, and is the domain control.** It is already wired into forge-ideate ("the idea MUST align with the anchor goal"). Renaming to MISSION.md would require touching the protocol and all seven skills for zero functional gain. The anchor file is the clean mechanism for deciding Neo's research domain later: edit the file, he re-anchors.

4. **Keep the fresh-start identity rule, but make IDENTITY.md the experimental record.** memory/ and identity/ folders stay empty at birth (no inherited history); Mnemosyne is seeded for knowledge. IDENTITY.md with the six-question evolution framework is not optional polish for an experimental agent: it is the measurable evidence that self-learning is occurring. Each evolution entry answers the six questions from his own experience.

5. **No preflight, no session-end; the loop replaces them.** The loop bookends (read state at start, write state at end) fulfill the same role for a solo research agent that preflight and session-end fulfill for fleet agents. What must not be lost is the gate discipline: the forge's binary PASS/HALT gates are the same philosophy as the fleet's HARD GATES, applied to research artifacts.

6. **Add stop conditions.** Long-running agent practice mandates max-iteration limits, time caps, and idle detection ("no commit in N iterations -> break"). An autonomous research loop without stop conditions can burn tokens indefinitely on a stalled question.

7. **Write completed insights into Mnemosyne.** Each pipeline that reaches the INSIGHT stage should also write a compact memory (private + shared surface) so recall works in addition to file search.

## Counter-evidence

This insight would be invalidated if:

- A forge agent completes multi-stage pipelines across sessions WITHOUT a STATUS/JOURNAL/LEARNINGS layer, with no detectable quality loss or rework (demonstrating the state layer is unnecessary). This has not been tested; the entire research consensus predicts failure.
- A self-graded artifact (author-only verification) achieves the same error-catch rate as independent maker-checker review across a statistically meaningful sample (demonstrating evaluator separation is over-engineering). The fleet's verification bottleneck insight (`research/insights/harness-engineering.md`, `loop-engineering.md`) already argues the opposite.
- The forge produces insights that prove untransferable or unactionable despite full provenance chains (demonstrating the pipeline's final gate is cosmetic). The first several completed pipelines will provide the data.
- A model with a sufficiently large context window runs the same research without external state and matches the forge's quality and resumability (demonstrating context solves what the filesystem was added to solve). No current model is close to this threshold for multi-day research.

## Cross-Links

- `forge/protocol.md` in repo `Suggi-Workstation/agentic-forge` (id `20260801T000008Z`) - the source protocol this insight analyzes
- `research/insights/harness-engineering.md` - harness-as-safety-mechanism, the verification boundary this extends
- `research/insights/loop-engineering.md` - loop width vs architecture, the loop-design counterpart
- `research/insights/agent-evolution.md` - identity/evolution versioning, the experimental-record principle
- `research/insights/context-engineering.md` - context rot and why external state is mandatory
- `governance/system-constitution.md` - the governance frame all agents, including a forge agent, operate under
