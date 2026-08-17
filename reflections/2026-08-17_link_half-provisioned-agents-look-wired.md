---
name: half-provisioned-agents-look-wired
id: 20260817T123550Z
tier: reflection
trigger: surprise
author: Link
tags: [mnemosyne, provisioning, fleet, verification, cron]
links:
  - research/insights/mnemosyne-system.md
  - research/insights/two-tier-fleet-memory-single-vector-space.md
  - reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md
---

# Half-Provisioned Agents Look Exactly Like Wired Ones

## I -- Idea

Provisioning completeness is invisible from the outside: an agent can
carry every credential, every environment variable, and every config
key that a fully wired agent has, while being completely disconnected
from the fleet memory system. The only reliable signal that an agent
is wired is a live probe on each link of the chain, not the presence
of configuration.

The trigger was wiring Neo into the fleet shared-Mnemosyne system on
2026-08-17. Neo was born the day before, and at birth his profile was
seeded with the four sync environment variables
(MNEMOSYNE_SYNC_REMOTE, MNEMOSYNE_SYNC_ENCRYPT, MNEMOSYNE_SYNC_TOKEN,
MNEMOSYNE_SYNC_KEY) plus the embedding model and dimension. Value-for
-value, those variables matched Morpheus's exactly (verified by
hashing each value). From any configuration-diff perspective, Neo
looked fully wired. He was not. He had no shared database file, no
sync-init state, no sync script, no cron job, no gateway process to
tick the job, and no shared_surface_path config key pointing his
memory adapter at the right file. Had anyone asked "is Neo in the
shared memory loop?" and answered by reading his .env, the answer
would have been a confident and completely wrong yes.

The session then proved the positive case. After running the full
recipe (sync-init, adapter path, watchdog script, gateway install,
cron registration), Neo's shared DB materialized all 18 fleet facts
and his cron job fired autonomously within one 5-minute window. The
verification battery -- row count in his local shared DB, device id
in sync_meta, manual script run with rc=0, ticker heartbeat
freshness, jobs.json last_status -- is what separated "configured"
from "wired". Configuration is a claim; a live probe is evidence.

The trigger for the whole session was Suggi's redundancy question
about the relay folder versus Morpheus's shared DB. Answering it
well required reading the entire loop: the relay's role as a blind
conduit (31 ciphertext events, zero materialized rows), the
per-agent local working copies, the cron ticker ownership rules,
and the paths the write tools actually use. The system that
emerged from that read-only audit is now documented in
`research/insights/mnemosyne-system.md`.

A second, quieter version of the same failure class appeared in the
audit that preceded the wiring: stale husks. The pre-fix-era phantom
DB at ~/.mnemosyne, the install-era default-profile DB, and the
relay's own main-file mtime all LOOKED alive or dead in ways that
misled. The relay main file said Aug 10 and was actually live (WAL
mode writes to the -wal sidecar); the phantom DBs said nothing at
all and were dead weight. In every case, the file's visible metadata
was the wrong lens -- only querying the live store answered the
question.

## O -- Opinion

Confidence: high (90%). The half-provisioned birth state is not a
hypothetical; it was observed directly on a production agent
yesterday and repaired today with a recipe that produced verifiable
convergence.

My position: "wired" must be defined operationally as "every link of
the memory loop answers a live probe", and birth procedures must end
with that probe battery, not with a config summary. Provisioning is
a state transition with observable consequences, and observable
consequences deserve observable confirmation. A fleet of
autonomous agents cannot afford provisioning states that differ only
by whether someone happened to run a test. The Neo case shows why:
everything downstream of the missing pieces -- shared recall,
cross-agent fact distribution, tombstone propagation -- fails
silently, and the failure mode is indistinguishable from "there is
simply nothing new in shared memory". An agent that cannot see fleet
facts does not know it cannot see them. That is the worst kind of
failure: invisible to the one who suffers it.

I also take a position on the tooling divergence I hit while
registering the cron job: the Hermes cronjob TOOL accepts an empty
prompt for no_agent jobs, while the hermes cron create CLI requires a
non-empty POSITIONAL prompt and rejects both the empty string and a
--prompt flag that the help text does not document. Same product,
two different contracts for the same operation. This class of
surface divergence is a trap that will bite every agent that
automates cron registration. The fix is not documentation in prose;
it is capturing the working invocation in the provisioning skill so
nobody re-derives it (which is what happened: three failed attempts
before the working form).

On the documentation front, I took an explicit position while
writing the system insight: the brain already held
`two-tier-fleet-memory-single-vector-space` (the WHY: two tiers, one
vector space, ticker ownership). Rather than re-derive it, the new
`mnemosyne-system.md` documents the WHAT/HOW -- paths, flows,
provisioning recipe, failure catalog -- and cross-links the older
insight as its rationale (R8: reference, never duplicate). A
reference document is only as good as its refusal to repeat what
another artifact already owns.

Finally, on the deletion work: I stand behind deleting the husks,
but only after read-only verification. Each deleted file was queried
directly (0 rows, 0 events, no process referencing the default home)
before removal. "Dont delete anything or break anything" was
respected until the explicit go-ahead, and the deletions themselves
were the smallest possible set.

## R -- Reflection

### Surprise (30%)

I expected "environment variables present at birth" to mean "wired".
It meant nothing of the sort -- Neo's .env was the ONLY completed
link, and six other links were absent. The surprise is not that
provisioning is multi-step; it is that the steps are not visible in
any single place. I also expected file mtimes to be a usable
staleness signal. The relay taught me otherwise: in WAL mode the
main file's mtime is a checkpoint artifact, and judging a live
system by it nearly produced a false "stale" verdict on a healthy
relay. A third, smaller surprise: write_file did not expand
$LOCALAPPDATA in the target path on this Windows host, silently
creating a literal "$LOCALAPPDATA" folder inside the workspace --
the kind of stray-file contract violation I am normally the one
catching in others.

### Feel (30%)

Mild embarrassment at the stray-folder slip; it was caught and
repaired within two tool calls, but it violated the workspace
contract and it should not have happened at all. The two failed
cron-create attempts were a plain quoting-discipline failure over
nested shells -- the skill literally warns about it and I still
walked into it once before switching to the script-file pattern.
That is the cost of doing it inline instead of reading my own
scar tissue. On the credit side: the device-id mapping (querying
each agent's sync_meta rather than guessing), the WAL diagnosis,
and the link-by-link verification of Neo's first autonomous cron
run were exactly the kind of evidence-based work this fleet runs
on, and the insight document that came out of it is the reference
I wish had existed when I started the audit.

### Learn (40%)

1. Verify links, not configuration. For any "is X wired / alive /
   stale" question, name every link of the loop and probe each one
   with a live query. Config presence is a claim; a probe is
   evidence.
2. Never trust a SQLite file's mtime. WAL-mode stores keep live
   state in the -wal sidecar; the main file mtime is a checkpoint
   artifact. Check the -wal mtime or query the store.
3. Birth procedures must end with the probe battery, not a config
   summary. The fleet-agent-birth and shared-sync procedures both
   need the explicit "verification probe" closing step.
4. Script-file-over-inline-quoting is not a preference; it is the
   only pattern that survives nested su/ssh quoting. (This session
   re-proved it.)
5. Convergence is measurable, and measuring it is cheap. The
   link-by-link probes cost one SSH call and a handful of COUNT
   queries; they converted "Neo is probably wired" into "18 rows
   materialized, cron fired, fleet converged at 18/18/18 working
   rows and 31 relay events". Every provisioning claim should end
   in numbers like these, or it is not a claim.

## One Actionable Change

Add a "provisioning verification probe" closing step to the
fleet-agent-birth and mnemosyne-shared-sync skill procedures: after
wiring any agent, run the 5-probe battery (local shared DB
working_memory count > 0, sync_meta device_id present, manual sync
script run with rc=0 and silent output, cron ticker_heartbeat fresh,
jobs.json last_status = ok) and only then declare the agent wired.
No config summary may substitute for the probes.

## Cross-links

- `research/insights/mnemosyne-system.md` -- the system anatomy this
  session produced; the probe battery lives in its Implications.
- `research/insights/two-tier-fleet-memory-single-vector-space.md` --
  the earlier realization this session extends (why + how).
- `reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md` --
  the build-process reflection that first named the operational
  failure class.
