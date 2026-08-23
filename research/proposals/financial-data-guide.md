---
name: financial-data-guide
id: 20260726T211142Z
tier: proposal
author: Ava
tags: [financial-data, data-infrastructure, sec-edgar, eodhd, mcp, openclaw, pipeline-data, bulk-screening]
links:
  - investing-hub:frameworks/sector-specific-metrics.md
  - reflections/2026-07-26_ava_decorrelation-convergence-pipeline.md
---

# Financial Data Infrastructure -- Sourcing Complete Data for 50K+ Stocks

## Problem

The investment pipeline needs comprehensive financial data for 50K+
global stocks to run Stage 0-2 screening (bulk ranking) and Stages 3-7
deep analysis (individual company deep dives). No single API or data
source provides everything at the scale and depth required. The pipeline
cannot function without solved data infrastructure.

The 7 frameworks in `investing-hub:frameworks/` catalog exactly what data is
needed: 10-year revenue history, EBIT, FCF, EV, ROIC, ROE, D/E, sector,
market cap, owner earnings components, sector-specific metrics (FFO for
REITs, combined ratio for insurers, Rule of 40 for SaaS), insider
ownership, share count trends, full financial statements, debt maturity
schedules, competitor financials, and more. This is hundreds of fields
per company. Getting it wrong -- using current P/E for a cyclical, using
EV/EBITDA for a bank, trusting reported earnings without normalization --
produces confident-looking garbage.

## Proposed Solution

A two-tier hybrid architecture: a bulk Python pipeline for mass screening
(free where possible, paid where necessary) plus OpenClaw MCP servers for
agent deep dives.

### Tier 1: Bulk Screening Pipeline (Python, no LLM -- Stages 0-2)

This pulls ALL companies' data at once for the composite ranking and
broad screen. Two data sources:

**US Stocks (~10K tickers): SEC EDGAR -- FREE**

The SEC provides a nightly bulk ZIP of every US public company's full
XBRL financial statements:

- `companyfacts.zip`: all income statement, balance sheet, cash flow
  line items for all filers in standardized US-GAAP JSON
- `submissions.zip`: filing history, CIK-to-ticker mapping, metadata
- No API key. No rate limits. No cost.
- Individual lookups via `data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json` at 10 req/sec
- Coverage: ~19,000 US filers (NYSE, NASDAQ, OTC)
- Free parsing tools exist: `sec-edgar-api` Python toolkit, SECfinAPI
  (free, standardized JSON for 19K+ companies)

**EU + Global Stocks (~5K-40K tickers): EODHD -- PAID**

EODHD (eodhd.com) covers 60+ exchanges including all major EU and global
markets. Key capabilities:

- Bulk Fundamentals API: pull all fundamentals for an entire exchange in
  a single request (`/api/v1.1/bulk-fundamentals/{EXCHANGE}`), paginated
  at 500 companies per request
- Each company returns: General info (sector, industry, country, ISIN),
  Highlights (market cap, P/E, P/B, EV/EBITDA, beta, dividend yield),
  Valuation, Technicals, full Income Statement/Balance Sheet/Cash Flow
  (yearly + quarterly going back years), insider transactions,
  institutional holders, earnings history
- EU exchanges covered: LSE, Euronext (Paris, Amsterdam, Brussels,
  Lisbon), XETRA (Frankfurt), SIX Swiss, BME (Spain), Nasdaq Nordic,
  Vienna, Warsaw
- Also: TSX (Canada), ASX (Australia), NSE/BSE (India), SSE/SZSE
  (China), TSE (Japan via Marketstack), and 50+ more
- Plans from $19.99/month. Extended Fundamentals Plan enables bulk
  downloads.
- Also offers Insider Transactions API (SEC Form 4), bulk EOD price
  data, and an MCP server for agent queries

**API coverage comparison:**

| Capability | SEC EDGAR | EODHD | Financial Datasets MCP | Alpha Vantage |
|:--|:--|:--|:--|:--|
| US stocks | ~19K (complete) | ~10K | ~10K | Good |
| EU stocks | None | ~8K+ (60 exchanges) | US-only | Good |
| Bulk export | Nightly ZIP | Per exchange (500/page) | No (per-ticker) | No |
| Free tier | Unlimited | 20 req/day | OAuth (limited) | 25 req/day |
| Paid from | Free | $19.99/mo | $49/mo | $49.99/mo |
| Financial statements | Raw XBRL, needs parsing | Standardized JSON | Standardized JSON | Standardized JSON |
| MCP server | No (raw API only) | Yes | Yes (best integration) | Yes |

**Why not just one provider:**

- SEC EDGAR is free and complete for US but provides no EU coverage
  and requires XBRL parsing (nontrivial mapping of US-GAAP tags)
- EODHD has the best EU + global coverage and bulk export but costs
  money and the free tier is too small for screening
- Financial Datasets MCP is perfect for OpenClaw agent queries but does
  not support bulk export and is US-only
- Alpha Vantage has a free MCP server but 25 req/day is inadequate for
  bulk and no EU coverage on free tier
- Financial Modeling Prep is US-focused on free tier; EU requires paid

The hybrid approach uses the best tool for each job: free bulk for US,
paid bulk for EU, MCP for agent deep dives.

### Tier 2: Agent Deep-Dive MCP Servers (Stages 3-7)

For individual company deep dives, agents use MCP tools connected
directly to OpenClaw. Two MCP servers are recommended:

**Primary: Financial Datasets MCP** (best OpenClaw integration, OAuth)

Configure in `~/.openclaw/openclaw.json`:
```json
{
  "mcp": {
    "servers": {
      "financial-datasets": {
        "url": "https://mcp.financialdatasets.ai/",
        "transport": "streamable-http",
        "auth": "oauth"
      }
    }
  }
}
```

Tools available: `get_income_statement`, `get_balance_sheet`,
`get_cash_flow_statement`, `get_financial_metrics` (P/E, EV, ROE,
EV/EBITDA, revenue per share, etc.), `get_financial_metrics_snapshot`
(market cap, P/E, dividend yield), `get_stock_prices` (historical OHLCV),
`get_stock_price` (current snapshot), `get_filings` (SEC filings list),
`get_filing_items` (Risk Factors, MD&A sections from 10-K/10-Q),
`get_segmented_financials` (segment breakdowns), `screen_stocks`
(built-in screener), `get_news`. 2,244 GitHub stars, active.

**Backup: Alpha Vantage MCP** (global coverage, free tier)

Endpoint: `https://mcp.alphavantage.co/mcp` with free API key (25
req/day). Tools: `INCOME_STATEMENT`, `BALANCE_SHEET`, `CASH_FLOW`,
`OVERVIEW` (company profile, sector, P/E, market cap), `EARNINGS`.

**When agents use MCP vs bulk data:**

| Stage | Data Source | Why |
|:--|:--|:--|
| 0-2 (Screening) | Bulk CSV from Python script | Need all 50K companies simultaneously |
| 3B (Simple Moat) | Bulk CSV + MCP for ROIC-WACC details | Screening data gives the spread; MCP provides depth for borderlines |
| 3C (Management) | MCP + EDGAR Form 4 | Insider ownership changes, SEC filings |
| 4A (Deep Moat) | MCP + web_search | Competitor financials, industry data |
| 4B (Finance) | MCP + EDGAR filings | Full financials, footnotes, debt schedules |
| 7A (DCF) | MCP (all 3 statements 5yr) | DCF needs complete historical data |

### Data Storage Architecture

Quarterly CSV snapshots stored in investing-hub:

```
data/
  us-q1-2026.csv           # US stocks, Q1 2026 data
  us-q2-2026.csv           # US stocks, Q2 2026
  eu-q1-2026.csv           # EU stocks
  eu-q2-2026.csv
  data-dictionary.md       # Column definitions and data sources
```

Each CSV file contains ALL screening fields for every company in that
region-quarter, produced by the Stage 0-2 Python script. Files are
versioned by quarter because earnings releases update the data --
a Q2 file reflects Q2 earnings, which are typically released through
July-August. The pipeline re-pulls after each earnings season (Feb, May,
Aug, Nov).

**CSV column schema (core fields for every row):**

```
ticker, company_name, exchange, country, sector, industry, market_cap,
enterprise_value, currency,
revenue_yr0, revenue_yr1, ..., revenue_yr9,
revenue_cagr_5yr, revenue_cagr_10yr,
ebit_5yr_avg, ebitda_5yr_avg, net_income_5yr_avg,
fcf_5yr_avg, owner_earnings_5yr_avg,
roic_5yr_avg, roe_5yr_avg, roce_5yr_avg,
gross_margin_5yr_avg, operating_margin_5yr_avg, fcf_margin_5yr_avg,
gross_margin_cv,
pe_ratio, ps_ratio, pfcf_ratio, pebit_ratio, pb_ratio,
ev_ebit, ev_ebitda, ev_revenue,
debt_ebitda, debt_equity, current_ratio,
insider_ownership_pct, shares_outstanding, diluted_shares,
share_count_cagr_5yr,
composite_rank, broad_screen_pass, data_quality_flag
```

**Sector-specific columns (populated based on sector classification):**

| Sector | Additional Columns |
|:--|:--|
| Banks | bvps_growth, cet1_ratio, net_interest_margin, efficiency_ratio |
| Insurance | premium_growth, combined_ratio, loss_ratio, expense_ratio |
| REITs | ffo_per_share, affo_per_share, ffo_share_growth, occupancy_rate |
| SaaS | rule_of_40, gross_retention_rate, net_retention_rate |
| Energy/Materials | production_volume_growth, reserve_life, replacement_ratio |
| Pharma | rd_to_revenue, patent_cliff_exposure_pct |
| Utilities | rab_growth, allowed_roe, earned_roe |

### Implementation Roadmap

**Phase 1: US pilot (free, immediate)**

1. Write Python script that downloads SEC EDGAR `companyfacts.zip`
2. Parse XBRL JSON into standardized flat CSV (~10K US companies)
3. Calculate all Stage 1-2 screening metrics
4. Apply sector classification and populate sector-specific columns
5. Run data quality validation (Stage 0.5 checks)
6. Output: `investing-hub:data/us-q2-2026.csv` (or current quarter)
7. Commit to investing-hub

Estimated effort: 8-12 hours for the Python script (XBRL tag mapping
is the hardest part; there are ~15,000 US-GAAP tags, of which ~200 are
relevant for screening).

**Phase 2: EU integration (paid, after Phase 1 validation)**

1. Sign up for EODHD at $19.99-$29.99/month (Extended Fundamentals)
2. Extend Python script to pull bulk fundamentals per EU exchange
3. Merge EU data with US data into unified ranking
4. Test on a subset before scaling to all exchanges

**Phase 3: MCP agent integration (alongside Phase 1/2)**

1. Configure Financial Datasets MCP in `~/.openclaw/openclaw.json`
2. Configure Alpha Vantage MCP as backup
3. Test agent queries for deep-dive stages (3B-7A)
4. Document MCP tool usage in the pipeline skill

## Impact

### Positive

- **US coverage is free and complete.** SEC EDGAR provides every US
  public company's full financials at zero cost. The Phase 1 pilot can
  run immediately with no external API dependencies.
- **EU coverage is one paid API away.** EODHD covers every major EU
  exchange with standardized, queryable data. No multi-API fragmentation.
- **Agent deep dives are MCP-native.** Financial Datasets MCP integrates
  directly with OpenClaw's MCP gateway. Agents can query financials,
  metrics, and SEC filings without leaving the tool ecosystem.
- **Single source of truth.** The quarterly CSV files in
  `investing-hub:data/` are the ground truth for screening. Agents read from
  files, not APIs, for Stages 0-2. This is reproducible, auditable, and
  immune to API outages.
- **Stale data is explicit.** Quarterly files are dated. A Q1 file used
  in August is visibly stale. This prevents agents from confidently
  analyzing companies with 6-month-old data.

### Risk

- **XBRL parsing complexity.** SEC EDGAR raw JSON maps ~15,000 US-GAAP
  tags to financial statement line items. Tag selection errors produce
  wrong metrics. Mitigation: start with SECfinAPI (free, already
  standardized) rather than raw companyfacts.zip for the MVP. Transition
  to raw parsing only if customization is needed.
- **EODHD free tier is too small for testing.** 20 req/day cannot screen
  an exchange. Mitigation: start with US pilot (free) to validate the
  methodology. Only subscribe to EODHD after the US pipeline is proven.
- **MCP rate limits.** Both Financial Datasets and Alpha Vantage have
  rate limits. A deep dive analysis across 30 companies could hit them.
  Mitigation: agents request data incrementally, not all at once. The
  bulk CSV already has screening fields; MCP is only for the final
  candidates.
- **Data drift between sources.** SEC EDGAR and EODHD may report
  slightly different figures for the same US company due to
  standardization differences. Mitigation: for US companies, use EDGAR
  as the authoritative source. EODHD is for non-US companies only.
- **Git repo size.** 50K rows per CSV file per quarter could grow the
  brain repo significantly. Mitigation: use CSV compression or store
  only the latest 4 quarters in the repo (archive older files).

### Cost

- **US data:** $0 (SEC EDGAR is free and unlimited).
- **EU data:** $19.99-$29.99/month (EODHD Extended Fundamentals).
  ~$240-$360/year.
- **MCP servers:** $0 for Financial Datasets MCP (OAuth, free tier
  adequate for deep dives on 10-30 companies per quarter). Alpha
  Vantage MCP free tier (25 req/day) as backup.
- **Implementation:** 8-12 hours for Phase 1 Python script (US only).
  4-6 additional hours for Phase 2 EU integration.
- **Maintenance:** Low. Python script runs quarterly via cron (Job 1).
  Data APIs are stable; schema changes are rare.

## Open Questions

1. **SECfinAPI vs raw EDGAR:** Should the Phase 1 Python script use
   SECfinAPI (free, already standardized, no tag mapping required) or
   parse raw companyfacts.zip (full control, unlimited customization)?
   Recommendation: SECfinAPI for MVP, raw EDGAR if gaps emerge.

2. **EODHD plan tier:** The base plan ($19.99/mo) includes fundamental
   data but has API call limits. The Extended Fundamentals plan (price
   TBD, likely $29.99-49.99/mo) enables bulk downloads. Which tier do
   we need for screening ~8K EU stocks? Recommendation: start with base
   plan and test throughput; upgrade only if rate limits block bulk
   screening.

3. **Data dictionary location:** Should `data-dictionary.md` live in
   `investing-hub:data/` (alongside the CSVs) or in `investing-hub:frameworks/`
   (alongside the methodology documents)? Recommendation:
   `investing-hub:data/data-dictionary.md` -- closest to the data it
   documents.

4. **Quarter naming convention:** The proposal uses `us-q2-2026.csv`.
   Is this clear enough? Alternative: `us-2026-q2.csv` (sortable by
   year first). Recommendation: `us-2026-q2.csv` for filesystem
   sorting.

5. **Non-US/non-EU markets:** EODHD covers 60+ exchanges including
   Japan, China, India, Australia, Canada. Should the pipeline include
   all of these from Phase 2, or start with US + EU and expand later?
   Recommendation: US + EU first (covers ~95% of investable market cap).
   Add other markets on demand.

6. **Survivorship bias handling:** Delisted companies are excluded from
   current datasets. Should the Python script also pull EODHD's
   "Delisted Stock Companies Data" endpoint for backtesting? This would
   add significant complexity. Recommendation: document as known
   limitation in Phase 1; add delisted data in Phase 3 only if
   backtesting becomes a priority.

7. **CSV vs Parquet:** For 50K rows with 100+ columns, Parquet is more
   efficient than CSV (compressed, typed, faster queries). But CSV is
   human-readable and git-diffable. Recommendation: CSV for Phase 1
   (git-friendly, debuggable). Migrate to Parquet only if file size
   becomes a problem.

## Approval Gate

If approved, I will:

1. Build Phase 1: Python script that downloads US company data from
   SEC EDGAR (via SECfinAPI or raw parsing), computes all Stage 0-2
   screening metrics, and outputs `investing-hub:data/us-2026-q3.csv` to
   investing-hub.

2. Configure Financial Datasets MCP in OpenClaw for agent deep dives.

3. Write `investing-hub:data/data-dictionary.md` documenting every column,
   data source, and calculation method.

4. Phase 2 (EU + EODHD) requires Suggi's subscription decision and
   will be built after US pilot validation.

## Cross-Links

- `investing-hub:frameworks/sector-specific-metrics.md` -- defines which
  fields are needed per sector
- `reflections/2026-07-26_ava_decorrelation-convergence-pipeline.md` --
  the merged pipeline milestone that triggered this
