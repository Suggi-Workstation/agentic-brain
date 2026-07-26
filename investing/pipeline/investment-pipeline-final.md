---
name: investment-pipeline-final
id: 20260726T081700Z
tier: proposal
author: Ava + Link (merged)
tags: [value-investing, pipeline, screening, agent-architecture, multi-agent, buffett, munger, greenblatt, pabrai, sleep, magic-formula, job-decomposition, moat-scoring, management-scoring, position-sizing, post-mortem]
links:
  - governance/suggi-investment-approach.md
  - investing/pipeline/investment-pipeline-architecture.md
  - investing/pipeline/link-investment-pipeline.md
  - library/coding-agentic-ai/multi-agent-orchestration.md
  - library/value-investing/anchor-value-investing.md
  - library/value-investing/economic-moats.md
  - library/value-investing/margin-of-safety.md
  - library/investors/charlie-munger.md
---

# Investment Pipeline -- Final Merged Architecture (v3)

## Origin

This proposal merges two independent analyses:

- **Ava's v2** (2026-07-26): 10-stage pipeline grounded in 5 external
  research sources (CFA Institute, FinCatch, AlphaAgents, Google ADK,
  StackAI). Strengths: sector-specific screening, data quality validation,
  sentiment analysis, investment thesis formulation, continuous monitoring.
- **Link's enhanced proposal** (2026-07-26): 7-stage pipeline with 10
  specific value-investor-aligned gaps (G1-G10). Strengths: philosophical
  precision, "too hard" pile, owner earnings, post-mortem loop, job
  decomposition clarity.

Where the proposals agreed, the convergence validates the design. Where
they differed, the gaps are complementary. This merged proposal
incorporates the strongest elements of both. No compromises were needed
-- every addition from each proposal fills a genuine gap in the other.

## Problem

Suggi has a defined value investing methodology (documented in
`governance/suggi-investment-approach.md`) -- a Greenblatt-style composite
ranking of ~3,500 companies by growth, ROIC, and cheapness, followed by
manual 1-by-1 review to separate genuine bargains from value traps, with
moat analysis, management assessment, and a 30-50% margin-of-safety
threshold before any buy decision.

This is currently a manual process. At 3,500 companies, even a rapid
triage takes weeks per screening cycle. The agent team has no structured
pipeline to execute this methodology. The investing/ directory in the
agentic-brain is empty.

Two prior proposals (Ava v2, Link v1) identified different gap classes:

1. **Operational gaps** (Ava): No sector-specific metrics, no data quality
   validation, no sentiment analysis, no investment thesis formalization,
   no continuous monitoring infrastructure.

2. **Philosophical gaps** (Link): No "too hard" pile (Buffett), no owner
   earnings normalization (Buffett), no moat durability scoring (Munger),
   no management quality scoring (Pabrai), no "wonderful business at fair
   price" filter (Buffett evolution), no cycle awareness (Greenblatt), no
   post-mortem error loop (Munger/R5), no reverse-screening mode (Sleep),
   no position sizing framework (Munger/Kelly).

This merged proposal closes both classes. Every gap from both analyses
maps to a specific pipeline stage, job, or gate.

## Research Foundation

### External Validation (from Ava v2)

Five industry sources validate the architecture:

1. **CFA Institute (2025):** "Agentic AI for Finance" recommends workflows
   over autonomous agents, 5-component agent instructions, evaluator-optimizer
   pattern, guardrails at four layers, and human-in-the-loop for high-impact
   decisions. All four principles are embedded in this pipeline.

2. **FinCatch (May 2026):** Production equity research pipeline validates
   modular section writers, tiered parallelism, and deterministic assembly.
   Their architecture maps directly to our Stage 4 parallel fan-out and
   Stage 8 checklist synthesis.

3. **AlphaAgents (arXiv:2508.11152, Aug 2025):** Multi-agent debate reduces
   hallucination and improves reasoning quality. Validates our decorrelated
   researcher pattern and adds a dedicated sentiment dimension.

4. **Google ADK (2026):** 8 multi-agent patterns built on sequential, loop,
   and parallel primitives. "Reliability comes from decentralization and
   specialization." Our 5-job decomposition follows this principle.

5. **StackAI (Jan 2026):** "Add autonomy in layers. Invest in foundations
   that survive model changes." Our pipeline layers determinism (Stages 0-2)
   under agent judgment (Stages 3-7) under synthesis (Stages 8-10).

### Value Investor Alignment (merged)

Six principles are universal across Buffett, Munger, Greenblatt, Pabrai,
and Sleep:

1. **Screen broadly, then go deep.** Quantitative screens as first pass;
   qualitative deep dives for survivors.
2. **Moat is everything.** Durable competitive advantage is THE critical
   factor. No moat = no investment.
3. **Management matters enormously.** Owner-orientation, capital allocation
   skill, integrity. No cheapness compensates for bad management.
4. **Margin of safety is non-negotiable.** 30-50% discount to intrinsic
   value. Without it, you are speculating.
5. **Concentrate on your best ideas.** 5-15 positions, not 50-100.
   Diversification is protection against ignorance.
6. **Patience is the ultimate edge.** Most cycles should produce nothing.
   Forced action destroys returns.

Every pipeline stage maps to at least one of these principles. Every
investor-specific addition (Greenblatt's cycle awareness, Sleep's
destination analysis, Pabrai's checklist, Munger's inversion) has a
concrete stage, gate, or job.

---

## Proposed Solution -- 10-Stage Pipeline with 5 Jobs

The pipeline is organized into five phases: **Definition** (deterministic),
**Screening** (deterministic), **Triage** (agentic, decorrelated),
**Deep Analysis** (agentic, decorrelated + parallel), and **Decision +
Compounding** (synthesis + monitoring).

Two meta-capabilities run across stages rather than within them: **Cycle
Awareness** and **Reverse-Screening Mode**.

### Phase 0: Universe Definition (Deterministic)

#### Stage 0: Universe Definition + "Too Hard" Exclusion

**Source: Link G1. Ava had circle-of-competence mentions but no pre-gate.**

Before any data is pulled, define the investable universe. This is a
config file in the brain: `investing/universe.yaml`.

```yaml
universes:
  us-sp500:
    source: SEC EDGAR + Yahoo Finance
    exclude_sectors: [commercial-banks, life-insurance, property-casualty]
    exclude_if: market_cap < 500M
  eu-broad:
    source: Financial Modeling Prep
    exclude_sectors: []
    exclude_if: market_cap < 100M

circle_of_competence:
  understood: [software, consumer-staples, insurance-brokers,
               specialty-retail, industrials]
  avoid: [biotech-pre-revenue, chinese-vi, spacs, crypto-related,
          mining-exploration]
```

Companies in "avoid" sectors never enter the pipeline. Buffett: "We have
to stay within our circle of competence. Knowing its boundary is vital."
Suggi maintains this file as his understanding evolves. The "too hard"
pile is a feature, not a failure.

### Phase A: Screening (Deterministic -- Python, No LLM)

#### Stage 0.5: Data Quality Validation

**Source: Ava v2. Link did not address data quality.**

Before any ranking, validate the dataset:

- Negative enterprise values: flag as possible data error or net-cash company
- Missing data fields: exclude from ranking, flag for investigation
- Stale data: >90 days since last reported period
- Extreme outliers: >5 standard deviations from sector median
- Restated financials: flag for extra scrutiny
- Survivorship bias: document as known limitation (delisted companies excluded)

Output: clean, validated dataset with quality flags per company. If >20% of
fields are missing, HALT -- do not proceed with bad data.

#### Stage 1: Sector-Aware Composite Ranking with Owner Earnings

**Source: Ava v2 (sector metrics) + Link G2 (owner earnings).**

Different sectors require different metrics. A one-size-fits-all ranking
misprices banks, SaaS companies, REITs, and insurers.

| Sector | Growth Metric | Quality Metric | Cheapness Metric |
|:--|:--|:--|:--|
| Industrial/Consumer | Revenue CAGR (5-10yr) | ROIC | EV/EBIT |
| Financial (Banks) | Book Value Growth | ROE | P/B |
| Financial (Insurance) | Premium Growth | Combined Ratio | P/B |
| Technology (SaaS) | Revenue CAGR | Rule of 40 (Rev Growth + FCF Margin) | EV/Revenue |
| REITs | FFO/Share Growth | ROE | P/FFO |
| Energy/Materials | Production Volume Growth | ROCE | EV/EBITDA |
| Healthcare (Pharma) | Revenue CAGR | ROIC | EV/EBIT |
| Default | Revenue CAGR | ROIC | EV/EBIT |

**Owner earnings normalization (Link G2):**

Buffett's preferred metric: owner earnings = net income + depreciation
- average annual maintenance capex. Maintenance capex is estimated as:
(average capex/depreciation ratio over 5 years) * current depreciation.
This replaces raw FCF in the cheapness calculation. Using raw capex
overstates capital requirements of asset-light businesses and understates
them for asset-heavy ones.

Composite ranking weights (unchanged):
- Growth: 25% (percentile rank within sector)
- Quality: 25%
- Cheapness: 50% (using owner-earnings-normalized metric)

Composite = 0.25 * growth_rank + 0.25 * quality_rank + 0.50 *
cheapness_rank. Sort ascending. Deterministic. Pure math. No LLM.

#### Stage 2: Broad Screen + Wonderful Business Check

**Source: Ava v2 (thresholds) + Link G6 (wonderful business heuristic).**

Walk the ranked list 1-by-1. A company must meet BOTH thresholds:
- CAGR growth >= 10% over 5-10 years (sector-appropriate metric)
- ROIC >= 15% and/or ROE >= 15% (sector-appropriate metric)

For MVP: tightened thresholds (CAGR >= 15%, ROIC >= 20%) reduce candidates
to 20-50.

**Wonderful business at fair price check (Link G6):**

After threshold filtering, for each remaining company, run a heuristic:

1. Revenue growth in 7+ of the last 10 years? (No = cyclical/unreliable)
2. Gross margin stable or expanding over 5 years? (Declining = competitive
   pressure, likely not wonderful)
3. ROIC >= cost of capital by 500+ bps over 5 years? (No = destroys value
   despite accounting profits)

Companies failing any check are flagged "statistically cheap but possibly
not wonderful" -- they proceed to Stage 3 with a warning tag that the
deep-dive agent must specifically investigate.

Greenblatt's formula finds statistically cheap stocks. Buffett/Munger want
wonderful businesses at fair prices. This heuristic bridges the gap.

### Phase B: Triage (Agentic -- Sequential, Decorrelated)

#### Stage 3: Exclusion Filtering + Moat + Management Scoring

**Source: Both proposals, merged scoring systems.**

For each company surviving Stage 2, evaluate against explicit criteria.
Deterministic where possible, agentic where judgment is required.

**3A. Deterministic exclusions (auto-DISCARD, no agent):**

- P/E > 40, P/S > 5, P/FCF > 30, P/EBIT > 25 (configurable)
- Debt/EBITDA > 4x (or > 3x for cyclicals)
- Debt/Equity > 1.5 (use regulatory capital ratios for financials)
- Negative free cash flow for 3+ consecutive years
- Market cap < $50M (micro-cap liquidity risk)
- Current ratio < 1.0 (liquidity red flag, from Link)

**3B. Moat Scoring (agent judgment -- researcher-1):**

Uses the expanded 6-source moat framework (Ava: added scale-economies-shared
to Morningstar's 5 sources) with Link's 4-dimension durability scoring:

| Dimension | Score (1-5) | Weight |
|-----------|-------------|--------|
| Source clarity (which of 6 sources) | 1-5 | 20% |
| Width (narrow = 1-2, wide = 4-5) | 1-5 | 30% |
| Threat horizon (1-3yr = 1, 5-10yr = 3, 10yr+ = 5) | 1-5 | 25% |
| Trend (narrowing = 1, stable = 3, widening = 5) | 1-5 | 25% |

Moat score < 3.0 = DISCARD (unless exceptional management compensates --
rare, requires specific evidence).

**3C. Management Scoring (agent judgment -- researcher-2):**

Structured rubric with Pabrai's ownership mindset criteria:

| Dimension | Score (1-5) | Weight |
|-----------|-------------|--------|
| Insider ownership (0% = 1, >20% = 5) | 1-5 | 25% |
| Buyback quality (dilution = 1, opportunistic = 5) | 1-5 | 20% |
| Acquisition track record (overpaying = 1, disciplined = 5) | 1-5 | 20% |
| Shareholder communication (opaque = 1, candid = 5) | 1-5 | 15% |
| Capital allocation (empire-building = 1, returns-focused = 5) | 1-5 | 20% |

Management score < 3.0 = DISCARD.

**3D. Cheap-and-good vs cheap-because-bad triage:**

The critical triage. Both researchers produce independent verdicts:
- PASS: Genuinely out of favor, business quality intact
- WATCHLIST: Good business but too expensive right now
- DISCARD: Correctly cheap for structural reasons

Agent must cite specific evidence for why the cheapness is temporary
(cyclical, sentiment, overreaction) vs structural (declining industry,
lost moat, poor management). Every claim requires a source URL.

**3E. Structured Debate Protocol:**

When researchers disagree on PASS/DISCARD: each produces a rebuttal
addressing the other's evidence. Maximum 2 debate rounds. If consensus
is not reached, escalate to Suggi with both analyses and specific
points of disagreement. Document in investing.log.

Output per company: PASS (proceed to Phase C), WATCHLIST (to Phase E
monitoring), or DISCARD (with structured reason).

### Phase C: Deep Analysis (Agentic -- Decorrelated, Parallel)

#### Stage 4: Deep Dive (Parallel Fan-Out)

**Source: Both proposals. Ava added sentiment dimension.**

For each PASS company, two independent analyses run in parallel:

**4A. Moat & Competitive Dynamics (researcher-1):**

- Full moat durability assessment (6-source framework + 4-dimension scoring)
- Industry competitive positioning (Porter's Five Forces, market share trends)
- Customer value proposition analysis
- Threat horizon: how many years of protected returns remain?
- Competitor benchmarking (top 3-5 by market share, margins, growth, ROC)
- **Destination analysis (Sleep/Zakaria):** Project the business 10+ years
  forward. What will it look like? Will its moat be wider or narrower? What
  must go right (and wrong) for the favourable destination to materialize?

**4B. Financial Health & Red Flags (researcher-2):**

- Normalized earnings (adjusting for unusual items, cycles)
- Free cash flow conversion quality (FCF/Net Income, 5-year trend)
- Debt structure analysis (maturity ladder, fixed vs floating, covenants)
- Return on incremental invested capital
- **Structured red flag scan:**
  - Earnings quality: growing DSO, DSI divergence, aggressive revenue
    recognition, serial "one-time" charges
  - Balance sheet: goodwill > 50% of assets, off-balance-sheet items,
    pension underfunding
  - Cash flow: persistent gap between reported earnings and FCF
  - Governance: related-party transactions, dual-class shares with poor
    alignment, frequent auditor changes
  - **Munger psychology flags (Link):** promotional management language,
    excessive M&A ("empire building"), serial restructuring charges

**4C. Sentiment & Market Context (researcher-2):**

**Source: Ava v2. Link did not include sentiment dimension.**

- News sentiment analysis (12 months of major news, analyst rating changes)
- Insider transaction patterns (significant buying = positive, selling = red flag)
- Short interest and trend
- Institutional ownership trends
- Earnings surprise history
- Market narrative: what story is the market telling, and is it accurate?

Disagreement resolution: same debate protocol as Stage 3E.

#### Stage 5: Conviction Check -- Three Questions

**Source: Link G6/Stage 4.5. Ava had destination analysis in Stage 4A
but no clean conviction gate before valuation.**

Before expensive valuation, three questions adapted from Sleep, Pabrai,
and Munger. Only companies passing all three proceed to valuation.

1. **Destination question (Nick Sleep):** "Can I describe what this
   business looks like in 5-10 years with reasonable confidence?" If no,
   move to WATCHLIST -- wait for more clarity. Do not waste a DCF on an
   unknowable destination.

2. **Fat pitch question (Pabrai):** "Is this a no-brainer? Would I bet
   heavily on this outcome?" If the answer requires complex justification,
   it is not a fat pitch. Move to WATCHLIST.

3. **Munger inversion question:** "What is the single worst thing that
   could happen to this business, and how likely is it?" If likelihood
   > 20% and impact is catastrophic (permanent capital loss), DISCARD.

This gate is lightweight (no LLM-heavy DCF) but powerful -- it catches
the most common value investing failure: spending hours modeling a
company you should have discarded in 15 minutes.

#### Stage 6: Investment Thesis Formulation

**Source: Ava v2. Link did not formalize thesis stage.**

Before valuation, crystallize why this company might be a good investment
in 3-5 testable pillars. Each pillar:

- **Specific:** "Company X will grow revenue at 8%+ CAGR for 5 years
  because product Y is gaining share in growing market Z."
- **Falsifiable:** A future data point that would disprove it. "If market
  Z growth drops below 3%, this pillar breaks."
- **Monitored:** Maps to a metric with update cadence.

The thesis also includes:

- **Key risks** with impact pathways (not generic disclaimers)
- **Catalysts** to monitor (product launches, regulatory decisions,
  earnings inflection points, potential spinoffs)
- **Variant perception:** What does the market believe that we believe is
  wrong? Without variant perception, there is no edge. If you cannot
  articulate what you see that the market misses, you should not invest.

### Phase D: Decision (Valuation + Synthesis)

#### Stage 7: Valuation + Position Sizing

**Source: Both proposals, merged. Ava's sector-specific valuation + Link's
position sizing with conviction increments.**

**7A. DCF Model (Investor agent):**

- Bull/Base/Bear scenarios with explicit assumptions
- Revenue growth path, margin path, reinvestment assumptions, terminal
  growth rate
- Sector-appropriate methodology (auto-selected):
  - Generic: 2-stage DCF (5-year explicit + terminal value)
  - SaaS: revenue-based DCF with churn/CAC/LTV parameters
  - REIT: FFO/AFFO multiple + NAV
  - Bank: excess returns model (ROE - COE * Book Value)
  - Insurance: combined ratio + float value + investment portfolio
  - Energy/Materials: cycle-normalized earnings + reserve valuation

**7B. Earnings Power Value (EPV):**

Cross-check against DCF. EPV = Adjusted Earnings / Cost of Capital (no
growth assumption). This is the "no-growth floor" -- if the stock trades
below EPV, growth comes free. Significant divergence from DCF requires
explanation.

**7C. Multiple-Based Sanity Check:**

Compare current multiples against 5-year historical range and industry
peers. Does the multiple narrative match the fundamental narrative?

**7D. Margin of Safety Calculation:**

- Intrinsic value range (bull-base-bear weighted, base case highest weight)
- MOS = 1 - (Market Price / Intrinsic Value Base Case)
- Classification:
  - MOS >= 30%: BUY CANDIDATE
  - MOS >= 20% and < 30%: WATCHLIST
  - MOS < 20% but strong moat: WATCHLIST

**7E. Position Sizing (Link G5):**

Finding cheap stocks is one problem. Deciding how much capital to allocate
is a separate, harder problem. Munger: "The wise bet heavily when the world
gives them the opportunity."

Pabrai's Quarter-Kelly framework:

| Factor | Adjustment |
|--------|-----------|
| MOS >= 50% | +1 position increment |
| MOS 30-50% | Baseline |
| MOS < 30% | WATCHLIST (do not buy) |
| Moat score >= 4.0 | +1 increment |
| Management score >= 4.0 | +1 increment |
| "Fat pitch" confidence = high | +1 increment |
| Circle of competence: deeply understood | +1 increment |
| Circle of competence: adequate | Baseline |
| Circle of competence: marginal | DISCARD (should not reach this stage) |

Base position = X% of portfolio (configurable, default 5%). Each +1
increment adds 2.5%. Maximum single position: 15% (hard cap, Sleep/Zakaria
limit). Maximum sector exposure: 30%.

Position sizing is a recommendation, not an execution. Suggi decides.

#### Stage 8: Investment Checklist Gate

**Source: Ava v2 (9-item checklist). Link proposed similar in management
scoring section but not as standalone gate.**

Before any BUY CANDIDATE classification is finalized, the full checklist
synthesizes Pabrai's 7 questions with Buffett/Munger/Sleep criteria:

- [ ] **Circle of competence:** Can I describe this business's destination
  10 years out? If not, TOO HARD.
- [ ] **Durable moat:** Is the competitive advantage widening, stable, or
  narrowing? Evidence from Stage 4A.
- [ ] **Able and honest management:** Skin in the game? Intelligent capital
  allocation? Candor in communication? Evidence from Stage 3C.
- [ ] **Strong balance sheet:** Can it survive a 2-year recession without
  raising capital? Evidence from Stage 4B.
- [ ] **Simple and predictable:** Can a reasonably intelligent person
  understand this in 30 minutes? If not, flag complexity premium.
- [ ] **Favourable destination:** Where is this business in 10+ years?
  Evidence from Stage 4A destination analysis.
- [ ] **Margin of safety >= 30%:** From Stage 7D. Below threshold =
  WATCHLIST regardless of quality.
- [ ] **No fatal red flags:** Any Stage 4B red flags that are dealbreakers?
- [ ] **Patience check:** Is this the best available opportunity RIGHT NOW,
  or am I buying because I am bored? If forced, HALT.

Every answer MUST cite evidence from Stages 3-7. A "yes" without evidence
is a FAIL. This is the final gate before BUY CANDIDATE.

### Phase E: Compounding & Monitoring

#### Stage 9: Knowledge Compounding

**Source: Both proposals, convergent.**

Write outputs to the agentic-brain. Every artifact is structured,
searchable, and cross-referenced:

- `investing/watchlist.md`: Tiered list (BUY CANDIDATES, WATCH, MONITOR)
  with price, IV range, MOS, thesis summary, last updated date
- `investing/companies/{TICKER}.md`: Full deep-dive with moat, financials,
  management, thesis, DCF, EPV, MOS, risks, catalysts, sentiment, citations
- `investing/theses/{TICKER}-thesis.md`: Condensed 1-page thesis with
  testable pillars and falsification conditions
- Library topic: only if genuinely novel industry/competitive insight
  emerges (do not dilute the library with boilerplate)
- IOR reflection: durable investment insight from the analysis
- `investing.log`: Full analysis record with all stage outputs, agent
  verdicts, debate resolution, and final classification
- Brain-index rebuilt

#### Stage 10: Continuous Monitoring + Post-Mortem Loop

**Source: Ava v2 (monitoring infrastructure) + Link G8/G10 (staleness
tracking + post-mortem).**

**10A. Watchlist Price Monitoring (automated, weekly):**

- Recalculate MOS for all watchlist entries against current prices
- If MOS crosses >= 30% threshold: flag for Suggi review
- If MOS drops below 10%: flag for thesis re-evaluation
- Deterministic. No LLM.

**10B. Quarterly Earnings Review (per company, when earnings release):**

- Fetch latest 10-Q/10-K
- Recalculate key metrics
- Check against thesis pillars: is each pillar still intact?
- Update MOS with latest financials
- Agent produces 1-page earnings update note appended to company file

**10C. Event-Triggered Reviews:**

- Significant insider buying/selling (>$500K large cap, >$100K small cap)
- Major M&A announcement
- Regulatory action or investigation
- Management change (CEO/CFO departure)
- Thesis-breaking news
- Agent scans weekly for trigger events

**10D. Analysis Staleness Tracking (Link G8):**

Every company analysis carries a freshness timestamp. Staleness rules:

- DCF > 3 months old: flag for re-evaluation at next earnings release
- DCF > 6 months old: mark as STALE; do not reference MOS without recalculating
- Earnings release occurred since last analysis: trigger re-analysis
- CEO/CFO departure since last analysis: trigger management re-assessment
- Archived after 12 months if company is not held

This prevents the pipeline from accumulating stale analyses that agents
confidently reference as if current.

**10E. Post-Mortem Loop (Link G10):**

For every BUY CANDIDATE that Suggi acted on, schedule a quarterly review
comparing actual business performance vs the investment memo's assumptions:

- Was revenue growth on track? If not, why?
- Did the moat widen, hold, or narrow? If narrowed, what was missed?
- Were there red flags the pipeline should have caught?
- Did management perform as assessed?

Write findings to `investing/post-mortems/{TICKER}-{date}.md`.

**Critical (R5 applied to investing):** If a pattern emerges across
multiple post-mortems (e.g., "3 of 5 failures had deteriorating gross
margins that the pipeline missed"), add a new gate to Stage 2, 3, or 4.
Every significant error must produce a structural improvement in a
pipeline gate. This is the same R5 principle that governs agent operations
applied to investing: "Would the ORIGINAL failure have been prevented by
this fix?" If no, the fix is incomplete.

Munger: "It is remarkable how much long-term advantage people have gotten
by trying to be consistently not stupid, instead of trying to be very
intelligent."

### Meta-Capabilities (Cross-Stage)

#### M1: Cycle Awareness Monitor

**Source: Link G7. Ava did not address this.**

Greenblatt himself warned the Magic Formula underperforms in certain
cycles (2008-2009, strong bull markets). The pipeline must track when
the strategy is working vs not:

- Spread between cheapest and most expensive decile in the universe
- Value factor performance vs growth factor
- Hit rate of BUY CANDIDATE -> actual outperformance
- Average MOS across the screened universe (wide = opportunity, narrow = caution)

A quarterly cycle health report informs Suggi whether the current
environment favors the strategy. This does not override buy decisions
but provides context: a BUY CANDIDATE during unfavorable cycles demands
higher conviction.

Greenblatt: "The strategy doesn't work every year. In fact, it doesn't
work about one out of every three or four years. The average person
abandons a strategy after a year or two of underperformance."

#### M2: Reverse-Screening Mode

**Source: Link G9. Ava did not address this.**

Nick Sleep's approach was the inverse of screening: start with businesses
you understand deeply from first principles, then wait for them to become
cheap. The pipeline currently supports "screen -> evaluate" (broad to
narrow). It must also support "watchlist -> re-evaluate" (narrow to
narrower).

Suggi's manual approach places good-but-expensive companies on the
watchlist. The pipeline must periodically re-evaluate watchlist companies
against current prices to catch fat pitches. This runs as part of Job 4
(watchlist maintenance) but is a distinct operational mode: seeking
opportunity in the known, not the unknown.

---

## Job Architecture -- 5 Independent Jobs

**Source: Both proposals (both arrived at 4 jobs independently). Merged
into 5 with cycle monitor separated.**

Loose coupling with clear handoffs. Each job has independent failure
boundaries.

### Job 1: Data Pipeline

| Attribute | Value |
|:--|:--|
| **Owner** | investor |
| **Schedule** | Weekly (Saturdays 06:00 UTC) |
| **Type** | Python script. No LLM. |
| **Stages** | 0 (universe), 0.5 (data quality), 1 (ranking), 2 (broad screen) |
| **Input** | `investing/universe.yaml` + financial data APIs |
| **Output** | `investing/data/ranking-YYYY-MM-DD.csv` |
| **Cost** | $0 (no LLM). Data API cost only. |
| **Dependencies** | None |

Data pull, quality validation, sector classification, owner-earnings-
normalized composite ranking, broad screen thresholds, wonderful business
heuristic. Pure Python. No LLM calls. No agent spawns. If it fails, it's
a data API issue or a code bug -- both debuggable without an agent.

### Job 2: Screening + Triage

| Attribute | Value |
|:--|:--|
| **Owner** | main |
| **Schedule** | Monthly (first Sunday 12:00 UTC, after Job 1) |
| **Type** | LLM-driven orchestrator |
| **Stages** | 3 (exclusion + moat + management scoring) |
| **Input** | Latest `ranking-*.csv` from Job 1 (with freshness check) |
| **Output** | `investing/screens/screen-YYYY-MM-DD.md` |
| **Cost** | ~$10-30/cycle |
| **Dependencies** | Job 1 must complete first. `context_from` chains them. |

Main agent as orchestrator. Spawns researcher-1 and researcher-2 as
leaf workers for each company's moat/management assessment. Decorrelated:
both evaluate independently; discrepancies trigger debate protocol.

Batching for full scale: process top-N by rank. First batch = top 25.
If sufficient BUY CANDIDATES emerge (3-5+), pause remaining. If
insufficient, continue next batch.

### Job 3: Deep Analysis + Valuation

| Attribute | Value |
|:--|:--|
| **Owner** | main |
| **Schedule** | On-demand. Triggered when Job 2 produces PASS candidates. |
| **Type** | LLM-driven orchestrator |
| **Stages** | 4 (deep dive), 5 (conviction check), 6 (thesis), 7 (valuation + sizing), 8 (checklist) |
| **Input** | PASS company tickers from Job 2 output |
| **Output** | `investing/companies/{TICKER}.md` |
| **Cost** | ~$1-3/company |
| **Dependencies** | Job 2 must complete first |

Not a cron job -- triggered by Job 2 results. Also invocable manually
by Suggi for single-ticker mode ("Analyze {TICKER}"). Deep dives are
expensive; only run on survivors. Semi-automated: Job 2 flags PASS
candidates; Suggi reviews and triggers Job 3 selectively.

### Job 4: Watchlist + Monitoring

| Attribute | Value |
|:--|:--|
| **Owner** | investor |
| **Schedule** | Weekly (Mondays 08:00 UTC) |
| **Type** | Python + light LLM |
| **Stages** | 10A-10D (monitoring + staleness + reverse-screening) |
| **Input** | `investing/watchlist.md` |
| **Output** | Updated watchlist with freshness timestamps, price alerts, re-analysis flags |
| **Cost** | ~$0.50-1.00/week |
| **Dependencies** | Independent of Jobs 1-3 |

Price movements happen daily. Staleness accumulates weekly. Reverse-
screening mode: if a watchlist company's price drops 20%+ since last
analysis, flag for re-evaluation.

### Job 5: Cycle Monitor + Post-Mortem

| Attribute | Value |
|:--|:--|
| **Owner** | investor |
| **Schedule** | Quarterly |
| **Type** | Python + LLM |
| **Stages** | M1 (cycle awareness), 10E (post-mortem analysis) |
| **Input** | Market data + `investing/post-mortems/` history + pipeline run history |
| **Output** | Cycle health report + error pattern summary + proposed gate updates |
| **Cost** | ~$1-2/quarter |
| **Dependencies** | Reads outputs from Jobs 1-4 |

Not MVP. Build after 2-3 quarters of pipeline operation when there are
actual post-mortems and cycle data to analyze.

### Job Dependency Graph

```
[Job 1: Data Pipeline] --weekly-->
    [Job 2: Screening + Triage] --monthly, after Job 1-->
        [Job 3: Deep Analysis + Valuation] --on-demand, per PASS candidate-->
            [investing/companies/{TICKER}.md]

[Job 4: Watchlist + Monitoring] --weekly, independent-->

[Job 5: Cycle Monitor + Post-Mortem] --quarterly, reads all outputs-->
```

Jobs 1 and 4 run independently. Job 2 depends on Job 1. Job 3 depends on
Job 2. Job 4 runs on its own schedule. Job 5 reads from all.

### Execution Model

**Full Screen Cycle (cron, quarterly):** Jobs 1 -> 2 -> 3 run as coordinated
pipeline. Output written to brain. Suggi reviews BUY CANDIDATE outputs.

**Single-Ticker Mode (on-demand):** Suggi asks "Analyze {TICKER}." Pipeline
starts at Stage 3, using API-fetched data. All subsequent stages run.

**Watchlist Maintenance (cron, weekly):** Job 4 only. Updates MOS, flags
threshold crossings, runs reverse-screening.

---

## Impact

### Positive

- **Coverage:** 3,500 -> 20-200 candidates (deterministic) -> 5-15 deep
  dives (agentic) per cycle. Systematic where Suggi is currently manual.
- **Philosophical alignment:** Every stage maps to a specific value
  investor's framework. The "too hard" pile, owner earnings, wonderful
  business filter, moat durability scoring, management quality scoring,
  destination analysis, fat pitch check, Munger inversion, and
  post-mortem loop are not abstract "best practices" -- they are what
  Buffett, Munger, Greenblatt, Pabrai, and Sleep actually did.
- **Operational completeness:** Sector-specific metrics prevent
  miscategorization. Data quality validation prevents garbage-in.
  Sentiment analysis captures what fundamentals miss. Thesis formulation
  with variant perception identifies edge. Continuous monitoring catches
  deterioration before it compounds.
- **Error feedback loop:** The post-mortem loop (R5 applied to investing)
  means the pipeline gets structurally better with every mistake. This
  is the single most important feature for long-term compounding.
- **Decorrelation payoff:** Two independent agent perspectives cross-check
  at triage and deep dive. Structured debate resolves or escalates
  disagreements.
- **Compounding:** Every analysis enriches the brain. Industry patterns
  accumulate. Knowledge compounds across cycles.
- **Patience enforcement:** Most cycles should produce ZERO new buys.
  This is a feature, not a failure.

### Risk

- **Hallucination in qualitative stages:** Mitigations: (a) every claim
  requires source URL, (b) structured debate protocol, (c) checklist gate
  requires evidence, (d) Suggi reviews all BUY CANDIDATE outputs, (e) TOO
  HARD classification is explicit escape hatch.
- **API data quality:** Mitigations: (a) Stage 0.5 data quality validation,
  (b) cross-check key metrics against two sources for top-ranked companies,
  (c) start with SEC EDGAR (US, high-quality, free) for pilot.
- **Pipeline complexity:** 10 stages, 5 jobs. Mitigations: (a) deterministic
  stages independent of agentic stages, (b) each job has independent failure
  boundaries, (c) single-ticker mode bypasses full pipeline, (d) test each
  stage in isolation before chaining.
- **Survivorship bias:** Mitigation: document as known limitation. Use
  point-in-time data where available. Do not claim "historical performance."
- **Job chain failure:** If Job 1 fails, Job 2 runs on stale data. Mitigation:
  Job 2 verifies ranking data timestamp before proceeding. HALT on stale data.
- **Scoring subjectivity:** Moats and management quality are inherently
  qualitative. Mitigation: scores are diagnostic, not decision-makers.
  Decorrelated agents + evidence requirements. Suggi's judgment is final.

### Cost

- **Data API:** $0 (US pilot, SEC EDGAR). ~$30/month (EU, Financial
  Modeling Prep or EODHD).
- **LLM tokens:** ~$25-75 per quarterly cycle (20-30 PASS companies).
  At full scale: ~$80-250/cycle, mitigated by batching.
- **Implementation:** Phase 1 (MVP, 2-4 weeks): single-ticker pipeline +
  US screening script. Phase 2 (2-4 weeks): cron automation + EU data.
  Phase 3 (ongoing): cycle monitor + post-mortem + optimization.
- **Maintenance:** Low. Uses existing agent infrastructure. No new
  services, repos, or deployment complexity.

---

## Implementation Roadmap

### Phase 1: MVP (2-4 weeks)

1. Python screening script (Stages 0-2) for S&P 500 pilot
2. `investing/universe.yaml` with circle-of-competence definition
3. `investing/` directory structure in the brain
4. Single-ticker deep-dive pipeline (Stages 3-8) tested on 3 known tickers
5. Investment checklist gate
6. Knowledge compounding outputs

**Validation:** Produce complete analyses for 3 test tickers (e.g., AAPL,
JNJ, BRK.B). Submit for Suggi review. Iterate.

### Phase 2: Automation (2-4 weeks)

1. Cron job architecture (Jobs 1-4, Job 5 deferred)
2. EU data API integration
3. Watchlist monitoring (Stage 10A-10D)
4. Reverse-screening mode (M2)
5. Pipeline skill document

### Phase 3: Optimization (ongoing)

1. Cycle monitor + post-mortem loop (Job 5)
2. Evaluation harness for pipeline accuracy
3. Sector-specific refinements
4. Debate protocol tuning based on real disagreements

---

## Open Questions

1. **Data API choice:** Financial Modeling Prep ($29/month) vs EODHD
   ($30/month) vs Alpha Vantage (free tier, 25 req/day). Which has best
   EU small/mid-cap coverage?

2. **MVP ticker selection:** Which 3 known tickers for Phase 1 validation?
   Recommendation: one wide-moat compounder (e.g., MSFT or V), one
   cyclical/out-of-favor (e.g., auto or energy), one "too hard" test
   case (e.g., a bank or biotech Suggi would exclude).

3. **Cron schedule:** Quarterly (aligned with earnings: Feb, May, Aug,
   Nov) or monthly? Quarterly matches data refresh cycle. Monthly
   provides faster idea flow but risks analyzing stale financials.
   Recommendation: quarterly for full screen.

4. **Screening thresholds:** MVP uses tightened (CAGR >= 15%, ROIC >= 20%).
   Should these be configurable via `investing/config/screening-thresholds.json`
   or hardcoded? Recommendation: brain file for easy adjustment per
   market cycle.

5. **Position sizing calibration:** Base position 5%? Max 15%? These
   are reasonable defaults but should be tuned against Suggi's actual
   portfolio.

6. **Should Job 3 be fully automated?** Deep dives are expensive and
   high-stakes. Recommendation: semi-automated. Job 2 flags PASS
   candidates. Suggi reviews and triggers Job 3 selectively.

7. **Classic Magic Formula calibration:** Should the pipeline also run
   the classic Greenblatt formula (ROC + Earnings Yield only, no growth
   weight) as a calibration check? This would help identify when the
   growth factor is driving results vs the value factor.

8. **Phase ordering of philosophical additions:** Link's G1 (too hard)
   and G3 (moat scoring) in Phase 1. G2 (owner earnings), G4 (management),
   G5 (position sizing) in Phase 2. G6-G10 in Phase 3. Confirm priority.

---

## Approval Gate

If approved, I will:

1. Build Phase 1 (MVP):
   - Python screening script with sector-specific metrics, owner earnings
     normalization, and data quality validation
   - `investing/universe.yaml` with circle-of-competence definition
   - Single-ticker pipeline (Stages 3-8) tested on 3 known tickers
   - Investment checklist gate
   - Create `investing/` directory structure in the brain
   - Write `investing-pipeline` skill documenting the full procedure

2. Validate: Produce complete analyses for 3 test tickers. Submit for
   Suggi review. Iterate based on feedback.

3. Build Phase 2 (after Phase 1 validation):
   - 5-job cron architecture
   - EU data API integration
   - Watchlist monitoring + reverse-screening mode
   - Full pipeline automation

4. Defer Phase 3 until 2-3 quarters of pipeline operation produce
   sufficient data for cycle analysis and post-mortems.

---

## Cross-Links

- `governance/suggi-investment-approach.md` -- methodology this pipeline implements
- `investing/pipeline/investment-pipeline-architecture.md` -- Ava v2 (operational foundation)
- `investing/pipeline/link-investment-pipeline.md` -- Link v1 (philosophical foundation)
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- orchestration patterns
- `library/value-investing/anchor-value-investing.md` -- domain anchor
- `library/value-investing/economic-moats.md` -- 6-source moat framework
- `library/value-investing/margin-of-safety.md` -- MOS thresholds
- `library/investors/charlie-munger.md` -- Munger mental models
- `governance/system-constitution.md` -- R5 (root cause fix) applied to post-mortem loop
