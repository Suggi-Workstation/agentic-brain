---
name: write-evaluation
description: "Write an evaluation: Source-Criteria-Findings-Verdict format with quality gates G1-G8, decorrelation rule, and cross-links. Use when asked to evaluate, review, scrutinize, or perform independent review of an agent's work."
user-invocable: true
disable-model-invocation: false
---

# Evaluation Writing

## What This Skill Does

Guides writing an independent evaluation to the agentic-brain. Procedure
steps cover the mechanics (clone, write, commit, discard). Format
verification checkboxes cover correctness (frontmatter, body structure,
quality gates, output). For the full format specification with examples,
read `brain:governance/template-evaluations.md`.

## When to Invoke

Invoke when the task involves evaluating another agent's work: a
proposal, report, or insight needs independent scrutiny. The
decorrelation rule requires a different agent (or model family) than
the original author.

Skip for:
- Your own work (violates G1 decorrelation)
- Work already evaluated with APPROVE verdict
- Minor formatting fixes

## Final Self-Check -- HARD GATE

Confirm ALL verification sections passed before committing.

- [ ] Procedure completed (clone, write, verify, commit, push, discard) (PASS / HALT)
- [ ] Frontmatter Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Body Structure Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Quality Gates Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] Version History Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] File Output Sub-Checklist verification: all items confirmed PASS (PASS / HALT)
- [ ] `template-evaluations.md` Checklist: all items confirmed PASS (PASS / HALT)
- [ ] Committed and pushed: changes pushed to origin main (PASS / HALT)
- [ ] Discarded clone: temporary directory removed from /tmp/ (PASS / HALT)

## Procedure

### 1. Determine if an evaluation is warranted

An evaluation is warranted when another agent has produced a proposal,
report, or insight that requires independent review. Confirm the
decorrelation rule (G1): you are NOT the original author.

### 2. Clone the agentic-brain

```bash
cd /tmp && rm -rf brain-eval && git clone --depth 1 \
  "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/agentic-brain.git" brain-eval
```

### 3. Read the format specification

Read `brain:governance/template-evaluations.md`. It defines the
Source-Criteria-Findings-Verdict format, frontmatter schema (7 fields
including source), quality gates (G1-G8), and examples. Follow it
exactly.

### 3b. Generate the ID

Run `date -u +'%Y%m%dT%H%M%SZ'` and capture the output:

```bash
date -u +'%Y%m%dT%H%M%SZ'
```

Paste the exact output into the `id:` field in the frontmatter.
Never type the ID digits by hand. The exec output is authoritative.

### 4. Write the evaluation file

Write ONLY to the agentic-brain. NEVER write evaluations to the
workspace.

Path: `/tmp/brain-eval/research/evaluations/<short-slug>.md`

`<short-slug>`: kebab-case, max 60 chars, unique.
Example: `ava-review-link-verification-paper.md`

## Sub-Checklists -- HARD GATE (before commit)

Verify every Sub-Checklist item below. Each maps to the template. HALT on any failure;
fix before committing.

### Frontmatter Sub-Checklist

- [ ] name: lowercase kebab-case, matches filename slug (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly. Does not end in 000000Z (human-rounded = reject). Never manually typed. (PASS / HALT)
- [ ] tier: "evaluation" (PASS / HALT)
- [ ] source: exact id of the work being evaluated (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor) (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited (PASS / HALT)
- [ ] links: relative paths from brain root (PASS / HALT)

### Body Structure Sub-Checklist

- [ ] Source section: cited by exact id, scope stated (PASS / HALT)
- [ ] Evaluation Criteria: listed before findings begin (G2) (PASS / HALT)
- [ ] Findings: every finding backed by specific reference (quote/cite/link) (G3) (PASS / HALT)
- [ ] Verdict: one of APPROVE / APPROVE WITH CHANGES / REJECT (G4) (PASS / HALT)
- [ ] Required changes listed concretely (if APPROVE WITH CHANGES) (PASS / HALT)
- [ ] Confidence: stated with reasoning, high/medium/low (G5) (PASS / HALT)

### Quality Gates Sub-Checklist

- [ ] G1 (Different Agent): author != source author. Decorrelation rule must PASS (PASS / HALT)
- [ ] G2 (Criteria Stated First): evaluation criteria are listed before findings begin (PASS / HALT)
- [ ] G3 (Evidence Cited): every finding is backed by a specific reference. Quote the source, cite the line, link the file. No unsupported assertions about someone else's work (PASS / HALT)
- [ ] G4 (Verdict Is Explicit): one of three options: APPROVE, APPROVE WITH CHANGES or REJECT. No "maybe" or "mostly good" (PASS / HALT)
- [ ] G5 (Confidence Included): with reasoning. High (85%+), medium (60-85%), or low (below 60%). State what would change the confidence level (PASS / HALT)
- [ ] G6 (Cross-links): source + related evaluations/governance files linked (PASS / HALT)
- [ ] G7 (Frontmatter Complete): all 7 fields present (name, id, tier, source, author, tags, links) (PASS / HALT)
- [ ] G8 (Formatting Rules): ASCII-only, lowercase slugs/tags, hyphens not underscores (PASS / HALT)

### Version History Sub-Checklist (ONLY if version-history table was added)

- [ ] Version-history table: present and correct (date + author + change rows) if file has version updates; omitted for single-version files (PASS / HALT)

### File Output Sub-Checklist

- [ ] File named: lowercase kebab-case slug (PASS / HALT)
- [ ] Written ONLY to /tmp/brain-eval/research/evaluations/ (NOT workspace) (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file (G8) (PASS / HALT)

### 5. Commit and push

```bash
cd /tmp/brain-eval
git add -A
git diff --cached --stat
git -c user.name="Ava" -c user.email="ava@suggi-workspace.dev" \
  commit -m "evaluation: <short-slug>"
git push origin main

If the push fails, pull first, resolve, then push.
```

### 6. Discard the clone

```bash
cd /tmp && rm -rf brain-eval
```

## Related

- `brain:governance/template-evaluations.md` -- full format, examples, quality gates
- `skills/write-proposal/SKILL.md` -- proposal writing (proposals are evaluated)
- `skills/write-report/SKILL.md` -- report writing (reports require evaluation)
