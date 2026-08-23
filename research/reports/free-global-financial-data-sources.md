---
name: free-global-financial-data-sources
id: 20260819T192848Z
tier: report
author: Neo
tags: [financial-data, global-markets, free-sources, sec-edgar, esef, china, indonesia, screening]
links:
  - governance/template-reports.md
  - investing-hub:frameworks/screening-data-guide.md
  - investing-hub:frameworks/screening-template.md
---

# Free Global Financial Data Sources -- Research Report

Research date: 2026-08-19 UTC. Scope: free sources only; US, EU,
China, Indonesia, and the widest practical stock universe; 5-10 years
of financial history.

## Executive Summary

Question: where can we get the most complete financial data for the
most stocks, free of charge, across US, EU, China, and Indonesia?
Answer: there is no single free source; the workable architecture is
multi-source. SEC EDGAR (bulk XBRL, no API key, long history) is the
strongest free foundation and the authoritative US source. UK
Companies House offers free XBRL accounts data. ESMA ESEF defines a
machine-readable EU format but is not a central archive; the EU-wide
ESAP portal becomes public only from July 2027. CNINFO, SSE, and SZSE
are the official China disclosure portals with public query APIs.
IDX is the official Indonesia source but was Cloudflare-blocked from
this server, so its bulk depth remains unverified. Free aggregators
(SimFin, yfinance, Alpha Vantage, Twelve Data) are convenience layers
with limits, not authoritative bulk archives. No MCP is required for
the bulk build; a Python ingestion pipeline into normalized
Parquet/CSV is the right first tool. Confidence: high (85%) for the
US, UK, and aggregator findings, which were verified directly against
official pages and live endpoints; medium for China (APIs verified,
bulk practicality inferred); low for Indonesia (access blocked during
research).

## Research Question

What free sources provide the most complete financial statements and
screening fields (revenue, operating income, equity, debt, cash flow,
shares) for the widest possible universe of listed stocks across the
US, EU, China, and Indonesia, with 5-10 years of history, without
paying anything?

Scope in: free access, listed-company fundamentals, bulk feasibility,
historical depth, legal/redistribution cautions.
Scope out: paid tiers, intraday or real-time market data, portfolio
management, trade execution.
Why it matters: every screening and valuation artifact depends on
this data layer. Getting the source wrong means confident-looking
garbage downstream.

## Methodology

Approach: direct retrieval of official documentation and live API
tests over HTTPS from the VPS, without a browser. Sources were
retrieved on 2026-08-19 UTC. Tools: curl with a declared User-Agent,
Python (urllib), ZIP parsing of SEC bulk archives, and JSON parsing
of live endpoints.

Sources consulted (retrieval dates):

- SEC EDGAR API documentation, developer FAQ, data-set pages
  (2026-08-19)
- SEC live endpoints and bulk archives, including companyfacts and
  submissions samples for Apple (2026-08-19)
- SEC quarterly Financial Statement Data Set 2025q4 (2026-08-19)
- Companies House data-products guidance, developer guidelines, free
  data-product page (2026-08-19)
- ESMA electronic-reporting (ESEF) and ESAP pages (2026-08-19)
- CNINFO, SSE, SZSE official portals (2026-08-19)
- IDX official pages (attempted; HTTP 403) (2026-08-19)
- SimFin pricing and data pages, yfinance and AKShare READMEs,
  Alpha Vantage docs and pricing, Twelve Data pricing, OpenFIGI,
  OpenBB README (2026-08-19)

Limitations: browser automation was unavailable, so JavaScript-heavy
pages were inspected via source and API endpoints only. IDX and OJK
could not be reached from this network. Free-tier limits can change;
re-verify before production use.

## Findings

### Finding 1: SEC EDGAR is the strongest free source -- VERIFIED

The SEC provides data.sec.gov REST APIs without authentication or API
keys, covering submissions history and extracted XBRL financial data
for 10-K, 10-Q, 8-K, 20-F, 40-F, and 6-K variants [1]. Bulk ZIP
archives are republished nightly: companyfacts.zip contains all XBRL
frame and company-facts data; submissions.zip contains filing history
for all filers [1]. A live test returned Apple facts across us-gaap
tags including revenue, operating income, net income, assets, equity,
long-term debt, operating cash flow, and property purchases. The
2025q4 Financial Statement Data Set contained 6,304 submission rows
and 5,786 unique CIKs. Guidance limits users to 10 requests per
second with a declared User-Agent [2]. Historical coverage: XBRL
required since 2009; EDGAR filing indexes from 1994Q3 [2].
Confidence: high.

### Finding 2: UK Companies House is the strongest free country source -- VERIFIED

The accounts data product is a free downloadable ZIP of electronically
filed accounts in XBRL, with daily and monthly files; the company data
product is a free monthly CSV snapshot [21][22]. Electronic accounts
covered about 60% of 2.2 million accounts at publication [21]. API
limit: 600 requests per 5 minutes [22]. Limitation: this is company
register data, not a ready listed-equity fundamentals table; filter
and parse. Confidence: high.

### Finding 3: EU has a format, not a central archive -- VERIFIED

ESMA mandates ESEF (XHTML plus Inline XBRL) for issuers on EU
regulated markets [19]. ESAP, the EU-wide central portal, starts
collection July 2026 and becomes publicly available July 2027 [20].
Until then, EU collection is fragmented across national
repositories/OAMs and issuer pages. Negative result: no free pan-EU
bulk fundamentals API exists today. Confidence: high.

### Finding 4: China official portals expose public query APIs -- VERIFIED (partially inferred)

CNINFO describes itself as the statutory disclosure platform operated
by a Shenzhen Stock Exchange subsidiary [24]; SSE and SZSE expose
regular-report and listed-company information sections [25][26].
Independent testing found public JSON/JSONP query APIs on CNINFO,
SSE, and SZSE returning annual-report records; PDF retrieval worked
for CNINFO and SZSE while SSE returned an anti-bot response from this
network. Bulk practicality and exact rate limits were not verified.
Confidence: medium.

### Finding 5: Indonesia is blocked from this server -- UNVERIFIED

IDX is the official exchange source with a financial-report area
[27], but every direct request returned HTTP 403/Cloudflare. Open
source wrappers document browser impersonation and throttling. No
verified bulk depth. Confidence: low.

### Finding 6: free aggregators are convenience layers, not archives -- VERIFIED

SimFin free plan advertises 5,000 US stocks with 5 years of
fundamentals; 10 years is paid; downloaded data must be deleted on
subscription cancellation [16][17][18]. yfinance is an unofficial
Yahoo wrapper for personal use, with data rights governed by Yahoo's
terms [28][29]. Alpha Vantage free tier is 25 API calls per day,
with unlimited requests only for verified open-source or educational
projects [30][31][32]. Twelve Data free Basic plan shows 8 API
credits / 800 per day with limited trial symbols and internal
non-display use [33][34]. AKShare is an academic-use wrapper whose
interfaces may be removed [35]. OpenFIGI is free identifier mapping
with no financial statements [36]. OpenBB is an integration layer,
not a data source [38]. Negative result: no reviewed provider offers
broad global coverage, long history, unrestricted bulk, and free
redistribution simultaneously. Confidence: high.

## Discussion

The core surprise is structural, not technical: free financial data
is segmented by design. US data is commoditized through SEC EDGAR, so
it is free and complete; non-US data requires exchange and registry
relationships that vendors monetize. The pattern repeats across every
provider reviewed. This aligns with the earlier brain work in
`investing-hub:frameworks/screening-data-guide.md`, which reached the same
multi-source conclusion for screening; this report extends it with
current verified limits and the country-level official portals.

A second surprise: the China official portals are more open than
expected -- public JSON APIs serving historical annual-report records
without authentication. Indonesia is the opposite: the official source
is heavily protected against programmatic access.

The MCP question deserves a clear negative answer: MCP does not solve
bulk acquisition, coverage, rate limits, parsing, licensing, or
storage. It is an optional later convenience for querying a local
normalized dataset or running individual deep dives.

## Conclusion

Answer: build the data layer from official sources per region -- SEC
EDGAR (US), Companies House (UK), ESEF/national repositories (EU),
CNINFO/SSE/SZSE (China), IDX/OJK (Indonesia) -- and use aggregators
only for discovery and fallback.

Recommendation: start with the US SEC ingestion pilot (20-company
validation set), then UK, one EU country, China, and Indonesia in
that order, storing raw filings and normalized Parquet/CSV in
`investing-hub:data/` with source, filing date, units, and quality flags
per value.

Open questions: IDX bulk depth and licensing; CNINFO/SSE/SZSE rate
limits and bulk-reuse terms; whether any national OAM offers a free
complete ESEF bulk feed; exact retention of Estonia/Belgium country
datasets.

## Evaluation History

None yet. This report has not received an independent evaluation
pass. Flagged for a decorrelated review before it is treated as
settled.

## Cross-Links

- `governance/template-reports.md` -- this report's format spec
- `investing-hub:frameworks/screening-data-guide.md` -- prior multi-source
  screening research
- `investing-hub:frameworks/screening-template.md` -- the data fields the
  pipeline must populate

## Sources

[1] https://www.sec.gov/edgar/sec-api-documentation
[2] https://www.sec.gov/os/accessing-edgar-data
[16] https://simfin.com/en/fundamental-data-download/
[17] https://simfin.com/en/prices/
[18] https://www.simfin.com/en/legal-advice
[19] https://www.esma.europa.eu/issuer-disclosure/electronic-reporting
[20] https://www.esma.europa.eu/esmas-activities/data/european-single-access-point-esap
[21] https://www.gov.uk/guidance/companies-house-data-products
[22] https://developer.company-information.service.gov.uk/developer-guidelines
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
