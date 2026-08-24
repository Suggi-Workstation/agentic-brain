---
name: limits-are-choices-in-disguise
id: 20260824T195508Z
tier: reflection
trigger: surprise
author: Morpheus
tags: [infrastructure, performance, verification, tooling]
links:
  - research/insights/vps-brainclone-plus-index.md
  - governance/skills/query-brain-vps.md
  - reflections/2026-08-23_morpheus_gates-expose-what-prose-tolerates.md
---

# Limits Are Choices in Disguise -- The Cap That Was a Tool

## I -- Idea
A system's observed performance limit is often not a constraint someone
configured but a choice someone made by picking the tool -- and the two
leave completely different fingerprints on the machine. This session,
Suggi asked me to check whether "we limited the security crons to run
on only 1 CPU core," suspecting a throttle he and Link had set. I went
looking for that limit: no `nice`, no `taskset`, no cgroup, no config
line in either scan script, nothing in `/etc/clamav`. The honest answer
was "denied as stated." But the search surfaced something better: the
box ran TWO ClamAV frontends. Our scripts called `clamscan`, which is
architecturally single-threaded -- it contains no threading code path
at all. Meanwhile `clamd`, the resident daemon with a `MaxThreads`
knob set to 12, sat installed, systemd-enabled, active since August 21,
and almost perfectly idle. The "limit" was real -- one core, exactly
as Suggi remembered -- but it had never been written down anywhere
because it lived inside the tool selection itself.

The stakes were not abstract. Those scans guard a machine that holds
three fleet repositories, every agent profile, and the shared memory
relay -- infrastructure whose compromise would propagate to every
agent at once. A scanner pinned to one core was not an inconvenience;
it was a security posture quietly tuned to miss whatever arrives
during the forty-three minutes it spends walking the disk. Speed here
is not convenience; it shrinks the window an attacker lives in.

The same pattern showed up twice more before the day ended, which is
what elevates this from an anecdote to a method. First: the daily scan
script contained `INFECTED=$(grep -c "FOUND" "$LOG" 2>/dev/null ||
echo 0)` -- defensive-looking code whose failure mode was invisible.
`grep -c` already prints its own zero but exits nonzero when the count
is zero, so the `|| echo 0` fired *on top of* the printed zero and
produced the two-line value `"0\n0"`. Every clean scan since August 10
carried a corrupted counter, and nobody noticed because the corruption
only mattered when the alert branch evaluated it, and the alert text
looked superficially plausible right up until bash rejected it with
"integer expression expected". Second: Neo's investing-hub session had
asked "will PDFs be searchable?", which also looked like a
configuration question. The answer had the same shape again: the
indexer's `.md`-only whitelist at one line of its source is not a
setting anyone can flip; it is a property of the code path,
discoverable only by reading the indexer itself. Switching to the
daemon took minutes; the sweep dropped from 43m40s to 4m28s, a 9.8x
speedup, verified with live thread counts (~830% CPU) and load average
pinned near the agreed 8-of-12 budget.

## O -- Opinion
Confidence: high (90%). When auditing why a system is slow or limited,
the first sweep should look for explicit constraints (config, cgroups,
nice levels) because those are cheap to find -- but if that sweep comes
back empty, the correct conclusion is NOT "there is no limit." The
correct conclusion is "the limit is structural, embodied in which
binary we invoke." These two cases demand opposite remedies: configured
limits are lifted by editing values; structural limits are lifted by
replacing components. Confusing them wastes effort in both directions --
tuning configs that govern nothing, or rewriting code when a knob
existed all along.

I also hold, medium confidence (75%), that this distinction generalizes
beyond performance into capability audits generally. "Can our indexer
read PDFs?" and "can our fleet share one skill?" have the same grammar
as "how many cores does the scanner use?" -- the answer lives in what
was chosen (whitelists, install locations, invocation patterns), not
in what was configured. Evidence for the generalization: three hits in
one session across three different subsystems (security scanning,
indexing, skill distribution). Evidence against: these are all
infrastructure domains where choices fossilize into behavior; the
pattern may not transfer to, say, research-quality problems where
nothing is binary.

There is a governance implication worth stating. Suggi's writing
standard from this same session -- pitfalls must be procedure plus a
one-clause mechanism, zero story -- is the textual twin of this
principle. Bloated documentation is rarely an accident of phrasing; it
is the structural consequence of generators that produce narrative by
default. You do not fix it by editing adjectives (configured-limit
thinking); you fix it by changing what the writer emits (structural
thinking): fixed shapes, enforced at creation and at review. The
measured result on preflight's catalog, roughly a quarter smaller with
zero procedures lost, is the same kind of jump the scan got from
switching binaries.

One caution tempers the opinion: structural limits are usually MORE
expensive to lift than configured ones, which is precisely why they
hide so well. Nobody writes down "we chose the slow tool" because the
choice did not feel like a decision when it was made -- it felt like
the obvious default. So audits should weight recency: the older an
invocation pattern is, the more likely everyone has forgotten that it
is a choice rather than a law. Today's clamscan call dated from
August 7; eleven days was long enough for two humans and one agent to
misremember a tool choice as a configured cap.

## R -- Reflection

### Surprise (30%)
I expected to find a configuration limit and expected to report back
"no throttle found, the scans are just slow." Instead the premise was
half-right in a way neither of us predicted: Suggi's memory of "we set
it to one core" was accurate about *effect* while wrong about
*mechanism* -- nobody ever set anything; the tool simply cannot use
more than one core. The second surprise was the daemon: a parallel
engine with an idle thread pool had been running on this box for days.
We were not missing a capability; we were standing next to it. Third:
the Aug-10 counter bug survived fourteen days of clean-looking
summaries, and the thing that exposed it was a background-process exit
notification -- an artifact of process hygiene, not any verification
gate I own.

### Feel (30%)
Mixed. Genuinely good: the rename of `/opt/brain-tools` to
`/opt/repo-tools` went off with zero downtime because the sequence
(copy, repoint cron and systemd, verify manual runs AND live cron
ticks, then delete the old dir) refused every shortcut, and the E2E
chunk arithmetic (+1/-1 per repo, ending at exact baseline) turned
"trust me" into arithmetic. Uncomfortable: my foreground run of the
daily scan got killed by a tool timeout while its child clamscan
orphaned onward, producing a half-finished run that looked finished
until log forensics showed the missing marker line. That is twice this
month a "successful" state was actually a partial one, and both times
the tell was in a log rather than in any status I reported. Also
uncomfortable: two greedy patches ate neighboring bullets mid-session;
my verify-after-patch habit caught both, but habits that fire twice a
day are begging to become mechanical gates instead.

### Learn (40%)
1. When hunting a limit: check explicit constraints first (cheap),
then treat "none found" as evidence of a STRUCTURAL limit and go read
what binary/code-path is actually being invoked. Configured limits are
edited; structural limits require component replacement.
2. An idle enabled service is inventory, not decoration. Before
building or buying capacity, enumerate what already runs on the box
(`systemctl list-units`, then check what each unit actually does).
The fastest speedup available was installed and sleeping.
3. Defensive shell idioms deserve the same suspicion as clever ones.
`grep -c X file || echo 0` reads as safety and behaves as corruption,
because grep -c emits output on the very condition that trips its exit
code. Test counters by executing the consuming comparison
(`[ "$V" -gt 0 ]`), not by eyeballing the assignment.

## One Actionable Change
Add a step to infrastructure-change procedure (vps-remote-ops /
preflight references): before diagnosing any performance or capability
limit as "missing," run a two-question audit -- (1) `grep -r` the
relevant configs for throttles (nice/taskset/cgroup/MaxThreads-class
knobs); (2) `systemctl list-units --type=service --state=running` and
check whether a component that already provides the capability exists.
Both must come back negative before concluding "build or install
something new." Gate: any proposal to add a new tool to /opt must cite
this audit's output.

## Cross-links
- `research/insights/vps-brainclone-plus-index.md` -- the watcher/index
  architecture whose v5 update this session performed
- `governance/skills/query-brain-vps.md` -- canonical query skill synced
  to runtime truth during the same pass
- `reflections/2026-08-23_morpheus_gates-expose-what-prose-tolerates.md`
  -- prior session-end insight on gates surfacing what prose tolerates;
  the counter bug is a fresh instance (prose tolerated a lie for 14 days)
