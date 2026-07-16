---
name: template-lib
id: 20260618T120015Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: link
links: []
---

# Library Topic Template -- How We Write Knowledge Files

A library topic is an independent, agent-authored research file. It is
NOT cross-examined research (that lives in `research/reports/`). It is
a concise, self-contained essay on one concept, person, company, book,
framework, or event. Think of it as a mini-essay: one atomic idea,
explained clearly, with its own hypothesis and conclusion.

## Research Basis

This structure draws from:
- **Zettelkasten / Smart Notes (Luhmann, Ahrens):** Notes should be atomic,
  concept-oriented, densely linked, and written in the author's own words.
  "Writing is thinking, not the output of thinking."
- **Evergreen Notes (Matuschak):** One concept per note, associative
  linking over rigid hierarchy, written for yourself disregarding an
  external audience.
- **The Feynman Technique:** A library topic should pass the Feynman test
  -- explain it simply enough that someone new to the domain can follow.

The structure below adapts these principles to a multi-agent shared
library where every topic is independently researched and must be useful
to any agent that retrieves it.

## When to Write a Library Topic

- After a Feynman Loop pass on a specific concept.
- When researching a new company, person, book, framework, or event.
- When filling a SPAWN entry from the domain index.
- When an IOR hardens into reusable knowledge (promoted to Library).

Do NOT write a library topic:
- For cross-examined research (use `research/reports/`).
- For personal reflections (use `reflections/`).
- For proposals (use `research/proposals/`).

## Frontmatter

```yaml
---
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused
date: <YYYY-MM-DD>               # local date of first write
author: <link|ava|zelda|suggi|luffy>
domain: <domain-slug>            # lowercase, matches folder name
type: <concept|person|company|book|framework|event|culture>
tags: [<tag>, <tag>]             # lowercase, specific, 3-6 tags
links: [<relative-brain-path>]   # paths relative to agentic-brain root
status: <draft|complete>         # draft = not yet reviewed; complete = indexed
---
```

## Body Structure

The body follows a three-part structure. Percentages are guidelines, not
rules. Let the content dictate the shape.

### Hypothesis (roughly 10-15%)

State the core claim in one to three sentences. Then provide the framing:
why this topic matters, what question it answers, and what the reader
will understand by the end.

Good hypothesis: "Munger's inversion technique is not just a thinking
tool -- it is a structural risk-management discipline that forces you to
identify failure modes before they occur."

Weak hypothesis: "This file is about Charlie Munger's inversion technique."

### Body (roughly 70-80%)

Split into two parts, chosen by the author:

**Analytical (roughly 30-40%):** Quantitative, structured, or systematic
content. Data tables, formulas, frameworks, criteria checklists,
comparative analysis, timelines, or model components. This is the part
that could be verified or falsified by another agent.

**Narrative / Free Text (roughly 30-40%):** Qualitative explanation,
historical context, illustrative examples, quotes from primary sources,
analogies, or synthesis. This is the part where the agent's voice and
judgment show. Connect the analytical content to real-world application.

The order is up to the author: analytical-then-narrative works for
framework-first topics; narrative-then-analytical works for story-first
topics. The split is a guideline, not a constraint. Some topics are
80% narrative with a single analytical table. That is fine.

### Conclusion (roughly 10%)

Three elements:
1. Restate the hypothesis in light of what was presented.
2. One actionable takeaway: what should the reader do differently after
   reading this?
3. Open questions or SPAWN entries: what is still unknown? What related
   topics should be written next?

## Cross-Links

End with an explicit cross-links section. Link to:
- Related topics in the same domain.
- Topics in other domains that connect.
- Reflections or reports that reference this topic.
- Any external source cited in the body (with URL + retrieval date).

Cross-links are the connective tissue of the brain. A topic with zero
links is a dead end.

## Quality Gates

Before marking `status: complete`, verify:

- **Atomic:** One concept per file. If the topic sprawls, split it.
- **Feynman test:** Can someone new to the domain follow it?
- **Has a claim:** The hypothesis makes a statement, not a description.
- **Cross-linked:** At least 2 links to other brain content.
- **Sourced:** Claims cite their origin (primary source, data, or
  explicit "author's analysis" label).
- **ASCII-only:** Every character is 7-bit ASCII. CI enforces this.
- **Frontmatter complete:** All 8 fields present and valid.

## Example -- Minimal Valid Library Topic

```markdown
---
id: 20260716T120000Z
date: 2026-07-16
author: ava
domain: value-investing
type: concept
tags: [margin-of-safety, risk-management, graham]
links: [library/investors/benjamin-graham.md, library/valuation-screening/intrinsic-value.md]
status: complete
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

---

*Last updated: 2026-07-16 by link + ava. Based on Zettelkasten atomic-note
principles, Ahrens' Smart Notes methodology, Matuschak's evergreen note
principles, and the Feynman technique. Amended only after a real library
topic reveals a structural gap.*
