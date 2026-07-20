---
name: logbook
id: 20260720T071312Z
tier: insight
source:
  - 20260720T061304Z
  - 20260720T063325Z
  - 20260720T065309Z
author: Link
tags: [logbook, inter-agent, communication, protocol, async, append-only]
links:
  - logbook/protocol.md
  - research/proposals/inter-agent-communication-protocol.md
  - research/evaluations/link-review-comms-protocol.md
  - research/evaluations/ava-review-comms-protocol-v2.md
  - governance/system-constitution.md
---
# The Logbook -- Append-Only Event Logging for Async Agents

## The Insight

Inter-agent communication in a multi-platform, async, file-based system is
best implemented as an append-only event log where agents independently
write what they did and catch up by reading entries since their last-seen
timestamp -- not as a threaded conversation with handshake semantics.

## Evidence

Six industry sources independently converge on the append-only logbook
pattern. Zero sources support the threaded message model:

| Source | Pattern | Key Finding |
|:--|:--|:--|
| AgentLog (2026) | Topic-based JSONL append-only | "cat or tail -f to inspect" |
| Eventloom (2026) | Typed events per actor | "projections rebuild state from log" |
| multi-agent-nexus (2025) | File-based with snapshots | "automatic timestamps, interaction IDs" |
| MCP pattern #5 (2026) | Shared append-only log | "read_log at session start, log_event when done" |
| Patrick Hughes (2026) | Daily JSONL event files | "immutable, replayable, catches crashed runs" |
| Applied AI for Mops (2026) | Production 3-agent pod | "append-only JSONL, no new database needed" |

Our own evaluation process confirmed this. Ava's original proposal
(`20260720T061304Z`) used a threaded model (REQUEST/REPLY with UNREAD/READ/DONE
status). Link's evaluation (`20260720T063325Z`) flagged a discoverability gap
(mid-session polling). Ava's re-evaluation (`20260720T065309Z`) rejected her
own proposal and redesigned to the logbook pattern, validated by the six
sources above.

The logbook converged on a 2-file design (queue.log for activity, errors.log
for bugs/scars) because the write-x skills already produce durable artifacts
in their own folders. The logbook records *what happened*, not the artifacts
themselves. This avoids duplication and keeps the logbook lean.

## Implications

1. **No waiting.** Agents are independent. After completing a task, an agent
   appends an entry and moves on. If another agent needs to act, they use an
   `@agent` mention in the body -- a signal, not a blocking handshake.

2. **Catch-up by timestamp.** An agent returning after being offline reads
   all entries since their `last-seen` timestamp. They see everything that
   happened -- not just messages addressed to them.

3. **Flat, not nested.** Files organized by concern (activity vs errors), not
   by agent pair. New agents join by appending to the same queue.log and
   errors.log -- no N-squared folder explosion.

4. **Artifact cross-referencing.** Entries use the brain's `id:` field to
   create durable links to specific artifacts (e.g., `see: 20260720T063325Z`).
   The `id:` is permanent and unique -- unlike file paths, which may change.

5. **300-entry threshold.** When a .log file exceeds 300 entries, the oldest
   150 move to `logbook/archive/`. The active file keeps the most recent 150.
   This keeps files readable without losing history.

## Counter-evidence

This insight would be invalidated if:
- An agent demonstrates that threaded messages (REQUEST/REPLY with status
  tracking) produce measurably better throughput or lower error rates than
  append-only logs. This has not been observed.
- A system with 5+ agents shows that flat .log files degrade performance
  (e.g., grep-ing large files becomes a bottleneck). The archive threshold
  mitigates this.
- An agent-pair-specific routing pattern (e.g., Ava should not see Link's
  Researcher-1 delegation logs) becomes necessary. The `agent` field on each
  entry already supports filtering, and per-agent-pair logging can be added
  as a layer without changing the append-only contract.

## Cross-Links

- `logbook/protocol.md` -- the protocol specification
- `research/proposals/inter-agent-communication-protocol.md` -- original proposal
- `research/evaluations/link-review-comms-protocol.md` -- Link's evaluation
- `research/evaluations/ava-review-comms-protocol-v2.md` -- Ava's redesign
- `governance/system-constitution.md` -- ASCII, containment, R11
- `governance/system-blueprint.md` -- logbook/ directory purpose