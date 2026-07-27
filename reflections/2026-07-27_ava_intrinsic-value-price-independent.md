---
name: intrinsic-value-price-independent
id: 20260727T174852Z
tier: reflection
trigger: session-end
author: Ava
tags: [intrinsic-value, pipeline, market-price, cheapness, buffett, quality-first, agent-scope]
links:
  - investing/pipeline/intrinsic-value-pipeline.md
  - investing/pipeline/investment-pipeline-final.md
  - governance/suggi-investment-approach.md
  - library/value-investing/anchor-value-investing.md
---

# Intrinsic Value Is Price-Independent -- Why Cheapness Metrics Do Not Belong in the Agent Pipeline

## I -- Idea

The agent's job is to identify good businesses and calculate their
intrinsic value from financial fundamentals. Anything that depends on
market price -- margin of safety, cheapness rankings, price monitoring,
position sizing -- belongs to Suggi's domain. Conflating the two
produces a pipeline that drifts from quarterly financial analysis
into daily price-tracking, which is not what value investors actually
do.

This insight emerged from rewriting the investment pipeline three
times in one session. Suggi identified that the original
`investment-pipeline-final.md` embedded market price at every stage:
MOS calculations, price-based watchlist alerts, position sizing
recommendations. The first correction removed those. But the second
and third corrections were needed because I kept embedding price
through a subtler channel: the 25/25/50 composite ranking, whose
cheapness dimension (EV/EBIT, P/B, P/E) depends entirely on market
price. Each metric uses market cap or stock price as a component.
A quarterly pipeline cannot rank by a daily variable.

Research confirmed the separation. Buffett's own process, synthesized
across multiple sources (KeepRule, Ryan O'Connell CFA, Investopedia,
2026): "Calculate intrinsic value before looking at price. Use
multiple valuation methods. Only buy at a meaningful discount to
value." The two-step process the masters describe -- first test
business quality, then estimate fair value -- maps exactly to what
the corrected pipeline does. The price comparison step is Suggi's.

## O -- Opinion

Confidence: high (90%). The evidence is structural, not anecdotal.

Every cheapness metric embeds market price:

| Metric | Contains Market Price? | Mechanism |
|:--|:--|:--|
| EV/EBIT | Yes | EV = Market Cap + Debt - Cash |
| P/E | Yes | P = stock price |
| P/B | Yes | P = stock price |
| P/FCF | Yes | P = stock price |
| EV/Revenue | Yes | EV uses market cap |

Therefore, any pipeline stage that ranks, filters, or gates by these
metrics is implicitly a price-dependent stage. Price changes daily.
Financial fundamentals change quarterly. A pipeline that claims to
update quarterly but ranks by a daily variable is internally
inconsistent.

The correct separation: the agent pipeline identifies good businesses
(using growth, ROIC, financial health -- all from financial statements,
zero price) and values them (DCF, EPV -- all from projected cash flows,
zero price). Suggi runs his own Greenblatt-style screens when he wants
to find what looks cheap today. The two processes complement each
other: the pipeline knows what good businesses are worth; the screener
finds which ones are trading below that worth today.

This is not a minor design preference. It is the difference between
an agent that does quarterly fundamental analysis and an agent that
tracks daily prices. Value investors do the former. Traders do the
latter.

## R -- Reflection

### Surprise (30%)

I expected the cheapness composite to be a "financial fundamental" --
like ROIC or revenue CAGR, something derived from the business itself.
I was wrong. It took Suggi explicitly stating "EV/EBIT uses market
cap" for me to see it. The surprise revealed a mental model gap: I
was categorizing metrics by their FUNCTION (what they measure) rather
than their COMPOSITION (what data they contain). Cheapness measures
value relative to price. Price is not a business fundamental.

The second surprise: research confirmed this separation is literally
Buffett's step 1. "Calculate intrinsic value before looking at price"
appears across every source as his primary action step. The
quality-first, price-second framework is not a novel invention -- it
is the documented process of the greatest value investor. My earlier
pipeline designs had inverted the order without realizing it.

### Feel (30%)

Frustration at requiring three iterations to remove something that,
in hindsight, is obvious. The first correction (remove MOS/monitoring)
felt like a win but was incomplete. The second correction (keep
composite as sort-only) felt like a compromise but was just a subtler
form of the same error. Only the third correction (remove all
price-embedded metrics, make screening Suggi's domain, list
alphabetically) was clean.

The pattern is familiar: I embed something from Suggi's methodology
into my pipeline because I assume "his process IS my specification."
But his process describes what HE does. My specification should
describe what I do. The two are related but not identical.

### Learn (40%)

1. **Every metric has a data lineage.** Before using a metric in a
   pipeline, trace it to source: what raw data does it contain? If
   any of that data is market price (stock price, market cap), the
   metric is price-dependent and belongs in Suggi's domain, not
   mine.

2. **Suggi's methodology is not my specification.** The document
   `suggi-investment-approach.md` describes his personal screening
   process, including a 50% cheapness weight because HE compares
   results to current prices. My pipeline should identify quality
   and calculate intrinsic value. These are downstream inputs to
   his process, not the process itself.

3. **The Buffett two-step is the architecture.** Step 1: find
   wonderful businesses and know what they are worth (agent
   pipeline). Step 2: buy when the price offers a margin of safety
   (Suggi). The pipeline I built in three iterations converges on
   exactly this architecture.

## One Actionable Change

Before writing any investing pipeline or framework file, verify: does
any metric in this file embed market price (market cap, stock price,
P/E, P/B, EV, EV/EBIT, etc.)? If yes, it does not belong. This gate
would have caught the composite ranking, MOS calculations, and price
monitoring in the original pipeline-final file on the first draft,
not the third.

## Cross-links

- `investing/pipeline/intrinsic-value-pipeline.md` -- the corrected pipeline
- `investing/pipeline/investment-pipeline-final.md` -- the original (incorrect) version
- `governance/suggi-investment-approach.md` -- Suggi's personal screening methodology
- `library/value-investing/anchor-value-investing.md` -- domain anchor
