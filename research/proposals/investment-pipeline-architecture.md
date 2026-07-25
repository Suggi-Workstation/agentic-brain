---
name: investment-pipeline-architecture
id: 20260725T220248Z
tier: proposal
author: Ava
tags: [value-investing, pipeline, screening, agent-architecture, multi-agent, dcf, moat-analysis, greenblatt, magic-formula]
links:
  - governance/suggi-investment-approach.md
  - library/value-investing/anchor-value-investing.md
  - library/value-investing/economic-moats.md
  - library/value-investing/margin-of-safety.md
---

# Investment Pipeline Architecture -- Automated Value Investing Research Pipeline

## Problem

Suggi has a defined value investing methodology (documented in
`governance/suggi-investment-approach.md`) -- a Greenblatt-style
composite ranking of ~3,500 companies by growth, ROIC, and cheapness,
followed by manual 1-by-1 review to separate genuine bargains from
value traps, with moat analysis, management assessment, and a 30-50%
margin-of-safety threshold before any buy decision. This is currently
a manual process. At 3,500 companies, even a rapid triage takes
weeks per screening cycle. The agent team (Ava + researcher-1 +
researcher-2 + investor) has no structured pipeline to execute this
methodology. The investing/ directory in the agentic-brain is empty.
The library has foundational value-investing knowledge (moats, margin
of safety) but no mechanism to apply it systematically to real
companies.

## Proposed Solution

Build a 6-stage investing pipeline that automates the deterministic
parts of Suggi's methodology and deploys decorrelated agent judgment
where qualitative assessment is required. The pipeline uses our
existing sub-agent architecture: main session as orchestrator,
researcher-1 and researcher-2 for decorrelated analysis, investor
for valuation.

### Stage 0: Data Ingestion

Pull financial data for the target universe (e.g., S&P 500 for US
pilot, ~3,500 EU companies at full scale). Deterministic. No LLM.
Python script calling a financial data API.

Data collected per company: revenue (5-10 years), EBIT/operating
income, FCF, ROIC, ROE, enterprise value, market cap, P/E, P/S,
P/FCF, P/EBIT, total debt, debt/equity, current ratio, insider
ownership percentage.

### Stage 1: Composite Ranking

Rank every company on a Greenblatt-style composite:

- Growth (Operating Income/EBIT, Revenue, or FCF depending on
  sector): 25% weight
- ROIC: 25% weight
- Cheapness (EV/EBIT or MC/EBIT, lower is better): 50% weight

Each factor gets a percentile rank within the universe. Composite =
0.25 * growth_rank + 0.25 * ROIC_rank + 0.50 * cheapness_rank.
Sort ascending. Deterministic. Pure math. No LLM.

### Stage 2: Broad Screen Filtering

Walk the ranked list 1-by-1. A company must meet BOTH:

- CAGR growth >=10% over 5-10 years (revenue growth minimum)
- ROIC >=15% and/or ROE >=15%

Companies meeting both thresholds enter the "broad screen result."
Deterministic threshold checks. No LLM.

Tightening thresholds for MVP (CAGR >=15%, ROIC >=20%) reduces the
result set to 20-50 candidates, keeping agent processing manageable.

### Stage 3: Exclusion Filtering (Agent-Assisted)

For each company in the broad screen result, the agent evaluates:

- **Multiples (deterministic):** Auto-discard if P/E, P/S, P/FCF,
  or P/EBIT exceed configurable thresholds.
- **Debt (deterministic):** Auto-discard if debt/EBITDA >4x or
  debt/equity >1.5.
- **Moat (agent judgment):** Does the company have a clearly
  identifiable moat? Which of the 5 Morningstar sources? How
  durable? The agent must cite specific evidence.
- **Management (agent judgment):** Is management high-quality?
  Do they have skin in the game (insider ownership)? Track record
  of intelligent capital allocation?
- **Cheap-and-good vs cheap-because-bad (agent judgment):** The
  critical triage. Is this company genuinely out of favor, or
  correctly cheap for structural reasons?

Output per company: PASS (to deep dive), WATCHLIST (good but
expensive), or DISCARD (with reason). Decorrelated: researcher-1
and researcher-2 evaluate independently; cross-check disagreements.

### Stage 4: Deep Dive (Decorrelated)

For each PASS company, two independent analyses run in parallel:

- **researcher-1:** Moat durability assessment using the 4-step
  framework from `library/value-investing/economic-moats.md` (identify
  source, verify with financial evidence, assess threat horizon,
  determine width). Industry position. Competitive dynamics.
- **researcher-2:** Financial health deep-dive. Normalized earnings
  (adjusting for unusual items). Free cash flow conversion quality.
  Debt structure analysis. Management capital allocation track
  record (buybacks at what price, acquisitions at what multiple,
  dividend policy). Red flag scan (aggressive revenue recognition,
  growing DSO, frequent restatements).

Disagreements between the two researchers are escalated for
investigation -- this is the decorrelation payoff.

### Stage 5: Valuation and Watchlist Decision

The investor sub-agent produces:

- DCF model with bull/base/bear scenarios, sector-appropriate
  methodology (generic DCF, SaaS Rule of 40, REIT FFO/AFFO, bank
  excess returns model -- auto-selected by industry classification)
- Earnings Power Value as a cross-check
- Intrinsic value range
- Margin of safety vs current market price

Classification:

- MOS >=30%: BUY CANDIDATE -- write full investment memo
- MOS <30% but strong moat: WATCHLIST -- track for price decline
- Fails any exclusion: DISCARD

### Stage 6: Knowledge Compounding

Write outputs to the agentic-brain:

- `investing/watchlist.md`: updated with tiered list (BUY CANDIDATE /
  WATCH / MONITOR)
- `investing/companies/{TICKER}.md`: full deep-dive analysis with
  moat assessment, financial health, DCF, and MOS calculation
- Library topic: if novel industry or competitive insight emerges,
  write to `library/value-investing/` or appropriate domain
- IOR reflection: durable investment insight from the analysis
- Logbook entry: `investing.log` entry recording the analysis
- Brain-index rebuilt for future retrieval

### Agent Instruction Design

Stage 3 agents follow the CFA Institute 5-component instruction format
validated by Anthropic's agent-building research:

1. **Role:** "Value investor, Buffett-Graham-Munger school. Expert in
   moat analysis (Morningstar 5-source framework) and value trap
   detection."
2. **Task:** Specific per-company evaluation with ranking context.
3. **Constraints:** Every moat claim must cite evidence. Flag accounting
   red flags. Auto-DISCARD if debt/EBITDA >4x without justification.
4. **Guidance:** Tool usage order (web_search for moat/management,
   web_fetch for filings, brain-index for prior industry analysis).
5. **Response Format:** Structured JSON with PASS/DISCARD/WATCHLIST
   verdict, moat classification, evidence array with source URLs,
   and 2-3 sentence narrative.

### Execution Model

Two modes:

**Batch Mode (cron-triggered):** Full universe screen on a schedule
(quarterly with earnings, or monthly). Stages 0-2 run as a Python
script. Stages 3-5 process the top-N candidates sequentially. Output
written to brain. Cron job owned by investor sub-agent.

**Single-Ticker Mode (on-demand):** Suggi asks "Analyze {TICKER}."
Pipeline skips Stages 0-2 and starts at Stage 3 (exclusion filtering)
or Stage 4 (deep dive) depending on whether the company was previously
screened.

## Impact

### Positive

- **Coverage:** Systematic triage of 3,500 companies becomes feasible.
  Agent processes 20-50 deep-candidates per cycle rather than Suggi
  manually reviewing hundreds.
- **Consistency:** Every company evaluated against the same criteria
  (moat framework, MOS threshold, exclusion checklist). No fatigue
  bias in the later hours of manual review.
- **Compounding:** Every analysis permanently enriches the brain.
  A company analyzed in Q1 is retrievable in Q3 via brain-index.
  Industry patterns accumulate across analyses.
- **Decorrelation:** Two independent agent perspectives cross-check
  each other, following the same pattern that Suggi designed for
  research quality. The system catches what a single agent would miss.
- **Auditability:** Every decision logged in `investing.log`. Every
  analysis has source citations. MOS calculations are reproducible.

### Risk

- **Hallucination in qualitative stages:** Moat and management
  assessment can produce confident-sounding but incorrect analysis.
  Mitigation: (a) every moat/management claim requires a source URL,
  (b) decorrelated agents must agree, disagreement triggers escalation,
  (c) Suggi reviews all BUY CANDIDATE outputs before any action.
- **API data quality:** Free financial data APIs may have stale or
  incorrect data, producing wrong rankings. Mitigation: cross-check
  key metrics against SEC EDGAR for US stocks; for EU, start with a
  small verified sample before scaling.
- **Over-automation:** The agent could miss qualitative red flags that
  Suggi would catch. Mitigation: the pipeline is a research tool, not
  a trading system. Suggi's review is the final gate. No automated
  execution.
- **Pipeline complexity:** Six stages with multiple sub-agents creates
  failure points. Mitigation: follow Anthropic's principle -- start
  simple, test each stage in isolation before chaining.

### Cost

- **Data API:** $0 for US pilot (SEC EDGAR free). ~$30/month for EU
  data when scaling (Financial Modeling Prep or EODHD).
- **LLM tokens:** ~$0.50-1.50 per deep-dive analysis (VYNN benchmark).
  At 20-50 companies per quarterly cycle: ~$10-75 per cycle.
- **Implementation effort:** ~8-12 hours for MVP (single-ticker
  pipeline + Python ranking script). ~20-30 hours for full pipeline
  with cron automation.
- **Maintenance:** Low. The pipeline uses existing agent infrastructure.
  No new services, no new repos, no deployment complexity.

## Open Questions

1. **Data API choice:** Financial Modeling Prep vs EODHD vs Alpha
   Vantage for EU data. Which has the best coverage of EU small/mid
   caps at the lowest cost tier? Suggi's preference?

2. **MVP scope:** Prove the pipeline on 1-3 known US tickers first
   (single-ticker mode, SEC EDGAR data), or build the screening
   infrastructure first (Stages 0-2) so the agent has candidates
   to analyze? Recommendation: single-ticker MVP first.

3. **Cron schedule:** Quarterly (aligned with earnings seasons) or
   monthly? Quarterly matches the data refresh cycle (new 10-K/10-Q
   filings) and keeps token costs manageable.

4. **Stage 0-2 implementation:** Python script in a new
   `investing/scripts/` directory in the brain, or a skill package
   in the investor workspace? The brain is the natural home since
   the pipeline's output lives there.

5. **Screening thresholds:** The MVP uses tightened thresholds
   (CAGR >=15%, ROIC >=20%) to keep agent processing manageable.
   Should these be configurable (brain file) or hardcoded? Suggi
   may want to adjust them per market cycle.

6. **EU data timing:** When does Suggi want to target EU companies?
   US pilot first lets us validate the methodology with free data.
   EU requires a paid API. Timeline preference?

## Approval Gate

If approved, I will:

1. Write an `investing-pipeline` skill (SKILL.md) documenting the
   6-stage procedure for agent execution.
2. Build the Stage 0-2 Python ranking script using SEC EDGAR + Yahoo
   Finance for a US pilot.
3. Implement the single-ticker deep-dive pipeline (Stages 3-6) as a
   coordinated sub-agent spawn flow, tested on 2-3 known tickers.
4. Create `investing/scripts/`, `investing/companies/`, and initialize
   `investing/watchlist.md` in the brain.
5. Document findings in a spike report and iterate based on Suggi's
   review of the first outputs.

## Cross-Links

- `governance/suggi-investment-approach.md` -- the methodology this
  pipeline implements
- `library/value-investing/anchor-value-investing.md` -- domain anchor
- `library/value-investing/economic-moats.md` -- moat framework used
  in Stage 3-4
- `library/value-investing/margin-of-safety.md` -- MOS threshold used
  in Stage 5
- CFA Institute: Agentic AI for Finance (2025) -- external validation
  of the workflow patterns used (orchestrator-workers, parallelization,
  evaluator-optimizer)
- Anthropic: Building Effective Agents (Dec 2024) -- architectural
  principle: prefer workflows over autonomous agents in high-stakes
  domains
- Agentic-Analyst/stock-analyst (VYNN) -- open-source reference
  implementation of supervisor-worker equity research pipeline with
  3-layer recommendation engine
- AlphaAgents (arXiv:2508.11152) -- multi-agent debate pattern for
  equity analysis, validates our decorrelated agent approach
