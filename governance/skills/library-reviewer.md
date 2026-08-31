---
name: library-reviewer
description: "Review and refresh existing library topics: find topics overdue for review via the per-domain index files, re-read each topic, web-search to verify accuracy, rewrite stale sections in-place, stamp reviewed date in frontmatter. VPS-native dual-option: direct read/write for VPS agents, SSH transfer for VPS-connected agents -- no clone, no push, the watcher pushes. Use when the review cron cycle fires."
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

Invoke when the cron scheduler triggers a review cycle. Each cycle
picks up to 5 topics that are overdue for review and processes them
sequentially.

Skip for:
- No topics overdue for review (all within their domain threshold)
- Topics in quarantine directory

## Path Convention -- Dual Platform

The brain working copy lives at `/srv/brain/agentic-brain` on the
fleet VPS. The watcher keeps it in two-way sync with GitHub and
pushes commits. There is NO clone step and NO push step in this
skill.

- **VPS agents** (running on the server, no SSH): every path below is
  a literal filesystem path under `/srv/brain/agentic-brain/`. Write
  files directly and commit as yourself (agents group, no su).
- **VPS-connected agents** (remote machines, e.g. PC or laptop
  agents): read and write through the key door, commit via su:

```bash
# read a brain file
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat /srv/brain/agentic-brain/<path>'

# write a brain file from local scratch
cat "<local-scratch>" | ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'cat > /srv/brain/agentic-brain/<path>'

# commit (one or more paths)
ssh -i "$VPS_SSH_KEY" -p 22 root@100.99.142.120 \
  'su - hermes -c "cd /srv/brain/agentic-brain && git add <path1> <path2> && git commit -m \"<msg>\" && echo COMMITTED"'
```

Quoting rule: the remote command sits in double quotes; inner quotes
sit in single quotes. A broken quote fails the whole command.

## Domain Review Thresholds

Different domains age at different rates. The reviewer uses these
thresholds to determine when a topic is overdue:

| Cadence | Months | Domains |
|:--|:--|:--|
| Fast-moving | 3 | coding-agentic-ai, technology |
| Moderate | 6 | finance, geopolitics, health-medicine, industries-sectors, science, macro-micro |
| Slow | 12 | history, anthropology, ethics-philosophy, pop-culture, books, communication, education-learning, law-regulation, psychology-behavior, case-studies, notable-people, self-improvement |
| Timeless | 24 | mathematics-statistics, value-investing, investors, valuation-screening, portfolio-risk-management, probabilistic-thinking-forecasting, accounting-financial-shenanigans |

A topic is overdue if:
- It has no `reviewed:` field in frontmatter (never reviewed)
- Its `reviewed:` date is older than the domain's threshold

## Accuracy Threshold

The reviewer verifies each topic against current web sources. After
re-reading the topic and web-searching its key claims:

- **85%+ of claims still accurate:** topic is current. Stamp
  `reviewed: <today>`, no content changes needed.
- **Below 85%:** topic is stale. Rewrite the inaccurate sections
  in-place, update the Sources section with current URLs, then stamp
  `reviewed: <today>`.

The 85% threshold is the reviewer's judgment, not a mechanical word
count. It means "most of the content is still correct; a few specific
claims or sections need updating." If the topic's core thesis is
wrong or the field has fundamentally changed, that is below 85% --
rewrite the affected sections.

## Final Self-Check -- HARD GATE

Confirm ALL items before committing. One checklist -- no
sub-checklists, no section summaries. Each item maps to a procedure
step or a library guide rule. HALT on any failure; fix before
committing.

- [ ] Procedure completed: read index, select overdue topics, read template, review each topic, verify sources, rewrite if needed, stamp reviewed date, log, commit (PASS / HALT)
- [ ] Template read before reviewing: `template-library.md` opened in step 4 and used as format reference for any rewrites (PASS / HALT)
- [ ] Topics selected are genuinely overdue: no `reviewed:` field OR `reviewed:` date exceeds domain threshold (PASS / HALT)
- [ ] Each topic read in full before web-searching (PASS / HALT)
- [ ] Web search conducted for each topic to verify key claims against current sources (PASS / HALT)
- [ ] Accuracy assessment recorded: approximate percentage of claims still accurate (PASS / HALT)
- [ ] If stale: rewritten sections preserve the template's body structure (Background, Core Concepts, Evidence, Implications, Sources, See Also) (PASS / HALT)
- [ ] If stale: Sources section updated with current URLs; broken links replaced (PASS / HALT)
- [ ] If stale: rewritten content is ASCII-only (PASS / HALT)
- [ ] `reviewed: <YYYY-MM-DD>` added or updated in frontmatter of each reviewed topic (PASS / HALT)
- [ ] No topic content changed beyond what was needed for accuracy (no cosmetic rewrites) (PASS / HALT)
- [ ] Logbook entry written to logbook/library.log (PASS / HALT)
- [ ] Logbook entry format: each data field on its own line, matching the step 9 example exactly (PASS / HALT)
- [ ] Logbook entry properly separated: exactly one blank line between this entry and the previous (PASS / HALT)
- [ ] Committed on the VPS clone: split-commit pattern followed (topic files first, then pull --rebase + re-read shared files, then commit shared files). Never `git add -A` in the shared clone. (PASS / HALT)
- [ ] Watcher push verified: AHEAD: 0 or fresh push line in /srv/brain/logs/brain-pull.log (PASS / HALT)

## Procedure

### 1. Locate the brain working copy

VPS agents: `cd /srv/brain/agentic-brain`. The watcher keeps the
clone fresh (<= 1 min behind GitHub). Trust your reads.

VPS-connected agents: no local clone. Every read and write below goes
through the Path Convention commands above.

### 2. Read the master index

Read `library/index-library.md`. Note the topic counts per domain.
The master index gives the full domain coverage table.

### 3. Select overdue topics

Read per-domain `index-<domain>.md` files to find topics with
`[reviewed: never]` or `[reviewed: <date>]` where the date is older
than the domain's threshold (see Domain Review Thresholds above).

Prioritize:
1. Topics with `[reviewed: never]` (never reviewed -- highest
   priority).
2. Topics with the oldest `reviewed:` dates (most overdue).
3. Spread across domains if possible (do not review 5 topics from
   the same domain in one cycle unless that domain has the most
   overdue topics).

Select up to 5 topics for this cycle.

A bash one-liner can help identify overdue topics across all domains:

```bash
cd /srv/brain/agentic-brain
for d in library/*/; do
  domain=$(basename "$d")
  idx="${d}index-${domain}.md"
  [ -f "$idx" ] && grep '\[reviewed: never\]\|\[reviewed: [0-9]' "$idx"
done
```

The index files show the reviewed date on every topic line. Use the
domain thresholds to determine which are overdue. Pick the 5 most
overdue across all domains.

### 4. Read the library template

Read `governance/template-library.md` before reviewing. This is the
format specification for library topics. Any rewrites MUST preserve
the template's body structure (Background, Core Concepts, Evidence,
Implications, Sources, See Also) and follow the same formatting
rules (ASCII-only, lowercase slugs, hyphens, authority-rated sources).

### 5. Review each topic

For each selected topic, in order:

**5a. Read the topic file.** Read
`library/<domain>/<topic-slug>.md` in full. Note the key claims,
the Sources section, and the body structure.

**5b. Web-search to verify.** Search for the topic's key claims to
check if they are still accurate. Focus on:
- Core factual claims (numbers, dates, study results, named
  entities).
- Sources -- do the URLs still work? Has the source been updated?
- Any time-sensitive claims (current events, market data, technology
  specifics, regulatory references).

**5c. Assess accuracy.** Estimate what percentage of the topic's
claims are still accurate:
- If 85%+ are still accurate: the topic is current. No content
  changes needed. Proceed to step 6 (stamp the date).
- If below 85%: the topic is stale. Proceed to step 5d (rewrite).

**5d. Rewrite stale sections (if needed).** When the topic is stale:
- Rewrite only the sections that contain inaccurate or outdated
  claims. Do not rewrite the entire topic -- patch the stale parts.
- Preserve the template's body structure. Do not add or remove
  `##` section headings unless the content requires a new section
  that did not exist before.
- Update the Sources section: replace dead URLs with working ones,
  add new sources if new evidence is available, keep sources that
  are still valid.
- All rewritten content MUST be ASCII-only.
- All new factual claims MUST trace to a source in the Sources
  section (G3 from the template).
- New sources MUST include authority ratings [high], [medium], or
  [low] (G4 from the template).

### 6. Stamp the reviewed date

For each reviewed topic, add or update the `reviewed:` field in the
topic file's frontmatter. Use today's date in `YYYY-MM-DD` format.

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

### 7. Verify cross-references (if content changed)

If any content was rewritten in step 5d, verify that all
cross-references in `## See Also` and `links:` frontmatter still
point to files that exist. If a rewrite removed a reference to a
topic that no longer exists in the text, update the cross-reference
list. Verify with `ls <path>` before committing.

### 8. Run the index regeneration script

After all topics are reviewed and stamped, regenerate the index so
the `reviewed:` dates show up in the per-domain index files:

```bash
cd /srv/brain/agentic-brain
/opt/repo-tools/venv/bin/python scripts/index-library.py
```

This updates `library/index-library.md` and every per-domain
`index-<domain>.md` file with the new `reviewed:` dates. The
GitHub Action will also regenerate on push, but running it locally
ensures the index is current in the VPS clone before commit.

### 9. Write logbook entry

Append to `logbook/library.log`. The logbook entry MUST follow this
exact format. Each data field MUST be on its own line. Topics MUST
be listed one per line using bullet points (`-`). Do NOT pack
multiple fields onto a single line.

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md
Review cycle: N topics reviewed, M current, K rewritten.
Topics:
- <title> (<domain>): current, no changes
- <title> (<domain>): rewritten (accuracy ~X%, updated sources, rewrote <sections>)
Domain coverage: reviewed across N domains.
```

Increment ENT counter from the last entry in library.log.

Before appending, check whether the file already ends with a blank
line. If the last character is a newline (the file has a trailing
blank line from the previous entry), append directly without adding
another blank line. If it is not, add ONE blank line, then append
your entry. Never add a second blank line -- double gaps between
entries are a format violation.

### 9a. Log errors (if any)

If any step failed or produced unexpected results (file write
error, commit rejection, or any crash), append to
`logbook/errors.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | error | ref: library/<domain>/<topic-slug>.md | see: <related-ent-id>
<description of what went wrong, what was expected, and any partial results>
```

Only write to errors.log if something actually failed. Successful
review cycles go to library.log. Errors.log is for unexpected
failures only.

### 10. Commit on the VPS clone -- NO push

The watcher pushes within 1 min and reindexes. Verify after ~1 min:
`AHEAD: 0`, or a fresh push line in /srv/brain/logs/brain-pull.log.

**Split-commit pattern (prevents shared-file race conditions):**

The topic files you reviewed are unique -- no other agent touches the
same topic file in the same cycle. But shared files (library.log,
index files, candidate-queue.md) can be modified by other agents
running simultaneously. To avoid overwriting their changes, commit
the topic files first, then sync and re-read shared files before
modifying them.

**Phase 1 -- commit the reviewed topic files (no race possible):**

```bash
cd /srv/brain/agentic-brain
git add library/<domain>/<topic-slug>.md
git commit -m "library: review -- <topic-slug> reviewed + updated"
```

**Phase 2 -- sync, re-read, then commit shared files:**

```bash
git pull --rebase origin main
```

Re-read `logbook/library.log` from the filesystem -- it may have
changed since you last read it. Append your logbook entry to the
CURRENT version, not the version you read earlier. Re-run the index
regeneration script if other agents wrote new topics during your
session:

```bash
/opt/repo-tools/venv/bin/python scripts/index-library.py
git add library/index-library.md library/*/index-*.md logbook/library.log
git diff --cached --stat   # verify ONLY your paths are staged
git commit -m "library: review cycle -- N topics reviewed (M current, K rewritten)"
```

VPS-connected agents: run the same commands through the commit
command in the Path Convention.

NEVER `git add -A` in the shared clone -- it stages other agents'
in-progress files. Stage only this cycle's paths.

## Related

- `agentic-brain:governance/template-library.md` -- topic format specification (read before any rewrites)
- `agentic-brain:library/guide-library.md` -- pipeline architecture, weights, anchor format
- `agentic-brain:research/insights/library-system.md` -- full system blueprint, anti-staleness design
- `agentic-brain:governance/skills/library-writer.md` -- writer skill (produces new topics)
- `agentic-brain:governance/skills/library-discoverer.md` -- discoverer skill (proposes candidates)
- `agentic-brain:logbook/protocol.md` -- logbook entry format