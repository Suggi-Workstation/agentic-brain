---
name: intrinsic-value-pipeline
id: 20260727T173500Z
tier: pipeline
author: Ava
tags: [value-investing, intrinsic-value, quality, screening, dcf, EPV, buffett, quarterly, patience]
links:
  - governance/suggi-investment-approach.md
  - investing/frameworks/dcf-intrinsic-value.md
  - investing/frameworks/sector-specific-metrics.md
  - investing/frameworks/simple-moat-scoring.md
  - investing/frameworks/simple-management-scoring.md
  - investing/frameworks/deep-moat-scoring.md
  - investing/frameworks/deep-financial-scoring.md
  - investing/pipeline/screener-intrinsic-value-pipeline.md
---

# Intrinsic Value Pipeline -- Value Good Companies, Wait for Price

## Core Principle

Find every good company in a region. Value each one. Maintain the
list. Wait.

When Mr. Market eventually offers a good company at a discount to
its intrinsic value, the work is already done. The intrinsic value
calculation sits ready. Suggi acts -- or does not act. Either way,
the calculation was not rushed by a price move. It was done calmly,
with quarterly-fresh data, long before any buy decision.

This is the opposite of screening for cheapness. Screening for
cheapness surfaces junk and value traps alongside bargains. Screening
for quality surfaces wonderful businesses. Most will be expensive
most of the time. That is fine. The list exists so that when one
becomes cheap, the intrinsic value number is already known.

Buffett: "I don't look at the price first. I look at the business.
If the business is wonderful, I figure out what it is worth. Then I
look at the price. If the price is right, I buy."

## What This Pipeline Does

1. Pull financial data for a target region.
2. Filter for quality: growth, returns on capital, financial health.
3. Filter for durability: moat, management quality.
4. Calculate intrinsic value for every company that passes all
   quality gates.
5. Maintain the list. Recalculate quarterly with new financial data.
6. Output: "Here are the good companies and what they are worth."

## What This Pipeline Does NOT Do

- Does not filter by cheapness. A wide-moat compounder trading at
  30x earnings belongs on the list. Suggi decides what price is
  acceptable.
- Does not calculate margin of safety. MOS depends on market price,
  and market price is Suggi's domain.
- Does not monitor prices. Intrinsic value changes quarterly with
  financial data. Between quarters, the number is stable.
- Does not recommend buys, sells, or position sizes. Suggi decides.

## The Pipeline

### Phase A: Quality Screening (Deterministic -- Python, No LLM)

#### Stage 0: Universe Definition

Define the investable universe. Maintained as `investing/universe.yaml`:

```yaml
universe:
  region: eu
  source: financial_modeling_prep
  exclude_sectors: []
  min_market_cap: 100M

circle_of_competence:
  understood: [software, consumer-staples, insurance-brokers,
               specialty-retail, industrials]
  avoid: [biotech-pre-revenue, chinese-vi, spacs, crypto-related,
          mining-exploration]
```

Companies in "avoid" sectors never enter the pipeline.

#### Stage 1: Data Ingestion and Quality Validation

Pull complete financial data for every company in the universe.

Per company: revenue (10 years), EBIT, FCF, ROIC, ROE, enterprise
value, market cap, total debt, debt/equity, debt/EBITDA, insider
ownership, sector classification.

Validate before ranking:
- Negative enterprise values: flag
- Missing fields: exclude from ranking, flag for investigation
- Stale data (>90 days since last filing): flag
- Extreme outliers (>5 SD from sector median): flag
- If >20% of fields missing across the universe: HALT

#### Stage 2: Quality Filter

The only pass-through gate. Cheapness plays no role here. If a
company is good, it proceeds. If not, it does not.

**Growth requirement:**
- Revenue CAGR >= 10% over 5-10 years (using sector-appropriate
  growth metric from the sector metrics framework)

**Returns requirement:**
- ROIC >= 15% and/or ROE >= 15% (using sector-appropriate quality
  metric, 5-year average)

**Financial health minimums:**
- Debt/EBITDA < 4x (or < 3x for cyclicals)
- Interest coverage > 3x
- No 3+ consecutive years of negative FCF

**Wonderful business heuristics (informational flags, not gates):**
- Revenue grew in 7+ of last 10 years?
- Gross margin stable or expanding over 5 years?
- ROIC >= cost of capital by 500+ bps over 5 years?

Companies failing the heuristics are not discarded -- they are
flagged. The flag tells the deep-dive agent: "this company passed
the quality thresholds but may not be wonderful. Investigate."

Companies passing the quality filter enter Phase B. Typically
100-300 companies from a 3,500-company universe. This is the
"good companies" candidate set.

#### Stage 3: Composite Ranking (Sorting, Not Filtering)

For Suggi's convenience, rank the surviving companies by the
25/25/50 composite:

- Growth: 25% (percentile rank on sector-appropriate growth metric)
- Quality: 25% (percentile rank on sector-appropriate quality metric)
- Cheapness: 50% (percentile rank on EV/EBIT or sector equivalent)

**Important: the composite rank is used ONLY for sorting the
list, not for excluding companies.** A company ranked #150 is
still in the pipeline if it passed Stage 2. The ranking tells
Suggi "start here" when he reviews the list -- the higher-ranked
companies are both good AND cheap, which is the sweet spot. But
the lower-ranked companies are still on the list because they
are good. When their price drops, they surface.

Sector-specific metrics as defined in:
`investing/frameworks/sector-specific-metrics.md`

Owner earnings normalization (Buffett) applied to cheapness:

```
Owner Earnings = Net Income + Depreciation - Avg Maintenance Capex
Cheapness Metric = EV / Owner Earnings (or sector equivalent)
```

### Phase B: Qualitative Gates (Agentic -- Decorrelated)

Every company that passed Phase A enters Phase B. No company is
skipped because of its composite rank. The rank only determines
processing order: top-ranked first.

#### Stage 4: Moat Scoring

See: `investing/frameworks/simple-moat-scoring.md`

Researcher-1 scores each company on 4 dimensions:
- Source Clarity (20%): which of 6 moat sources, with evidence
- Moat Width (30%): ROIC-WACC spread magnitude and persistence
- Threat Horizon (25%): years before moat could be breached
- Moat Trend (25%): widening, stable, or narrowing

Moat score >= 3.0: the company has at least a narrow moat. Proceed.
Moat score < 3.0: the company has no durable competitive advantage.
It may still be a good business, but without a moat, it cannot
sustain its returns. **The company stays on the list but is flagged
"no durable moat."** Suggi decides whether a company without a moat
warrants attention.

#### Stage 5: Management Scoring

See: `investing/frameworks/simple-management-scoring.md`

Researcher-2 scores each company on 5 dimensions:
- Insider Ownership (25%)
- Buyback Quality (20%)
- Acquisition Track Record (20%)
- Shareholder Communication (15%)
- Capital Allocation Discipline (20%)

Management score >= 3.0: owner-oriented stewards. Proceed.
Management score < 3.0: the company is flagged "management concerns."
Suggi decides.

#### Stage 6: Cheap-and-Good vs Cheap-Because-Bad Triage

Both researchers produce independent verdicts for each company:
- GOOD: business quality intact, durable competitive position,
  honest management. Deserves an intrinsic value calculation.
- WATCH: questions remain. Flagged for Suggi's attention but
  intrinsic value is still calculated (with caveats noted).
- BAD: structural decline, broken business model, fraudulent
  management. No intrinsic value calculation. Removed from list.

Structured debate protocol for disagreements: 2 rounds, escalate
unresolved disagreements to Suggi.

Output: a list of GOOD + WATCH companies that proceed to valuation.

### Phase C: Intrinsic Value Calculation (Agentic)

For every GOOD and WATCH company, calculate intrinsic value. No
company is skipped because it is "too expensive." Price is
irrelevant here.

#### Stage 7: Deep Dive (Parallel)

Two independent analyses run in parallel:

**7A. Moat & Competitive Dynamics (researcher-1)**

See: `investing/frameworks/deep-moat-scoring.md`

- Full moat durability assessment (6-source framework)
- Porter's Five Forces industry analysis
- Competitor benchmarking (top 3-5)
- 10+ year destination projection (Sleep/Zakaria)

**7B. Financial Health & Red Flags (researcher-2)**

See: `investing/frameworks/deep-financial-scoring.md`

- Normalized earnings (adjusting for one-time items, cycles)
- FCF conversion quality (5-year trend)
- Debt structure analysis (maturity ladder, leverage)
- ROIIC (return on incremental invested capital)
- Red flag scan (earnings quality, balance sheet, governance)

#### Stage 8: Conviction Check

Three questions before committing to a valuation:

1. **Destination question (Sleep):** Can I describe what this
   business looks like in 5-10 years with confidence?
2. **Fat pitch question (Pabrai):** Is this a no-brainer? Not
   "would I buy at this price" -- just "is this an obviously
   good business?"
3. **Munger inversion:** What is the single worst thing that
   could happen to this business, and how likely?

#### Stage 9: Intrinsic Value Calculation

See: `investing/frameworks/dcf-intrinsic-value.md`

**Market price is not used anywhere in this stage.**

**9A. Two-Stage DCF with Bull/Base/Bear Scenarios**

```
FCF = EBIT * (1 - Tax Rate) + Depreciation - CapEx - Change in WC
PV of Explicit Period = Sum of [FCF_YearN / (1 + WACC)^N] for N = 1 to 5
Terminal Value = FCF_Year5 * (1 + g) / (WACC - g)
Enterprise Value = PV of Explicit + PV of Terminal
Equity Value = EV - Total Debt + Cash
Intrinsic Value Per Share = Equity Value / Diluted Shares
```

Three scenarios:

| Parameter | Bear (-) | Base | Bull (+) |
|:--|:--|:--|:--|
| Revenue growth (Y1-3 avg) | Base - 2.0pp | Thesis-driven | Base + 1.5pp |
| Operating margin (terminal) | Base - 2.0pp | Normalized | Base + 1.5pp |
| WACC | Base + 1.5pp | CAPM + moat adj | Base - 1.0pp |
| Terminal growth rate | Base - 0.5pp | GDP-based | Base + 0.3pp |

Sector-appropriate methodology auto-selected:

| Sector | Methodology |
|:--|:--|
| Industrial/Consumer | 2-stage DCF |
| SaaS | Revenue-based DCF (churn/CAC/LTV) |
| REITs | FFO/AFFO multiple + NAV |
| Banks | Excess returns model (ROE - COE * BV) |
| Insurance | Combined ratio + float value |
| Energy/Materials | Cycle-normalized earnings + reserve valuation |

**9B. Earnings Power Value (EPV)**

No-growth floor. Cross-check against DCF:

```
EPV = Normalized EBIT * (1 - Tax Rate) / WACC
EPV per Share = (EPV - Net Debt) / Diluted Shares
```

DCF > 2x EPV: growth assumptions dominate. Flag for scrutiny.

**9C. Sensitivity Matrix**

WACC vs terminal growth rate grid (5x5). Shows IV range across
reasonable assumptions.

#### Stage 10: Investment Thesis

3-5 testable pillars per company:
- Specific: what will happen and why
- Falsifiable: what data point would disprove it
- Monitored: metric + update cadence

Variant perception: what do we believe that the market does not?

#### Stage 11: Quality Checklist

- [ ] Do I understand this business?
- [ ] Does it have a durable competitive advantage?
- [ ] Is management owner-oriented and honest?
- [ ] Can it survive a 2-year recession?
- [ ] Is the business simple and predictable?
- [ ] Favourable 10+ year destination?
- [ ] No fatal red flags?

---

## Output: The Good Companies List

After each quarterly cycle, Suggi receives a single document:

`investing/good-companies.md`

### Structure

```markdown
# Good Companies -- Intrinsic Value Estimates
# Data as of: Q2 2026 earnings

## Summary

229 companies screened. 47 passed quality gates. 41 valued
(4 WATCH, 2 DISCARDED).

## The List

Sorted by composite rank (25/25/50) for convenience. Higher rank =
both good AND cheap. Lower rank = good but expensive.

| Rank | Ticker | Company | Sector | Growth | ROIC | Moat | Mgmt | Bear IV | Base IV | Bull IV |
|:--|:--|:--|:--|--:|--:|--:|--:|--:|--:|--:|
| 1 | EXAMPLE | Example Corp | Industrials | 14.2% | 22.1% | 4.2 | 3.8 | $42 | $58 | $71 |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 41 | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Companies Not Valued

| Ticker | Company | Reason |
|:--|:--|:--|
| BADCO | Bad Corporation | DISCARD: structural decline, no moat |

## Full Analyses

Individual deep-dive files: investing/companies/{TICKER}.md
```

Each `investing/companies/{TICKER}.md` contains the full analysis:
moat assessment, management assessment, financial health, DCF with
scenarios, EPV, sensitivity matrix, thesis, checklist, citations.

### How Suggi Uses This

1. Review the list. The composite rank sorts good-and-cheap to the
   top -- these are the most immediately actionable.
2. For any company of interest, read the full deep-dive in
   `investing/companies/{TICKER}.md`.
3. Look up the current market price. Compare to the intrinsic value
   range.
4. If price < intrinsic value by a sufficient margin of safety:
   consider buying.
5. If price > intrinsic value: wait. The calculation is done. When
   price eventually drops (earnings miss, market panic, sector
   rotation), the IV estimate is already sitting there.

## Quarterly Cadence

The entire pipeline runs quarterly, aligned with earnings seasons:

- Mid-February (Q4/H2 earnings)
- Mid-May (Q1 earnings)
- Mid-August (Q2 earnings)
- Mid-November (Q3 earnings)

Between quarters: the list is static. Intrinsic value does not
change. Mr. Market's mood swings do not alter a company's worth.

Single-ticker mode: Suggi can request "Value {TICKER}" at any time.
The pipeline runs Stages 4-11 for that single company using the
latest available financial data.

## Job Architecture

One quarterly cron job. One on-demand mode.

### Job: Quarterly Quality Screen + Intrinsic Value

| Attribute | Value |
|:--|:--|
| **Owner** | main |
| **Schedule** | Quarterly: mid-Feb, mid-May, mid-Aug, mid-Nov |
| **Type** | Python (Phase A) + Agent orchestration (Phases B-C) |
| **Input** | Financial data APIs for target universe |
| **Output** | `investing/good-companies.md`, `investing/companies/{TICKER}.md` for each valued company |
| **Cost** | Data API + LLM tokens |

**Process:**

1. Python script: pull data, validate quality, filter for growth
   and ROIC thresholds, rank by composite. ($0 LLM)
2. For each surviving company (typically 30-100): spawn
   researcher-1 and researcher-2 for moat/management/triage.
3. For each GOOD/WATCH company: deep dive -> conviction check ->
   DCF + EPV -> thesis -> checklist.
4. Write all outputs to the brain. Rebuild brain-index.

**Batching:** Process top-ranked companies first. After producing
analyses for the top 25, pause for Suggi review. If he wants more
depth on lower-ranked (good-but-expensive) companies, continue.

### On-Demand: Single Ticker

Triggered by Suggi: "Value {TICKER}"
Same pipeline, single company, latest data.

---

## Comparison: This Pipeline vs Others

| Aspect | This Pipeline | Screener Pipeline | Pipeline-Final (Wrong) |
|:--|:--|:--|:--|
| What it finds | All good companies | Cheap companies first | Cheap companies first |
| Who gets valued | Every good company | Only PASS (quality + cheap) | Only PASS (quality + cheap) |
| Cheapness role | Sort order only | Filter (determines who proceeds) | Filter (determines who proceeds) |
| Market price | Not used | Not used | Central (MOS, alerts) |
| Output | List of good companies with IV | List of cheap+good with IV | BUY/WATCH/DISCARD with MOS |
| Goal | Be ready when price drops | Find bargains now | Find bargains now |
| Philosophy | Buffett: know what things are worth, wait | Greenblatt: buy cheap, sort later | Mixed (confused) |

---

## Cross-Links

- `governance/suggi-investment-approach.md` -- the original methodology
- `investing/pipeline/screener-intrinsic-value-pipeline.md` -- the screener-first variant
- `investing/pipeline/investment-pipeline-final.md` -- the previous (incorrect) version
- `investing/frameworks/dcf-intrinsic-value.md` -- DCF methodology
- `investing/frameworks/sector-specific-metrics.md` -- sector metrics
- `investing/frameworks/simple-moat-scoring.md` -- moat scoring
- `investing/frameworks/simple-management-scoring.md` -- management scoring
- `investing/frameworks/deep-moat-scoring.md` -- deep competitive analysis
- `investing/frameworks/deep-financial-scoring.md` -- financial health analysis
