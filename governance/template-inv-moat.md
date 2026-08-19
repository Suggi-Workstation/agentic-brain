---
name: template-inv-moat
id: 20260819T171739Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Neo
links:
  - investing/frameworks/simple-moat-scoring.md
  - library/value-investing/economic-moats.md
---

# Investment Template -- Moat Scoreboard

The output format for a competitive advantage assessment. Produces
a quantitative baseline (ROIC-WACC), six moat source scores, Porter's
Five Forces, a 4-dimension composite score, and a trend verdict.
The methodology lives in `investing/frameworks/simple-moat-scoring.md`;
this template defines what the completed analysis looks like.

## What This Template Is

A scoreboard for competitive durability. Every score needs a cited
data point. A score without evidence is an opinion, not an assessment.

## Global Formatting Rules

Same as all brain files: 7-bit ASCII, lowercase, hyphen-delimited.

## Compliance Checklist -- HARD GATE

Pre-commit gate. Every item MUST be confirmed.

- [ ] Ticker and company name stated  (PASS / HALT)
- [ ] ROIC calculated (5-year average, source cited)  (PASS / HALT)
- [ ] WACC stated (source: DCF template or CAPM derivation)  (PASS / HALT)
- [ ] ROIC-WACC spread computed and classified  (PASS / HALT)
- [ ] Gross margin stability (CV) calculated  (PASS / HALT)
- [ ] Spread trend: widening / stable / narrowing  (PASS / HALT)
- [ ] Quantitative gate decision: proceed or auto-score 1.0  (PASS / HALT)
- [ ] All 6 moat sources assessed (present/absent + evidence)  (PASS / HALT)
- [ ] Porter's Five Forces: all 5 forces scored  (PASS / HALT)
- [ ] 4 scoring dimensions: each 1-5 with cited evidence  (PASS / HALT)
- [ ] Composite score calculated (weighted sum)  (PASS / HALT)
- [ ] Moat classification: wide / narrow / weak / none  (PASS / HALT)
- [ ] Required MOS derived from moat score  (PASS / HALT)
- [ ] Pipeline verdict: PASS / WATCHLIST / DISCARD  (PASS / HALT)
- [ ] Every score of 4+ has at least one primary source  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <ticker>-moat
id: <YYYYMMDDTHHMMSSZ>
tier: investment-moat
author: Neo
tags: [moat, competitive-advantage, <ticker>]
links:
  - investing/frameworks/simple-moat-scoring.md
  - investing/companies/<ticker>.md
---
```

## Scoreboard

### Header

```
Company:    <name>
Ticker:     <ticker>
Sector:     <sector>
```

### Quantitative Baseline

```
ROIC (5yr avg):     <X>%  (source: <filing years>)
WACC:               <X>%  (source: <DCF template or CAPM>)
ROIC-WACC spread:   <X>%  (classification: <strong/moderate/weak/none>)
Gross margin CV:    <X>%  (5yr, source: <filings>)
Spread trend:       <widening / stable / narrowing>
```

Quantitative gate: <PROCEED to qualitative / AUTO-SCORE 1.0 -- no
quantitative moat evidence>

### Moat Source Assessment

For each source: present or absent, which mechanism, evidence.

| Source | Present? | Mechanism | Key Evidence |
|:--|:--|:--|:--|
| Switching costs | Y/N | <how it works> | <data point + source> |
| Network effects | Y/N | <how it works> | <data point + source> |
| Intangible assets | Y/N | <how it works> | <data point + source> |
| Cost advantage | Y/N | <how it works> | <data point + source> |
| Efficient scale | Y/N | <how it works> | <data point + source> |
| Scale economies shared | Y/N | <how it works> | <data point + source> |

Multi-source reinforcement: <Y/N -- which sources reinforce each other>

### Porter's Five Forces

| Force | Strength (1-5) | Key Evidence |
|:--|:--|:--|
| Threat of new entrants | X | <barriers, evidence> |
| Bargaining power of suppliers | X | <concentration, evidence> |
| Bargaining power of buyers | X | <concentration, evidence> |
| Threat of substitutes | X | <alternatives, evidence> |
| Competitive rivalry | X | <landscape, evidence> |

Porter composite: <X.X> (average of 5 forces, inverted: 5 = weak
competitive pressure = strong moat)

### 4-Dimension Scoring

| Dimension | Weight | Score (1-5) | Evidence Summary |
|:--|:--|:--|:--|
| Source clarity | 20% | X | <which sources, how documented> |
| Moat width | 30% | X | <ROIC-WACC spread, durability> |
| Threat horizon | 25% | X | <nearest credible threat + timeline> |
| Moat trend | 25% | X | <widening/stable/narrowing + evidence> |

### Composite Score

```
Moat Score = (Source Clarity * 0.20) + (Moat Width * 0.30)
           + (Threat Horizon * 0.25) + (Moat Trend * 0.25)
         = <X.X>
```

| Composite Score | Classification | Verdict |
|:--|:--|:--|
| 4.0 - 5.0 | Wide moat | PASS (strong conviction) |
| 3.0 - 3.9 | Narrow moat | PASS |
| 2.0 - 2.9 | Weak / narrowing | WATCHLIST |
| 1.0 - 1.9 | No moat | DISCARD |

### Margin of Safety Link

```
Moat score:     <X.X>
Required MOS:   <X>%  (wide >= 20%, narrow >= 30%, weak >= 40%)
```

### Verdict

```
MOAT SCORE: <X.X>
CLASSIFICATION: <Wide / Narrow / Weak / None>
PIPELINE VERDICT: <PASS / WATCHLIST / DISCARD>
REQUIRED MOS: <X>%

Key risk to moat: <single most credible threat + timeline>
```

---

*Last updated: 2026-08-19 by Neo. Scoreboard format; methodology in the framework file.*