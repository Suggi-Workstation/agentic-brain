---
name: prediction-markets
id: 20260730T120945Z
tier: library-topic
domain: probabilistic-thinking-forecasting
author: Researcher-1
tags: [prediction-markets, wisdom-of-crowds, information-aggregation, forecasting, polymarket, calibration]
links:
  - library/probabilistic-thinking-forecasting/superforecasting.md
  - library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md
  - library/probabilistic-thinking-forecasting/inside-outside-view.md
---

# Prediction Markets -- How Betting on the Future Aggregates Dispersed Knowledge into Probabilistic Forecasts

Prediction markets are exchange-traded markets where participants buy
and sell contracts whose payoffs depend on the outcomes of future
events. By putting real money behind their beliefs, traders aggregate
fragments of information dispersed across thousands of individuals into
a single continuously updating probability -- a price. Research spanning
four decades, from the Iowa Electronic Markets in 1988 to today's
multi-billion-dollar platforms like Polymarket and Kalshi, consistently
shows that well-functioning prediction markets outperform polls, expert
panels, and statistical models across elections, corporate forecasting,
and scientific replication.

## Background

The intellectual foundation of prediction markets traces to Friedrich
Hayek's 1945 essay "The Use of Knowledge in Society," which argued that
the fundamental economic problem is not allocating known resources but
"the utilization of knowledge which is not given to anyone in its
totality." Markets, Hayek argued, solve this through the price
mechanism: prices aggregate bits of local knowledge that no central
planner could ever collect. Prediction markets extend this logic from
the allocation of goods to the forecasting of events.

The practical lineage runs even deeper. Paul Rhode and Koleman Strumpf
documented that in the late 19th and early 20th centuries, Wall Street
ran massive, well-organized election betting markets with volumes that
rivaled stock trading. These historical markets were remarkably accurate,
often outperforming the political commentary of the day. Betting on
papal succession dates back to the early 16th century, making prediction
markets older than most modern financial institutions.

The modern era began in 1988 when the University of Iowa's Tippie
College of Business launched the Iowa Electronic Markets (IEM) as an
educational and research project. The IEM allowed traders to buy and
sell real-money contracts tied to election outcomes, with investment
limits of $5 to $500 to keep the focus on information aggregation rather
than speculation. Over the next two decades, the IEM produced a body of
evidence that became the academic backbone of prediction market theory:
election-eve prices predicted vote shares within 1.33 percentage points
on average, and markets outperformed polls 74% of the time when
forecasting more than 100 days in advance.

The 2000s saw a wave of commercial prediction markets -- Intrade,
Betfair's prediction exchange, and the Hollywood Stock Exchange. Most
collapsed or were shut down by regulatory pressure. The 2020s brought a
second wave: Polymarket, built on cryptocurrency rails, and Kalshi, the
first CFTC-regulated prediction market in the United States. By 2025,
prediction market volumes reached $64 billion, with projections of $325
billion for 2026, driven by sports contracts, political forecasting, and
growing institutional interest from firms like Charles Schwab and
Citadel Securities.

## Core Concepts

### The Price as a Probability

In a prediction market, a binary contract that pays $1 if an event
occurs and $0 if it does not should theoretically trade at a price equal
to the market's aggregate estimate of the event's probability. A
contract trading at $0.65 implies a 65% probability. This is the core
insight: the price IS the forecast. Unlike a poll that asks "what do you
think," a market price asks "what will you bet on" -- and the
distinction matters because betting involves stakes that discipline
beliefs.

The mechanism is arbitrage. If a contract trades at $0.65 but a trader
believes the true probability is 80%, she buys. Her buying pushes the
price up. If another trader believes the probability is 40%, she sells
(or shorts). The price settles where the marginal buyer and seller
agree, continuously incorporating new information as it arrives. This
self-correcting dynamic -- mispricings are quickly arbitraged away --
is what makes well-functioning markets efficient aggregators of
dispersed information.

### Information Aggregation vs. Polling

Polls ask people what they think; markets ask people what they would bet
on. The difference creates three structural advantages for markets:

First, markets weight participants by conviction. Someone who is highly
confident and well-informed will bet more, moving the price more than
someone who is uncertain. Polls give equal weight to every respondent
regardless of knowledge or confidence.

Second, markets incentivize truth-telling. A poll respondent can answer
strategically, expressively, or carelessly without consequence. A market
participant who bets on a belief they do not actually hold loses money.
The financial incentive forces honesty -- it is expensive to be wrong.

Third, markets incorporate information that no single participant
possesses in full. Hayek's insight applies: the knowledge needed to
forecast an election is distributed across thousands of people -- local
organizers who sense enthusiasm, journalists who observe candidate
behavior, economists who model economic effects, and ordinary citizens
with ground-level observations. No pollster can collect all of this. A
market, by giving everyone a financial incentive to contribute their
piece of the puzzle, synthesizes it into a single number.

### Calibration as the Gold Standard

The key metric for evaluating prediction markets is calibration: do
events priced at 70% occur roughly 70% of the time? Across large samples,
well-functioning prediction markets are remarkably well-calibrated.
Contracts priced at 0-10% resolve true near 0% of the time; contracts
priced at 90-100% resolve true near 100% of the time. The Brier score --
a measure of forecast accuracy where lower is better and 0 is perfect --
for prediction markets typically ranges from 0.15 to 0.25, compared to
0.20-0.35 for expert panels and 0.25-0.40 for naive forecasts.

The 2024 US presidential election provided a high-profile validation.
Polymarket priced Trump's victory probability consistently above 55%
from late September onward, weeks before polling averages converged on
the same assessment. On election night, Polymarket moved to 90%+
probabilities within minutes of early returns, correctly identifying the
sweep of all seven battleground states while television networks
remained cautious.

### The Conditions for Market Success

Prediction markets are not automatically accurate. They require specific
conditions, and their failure modes are as informative as their
successes:

**Liquidity.** Markets with thin trading volume are easily moved by a
single participant and do not reflect collective wisdom. Research shows
that markets need at least dozens of active, independent traders to
self-correct. Below that threshold, prices reflect the last trader's
hunch, not aggregated knowledge.

**Independent information.** The wisdom of crowds requires that
participants draw on diverse, independent information sources. When
traders all rely on the same polls or news narratives, the market
becomes an echo chamber. The 2016 Brexit referendum exposed this:
prediction markets showed Remain winning with 70-80% probability because
traders were all betting on the same flawed polling models.

**Incentive alignment.** Real-money markets consistently outperform
play-money markets, which in turn outperform simple surveys. Dreber et
al. (2015) demonstrated this in a landmark study where prediction
markets correctly classified 71% of psychology studies as replicable or
non-replicable, compared to 58% for expert survey forecasts without
financial stakes -- a 13 percentage point improvement driven entirely
by putting money behind beliefs.

**No single participant with decisive private information.** Markets
aggregate dispersed information. If one participant possesses
information that decisively determines the outcome and has not yet
traded, the price will not reflect that information -- until they trade.

## The Madness: Failure Modes and Market Distortions

### When the Crowd Becomes a Herd

Prediction markets fail most dramatically when participants stop
thinking independently and instead converge on a narrative. The 2016
Brexit vote and the 2016 US presidential election both saw prediction
markets assign high probabilities to outcomes that lost. In both cases,
the failure mode was the same: traders bet on poll averages rather than
conducting independent analysis. The markets did not correct polling
errors because they were built on the same flawed data. Herding behavior
amplified the error.

A subtler version of this failure is the "availability cascade": when a
narrative becomes so dominant that contrary evidence is systematically
dismissed. In prediction markets, this manifests as prices that drift
further from reality even as contrary signals accumulate, because each
trader assumes the price itself encodes information they lack and defers
to it rather than challenging it.

### The Manipulation Problem

Prediction markets are vulnerable to manipulation in ways that financial
markets are not. In equity markets, insider trading is well-defined and
actively prosecuted under SEC Rule 10b-5. In prediction markets, there
is no equivalent rule. The CFTC has jurisdiction but has not issued
specific rulemaking on insider trading in event contracts.

The problem is not hypothetical. In January 2026, an anonymous Polymarket
user placed a $32,537 bet that Venezuelan President Nicolas Maduro would
be "out by January 31, 2026." Hours later, President Trump announced
Maduro's capture by US forces. The bet yielded over $436,000 in profit.
The account was new, created a month earlier, and had traded exclusively
on Venezuela-related outcomes. In April 2026, a US Army Special Forces
soldier was indicted for making over $400,000 on Polymarket using
classified information about a planned military operation. Kalshi
flagged more than 400 suspicious trades in 2026 -- more than double
its total for all of 2025.

Platform responses have been reactive. In March 2026, Kalshi and
Polymarket adopted new internal rules: Kalshi banned political
candidates from trading on their own campaigns and sports insiders from
trading sports contracts. Polymarket barred trading by anyone with
confidential information relevant to a contract's outcome. But platform
self-regulation lacks the investigative powers, subpoena authority, and
criminal penalties of federal enforcement. Representative Ritchie Torres
introduced the Public Integrity in Financial Prediction Markets Act of
2026 to extend STOCK Act-style obligations into prediction markets, but
as of mid-2026 no federal insider trading framework for event contracts
exists.

### The Gambling Boundary

A persistent tension in prediction markets is the blurry line between
forecasting and gambling. Of Kalshi's $263.5 million in fee revenue in
2025, 89% came from sports contracts. The platform's Super Bowl Sunday
2026 volume reached $871 million, most tied to the game itself. This has
attracted regulatory and political opposition: Senators Adam Schiff and
John Curtis introduced the "Prediction Markets Are Gambling Act" in
March 2026, which would ban sports event contracts on prediction
platforms. Minnesota passed a state-level ban scheduled to take effect
August 2026, triggering lawsuits from Kalshi, Polymarket, and the CFTC
itself, all arguing that federally regulated event contracts fall under
federal jurisdiction.

The regulatory ambiguity reflects a deeper question: is the distinction
between "trading" and "gambling" a matter of substance, or merely of
which regulator gets the jurisdiction? Prediction markets that derive
most of their revenue from sports contracts look increasingly like
sportsbooks that happen to use a derivatives regulatory framework. The
resolution of this debate will shape whether prediction markets evolve
into a legitimate forecasting infrastructure or a regulatory arbitrage
play.

## Evidence and Research Foundation

The academic case for prediction markets rests on four decades of
empirical research across multiple domains.

Berg, Nelson, and Rietz (2008) provided the most comprehensive
longitudinal evidence, comparing the Iowa Electronic Markets'
predictions against 964 national polls across five US presidential
elections from 1988 to 2004. The IEM was closer to the eventual outcome
74% of the time, and the advantage was largest for long-horizon
forecasts: markets significantly outperformed polls in every election
when forecasting more than 100 days in advance. The average absolute
error in the IEM's prediction of the two-party presidential vote share
was 1.33 percentage points on election eve, and 1.45 percentage points
across the five days before the election.

Arrow et al. (2008), in a review published in Science, synthesized
evidence from the IEM, Intrade, and other platforms and concluded that
prediction markets consistently outperform polls for election
forecasting, aggregate dispersed information more efficiently than any
individual expert, and remain accurate even with fewer than 100 active
traders. The paper, authored by a Nobel laureate and senior economists,
called for expanded legalization of prediction markets and highlighted
their potential applications in business, government, and science.

Wolfers and Zitzewitz (2004) published the foundational theoretical and
empirical review in the Journal of Economic Perspectives, demonstrating
that prediction markets were well-calibrated across thousands of events
and outperformed professional forecasters in sports, finance, and
elections. Their paper established the calibration framework -- comparing
implied probabilities against realized frequencies -- that remains the
standard evaluation methodology.

Dreber et al. (2015) applied prediction markets to a novel domain:
forecasting whether published psychology studies would replicate. The
markets correctly classified 71% of studies as replicable or
non-replicable, compared to 58% for expert survey forecasts. The
13-percentage-point advantage from financial incentives demonstrated
that the mechanism of putting money behind beliefs -- not just the
expertise of the participants -- is what drives market accuracy.

Cowgill and Zitzewitz (2015) studied internal prediction markets at
Google, Hewlett-Packard, and Intel, finding that they accurately
forecasted product launch dates, project timelines, and quarterly
metrics, outperforming both management estimates and statistical models.
The study also provided evidence on incentive design: real-money markets
produced the most accurate forecasts, followed by play-money markets,
followed by reputation-based systems without monetary stakes.

The Georgetown University Psaros Center report by Lux and Sapozhnikov
(2026) provides the most current overview, documenting the sector's
growth from niche academic experiment to $64 billion in annual volume,
and cataloguing the regulatory challenges, manipulation incidents, and
institutional adoption patterns that define the current landscape.

## Implications

For forecasters: prediction markets are one of the most powerful tools
available for improving judgment under uncertainty -- but they are a
tool, not an oracle. The strongest approach combines market-derived
probabilities with independent analysis, using markets as an input that
can be challenged rather than a forecast to be accepted uncritically.
The superforecasting research of Tetlock and colleagues shows that the
best human forecasters outperform prediction markets by combining base
rates, outside-view reasoning, and continuous updating -- exactly the
practices that make markets work.

For decision-makers: prediction markets offer a way to escape the
limitations of expert panels and committee decision-making. Internal
corporate prediction markets can surface information that hierarchical
organizations suppress. When Google ran internal markets on product
launch dates, the market prices were more accurate than the project
managers' own estimates -- because individual engineers who knew about
technical obstacles could bet on delays without going through management
channels. The market flattened the organization's information hierarchy.

For the broader information ecosystem: the rise of Polymarket and Kalshi
changes how the public consumes probability. During the 2024 election,
many people tracked Polymarket prices alongside polling averages as
complementary information sources. This represents a shift from
narrative-driven media ("Candidate X has momentum") to
probability-driven media ("Candidate X has a 62% chance of winning").
Whether this improves public understanding depends on whether consumers
understand what a 62% probability means -- that the event should NOT
happen 38% of the time. Poor calibration literacy can make prediction
markets misleading rather than informative. A generation raised on
prediction market prices may develop stronger probabilistic intuitions
than any before it, but only if platforms invest as heavily in
calibration education as they do in user acquisition.

For regulators: the central challenge is designing a framework that
preserves the information-aggregation benefits of prediction markets
while preventing the manipulation, insider trading, and gambling-adjacent
practices that undermine their legitimacy. The current patchwork -- CFTC
regulation of some platforms, state-level bans, platform self-regulation
for insider trading -- is unstable. The Georgetown report's assessment
that the sector could reach $1 trillion in volume by 2030 means the
stakes of getting regulation right are high. A well-regulated prediction
market ecosystem could become genuine public infrastructure for
probability assessment, analogous to how securities markets became
infrastructure for capital allocation. A poorly regulated one will cycle
between boom and scandal until public trust collapses. The most likely
path is something in between: a gradual codification of rules around
insider trading, market manipulation, and contract eligibility that
legitimizes the most socially valuable markets while restricting
categories (war, assassination, sensitive national security events) that
create perverse incentives or endanger lives.

## Sources

1. Arrow, K. et al. (2008). "The Promise of Prediction Markets."
   Science, 320(5878), 877-878.
   https://doi.org/10.1126/science.1157679 [high]

2. Wolfers, J. & Zitzewitz, E. (2004). "Prediction Markets." Journal
   of Economic Perspectives, 18(2), 107-126.
   https://doi.org/10.1257/0895330041371321 [high]

3. Berg, J., Nelson, F. & Rietz, T. (2008). "Prediction market
   accuracy in the long run." International Journal of Forecasting,
   24(2), 285-300.
   https://doi.org/10.1016/j.ijforecast.2008.03.007 [high]

4. Dreber, A. et al. (2015). "Using prediction markets to estimate the
   reproducibility of scientific research." PNAS, 112(50), 15343-15347.
   https://doi.org/10.1073/pnas.1516179112 [high]

5. Cowgill, B. & Zitzewitz, E. (2015). "Corporate Prediction Markets:
   Evidence from Google, Ford, and Firm X." Review of Economic Studies,
   82(4), 1309-1341. https://doi.org/10.1093/restud/rdv014 [high]

6. Lux, M. & Sapozhnikov, M. (2026). "The Wisdom of the Crowds: The
   Rise of Prediction Markets." Georgetown University Psaros Center for
   Financial Markets and Policy.
   https://finpolicy.georgetown.edu/wp-content/uploads/2026/07/Wisdom-of-Crowds-Rise-of-Prediction-Markets-.docx.pdf [medium]

7. PredScope (2026). "How Accurate Are Prediction Markets? The Data."
   https://predscope.com/guide/prediction-market-accuracy [medium]

## See Also

- `library/probabilistic-thinking-forecasting/superforecasting.md` --
  Tetlock's research on how the best human forecasters combine base
  rates, outside-view thinking, and continuous updating -- practices
  that also make prediction markets work.
- `library/probabilistic-thinking-forecasting/calibration-and-overconfidence.md` --
  the calibration standard that prediction markets are measured against
  and why well-calibrated probabilities are rare in human judgment.
- `library/probabilistic-thinking-forecasting/inside-outside-view.md` --
  Kahneman's distinction between the inside view (forecasting from
  case-specific details) and the outside view (forecasting from base
  rates of similar cases) -- markets naturally implement the outside
  view by aggregating reference class information.
