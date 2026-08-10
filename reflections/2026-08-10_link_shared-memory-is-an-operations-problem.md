---
name: shared-memory-is-an-operations-problem
id: 20260810T112711Z
tier: reflection
trigger: milestone
author: Link
tags: [mnemosyne, fleet, shared-memory, cron, operations, infrastructure, learning]
links:
  - research/insights/two-tier-fleet-memory-single-vector-space.md
  - research/reports/link-hermes-memory-system.md
---

# Shared Memory Is an Operations Problem, Not a Storage Problem

## I -- Idea

Building a fleet-wide shared memory system for three agents was 20%
storage design and 80% operations, and the operations failures were
the only ones that cost real debugging time.

The task was to give Link (PC), Linkie (laptop), and Morpheus (VPS)
the same two-tier Mnemosyne architecture: a private personal database
per agent, plus a shared surface synchronized through a blind relay on
the VPS, all running on a 5-minute cadence with no tokens and no
popups. The storage half -- two SQLite databases per agent, a relay
that stores only encrypted events, a stdlib-only file-sync protocol
with HMAC auth and client-side encryption -- was designed, built, and
verified working on the first attempt. The live end-to-end test (a fact
written on Linkie, pushed to the relay, pulled onto Link's PC) passed
immediately.

Everything that broke afterward was operational. The embedding model
upgrade exposed a sequencing rule: reindexing while an old-model
process still runs writes stale-dimension rows into a rebuilt database,
and the sync then emits backfill warnings on every cycle. The cron
automation exposed the real trap: a Hermes cron job present in
jobs.json with state=scheduled is NOT running unless a process owns
that profile's HERMES_HOME. The desktop app's backend ticks cron only
when it serves the profile -- which it decides from the sticky
active_profile file, not from the --profile flag on the app's launch
line. Linkie's job sat dormant for an hour while the laptop app served
the default home; Morpheus's job could never fire because a headless
serve process does not tick cron at all (only HERMES_DESKTOP=1 backends
and gateways do). Each of these was found by reading source code after
the symptom, not by the initial mental model.

## O -- Opinion

Confidence: high (85%). The architecture we built is sound, and the
operational layer around it -- who ticks the scheduler, which home the
app serves, what order a model switch happens in -- is the part that
determines whether the system actually works.

I take this position because the evidence is asymmetric. The storage
layer never failed once: the sync protocol, the relay, the encryption,
the two-tier split, the write-time auto-embedding all worked as
designed and were verified with live tests. Every incident in the
session trace back to operations: a Windows task that popped up
(because a stopgap was chosen over diagnosis), a cron job that looked
scheduled but never fired (because profile resolution was wrong), a
reindex that left phantom rows (because sequencing was wrong), a sync
script that reported failure on success (because my own error-check
matched the literal word "conflict" inside the CLI's normal
"Conflicts: 0" output). The last one is the sharpest example: the
system was fine; my verification logic was wrong.

This matters because it inverts the natural instinct. When a fleet
system misbehaves, the temptation is to inspect the storage, the
schema, the sync. The productive move is to ask who owns the process,
which home it resolved, and whether the scheduler has a ticker. In
this session, every answer to those three questions pointed at the
real fault within minutes; every inspection of tables and schemas
pointed at nothing. Generalized: distributed systems fail at the
seams -- process ownership, resolution order, sequencing -- not at
the core data structures. I expect this to hold for any multi-agent
fleet, not just ours, which is exactly why the operational layer of
this architecture must be documented as carefully as the storage
layer itself.

## R -- Reflection

### Surprise (30%)

I expected the storage design to be the hard part and the automation to
be routine. It was exactly reversed. The relay, the protocol, the
encryption, the two-tier split -- all first-try. The cron, the profile
resolution, the model-switch sequencing -- every one of them produced a
failure class I had not anticipated. The deepest surprise was that the
desktop app's --profile linkie launch flag does not reach the backend
spawn; the backend reads a sticky active_profile file, and an empty
file silently means "serve the default home." A job that "looks
scheduled" while nothing owns its home is the single most misleading
state in the whole system. The CLI even warns about it at creation time
("Gateway is not running -- jobs won't fire automatically"), and I still
needed to read the source to understand why the ticker was dead.

### Feel (30%)

There are two honest reads. The good one: the fleet now runs the exact
same pattern on all three machines, with evidence for every claim --
ticker heartbeats, job statuses, embedding rows at 1024 dims, a deleted
Windows task, a cleaned OS crontab. That part earns its keep.

The uncomfortable one: I created the Windows Task Scheduler entry for
Linkie as a "working" stopgap when the Hermes cron did not tick, and I
justified it long enough for Suggi to have to ask why the pattern had
changed. The sibling-parity principle -- Linkie should get the same
procedure as Link, PERIOD -- was correct, and my workaround was the
wrong answer to a diagnosable problem. I also wrote a sync script whose
own error-detection line flagged the CLI's normal success output as a
failure, and I shipped that same bug to all three machines before
catching it in a manual run. Both were cases of acting before fully
understanding the running system. Naming them is the point; they are
the scar tissue this reflection exists to preserve.

### Learn (40%)

1. When a scheduled job does not fire, do not add an external scheduler
   (Windows task, OS cron). Diagnose process ownership first: which
   process should own this HERMES_HOME, is it running, is the ticker
   heartbeat fresh? The fix is Hermes-native (active_profile file,
   gateway install), never a parallel scheduler.
2. Profile resolution has one authoritative file on Windows desktops:
   the sticky active_profile at the Hermes home root. The app's launch
   flag is cosmetic for the backend. Check the file before touching
   anything else.
3. Model switches in a shared vector space are fleet-wide, sequenced
   events: stop old-model writers, switch env, reindex, restart. A
   single stale-dimension row is a corruption signal, not a nuance.
4. Verification code can be wrong in ways that look like the system is
   wrong. When a watchdog reports failure, check the watchdog first:
   string matching against CLI output that contains "Conflicts: 0" on
   success is a false positive by construction.

## One Actionable Change

Add a "scheduler ownership" preflight check to the session-end and
preflight skills: for every profile with a Hermes cron job, verify a
live ticker exists (ticker_heartbeat mtime within 2 minutes, or an
active gateway unit on headless servers) and that active_profile names
the intended profile -- PASS only when both hold. This converts the
two costliest failure classes of this session into automatic gates.

## Cross-Links

- `research/insights/two-tier-fleet-memory-single-vector-space.md` --
  the co-produced insight (architecture + one-vector-space rule).
- `research/reports/link-hermes-memory-system.md` -- the prior 5-layer
  personal memory report this fleet build extends.
- `governance/skills/query-brain-vps.md` -- the VPS transport pattern
  used for this artifact.
