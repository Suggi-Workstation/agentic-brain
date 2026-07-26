---
name: library-writer
description: "Research and write a library topic file to the agentic-brain. Follows the write-X pattern with Final Self-Check plus Sub-Checklists for frontmatter, body structure, quality gates, scoring, and file output. Reads governance/template-library.md for the full format specification."
user-invocable: false
disable-model-invocation: false
---

# Library Writer

## What This Skill Does

Guides the writing process of the library pipeline. Receives a candidate
topic title + domain anchor from the discovery queue, performs web
search, synthesizes knowledge, and writes a markdown topic file to the
domain folder. Scores the candidate across 4 dimensions before writing.
For the full format specification with frontmatter schema, body
structure, mandatory sections, quality gates (G1-G12), anti-patterns,
and a complete example, read `governance/template-library.md`. Follow
it exactly.

## When to Invoke

Invoke when a candidate topic is ready from the discovery queue and a
writing cycle is triggered by the cron scheduler. The writer processes
one candidate topic per cycle.

Skip for:
- Topics already covered by an existing file (>= 80% semantic overlap)
- Topics whose weighted score falls below 7.0 (log FLAG or REJECT)
- Domains without an anchor file
- Topics whose sources are too weak to proceed (authority < 3.0 AND
  core match would still not reach 7.0 after accounting for it)
- An empty candidate queue (log to library.log and exit)

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, read template, pick candidate, read anchor, research, score all 4 dimensions, check similarity, write, log, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `governance/template-library.md` Checklist: all items confirmed PASS (PASS / HALT)
- [ ] Logbook entry written to library.log (PASS / HALT)
- [ ] Errors logged to errors.log (if any) (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-writer && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-writer
```

### 2. Read the format specification

Read `governance/template-library.md`. It defines the body structure
(mandatory sections in order), frontmatter schema (7 fields + 2 optional
auditor fields), quality gates (G1-G12), anti-patterns, and the complete
example. Follow it exactly. Do not substitute your own section order or
naming -- the template is the single source of format truth.

### 3. Pick a candidate topic from the discovery queue

Read `/tmp/brain-writer/library/candidate-queue.md`. Select the
highest-scored unaudited candidate (by discoverer score). Note the
candidate ID, title, domain, and proposed scope.

### 3a. Remove the candidate from the queue

Remove the selected candidate entry from
`/tmp/brain-writer/library/candidate-queue.md`.

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

### 6. Score the candidate (4 dimensions, v2 weights)

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

### 7b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 8. Write the topic file

Write ONLY to the agentic-brain. NEVER write topic files to the
workspace. Follow the body structure and section order specified in
`governance/template-library.md` exactly.

Path: `/tmp/brain-writer/library/<domain>/<topic-slug>.md`

`<topic-slug>`: lowercase kebab-case, max 80 chars, unique within the
domain. Derive from the topic title.

### 9. Verify cross-references

Before writing the logbook entry, verify every cross-referenced file
actually exists in the brain clone. Hallucinated references to deleted
or assumed files produce broken links that fail G5.

```bash
# Extract paths from the topic's links: frontmatter and See Also,
# then verify each exists
for f in <path1> <path2>; do
  ls /tmp/brain-writer/$f || { echo "MISSING: $f -- remove from topic"; exit 1; }
done
```

If any path fails, remove it from both `links:` frontmatter and
`## See Also` before committing.

### 10. Write logbook entry

Append to `/tmp/brain-writer/logbook/library.log`. The logbook entry
MUST follow this exact format. Each data field MUST be on its own line.
Do NOT pack multiple fields onto a single line. The archiving system
counts lines, not bytes -- single-line entries defeat line-based
archiving.

```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | <agent-name> | library | ref: library/<domain>/<topic-slug>.md | see: <candidate-id>
Wrote topic <title> to <domain>. Weighted score: X.X/10.0
(core=X.X, scope=X.X, value=X.X, authority=X.X).
Similarity overlap: X%. Sources: N (N high, N medium, N low).
Cross-references: N topics.
```

Increment ENT counter from the last entry in library.log.

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

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to a section of
`governance/template-library.md`. HALT on any failure; fix before
committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug. Unique within the domain. (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "library-topic" (PASS / HALT)
- [ ] domain: `<domain-slug>` matching the folder name. Must match one of the 28 domain anchors exactly. (PASS / HALT)
- [ ] author: agent name, capitalized (e.g. Ava, Link, Researcher-1) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, domain-specific. At least 3 tags. (PASS / HALT)
- [ ] links: relative paths from brain root to related library topics or brain artifacts. At least 1 link. (PASS / HALT)
- [ ] audited + audit-score fields OMITTED (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Title is a level-1 heading making a claim about the topic (G1). Something a reader can agree or disagree with. (PASS / HALT)
- [ ] Opening paragraph summarizes the topic in 2-3 sentences. A reader with no domain knowledge understands what this topic is and why it matters. (G2) (PASS / HALT)
- [ ] `## Background` section present and contains substantive content (not a one-liner) (PASS / HALT)
- [ ] `## Core Concepts` section present and contains the essential ideas. Title MAY vary by domain (e.g. `## Core Biases by Category`, `## Core Principles`) but the section MUST exist. Contains substantive content -- at least 600 words. (G12) (PASS / HALT)
- [ ] `## Evidence` section present with empirical support, research findings, or case studies. Title MAY vary (e.g. `## Evidence and Research Foundation`) but MUST exist. Contains substantive content -- at least 400 words. (G12) (PASS / HALT)
- [ ] `## Implications` section present -- why the topic matters, practical application. Contains substantive content -- at least 400 words. (PASS / HALT)
- [ ] Domain-specific body sections (if any) positioned correctly: between Core Concepts and Evidence. Each must contain substantive, domain-relevant content. (PASS / HALT)
- [ ] Optional supplementary sections (if any: Common Pitfalls, Criticism, Practical Frameworks, etc.) positioned correctly between Implications and Sources. Each must contain substantive content. (PASS / HALT)
- [ ] `## Sources` section present with 3+ sources, each annotated with authority rating (high/medium/low) (G4) (PASS / HALT)
- [ ] `## See Also` section present with 1+ cross-reference to a related library topic or brain artifact (G5) (PASS / HALT)
- [ ] Section order enforced: Background -> Core Concepts -> (domain sections) -> Evidence -> Implications -> (optional) -> Sources -> See Also (G11) (PASS / HALT)
- [ ] No content follows `## See Also` (G11) (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Title Makes a Claim): PASS. Level-1 heading is something a reader can agree or disagree with. Not a label. (PASS / HALT)
- [ ] G2 (Opening Paragraph Self-Contained): PASS. Reader with no domain knowledge understands the topic and why it matters from the opening alone. (PASS / HALT)
- [ ] G3 (Every Claim Sourced): PASS. Every factual claim traces to a source in Sources. Synthesized claims labeled as such. No orphan facts. (PASS / HALT)
- [ ] G4 (Sources Have Authority Ratings): PASS. Every source has [high], [medium], or [low]. At least 2 of 3+ sources are high or medium. (PASS / HALT)
- [ ] G5 (Cross-references Exist): PASS. At least 1 link to a related library topic or brain artifact. (PASS / HALT)
- [ ] G6 (Domain Anchor Compliant): PASS. Topic stays within the domain anchor's In scope and avoids Out scope. Verified by reading anchor-<domain>.md. (PASS / HALT)
- [ ] G7 (Topic Similarity Checked): PASS. Candidate checked against existing topics. Overlap < 80%. Estimate recorded. (PASS / HALT)
- [ ] G8 (Frontmatter Complete): PASS. All 7 required fields present (name, id, tier, domain, author, tags, links). id from date command, not human-rounded. (PASS / HALT)
- [ ] G9 (Formatting Rules): PASS. ASCII-only (zero non-ASCII characters), lowercase slugs/tags, hyphens not underscores. (PASS / HALT)
- [ ] G10 (Output Destination Correct): PASS. File written ONLY to library/<domain>/<topic-slug>.md. NOT the workspace. (PASS / HALT)
- [ ] G11 (Section Order): PASS. Mandatory sections present and in correct sequence. No content after See Also. (PASS / HALT)
- [ ] G12 (Mandatory Section Quality): PASS. Each mandatory section (Background, Core Concepts, Evidence, Implications) contains substantive content. Core Concepts >= 600 words; Evidence >= 400 words; Implications >= 400 words. Verified by word count on extracted section text. Not a single sentence, not a placeholder. (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug, matching topic title. Max 80 chars, unique within domain. (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-writer/library/<domain>/ (NOT workspace, NOT any other path) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G9) (PASS / HALT)
- [ ] Candidate removed from candidate-queue.md (PASS / HALT)
- [ ] Logbook entry format: each data field (score, similarity, sources, cross-references) on its own line, matching the step 10 example exactly (PASS / HALT)

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

## Related

- `governance/template-library.md` -- full format specification, mandatory body sections, quality gates G1-G12, anti-patterns, complete example
- `governance/library-auditor.md` -- auditor skill (reviews written topics)
- `governance/library-discoverer.md` -- discoverer skill (proposes candidates)
- `library/guide-library.md` -- pipeline architecture, v2 weights, anchor format
- `research/insights/library-system.md` -- full system blueprint, scoring rationale
- `logbook/protocol.md` -- logbook entry format
