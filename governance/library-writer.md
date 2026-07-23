---
name: library-writer
description: "Research and write a library topic file: web-search, synthesize, score across 4 dimensions, check anchor compliance and topic similarity before writing. Use when a candidate topic is ready from the discovery queue."
user-invocable: false
disable-model-invocation: false
---

# Library Writer (v3)

## What This Skill Does

Guides the writing process of the library pipeline. Receives a candidate
topic title + domain anchor from the discovery queue, performs web
search, synthesizes knowledge, and writes a markdown topic file to the
domain folder. Scores the candidate across 4 dimensions before writing.
For the full format specification with frontmatter schema, body structure,
mandatory sections, quality gates (G1-G11), and a complete example, read
`governance/template-library.md`. Follow it exactly.

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

- [ ] Procedure completed (clone, read template, pick candidate, read anchor, research, score all 4 dimensions, check similarity, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Template-library checklist: all items confirmed PASS (per `governance/template-library.md`) (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)
- [ ] Errors logged to errors.log (if any) (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-writer && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-writer
```

### 2. Read the format specification

Read `governance/template-library.md`. It defines the body structure
(mandatory sections in order), frontmatter schema (7 fields), quality
gates (G1-G11), and the complete example. Follow it exactly. Do not
substitute your own section order or naming -- the template is the
single source of format truth.

### 3. Pick a candidate topic from the discovery queue

Read `/tmp/brain-writer/library/candidate-queue.md`. Select the
highest-scored unaudited candidate (by discoverer score). Note the
candidate ID, title, domain, and proposed scope.

If the queue is empty, log to `library.log` and exit.

### 4. Read the domain anchor

Read `/tmp/brain-writer/library/<domain>/anchor-<domain>.md`. This is
the eternal reference against which all topics are measured. The
anchor paragraph, scope (In/Out), and adjacent domain boundary rules
are non-negotiable.

### 5. Research the topic

Perform web search using the domain name + topic title as query terms.
Collect 3-5 sources. Evaluate source quality:
- **High authority (8-10):** academic papers, reputable publications,
  primary sources, official data.
- **Medium authority (4-7):** reputable blogs, industry publications,
  secondary sources with attribution.
- **Low authority (1-3):** personal blogs, forums, unattributed content.

Synthesize into a coherent topic file following the body structure
defined in `governance/template-library.md`.

### 6. Score the candidate (writer weight, v2: 4 dimensions)

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

### 7. Check topic similarity

Scan existing topic files in `library/<domain>/` for semantic overlap
with the candidate topic. Estimate overlap percentage:

- >= 80% overlap: skip. Log DUPLICATE to library.log.
- 50-80% overlap: proceed but cross-reference the existing topic and
  focus on the uncovered portion.
- < 50% overlap: proceed normally.

### 8. Write the topic file

Write ONLY to the agentic-brain. NEVER write topic files to the
workspace. Follow the body structure and section order specified in
`governance/template-library.md` exactly.

Path: `/tmp/brain-writer/library/<domain>/<topic-slug>.md`

`<topic-slug>`: lowercase kebab-case, max 80 chars, unique within the
domain. Derive from the topic title.

### 9. Write logbook entry

Append to `/tmp/brain-writer/logbook/library.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <candidate-id>
Wrote topic <title> to <domain>. Weighted score: X.X/10.0
(core=X.X, scope=X.X, value=X.X, authority=X.X).
Similarity overlap: X%. Sources: N (N high, N medium, N low).
Cross-references: N topics.
```

Increment ENT counter from the last entry in library.log.

### 10. Remove the candidate from the queue

Remove the processed candidate entry from
`/tmp/brain-writer/library/candidate-queue.md`.

### 10a. Log errors (if any)

If any step failed or produced unexpected results (score below threshold,
duplicate topic detected, source authority too low, push conflict),
append to `/tmp/brain-writer/logbook/errors.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | error | ref: library/<domain>/<topic-slug>.md | see: <related-ent-id>
<description of what went wrong, what was expected, and any partial results>
```

Only write to errors.log if something actually failed. Successful writes
and normal pipeline outcomes (FLAG, REJECT, DUPLICATE) go to library.log.
Errors.log is for unexpected failures: clone failed, push rejected,
file write error, or any crash.

### Frontmatter

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "library-topic" (PASS / HALT)
- [ ] domain: `<domain-slug>` matching the folder name (PASS / HALT)
- [ ] author: agent name (e.g. Ava, Link, Researcher-1) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, domain-specific (PASS / HALT)
- [ ] links: relative paths from brain root (PASS / HALT)

### Body Structure

- [ ] Title is a level-1 heading making a claim about the topic (G1) (PASS / HALT)
- [ ] Opening paragraph summarizes the topic in 2-3 sentences (G2) (PASS / HALT)
- [ ] `## Background` section present -- historical/intellectual context (PASS / HALT)
- [ ] `## Core Concepts` section present -- essential ideas. Title MAY vary by domain (e.g. `## Core Biases by Category`) but MUST exist. (PASS / HALT)
- [ ] `## Evidence` section present -- empirical support, research findings. Title MAY vary (e.g. `## Evidence and Research Foundation`) but MUST exist. (PASS / HALT)
- [ ] `## Implications` section present -- why the topic matters, practical application (PASS / HALT)
- [ ] Domain-specific body sections (if any) positioned correctly: between Core Concepts and Evidence, or between Implications and Writer Scoring (PASS / HALT)
- [ ] `## Writer Scoring` section present with all 4 dimensions scored, justifications, weighted formula, and similarity overlap recorded (PASS / HALT)
- [ ] `## Sources` section present with 3+ sources, each annotated with authority rating (high/medium/low) (PASS / HALT)
- [ ] `## See Also` section present with 1+ cross-reference to a related library topic or brain artifact (PASS / HALT)
- [ ] Section order: Background -> Core Concepts -> (domain sections) -> Evidence -> Implications -> (optional sections) -> Writer Scoring -> Sources -> See Also (G11) (PASS / HALT)
- [ ] No content follows `## See Also` (G11) (PASS / HALT)

### Quality Gates

- [ ] G1 (Title Makes a Claim) -- PASS (PASS / HALT)
- [ ] G2 (Opening Paragraph Self-Contained) -- PASS (PASS / HALT)
- [ ] G3 (Every Claim Sourced) -- PASS (PASS / HALT)
- [ ] G4 (Sources Have Authority Ratings, 2+ high/medium) -- PASS (PASS / HALT)
- [ ] G5 (Cross-references Exist) -- PASS (PASS / HALT)
- [ ] G6 (Domain Anchor Compliant) -- PASS (PASS / HALT)
- [ ] G7 (Topic Similarity Checked) -- PASS (PASS / HALT)
- [ ] G8 (Frontmatter Complete, id from date command) -- PASS (PASS / HALT)
- [ ] G9 (Formatting Rules: ASCII-only, lowercase, hyphens) -- PASS (PASS / HALT)
- [ ] G10 (Output Destination Correct: library/<domain>/, not workspace) -- PASS (PASS / HALT)
- [ ] G11 (Section Order: mandatory sections present and in correct sequence) -- PASS (PASS / HALT)

### File Output

- [ ] File named: lowercase kebab-case slug, matching topic title (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-writer/library/<domain>/ (NOT workspace) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (PASS / HALT)

### 11. Commit and push

```bash
cd /tmp/brain-writer
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: write <topic-slug> to <domain>"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 12. Discard the clone

```bash
cd /tmp && rm -rf brain-writer
```

## Format Verification -- HARD GATE (before commit)

Verify every item below. Each maps to the template-library checklist
and quality gates. HALT on any failure; fix before committing.

## Related

- `governance/template-library.md` -- full format specification, mandatory body sections, quality gates G1-G11, complete example
- `library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `research/insights/library-system.md` -- full system blueprint, scoring rationale
- `governance/library-auditor.md` -- auditor skill (reviews written topics)
- `governance/library-discoverer.md` -- discoverer skill (proposes candidates)
- `logbook/protocol.md` -- logbook entry format
