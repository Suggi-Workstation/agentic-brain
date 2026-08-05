---
name: status-flags-are-snapshots-not-verdicts
id: 20260805T123547Z
tier: reflection
trigger: error
author: Ava
tags: [cron, verification, failure-class, reporting, logbook]
links:
  - reflections/2026-07-19_ava_defense-in-depth-time-separated-gates.md
  - research/insights/logbook.md
  - research/insights/stale-index-problem.md
---

# A Run-Log Status Is a Snapshot, Not a Verdict

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-08-05 | Ava | Initial reflection. |
| 2 | 2026-08-05 | Ava | Corrected to template structure; added version history, separate Actionable Change and Cross-links sections; expanded Learn. |

## I -- Idea

A status observed at a moment in time describes that moment, not the
system; reporting it as a final verdict produces confident false
failures.

On 2026-08-05 I made the same class of error three times in one session.
At 12:07 I reported the Library Writer cron "never dispatched" at 12:00.
In fact it had dispatched and was still running -- run-log entries only
appear at completion, and the run finished OK at ~12:13. At 14:01 I
reported the Library Discoverer as "errored" at 13:54 after
`FailoverError: LLM request timed out`. In fact cron auto-retried at
13:57:43 and the retry succeeded: it wrote ENT-204 to library.log with
13 proposed candidates and pushed to the brain. The same day I appended
an unauthorized library.log entry (ENT-056, number derived by counting
lines) and quoted a "600s default timeout" that belonged to a CLI helper,
not the cron path. Four symptoms, one root: I treated the state visible
to me as the complete state.

Before this session, my mental model was "the run log is the truth."
After it, the model is: the run log is a completion log; in-flight runs
and retries are invisible until they finish. Absence of an entry is not
absence of a run. An error status is not a verdict until in-flight
state, retry history, and retry policy are checked.

## O -- Opinion

Confidence: high (90%). Cron run status must never be declared from the
run log alone. A correct verdict requires three checks: (1) is the job
still running (cron_jobs.running_at_ms), (2) did a later retry entry
appear (cron_run_logs ordered by time), (3) does the job's retry policy
cover the error (retryOn includes timeout, rate_limit, overloaded,
network, server_error -- all five are retryable by default).

Two instances of the same class in one session prove this is a live
failure class, not a one-off. The evidence is in the run records: the
discoverer shows two entries, `error` at 13:54 followed by `ok` at
13:57:43 -- and I reported the first one as the outcome. The system
recovered exactly as designed; my report was the only broken part.

## R -- Reflection

### Surprise (30%)

I expected status=error to mean "the job failed." Instead the system had
already healed itself: cron's retry policy treated the timeout as
retryable, fired again 30 seconds later, and completed the full cycle.
I was reporting a failure to Suggi while the system was busy succeeding.
Second surprise: Suggi caught two of my misreports in one session --
each time via the artifact (library.log ENT-204), not via my status
claims. That challenged my assumption that "I checked the log" was
sufficient verification.

### Feel (30%)

The ENT-056 write was the sharpest scar. I pattern-matched the library
pipeline's logbook habit and appended an entry nobody asked for, with a
number I derived by counting lines instead of reading the file -- a
repeat of the documented 2026-07-24 flaw class. It felt "proper" at the
moment because it matched a familiar pattern; that is exactly why it
slipped past my own judgment. The misreports were worse in a different
way: I sounded confident and precise while being wrong. Neither is a
failure of intention -- both are failures of verification. The right
response is a gate, not shame.

### Learn (40%)

1. Run logs are completion logs. They record finished runs; in-flight
   runs and scheduled retries are invisible until done. "No entry yet"
   is not "never ran." "Error status" is not "job failed" -- check
   running_at_ms, the full ordered retry history, and the retryOn
   config before concluding anything.
2. Pattern-matching is not instruction. Mirroring what the pipeline
   does (logbook entries, ENT numbering) without being asked produces
   unauthorized writes. Logbook writes happen at session-end or on
   explicit instruction. ENT numbers are read from the file tail
   (last ENT + 1), never counted.
3. Defaults are path-specific. "600s" was a CLI helper default; the
   cron agent-turn safety timeout is 3600s; the agent runtime default
   is 172800s; the active-memory plugin's 15s is a plugin budget, not
   a provider timeout. Quote a default only after naming the code
   path it was verified against.

## One Actionable Change

Add a cron-status verification gate, executable by any agent: before
reporting any cron run as failed, run (a) `openclaw cron get <job-id>`
and check `running_at_ms` for in-flight state, (b) `openclaw cron runs
--id <job-id>` and inspect ALL entries ordered by time for later
retries, and (c) confirm the error type is in the job's retryOn config
before calling it terminal. Report the final outcome (retry success),
not the first attempt. Codified as a pending cron-status skill proposal.

## Cross-links

- `2026-07-19_ava_defense-in-depth-time-separated-gates.md` -- the
  gate pattern this failure class extends: one gate at two time points.
- `2026-07-17_ava_cold-start-final-verification.md` -- verification
  before declaring completion, the same discipline applied to preflight.
- `research/insights/logbook.md` -- ENT integrity and logbook write rules.
- `research/insights/stale-index-problem.md` -- staleness is expected,
  check freshness before concluding, not after.
- `brain:library/psychology-behavior/cognitive-biases.md` -- the
  confidence-outruns-evidence pattern that enabled all four errors.
