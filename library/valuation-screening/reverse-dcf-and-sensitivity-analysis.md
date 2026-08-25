---
name: reverse-dcf-and-sensitivity-analysis
id: 20260825T141656Z
tier: library-topic
domain: valuation-screening
author: Library-Runner
tags: [reverse-dcf, implied-growth, sensitivity-analysis, scenario-analysis, valuation, expectations-investing, monte-carlo]
links: [library/valuation-screening/discounted-cash-flow-dcf-methodology.md, library/valuation-screening/cost-of-capital-capm-wacc-erp.md, library/valuation-screening/terminal-value-dcf-methods-and-biases.md, library/value-investing/margin-of-safety.md]
---

# Reverse DCF and Sensitivity Analysis -- Why Stress-Testing Your Assumptions Beats Guessing Your Answer

Reverse DCF inverts the standard discounted cash flow model: instead of
guessing a growth rate and solving for intrinsic value, it takes the
observable market price as given and solves backward for the growth and
profitability assumptions that price already implies. The result is a
single, testable number -- the implied growth rate -- that strips away
the analyst's optimism bias and forces a concrete question: is what the
market has priced in actually achievable? Sensitivity analysis is the
companion discipline that maps how valuation outputs shift when key
assumptions move within plausible ranges, transforming a brittle point
estimate into a defensible range. Together, these two tools are the
valuation analyst's humility checks -- they reveal how much optimism or
pessimism a thesis requires relative to consensus, and they expose
which assumptions carry the most leverage over the final answer.

## Background

The intellectual foundation of reverse-engineering market expectations
belongs to Alfred Rappaport and Michael Mauboussin, whose 2001 book
"Expectations Investing: Reading Stock Prices for Better Returns"
(revised and updated in 2021) formalized the approach. Their central
thesis was that investors should not try to forecast the future from
scratch -- an exercise plagued by optimism bias and overconfidence --
but should instead read the expectations already embedded in the
stock price and then judge whether those expectations are too high,
too low, or about right. Rappaport, who had earlier authored "Creating
Shareholder Value" (1986), supplied the free-cash-flow framework;
Mauboussin, then at Credit Suisse and later at Legg Mason, supplied
the behavioral-finance lens that explained why conventional forecasting
so consistently fails. Their method, which they called price-implied
expectations (PIE) analysis, asked investors to solve for the value
drivers -- sales growth, operating margin, investment rates, and
forecast duration -- that the current price demanded, and then to
assess whether a company's competitive position and industry dynamics
could plausibly deliver those drivers.

The approach drew on earlier traditions. Aswath Damodaran, professor
at NYU Stern and the most prolific contemporary voice in valuation,
had long taught that every market price is already a DCF -- whether
or not anyone explicitly built one. The price reflects somebody's
aggregate assumptions about growth, margins, and risk, transmitted
through the buying and selling of every market participant. A reverse
DCF simply makes those latent assumptions explicit and falsifiable.
Damodaran extended the logic beyond individual stocks: his annual
implied equity risk premium (ERP) calculations apply the same
reverse-engineering principle to entire market indices, solving for
the risk premium that the index's current level implies given
consensus earnings forecasts. This macro application demonstrated that
the technique was not a narrow stock-picking trick but a general
framework for reading expectations at any scale.

Sensitivity analysis developed as a parallel discipline within
financial modeling. Its roots lie in operations research and decision
analysis, where techniques like the tornado chart (ranking variables
by their impact on an output) and Monte Carlo simulation (sampling
from distributions over many uncertain inputs) were developed in the
1960s and 1970s. The adaptation to DCF valuation was straightforward:
because a DCF model's output depends on a handful of high-leverage
assumptions -- the discount rate, the terminal growth rate, the
explicit-period growth rate, and the operating margin -- systematically
varying each one across a plausible range reveals which assumptions
matter most and how wide the band of reasonable valuations actually
is. The two-way data table (varying WACC against terminal growth) and
the scenario analysis (base, upside, downside cases) became standard
exhibits in investment banking pitchbooks, private equity memos, and
fairness opinions -- not as afterthoughts, but as the primary
communication of valuation uncertainty to decision-makers.

The cultural shift these tools represent is important. Traditional
DCF practice, especially among retail investors, tends toward false
precision: the analyst picks a growth rate that feels defensible, the
model obliges with a value to three decimal places, and the output is
presented as an intrinsic truth. Reverse DCF and sensitivity analysis
interrupt this pattern. The reverse DCF replaces the analyst's
guessed growth rate with the market's observable, falsifiable
expectation. The sensitivity table replaces the single point estimate
with a range that honestly depicts irreducible uncertainty. Together
they shift the analyst's job from forecasting the unknowable to
stress-testing the knowable -- a humbler and more productive frame.

## Core Concepts

### The Reverse DCF Inversion

A conventional DCF works forward: given assumptions about future free
cash flow growth, the discount rate, and terminal value, it solves
for intrinsic value per share. The reverse DCF inverts this: given
the current market price (and thus the market-implied enterprise
value), it solves backward for the growth rate the price implies.
The underlying equation is identical -- only the known and unknown
variables are swapped.

The formal setup treats the standard DCF equation as a root-finding
problem. For a company with current free cash flow FCF0, a discount
rate WACC, a terminal growth rate g_t, and an explicit forecast
horizon of n years, the enterprise value is:

EV = sum( FCF0 * (1+g)^t / (1+WACC)^t, t=1..n ) + TV / (1+WACC)^n

where TV = FCF0 * (1+g)^n * (1+g_t) / (WACC - g_t).

In the forward DCF, g is the input and EV is the output. In the
reverse DCF, the market-implied EV is the input (calculated as market
capitalization plus net debt minus cash) and g is the solved output.
Because the equation has no closed-form solution when n > 1 and
terminal value is included, the growth rate is found numerically --
typically via Excel's Goal Seek, a binary search algorithm, or an
iterative solver that converges on the growth rate making the model's
calculated EV equal the observed EV.

### The Implied Growth Rate as a Diagnostic

The implied growth rate is the single most important output of a
reverse DCF. It answers a precise question: what annual free cash flow
growth rate, sustained over the explicit forecast period, would
make the current stock price exactly fair value? This number is a
diagnostic, not a prediction. Its value lies in comparison against
reference points:

1. **Historical growth:** If the implied rate is 18% but the company
   has grown FCF at 10% over the past five years, the market is pricing
   in a substantial acceleration. The investor must decide whether a
   specific, articulable reason exists for that acceleration.

2. **Peer growth:** Running the same reverse DCF on three to five
   close peers produces a peer-implied growth cluster. If the subject
   company implies 15% while peers cluster at 8-10%, the investor is
   paying a premium that requires a competitive justification expressed
   in numbers, not adjectives.

3. **Sell-side consensus:** If the implied rate exceeds the consensus
   three-year FCF growth estimate, the market is betting on upside
   beyond what the analysts who follow the company most closely are
   projecting. That gap is the location of the disagreement -- and the
   investment thesis lives in that gap.

The comparison, not the absolute number, is the decision input. An
implied growth rate of 12% is aggressive for a mature industrial
growing at 4% historically, but conservative for a software compounder
growing at 20%. Context converts the number into a judgment.

### The Single-Stage Shortcut

For a quick, approximate read, a single-stage reverse DCF collapses
the model to a perpetuity. Under the Gordon Growth Model, if a
company's free cash flow is expected to grow at a constant rate
forever, then EV = FCF1 / (WACC - g), which rearranges to:

g(implied) = WACC - (FCF1 / EV)

This shortcut is crude -- it ignores the multi-stage reality of most
businesses, where growth is high in the explicit period and tapers to
a terminal rate -- but it is useful for a rapid sanity check. If the
single-stage implied growth for a mature consumer staples company
comes out at 8%, that alone signals the price is demanding far more
than perpetual GDP-level growth, and a full multi-stage model is
warranted to confirm.

### Sensitivity Analysis: One-Way and Two-Way Data Tables

Sensitivity analysis varies one or two model inputs across a
plausible range and observes how the output changes. The two
fundamental tools are the one-way and two-way data tables.

A **one-way data table** varies a single input -- say, the terminal
growth rate from 1.5% to 4.0% in 0.5% increments -- holding all other
assumptions at base case, and displays the resulting intrinsic value
for each. It reveals the direction and steepness of the relationship:
does a 1% change in terminal growth move the valuation by 5% or by
25%? This isolates the marginal sensitivity of each assumption and
identifies which inputs deserve the most analytical attention.

A **two-way data table** varies two inputs simultaneously -- typically
WACC across rows and terminal growth rate across columns -- producing
a matrix of outputs. This is the workhorse of valuation sensitivity
analysis because it captures the interaction between the two
highest-leverage assumptions. The standard presentation highlights the
base case cell and shades the "reasonable range" -- the combination
of WACC and terminal growth that both the analyst and a skeptical
reader would accept as defensible. The corners of the matrix show
extreme combinations that may be unrealistic but provide bounds on
the full possible range.

The practical insight from two-way tables is that the interaction
between WACC and terminal growth is non-linear and sometimes
counterintuitive. Raising WACC by 1% does not reduce value by a fixed
percentage; the effect is amplified by terminal value dominance. When
terminal value is 80% of enterprise value, the discount rate is
compounding against a large, distant number, so small changes in
either WACC or terminal growth produce outsized swings in the final
answer. The two-way table makes this leverage visible.

### Scenario Analysis: Base, Upside, and Downside

Where sensitivity analysis varies individual inputs mechanically,
scenario analysis constructs three coherent, internally consistent
valuation cases. The **base case** uses the analyst's central
estimates for every assumption. The **upside case** applies
optimistic-but-plausible assumptions across the board -- higher
growth, higher margins, lower discount rate. The **downside case**
applies pessimistic-but-plausible assumptions. The discipline is
that each scenario must be a self-consistent story: a high-growth
scenario must include the reinvestment that growth requires; a
low-margin scenario must reflect the competitive pressure that
causes margin compression.

Scenario analysis differs from sensitivity analysis in a crucial
way. Sensitivity tables hold the world still and move one or two
dials; scenario analysis moves the whole world at once. The two are
complementary: sensitivity analysis tells you which assumptions
matter most, and scenario analysis tells you what plausible
combinations of those assumptions would produce. Best practice
presents both -- the sensitivity tables as the mechanical
explanation of why the range is what it is, and the scenarios as
the narrative framing of the range for a decision-maker.

### Tornado Charts: Ranking Assumptions by Impact

A tornado chart is a horizontal bar chart that ranks model inputs by
their impact on the output. Each variable is shown as a bar extending
left (downside) and right (upside) from the base case value, with the
longest bars representing the most influential assumptions. The chart
is built by varying each assumption individually from its low to high
end while holding all others at base case, measuring the swing in
enterprise value, and sorting from largest to smallest swing.

The tornado chart answers a question that sensitivity tables leave
implicit: of all the uncertain inputs in the model, which ones
deserve the most analytical effort? If the WACC bar is twice as wide
as the revenue growth bar, the analyst should spend more time
defending the discount rate than debating the top-line forecast. This
prioritization is valuable because analyst time is finite and the
marginal return on refining a low-impact assumption is near zero.

A critical caveat: tornado charts show sensitivity (the magnitude of
impact when an assumption changes), not risk (the likelihood that the
assumption will change). A variable with high sensitivity but low
uncertainty is low risk; a variable with moderate sensitivity but
high uncertainty may be the true risk driver. Sophisticated analysts
combine the tornado ranking with a qualitative or quantitative
uncertainty assessment to identify the assumptions that are both
high-impact and high-uncertainty -- the true risk concentrations.

### Monte Carlo Simulation

Monte Carlo simulation extends sensitivity analysis from one or two
variables to all uncertain inputs simultaneously. Instead of picking
point estimates, the analyst assigns each uncertain assumption a
probability distribution (e.g., triangular, normal, uniform) defined by
a low, base, and high estimate. The simulation then draws random
samples from each distribution thousands of times, recalculating the
full model each iteration, and produces a distribution of possible
outcomes -- a histogram of intrinsic values rather than a single
number or a small matrix.

The output is richer than any data table: a probability-weighted
range with percentiles (the 10th percentile downside, the 90th
percentile upside), a mean and median, and the shape of the
distribution (symmetric, skewed, fat-tailed). This captures the full
interaction space among all uncertain inputs, which two-way tables
necessarily miss because they can only show the interaction between
exactly two variables at a time.

The limitation is that the quality of the output depends entirely on
the quality of the input distributions. If the analyst assigns a
uniform distribution to a terminal growth rate because the true
distribution is unknown, the simulation produces a range that looks
precise but is built on a speculative foundation. Monte Carlo is most
valuable when the input distributions can be grounded in historical
data, industry benchmarks, or genuine expert elicitation -- not when
they are guesswork dressed in statistical clothing.

### Reverse DCF and Sensitivity Analysis as a Combined Discipline

The reverse DCF and sensitivity analysis are most powerful when used
together. The reverse DCF produces a single implied growth rate given
fixed WACC and terminal growth assumptions. But those assumptions are
themselves uncertain. Running the reverse DCF across a sensitivity
grid -- varying WACC by plus or minus 1% and terminal growth by plus
or minus 0.5% -- produces a range of implied growth rates rather than
a single number. This range is the honest answer to the question
"what is the market pricing in?" because it acknowledges that the
implied growth rate is itself a function of assumptions the analyst
cannot pin down precisely.

When the implied growth rate stays unreasonably high across the
entire sensitivity grid -- meaning no defensible combination of WACC
and terminal growth produces an implied rate close to the company's
historical performance -- the stock is expensive by any reasonable
measure. When the implied rate drops below historical growth even at
conservative WACC and terminal assumptions, the market is pricing in
deterioration that may or may not materialize. The grid does not
deliver a verdict; it narrows the question to the specific
disagreement between the market's expectations and the analyst's
assessment of the business.

## Evidence

### The Expectations Investing Framework

Rappaport and Mauboussin (2001, revised 2021) provided the foundational
academic and practitioner treatment of price-implied expectations. In
"Expectations Investing," they demonstrated that solving for the value
drivers a stock price implies -- rather than forecasting those drivers
independently -- systematically removes the optimism bias that plagues
conventional DCF. Their worked examples (Gateway, Domino's) showed how
extending the forecast period until the present value of free cash
flows matches the current price reveals the market-implied forecast
horizon and the growth rate it embeds. The method was later adopted
and extended by practitioners across buy-side and sell-side research,
and the book remains a core reference in valuation curricula.

### Terminal Value Dominance and Sensitivity Magnitude

Empirical work consistently shows that terminal value accounts for
60-80% of enterprise value in standard DCF models. The CFA Institute
(2025) notes that terminal value "often accounts for up to 80% of
total valuation" and rests on assumptions about survival and
prosperity decades into the future. This dominance has a direct
implication for sensitivity analysis: because terminal value is
calculated as FCF_final * (1 + g_t) / (WACC - g_t), small changes in
either WACC or terminal growth produce leveraged swings. Changing
the terminal growth rate from 2% to 3% when WACC is 9% raises the
terminal value multiplier from 14.3x to 16.7x -- a 17% increase in
terminal value from a one-percentage-point input change. This is why
the two-way WACC-by-terminal-growth table is the standard first
sensitivity exhibit in professional valuation work.

### Implied Growth Rate Sensitivity to WACC

Practitioner evidence documents the high sensitivity of implied growth
rates to the discount rate assumption. Analyses from Basis Report
(2026) and Alphactor (2026) show that a 2% change in WACC can shift
the implied growth rate by 2-4 percentage points. A higher WACC
lowers the present value of future cash flows, requiring a higher
growth rate to justify the same current price. This sensitivity is why
professional analysts always present a sensitivity strip (implied
growth at WACC plus or minus 1%) alongside any headline implied growth
figure. Two analysts using identical free cash flow data can publish
wildly different implied growth rates for the same stock on the same
day -- not because they disagree about the company, but because they
disagree about WACC by 50-100 basis points. A bare implied growth
number with no stated WACC is not analysis; it is a number with no
context.

### Case Study: The Software Compounder

A practitioner case from Alphactor (2026) illustrates the method's
value. A mature software compounder traded at 28x forward free cash
flow. A conventional DCF built by one analyst said "fairly valued" at
11% growth; another said "undervalued" at 13%; a third said
"overvalued" at 9%. Three analysts, three "right" answers, each
reflecting the assumptions they walked in with. The reverse DCF,
holding WACC at 9% and terminal growth at 2.5%, produced an implied
growth rate of 11.6%. Comparison against reference points revealed
convergence against the price: the company's own five-year realized
growth was 9.2% (240 basis points below implied), peer implied growth
clustered at 8-10% (250 basis points below), and sell-side consensus
was 10.5% (110 basis points below). No single comparison was damning,
but the convergence was: every available reference point sat below the
implied rate. The investor passed, unable to articulate a one-sentence
reason the business would outgrow its history and peers by 100-plus
basis points for a decade. The stock underperformed by 14 points over
the subsequent nine months as consensus estimates were trimmed. The
reverse DCF did not forecast the decline; it made the bet the investor
would have been taking visible in a single, testable number.

### Case Study: Trent Limited and Hypergrowth Pricing

A worked example from FinPAB (2026) demonstrates reverse DCF applied
to a high-multiple growth retailer, Trent Limited, in the Indian
market. Solving iteratively, the implied FCF growth rate converged at
33.9% -- the annual growth the market price required over the
explicit forecast period. The sensitivity table showed implied growth
ranging from 26.8% to 39.1% across plausible WACC (10.5%-12.5%) and
terminal growth (5.5%-7.5%) combinations. This range is the honest
output: rather than claiming precision the model cannot deliver, the
sensitivity grid showed that the market was pricing in roughly three
decades of hypergrowth under any defensible set of discount rate
assumptions. The implied rate was then compared against historical
performance, industry capacity, and the competitive structure to judge
whether such growth was plausible. The grid did not deliver a
verdict, but it narrowed the question to whether a retailer could
sustain growth far above industry rates for a decade -- a question
answerable from business analysis, not from further modeling.

### Scenario Analysis in Professional Practice

Investment banking and private equity practice standardizes the
base-upside-downside scenario framework. IB Interview Questions (2026)
documents that sensitivity tables and scenario analysis appear in
virtually every pitchbook, board presentation, and fairness opinion
deliverable. The sensitivity table is typically formatted as a matrix
with the base case cell highlighted, the reasonable range shaded, and
extreme corner values providing bounds. The scenario-based range (base
to upside, base to downside) feeds into the "football field" chart as
the DCF valuation bar, while the sensitivity tables appear as
supporting exhibits explaining why the range is what it is. This
dual presentation -- mechanical sensitivity plus narrative scenarios
-- is the professional standard because it answers both "what drives
the number" and "what plausible outcomes exist."

## Implications

For investors, the combined discipline of reverse DCF and sensitivity
analysis reframes the valuation question in a way that is both more
honest and more actionable than conventional forecasting. Rather than
asking "what is this business worth?" -- a question that requires
estimating an unknowable future -- the reverse DCF asks "what does
today's price already require, and do I believe it?" This is a
question that can be tested against history, peers, and consensus.
The investor who knows that a stock's price implies 15% FCF growth
while the company has grown at 8% and peers cluster at 9% has a
concrete, bounded disagreement to resolve: either identify the
specific competitive advantage that justifies the premium, or
conclude the price is ahead of the fundamentals. This is a far more
productive frame than debating whether a self-built DCF model's
assumptions are "right" -- a debate that typically devolves into
defending the analyst's prior beliefs.

For analysts and modelers, sensitivity analysis is not optional -- it
is the bridge between a static forecast and actionable insight. A
DCF that outputs a single intrinsic value per share is incomplete and
misleading; it implies a precision the model does not possess. Every
valuation should present a range, typically through a two-way WACC
versus terminal growth sensitivity table and a three-case scenario
analysis. The tornado chart identifies which assumptions deserve the
most analytical effort, ensuring that the analyst's time is allocated
to the inputs with the highest leverage over the output. Monte Carlo
simulation, when input distributions can be grounded in data, provides
the fullest picture of valuation uncertainty -- a probability-weighted
range rather than a small matrix. The discipline of presenting
sensitivity is what separates a valuation that supports a decision
from one that manufactures false confidence.

For portfolio construction, the reverse DCF provides a consistent
framework for comparing expectations across holdings. Because the
implied growth rate is a standardized output -- the annual FCF growth
the current price requires -- it can be compared across companies,
sectors, and the portfolio as a whole. A portfolio where every holding
implies growth well above historical and peer benchmarks is a
portfolio priced for perfection, with thin margin for error if any
individual thesis disappoints. A portfolio where implied growth sits
at or below historical performance has a structural margin of safety
built into the aggregate expectations. This portfolio-level
expectations audit, performed by running the reverse DCF on each
holding, is a diagnostic that aggregate valuation metrics (portfolio
P/E, portfolio EV/EBITDA) cannot provide because those metrics do not
account for differences in growth, capital intensity, and competitive
durability across holdings.

For risk management specifically, the combination of reverse DCF and
sensitivity analysis identifies where the margin of safety is thin.
When the implied growth rate is highly sensitive to the WACC
assumption -- meaning a 1% change in WACC shifts the implied growth by
3-4 percentage points, crossing from "reasonable" to "aggressive" --
the investor knows that the thesis lives or dies on a discount rate
assumption they cannot pin down precisely. That knowledge is itself
the risk signal: a valuation whose conclusion flips on an assumption
within the model's irreducible uncertainty is a fragile thesis. The
honest response is not to pick the WACC that produces the desired
answer, but to acknowledge the fragility and size the position
accordingly, demand a wider margin of safety, or pass. The
sensitivity table, by making the fragility visible, is the tool that
enforces this discipline.

For corporate strategy and M&A, the reverse DCF has a natural
application that is often overlooked. An acquirer evaluating a target
can run a reverse DCF on the offer price to reveal the synergies and
growth the deal must deliver to justify that price. If the implied
growth rate embedded in the premium-offered price is 20% but the
target's standalone historical growth is 8%, the acquirer is betting
that synergies -- revenue cross-sell, cost removal, tax structuring --
will more than double the growth trajectory. That bet can be
decomposed: how much of the implied growth comes from cost synergies
(quantifiable from overlap analysis), how much from revenue synergies
(speculative and historically over-estimated), and how much from
pure multiple expansion (the most dangerous source, because it
depends on market sentiment, not fundamentals). The reverse DCF
makes the synergy requirement explicit and falsifiable before the
deal closes, when the acquirer can still walk away. Post-merger, the
same technique tracks whether realized performance is meeting the
implied expectations the acquisition price embedded -- a discipline
that integration reviews too often omit in favor of reported
earnings accretion, which can be manufactured by purchase accounting
and tells nothing about whether the deal's economic thesis is
playing out.

For behavioral discipline, perhaps the most underappreciated
implication of the reverse DCF is its power to counter the
confirmation bias that infects conventional valuation. When an
analyst builds a forward DCF, the temptation is to tune assumptions
until the model produces a value near the current price -- anchoring
the conclusion to the very market the analyst claims to be
independently assessing. The reverse DCF breaks this loop by making
the market's assumptions the output, not the target. The analyst
can no longer quietly nudge the growth rate to reach a predetermined
conclusion; the growth rate is solved, not chosen. This forced
objectivity is why disciplined investors treat the reverse DCF as a
gating check: any forward DCF whose growth assumption sits
significantly above the market-implied rate carries an implicit claim
that the analyst sees something the market does not, and that claim
must be supported by specific, articulable evidence -- not by the
comfort of a model that confirms a prior.

## Sources

1. Rappaport, A. & Mauboussin, M. (2021). "Expectations Investing:
   Reading Stock Prices for Better Returns." Revised and Updated.
   Columbia University Press. Chapter 5: "How to Estimate Price-Implied
   Expectations." https://doi.org/10.7312/maub20304-008 [high]

2. Wall Street Prep (2024). "Reverse DCF Model: Step-by-Step Guide to
   Understanding the Reverse DCF Model."
   https://www.wallstreetprep.com/knowledge/reverse-dcf-model/ [high]

3. Damodaran, A. (2012). "Investment Valuation: Tools and Techniques
   for Determining the Value of Any Asset." 3rd Edition. Wiley.
   Chapters on implied growth, reverse valuation, and the implied
   equity risk premium. [high]

4. CFA Institute (2025). "The Discounted Cash Flow Dilemma: A Tool
   for Theorists or Practitioners?" Enterprising Investor.
   https://rpc.cfainstitute.org/blogs/enterprising-investor/2025/
   the-discounted-cash-flow-dilemma-a-tool-for-theorists-or-practitioners [high]

5. IB Interview Questions (2026). "Sensitivity and Scenario Analysis
   in Valuation Models."
   https://ibinterviewquestions.com/guides/valuation-investment-banking/
   sensitivity-scenario-analysis-valuation-models [medium]

6. Alphactor (2026). "Reverse DCF: Solving for the Market's Implied
   Growth." https://alphactor.ai/blog/reverse-dcf-implied-growth [medium]

7. Basis Report (2026). "Reverse DCF Calculator: Implied Growth Rate."
   https://www.basisreport.com/tools/reverse-dcf-calculator [medium]

8. FinPAB (2026). "Reverse DCF -- Formula, Implied Growth Rate and How
   to Decode What the Market Already Believes."
   https://finpab.com/pages/resources/blog/reverse-dcf-india-2026.html [medium]

## See Also

- `library/valuation-screening/discounted-cash-flow-dcf-methodology.md`
  -- the forward DCF framework that the reverse DCF inverts; covers
  free cash flow calculation, terminal value, and the common errors
  that sensitivity analysis is designed to expose.
- `library/valuation-screening/cost-of-capital-capm-wacc-erp.md` --
  the discount rate whose estimation uncertainty drives much of the
  sensitivity that reverse DCF and two-way tables reveal.
- `library/valuation-screening/terminal-value-dcf-methods-and-biases.md`
  -- the terminal value assumptions whose leverage over the final
  answer makes them the dominant axis in every sensitivity grid.
- `library/value-investing/margin-of-safety.md` -- the buffer that
  sensitivity analysis quantifies: how much can assumptions be wrong
  before the investment thesis breaks.