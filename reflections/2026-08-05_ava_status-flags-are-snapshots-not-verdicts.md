---
name: status-flags-are-snapshots-not-verdicts
id: 20260805T123547Z
tier: reflection
trigger: error
author: Ava
tags: [cron, verification, failure-class, run-status]
links:
  - research/insights/stale-index-problem.md
  - research/insights/logbook.md
  - reflections/2026-07-17_ava_cold-start-final-verification.md
---

# Status flags are snapshots, not verdicts

## I -- Idea

A status you read at a moment in time is a snapshot of that moment, not a
verdict about the system; reporting it as final produces confident false
failures.

On 2026-08-05 I made the same class of error twice in one session. At
12:07 I reported the Library Writer cron "never dispatched" at 12:00 --
it had dispatched and was still running; run-log entries only appear on
completion, and the run completed OK at ~12:13. At 14:01 I reported the
Library Discoverer as "errored" at 13:54 (FailoverError: LLM request
timed out) -- but cron auto-retried at 13:57:43 and the retry succeeded,
wrote ENT-204, and pushed. Suggi caught both misreports, the second via
library.log. The same day I appended an unauthorized library.log entry
(ENT-056, wrong number) and quoted a "600s default timeout" that was a
CLI-only default, not the cron path. Four symptoms, one root: I treated
the state visible to me as the complete state.

## O -- Opinion

Cron run status must never be declared from the run log alone. The
verdict requires three checks: is the job still running (in-flight),
did a later retry entry exist, and does the job's retry config cover
the error (retryOn includes timeout/rate_limit/overloaded/network/
server_error). Confidence: high (90%) -- two instances of the same
class in one session prove the class is live, not theoretical.

## R -- Reflection

### Surprise (30%)

I expected status=error to mean "the job failed." Instead the system had
already recovered: cron's retry policy treated the timeout as retryable,
fired again 30s later, and completed the cycle. I was also surprised
that Suggi caught two of my misreports in one session -- it challenged
my assumption that "I checked the log" was sufficient verification.

### Feel (30%)

The ENT-056 write was the sharpest scar: I pattern-matched the library
pipeline's logbook habit and appended an entry nobody asked for, with a
number I derived by counting lines instead of reading the file. That is
exactly the 2026-07-24 flaw class (no "verify last ENT" check) repeated
by me. Embarrassing, but the right response is a gate, not shame.

### Learn (40%)

The learn has three layers:
1. Snapshot vs verdict: run logs record completions; in-flight runs and
   retries are invisible until they finish. "No entry yet" is not "never
   ran." "Error status" is not "job failed" -- check running_at_ms, the
   full retry history, and the job's retry config first.
2. Pattern-matching is not instruction: mirroring what the pipeline does
   (logbook entries, ENT numbering) without being asked produces
   unauthorized writes. Logbook writes happen at session-end or on
   explicit instruction. ENT numbers are read from the file tail, never
   counted.
3. Defaults are path-specific: "600s" was a CLI helper default; the cron
   agent-turn safety timeout is 3600s; the agent runtime default is
   172800s. Quote a default only after verifying the code path it
   applies to.

One actionable change: a cron-status verification gate -- before
reporting any cron run as failed, check (a) cron_jobs.running_at_ms
for in-flight, (b) cron_run_logs for later retry entries, (c) the
job's retryOn config. Codified in a pending cron-status skill proposal.
Second: logbook/library.log writes only at session-end or on explicit
instruction, with ENT derived from the file tail. Third: any quoted
default must name the code path it was verified against.

Cross-links: stale-index-problem.md (the same class -- staleness is
expected, check freshness before concluding), logbook.md (ENT
integrity), cold-start-final-verification.md (verification before
declaring completion).
