---
name: template-library
id: 20260618T120015Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Suggi
links: []
---

# Library Topic Template -- How We Write Knowledge Files

A library topic is an independent, agent-authored research file: a
self-contained essay on one concept, person, company, book, framework,
or event. One atomic idea, explained clearly, with its own hypothesis
and conclusion.

## Global Formatting Rules

The entire GitHub org is plain 7-bit ASCII, lowercase, hyphen-delimited.
These rules are non-negotiable. CI enforces them.

- **ASCII-only:** Every character in every file is 7-bit ASCII (U+0000
  through U+007F). No emoji, no smart quotes, no Unicode dashes or
  arrows, no accented letters. The `ascii-guard.yml` CI gate fails the
  build on any violation.
- **Lowercase only:** All filenames, slugs, tags, domains, and folder
  names use lowercase exclusively. No CamelCase, no UPPERCASE, no
  mixed case.
- **Hyphens, not underscores:** Use hyphens (`-`) to separate words in
  filenames, slugs, and tags. Never use underscores (`_`).
  Correct: `margin-of-safety.md`. Wrong: `margin_of_safety.md`.

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. Use the exact second of creation -- do not pad with 00.
tier: library                     # always library
domain: <domain-slug>            # lowercase, matches folder name
author: <link|ava|zelda|suggi|luffy>  # who wrote this topic
tags: [<tag>, <tag>]             # lowercase, 3-6 tags. Include type as a tag
                                 # (concept, person, company, book, framework,
                                 #  event, culture) plus topic tags
links: [<relative-brain-path>]   # paths relative to agentic-brain root
---
```

## Naming Convention

Files are named: `<domain>/<slug>.md`

- `domain` -- lowercase folder name
- `slug` -- kebab-case, max 60 chars, unique within the domain

Example: `value-investing/margin-of-safety.md`

## Frontmatter Rules:
- `name` is a short lowercase kebab-case slug unique within the domain.
  Example: `margin-of-safety`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. Use the exact second of creation -- do not pad with 00.
- `tier` is always `library`.
- `domain` is the lowercase folder name (e.g., `value-investing`).
- `author` is who wrote the topic. The author list is {link, ava, zelda,
  suggi, luffy}. Suggi is the human; others are agents.
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry. Include the file's type as a tag
  (concept, person, company, book, framework, event, culture).
- `links` are relative paths from the agentic-brain root. Do not use
  absolute paths or file:// URIs.

## Body Structure

Three parts. Percentages are guidelines, not rules. Let the content
dictate the shape.

### Hypothesis (roughly 10-15%)

State the core claim in one to three sentences. Then provide the framing:
why this topic matters and what question it answers.

Good: "Munger's inversion technique is not just a thinking tool -- it is
a structural risk-management discipline that forces you to identify
failure modes before they occur."

Weak: "This file is about Charlie Munger's inversion technique."

### Body (roughly 70-80%)

Split into two parts, chosen by the author:

**Analytical (roughly 30-40%):** Quantitative, structured, or systematic
content. Data tables, formulas, frameworks, criteria checklists,
comparative analysis, timelines, or model components. Verifiable or
falsifiable by another agent.

**Narrative / Free Text (roughly 30-40%):** Qualitative explanation,
historical context, illustrative examples, quotes from primary sources,
analogies, or synthesis. The agent's voice and judgment.

The order is up to the author. The split is a guideline -- some topics
are 80% narrative with one analytical table; that is fine.

### Conclusion (roughly 10%)

Three elements:
1. Restate the hypothesis in light of what was presented.
2. One actionable takeaway: what changes after reading this?
3. Open questions or SPAWN entries: what is still unknown?

## Cross-Links

End with an explicit cross-links section. Include:
- Related topics in the same domain.
- Topics in other domains that connect.
- Reflections or reports that reference this topic.
- Any external source cited (with URL + retrieval date).

Cross-links are the connective tissue of the brain. Zero links = dead end.

## Quality Gates

Every library topic passes these checks before committing:

- **G1 -- Atomic:** One concept per file. If the topic sprawls, split it.
  The test: can you state the entire topic in one sentence without
  "and" connecting unrelated ideas?
- **G2 -- Feynman Test:** A reader new to the domain can follow it from
  start to finish without needing external context.
- **G3 -- Hypothesis Makes a Claim:** The hypothesis states a position
  someone could disagree with, not a description of what the file
  contains.
- **G4 -- Sourced:** Every factual claim cites its origin. Primary
  sources, data, or an explicit "author's analysis" label. No
  unattributed assertions.
- **G5 -- Cross-links Exist:** At least 2 links to other brain content
  (library topics, reflections, insights, or reports). Zero links =
  dead-end knowledge.
- **G6 -- Frontmatter Complete:** All 7 fields present (name, id,
  tier, author, domain, tags, links). Name is unique within the
  domain. Type is included as a tag.
- **G7 -- Formatting Rules:** ASCII-only (zero non-ASCII characters),
  lowercase slugs and tags, hyphens not underscores. CI enforces
  ASCII via `ascii-guard.yml`.

## Example -- Minimal Valid Library Topic

```markdown
---
name: margin-of-safety
id: 20260716T120000Z
tier: library
domain: value-investing
author: Ava
tags: [concept, margin-of-safety, risk-management, graham]
links: [library/investors/benjamin-graham.md, library/valuation-screening/intrinsic-value.md]
---

# Margin of Safety -- Why Price Must Lag Value

## Hypothesis
The margin of safety is not a valuation metric -- it is a risk-management
discipline. Graham's original formulation demands a discount to intrinsic
value sufficient to absorb estimation error, not just market volatility.
The margin is insurance against being wrong, not against the market being
wrong.

## Analytical Framework

### Graham's Original Criteria (The Intelligent Investor, 1949)
| Criterion | Threshold | Purpose |
|---|---|---|
| Price / Book | Below 0.67 | Asset-backing floor |
| Current Ratio | Above 2.0 | Liquidity buffer |
| Earnings Yield | 2x AAA bond yield | Return premium |
| Debt / Equity | Below 1.0 | Leverage constraint |

### Quantifying the Margin
Margin of Safety (%) = (Intrinsic Value - Market Price) / Intrinsic Value
- Minimum acceptable: 33% (Graham)
- Buffett adjusted: 25-50% depending on business quality
- During 2008-09 crisis: 60%+ margins available on quality names

## Historical Context

Graham developed the margin concept after losing nearly everything in the
1929 crash. The margin of safety was not a theoretical construct -- it was
scar tissue. His core insight: intrinsic value is an estimate, and
estimates are wrong. The margin absorbs the error.

Buffett evolved the concept from quantitative-only (Graham's net-net
approach) to qualitative-adjusted. A wonderful business at a fair price
may require a smaller margin than a fair business at a wonderful price,
because the wonderful business's intrinsic value grows over time, closing
any initial gap.

## Conclusion

The margin of safety is the bridge between valuation and risk management.
It answers: "What if I am wrong about my estimate?" not "What if the
market disagrees with me?" The margin protects against the first kind of
error. Patience protects against the second.

**Actionable takeaway:** Never buy without calculating the margin. If the
margin is below 25%, the investment thesis must explain why business
quality compensates for estimation risk.

**Open questions:**
- How does margin of safety interact with portfolio concentration?
- Does the margin requirement change with holding period?

## Cross-Links
- `library/investors/benjamin-graham.md` -- Graham's biography and full
  investment philosophy
- `library/valuation-screening/intrinsic-value.md` -- DCF and EPV methods
- `library/value-investing/mr-market.md` -- Graham's allegory on market
  psychology vs. intrinsic value

## References
- Graham, B. (1949). The Intelligent Investor. Chapter 20.
- Buffett, W. (1992). Berkshire Hathaway Annual Letter.
- Retrieved: 2026-07-16.
```


## The Library Checklist

Pre-commit gate: every item below MUST be confirmed. The file
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file.

```
[ ] Frontmatter Schema complete (7 fields: name, id, tier, domain, author, tags, links)
[ ] Frontmatter Rules correctly applied (7 fields: name, id, tier, domain, author, tags, links)
[ ] id is UTC timestamp with exact second, never used before
[ ] Domain matches the folder the file lives in
[ ] Tags include the file's type (concept, person, company, book, etc.)
[ ] Hypothesis makes a claim (not a description)
[ ] Analytical section: at least one structured element (table, formula, criteria, framework)
[ ] Narrative section: qualitative explanation with examples or quotes
[ ] Conclusion: restates hypothesis + one actionable takeaway + open questions
[ ] Cross-links: at least 2 links to other brain content (library/reflections/insights/reports)
[ ] Source citations: every factual claim traces to a primary source, data, or "author's analysis"
[ ] Feynman test: a domain newcomer can follow from start to finish
[ ] Filename: <domain>/<slug>.md -- lowercase, kebab-case
[ ] ASCII-only: zero non-ASCII characters in the file
```

---

*Last updated: 2026-07-16 by Suggi. Rules are scar tissue -- each
one should trace to a failure that proved it necessary.*
