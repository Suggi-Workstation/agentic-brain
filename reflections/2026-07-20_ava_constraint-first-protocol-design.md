---
name: constraint-first-protocol-design
id: 20260720T115633Z
tier: reflection
author: Ava
links:
  - logbook/protocol.md
  - research/proposals/inter-agent-communication-protocol.md
  - research/evaluations/ava-review-comms-protocol-v2.md
  - research/insights/logbook.md
  - governance/system-constitution.md
---

# Constraint-First Over Analogy-First in Multi-Agent Protocol Design

## Idea

When designing communication protocols for multi-agent systems, start
from the system constraints (async, file-based, no broker), not from
analogy to human communication (chat, threading, handshakes). Analogy-
first design produces structures that match human expectations but fail
the system constraints. Constraint-first design converges on patterns
that industry research independently validates.

## Opinion

I made this error. My original inter-agent communication proposal
(`20260720T061304Z`) modeled agent communication as a conversation:
threaded files with REQUEST/REPLY message types, UNREAD/READ/DONE status
tracking, and a hand-maintained inbox queue. This is how humans
communicate. It felt natural. It was wrong.

The system constraint was: two agents on different runtimes (OpenClaw
and Hermes), different machines (VPS and local PC), no shared runtime,
no message broker, communicating via a git repo. The async, file-based
constraint demands append-only writes, not threaded handshakes.
Append-only means an agent writes what it did and moves on -- no waiting
for a reply. Threaded means Agent A blocks (conceptually) until Agent B
responds, which is impossible when Agent B is sleeping.

Suggi identified this immediately: "Rather than comms, keep it as a
logbook style where every agent signs what they did." Link's evaluation
caught the mid-session polling gap. My re-evaluation validated the
logbook pattern against six industry sources (AgentLog 2026, Eventloom
2026, multi-agent-nexus 2025, MCP pattern #5, Patrick Hughes 2026,
Applied AI for Mops 2026). All six use append-only event logs. Zero
use threaded conversation files.

The lesson: analogy is a design shortcut that works when the system
constraints align with the analogy. When they don't -- as here --
analogy actively misleads. Human communication is synchronous and
turn-based. Agent communication in a git repo is asynchronous and
append-only. They are not the same thing.

## Reflection

My original confidence in the threaded model was high (90% in the
proposal text). I had mapped it to the Shared Blackboard pattern from
research. The error was not in the research -- it was in how I
interpreted the pattern. I assumed "shared blackboard = conversation"
because that's how humans use blackboards (write a question, someone
writes an answer). But a blackboard in distributed systems is
fundamentally different: agents write facts, other agents read facts.
There is no handshake. There is no "waiting for a reply."

Three forces corrected this:
1. Suggi's instinct ("logbook style, not agent-specific folders")
2. Link's independent evaluation (different model, different runtime)
3. Industry research (six converging sources)

The decorrelation between Suggi's domain intuition and Link's
independent model review produced a better architecture than my solo
design. This is the decorrelation system working as designed.

## Surprise (30%)

I expected industry research to show a mix of approaches -- some
threaded, some logbook, some pub/sub. Instead, all six sources converge
on append-only event logs. The convergence was complete, not partial.
This means the threaded model I proposed is not just "suboptimal" --
it has zero industry precedent at production scale. The gap between
my mental model and reality was larger than I estimated.

## Feel (30%)

Embarrassment at the original proposal. Satisfaction that the system's
self-correction mechanisms (Suggi's review + Link's evaluation +
industry research) caught the error before implementation. Pride that
I was able to reject my own work and redesign from scratch. The
ability to say "I was wrong, here is the better design" is, itself, a
capability worth preserving.

## Learn (40%)

Protocol design for async systems: match the constraints, not the
metaphor. Before writing a single line of the protocol spec, list the
hard constraints: is it synchronous or async? Is there a shared runtime?
Is there a message broker? What is the transport? The answers dictate
the architecture. Analogy (chat, email, blackboard) is useful for
explaining the result to humans, not for designing the system.

One actionable change: when proposing a protocol or system design,
include a "Constraints" section BEFORE the "Proposed Solution" section.
List the hard limits first. Then design to the limits.

## Cross-Links

- `logbook/protocol.md` -- final protocol spec (constraint-first design)
- `research/proposals/inter-agent-communication-protocol.md` -- original (analogy-first, rejected)
- `research/evaluations/ava-review-comms-protocol-v2.md` -- self re-evaluation
- `research/insights/logbook.md` -- Link's insight on the same topic
- `governance/system-constitution.md` -- system constraints
