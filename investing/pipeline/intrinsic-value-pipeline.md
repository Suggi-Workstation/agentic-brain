---
name: intrinsic-value-pipeline
id: 20260727T173900Z
tier: pipeline
author: Ava
tags: [value-investing, intrinsic-value, quality, dcf, EPV, buffett, munger, quarterly, patience, wonderful-business]
links:
  - governance/suggi-investment-approach.md
  - investing/frameworks/dcf-intrinsic-value.md
  - investing/frameworks/sector-specific-metrics.md
  - investing/frameworks/simple-moat-scoring.md
  - investing/frameworks/simple-management-scoring.md
  - investing/frameworks/deep-moat-scoring.md
  - investing/frameworks/deep-financial-scoring.md
---

# Intrinsic Value Pipeline -- Find Good Businesses, Value Them, Wait

## The Philosophy

Warren Buffett evolved from Graham's "buy any cheap stock" to
Munger's "buy wonderful businesses." This pipeline follows that
evolution.

> "It's far better to buy a wonderful company at a fair price
> than a fair company at a wonderful price."
> -- Buffett, 1989 Berkshire Letter

> "Separate analysis into two steps. First, test business quality:
> moat durability, return profile, management discipline, cash
> resilience. Second, estimate a conservative fair value range."
> -- KeepRule, synthesizing Buffett's process

The modern research validates this approach. Quality value investing
-- identifying excellent businesses first, valuing them second, and
only then looking at price -- has dominated in recent decades.
Purely mechanical deep-value approaches that rank by cheapness have
seen diminished returns as markets have become more informationally
efficient.

## What This Pipeline Does

1. Pull raw financial data for a target region.
2. Identify good businesses: growth, returns on capital, durable
   competitive advantage, honest management, strong balance sheet.
3. Calculate intrinsic value for every good business.
4. Maintain the list. Recalculate quarterly with new financial data.

## What This Pipeline Does NOT Do

- **Does not rank by cheapness.** Cheapness metrics (EV/EBIT, P/B,
  P/E) embed market price. Market price changes daily. A quarterly
  pipeline cannot rank by a daily variable. Cheapness screening is
  Suggi's domain -- he runs his own Greenblatt-style screens when
  he wants to find bargains.

- **Does not calculate margin of safety.** MOS requires market price.
  Market price is Suggi's domain.

- **Does not monitor prices or send price alerts.** Intrinsic value
  changes quarterly with financial data. Between quarters, the
  number is stable. Mr. Market's daily mood swings do not change
  what a business is worth.

- **Does not recommend buys, sells, or position sizes.** Suggi decides.

- **Does not gate companies by price.** A wonderful business trading
  at 40x earnings belongs on the list. It is a good business. The
  price may never be attractive, but the intrinsic value calculation
  is ready if it ever becomes so.

## Why Cheapness Ranking Is Irrelevant Here

The 25/25/50 composite from `suggi-investment-approach.md` uses:

| Metric | Contains Market Price? |
|:--|:--|
| EV/EBIT | Yes -- Enterprise Value = Market Cap + Debt - Cash |
| P/B | Yes -- Price-to-Book |
| P/E | Yes -- Price-to-Earnings |
| P/FCF | Yes -- Price-to-Free Cash Flow |

Every cheapness metric embeds the market price. The market price
changes every second the market is open. Therefore, a cheapness
ranking produced on a Monday is different from one produced on a
Tuesday, even though the business has not changed at all.

This is useful for Suggi when he is actively screening for bargains.
It is useless for a quarterly pipeline whose purpose is to identify
good businesses and value them independent of price.

**What changes quarterly:** Revenue, earnings, cash flows, margins,
debt levels, ROIC. These are financial fundamentals reported in
10-Q/10-K filings. They are the inputs to intrinsic value. They do
not change day-to-day.

---

## The Pipeline

### Phase A: Quality Identification (Deterministic + Agentic)

#### Stage 0: Universe Definition

Define the investable universe. Maintained as a config file:
`investing/universe.yaml`.

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

Companies in "avoid" sectors are excluded before any analysis.

#### Stage 1: Data Ingestion and Quality Validation

Pull raw financial data for every company in the universe.

**Per company collected:** Revenue (10 years), EBIT, net income,
operating cash flow, free cash flow, CapEx, depreciation, total
assets, total debt, shareholders' equity, cash and equivalents,
shares outstanding (basic + diluted), gross margin, sector
classification, insider ownership percentage.

**Data quality validation (before any analysis):**
- Negative enterprise values: flag
- Missing critical fields (>3): exclude, flag for investigation
- Stale data (>90 days since last filing): flag
- Extreme outliers (>5 SD from sector median): flag
- If >20% of fields missing across the universe: HALT

#### Stage 2: Quantitative Quality Gates

These are the only quantitative thresholds. They are based on raw
financial data -- no market price in any of them.

**Growth requirement:**

| Sector | Growth Metric |
|:--|:--|
| Industrial / Consumer | Revenue CAGR, 5-10 years |
| Technology (SaaS) | Revenue CAGR, 5 years |
| Financial (Banks) | Book Value per Share Growth, 5 years |
| Financial (Insurance) | Premium Growth, 5 years |
| REITs | FFO per Share Growth, 5 years |
| Energy / Materials | Production Volume Growth, 5 years |
| Healthcare (Pharma) | Revenue CAGR, 5-10 years |

Threshold: CAGR >= 10%.

**Returns requirement:**

| Sector | Quality Metric |
|:--|:--|
| Industrial / Consumer | ROIC, 5-year average |
| Technology (SaaS) | Rule of 40 (Rev Growth + FCF Margin) |
| Financial (Banks) | ROE, 5-year average |
| Financial (Insurance) | Combined Ratio |
| REITs | ROE, 5-year average |
| Energy / Materials | ROCE, 5-year average |
| Healthcare (Pharma) | ROIC, 5-year average |

Threshold: ROIC >= 15% and/or ROE >= 15% (or sector equivalent).

**Financial health minimums (deterministic):**

| Gate | Threshold | Rationale |
|:--|:--|:--|
| Debt / EBITDA | < 4x (< 3x for cyclicals) | Excessive leverage |
| Interest Coverage | > 3x | Cannot service debt |
| Negative FCF years | < 3 consecutive | Persistent cash burn |
| Current Ratio | > 1.0 | Liquidity crisis risk |

Companies failing any financial health gate are DISCARDED. A good
business must be able to survive a recession.

**Quality consistency heuristics (informational flags):**

These are not gates. They are flags attached to the company record.
The deep-dive agent investigates flagged items.

- Revenue grew in 7+ of last 10 years?
- Gross margin stable or expanding over 5 years?
- ROIC >= estimated cost of capital by 500+ bps over 5 years?
- FCF / Net Income > 0.7 over 5-year average?

A company that fails multiple consistency checks is flagged for
extra scrutiny. It may still be a good business in a cyclical
downturn. The deep dive determines this.

#### Stage 3: Moat Assessment

See: `investing/frameworks/simple-moat-scoring.md`

For every company passing Stage 2, researcher-1 scores the moat
on 4 dimensions:

| Dimension | Weight | Question |
|:--|:--|:--|
| Source Clarity | 20% | Which of 6 moat sources? With what evidence? |
| Moat Width | 30% | How strong is the advantage? ROIC-WACC spread and persistence? |
| Threat Horizon | 25% | How many years before the moat could be breached? |
| Moat Trend | 25% | Widening, stable, or narrowing? |

**Moat score >= 3.0:** The company has at least a narrow durable
competitive advantage. Proceed to Stage 4.

**Moat score < 3.0:** The company lacks a durable moat. It is
flagged "no durable moat." It stays on the list -- Suggi decides
whether a company without a moat warrants attention. The intrinsic
value is still calculated, with a note that terminal value assumptions
must be conservative (no moat = returns revert to cost of capital
faster).

#### Stage 4: Management Assessment

See: `investing/frameworks/simple-management-scoring.md`

For every company passing Stage 2, researcher-2 scores management
on 5 dimensions:

| Dimension | Weight | Question |
|:--|:--|:--|
| Insider Ownership | 25% | Skin in the game? |
| Buyback Quality | 20% | Buying at attractive prices or just offsetting dilution? |
| Acquisition Track Record | 20% | Disciplined or empire-building? |
| Shareholder Communication | 15% | Candid or promotional? |
| Capital Allocation | 20% | Returns-focused or growth-at-any-cost? |

**Management score >= 3.0:** Owner-oriented stewards. Proceed.

**Management score < 3.0:** Flagged "management concerns." Stays on
the list. Suggi decides. Intrinsic value is still calculated, with
a note that management quality is a risk factor.

### Phase B: Intrinsic Value Calculation

Every company that passed Stage 2 (regardless of moat or management
scores) proceeds to intrinsic value calculation. The moat and
management scores inform the DCF assumptions (terminal value,
margin sustainability, WACC adjustment). They do not gate access
to valuation.

#### Stage 5: Deep Dive (Parallel)

Two independent analyses for each company:

**5A. Moat & Competitive Dynamics (researcher-1)**

See: `investing/frameworks/deep-moat-scoring.md`

- Full moat durability assessment
- Porter's Five Forces industry analysis
- Competitor benchmarking (top 3-5)
- 10+ year destination projection (Sleep/Zakaria)

**5B. Financial Health & Normalized Earnings (researcher-2)**

See: `investing/frameworks/deep-financial-scoring.md`

- Normalized earnings (adjusting for one-time items, cycles)
- FCF conversion quality (5-year trend)
- Debt structure analysis (maturity ladder)
- ROIIC (return on incremental invested capital)
- Structured red flag scan

#### Stage 6: Conviction Check

Three questions from Sleep, Pabrai, and Munger. These are about
the BUSINESS, not the PRICE:

1. **Destination question (Sleep):** "Can I describe what this
   business looks like in 5-10 years with reasonable confidence?"
   If no: the IV carries a wider range. The destination is uncertain.

2. **Fat pitch question (Pabrai):** "Is this an obviously good
   business?" Not "would I buy at this price" -- just "is this
   business excellent?" If the answer requires complex justification,
   it may not be excellent.

3. **Munger inversion:** "What is the single worst thing that could
   happen to this business, and how likely?" This informs the bear
   case assumptions.

#### Stage 7: Intrinsic Value Calculation

See: `investing/frameworks/dcf-intrinsic-value.md`

**Market price is not used anywhere in this stage.**

**7A. Two-Stage DCF with Bull/Base/Bear Scenarios**

```
FCF = EBIT * (1 - Tax Rate) + Depreciation - CapEx - Change in WC
PV = Sum of [FCF_YearN / (1 + WACC)^N] for N = 1 to 5
Terminal Value = FCF_Year5 * (1 + g) / (WACC - g)
Enterprise Value = PV_Explicit + PV_Terminal
Equity Value = EV - Total Debt + Cash
Intrinsic Value Per Share = Equity Value / Diluted Shares
```

Key: diluted shares, not basic. SBC is a real cost.

Three scenarios:

| Parameter | Bear (--) | Base | Bull (+) |
|:--|:--|:--|:--|
| Revenue growth (Y1-3) | Base - 2.0pp | Thesis-driven | Base + 1.5pp |
| Operating margin (term.) | Base - 2.0pp | Normalized | Base + 1.5pp |
| WACC | Base + 1.5pp | CAPM + moat adj | Base - 1.0pp |
| Terminal growth rate | Base - 0.5pp | GDP-based | Base + 0.3pp |

Bear shifts are larger than bull shifts. Downside is non-linear.

**Moat score -> terminal value assumptions:**

| Moat Score | Terminal Growth | WACC Adjustment | Terminal Margin |
|:--|:--|:--|:--|
| 4.0-5.0 (Wide) | GDP + 0.5% | -1.0% | Stable or expanding |
| 3.0-3.9 (Narrow) | ~GDP | None | Stable |
| 2.0-2.9 (Weak) | GDP - 0.5% | +0.5% | Converging to industry avg |
| <2.0 (None) | GDP - 1.0% | +1.0% | At or below industry avg |

**Management score -> margin and reinvestment assumptions:**

| Mgmt Score | Margin Assumption | Reinvestment Assumption |
|:--|:--|:--|
| 4.0-5.0 | Can sustain or expand | High ROIIC, disciplined |
| 3.0-3.9 | Stable at normalized | Adequate |
| 2.0-2.9 | May deteriorate | Watch for empire-building |
| <2.0 | Assume deterioration | Conservative (value-destructive possible) |

**Sector-appropriate methodology auto-selected:**

| Sector | DCF Method |
|:--|:--|
| Industrial/Consumer | 2-stage DCF |
| SaaS | Revenue-based DCF (CAC/LTV/churn) |
| REITs | FFO/AFFO multiple + NAV |
| Banks | Excess returns model (ROE - COE * BV) |
| Insurance | Combined ratio + float value + investment portfolio |
| Energy/Materials | Cycle-normalized earnings + reserve valuation |

**7B. Earnings Power Value (EPV) -- No-Growth Floor**

```
EPV = Normalized EBIT * (1 - Tax Rate) / WACC
EPV per Share = (EPV - Net Debt) / Diluted Shares
```

This is what the business is worth if it never grows again. The
gap between DCF and EPV is the value the market assigns to growth.
If DCF > 2x EPV, the growth assumptions dominate the valuation --
flag for scrutiny.

**7C. Sensitivity Matrix**

5x5 grid: WACC vs terminal growth rate. Shows the IV range across
reasonable assumptions. Included in the company report.

#### Stage 8: Investment Thesis

3-5 testable pillars per company:
- **Specific:** what will happen, and why
- **Falsifiable:** what data point would disprove it
- **Monitored:** metric + update cadence

Variant perception: "What do we believe that the market does not?"
Without variant perception, there is no edge. But the variant
perception is about the BUSINESS, not the PRICE.

Example of a business variant perception (valid): "The market
believes Company X's core product is being commoditized, but its
recent shift to subscription pricing is not yet reflected in
analyst models. Recurring revenue will grow from 30% to 60% of
total within 3 years."

Example of a price variant perception (irrelevant for this
pipeline): "The stock is undervalued because it trades at 8x
earnings." That is Suggi's call to make when he compares IV to
market price.

#### Stage 9: Quality Checklist

- [ ] Do I understand this business? Can I explain it simply?
- [ ] Does it have a durable competitive advantage? (Moat score,
  evidence from Stage 3 + 5A)
- [ ] Is management owner-oriented and capable? (Mgmt score,
  evidence from Stage 4)
- [ ] Can it survive a 2-year recession? (Balance sheet from Stage
  5B)
- [ ] Is the business simple and predictable? (Not complexity for
  complexity's sake)
- [ ] Favourable 10+ year destination? (Stage 5A destination
  analysis)
- [ ] No fatal red flags? (Stage 5B red flag scan)

Every answer cites evidence from Stages 3-5.

---

## Output: The Good Companies List

After each quarterly cycle, one document is produced and maintained:

`investing/good-companies.md`

### Structure

```markdown
# Good Companies -- Intrinsic Value Estimates
# Updated: Q2 2026 (data as of latest 10-Q/10-K filings)

Total universe: 3,500 companies
Quality gates passed: 47 companies
Intrinsic value calculated: 47 companies
Not valued: 6 (data quality issues, unresolved red flags)

---

## Alphabetical List

| Ticker | Company | Sector | Rev CAGR | ROIC | Moat | Mgmt | Bear IV | Base IV | Bull IV |
|:--|:--|:--|--:|--:|--:|--:|--:|--:|--:|
| ABC | Alpha Corp | Consumer | 12.3% | 18.2% | 3.8 | 4.1 | $31 | $42 | $55 |
| DEF | Beta Inc | Software | 22.1% | 35.0% | 4.5 | 3.2 | $98 | $145 | $188 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| ZZZ | Zeta Ltd | Industrials | 10.1% | 16.7% | 3.2 | 3.8 | $14 | $19 | $24 |

## Flagged Companies

Companies with moat or management concerns. Included in the list
above. Flagged so Suggi can apply his own judgment.

| Ticker | Flag | Detail |
|:--|:--|:--|
| GHI | Moat < 3.0 | Narrowing moat -- competitor gaining share. Terminal value assumptions are conservative. |
| JKL | Mgmt < 3.0 | Serial dilution -- share count up 15% in 5 years. Margin assumptions reflect potential deterioration. |

## Discarded Companies

Companies that failed quantitative gates or have fatal red flags.

| Ticker | Reason |
|:--|:--|
| MNO | Debt/EBITDA 6.2x -- cannot survive a recession |
| PQR | 5 consecutive years of negative FCF |

---

## Individual Company Files

Full deep-dive analyses: investing/companies/{TICKER}.md

Each file contains:
- Business description and industry context
- Moat assessment with 4-dimension scores and evidence
- Management assessment with 5-dimension scores and evidence
- Normalized earnings and financial health report
- DCF model: bull/base/bear scenarios with explicit assumptions
- EPV cross-check
- Sensitivity matrix (WACC vs terminal growth)
- Investment thesis with testable pillars
- Quality checklist results
- Full source citations
```

### How Suggi Uses This

1. Review the list. Every company on it is a good business with a
   durable competitive advantage, honest management, and a strong
   balance sheet.
2. For any company of interest, read the full deep-dive analysis.
3. Look up the current market price. Compare to the intrinsic value
   range in the table.
4. If the price is below intrinsic value by a sufficient margin of
   safety: consider buying.
5. If the price is above intrinsic value: wait. The IV calculation
   is already done. When the price drops -- earnings miss, market
   panic, sector rotation, recession -- the number is sitting there
   ready.
6. Most quarters, the answer will be "nothing to do." This is a
   feature, not a failure. Patience is the edge.

### The Screener Is Separate

Suggi runs his own Greenblatt-style screens when he wants to find
bargains among the universe. He uses his own 25/25/50 composite with
current market prices. That is transaction-level work -- daily,
active screening.

This pipeline is valuation-level work -- quarterly, patient, price-
independent. The two complement each other: the screener finds what
looks cheap today; the pipeline knows what the good businesses are
actually worth, so when the screener flags one of them, Suggi
already has the intrinsic value number.

---

## Quarterly Cadence

The pipeline runs quarterly, aligned with earnings seasons:

| Run | Timing | Data Source |
|:--|:--|:--|
| Q1 | Mid-February | Q4/H2 10-K / annual reports |
| Q2 | Mid-May | Q1 10-Q |
| Q3 | Mid-August | Q2 10-Q |
| Q4 | Mid-November | Q3 10-Q |

Between quarters: the list is static. Intrinsic value does not
change because Mr. Market changed his mood. If a material event
occurs (major acquisition, CEO departure, fraud revelation), Suggi
can trigger a single-ticker revaluation.

**Single-ticker mode:** Triggered by Suggi: "Value {TICKER}."
Same pipeline (Stages 3-9) for one company, using latest available
data.

## Job Architecture

One cron job. One on-demand mode.

### Job: Quarterly Good Companies + Intrinsic Value

| Attribute | Value |
|:--|:--|
| **Owner** | main |
| **Schedule** | Quarterly: mid-Feb, mid-May, mid-Aug, mid-Nov |
| **Type** | Python (Phase A, Stages 0-2) + Agent orchestration (Phase B, Stages 3-9) |
| **Input** | Financial data APIs for target universe |
| **Output** | `investing/good-companies.md`, `investing/companies/{TICKER}.md` for each valued company |
| **Cost** | Data API + ~$30-100/cycle in LLM tokens |

**Process:**

1. Python script (no LLM): pull data, validate quality, apply
   quantitative quality gates (growth, ROIC, financial health).
   Output: list of companies that passed Stage 2.
2. For each survivor (typically 30-100 companies): spawn
   researcher-1 and researcher-2 in parallel for moat scoring
   and management scoring.
3. For each company: deep dive -> conviction check -> DCF + EPV
   -> thesis -> checklist.
4. Write `investing/good-companies.md` and all individual company
   files. Commit to brain. Rebuild brain-index.

**Batching strategy for large universes:** Process in batches of
25, highest-quality first (sorted by ROIC). After the first batch,
pause for Suggi to review. He may want to add or remove companies
from the list before the pipeline continues.

---

## Research Foundation

The quality-first approach is validated across sources:

**Buffett's own evolution (from Ryan O'Connell, CFA, 2026):**
"Charlie Munger changed everything. Munger persuaded Buffett that
it was 'far better to buy a wonderful company at a fair price than
a fair company at a wonderful price.' This philosophical shift --
from quantitative cheapness to qualitative excellence -- transformed
Buffett from a deep-value practitioner into the world's greatest
quality-value investor."

**Two-step process (KeepRule, synthesizing Buffett):**
"Separate analysis into two steps. First, test business quality:
moat durability, return profile, management discipline, and cash
resilience. Second, estimate a conservative fair value range and
buy only when price is reasonable relative to that range."

**Quality over cheapness (Investopedia, 2026):**
"Quality value investing -- identifying excellent businesses first,
valuing them second, and only then looking at price -- has dominated
in recent decades. Purely mechanical deep-value approaches that
rank by cheapness have seen diminished returns."

**Price vs value separation (KeepRule, Buffett's action steps):**
"1. Calculate intrinsic value before looking at price. 2. Use
multiple valuation methods. 3. Only buy at a meaningful discount
to value."

**Recalculation frequency (deepviews.dev, myfastbroker.com, 2026):**
"You should recalculate intrinsic value at least quarterly when new
financial results are released, or whenever there is a material
change in the company's fundamentals."

---

## Comparison With Previous Pipeline Versions

| Aspect | This Pipeline (v3) | Screener Pipeline (v2) | Pipeline-Final (v1, Wrong) |
|:--|:--|:--|:--|
| What it finds | All good businesses | Good AND cheap companies | Good AND cheap companies |
| Cheapness role | Absent | Sort order only | Filter + sort + monitoring |
| Who gets valued | Every good business | Only PASS (cheap+good) | Only PASS (cheap+good) |
| Market price | Not used | Not used | Central (MOS, alerts, sizing) |
| Ranking | Alphabetical or quality-sorted | 25/25/50 composite | 25/25/50 composite |
| Output | List of good companies + IV | Ranked list + IV | BUY/WATCH/DISCARD + MOS |
| Screener | Separate (Suggi's domain) | Part of pipeline | Part of pipeline |
| Philosophy | Buffett/Munger: quality first | Hybrid: quality + cheapness | Confused: Greenblatt + Buffett |

---

## Cross-Links

- `governance/suggi-investment-approach.md` -- Suggi's personal screening methodology (separate from this pipeline)
- `investing/pipeline/screener-intrinsic-value-pipeline.md` -- the screener-first variant (earlier version)
- `investing/pipeline/investment-pipeline-final.md` -- the original proposal (superseded)
- `investing/frameworks/dcf-intrinsic-value.md` -- full DCF methodology
- `investing/frameworks/sector-specific-metrics.md` -- sector-appropriate growth and quality metrics
- `investing/frameworks/simple-moat-scoring.md` -- moat scoring framework
- `investing/frameworks/simple-management-scoring.md` -- management scoring framework
- `investing/frameworks/deep-moat-scoring.md` -- deep competitive dynamics analysis
- `investing/frameworks/deep-financial-scoring.md` -- financial health and red flag analysis
