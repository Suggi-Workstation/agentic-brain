---
name: global-free-financial-data-2026-08
id: 20260819T192848Z
tier: research
domain: value-investing
author: Neo
tags: [financial-data, global-markets, free-sources, sec-edgar, esef, china, indonesia, screening]
links:
  - investing/frameworks/screening-data-guide.md
  - investing/frameworks/screening-template.md
---

# Global Free Financial Data -- Practical Research Result

Research date: 2026-08-19 UTC
Scope: free sources only; US, EU, China, Indonesia, and the widest
practical stock universe; 5-10 years of financial history.

## Executive Verdict

There is no single free source that provides complete, standardized,
5-10 year financial statements for 50,000+ global stocks. The free
solution is a multi-source system:

1. US: SEC EDGAR raw XBRL and bulk data. This is the strongest free
   foundation and should be the authoritative US source.
2. UK: Companies House bulk company and accounts data. This is the
   strongest free country-level EU/Europe source found in this pass.
3. EU: ESEF creates machine-readable annual reports, but there is not
   yet one mature, public, EU-wide bulk fundamentals API to replace
   country-level collection. ESAP is planned as the central access
   point, with public availability scheduled for July 2027.
4. China: CNINFO, SSE, and SZSE are the official disclosure portals.
   They are usable as filing sources, but a clean free bulk standardized
   history needs a parser and careful access testing.
5. Indonesia: IDX is the official exchange source. Its public page was
   Cloudflare-blocked from this server during research, so bulk depth
   and automation remain unverified here.
6. Global discovery and fallback: yfinance, AKShare, and OpenFIGI can
   help discover symbols, normalize identifiers, or fill gaps. They
   are not a substitute for authoritative filings.

No MCP is required for the bulk data build. Use Python scripts and
store normalized Parquet/CSV data in `investing/data/`. An MCP would
only help an agent query a small set of already-collected records or
perform individual deep dives. It would be the wrong first tool for
50,000-stock ingestion.

## Source Scoreboard

| Source | Region | Fundamentals | History | Bulk potential | Verdict |
|:--|:--|:--|:--|:--|:--|
| SEC EDGAR XBRL/bulk | US filers, some foreign filers | Full filed XBRL facts and filings | Long; company facts are filer history | Excellent | Primary US source |
| Companies House | UK | Electronic accounts in XBRL; company snapshots in CSV | Daily/monthly accounts files advertised for last year; older filings via register | Good for UK | Primary UK source |
| ESMA ESEF | EU regulated-market issuers | XHTML/iXBRL annual reports | Annual reports; historical collection is fragmented | Medium after country/OAM discovery | Primary EU format, not a ready bulk dataset |
| CNINFO/SSE/SZSE | China | Official announcements and regular reports | Historical reports accessible by issuer/date | Medium, parser required | Primary China source |
| IDX/OJK | Indonesia | Official reports and disclosures | Historical reports likely available; automation not verified here | Unknown | Primary Indonesia source, needs access test |
| SimFin | Mainly US; provider-specific coverage | Standardized statements and metrics | Free plan advertises 5 years; 10 years is paid | Bulk CSV/API advertised | Useful convenience source, not fully free for 10 years |
| yfinance/Yahoo | Broad global market symbols | Per-ticker statements and market data where Yahoo has it | Per-ticker; depth varies | Poor for 50,000 fundamentals; rate limiting and terms matter | Discovery/fallback only |
| Alpha Vantage | Global market data; fundamentals coverage varies | Per-ticker statements | Documentation advertises 20+ years for some history endpoints | Poor at free throughput | Individual-company fallback |
| Twelve Data | Global market data and fundamentals | Basic free plan advertises limited global trial symbols and 8 API credits / 800 daily | Depth and fundamental availability depend on plan/endpoint | Poor for bulk free ingestion | Not a free bulk solution |
| AKShare | Wrapper over multiple public Chinese and other sources | Interface-dependent | Interface-dependent | Useful China adapter; source/licence varies | Research adapter, not authority |
| OpenFIGI | Global identifiers | No financial statements | N/A | Excellent identifier mapping | Use for security identity, not fundamentals |
| OpenBB | Open-source integration layer | Depends on providers | Depends on providers | Tooling, not a free data supply | Optional, not required |

## Primary US Build: SEC EDGAR

Official SEC REST APIs on `data.sec.gov` provide submissions history and
extracted XBRL financial-statement data without API keys. The SEC API
documentation says the APIs cover filings including 10-K, 10-Q, 8-K,
20-F, 40-F, and 6-K variants. The SEC asks scripted clients to declare
a descriptive User-Agent and states a current maximum access rate of
10 requests per second. [1][2]

The SEC publishes ticker/exchange mappings and bulk archives. The
companyfacts archive is a ZIP of per-CIK JSON company facts; the
submissions archive contains filer submission histories. A direct test
of Apple companyfacts returned `us-gaap` and `dei` facts, including
revenue, operating income, net income, assets, equity, long-term debt,
operating cash flow, and property-and-equipment purchases. [3][14][15]

The quarterly Financial Statement Data Sets are flattened, tab-separated
files (`sub.txt`, `pre.txt`, `num.txt`, `tag.txt`) sourced from XBRL
financial statements. The SEC describes the data as filed by registrants,
updated quarterly, and including numeric data rendered in primary
financial statements. A downloaded 2025 Q4 set contained 6,304 submission
rows and 5,786 unique CIKs; this is a quarter's filing population, not a
unique global-stock count. [10][11]

Recommended US files:

- `companyfacts.zip`: broad per-filer facts, best raw foundation.
- `submissions.zip`: filing metadata and historical submission files.
- Quarterly `financial-statement-data-sets`: efficient flattened ingestion.
- `company_tickers_exchange.json`: starting identifier map.

Do not assume one XBRL tag maps cleanly across every company. Build a tag
precedence map, keep the raw accession/tag/unit/context, and expose
`missing`, `ambiguous`, and `restated` flags. Financial statements are
reported figures; derived metrics such as ROIC, FCF, EV, and normalized
earnings must be calculated separately.

## UK and EU

Companies House provides a free monthly snapshot of live-company basic
data in CSV ZIP files. More importantly for this task, its official data
products page states that the accounts product is a free downloadable ZIP
of electronically filed accounts in XBRL, with daily and monthly files.
The same page says electronic accounts were about 60% of the 2.2 million
accounts at the time of publication. The API has a documented limit of
600 requests per five minutes. This is a strong free UK source, but the
accounts product is not the same as a clean listed-equity fundamentals
table; filter to public/listed entities and parse accounts carefully.
[21][22][23]

ESMA states that ESEF is mandatory for issuers with securities traded on
EU regulated markets. Annual financial reports are XHTML; IFRS consolidated
statements are tagged with Inline XBRL, making the disclosures structured
and machine-readable. This is the right common format to target for EU
annual reports. [19]

The EU-wide ESAP is not the immediate answer today. ESMA says the portal
will be made available to the public from July 2027, with collection
starting in July 2026 and phased information thereafter. Until then, an EU
collector must locate national collection bodies/OAMs, issuer pages, or
exchange repositories country by country. [20]

Practical EU order:

1. UK Companies House XBRL accounts.
2. ESEF annual-report discovery for each target country/OAM.
3. National exchange/regulator repositories.
4. Issuer IR pages as a last-mile fallback.
5. Standardize only after preserving the original XHTML/iXBRL and filing URL.

## China

CNINFO describes itself as the statutory information-disclosure platform
operated by a wholly owned Shenzhen Stock Exchange subsidiary. The live
portal exposes company announcements, regular reports, data services, and
API/data-service menus. SSE exposes a regular-report disclosure section;
SZSE exposes listed-company information and announcements. [24][25][26]

These official portals are the right source for Chinese filings. They are
not equivalent to a free, standardized, 10-year fundamentals API. The
implementation should first build a small parser and test:

- annual report discovery by issuer/security code and reporting year;
- PDF/XHTML/XBRL availability;
- Chinese accounting labels and unit/currency normalization;
- access rate limits, robots/terms, and whether bulk downloads are allowed;
- restatements and calendar/fiscal-year differences.

AKShare can be used as a Python adapter for some public Chinese interfaces,
but its README warns that interfaces may be removed and says the data is
for academic/reference use with source-specific open-source protocols.
Treat it as a convenience layer and retain the official source URL for
every row. [35]

## Indonesia

IDX is the official exchange source and exposes a financial-report and
annual-report area. The IDX page returned HTTP 403/Cloudflare to this
server, so I am not claiming verified bulk coverage, API availability, or
10-year depth from it. [27]

The correct free-first path is:

1. Obtain the IDX listed-company/security master from the official exchange.
2. Collect annual and quarterly financial-report links.
3. Test whether reports are downloadable as PDF, XHTML, or XBRL.
4. Add OJK disclosures where IDX is incomplete.
5. Preserve Indonesian labels, original currency, filing date, and source URL.
6. Only then decide whether a public wrapper is safe and complete enough.

A wrapper that returns Indonesian data is not automatically authoritative.
It must be checked against IDX/OJK filings for a sample before bulk use.

## Global Fallbacks and Their Limits

### SimFin

SimFin's official pages advertise a free account, 5,000 US stocks, bulk
CSV/API access, and 5 years of fundamentals. Its pricing page shows 10
years of fundamentals under the paid START plan, while the free plan shows
5 years of bulk fundamentals. Therefore it is useful for a quick US pilot,
but it does not meet the user's free 10-year requirement. SimFin also states
that downloaded data must be deleted after subscription cancellation; do not
place it in a permanent brain dataset without checking the current license.
[16][17][18]

### yfinance

yfinance is an open-source Python tool for Yahoo Finance and explicitly
states that it is not affiliated with Yahoo. The README points users to
Yahoo's terms for rights to use the downloaded data. It is useful for global
symbol discovery, prices, and opportunistic fallback statements, but it is
unofficial, per-ticker, rate-limited in practice, and depth/field quality
varies by market. Do not treat it as a license-cleared bulk redistribution
source. [28][29]

### Alpha Vantage

Alpha Vantage documents fundamental endpoints such as overview, income
statement, balance sheet, cash flow, shares outstanding, and earnings. Its
support page states a standard free allowance of 25 API requests per day,
while verified open-source or educational projects may receive unlimited
requests subject to verification. The documentation advertises 20+ years
for some historical time-series endpoints; fundamental depth and market
coverage must be tested per symbol/endpoint. This is suitable for
individual-company deep dives, not 50,000-stock free ingestion. [30][31][32]

### Twelve Data

Twelve Data's free Basic plan shows 8 API credits and 800 per day, limited
markets/trial symbols, and internal non-display use. It lists income
statement, balance sheet, and cash flow among the product capabilities, but
its EDGAR archive endpoint is restricted to Ultra/Enterprise. It is therefore
not a free bulk fundamentals solution. [33][34]

### OpenFIGI and OpenBB

OpenFIGI is useful for mapping identifiers; its API page says the API is
free without daily, weekly, or monthly limitations and can map large numbers
of instruments. It does not provide financial statements. [36]

OpenBB is an open-source integration layer. It can simplify provider access,
but it does not create free data coverage; the underlying provider and
license still govern each output. [38]

## Recommended Architecture

Do not create one giant Markdown table for raw financial data. Markdown is
human-readable but inefficient, lossy for types, and unsuitable for millions
of facts. Use:

```
investing/data/
  README.md
  global-free-financial-data-2026-08.md
  raw/
    sec/
    companies-house/
    esef/
    cninfo/
    idx/
  normalized/
    securities.parquet
    annual_financials.parquet
    quarterly_financials.parquet
    filings.parquet
  exports/
    us-2026-q2.csv
    eu-2026-q2.csv
    cn-2026-q2.csv
    id-2026-q2.csv
  manifests/
    source-run-YYYYMMDD.json
```

Minimum normalized annual schema:

```
source,source_url,source_file,accession,issuer_id,ticker,isin,figi,
company_name,country,exchange,currency,fiscal_year,fiscal_period,
period_start,period_end,filing_date,statement,tag,standard_tag,
label,unit,value,scale,dimensions,restated,quality_flag
```

Keep raw filings and raw facts outside the exported scoreboard. The
scoreboard should contain derived columns only after the raw lineage exists:
revenue, EBIT, net income, CFO, CapEx, equity, debt, cash, diluted shares,
ROIC, FCF, margins, growth, and quality flags.

## Build Order

1. Build the SEC US ingestion first. It is the only source here with a
   genuinely strong free bulk foundation.
2. Validate 20 US companies across industrial, bank, insurer, REIT, SaaS,
   cyclical, and foreign private issuer cases.
3. Add UK Companies House XBRL as the first European country.
4. Add one EU ESEF country and one Chinese exchange as parser pilots.
5. Add Indonesia only after IDX access and report format are tested.
6. Use yfinance/AKShare only to fill discovery gaps or create candidate
   lists, never silently overwrite authoritative filing data.
7. Generate a quarterly CSV/Parquet export after each source run.
8. Record source, accession, filing date, units, and quality flags for every
   value.

## MCP Decision

No MCP is needed for the first build. MCP does not solve bulk acquisition,
source licensing, rate limits, parsing, or storage. It adds value later for:

- querying the local normalized dataset;
- retrieving one company's filings for a deep dive;
- letting an agent request a targeted data refresh;
- explaining data lineage from a row to the filing.

The first deliverable should be a Python ingestion and normalization
pipeline, not an MCP server.

## Bottom Line

For the most stocks at zero cost, use SEC EDGAR plus country/regulator
filings, not a single commercial-style API. A realistic free outcome is:
excellent US coverage, strong UK coverage, and progressively improving EU,
China, and Indonesia coverage with more parser work and less standardization.
A clean, global, standardized 5-10 year dataset for 50,000+ stocks is not
available for free as one download. We should build the dataset in layers
and label every row by source quality instead of pretending that a global
aggregator is complete.

## Sources

[1] https://www.sec.gov/edgar/sec-api-documentation
[2] https://www.sec.gov/os/accessing-edgar-data
[3] https://www.sec.gov/files/company_tickers_exchange.json
[10] https://www.sec.gov/dera/data/financial-statement-data-sets.html
[11] https://www.sec.gov/files/dera/data/financial-statement-data-sets/2025q4.zip
[12] https://www.sec.gov/dera/data/financial-statement-and-notes-data-set.html
[14] https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip
[15] https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip
[16] https://simfin.com/en/fundamental-data-download/
[17] https://simfin.com/en/prices/
[18] https://www.simfin.com/en/legal-advice
[19] https://www.esma.europa.eu/issuer-disclosure/electronic-reporting
[20] https://www.esma.europa.eu/esmas-activities/data/european-single-access-point-esap
[21] https://www.gov.uk/guidance/companies-house-data-products
[22] https://developer.company-information.service.gov.uk/developer-guidelines
[23] https://download.companieshouse.gov.uk/en_output.html
[24] https://www.cninfo.com.cn/new/index
[25] https://www.sse.com.cn/disclosure/listedinfo/regular/
[26] https://www.szse.cn/disclosure/listed/notice/index.html
[27] https://www.idx.co.id/en/listed-companies/financial-report-and-annual-report/
[28] https://raw.githubusercontent.com/ranaroussi/yfinance/main/README.md
[29] https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html
[30] https://www.alphavantage.co/support/#api-key
[31] https://www.alphavantage.co/documentation/
[32] https://www.alphavantage.co/premium/
[33] https://twelvedata.com/pricing
[34] https://twelvedata.com/docs/llms/regulatory/edgar-filings-archive.md
[35] https://raw.githubusercontent.com/akfamily/akshare/main/README.md
[36] https://www.openfigi.com/api
[38] https://raw.githubusercontent.com/OpenBB-finance/OpenBB/develop/README.md
