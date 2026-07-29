---
name: safe-push-retry-library-skills
id: 20260729T123859Z
tier: proposal
author: Ava
tags: [library-pipeline, race-condition, git, push-retry, skills, governance]
links:
  - governance/skills/library-writer.md
  - governance/skills/library-discoverer.md
  - reflections/2026-07-29_ava_free-financial-data-segmented-by-design.md
---

# Safe Push Retry for Library Pipeline Skills -- Prevent Lost Writes From Clone-Push Race Conditions

## Problem

The library Writer and Discoverer run on independent 15-minute and
2-hour cron schedules. Both clone the agentic-brain repo to `/tmp/`,
modify files (candidate queue, topic files, logbook), and push back
to `origin main`. When their push windows overlap, a race condition
occurs:

1. Writer clones brain at T1.
2. Discoverer clones brain at T2 (Writer has not pushed yet).
3. Writer pushes at T3. Succeeds.
4. Discoverer pushes at T4. Push is rejected (non-fast-forward) because
   Discoverer's local clone is behind Writer's pushed commit.
5. Current instruction: "If the push fails, pull first, resolve, then
   push." This is a manual one-liner with no retry, no backoff, and no
   error logging if it fails again.

This caused ENT-129's Expected Value Thinking candidate to remain in
the queue with status `written` instead of being deleted -- the
Discoverer's clone (which still had the stale queue) was pushed AFTER
the Writer's correct version, re-introducing the stale entry.

The same race can silently drop topic files, lose logbook entries, or
revert candidate queue edits -- all without error logging because the
second agent's push either succeeds (overwriting) or the agent gives
up after one manual pull attempt.

## Proposed Solution

Replace the single-attempt `git push` in both skills with a pull-rebase-push
retry loop. This is the standard "optimistic concurrency" pattern used by
GitHub's own multi-agent pipeline (`gh-aw` issue #19476).

### Changes to `governance/skills/library-writer.md` (Step 11)

**Replace:**
```bash
cd /tmp/brain-writer
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: write <topic-slug> to <domain>"
git push origin main
```

"If the push fails, pull first, resolve, then push."

**With:**
```bash
cd /tmp/brain-writer
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: write <topic-slug> to <domain>"

# Safe push with retry: if another agent pushed between our pull and now,
# pull their changes, rebase ours on top, and retry.
PUSHED=0
for attempt in 1 2 3; do
  if git push origin main; then
    PUSHED=1
    break
  fi
  echo "[safe-push] Attempt $attempt/3 failed. Pulling latest and retrying in ${attempt}s..."
  git pull --rebase origin main
  sleep $attempt
done

if [ "$PUSHED" -eq 0 ]; then
  echo "[safe-push] FAILED after 3 attempts. Logging to errors.log."
  # The agent MUST append to errors.log before exiting
  exit 1
fi
```

### Changes to `governance/skills/library-discoverer.md` (Step 12)

Identical replacement -- same retry loop, substituting `brain-discover`
for `brain-writer` and the commit message template.

### New checklist items

**In Writer's `File Output Sub-Checklist` (after line item for logbook):**
```
- [ ] Safe push executed: push retried up to 3 times with pull --rebase on rejection. Final push succeeded or error logged to errors.log (PASS / HALT)
```

**In Discoverer's `File Output` verification (after last line):**
```
- [ ] Safe push executed: push retried up to 3 times with pull --rebase on rejection. Final push succeeded or error logged to errors.log (PASS / HALT)
```

**In Writer's `Final Self-Check` (before "Discarded clone"):**
```
- [ ] Safe push verified: retry loop completed, final push succeeded (PASS / HALT)
```

## Impact

**Positive:** Eliminates the race condition class where concurrent
clone-push cycles silently lose data. The Writer and Discoverer can
run at any schedule offset without losing each other's changes. No
new infrastructure. No lock files. No architecture changes. The
existing schedule offset becomes a performance optimization (fewer
retries) rather than a fragile correctness guarantee.

**Risk:** Low. The retry loop uses `git pull --rebase`, which is safe
for these two skills because:
- Each agent modifies disjoint files (Writer: topic files + queue
  deletions. Discoverer: queue appends + logbook). They never edit
  the same line of the same file simultaneously.
- If a genuine conflict occurs (same file line edited by both), the
  rebase will fail. This is caught by the retry loop exhausting and
  logging to errors.log. This is strictly better than the current
  silent failure.
- The exponential backoff (1s, 2s) is tuned for the typical 4-12
  minute Writer cycle window.

**Cost:** Zero. No new dependencies. ~10 extra lines per skill. The
sleep overhead (1-2 seconds) only applies when a push actually fails.

## Open Questions

1. Should the retry count (3) and backoff (1s, 2s) be configurable, or
   are these reasonable defaults for the 15-minute Writer cycle?
2. Should we apply the same retry pattern to the logbook-only push step
   in the `session-end` skill and `preflight` skill, or keep those
   manual for now?

## Approval Gate

Suggi approves the changes to `governance/skills/library-writer.md` and
`governance/skills/library-discoverer.md`. Upon approval, Ava implements
the edits to both files in one commit.
