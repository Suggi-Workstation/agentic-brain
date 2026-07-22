---
name: library-discoverer-test
id: 20260722T184716Z
tier: proposal
author: Link
tags: [library, discoverer, test, pipeline, expected-results]
links: [governance/library-discoverer.md, library/guide-library.md, research/insights/library-system.md]
---

# Library Discoverer Test -- Expected Results

## Purpose

This proposal defines the expected outputs when Researcher-1 runs the
`library-discoverer` skill for the first time. All 28 domains have 0
topics. The discoverer must survey domains, select 4-6 across major
categories, read anchors, identify knowledge gaps, score candidates,
and append proposals to `library/candidate-queue.md`.

This document is the acceptance criteria. After the test run, compare
actual outputs against these expectations. Deviations must be explained
or fixed.

## Expected Outputs

### 1. library.log entry

A single entry in `logbook/library.log` with format:
```
## [ENT-NNN] | YYYY-MM-DD HH:MM UTC | Researcher-1 | library | ref: library/candidate-queue.md
Discovery cycle: N domains scanned, M candidates proposed.
Domains: <list with topic counts>. Candidates: <list with all 4 dimension scores>.
Domain balance survey: <least-covered domain (0 topics)> to <most-covered (0 topics)>.
```

Acceptance criteria:
- ENT counter increments from last library.log entry (currently ENT-001)
- N = 4-6 (the number of domains selected for this cycle)
- M = 4-18 (each domain yields 1-3 candidates; 4 domains x 1 = 4 minimum, 6 x 3 = 18 maximum)
- All domains listed with topic count = 0 (no topics exist yet)
- Each candidate includes all 4 dimension scores (gap, compounding, timeliness, balance)
- Domain balance survey shows 0 topics for all domains (all equally underrepresented)

### 2. candidate-queue.md

File at `library/candidate-queue.md` contains M candidate entries. Each entry:
```markdown
## Candidate: <topic-title>
- **Domain:** <domain-slug>
- **Proposed by:** Researcher-1
- **Date:** 2026-07-22
- **Discovery score:** X.X/10.0 (gap=X.X, compounding=X.X, timeliness=X.X, balance=X.X)
- **Scope:** <2-3 sentence scope description for the writer>
- **Status:** proposed
```

Acceptance criteria:
- File retains its header: `# Library Candidate Queue -- topics proposed for the writing process`
- M candidates appended (not overwritten)
- No duplicate candidates (checked by title and scope)
- Each candidate's domain has an anchor file
- Domain balance scores reflect the survey: all domains at 0 topics -> all balance scores are 10.0
- No candidate proposes a topic outside its domain's In scope
- ASCII-only

### 3. errors.log (expected: no entry)

Acceptance criteria:
- No new entry in `logbook/errors.log`
- If an entry IS written, it MUST describe an unexpected failure (clone failed, push rejected, file write error). Normal pipeline outcomes go to library.log only.

### 4. No other files modified

Acceptance criteria:
- No topic files created (discoverer proposes, does not write)
- No anchor files modified
- No governance files modified
- No index regeneration (that is the auditor's job)

## Domain Selection Expectations

With all 28 domains at 0 topics, the discoverer must:
1. Prioritize domain balance (all equal at 0)
2. Cover at least one domain from each major category:
   - **investing:** value-investing, finance, valuation-screening, portfolio-risk-management, accounting-financial-shenanigans, macro-micro, industries-sectors
   - **science:** science, earth-climate, mathematics-statistics, technology
   - **human/social:** psychology-behavior, anthropology, health-medicine, education-learning, communication, ethics-philosophy, history, law-regulation, self-improvement
   - **global:** geopolitics
   - **thinking:** probabilistic-thinking-forecasting
   Plus: books, case-studies, coding-agentic-ai, investors, notable-people, pop-culture

3. Select 4-6 domains total, rotating across categories

Acceptance criteria:
- At least 4 categories represented across the selected domains

## Scoring Expectations

All domains have 0 topics -> domain balance = 10.0 for every candidate.
Other dimensions (gap, compounding, timeliness) vary by candidate.

Acceptance criteria:
- Every candidate has all 4 dimensions scored
- Every dimension has a brief justification (1-2 sentences)
- Weighted score formula correct: (gap*0.40 + compounding*0.25 + timeliness*0.20 + balance*0.15)
- Domain balance derived from the topic count survey, not hardcoded

## Open Questions

1. Will the discoverer select exactly 4-6 domains or pick all 28? The skill says "4-6 per cycle" but with 0 topics everywhere, the temptation to over-select is real.
2. Will gap scores be inflated? With no existing topics, every proposed topic is a "gap" -- but some gaps are larger than others. The discoverer must distinguish critical gaps from nice-to-haves.
3. Will the balance survey for-loop work correctly in the cron environment? The skill uses bash `for domain in library/*/; do` -- this depends on the shell and the clone being at the expected path.
4. Will the queue format match exactly? The skill shows a markdown template. If the discoverer deviates (adds extra fields, changes indentation), the writer may not parse the candidate correctly.

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1.0 | 2026-07-22 | Link | Initial test specification |
