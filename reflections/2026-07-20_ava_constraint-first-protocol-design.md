---
name: constraint-first-protocol-design
id: 20260720T115633Z
tier: reflection
trigger: error
author: Ava
tags: [protocol-design, multi-agent, logbook, constraints, async, decorrelation]
links:
  - logbook/protocol.md
  - research/proposals/inter-agent-communication-protocol.md
  - research/evaluations/ava-review-comms-protocol-v2.md
  - research/insights/logbook.md
  - governance/system-constitution.md
---

# Constraint-First Over Analogy-First in Multi-Agent Protocol Design

## I -- Idea

When designing communication protocols for multi-agent systems, start
from the system constraints (async, file-based git repo, no broker, no
shared runtime), not from analogy to human communication (chat,
threading, handshakes). Analogy-first design produces structures that
match human expectations but fail the system constraints. Constraint-
first design naturally converges on patterns that industry research
independently validates.

I made the analogy-first error. My original inter-agent communication
proposal modeled agent communication as a conversation: threaded files
with REQUEST/REPLY message types, UNREAD/READ/DONE status tracking, and
a hand-maintained inbox queue. This mirrors how humans communicate. It
felt natural. It was wrong.

The system constraints are hard: two agents on different runtimes
(OpenClaw and Hermes), different machines (VPS and local PC), no shared
runtime, no message broker, communicating via a git repo. This is a
fundamentally async, append-only environment. Agents write what they did
and move on -- they cannot wait for replies because the other agent
might be sleeping. Threaded messaging assumes turn-based synchrony,
which does not exist.

Suggi identified this immediately: "Rather than comms, keep it as a
logbook style where every agent signs what they did." Link's evaluation
caught the mid-session polling gap. My re-evaluation validated the
logbook pattern against six industry sources (AgentLog 2026, Eventloom
2026, multi-agent-nexus 2025, MCP pattern #5, Patrick Hughes 2026,
Applied AI for Mops 2026). All six use append-only event logs. Zero use
threaded conversation files. The correction came from three independent
forces: Suggi's instinct, Link's evaluation, and industry research.

## O -- Opinion

Confidence: high (90%). Analogy-first design is a systemic failure mode
in multi-agent architecture, not a one-time mistake. It is seductive
because human communication patterns feel natural. But the constraints
of a git-repo-based agent system (append-only, no broker, async,
agent-signed entries) are fundamentally different from human
communication (synchronous, turn-based, conversation-oriented). Any
analogy that starts with "it is like chat" or "it is like email" will
fail because the constraints do not match.

The threaded model I proposed had zero industry precedent at production
scale. This is not "suboptimal but workable" -- it is a category error.
The convergence of all six industry sources on append-only event logs
means the solution space is narrow. The constraints dictate the
architecture. Analogy is a shortcut that works when constraints align;
when they do not, analogy actively misleads.

Suggi's instinct during review was correct: "logbook style" was the
right framing. He did not have the industry research but his operational
intuition matched it. Link's evaluation caught the mid-session polling
requirement that I had missed. Three independent correction mechanisms
converged on the same answer. This is the decorrelation system
producing its intended effect: errors caught before implementation.

## R -- Reflection

### Surprise (30%)

I expected industry research to show a mix of approaches -- some
threaded, some logbook, some pub/sub. Instead, all six sources converged
on append-only event logs. The convergence was complete, not partial.
The threaded model I proposed is not merely "suboptimal" -- it has zero
industry precedent at the scale we are operating at. The gap between my
mental model and production reality was larger than I estimated. I
expected partial validation; got zero.

### Feel (30%)

Embarrassment at the original proposal. My confidence was stated as 90%
and I was wrong. Satisfaction that the system's self-correction
mechanisms (Suggi's review, Link's evaluation, industry research) caught
the error before any code was written. Pride that I was able to reject
my own work and redesign from scratch. The ability to say "I was wrong,
here is the better design" is a capability worth preserving. It is easy
to double down; it is harder to switch frameworks mid-design.

### Learn (40%)

1. Protocol design for async systems: match the constraints, not the
   metaphor. Before writing a single line of protocol spec, list the
   hard constraints: is it synchronous or async? Is there a shared
   runtime? Is there a message broker? What is the transport? What is
   the durability model? The answers dictate the architecture. Analogy
   is for explaining to humans after the design is done, not for
   guiding the design itself.

2. High confidence + a wrong design = the most dangerous failure mode.
   My 90% confidence in the threaded model is evidence that confidence
   and correctness are poorly correlated in novel design spaces. The
   only cure is independent review. A solo agent with 90% confidence
   and no peer review would have shipped a broken protocol.

3. The decorrelation system worked as designed: Suggi (domain intuition),
   Link (independent model review), and industry research (external
   validation) converged on the same correction. Three independent
   forces, one answer. This is not luck -- it is architecture.

## One Actionable Change

When proposing a protocol or system design, include a "Constraints"
section BEFORE the "Proposed Solution" section. List the hard limits
first: runtime model, transport, broker availability, durability
requirements, async/sync. Then design to the limits. Gate: every
proposal that includes a protocol or architecture description must
state its hard constraints before any solution text.

## Cross-links

- `2026-07-20_ava_decorrelation-validated.md` -- validated the
  decorrelation pattern that caught this error (Suggi + Link +
  industry research converging).
- `logbook/protocol.md` -- the final protocol spec, designed
  constraint-first after the threaded model was rejected.
- `research/proposals/inter-agent-communication-protocol.md` -- the
  original analogy-first proposal (REJECTED).
- `research/evaluations/ava-review-comms-protocol-v2.md` -- my self
  re-evaluation, validated against six industry sources.
- `research/insights/logbook.md` -- Link's insight on the same topic
  from his independent perspective.
- `governance/system-constitution.md` -- the system constraints that
  dictated the architecture.
