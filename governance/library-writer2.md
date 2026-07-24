---
name: library-writer2
description: "Research and write a library topic file: web-search, synthesize, score across 4 dimensions, check anchor compliance and topic similarity before writing. Use when a candidate topic is ready from the discovery queue."
user-invocable: false
disable-model-invocation: false
---

# Library Writer (v4)

## What This Skill Does

Guides the writing process of the library pipeline. Receives a candidate
topic title + domain anchor from the discovery queue, performs web
search, synthesizes knowledge, and writes a markdown topic file to the
domain folder. Scores the candidate across 4 dimensions before writing.
For the full format specification with frontmatter schema, body structure,
mandatory sections, quality gates (G1-G11), and a complete example, read
`governance/template-library2.md`. Follow it exactly.

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

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, read template, pick candidate, read anchor, research, score all 4 dimensions, check similarity, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Writer Scoring Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `template-library2.md` Self-Check: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)
- [ ] Errors logged to errors.log (if any) (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
set -a && source "/c/AI Stuff/Hermes Agent/profiles/link/.env" && set +a
cd /tmp && rm -rf brain-writer && git clone --depth 1 \
  "https://${GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-writer
```

If GITHUB_TOKEN is unset after sourcing .env, fall back to:
`export GITHUB_TOKEN=$(gh auth token 2>/dev/null)`. HALT if neither works.

### 2. Read the format specification

Read `governance/template-library2.md`. It defines the body structure
(mandatory sections in order), frontmatter schema (7 fields), quality
gates (G1-G11), library-specific gates (L1-L4), and the complete
example. Follow it exactly. Do not substitute your own section order
or naming -- the template is the single source of format truth.

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
defined in `governance/template-library2.md`.

### 6. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 7. Score the candidate (writer weight, v2: 4 dimensions)

Before writing, score the candidate topic across four dimensions
using a 0.0-10.0 scale:

| Dimension | Weight | What it measures |
|:--|:--|:--|
| Core match | 0.35 | How central is this topic to the domain anchor? |
| Scope fit | 0.35 | Does it fit In scope? Avoid Out scope and adjacent overlap? |
| Knowledge value | 0.20 | Would this compound with existing brain knowledge? |
| Source authority | 0.10 | Are the web sources credible? Rated by the high/medium/low scale above. |

Calculate weighted score:
`(core * 0.35) + (scope * 0.35) + (value * 0.20) + (authority * 0.10)`.

- >= 7.0: proceed to write.
- 5.0-6.9: log to library.log with FLAG and the scores. Skip.
- < 5.0: log to library.log with REJECT and suggested redirect domain. Skip.

Record the scores in the topic file using the format specified in the
Writer Scoring Sub-Checklist below.

### 8. Check topic similarity

Scan existing topic files in `library/<domain>/` for semantic overlap
with the candidate topic. Estimate overlap percentage:

- >= 80% overlap: skip. Log DUPLICATE to library.log.
- 50-80% overlap: proceed but cross-reference the existing topic and
  focus on the uncovered portion.
- < 50% overlap: proceed normally.

### 9. Write the topic file

Write ONLY to the agentic-brain. NEVER write topic files to the
workspace. Follow the body structure and section order specified in
`governance/template-library2.md` exactly.

Path: `/tmp/brain-writer/library/<domain>/<topic-slug>.md`

`<topic-slug>`: lowercase kebab-case, max 80 chars, unique within the
domain. Derive from the topic title.

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to the
template-library2.md Self-Check and quality gates (G1-G11, L1-L4).
HALT on any failure; fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "library-topic" (PASS / HALT)
- [ ] domain: `<domain-slug>` matching the folder name exactly (PASS / HALT)
- [ ] author: agent name capitalized (e.g. Ava, Link, Researcher-1) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, domain-specific (PASS / HALT)
- [ ] links: relative paths from brain root. No `brain:` prefix. (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Title is a level-1 heading making a claim about the topic (G1) (PASS / HALT)
- [ ] Opening paragraph summarizes the topic in 2-3 sentences (G2) (PASS / HALT)
- [ ] `## Background` section present -- historical/intellectual context. MUST appear after opening paragraph. (PASS / HALT)
- [ ] `## Core Concepts` section present -- essential ideas. Title MAY vary by domain (e.g. `## Core Biases by Category`, `## Core Principles`) but MUST exist. (PASS / HALT)
- [ ] `## Evidence` section present -- empirical support, research findings. Title MAY vary (e.g. `## Evidence and Research Foundation`) but MUST exist. (PASS / HALT)
- [ ] `## Implications` section present -- why the topic matters, practical application. MUST exist. (PASS / HALT)
- [ ] Domain-specific body sections (if any) positioned correctly: between Core Concepts and Evidence (expansion sections) OR after Implications (frameworks, pitfalls, criticisms). See template-library2.md Section Order. (PASS / HALT)
- [ ] `## Writer Scoring` section present with all 4 dimensions scored, justifications, weighted formula, and similarity overlap (PASS / HALT)
- [ ] `## Sources` section present with 3+ sources, each annotated with authority rating (high/medium/low) (G4) (PASS / HALT)
- [ ] `## See Also` section present with 1+ cross-reference to a related library topic or brain artifact (G5) (PASS / HALT)
- [ ] Section order enforced: Background -> Core Concepts -> (domain expansion sections) -> Evidence -> Implications -> (pitfalls/criticisms/frameworks) -> Writer Scoring -> Sources -> See Also (G11) (PASS / HALT)
- [ ] No content follows `## See Also` (G11) (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Title Makes a Claim) -- PASS. Reader can agree or disagree. (PASS / HALT)
- [ ] G2 (Opening Paragraph Self-Contained) -- PASS. Reader with no domain knowledge understands the topic. (PASS / HALT)
- [ ] G3 (Every Claim Sourced) -- PASS. Every factual claim traces to a source. Synthesized claims labeled. (PASS / HALT)
- [ ] G4 (Sources Have Authority Ratings, 2+ high/medium) -- PASS. 2 of 3+ sources rated high or medium. (PASS / HALT)
- [ ] G5 (Cross-references Exist) -- PASS. At least 1 link to related topic or brain artifact. (PASS / HALT)
- [ ] G6 (Domain Anchor Compliant) -- PASS. Topic stays within anchor In scope, avoids Out scope. (PASS / HALT)
- [ ] G7 (Topic Similarity Checked) -- PASS. Overlap estimate recorded. (PASS / HALT)
- [ ] G8 (Frontmatter Complete, id from date command) -- PASS. All 7 fields present, id machine-generated. (PASS / HALT)
- [ ] G9 (Formatting Rules: ASCII-only, lowercase, hyphens) -- PASS. CI enforces. (PASS / HALT)
- [ ] G10 (Output Destination Correct: library/<domain>/, not workspace) -- PASS. (PASS / HALT)
- [ ] G11 (Section Order: mandatory sections present and in correct sequence) -- PASS. (PASS / HALT)

### Library Gates Sub-Checklist

- [ ] L1 (Pipeline Integration) -- Candidate ID from queue recorded in Writer Scoring. (PASS / HALT)
- [ ] L2 (Anchor Freshness) -- Domain anchor read and confirmed current. Anchor paragraph not summarized from memory. (PASS / HALT)
- [ ] L3 (Candidate Queue Updated) -- Processed candidate removed from candidate-queue.md. (PASS / HALT)
- [ ] L4 (Library Log Written) -- Entry appended to logbook/library.log with ENT counter, scores, sources, and overlap. (PASS / HALT)

### Writer Scoring Sub-Checklist

- [ ] All 4 dimensions scored with justifications: core match, scope fit, knowledge value, source authority (PASS / HALT)
- [ ] Format: `**Dimension:** X.X/10.0 -- <1-2 sentence justification>` (PASS / HALT)
- [ ] Weighted formula shown: `(core * 0.35) + (scope * 0.35) + (value * 0.20) + (authority * 0.10) = **X.X/10.0**` (PASS / HALT)
- [ ] Final weighted score calculated correctly (PASS / HALT)
- [ ] Topic similarity overlap percentage recorded (PASS / HALT)
- [ ] Writer Scoring appears after last body section and before `## Sources` (PASS / HALT)
- [ ] Candidate queue ID referenced in the scoring justification (L1) (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, matching topic title (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-writer/library/<domain>/ (NOT workspace) (G10) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G9) (PASS / HALT)
- [ ] Candidate removed from candidate-queue.md (L3) (PASS / HALT)

### 10. Write logbook entry

Append to `/tmp/brain-writer/logbook/library.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <candidate-id>
Wrote topic <title> to <domain>. Weighted score: X.X/10.0
(core=X.X, scope=X.X, value=X.X, authority=X.X).
Similarity overlap: X%. Sources: N (N high, N medium, N low).
Cross-references: N topics.
```

Increment ENT counter from the last entry in library.log.

### 11. Remove the candidate from the queue

Remove the processed candidate entry from
`/tmp/brain-writer/library/candidate-queue.md`.

### 12. Log errors (if any)

If any step failed or produced unexpected results (score below threshold,
duplicate topic detected, source authority too low, push conflict),
append to `/tmp/brain-writer/logbook/errors.log`:

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | error | ref: library/<domain>/<topic-slug>.md | see: <related-ent-id>
<description of what went wrong, what was expected, and any partial results>
```

Only write to errors.log if something actually failed. Successful writes
and normal pipeline outcomes (FLAG, REJECT, DUPLICATE) go to library.log.

### 13. Commit and push

```bash
cd /tmp/brain-writer
git add -A
git diff --cached --stat
git -c user.name="<agent-name>" -c user.email="<agent-email>" \
  commit -m "library: write <topic-slug> to <domain>"
git push origin main
```

If the push fails, pull first, resolve, then push.

### 14. Discard the clone

```bash
cd /tmp && rm -rf brain-writer
```

## Related

- `governance/template-library2.md` -- full format specification, mandatory body sections, quality gates G1-G11 + L1-L4, self-check, complete example
- `library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `research/insights/library-system.md` -- full system blueprint, scoring rationale
- `governance/library-auditor.md` -- auditor skill (reviews written topics)
- `governance/library-discoverer.md` -- discoverer skill (proposes candidates)
- `logbook/protocol.md` -- logbook entry format
