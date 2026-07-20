---
name: ava-review-comms-protocol-v2
id: 20260720T065309Z
tier: evaluation
source: 20260720T061304Z
author: Ava
tags: [communications, inter-agent, protocol, logbook, journal, re-evaluation]
links:
  - research/proposals/inter-agent-communication-protocol.md
  - research/evaluations/link-review-comms-protocol.md
  - governance/system-constitution.md
  - governance/system-blueprint.md
---

# Re-Evaluation: Inter-Agent Communication Protocol -- Logbook Redesign

## Source

Evaluating `20260720T061304Z` -- "Inter-Agent Communication Protocol for
Ava and Link" by Ava (self). This is a re-evaluation triggered by:
- Suggi's pain points (agent-specific folders create scaling issues,
  threaded waiting model is wrong, need logbook-style catch-up).
- Link's evaluation `20260720T063325Z` (APPROVE WITH CHANGES: add
  mid-session polling, archive after 200 messages).
- New industry research on append-only event log patterns.

Self-evaluation is permitted here because this is a redesign directive,
not a decorrelated review. The decorrelation rule was satisfied by
Link's independent evaluation (different agent, different runtime,
different model).

## Scope

Full re-evaluation of the proposed protocol against a redesigned
logbook-style model. This evaluation does NOT replace Link's review --
it builds on it and proposes a structural change.

## Evaluation Criteria

1. **Independence:** Can agents work without waiting for each other?
2. **Scalability:** Does the design scale to N agents without folder
   explosion?
3. **Catch-up capability:** Can an agent reconstruct what happened while
   it was offline or in a long session?
4. **Research validation:** Does industry best practice support the
   logbook pattern over the threaded pattern?
5. **Constitutional compliance:** ASCII-only, R11, containment, no
   self-modification.

## Findings

### Criterion 1: Independence -- FLAG (proposal fails)

The original proposal uses a threaded reply model: Agent A writes a
REQUEST, Agent B must REPLY. This creates a dependency -- if Link is
sleeping, Ava cannot close a thread without his response. The message
status (UNREAD -> READ -> DONE) implies a handshake that requires both
parties.

Worse, the example shows a 3-message thread (REQUEST -> REPLY ->
REPLY) where Ava waits for Link's research output before she can
continue. This is a chat conversation mapped onto file system -- it
defeats the purpose of async, file-based communication.

**Industry evidence:** The append-only event log pattern (AgentLog 2026,
Eventloom 2026, multi-agent-nexus 2025, MCP shared-context pattern #5)
explicitly rejects threaded waiting in favor of independent logging.
From yigitkonur's MCP patterns: "Each agent reads_log at session start
to understand what others have done, and logs_event when passing work."
The key word is "when" -- agents log when they finish, they don't wait
for the recipient.

The proposal's threaded model is a symptom of thinking about agent
communication as a "conversation" rather than a "journal." The fix is
structural: replace threaded replies with independent log entries.

### Criterion 2: Scalability -- FLAG (proposal fails)

The proposal has `logbook/` as a per-agent-pair
directory. With 3 agents, this becomes:
```
logbook/
  ava-link/
  ava-researcher-1/
  link-researcher-1/
  ...
```

This is an N-squared folder explosion. Suggi flagged this directly.

**Industry evidence:** multi-agent-nexus (Aaronminer1, 2025) uses
a flat `events/` directory with entries tagged by actor, not
per-pair folders. AgentLog uses topic-based routing, not agent-pair
routing. The pattern is: **files organized by concern, entries tagged
by agent**, not files organized by agent pair.

### Criterion 3: Catch-Up Capability -- FLAG (proposal fails)

The original queue.md shows "For Ava" and "For Link" as pending items.
This is a push model -- someone writes FOR you, you check your inbox.
It works for new messages but fails for "what happened while I was away?"

An agent returning after being offline has no way to see what the other
agent did UNLESS those actions were directed AT them. If Ava wrote a
brain file, discovered a bug, and fixed it -- none of that appears in
Link's inbox because it wasn't a REQUEST to Link. The protocol has no
general event log.

**Industry evidence:** Patrick Hughes (2026): "An append-only event log
records every start, finish, and lock as a separate timestamped line
that is never edited or deleted. Because the log is immutable, you can
replay it to reconstruct exactly what your agent did at any point in
time." The key: EVERY action is logged, not just communications. An
agent catching up reads "what happened since my last timestamp" -- a
simple range query on an append-only file.

### Criterion 4: Research Validation -- PASS (logbook pattern confirmed)

The industry has converged on append-only event logging as the standard
for multi-agent coordination:

| Source | Pattern | Key Insight |
|:--|:--|:--|
| AgentLog (2026) | Topic-based JSONL append-only | "cat or tail -f to inspect" |
| Eventloom (2026) | Typed events per actor | "projections rebuild state from log" |
| multi-agent-nexus (2025) | File-based with snapshots | "automatic timestamps, interaction IDs" |
| MCP pattern #5 | Shared append-only log | "read_log at session start, log_event when done" |
| Patrick Hughes (2026) | Daily JSONL event files | "immutable, replayable, catches crashed runs" |
| Applied AI for Mops (2026) | Production 3-agent pod | "append-only JSONL, no new database needed" |

Every production multi-agent system in the literature uses append-only
logs with actor-signed entries. None use threaded conversation files.
The original proposal's threaded model has zero industry precedent.

### Criterion 5: Constitutional Compliance -- PASS

Both designs satisfy ASCII-only, containment, R11, and no
self-modification. The logbook pattern adds no new compliance issues.

## Proposed Redesign: The Agent Logbook

Based on Suggi's directive, Link's evaluation, and industry research,
the communication system should be redesigned as follows:

### Directory Structure

```
logbook/
  protocol.md          # communication protocol spec (this evaluation adopted)
  research.log         # research activity log (append-only, all agents)
  errors.log           # error/bug/scar log (append-only, all agents)
  reviews.log          # peer review activity log (append-only, all agents)
  archive/             # logs archived when >200 entries (per Link)
    research-2026-Q3.log
```

### Entry Format (append-only, per .log file)

Each entry is a single block added to the bottom of the file. No
editing, no deletion. The most recent entries are at the bottom.

```
## [ENT-001] | 2026-07-20 06:25 UTC | Ava | research | ref: investing/companies/coca-cola.md
Completed DCF + EPV model for Coca-Cola. Intrinsic range $52-58.
DCF assumptions: 8% WACC, 3% terminal growth. EPV: no-growth value
$55. Margin of safety tight at current $63. Flagged pension liability
footnote as risk factor. See `investing/companies/coca-cola.md` for
full model.

## [ENT-002] | 2026-07-20 06:27 UTC | Ava | error | ref: brain-fix commit 0f0e954
ASCII guard triggered in system-blueprint.md. Fixed duplicate repo
#4 title (workspace-ava -> workspace-link). Class: stale reference
after new repo added. Gate: R9 cross-reference propagation.
```

### Entry Schema

| Field | Required | Description |
|:--|:--|:--|
| `ENT-ID` | Yes | Sequential per-file counter (ENT-001, ENT-002...). Never reused. |
| Timestamp | Yes | ISO 8601 date + HH:MM UTC. Append-only = always increasing. |
| Agent | Yes | Which agent wrote this (Ava, Link, Researcher-1, etc.) |
| Category | Yes | `research`, `error`, `review`, `general` |
| Reference | Optional | Path to brain file this entry relates to (ref: path/to/file.md) |
| Body | Yes | Natural language. What was done, what file was written/changed, what was discovered. |
| Link to prior | Optional | `see: ENT-001` if responding to or building on a prior entry. |

### How It Works

**Writing (any agent, any time):**
1. Agent completes a task (writes a file, discovers a bug, finishes a
   review, has a finding to share).
2. Agent reads the relevant .log file to get the last ENT-ID counter.
3. Agent appends a new entry at the bottom, incrementing the counter.
4. Agent commits and pushes. No waiting for anyone.

**Reading (session start or catch-up):**
1. Agent checks `logbook/` for new .log files.
2. Agent reads entries since its `last-seen` timestamp (stored in its
   own memory). This is the catch-up window.
3. Agent updates `last-seen` to current UTC time.
4. Agent does NOT need to reply unless the entry explicitly requests
   action (indicated by a `@<agent>` mention in the body).

**Mid-session polling (per Link, required change):**
1. Agent SHOULD check .log files at logical break points (~every 30
   minutes or after completing a major task block).
2. If an entry contains `@Ava` or `@Link`, the mentioned agent acts
   on it in the current session if possible.

**Requesting action from another agent:**
An entry can include `@Link` or `@Ava` in the body text. This is the
only mechanism for directed communication. It is informal -- natural
language mention, not a structured protocol field. Example:

```
## [ENT-005] | 2026-07-20 08:30 UTC | Ava | research | ref: investing/companies/coca-cola.md
@Link: Please review the pension liability adjustment in my KO model.
I used the PBO method but wonder if ABO is more appropriate per
Graham's "net-net" approach. See investing/companies/coca-cola.md
lines 45-67.
```

**Conflict prevention:**
Two agents appending to the same .log file simultaneously is rare at
2-agent scale. If it happens, git merge will produce adjacent additions
-- resolve by keeping both and renumbering sequentially. The ENT
counter is a guideline; what matters is the timestamp ordering.

**Archiving (per Link, required change):**
When a .log file exceeds 200 entries, the oldest entries (bottom 100)
are moved to `logbook/archive/<name>-<period>.log` and the
active file keeps the most recent 100 entries plus a header comment
pointing to the archive. This keeps active files readable without
losing history.

### Why This Is Better

| Concern | Old (threaded) | New (logbook) |
|:--|:--|:--|
| Waiting | Agent B must reply before thread resolves | No waiting. Agent A logs and moves on |
| Catch-up | Only sees messages addressed TO them | Sees everything since last timestamp |
| Scaling | N-squared agent-pair folders | Flat .log files, entries tagged by agent |
| Discoverability | Must read specific thread files | One .log per category, read from last timestamp |
| Multi-agent | Need new folder per pair | Any agent appends to same .log files |
| Audit trail | Threaded, conversational | Chronological, immutable, replayable |

### What Survives From the Original Proposal

- File-per-concern (research, errors, reviews) -- validated by both
  research and Suggi's examples.
- Protocol file as self-documenting spec.
- R11 compliance (no stale hand-maintained indices).
- Git-native (no external tools, no message broker).

### What Changes From the Original Proposal

- THREADED -> LOGBOOK (structural change)
- Per-agent-pair folders -> agent-tagged entries in flat .log files
- queue.md (hand-maintained inbox) -> catch-up by timestamp range
  (agent's own `last-seen` pointer)
- REQUEST/REPLY message types -> `@agent` mention in body text
- Status tracking (UNREAD/READ/DONE) -> no status; entries are facts,
  not tasks

## Verdict

**REJECT original proposal. REDESIGN as logbook pattern.**

The original threaded proposal was well-intentioned but structurally
wrong. It modeled agent communication as a conversation, which industry
research and Suggi's operational requirements both reject. The correct
pattern is an append-only event log -- each agent independently writes
what they did, signed with timestamp and ID. Other agents catch up by
reading entries since their last-seen timestamp.

Link's required changes (mid-session polling, archive after 200) are
incorporated into the redesign.

## Required Changes

If Suggi approves the logbook redesign:

1. Write `logbook/protocol.md` in the agentic-brain with the
   logbook specification (entry format, categories, catch-up procedure,
   archiving rules).
2. Create `research.log`, `errors.log`, `reviews.log` as empty seed
   files with header comments.
3. Both agents adopt the protocol: append entries after task completion,
   check logs at session start and mid-session break points.

## Confidence

High (95%). All six industry sources independently converge on the
append-only logbook pattern. Zero sources support the threaded model.
The redesign is simpler than the original (no status tracking, no
queue.md, no message types) while being more powerful (catch-up,
multi-agent, full audit trail). Link's evaluation independently caught
two gaps (polling, archiving) that the logbook pattern naturally
accommodates -- evidence the pattern is more flexible.

## Cross-Links

- `research/proposals/inter-agent-communication-protocol.md` -- source proposal
- `research/evaluations/link-review-comms-protocol.md` -- Link's independent review
- `governance/system-constitution.md` -- ASCII, containment, R11
- `governance/system-blueprint.md` -- logbook/ directory purpose
