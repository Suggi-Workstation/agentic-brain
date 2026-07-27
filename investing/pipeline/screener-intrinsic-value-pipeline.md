---
name: screener-intrinsic-value-pipeline
id: 20260727T171700Z
tier: pipeline
author: Ava
tags: [value-investing, screener, intrinsic-value, dcf, EPV, composite-ranking, greenblatt, magic-formula, quarterly]
links:
  - investing/pipeline/investment-pipeline-final.md
  - governance/suggi-investment-approach.md
  - investing/frameworks/dcf-intrinsic-value.md
  - investing/frameworks/sector-specific-metrics.md
  - investing/frameworks/simple-moat-scoring.md
  - investing/frameworks/simple-management-scoring.md
---

# Screener + Intrinsic Value Pipeline -- Corrected Architecture

## What Changed and Why

The original `investment-pipeline-final.md` (v3) conflated two
separate responsibilities:

1. **My job:** Screen companies by 25/25/50 weights and calculate
   intrinsic value from financial fundamentals.
2. **Suggi's job:** Compare intrinsic value to market price, decide
   what to buy, when to buy, and at what price.

The original pipeline embedded market price into the process at
every stage: MOS calculations, price-based watchlist monitoring,
price-alert thresholds, position sizing. This was wrong.

**The correction:** Market price is irrelevant to intrinsic value
calculation. Intrinsic value is derived from a company's financial
fundamentals -- earnings, cash flows, growth rates, competitive
position. These change quarterly when new financial data is released.
They do not change day-to-day because the stock price moved.

Suggi receives the output (ranked list of companies with intrinsic
value ranges) and makes his own buy/sell/price decisions. I do not
track market prices, I do not calculate margin of safety against
market price, and I do not recommend position sizes.

## The Core Principle: Intrinsic Value Moves Quarterly, Not Daily

Graham, Buffett, and every serious value investor agree: intrinsic
value is the discounted value of all future cash a business will
generate. This number changes when the business changes its earnings
trajectory -- which happens quarterly when new financial statements
are released.

> "Intrinsic value is what a company is actually worth based on its
> earnings and assets. It is independent of the daily share price.
> The market price moves up and down every day because of news,
> sentiment, and emotions. Intrinsic value moves slowly because it
> depends on how much a business actually earns."

-- Benjamin Graham, The Intelligent Investor (summarized)

> "You should revisit your valuation at least quarterly when new
> financial results are released, or whenever there is a material
> change in the company's fundamentals."

-- Multiple valuation guides (deepviews.dev, myfastbroker.com, 2026)

**What this means for the pipeline:**

- Intrinsic value is recalculated quarterly, aligned with earnings
  release cycles.
- Between quarters, intrinsic value is treated as a constant -- it
  does not shift because Mr. Market changed his mood.
- The output to Suggi is: "Here are the companies ranked by the
  screening methodology. For those that pass qualitative filters,
  here is their intrinsic value range. The data is current as of
  [latest quarter's filings]."
- Suggi looks at the current market price himself and decides what
  to do. He does not need an agent tracking price movements.

## Pipeline Overview

The pipeline has three phases:

### Phase A: Screening (Deterministic -- Python, No LLM)

Pull financial data -> validate quality -> composite rank by 25/25/50
-> apply broad screen thresholds.

Output: ranked CSV of companies that passed the broad screen.

### Phase B: Qualitative Filters (Agentic -- Decorrelated)

For companies passing the broad screen: exclusion filtering, moat
scoring, management scoring. Separate cheap-and-good from
cheap-because-bad.

Output: PASS/WATCH/DISCARD with structured evidence.

### Phase C: Intrinsic Value Calculation (Agentic)

For PASS companies: DCF with bull/base/bear scenarios, EPV
cross-check, sector-appropriate methodology. No market price
involved.

Output: intrinsic value range per company, updated quarterly.

---

## Phase A: Screening

### Stage 0: Universe Definition

Before any data is pulled, define the investable universe:

- Target region (e.g., EU ~3,500 companies, S&P 500)
- Sector exclusions (circle of competence boundaries)
- Market cap minimums

Maintained as a config file: `investing/universe.yaml`.

### Stage 0.5: Data Quality Validation

Validate the dataset before ranking:

- Negative enterprise values: flag as data error or net-cash company
- Missing data fields: exclude from ranking, flag for investigation
- Stale data: >90 days since last reported period
- Extreme outliers: >5 standard deviations from sector median

If >20% of fields are missing, HALT -- do not proceed with bad data.

### Stage 1: Sector-Aware Composite Ranking

Different sectors need different metrics. One-size-fits-all ranking
misprices banks, SaaS companies, REITs, and insurers.

| Sector | Growth Metric (25%) | Quality Metric (25%) | Cheapness Metric (50%) |
|:--|:--|:--|:--|
| Industrial/Consumer | Revenue CAGR (5-10yr) | ROIC | EV/EBIT |
| Financial (Banks) | Book Value Growth | ROE | P/B |
| Financial (Insurance) | Premium Growth | Combined Ratio | P/B |
| Technology (SaaS) | Revenue CAGR | Rule of 40 | EV/Revenue |
| REITs | FFO/Share Growth | ROE | P/FFO |
| Energy/Materials | Production Volume Growth | ROCE | EV/EBITDA |
| Healthcare (Pharma) | Revenue CAGR | ROIC | EV/EBIT |
| Default | Revenue CAGR | ROIC | EV/EBIT |

**Owner earnings normalization (Buffett):**

For the cheapness metric, use owner earnings instead of raw EBIT or
FCF where possible:

```
Owner Earnings = Net Income + Depreciation - Average Annual Maintenance Capex
Maintenance Capex = (5yr avg Capex/Depreciation ratio) * Current Depreciation
```

This prevents overstating the cheapness of asset-heavy businesses
(where depreciation understates true capital needs) and
understating the cheapness of asset-light businesses.

**Composite ranking formula:**

```
Composite = 0.25 * growth_percentile + 0.25 * quality_percentile + 0.50 * cheapness_percentile
```

Within-sector percentile ranks. Sort ascending (lower = better).
Pure math. Deterministic. No LLM.

### Stage 2: Broad Screen Thresholds

Walk the ranked list 1-by-1. A company must meet BOTH:
- CAGR growth >= 10% over 5-10 years (sector-appropriate metric)
- ROIC >= 15% and/or ROE >= 15% (sector-appropriate metric)

For MVP: tighten to CAGR >= 15%, ROIC >= 20% to keep the candidate
set manageable (20-50 companies).

Also apply the "wonderful business at fair price" heuristic:
1. Revenue growth in 7+ of last 10 years?
2. Gross margin stable or expanding over 5 years?
3. ROIC >= cost of capital by 500+ bps over 5 years?

Companies failing any check are flagged "statistically cheap but
possibly not wonderful" -- proceed to Phase B with a warning tag.

---

## Phase B: Qualitative Filters

### Stage 3: Exclusion + Moat + Management Triage

Two decorrelated agents (researcher-1, researcher-2) evaluate each
company independently. Main session compares verdicts.

#### 3A. Deterministic Exclusions (auto-DISCARD)

- P/E > 40, P/S > 5, P/FCF > 30, P/EBIT > 25
- Debt/EBITDA > 4x (>3x for cyclicals)
- Debt/Equity > 1.5
- Negative FCF for 3+ consecutive years
- Market cap < $50M

These use reported metrics from the dataset. No agent judgment.

#### 3B. Moat Scoring (researcher-1)

See: `investing/frameworks/simple-moat-scoring.md`

4-dimension composite score:
- Source Clarity (20%): which of 6 moat sources, with evidence
- Moat Width (30%): ROIC-WACC spread magnitude and persistence
- Threat Horizon (25%): how many years before moat could be breached
- Moat Trend (25%): widening, stable, or narrowing

Moat score < 3.0 = DISCARD.

#### 3C. Management Scoring (researcher-2)

See: `investing/frameworks/simple-management-scoring.md`

5-dimension composite score:
- Insider Ownership (25%)
- Buyback Quality (20%)
- Acquisition Track Record (20%)
- Shareholder Communication (15%)
- Capital Allocation Discipline (20%)

Management score < 3.0 = DISCARD.

#### 3D. The Critical Triage: Cheap-and-Good vs Cheap-Because-Bad

Both researchers produce independent verdicts:
- PASS: genuinely out of favor, business quality intact
- WATCH: good business but concerns exist (expensive, unclear thesis)
- DISCARD: correctly cheap for structural reasons

Every claim requires a source URL or filing reference.

#### 3E. Structured Debate Protocol

When researchers disagree: each produces a rebuttal addressing the
other's evidence. Maximum 2 debate rounds. Unresolved disagreements
escalate to Suggi with both analyses.

---

## Phase C: Intrinsic Value Calculation

### Stage 4: Deep Dive (Parallel)

For each PASS company, two independent analyses run in parallel:

#### 4A. Moat & Competitive Dynamics (researcher-1)

See: `investing/frameworks/deep-moat-scoring.md`

- Full moat durability assessment (6-source framework)
- Porter's Five Forces industry analysis
- Competitor benchmarking (top 3-5 by market share, margins, ROC)
- 10+ year destination projection (Sleep/Zakaria)

#### 4B. Financial Health & Red Flags (researcher-2)

See: `investing/frameworks/deep-financial-scoring.md`

- Normalized earnings (adjusting for one-time items, cycles)
- FCF conversion quality (OCF/NI, FCF/NI ratios, 5-year trend)
- Debt structure analysis (maturity ladder, leverage ratios)
- ROIIC (return on incremental invested capital)
- Structured red flag scan (earnings quality, balance sheet, cash
  flow, governance, Munger psychology flags)

### Stage 5: Conviction Check -- Three Questions

Before valuation, three questions from Sleep, Pabrai, and Munger:

1. **Destination question (Sleep):** "Can I describe what this
   business looks like in 5-10 years with confidence?" No = WATCH.

2. **Fat pitch question (Pabrai):** "Is this a no-brainer?" If the
   answer requires complex justification, it is not a fat pitch.

3. **Munger inversion:** "What is the single worst thing that could
   happen, and how likely?" If likelihood >20% and impact is
   catastrophic, DISCARD.

### Stage 6: Intrinsic Value Calculation

**This is the core output. Market price is not used anywhere in
this calculation.**

See: `investing/frameworks/dcf-intrinsic-value.md`

#### 6A. Two-Stage DCF

```
FCF = EBIT * (1 - Tax Rate) + Depreciation - CapEx - Change in Working Capital
PV of Explicit Period = Sum of [FCF_YearN / (1 + WACC)^N] for N = 1 to 5
Terminal Value = FCF_Year5 * (1 + g) / (WACC - g)
Enterprise Value = PV of Explicit FCFs + PV of Terminal Value
Equity Value = Enterprise Value - Total Debt + Cash
Intrinsic Value Per Share = Equity Value / Diluted Shares
```

Three scenarios: Bull, Base, Bear.

| Parameter | Bear | Base | Bull |
|:--|:--|:--|:--|
| Revenue growth (Y1-3) | Base - 2.0pp | Thesis-driven | Base + 1.5pp |
| Operating margin (terminal) | Base - 2.0pp | Normalized | Base + 1.5pp |
| WACC | Base + 1.5pp | CAPM + moat adj | Base - 1.0pp |
| Terminal growth | Base - 0.5pp | GDP-based | Base + 0.3pp |

Bear shifts are larger than bull shifts -- downside risks are
non-linear. The bear case is a stress-test floor, not a midpoint.

**Sector-specific methodology:** Auto-selected by industry
classification.

| Sector | Methodology |
|:--|:--|
| Industrial/Consumer | 2-stage DCF |
| SaaS | Revenue-based DCF with churn/CAC/LTV |
| REITs | FFO/AFFO multiple + NAV |
| Banks | Excess returns model (ROE - COE * BV) |
| Insurance | Combined ratio + float value + investment portfolio |
| Energy/Materials | Cycle-normalized earnings + reserve valuation |

#### 6B. Earnings Power Value (EPV) Cross-Check

```
EPV = Adjusted Earnings / Cost of Capital
Adjusted Earnings = Normalized EBIT * (1 - Tax Rate)
```

This is the "no-growth floor." If the DCF base case is >2x EPV,
growth assumptions dominate the valuation -- are they justified?

#### 6C. Sensitivity Analysis (5x5 Matrix)

Grid of WACC vs terminal growth rate to show the intrinsic value
range across reasonable assumptions.

### Stage 7: Investment Thesis

For each company with a completed valuation, formulate 3-5
testable thesis pillars:

- **Specific:** "Company X will grow revenue at 8%+ CAGR because
  product Y is gaining share in growing market Z."
- **Falsifiable:** "If market Z growth drops below 3%, this pillar
  breaks."
- **Monitored:** Maps to a metric with update cadence.

Include variant perception: "What does the market believe that we
believe is wrong?" Without variant perception, there is no edge.

### Stage 8: Investment Checklist

Synthesizes Pabrai's checklist with Buffett/Munger/Sleep criteria:

- [ ] Circle of competence: can I describe the destination 10
  years out?
- [ ] Durable moat: widening, stable, or narrowing?
- [ ] Able and honest management: skin in the game?
- [ ] Strong balance sheet: survive 2-year recession?
- [ ] Simple and predictable: understand in 30 minutes?
- [ ] Favourable 10+ year destination?
- [ ] No fatal red flags?

Every answer cites evidence from Stages 3-6.

---

## Output: What Suggi Receives

### Quarterly Screening Report

After each quarterly cycle, Suggi receives:

1. **Ranked screening list** (`investing/screens/{DATE}-screen.csv`):
   All companies ranked by 25/25/50 composite, with sector metrics,
   broad screen PASS/FAIL, and quality flags.

2. **PASS company analyses** (`investing/companies/{TICKER}.md`):
   Full deep-dive for each company that passed all gates:
   - Moat assessment with 4-dimension scores
   - Management assessment with 5-dimension scores
   - Financial health report with normalized earnings and red flags
   - DCF valuation: Bull/Base/Bear intrinsic value per share
   - EPV cross-check
   - Sensitivity matrix
   - Investment thesis with testable pillars
   - Conviction check results
   - Investment checklist results
   - Full source citations

3. **Summary table** (`investing/screens/{DATE}-summary.md`):
   Quick-reference table of all PASS companies with ticker, sector,
   composite rank, moat score, management score, and intrinsic value
   range.

### What Is NOT Included

- **No margin of safety calculation.** MOS = (Intrinsic Value -
  Market Price) / Intrinsic Value. Since market price is Suggi's
  domain, MOS is Suggi's calculation.
- **No price monitoring or watchlist alerts.** Intrinsic value does
  not change between quarters. There is nothing to monitor daily.
- **No position sizing.** Capital allocation is Suggi's decision.
- **No buy/sell recommendations.** Suggi decides what, when, and
  at what price.

Suggi takes the intrinsic value range, compares it to the current
market price (which he can look up in seconds), and decides whether
the margin of safety is sufficient.

---

## Job Architecture

Two cron jobs. Clean separation. No market price tracking.

### Job 1: Quarterly Screening + Intrinsic Value

| Attribute | Value |
|:--|:--|
| **Owner** | main |
| **Schedule** | Quarterly. Week after most earnings releases: mid-Feb, mid-May, mid-Aug, mid-Nov |
| **Type** | Python (Phase A) + Agent (Phases B-C) |
| **Stages** | 0-8 (full pipeline) |
| **Input** | Financial data APIs for target universe |
| **Output** | `investing/screens/{DATE}-screen.csv`, `investing/screens/{DATE}-summary.md`, `investing/companies/{TICKER}.md` for each PASS company |
| **Cost** | Data API + ~$25-75/cycle in LLM tokens |

**Process:**
1. Python script pulls data, validates quality, runs composite
   ranking, applies broad screen thresholds. ($0 LLM)
2. Agent orchestration: main spawns researcher-1 and researcher-2
   for each broad-screen company (Phase B triage).
3. For PASS companies: deep dive -> conviction check -> DCF/EPV ->
   thesis -> checklist (Phase C).
4. Write all outputs to the brain. Rebuild brain-index.

### Job 2: Single-Ticker Mode (On-Demand)

Not a cron job. Triggered manually by Suggi: "Analyze {TICKER}."

Same pipeline (Stages 3-8) for a single company. Uses API-fetched
data. Output written to `investing/companies/{TICKER}.md`.

---

## What Stays From the Frameworks

The existing frameworks are correct and remain unchanged:

- `investing/frameworks/dcf-intrinsic-value.md` -- DCF methodology
- `investing/frameworks/sector-specific-metrics.md` -- sector metrics
- `investing/frameworks/simple-moat-scoring.md` -- moat scoring
- `investing/frameworks/simple-management-scoring.md` -- management scoring
- `investing/frameworks/deep-moat-scoring.md` -- deep moat analysis
- `investing/frameworks/deep-financial-scoring.md` -- financial health

These frameworks describe HOW to calculate intrinsic value, assess
moats, and evaluate management. They do not reference market price
in their methodology (the DCF framework uses market price only as
an output comparison in the MOS section, which is removed from the
pipeline output).

## Key Difference From Pipeline-Final

| Aspect | Pipeline-Final (Wrong) | This Pipeline (Correct) |
|:--|:--|:--|
| Market price in valuation | Central (MOS, price monitoring, alerts) | Absent (intrinsic value stands alone) |
| Output to Suggi | "BUY CANDIDATE with 35% MOS at $X" | "Intrinsic value range: $Y-$Z. Data as of Q2 2026." |
| Monitoring | Weekly price checks, MOS recalculation | None. IV updates quarterly with new financials. |
| Position sizing | Kelly-based formula, suggested % allocation | Not included. Suggi's decision. |
| Watchlist | Price-based (MOS crossing thresholds) | Quality-based (good business, monitor for thesis changes) |
| What changes between quarters | Price changes trigger alerts | Nothing. IV is stable until new financial data. |

## Implementation

### Phase 1: MVP (US Pilot)

1. Python screening script (Stages 0-2) for S&P 500.
   Composite ranking with sector-specific metrics, owner earnings
   normalization, data quality validation.
2. `investing/universe.yaml` with circle-of-competence definition.
3. Single-ticker deep-dive pipeline (Stages 3-8) tested on 3 known
   tickers.
4. Output template: `investing/companies/{TICKER}.md` with DCF,
   EPV, moat, management, thesis, checklist.

### Phase 2: Automation

1. Quarterly cron job (Job 1).
2. EU data API integration when ready.
3. Batch processing: top-N by rank, pause after producing 3-5
   completed analyses for Suggi review.

---

## Cross-Links

- `governance/suggi-investment-approach.md` -- the methodology this implements
- `investing/pipeline/investment-pipeline-final.md` -- the previous (incorrect) version
- `investing/frameworks/dcf-intrinsic-value.md` -- DCF methodology
- `investing/frameworks/sector-specific-metrics.md` -- sector-specific screening
- `investing/frameworks/simple-moat-scoring.md` -- moat scoring framework
- `investing/frameworks/simple-management-scoring.md` -- management scoring
- `investing/frameworks/deep-moat-scoring.md` -- deep competitive analysis
- `investing/frameworks/deep-financial-scoring.md` -- financial health analysis
