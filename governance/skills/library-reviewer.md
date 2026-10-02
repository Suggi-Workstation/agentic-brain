---
name: library-reviewer
description: "Use when asked to review library topics. Verify existing topics, correct every identified mismatch, and record completed reviews."
user-invocable: false
disable-model-invocation: false
---

# Library Reviewer

## What This Skill Does

Guides the review and refresh process of the library pipeline. Selects
a domain from the master index, then one topic from its domain index.
Verifies accuracy against current web sources, corrects the topic,
and adds or updates the `reviewed:` date in frontmatter.
Combines the old auditor and health-monitor roles into one pass: the
reviewer both checks AND fixes, because the agent that discovers what
is stale is the best positioned to fix it.

Does NOT propose new topics (that is the discoverer) or write new
topics from scratch (that is the writer). The reviewer refreshes
existing content -- it reads what exists, verifies it, and updates
what is stale.

## When to Invoke

Invoke when asked to review existing library topics.

Skip for:
- No eligible topics (all have been reviewed within the last six months)
- Topics in quarantine directory

## Path Convention -- Dual Platform

The brain working copy lives at `/srv/brain/agentic-brain` on the
fleet VPS. The watcher keeps it in two-way sync with GitHub and
pushes commits. There is NO clone step and NO push step in this
skill.

- **VPS agents** (running on the server, no SSH): every path below is
  a literal filesystem path under `/srv/brain/agentic-brain/`. Prepare
  drafts in OS temporary storage; publish through `scripts/library-publish.py`
  as yourself (agents group, no su).
- **VPS-connected agents** (remote machines, e.g. PC or laptop
  agents): read and write through the key door, commit via su:

```bash
# read a brain file
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat /srv/brain/agentic-brain/<path>'

# transfer a prepared draft to VPS temporary storage
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /tmp/<cycle>/<draft>'

# publish the prepared request as the clone owner
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'su - hermes -c "python3 /srv/brain/agentic-brain/scripts/library-publish.py publish /tmp/<cycle>/request.json"'
```

Quoting rule: the remote command sits in double quotes; inner quotes
sit in single quotes. A broken quote fails the whole command.

## Review Eligibility

Use one rule for every domain: a topic is eligible if it has no
`reviewed:` field, or six calendar months have elapsed since that date.
Use the current UTC date; include dates on or before the six-month cutoff.
For a shorter cutoff month, use that month's final day. Do not substitute
a fixed day count. Invalid or future review dates are ERROR outcomes, not
permission to invent a replacement date.

## Final Self-Check -- HARD GATE

Confirm each item at its corresponding step; commit and push checks follow
publication. One checklist -- no
sub-checklists, no section summaries. Each item maps to a procedure
step or a library guide rule. HALT on any failure; fix before
committing.

- [ ] Procedure completed: select one topic in step 2, read template, review and correct in step 4, re-read template and verify checklist, stamp reviewed date, log, publish (PASS / HALT)
- [ ] Template read in full before reviewing and re-read before final checklist verification (PASS / HALT)
- [ ] Topic selected per step 2; its frontmatter confirms eligibility (PASS / HALT)
- [ ] Topic and anchor read in full; independent research done; errors it revealed corrected; Sources and citations consistent (PASS / HALT)
- [ ] Whole final topic passes the Library Topic Checklist, including measured section word counts; creation-only actions excluded as specified below (PASS / HALT)
- [ ] `reviewed: <YYYY-MM-DD>` added or updated in frontmatter of each reviewed topic (PASS / HALT)
- [ ] Changes limited to accuracy, substantive completeness, and template compliance; no padding or cosmetic rewrites (PASS / HALT)
- [ ] Logbook entry written to logbook/library.log (PASS / HALT)
- [ ] Logbook entry format: each data field on its own line, matching the step 7 example (PASS / HALT)
- [ ] Logbook entry properly separated: exactly one blank line between this entry and the previous (PASS / HALT)
- [ ] Shared publication used the Library Guide's Publication procedure and returned PASS; no direct topic/log writes or staging outside the helper (PASS / HALT)
- [ ] No generated index files edited, regenerated, or staged by the reviewer (PASS / HALT)
- [ ] Every outcome, including ERROR, recorded in library.log when safe publication was available; otherwise failure surfaced to the caller (PASS / HALT)
- [ ] Exact committed work verified on the remote mirror; a fresh unrelated watcher log line alone is insufficient (PASS / HALT)

## Procedure

### 1. Locate the brain working copy

VPS agents: `cd /srv/brain/agentic-brain`. The watcher keeps the
clone synchronized with GitHub. Read the Publication section of
`agentic-brain:library/guide-library.md`. Capture selected topics and their
research inputs with the helper's snapshot command and read captured files
in full. Do not modify the live clone while reviewing or preparing drafts.

VPS-connected agents: no local clone. Every read and write below goes
through the Path Convention commands above.

### 2. Select one topic

1. Read `library/index-library.md`. For each domain, never-reviewed =
   Topics - Reviewed (the number before the parentheses).
2. If any domain has never-reviewed topics, take the domain with the
   highest count (tie: domain name). In its `index-<domain>.md`, select
   the first topic from the top tagged `[reviewed: never]`.
3. Otherwise, select the eligible topic with the oldest `reviewed:` date
   across all domains (tie: topic path).
4. If no topic is eligible, publish a log-only no-op and exit.
5. Confirm the selected topic's frontmatter matches the index; if it does
   not, select again from the topics' frontmatter.
6. Review only this topic. If the review cannot be completed, record
   ERROR and exit.

### 3. Read the library template

Read `governance/template-library.md` in full before reviewing. Follow its
format specification and Library Topic Checklist throughout the review.

### 4. Review the topic

1. Read the captured topic and its domain anchor in full.
2. Research the topic yourself as the template describes, using current
   high-authority sources, including evidence published since the topic
   was written. Check the topic's central claims (title claim, opening
   paragraph, key figures and findings in Evidence) against your research.
3. In a temporary draft, correct what your research shows is wrong or
   outdated, and add important missing concepts, evidence or applications
   within the topic's scope. Do not remove a claim only because your
   research did not find it.
4. Keep Sources consistent: add verified sources for new material with
   authority ratings, remove sources no longer cited, and update affected
   citations. Keep the section structure unless new content needs a new
   section. Keep the original ID and author. ASCII only.
5. If you find a problem you cannot resolve, record ERROR and leave the
   topic unchanged.

### 5. Re-read the template and verify its checklist

Re-read `governance/template-library.md` in full. Verify the entire final
draft, including unchanged sections, against its Library Topic Checklist.
Run the section word-count check and verify every content, source, format,
and cross-reference requirement. Keep the original ID and author; do not
repeat creation-only actions (new ID, initial omission of `reviewed`, or
candidate selection/scoring). Fix failures and recheck the final draft.
Recheck every occurrence of corrected facts and their citations against
the sources.
If any applicable item remains unconfirmed, record ERROR and do not stamp
or publish that topic as reviewed. Do not put the checklist in the topic.

### 6. Stamp the reviewed date

For each completed review, add or update `reviewed:` in the draft's
frontmatter. Use today's UTC date in `YYYY-MM-DD` format. Do not stamp
a topic with unresolved discrepancies. Keep id, name, domain, tier, and
original author unchanged.

```bash
date -u +'%Y-%m-%d'
```

Add the field after the `links:` line in the frontmatter, before the
closing `---`:

```yaml
links: [library/<domain>/<topic>.md, ...]
reviewed: 2026-08-25
---
```

If `reviewed:` already exists (from a prior review), update the date
in place. Do not add a second `reviewed:` line.

### 7. Write logbook entry

Prepare a body for `logbook/library.log`. The helper generates the ENT
number, UTC timestamp, actor, and `library` category under its lock. Do not
append directly or include the header in the request's log body.
The resulting entry follows this format. Each data field is on its own line. Topics MUST
be listed one per line using bullet points (`-`). Do NOT pack
multiple fields onto a single line.

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md
Review cycle: N topics reviewed, M current, K rewritten.
Topics:
- <title> (<domain>): <outcome and findings>
Domain coverage: reviewed across N domains.
```

Use one topic line. Its outcome is `current, no changes` or
`rewritten (corrected <mismatches>, updated <sources/sections>)`.

For unresolved topics or execution failures, prepare a log-only body
beginning `ERROR:` with the topic, failed check, and unresolved evidence.
Do not count unresolved topics as reviewed. If the helper cannot publish
safely, surface its HALT result to the caller; never bypass the lock to
write a failure entry.

### 8. Commit on the VPS clone -- NO push

Follow `agentic-brain:library/guide-library.md#publication`.
Use `kind: review` with only the completed topic in `writes` and `expected`,
its captured topic hash, and the log body. Omit queue operations and hashes
of indexes or other read-only inputs. The helper rechecks topic bytes and six-month
eligibility before saving the reviewed topic and log in one commit.
If a topic changed during research, read and review the current version;
do not apply corrections based on the stale copy.

Use `kind: log` with no writes for no-op or ERROR outcomes. Do not modify
the candidate queue or regenerate/stage index files. The `library-index.yml`
workflow regenerates the Markdown indexes after publication.

No direct append, `git add`, commit, pull, or rebase belongs in this cycle.
The existing `repo-pull.sh` watcher owns synchronization; its Brain log is
`/srv/brain/logs/brain-pull.log`. Verify the specific publication reached
GitHub after releasing the helper's lock.

## Related

- `agentic-brain:governance/template-library.md` -- topic format specification (read before any rewrites)
- `agentic-brain:library/guide-library.md` -- pipeline architecture, weights, anchor format
- `agentic-brain:research/insights/library-system.md` -- full system blueprint, anti-staleness design
- `agentic-brain:governance/skills/library-writer.md` -- writer skill (produces new topics)
- `agentic-brain:governance/skills/library-discoverer.md` -- discoverer skill (proposes candidates)
- `agentic-brain:logbook/protocol.md` -- logbook entry format