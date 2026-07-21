---
name: library-writer
description: "Research and write a library topic file: web-search, synthesize, score across 4 dimensions, check anchor compliance and topic similarity before writing. Use when a candidate topic is ready from the discovery queue."
user-invocable: false
disable-model-invocation: false
---

# Library Writer (v2)

## What This Skill Does

Guides the writing process of the library pipeline. Receives a candidate
topic title + domain anchor from the discovery queue, performs web
search, synthesizes knowledge, and writes a markdown topic file to the
domain folder. Scores the candidate across 4 dimensions before writing.
Checks anchor compliance, topic similarity, and source credibility.
For the full pipeline architecture and weight rules, read
`brain:library/guide-library.md` and
`brain:research/insights/library-system.md`.

## When to Invoke

Invoke when a candidate topic is ready from the discovery queue and a
writing cycle is triggered by the cron scheduler. The writer processes
one candidate topic per cycle.

Skip for:
- Topics already covered by an existing file (>= 80% semantic overlap)
- Topics whose weighted score falls below 7.0
- Domains without an anchor file
- Topics whose sources are too weak to proceed (authority < 3.0 AND
  core match would still not reach 7.0 after accounting for it)

## Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, pick candidate, read anchor, research, score all 4 dimensions, check similarity, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure verification: all items confirmed PASS (PASS / HALT)
- [ ] Scoring verification: all 4 dimensions scored, weighted sum calculated (PASS / HALT)
- [ ] File Output verification: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-writer && git clone --depth 1 \
  "https://${OPEN...KEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-writer
```

### 2. Pick a candidate topic from the discovery queue

Read `/tmp/brain-writer/library/candidate-queue.md`. Select the
highest-scored unaudited candidate. Note the candidate ID, title,
domain, and proposed scope.

If the queue is empty, log to `library.log` and exit.

### 3. Read the domain anchor

Read `/tmp/brain-writer/library/<domain>/anchor-<domain>.md`. This is
the eternal reference against which all topics are measured. The
anchor paragraph, scope (In/Out), and adjacent domain boundary rules
are non-negotiable.

### 4. Research the topic

Perform web search using the domain name + topic title as query terms.
Collect 3-5 sources. Evaluate source quality:
- **High authority (8-10):** academic papers, reputable publications,
  primary sources, official data.
- **Medium authority (4-7):** reputable blogs, industry publications,
  secondary sources with attribution.
- **Low authority (1-3):** personal blogs, forums, unattributed content.

Synthesize into a coherent topic file following the library topic
format (see Body Structure verification below).

### 5. Score the candidate (writer weight, v2: 4 dimensions)

Before writing, score the candidate topic across four dimensions
using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Core match | 0.35 | How central is this topic to the domain anchor? |
| Scope fit | 0.35 | Does it fit In scope? Avoid Out scope and adjacent overlap? |
| Knowledge value | 0.20 | Would this compound with existing brain knowledge? |
| Source authority | 0.10 | Are the web sources credible? Rated by the high/medium/low scale above. |

Calculate weighted score: `(core * 0.35) + (scope * 0.35) + (value * 0.20) + (authority * 0.10)`.

- >= 7.0: proceed to write.
- 5.0-6.9: log to library.log with FLAG and the scores. Skip.
- < 5.0: log to library.log with REJECT and suggested redirect domain. Skip.

### 6. Check topic similarity

Scan existing topic files in `library/<domain>/` for semantic overlap
with the candidate topic. Estimate overlap percentage:

- >= 80% overlap: skip. Log DUPLICATE to library.log.
- 50-80% overlap: proceed but cross-reference the existing topic and
  focus on the uncovered portion.
- < 50% overlap: proceed normally.

### 7. Write the topic file

Write ONLY to the agentic-brain. NEVER write topic files to the
workspace.

Path: `/tmp/brain-writer/library/<domain>/<topic-slug>.md`

`<topic-slug>`: lowercase kebab-case, max 80 chars, unique within the
domain. Derive from the topic title.

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the library guide rules. HALT on
any failure; fix before committing.

### Frontmatter

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "library-topic" (PASS / HALT)
- [ ] domain: `<domain-slug>` matching the folder name (PASS / HALT)
- [ ] author: agent name (e.g. Ava, Link, Researcher-1) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, domain-specific (PASS / HALT)
- [ ] links: relative paths from brain root (PASS / HALT)

### Body Structure

- [ ] Title is a level-1 heading making a claim about the topic (PASS / HALT)
- [ ] Opening paragraph summarizes the topic in 2-3 sentences (PASS / HALT)
- [ ] Body sections organized logically with ## headings (PASS / HALT)
- [ ] Sources cited: at least 3 web sources with URLs in a `## Sources` section (PASS / HALT)
- [ ] Source authority rated: each source annotated with high/medium/low rating (PASS / HALT)
- [ ] Cross-references to related library topics included where applicable (PASS / HALT)

### Scoring

- [ ] All four dimensions scored (core match, scope fit, knowledge value, source authority) (PASS / HALT)
- [ ] Each dimension has a brief justification (1-2 sentences) (PASS / HALT)
- [ ] Weighted score calculated correctly: (core*0.35 + scope*0.35 + value*0.20 + authority*0.10) (PASS / HALT)
- [ ] Weighted score >= 7.0 confirmed before writing (PASS / HALT)
- [ ] Topic similarity check completed; overlap estimate recorded (PASS / HALT)
- [ ] Source authority checked: 3+ sources, each rated on the high/medium/low scale (PASS / HALT)

### File Output

- [ ] File named: lowercase kebab-case slug, matching topic title (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-writer/library/<domain>/ (NOT workspace) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (PASS / HALT)

### 8. Write logbook entry

Append to `/tmp/brain-writer/logbook/library.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <candidate-id>
Wrote topic <title> to <domain>. Weighted score: X.X/10.0
(core=X.X, scope=X.X, value=X.X, authority=X.X).
Similarity overlap: X%. Sources: N (N high, N medium, N low).
Cross-references: N topics.
```

Increment ENT counter from the last entry in library.log.

### 9. Remove the candidate from the queue

Remove the processed candidate entry from
`/tmp/brain-writer/library/candidate-queue.md`.

### 10. Commit and push

```bash
cd /tmp/brain-writer
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: write <topic-slug> to <domain>"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 11. Discard the clone

```bash
cd /tmp && rm -rf brain-writer
```

## Related

- `brain:library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `brain:research/insights/library-system.md` -- full system blueprint, scoring rationale
- `brain:governance/library-auditor.md` -- auditor skill (reviews written topics)
- `brain:governance/library-discoverer.md` -- discoverer skill (proposes candidates)
- `brain:logbook/protocol.md` -- logbook entry format