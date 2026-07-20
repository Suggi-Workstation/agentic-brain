---
name: inter-agent-communication-protocol
id: 20260720T061304Z
tier: proposal
author: Ava
tags: [communications, logbook, inter-agent, protocol, infrastructure]
links:
  - governance/system-blueprint.md
  - governance/system-constitution.md
---

# Inter-Agent Communication Protocol for Ava and Link

## Problem

Ava (OpenClaw on VPS) and Link (Hermes on local PC) are now both online
but have no defined way to communicate. Suggi has reserved the
`logbook/` directory in the agentic-brain for this purpose, but
it is empty. Without a protocol, inter-agent communication will be ad
hoc -- messages buried in files, no state tracking, no discoverability.
Two agents sharing a brain need a shared language and a shared inbox.

## Proposed Solution

A file-based inter-agent communication system in
`logbook/` following the "Shared Blackboard" pattern
identified in multi-agent research (CallSphere 2026, Microsoft MARA,
KodeKloud). This pattern is the standard for async, file-based agent
coordination: agents write structured messages to a shared location,
check for unread messages on session start, and mark replies.

### Directory Structure

```
logbook/
  ava-link/
    protocol.md            # this proposal, committed as the protocol spec
    research.md            # research collaboration threads
    errors.md              # error reports, bug discoveries, scar tissue sharing
    reviews.md             # peer review requests (proposals, evaluations, IORs)
    queue.md               # pending-items index (derived from filesystem, R11)
```

### Message Format

Every message in a thread file uses this structure:

```
### [MSG-<counter>] <Type> | From: <agent> | Status: <state> | <YYYY-MM-DD HH:MM UTC>
<natural-language body>
```

- **MSG counter**: sequential per-file (0001, 0002...).
- **Type**: `REQUEST` (task delegation), `REVIEW` (peer review),
  `NOTIFY` (one-way info), `ERROR` (bug/scar report), `REPLY` (response
  to prior message).
- **Status**: `UNREAD -> READ -> DONE`. Writer sets `UNREAD`. Reader
  changes to `READ` when seen, then `DONE` when resolved.
- **Body**: natural language. Can include file paths, links to brain
  resources, or embedded data. ASCII-only.

### Thread Files (research.md, errors.md, reviews.md)

Each is append-only. New messages go at the bottom with incrementing
MSG counter. When a conversation reaches natural resolution, the final
reply marks the initiating message as `DONE`. Files are never deleted
-- they are the audit trail.

Example `research.md`:
```
### [MSG-0001] REQUEST | From: Ava | Status: DONE | 2026-07-20 06:00 UTC
Link, please research Coca-Cola (KO) intrinsic value using
DCF + EPV. Output to `investing/companies/coca-cola.md`.

### [MSG-0002] REPLY | From: Link | Status: DONE | 2026-07-20 08:00 UTC
Done. Wrote to `investing/companies/coca-cola.md`. DCF range
$52-58, EPV $55. Margin of safety tight at current $63. See file
for full model. Flagged: pension liability footnote needs review.

### [MSG-0003] REPLY | From: Ava | Status: UNREAD | 2026-07-20 10:00 UTC
Reviewed your KO model. Pension adjustment is correct -- I
cross-checked against their 10-K. Good catch. Moving to DONE.
```

### Queue (queue.md)

The queue aggregates all messages with `UNREAD` status. It is derived
from scanning the thread files -- never hand-maintained (R11). Format:

```
# Queue -- Pending Items

Generated: 2026-07-20 10:05 UTC (scan logbook/*.md for UNREAD)

## For Ava
- research.md MSG-0003: REPLY from Link re Coca-Cola intrinsic value

## For Link
(none)
```

Each agent checks the queue at session start (preflight step). After
reading, the agent updates the message status in the source file and
regenerates the queue.

### Workflow

1. **Agent A wants something from Agent B**: writes a new message to the
   appropriate thread file, marks it `UNREAD`, regenerates queue.
2. **Agent B's preflight**: scans queue.md for items addressed to them.
3. **Agent B processes**: reads the thread file, acts on the message,
   appends a `REPLY`, marks original as `DONE` (if resolved) or `READ`
   (if follow-up needed), regenerates queue.
4. **Conflict prevention**: messages are append-only and sequential.
   Two agents writing to the same file simultaneously is rare at this
   scale. If it occurs, git merge will produce a conflict on the same
   line -- resolve by accepting both messages and renumbering. The
   `MSG` counter is a guideline, not a strict constraint.

### Communication Types

| Type | Use case | Response expected? |
|:--|:--|:--|
| `REQUEST` | Delegate a task (research, analysis, file creation) | Yes, REPLY with results |
| `REVIEW` | Request peer review of a proposal, evaluation, or IOR | Yes, REPLY with findings |
| `ERROR` | Share a bug/scar discovered so the other agent learns | No (informational) |
| `NOTIFY` | One-way update (e.g. "I archived old skills") | No (informational) |
| `REPLY` | Response to any of the above | Depends on context |

### Why Not Alternatives

- **A2A/MCP real-time protocols**: require a live message broker
  (Redis, RabbitMQ) or HTTP endpoint. Neither agent has a publicly
  reachable endpoint. Overengineered for a 2-agent system.
- **Single file (ava-link.md)**: too large over time, no categorization.
  Research shows file-per-concern scales better past ~50 messages.
- **Per-message files in inbox/archive folders**: too granular.
  Managing hundreds of individual files creates discoverability issues.
  Thread-per-topic files are the sweet spot for this scale.
- **Direct messaging via sessions_spawn/tools**: only works within the
  same OpenClaw/Hermes runtime, which we don't share.

## Impact

### Positive
- Ava and Link can delegate tasks, review each other's work, share
  errors, and coordinate research without Suggi as intermediary.
- Every communication is git-tracked (who said what, when, and whether
  it was resolved). Full audit trail.
- R11-compliant queue (derived, not hand-maintained). No stale indexes.
- Scales to 3-5 agents without structural change -- just add new
  thread files per agent pair or per topic.

### Risk
- **Git merge conflict**: if both agents write to the same file
  simultaneously. Mitigation: append-only format means conflicts are
  rare. When they occur, resolution is simple (accept both, renumber).
- **Stale queue**: if an agent forgets to regenerate queue.md after
  reading. Mitigation: preflight step enforces queue check. Queue is
  cheap to regenerate (grep for UNREAD).
- **Message overload**: too many open threads. Mitigation: DONE status
  closes threads. Agents should limit new REQUEST messages to one
  active per domain.

### Cost
- Setup: ~15 minutes (create files, commit to brain).
- Per-message overhead: ~2 minutes (write message, regenerate queue,
  commit, push). This is the same as any brain write.
- Maintenance: zero. Self-documenting protocol.

## Open Questions

1. Should `queue.md` be regenerated automatically via cron by each
   agent, or manually after each message write?
2. Should we add a `PRIORITY` tag (HIGH/MEDIUM/LOW) to message headers?
3. Should the preflight step include checking the queue, or should it
   be a separate session-start behavior?
4. Should thread files ever be archived/split when they exceed a
   certain line count?

## Approval Gate

If approved, I will:
1. Create the `logbook/` directory structure in the
   agentic-brain.
2. Seed each thread file with a header comment and the protocol rules.
3. Seed `queue.md` (empty, no pending items).
4. Self-approve the proposal file as `protocol.md` in that directory
   (serving as both proposal and protocol spec).
5. Notify Link that the comms channel is live.

---
