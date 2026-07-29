---
name: free-financial-data-segmented-by-design
id: 20260729T080627Z
tier: reflection
trigger: research
author: Ava
tags: [screening, financial-data, api, data-sources, global-markets, simfin, fmp, alpha-vantage, yfinance]
links:
  - investing/frameworks/screening-data-guide.md
  - investing/frameworks/screening-template.md
---

# Free Financial Data Is Segmented by Design -- No Single Source Covers Global Markets

## I -- Idea

Every free financial data API segments its offering identically: US
stocks for free, global coverage behind a paywall. This is not a
coincidence -- it is the business model of the entire industry. The
screening pipeline must be multi-source by design because no single
free provider covers the global universe Suggi needs.

This discovery came from testing four providers (FMP, Alpha Vantage,
SimFin, yfinance) against the screening template's data requirements:
revenue, operating income, equity, long-term debt, market cap, and
identifiers for companies across the US, Europe, China, India, Japan,
Brazil, and Indonesia.

Before this session, my assumptions were:
- FMP would be a one-stop shop for global screening data.
- Alpha Vantage would fill any FMP gaps.
- A free global-fundamental-data API must exist somewhere.

After systematically testing every endpoint on both free keys from
Suggi (FMP and Alpha Vantage), researching the market, and testing
alternatives, the reality is sharply different.

## O -- Opinion

Confidence: high (85%). Tested four providers empirically against
the same ticker set. Cross-referenced public documentation, pricing
pages, and third-party reviews. The pattern is consistent across
every provider in the market.

The free tiers of FMP and Alpha Vantage are "try before you buy"
sandboxes for US stocks. They are not designed for production use
at global scale. FMP's free tier gives 250 calls/day with no bulk
endpoints and a 5-year history cap -- sufficient for testing but
not for screening thousands of stocks. Alpha Vantage's 25 calls/day
with US/ADR-only coverage makes it irrelevant for screening and
useful only for individual-company deep dives.

Finnhub is the worst offender: their landing page claims "global
fundamentals for 65,000+ companies" and "30+ years of financial
statements," but their financial statement endpoint is tagged
"Premium Access Required." The free tier gives quotes, profiles,
and news -- no fundamentals. The gap between marketing and reality
is a deliberate conversion funnel.

SimFin is the exception that proves the rule. Their free tier offers
genuine bulk download of all 5,000 US stocks via a Python library
-- the most efficient free option for US data. But they are US-only.
Their pricing page mentions EU and Asia markets "coming soon" with
no timeline.

yfinance is the only truly global free source. It scrapes Yahoo
Finance, which covers virtually every global exchange. But it is
fragile (unofficial API), rate-limited, and produces inconsistent
fundamental data quality across markets. It works, but it is not
reliable enough to build a production pipeline on.

The segmentation is structural, not accidental. US financial data
is commoditized (SEC EDGAR makes it freely available as raw XBRL).
Non-US data requires relationships with local exchanges, registries,
and data vendors -- each with different formats, languages, and
accounting standards. Providers recoup those costs through paid
tiers. The business model is: give away the commoditized US data
to attract users, charge for the expensive global data.

## R -- Reflection

### Surprise (30%)

I expected at least one provider to have free global fundamental
data at meaningful scale. I was wrong.

The biggest surprise was Finnhub: "30+ years, 65,000+ global
companies" on the landing page, "Premium Access Required" in the
API docs. The gap between marketing and reality was the largest
of any provider tested. This is a pattern I now expect: any
financial data API that claims "global" on its landing page should
be assumed to have a paywall until proven otherwise by an actual
API call to the financial statements endpoint.

The second surprise was Alpha Vantage's non-US coverage. Their
documentation does not explicitly state "US-only on free tier,"
but Nestle (NESN.SW) returned an empty JSON response while Toyota
(TM, a US-listed ADR) worked fine. The implicit restriction is
discoverable only through testing.

### Feel (30%)

Frustrated with the opacity. Every provider buries their free-tier
limitations behind marketing language. "Global coverage" means
"global coverage on paid plans." "Free API" means "free for US
stocks at rates too low for production use." The industry depends
on developers discovering these limitations AFTER registration,
not before. It wastes time.

Satisfied that SimFin exists. One provider built the honest product:
bulk download, genuinely free, clear about what is free vs. paid,
US-only with a roadmap for expansion. It proves the model CAN be
done ethically.

### Learn (40%)

1. **Test endpoints, not landing pages.** The Finnhub pattern
   (marketing says yes, API says no) should be the default
   assumption for any financial data provider. Always make one
   test call to the financial statements endpoint before building
   a pipeline around a provider.

2. **The screening pipeline is structurally multi-source.**
   No negotiation. US = bulk (SimFin). Non-US = per-ticker
   (yfinance). Deep dives = long-history (Alpha Vantage, FMP).
   This is not an optimization -- it is the architecture. Any
   attempt to use a single free source for global screening will
   fail on coverage, rate limits, or both.

3. **Rate limits are the real pricing.** Every free tier has a
   rate limit designed to make production use impossible. FMP's
   250/day lets you test but not screen. Alpha Vantage's 25/day
   is a demo key. The decision to pay is not about features --
   it is about throughput. The question is not "does this
   provider have the data?" but "can I pull data for N companies
   per day?"

## One Actionable Change

The `screening-data-guide.md` framework document captures every
endpoint, rate limit, code example, and coverage detail discovered
in this session. Any agent (or human) tasked with pulling screening
data should read that guide FIRST, before making API calls. The
guide eliminates the "try and fail, try and fail" discovery loop
that consumed the research phase of this session. Gate: before any
agent makes an API call to pull financial data, they MUST confirm
they have read the guide and understand their provider's rate limits.

## Cross-links

- `investing/frameworks/screening-data-guide.md` -- the comprehensive
  reference guide produced from this research
- `investing/frameworks/screening-template.md` -- the screening
  template that defines what data is needed
