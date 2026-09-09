---
name: library-reviewer
description: "Use when asked to review library topics. Verify existing topics, correct every identified mismatch, and record completed reviews."
user-invocable: false
disable-model-invocation: false
---

# Library Reviewer

## What This Skill Does

Guides the review and refresh process of the library pipeline. Scans
per-domain index files for topics overdue for review, re-reads each
topic, verifies accuracy against current web sources, rewrites stale
sections in-place, and stamps the `reviewed:` date in frontmatter.
Combines the old auditor and health-monitor roles into one pass: the
reviewer both checks AND fixes, because the agent that discovers what
is stale is the best positioned to fix it.

Does NOT propose new topics (that is the discoverer) or write new
topics from scratch (that is the writer). The reviewer refreshes
existing content -- it reads what exists, verifies it, and updates
what is stale.

## When to Invoke

Invoke when asked to review existing library topics. Select and attempt
at most 2 topics per cycle, sequentially. Do not replace blocked topics
with additional selections in the same cycle.

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

## Accuracy Requirement

Read the complete topic and verify its claims against current sources.
Correct every identified factual mismatch, outdated claim, broken source
reference, and substantive gap. There is no percentage allowance for leaving
known errors in place.
Preserve correct material and the topic's scope; do not make cosmetic rewrites.
If evidence cannot resolve a discrepancy, record ERROR and do not stamp or
publish that topic as reviewed. Complete the template checklist before stamping.

## Final Self-Check -- HARD GATE

Confirm each item at its corresponding step; commit and push checks follow
publication. One checklist -- no
sub-checklists, no section summaries. Each item maps to a procedure
step or a library guide rule. HALT on any failure; fix before
committing.

- [ ] Procedure completed: read index, select within cycle limit, read template, research each topic, correct errors and gaps, re-read template, verify checklist, stamp reviewed date, log, commit (PASS / HALT)
- [ ] Template read in full before reviewing and re-read before final checklist verification (PASS / HALT)
- [ ] Topics selected have no reviewed date or are at least six calendar months past review; actual frontmatter checked, not only index tags (PASS / HALT)
- [ ] Each topic read in full before web-searching (PASS / HALT)
- [ ] Independent web search conducted; existing sources and new findings checked against the topic's claims (PASS / HALT)
- [ ] Every identified mismatch and substantive gap resolved; incomplete topics logged and excluded from review stamps/publication (PASS / HALT)
- [ ] Stale, superseded, incorrect, duplicate, or unused sources removed or replaced; affected citations reconciled throughout the topic (PASS / HALT)
- [ ] Whole final topic passes the Library Topic Checklist, including measured section word counts; creation-only actions excluded as specified below (PASS / HALT)
- [ ] `reviewed: <YYYY-MM-DD>` added or updated in frontmatter of each reviewed topic (PASS / HALT)
- [ ] Changes limited to accuracy, substantive completeness, and template compliance; no padding or cosmetic rewrites (PASS / HALT)
- [ ] Logbook entry written to logbook/library.log (PASS / HALT)
- [ ] Logbook entry format: each data field on its own line, matching the step 8 example (PASS / HALT)
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

### 2. Read the master index

Read `library/index-library.md`. Note the topic counts per domain.
The master index gives the full domain coverage table.

### 3. Select overdue topics

Read per-domain `index-<domain>.md` files to find topics with
`[reviewed: never]` or `[reviewed: <date>]` at least six calendar months old.
Use the indexes to shortlist, then verify each topic's actual frontmatter
from its captured snapshot. Generated indexes may lag recent publications.

Prioritize:
1. Topics with `[reviewed: never]` (never reviewed -- highest
   priority).
2. Topics with the oldest `reviewed:` dates (most overdue).
3. Spread across domains if possible.

Select within the cycle limit under When to Invoke.

A bash one-liner can help identify overdue topics across all domains:

```bash
cd /srv/brain/agentic-brain
for d in library/*/; do
  domain=$(basename "$d")
  idx="${d}index-${domain}.md"
  [ -f "$idx" ] && grep '\[reviewed: never\]\|\[reviewed: [0-9]' "$idx"
done
```

The index files show a reviewed tag on every topic line. Apply the uniform
eligibility rule and actual source-date check. If none qualify, publish a
log-only no-op outcome and exit.

### 4. Read the library template

Read `governance/template-library.md` in full before reviewing. Follow its
format specification and Library Topic Checklist throughout the review.

### 5. Review each topic

For each selected topic, in order:

**5a. Read the topic file.** Read the captured
`library/<domain>/<topic-slug>.md` in full. Note the key claims,
the Sources section, and the body structure. Read its full domain anchor
before preparing corrections. Preserve the original topic identity/author.

**5b. Research and verify.** Perform independent web searches for the
topic. Read its existing sources and relevant new sources; compare their
actual findings with the topic's claims. Check:
- Core factual claims (numbers, dates, study results, named
  entities).
- Sources -- do they support the attributed claims? Are they current,
  accessible, and correctly identified?
- Any time-sensitive claims (current events, market data, technology
  specifics, regulatory references).

**5c. Identify errors and gaps.** Check every section for factual errors,
unsupported claims, missing concepts, examples, evidence, and applications
within the topic's scope. Compare depth and completeness with the template.
If none are found, still complete step 6. Otherwise correct them in step 5d.
Unresolved evidence, unavailable sources, or a
required change outside the topic's scope prevents a completed review;
record ERROR and leave that topic and its reviewed date unchanged.

**5d. Correct errors and fill gaps.** Prepare corrections in a temporary
draft, not the live topic file:
- Patch inaccurate, outdated, incomplete, or noncompliant sections.
  Preserve correct material; add substantive detail, not padding.
- Preserve the template's body structure. Do not add or remove
  `##` section headings unless the content requires a new section
  that did not exist before.
- Remove or replace stale, superseded, incorrect, duplicate, or unused
  sources. Update or remove their citations throughout the text. Keep valid
  sources that still support retained claims; age alone does not invalidate
  a historical source. Add relevant verified sources for new material.
- All rewritten content MUST be ASCII-only.
- All new factual claims MUST trace to a source in the Sources
  section (G3 from the template).
- New sources MUST include authority ratings [high], [medium], or
  [low] (G4 from the template).

### 6. Re-read the template and verify its checklist

Re-read `governance/template-library.md` in full. Verify the entire final
draft, including unchanged sections, against its Library Topic Checklist.
Run the section word-count check and verify every content, source, format,
and cross-reference requirement. Keep the original ID and author; do not
repeat creation-only actions (new ID, initial omission of `reviewed`, or
candidate selection/scoring). Fix failures and recheck the final draft.
If any applicable item remains unconfirmed, record ERROR and do not stamp
or publish that topic as reviewed. Do not put the checklist in the topic.

### 7. Stamp the reviewed date

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

### 8. Write logbook entry

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
- <title> (<domain>): current, no changes
- <title> (<domain>): rewritten (corrected <mismatches>, updated <sources/sections>)
Domain coverage: reviewed across N domains.
```

For unresolved topics or execution failures, prepare a log-only body
beginning `ERROR:` with the topic, failed check, and unresolved evidence.
Do not count unresolved topics as reviewed. If the helper cannot publish
safely, surface its HALT result to the caller; never bypass the lock to
write a failure entry.

### 9. Commit on the VPS clone -- NO push

Follow `agentic-brain:library/guide-library.md#publication`.
Use `kind: review` with only completed topic drafts, their captured expected
hashes, and the log body. The helper rechecks topic bytes and six-month
eligibility before saving the reviewed topics and log in one commit.
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