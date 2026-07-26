---
name: link-investment-pipeline
id: 20260726T055113Z
tier: proposal
author: Link
tags: [value-investing, pipeline, screening, agent-architecture, multi-agent, buffett, munger, greenblatt, pabrai, magic-formula, job-decomposition]
links:
  - governance/suggi-investment-approach.md
  - research/proposals/investment-pipeline-architecture.md
  - library/coding-agentic-ai/multi-agent-orchestration.md
  - library/value-investing/anchor-value-investing.md
  - library/value-investing/economic-moats.md
  - library/value-investing/margin-of-safety.md
  - library/investors/charlie-munger.md
---

# Link's Investment Pipeline -- Enhanced Architecture for Automated Value Investing

## Problem

Ava's `investment-pipeline-architecture.md` (2026-07-25) proposed a 6-stage
pipeline for Suggi's value investing methodology. It is a strong foundation --
the Greenblatt-style composite ranking, decorrelated deep-dive, and knowledge
compounding stages are correctly identified. But it was written before the
agent orchestration library topic existed (`multi-agent-orchestration.md`,
2026-07-24) and before the Munger library topic was written (2026-07-25).
As a result, three classes of gaps exist:

1. **Philosophical gaps:** The pipeline screens like Greenblatt but evaluates
   like an analyst, not like Buffett/Munger/Pabrai/Sleep. Quantitative ranking
   is necessary but insufficient. Several value-investor-critical stages are
   missing entirely: the "too hard" pile, owner earnings normalization, moat
   durability scoring, management quality scoring, position sizing, and a
   post-mortem error loop. Without these, the pipeline risks finding cheap
   stocks rather than wonderful businesses at fair prices.

2. **Job decomposition gaps:** The proposal describes stages but does not
   specify how many independent cron jobs are needed, what each job's
   boundaries are, or how they compose. The orchestration literature
   (Microsoft, Anthropic, ICLR 2025) is clear: pattern choice is the dominant
   factor in reliability. The pipeline needs explicit job decomposition.

3. **Operational gaps:** No cycle-awareness (when does the strategy work vs
   fail?), no analysis staleness tracking (a 6-month-old DCF is not current),
   no error post-mortem loop (if BUY CANDIDATE declined 40%, why?), and no
   reverse-screening mode (Nick Sleep: start with understood businesses).

## Assessment of Ava's Original Pipeline

### What Works (Keep)

| Stage | What | Why It Works |
|-------|------|-------------|
| 0: Data Ingestion | Python script, no LLM | Deterministic, cheap, reliable. Correct decision. |
| 1: Composite Ranking | Greenblatt-style 25/25/50 | Mirrors Suggi's methodology exactly. Pure math. |
| 2: Broad Screen | CAGR + ROIC thresholds | Deterministic gate. Tightened thresholds for MVP. |
| 3: Exclusion (moat + mgmt) | Agent-assisted triage | Correct to use decorrelated agents here. |
| 4: Deep Dive | Two researchers, parallel | Decorrelation payoff is real. Validated by debate pattern. |
| 5: Valuation + MOS | Investor sub-agent, DCF + EPV | Sector-appropriate methodology. Good. |
| 6: Knowledge Compounding | Brain writes, index rebuild | Essential for compounding across cycles. |
| Single-ticker mode | On-demand analysis | Critical for Suggi's ad-hoc research. |
| CFA 5-component instructions | Role/Task/Constraints/Guidance/Format | Anthropic-validated. Keep exactly. |

### What's Missing (10 Gaps)

#### G1: The "Too Hard" Pile (Buffett)

Buffett's most important decision is not what to buy -- it is what to put in
the "too hard" pile. Complex financials (banks, insurers), businesses with
unpredictable technological disruption, or industries Suggi does not
understand should be explicitly excluded BEFORE any ranking or analysis.
This is a separate stage between data ingestion and ranking, not a
byproduct of exclusion filtering. A company that is "too hard" should never
reach Stage 1.

**Value investor source:** Buffett: "We have to stay within our circle of
competence. We don't have to be an expert on every company. We only have to
be able to evaluate companies within our circle of competence. The size of
that circle is not very important; knowing its boundary, however, is vital."

#### G2: Owner Earnings Normalization (Buffett)

The pipeline uses reported EBIT and FCF. Buffett's preferred metric is
owner earnings: (a) reported earnings + (b) depreciation, depletion,
amortization - (c) average annual maintenance capex. Maintenance capex is
NOT the same as total capex -- it requires estimation. Using raw capex
overstates the capital requirements of asset-light businesses and understates
them for asset-heavy ones. The ranking stage must normalize for this before
calculating cheapness.

**Value investor source:** Buffett's 1986 Berkshire letter: "If we think
through these questions, we can gain some insights about what may be called
'owner earnings.' These represent (a) reported earnings plus (b)
depreciation, depletion, amortization, and certain other non-cash charges
less (c) the average annual amount of capitalized expenditures for plant
and equipment, etc. that the business requires to fully maintain its
long-term competitive position and its unit volume."

#### G3: Moat Durability Scoring (Morningstar + Munger)

The pipeline mentions the 5 Morningstar moat sources but lacks a structured
scoring system. A moat assessment that only says "has a moat" or "no moat"
is too binary. The scoring must address: which of the 5 sources applies,
how wide is the moat (narrow/wide), what is the threat horizon (short-term,
medium-term, long-term), and what is the moat trend (widening, stable,
narrowing). This is Munger's latticework applied: combine Morningstar's
framework with Porter's Five Forces, Christensen's disruption theory, and
industry-specific competitive dynamics.

**Value investor source:** Munger: "We have to have a business with some
moat. We have to have some insight into what gives the business the moat
and how durable it is. The durability of the moat is the key."

#### G4: Management Quality Scoring (Pabrai)

"Skin in the game" is mentioned but unstructured. Pabrai emphasizes a
checklist: insider ownership percentage, share buybacks at attractive
prices (not just any buybacks), acquisition track record (did they
overpay?), candid shareholder letters (do they admit mistakes?), capital
allocation discipline (do they hoard cash when returns are poor or return
it?). This needs a structured scoring rubric with a PASS/HALT threshold,
not free-form judgment.

**Value investor source:** Pabrai: "I want to see managers who treat
the business as if it were their only asset, who think like owners because
they are owners, and who allocate capital as if they're investing their
own family's money."

#### G5: Position Sizing Framework (Munger/Kelly)

Finding cheap stocks is one problem. Deciding how much capital to allocate
is a separate, harder problem. Munger: "The wise bet heavily when the world
gives them the opportunity. The rest of the time, they don't." The pipeline
produces BUY CANDIDATE / WATCHLIST / DISCARD but has no framework for how
much conviction maps to position size. This is a post-valuation stage:
given a company passes all gates with a 40% MOS, strong moat, and excellent
management, what percentage of portfolio does it warrant? This requires
Kelly criterion thinking combined with conviction scoring.

**Value investor source:** Munger: "The idea of excessive diversification
is madness. We're talking about people who don't know what they're doing
trying to reduce risk by buying more and more things they don't understand."

#### G6: The "Wonderful Business at Fair Price" Filter (Buffett Evolution)

Greenblatt's Magic Formula finds statistically cheap stocks -- but many are
cheap for good reason (commodity businesses, secular decline, technological
disruption). Buffett evolved from Graham's "cigar butt" approach (buy any
cheap stock) to Munger's "wonderful business at fair price" approach. The
pipeline needs an explicit filter AFTER ranking that asks: "Is this company
cheap because it is out of favor (cyclical, temporary), or because the
business is structurally declining?" Suggi's manual process does this
intuitively. The pipeline must make it explicit.

**Value investor source:** Buffett: "It's far better to buy a wonderful
company at a fair price than a fair company at a wonderful price."

#### G7: Cycle Awareness and Strategy Monitoring (Greenblatt)

Greenblatt himself warned that the Magic Formula underperforms in certain
cycles (2008-2009, strong bull markets). The pipeline must track when the
strategy is working (cheapness spreads wide) vs not (cheapness spreads
narrow). A meta-monitoring system that tracks: (a) the spread between
cheapest and most expensive decile in the universe, (b) value factor
performance vs growth factor, (c) the hit rate of BUY CANDIDATE -> actual
outperformance. Without this, the pipeline operates blindly across market
regimes.

**Value investor source:** Greenblatt in The Little Book That Still Beats
the Market: "The strategy doesn't work every year. In fact, it doesn't
work about one out of every three or four years. The average person
abandons a strategy after a year or two of underperformance. That's why
most people don't beat the market."

#### G8: Analysis Staleness and Re-Analysis Triggers

A DCF built in Q1 becomes stale by Q3. The watchlist needs freshness
tracking: when was each company last analyzed? What earnings releases have
occurred since? Did any thesis-breaking event occur (CEO departure,
regulatory change, major competitor entry)? A re-analysis trigger system
prevents the pipeline from accumulating stale analyses that agents
confidently reference as if current.

#### G9: Reverse-Screening Mode (Nick Sleep)

Nick Sleep's approach was the inverse of screening: start with businesses
you understand deeply from first principles, then wait for them to become
cheap. The pipeline currently only supports "screen -> evaluate" (broad to
narrow). It should also support "watchlist -> re-evaluate" (narrow to
narrower). Suggi's manual approach places good-but-expensive companies on
the watchlist. The pipeline must periodically re-evaluate watchlist
companies against current prices to catch fat pitches.

**Value investor source:** Nick Sleep's Nomad letters: "We spent most of
our time trying to understand the destination -- what the business would
look like in 5-10 years. Price was secondary. Only when we understood the
destination could we determine whether the current price offered a
sufficient return for the journey."

#### G10: Error Post-Mortem Loop (R5 -- Root Cause Fix)

If the pipeline identifies a company as BUY CANDIDATE with 40% MOS and it
subsequently declines 40%, what went wrong? Was the intrinsic value estimate
wrong? Did a moat erode faster than predicted? Was management worse than
assessed? Without a structured post-mortem, the same error class repeats.
This is R5 applied to investing: every significant error must produce a
structural improvement in a pipeline gate. The post-mortem writes to
`investing/errors.log` and updates the relevant gate threshold.

**Value investor source:** Munger: "It is remarkable how much long-term
advantage people have gotten by trying to be consistently not stupid,
instead of trying to be very intelligent."

## Proposed Solution: Enhanced 7-Stage Pipeline

Add one stage and enhance three existing stages. The pipeline follows the
sequential pipeline pattern (deterministic stages 0-2, the easily
decomposable parts) with a supervisor-worker pattern (stages 3-5, where
agent judgment is required) and an explicit loopback (stage 6 feeds back
into future screening runs).

### Stage 0: Universe Definition + "Too Hard" Exclusion [NEW]

**Before any data is pulled**, define the investable universe and apply the
"too hard" exclusion. This is a config file in the brain:
`investing/universe.yaml`.

```
universes:
  us-sp500:
    source: SEC EDGAR + Yahoo Finance
    exclude_sectors: [commercial-banks, life-insurance, property-casualty]
    exclude_if: market_cap < 500M  # micro-caps
  eu-broad:
    source: Financial Modeling Prep
    exclude_sectors: []
    exclude_if: market_cap < 100M

circle_of_competence:
  understood: [software, consumer-staples, insurance-brokers, specialty-retail, industrials]
  avoid: [biotech-pre-revenue, chinese-vi, spacs, crypto-related, mining-exploration]
```

Circle of competence is explicitly encoded. Companies in "avoid" sectors
never enter the pipeline. Suggi maintains this file as his understanding
evolves.

### Stage 0.5: Data Ingestion [KEPT from Ava's Stage 0]

Same as Ava's proposal. Pull financial data. Deterministic Python script.
Add owner earnings estimation: maintenance capex = average capex/depreciation
ratio over 5 years * current depreciation. This normalizes the cheapness
calculation in Stage 1.

### Stage 1: Composite Ranking with Owner Earnings [ENHANCED]

Same 25/25/50 ranking but with owner-earnings-normalized cheapness:

- Growth: Operating Income and Revenue CAGR, 5-10 years (25%)
- ROIC: NOPAT / Invested Capital, 5-year average (25%)
- Cheapness: EV / Owner Earnings or MC / Owner Earnings (50%)

Owner earnings = (net income + depreciation - avg maintenance capex).
This is deterministic. Pure math. No LLM.

### Stage 2: Broad Screen + Wonderful Business Check [ENHANCED]

Same CAGR + ROIC thresholds, but add the "wonderful business at fair price"
check (G6). After threshold filtering, for each remaining company, run a
heuristic:

1. Has revenue grown in 7+ of the last 10 years?
2. Is gross margin stable or expanding over 5 years? (declining margin =
   competitive pressure, likely not wonderful)
3. Is ROIC >= cost of capital by 500+ bps over 5 years? (if not, the
   business destroys value despite accounting profits)

Companies failing any of these are flagged as "statistically cheap but
possibly not wonderful" -- they proceed to Stage 3 but with a warning
tag that the deep-dive agent must specifically investigate.

### Stage 3: Exclusion Filtering + Moat + Management Scoring [ENHANCED]

Expanded from Ava's Stage 3. Now includes structured scoring:

**Deterministic gates (auto-DISCARD):**
- P/E > 30 or P/FCF > 25 or P/EBIT > 20 (configurable)
- Debt/EBITDA > 4x or Debt/Equity > 1.5
- Current ratio < 1.0 (liquidity red flag)

**Moat Scoring (agent judgment, G3):**

| Dimension | Score (1-5) | Weight |
|-----------|-------------|--------|
| Source clarity (which of 5 Morningstar sources) | 1-5 | 20% |
| Width (narrow = 1-2, wide = 4-5) | 1-5 | 30% |
| Threat horizon (1-3yr = 1, 5-10yr = 3, 10yr+ = 5) | 1-5 | 25% |
| Trend (narrowing = 1, stable = 3, widening = 5) | 1-5 | 25% |

Moat score < 3.0 = DISCARD (unless exceptional management can compensate).

**Management Scoring (agent judgment, G4):**

| Dimension | Score (1-5) | Weight |
|-----------|-------------|--------|
| Insider ownership % (0% = 1, >20% = 5) | 1-5 | 25% |
| Buyback quality (dilution = 1, opportunistic = 5) | 1-5 | 20% |
| Acquisition track record (overpaying = 1, disciplined = 5) | 1-5 | 20% |
| Shareholder communication (opaque = 1, candid = 5) | 1-5 | 15% |
| Capital allocation (empire-building = 1, returns-focused = 5) | 1-5 | 20% |

Management score < 3.0 = DISCARD.

**Cheap-and-good vs cheap-because-bad:** Agent must cite specific evidence
for why the cheapness is temporary (cyclical, sentiment, overreaction) vs
structural (declining industry, lost moat, poor management). This is the
critical G6 triage.

Output: PASS (both scores >= 3.0 + identified as cheap-and-good),
WATCHLIST (strong moat + management but expensive), or DISCARD.

Two decorrelated agents (researcher-1, researcher-2) evaluate independently.
Disagreement on PASS/DISCARD triggers escalation to Suggi or the investor
agent as tiebreaker.

### Stage 4: Deep Dive (Decorrelated) [KEPT]

Same as Ava's proposal. Two researchers in parallel. Excellent design.
Keep exactly.

- Researcher-1: Moat durability + industry position + competitive dynamics
- Researcher-2: Financial health + normalized earnings + capital allocation
  + red flag scan

### Stage 4.5: "Wonderful Business" Conviction Check [NEW]

Before valuation, a synthesis step:

Given the moat score, management score, industry position, and financial
health from Stages 3-4, answer three questions:

1. **Destination question (Nick Sleep):** "Can I describe what this
   business looks like in 5-10 years with reasonable confidence?" If no,
   move to WATCHLIST -- wait for more clarity. Do not proceed to valuation.

2. **Fat pitch question (Pabrai):** "Is this a no-brainer? Would I bet
   heavily on this outcome?" If the answer requires complex justification,
   it is not a fat pitch. Move to WATCHLIST.

3. **Munger inversion question:** "What is the single worst thing that
   could happen to this business, and how likely is it?" If likelihood
   > 20% and impact is catastrophic (permanent capital loss), DISCARD.

Only companies passing all three questions proceed to valuation.

### Stage 5: Valuation + Position Sizing [ENHANCED]

Same DCF/EPV as Ava's proposal, plus:

**Valuation (Investor agent):**
- DCF: bull/base/bear with explicit assumptions
- EPV cross-check
- Intrinsic value range
- MOS vs current price

**Position Sizing (Investor agent, G5):**

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

Base position = X% of portfolio (configurable, e.g., 5%). Each +1 increment
adds 2.5%. Max position = 15% (hard cap). This prevents the pipeline from
identifying great ideas but allocating them identically to mediocre ones.

Output:
- BUY CANDIDATE (MOS >= 30%, full investment memo)
- WATCHLIST (MOS < 30% but strong quality)
- DISCARD
- Suggested position size range

### Stage 6: Knowledge Compounding [KEPT]

Same as Ava's proposal. Write to brain. Rebuild index. Log to
`investing/investing.log`.

### Stage 6.5: Post-Mortem Loop [NEW for G10]

For every BUY CANDIDATE that was actioned (Suggi bought), schedule a
quarterly review. Compare actual business performance vs the investment
memo's assumptions:

- Was revenue growth on track? If not, why?
- Did the moat widen, hold, or narrow? If narrowed, what was missed?
- Were there red flags the pipeline should have caught?

Write findings to `investing/post-mortems/{TICKER}-{date}.md`. If a
pattern emerges across multiple post-mortems (e.g., "3 of 5 failures
had deteriorating gross margins that the pipeline missed"), add a new
gate to Stage 2 or 3. This is R5 in investing form: every error
produces a structural improvement.

## Job Architecture -- How Many Independent Jobs?

Ava's proposal mentions cron triggers but doesn't specify job decomposition.
Based on the orchestration literature's principle of loose coupling with
clear handoffs, the optimal decomposition is **4 independent jobs** plus one
watchdog:

### Job 1: Data Pipeline (cron: weekly, Saturdays 06:00 UTC)

**Type:** Python script (no LLM). `no_agent: true`.
**Stages:** 0 (universe definition), 0.5 (data pull), 1 (ranking).
**Input:** `investing/universe.yaml` + financial data APIs.
**Output:** `investing/data/ranking-YYYY-MM-DD.csv` -- ranked company list
  with composite scores, owner earnings, CAGR, ROIC, and cheapness percentiles.
**Dependencies:** None.
**Cost:** $0 (no LLM). Data API cost only.
**Why separate:** Deterministic. No agent judgment. Should never fail because
  of an LLM hallucination. If it fails, it's a data API issue or a code bug --
  both are debuggable without an agent in the loop.

### Job 2: Screening + Triage Orchestrator (cron: monthly, first Sunday 12:00 UTC)

**Type:** LLM-driven orchestrator. Hermes cron with `attach_to_session: true`.
**Stages:** 2 (broad screen), 3 (exclusion + moat + management scoring).
**Input:** `investing/data/ranking-YYYY-MM-DD.csv` (latest from Job 1 via
  `context_from`).
**Output:** `investing/screens/screen-YYYY-MM-DD.md` -- companies that passed
  Stages 2-3 with moat scores, management scores, and verdicts.
**Dependencies:** Job 1 must complete first (`context_from` chains them).
**Agents:** Main agent as orchestrator. Spawns researcher-1 and researcher-2
  as leaf workers via `delegate_task` for each company's moat/management
  assessment. Decorrelated: both agents evaluate; discrepancies flagged.
**Why monthly:** Aligns with earnings releases. Quarterly might miss
  opportunities; weekly is too frequent for qualitative analysis.
**Cost:** ~$10-30/cycle (20-50 companies * $0.50-1.50 per assessment).

### Job 3: Deep Dive + Valuation (on-demand, triggered by Job 2 output)

**Type:** LLM-driven. Not a cron job -- triggered when Job 2 produces
  PASS candidates. Or invoked manually by Suggi for single-ticker mode.
**Stages:** 4 (deep dive), 4.5 (conviction check), 5 (valuation + sizing).
**Input:** Company tickers from Job 2's output.
**Output:** `investing/companies/{TICKER}.md` -- full investment memo with
  moat assessment, financial health, DCF, MOS, position sizing, and BUY/
  WATCH/DISCARD verdict.
**Agents:** Main agent spawns researcher-1, researcher-2 (parallel deep dive),
  then investor agent (valuation + sizing), then synthesizes.
**Cost:** ~$1-3/company.
**Why on-demand:** Deep dives are expensive. Only run on companies that passed
  all screening gates. Triggers automatically from Job 2 results but can also
  be invoked manually.

### Job 4: Watchlist Maintenance (cron: weekly, Mondays 08:00 UTC)

**Type:** Python + light LLM.
**Stages:** G8 (staleness check), G9 (reverse-screening).
**Input:** `investing/watchlist.md`.
**Output:** Updated watchlist with freshness timestamps, re-analysis flags
  for stale entries, and price-check alerts (if a watchlist company's price
  has dropped 20%+ since last analysis, flag for re-evaluation).
**Cost:** ~$0.50-1.00/week (light LLM for staleness assessment).
**Why weekly:** Price movements happen daily. Staleness accumulates weekly.

### Job 5 (Optional, Future): Cycle Monitor + Post-Mortem (cron: quarterly)

**Type:** Python + LLM.
**Stages:** G7 (cycle awareness), G10 (post-mortem analysis).
**Input:** Market data + `investing/post-mortems/` history.
**Output:** Cycle health report + pipeline error pattern summary.
**Cost:** ~$1-2/quarter.
**Why later:** Not MVP. Build after 2-3 quarters of pipeline operation when
  there are actual post-mortems to analyze.

### Job Dependency Graph

```
[Job 1: Data Pipeline] --weekly-->
    [Job 2: Screening + Triage] --monthly, after Job 1-->
        [Job 3: Deep Dive + Valuation] --on-demand, per PASS candidate-->
            [investing/companies/{TICKER}.md]

[Job 4: Watchlist Maintenance] --weekly, independent of 1-2-3-->

[Job 5: Cycle Monitor] --quarterly, reads post-mortems from 1-2-3-4-->
```

Jobs 1 and 4 run independently. Job 2 depends on Job 1 (via `context_from`).
Job 3 is triggered by Job 2's output. Job 4 runs on its own schedule,
maintaining the watchlist regardless of screening cycles.

## Why 4 Jobs (Not 3, Not 7)

The Anthrophic principle: "Start simple. Add complexity only when a clear
failure mode requires it." Three jobs would combine screening + deep dive,
but that couples deterministic ranking (should never fail for LLM reasons)
with qualitative assessment (intrinsically LLM-dependent). Separating them
means the cheap, fast, deterministic parts (Jobs 1 + 4) run frequently while
the expensive, LLM-intensive parts (Jobs 2 + 3) run less frequently and
only on the most promising candidates.

Seven jobs would factor out moat scoring, management scoring, and valuation
into separate agents. But the handoff overhead and telephone-game risk
(described in `multi-agent-orchestration.md`) argue against this. The
current decomposition keeps pipelines shallow -- max depth of 3 agents for
the qualitative stages, with clear input/output schemas at each handoff.

## Impact

### Positive

- **Philosophical alignment:** The enhanced pipeline doesn't just rank
  stocks by cheapness -- it asks the questions Buffett, Munger, Pabrai,
  Sleep, and Greenblatt would ask. Every stage maps to a specific
  investor's framework.
- **Structured scoring:** Moat and management assessment moves from
  free-form text ("strong moat") to quantitative rubrics that are
  comparable across companies and trackable over time.
- **Error feedback loop:** Post-mortems close the learning loop. The
  pipeline gets structurally better with every mistake -- exactly the
  R5 principle applied to investing.
- **Cycle-aware operation:** The meta-monitoring prevents blind strategy
  execution during unfavorable market regimes.
- **Freshness guarantees:** Stale analyses are flagged, not silently
  trusted.
- **Position sizing:** Conviction maps to capital allocation, not just
  a binary BUY/DON'T BUY.

### Risk

- **Complexity creep:** 10 additional gates on top of Ava's already-
  substantive 6-stage pipeline. Mitigation: build incrementally. Start
  with G1 (too hard pile) and G3 (moat scoring). Add G2 (owner earnings),
  G4 (management), G5 (position sizing) in phase 2. G7-G10 are phase 3.
- **Scoring subjectivity:** Moats and management quality are inherently
  qualitative. A rubric introduces false precision. Mitigation: the
  scores are diagnostic tools, not decision-makers. The final gate is
  Suggi's judgment.
- **Agent hallucination in rubrics:** An agent might confidently assign
  a moat score of 4.5 to a company with no moat. Mitigation:
  decorrelation (two agents) + evidence requirements (every score
  dimension must cite a source URL or financial data point).
- **Job chain failure:** If Job 1 fails, Job 2 runs on stale data.
  Mitigation: `context_from` with freshness check -- Job 2 verifies
  the ranking data timestamp before proceeding.

### Cost

Same order of magnitude as Ava's estimate:
- Data API: $0-$30/month
- LLM tokens: $15-50/month for full pipeline operation
- Implementation: ~15-25 hours for MVP (Phase 1), ~40-60 hours for full
  pipeline
- Maintenance: Low. Jobs are hermetic with clear input/output schemas.

## Open Questions

1. **Phase ordering:** Which gaps should be Phase 1 (MVP) vs deferred?
   Recommendation: G1 (too hard pile) + G3 (moat scoring) + Job
   decomposition in Phase 1. G2, G4, G5 in Phase 2. G6-G10 in Phase 3.

2. **Management scoring data sources:** Where does the agent get insider
   ownership data? SEC EDGAR Form 4 filings. What about buyback quality
   and acquisition track record? Requires web search + 10-K reading.
   How reliable is this at scale?

3. **Moat durability prediction:** Can an LLM actually predict whether a
   moat will widen or narrow over 5-10 years? This is the hardest judgment
   in investing. The scoring rubric provides structure but the forecast
   itself depends on the agent's reasoning quality.

4. **Position sizing calibration:** The suggested formula (base + increments)
   needs backtesting against Suggi's actual portfolio. Should the base
   be 5% or 10%? Should the max be 15% or 25%? These numbers are
   reasonable defaults but should be tuned.

5. **EU data timing:** Same question as Ava's. US pilot first with free
   SEC EDGAR data validates the methodology. EU requires a paid API.
   Same recommendation: US pilot first.

6. **Should Job 3 be fully automated?** Deep dives are expensive and
   high-stakes. Should they auto-trigger from Job 2's output, or should
   Suggi review Job 2's output and manually kick off Job 3 for the
   candidates he's interested in? Recommendation: semi-automated.
   Job 2 flags PASS candidates. Suggi reviews the list and triggers
   Job 3 selectively.

7. **What replaces the Magic Formula?** Suggi's method IS heavily
   Greenblatt-inspired -- the composite ranking is essentially his formula
   with growth added. Should the pipeline also run the classic Magic
   Formula (ROC + Earnings Yield only, no growth weight) as a calibration
   check? This would help identify when the growth factor is driving
   results vs the value factor.

## Approval Gate

If approved, I will:

1. Write an `investing-pipeline-v2` skill documenting the enhanced
   7-stage procedure for agent execution.
2. Build the Phase 1 components: `investing/universe.yaml`, the "too
   hard" exclusion logic in the Stage 0 script, the moat scoring rubric
   in the Stage 3 agent instructions, and the 4-job decomposition with
   Hermes cron configurations.
3. Write a spike report validating moat scoring on 3-5 known companies
   (ones Suggi already has an opinion on) to test whether the rubric
   produces scores that match Suggi's judgment.
4. Coordinate with Ava: her original proposal is the foundation. This
   proposal extends it without replacing it. The `investing-pipeline`
   skill should be versioned (v1 = Ava's, v2 = enhanced).

## Cross-Links

- `governance/suggi-investment-approach.md` -- Suggi's methodology
- `research/proposals/investment-pipeline-architecture.md` -- Ava's
  original proposal (the foundation this extends)
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- orchestration
  patterns that inform the job decomposition
- `library/value-investing/anchor-value-investing.md` -- domain anchor
- `library/value-investing/economic-moats.md` -- moat framework in Stages 3-4
- `library/value-investing/margin-of-safety.md` -- MOS threshold in Stage 5
- `library/investors/charlie-munger.md` -- Munger's mental models applied
  throughout
- `governance/system-constitution.md` -- R5 (root cause fix) applied to
  the post-mortem loop (G10)
