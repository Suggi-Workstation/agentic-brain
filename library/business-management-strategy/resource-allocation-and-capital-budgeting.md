---
name: resource-allocation-and-capital-budgeting
id: 20260901T211535Z
tier: library-topic
domain: business-management-strategy
author: Library Runner
tags: [capital-allocation, capital-budgeting, npv, irr, hurdle-rate, real-options, internal-capital-markets, resource-allocation]
links: [library/finance/cost-of-capital-and-wacc.md, library/value-investing/capital-allocation.md, library/business-management-strategy/corporate-governance-board-effectiveness.md, library/business-management-strategy/executive-compensation-incentive-design.md, library/business-management-strategy/unit-economics-business-model-design.md]
---

# Resource Allocation and Capital Budgeting -- Why Deciding Where Every Dollar Goes Is the Most Important Job in the Company

Resource allocation and capital budgeting are the processes by which
organizations decide where to deploy their finite financial and
operational resources. These decisions -- which projects to fund, which
to reject, how much to reinvest versus return to shareholders, and how
to allocate capital across competing internal divisions -- determine
whether a company compounds value or destroys it over time. The tools
of capital budgeting (NPV, IRR, payback period, real options) provide
the analytical framework, but the real challenge is organizational:
who decides, under what incentives, and with what information. Warren
Buffett has repeatedly stated that capital allocation is the CEO's most
important job, and the empirical evidence confirms that systematic
differences in allocation skill produce dramatic differences in
long-run shareholder returns.

## Background

The intellectual history of capital budgeting begins with the
development of discounted cash flow (DCF) analysis in the early
twentieth century. Irving Fisher's 1930 work "The Theory of Interest"
established the foundational principle that the value of any asset
depends on the present value of its expected future cash flows,
discounted at a rate that reflects the time value of money and the
risk of those cash flows. This principle -- that a dollar today is
worth more than a dollar tomorrow, and that riskier cash flows deserve
higher discount rates -- became the bedrock of all modern investment
appraisal techniques.

The formalization of net present value (NPV) as a decision rule
followed in the decades after Fisher. The NPV rule states that a
project should be accepted if the present value of its expected cash
inflows exceeds the present value of its cash outflows, discounted at
the firm's cost of capital. This deceptively simple rule has a rigorous
foundation: under the assumptions of perfect capital markets, accepting
all positive-NPV projects maximizes shareholder wealth. The internal
rate of return (IRR) -- the discount rate at which NPV equals zero --
emerged as a complementary metric, expressing project returns as a
percentage that could be compared directly to the firm's hurdle rate.

The post-war era saw the diffusion of these tools from academic finance
into corporate practice. The Capital Asset Pricing Model (CAPM),
developed by Sharpe, Lintner, and Mossin in the 1960s, provided a
framework for estimating the cost of equity, which in turn made it
possible to calculate a firm's weighted average cost of capital (WACC).
WACC became the standard hurdle rate: the minimum return a project
must earn to create rather than destroy value. By the 1970s and 1980s,
NPV and IRR had become the dominant capital budgeting tools in large
corporations, displacing simpler metrics like payback period and
accounting rate of return, though these older metrics persisted as
supplementary screens.

A critical extension came with the recognition that traditional DCF
analysis undervalues projects with embedded flexibility. Stewart
Myers coined the term "real options" in 1977, drawing on the
Black-Scholes-Merton option pricing framework to argue that
corporate investments often contain valuable options -- the option to
expand, the option to abandon, the option to delay, the option to
contract. These options have value that static NPV calculations
ignore, particularly in environments with high uncertainty and
irreversibility. The real options literature, developed by Trigeorgis,
Brennan, Schwartz, Dixit, and Pindyck among others, formalized the
idea that managerial flexibility itself is a source of value that
should be priced and incorporated into investment decisions.

Parallel to the development of analytical tools, a separate literature
emerged examining the organizational and behavioral dimensions of
capital allocation. Michael Jensen's 1986 free cash flow hypothesis
argued that managers with excess cash flow tend to overinvest rather
than return it to shareholders, because growth increases their
compensation, power, and job security. This agency-theoretic view
framed capital allocation as a principal-agent problem: the tools
were sound, but the incentives to use them correctly were often
misaligned. Jeremy Stein's 1997 work on internal capital markets
showed that corporate headquarters can add value by "winner-picking" --
actively shifting funds from weaker to stronger divisions -- but
subsequent research by Scharfstein, Stein, and others showed that
internal capital markets are also prone to "socialism," where weaker
divisions are subsidized at the expense of stronger ones due to
divisional rent-seeking and CEO-level agency problems.

The behavioral finance literature added a third dimension. Gervais,
Heaton, and Odean showed that overconfident managers overinvest,
initiate too many projects, and hold onto unprofitable investments
longer than rational managers. The sunk cost fallacy and escalation of
commitment -- well-documented in psychological research -- cause
organizations to continue funding failing projects because of prior
investments rather than expected future returns. These behavioral
biases operate alongside agency problems to distort capital allocation
in ways that the analytical tools alone cannot correct.

Warren Buffett and Charlie Munger brought these threads together from
the practitioner's perspective. Buffett has stated repeatedly that
the most important job of a CEO is capital allocation, yet most CEOs
arrive in the role without having developed allocation skills.
Operations, sales, marketing, and engineering are the typical career
paths to the corner office, and none of them involve making
investment decisions about how to deploy large sums of capital.
Thorndike's "The Outsiders" (2012) documented eight CEOs whose
extraordinary returns came not from operational excellence but from
superior capital allocation: buying back stock when it was cheap,
making contrarian acquisitions, and returning cash to shareholders
when reinvestment opportunities did not clear the hurdle rate.

## Core Concepts

### Net Present Value (NPV)

NPV is the foundational capital budgeting metric. It calculates the
difference between the present value of a project's expected cash
inflows and the present value of its cash outflows, all discounted at
the firm's cost of capital. The decision rule is straightforward:
accept any project with positive NPV, reject any with negative NPV.
The logic is that a positive-NPV project adds more value to the firm
than it costs, measured in today's dollars. NPV is denominated in
absolute currency terms, which makes it the only metric that directly
measures the dollar value a project creates. A project with an NPV of
$2 million adds $2 million of value to the firm, regardless of its
size.

The CFA Institute's capital allocation curriculum identifies NPV as
the primary tool for estimating the increase in firm value from a
project. NPV accounts for the time value of money, making it more
reliable than payback period or accounting return for evaluating
long-term projects and large capital investments. However, NPV
depends critically on two inputs: the projected cash flows and the
discount rate. Errors in either can produce misleading results. Cash
flow projections are subject to optimism bias, strategic
misrepresentation by project sponsors, and genuine uncertainty about
the future. The discount rate -- typically the WACC or a risk-adjusted
hurdle rate -- reflects assumptions about the firm's capital structure,
market risk, and the project's specific risk profile.

NPV has an important limitation when comparing projects of different
sizes. A $10 million project with an NPV of $1 million and a $100
million project with an NPV of $1 million both add the same absolute
value, but the smaller project creates more value per dollar invested.
The profitability index (PI) -- NPV divided by the initial investment
-- addresses this by measuring value created per dollar of capital
deployed. When capital is constrained, ranking projects by PI rather
than NPV produces a more efficient allocation.

### Internal Rate of Return (IRR)

IRR is the discount rate at which a project's NPV equals zero. It
represents the project's expected annualized percentage return, making
it intuitive and comparable across projects of different sizes. The
decision rule: accept a project if its IRR exceeds the hurdle rate,
reject if it falls below. IRR is widely used in practice because
percentage returns are easier to communicate to non-financial
managers and board members than absolute dollar figures.

IRR has well-documented limitations. First, it can produce multiple
solutions when a project has unconventional cash flows (cash flows
that change sign more than once, such as a project requiring
significant mid-life refurbishment). Second, IRR implicitly assumes
that interim cash flows are reinvested at the IRR itself, which may
be unrealistic for high-IRR projects. The modified IRR (MIRR)
addresses this by assuming reinvestment at the cost of capital. Third,
IRR can give misleading rankings when comparing mutually exclusive
projects of different sizes or different durations: a project with a
higher IRR may have a lower NPV, and the NPV ranking is the correct
one for value maximization.

Despite these limitations, IRR remains valuable when used alongside
NPV. The two metrics are complementary: NPV measures absolute value
creation, IRR measures return efficiency. The CFA Institute
recommends using both together to get a complete picture of a
project's attractiveness. The common practice is to require both a
positive NPV and an IRR above the hurdle rate before approving a
project.

### Hurdle Rate and WACC

The hurdle rate is the minimum acceptable rate of return for an
investment. It is the bar a project must clear. In its simplest form,
the hurdle rate equals the firm's WACC -- the blended cost of debt and
equity financing, weighted by their proportions in the capital
structure. WACC represents the opportunity cost of capital: the return
shareholders and creditors could earn on alternative investments of
equivalent risk. Any project that earns less than WACC destroys value,
because the firm is paying more for its capital than it is earning
from deploying it.

A more refined approach adjusts the hurdle rate for project-specific
risk. A company with a WACC of 10% might set a hurdle rate of 12%
for a low-risk project (such as replacing existing equipment) and 20%
for a high-risk project (such as entering a new market). The risk
premium reflects the uncertainty of the project's cash flows and the
irreversibility of the investment. The Corporate Finance Institute
notes that most companies use WACC as the baseline hurdle rate, then
add risk premiums for specific projects based on their risk profile.

Hurdle rates also serve a behavioral and organizational function.
When division managers submit project proposals, they have incentives
to overstate projected returns and understate costs to secure funding
for their divisions. Inflated hurdle rates act as a correction for
this optimism bias: by setting the bar higher than the true cost of
capital, headquarters filters out marginal projects whose positive
NPV depends on optimistic assumptions. The CFO survey evidence from
Hoang, Gatzer, and Ruckes (published in Management Science, 2025)
confirms that firms use inflated hurdle rates as one of several
mechanisms to counteract division-level information bias.

### Payback Period and Accounting Rate of Return

Payback period measures how long it takes for a project to recover its
initial investment. It is simple, intuitive, and useful for assessing
liquidity risk -- a project that pays back in two years ties up
capital for less time than one that pays back in ten. However,
payback period ignores the time value of money (in its simple form)
and ignores all cash flows after the payback point. A project that
returns its investment in three years and then generates nothing for
the remaining seventeen years of its life looks identical to one that
returns its investment in three years and then generates large cash
flows for seventeen more years.

The accounting rate of return (ARR) divides average accounting profit
by average investment. It uses accounting figures rather than cash
flows, which means it is distorted by depreciation policies,
inventory valuation methods, and other accounting choices. Neither
payback period nor ARR is theoretically sound as a primary decision
criterion, but both remain in use as supplementary screens --
particularly in smaller firms or for smaller projects where the cost
of full DCF analysis is not justified.

### Real Options

Real options analysis applies financial option pricing techniques to
capital budgeting decisions. A real option is the right, but not the
obligation, to take a specific action related to a capital investment:
defer, expand, contract, abandon, or stage the investment. The key
insight is that traditional NPV treats investment as a "now or never"
decision, but most real-world investments involve sequential
commitments under uncertainty, where managers can adjust their plans
as new information arrives.

The value of a real option comes from the asymmetry it creates. The
holder of the option benefits from favorable outcomes (exercising the
option when conditions are good) but limits losses on unfavorable
ones (not exercising when conditions are bad). This asymmetry means
that the value of a project with embedded options exceeds its static
NPV. The option to delay, for example, is valuable when investment is
irreversible and uncertainty is high: waiting allows the firm to
observe market conditions before committing. The option to abandon is
valuable because it caps downside losses. The option to expand is
valuable because it preserves upside potential.

Real options are most valuable when three conditions hold
simultaneously: uncertainty is high, the investment is irreversible,
and management has genuine flexibility to change the project's course.
Pharmaceutical R&D, natural resource extraction, technology platform
investments, and real estate development are domains where real
options analysis adds the most value beyond static NPV. In these
contexts, the option to abandon a failed drug trial, delay a mine
opening, or scale a technology rollout can be worth more than the
project's static NPV suggests.

The limitations of real options analysis are practical rather than
theoretical. Estimating volatility for non-traded assets is difficult.
The computational complexity of multi-stage options (compound
options, sequential investments) can be high. The assumptions of
option pricing models -- particularly the ability to construct
replicating portfolios -- do not hold cleanly for real assets. As a
result, many firms use real options as a conceptual lens rather than
a precise calculation tool: they recognize that flexibility has value
and make qualitative adjustments to hurdle rates or project ranking
to account for it, rather than attempting exact option pricing.

### The Five Uses of Capital

Every dollar of free cash flow a company generates must go somewhere.
The five uses of capital are: (1) reinvest in the business through
capital expenditures and working capital, (2) acquire other companies,
(3) pay down debt, (4) pay dividends, and (5) repurchase shares. The
capital allocation framework requires comparing the expected return
of each use against the hurdle rate and choosing the highest-return
option.

Reinvestment in the business is value-creating only when the return
on invested capital (ROIC) exceeds the cost of capital (WACC). When
ROIC is above WACC, every dollar reinvested creates value and
management should deploy aggressively. When ROIC falls below WACC,
reinvestment destroys value regardless of revenue growth -- the
company is earning less on its capital than that capital costs. The
correct response is to return cash to shareholders rather than
empire-build. This is the core principle that connects capital
budgeting to value creation: growth without adequate returns is value
destruction.

Acquisitions are the most value-destructive use of capital on
average. The acquirer typically overpays, integration costs run long,
and synergies arrive late or not at all. Yet management teams return
to acquisitions repeatedly because deals increase firm size (which
increases executive compensation and prestige) and because the
optimism bias leads acquirers to believe they can extract synergies
that other acquirers could not. Disciplined acquirers -- those who
set clear price limits, require demonstrated ROIC above the hurdle
rate, and walk away from deals that do not meet their criteria -- are
rare but produce superior long-term returns.

Debt repayment reduces financial risk and improves the balance sheet.
It is the lowest-return use of capital in purely financial terms
(reducing debt saves the after-tax cost of interest, which is
typically below the return available from reinvestment or
acquisitions), but it is the safest. In high-interest-rate
environments, debt repayment becomes more attractive because the
after-tax interest cost rises, and in periods of financial stress,
a strong balance sheet is a competitive advantage.

Dividends and share buybacks return capital to shareholders. The
choice between them depends on tax considerations, signal effects,
and the firm's investment opportunities. Dividends are a visible,
sticky commitment that imposes discipline on management -- once a
dividend is established, cutting it sends a strong negative signal.
Buybacks are more flexible and tax-efficient but are also more easily
abused: management can repurchase shares at inflated prices to boost
short-term EPS and trigger compensation targets, destroying value for
continuing shareholders. Buffett's criterion is clear: buybacks
create value only when the stock trades below intrinsic value. Above
that price, every dollar spent on repurchases destroys value.

### Internal Capital Markets and Resource Reallocation

In multi-divisional firms, headquarters operates an internal capital
market: it collects cash flows from all divisions and reallocates
them across divisions based on investment opportunities. Jeremy
Stein's 1997 model showed that headquarters can create value through
"winner-picking" -- actively shifting funds from divisions with poor
investment prospects to those with strong prospects. Unlike external
capital markets (banks, public debt markets), headquarters has
control rights that enable it to override division-level preferences
and redirect resources. When winner-picking works, internal capital
markets allocate capital more efficiently than external markets could,
because headquarters has superior information about the relative
quality of the firm's divisions.

However, the empirical evidence shows that internal capital markets
frequently fail to allocate efficiently. Scharfstein (1998) found
that conglomerate division investment is virtually insensitive to
division investment opportunities (measured by industry Tobin's Q),
while standalone firm investment is significantly more sensitive --
a pattern he termed "socialism" in internal capital allocation. Weaker
divisions receive more capital than their prospects justify, and
stronger divisions receive less. The MIT working paper by Stein and
Scharfstein modeled this as a two-tiered agency problem: division
managers engage in rent-seeking to increase their bargaining power
and extract greater capital allocations, and the CEO -- who is herself
an agent of outside investors -- finds it less costly to distort
investment in favor of rent-seeking divisions than to pay their
managers higher cash wages.

The 2025 Management Science study by Hoang, Gatzer, and Ruckes
provides CFO survey evidence confirming that these agency problems
are real and pervasive. A majority of CFOs (56%) confirm
empire-building tendencies at the division level and attempts by
divisional managers to influence headquarters' allocation decisions
through lobbying and influencing activities. Firms counteract these
problems through layers of approval, divisional budgets, reporting
requirements, and compensation schemes that tie divisional manager
pay to overall firm performance. Inflated hurdle rates serve as a
correction for the systematic overstatement of project returns by
divisional managers. Despite these mechanisms, approximately 40% of
overall capital expenditures do not require explicit headquarters
approval -- a surprisingly high degree of decentralization that
reflects the tradeoff between the benefits of local information and
the costs of agency.

### Behavioral Biases in Capital Allocation

Capital budgeting is not purely a technical exercise. The humans who
make allocation decisions are subject to systematic cognitive biases
that distort their judgment. Overconfidence is the most documented:
managers systematically overestimate their ability to predict project
outcomes, leading to cash flow projections that exceed reality by
20-50% on average. The selection effect compounds this -- overconfident
individuals are more likely to seek management roles and more likely
to be promoted based on past successes that may have been partly
luck. Gervais, Heaton, and Odean formalized this in their behavioral
model of corporate investment, showing that overconfident managers
overinvest free cash flow, initiate too many projects, and persist
with unprofitable investments longer than rational managers.

The sunk cost fallacy and escalation of commitment cause organizations
to continue funding failing projects. The bias is well-documented:
decision-makers allocate additional capital to underperforming projects
because significant resources have already been invested, even when
the expected future NPV is negative. The psychological drivers include
loss aversion (abandoning a project feels like realizing a loss),
self-justification (admitting the initial decision was wrong damages
reputation), and organizational signaling (killing a high-profile
project is perceived as leadership failure). The result is that firms
routinely throw good money after bad, eroding shareholder value and
missing alternative opportunities.

Hurdle rate manipulation is a specific organizational bias. Managers
who want a favored "pet project" approved advocate for a lower hurdle
rate, while managers who want to block a competing division's project
argue for a higher one. The result is that capital allocation is
driven by internal politics rather than economic analysis. The CFA
Institute's curriculum explicitly identifies this as a common capital
allocation pitfall, alongside the failure to include opportunity
costs, double-counting benefits, and using the wrong discount rate
for the project's risk level.

## Evidence

### NPV and IRR in Corporate Practice

The CFA Institute's 2026 capital allocation refresher reading provides
the authoritative framework for how investment projects are evaluated
in practice. The reading identifies four categories of capital
investment: (1) going concern projects (maintaining operations),
(2) regulatory/compliance projects (mandated by law or regulation),
(3) expansion projects (growing existing or new markets), and (4)
other projects. Going concern and regulatory projects typically do
not require the same NPV analysis as expansion projects because they
are mandatory -- the decision is not whether to invest but how to
invest efficiently. Expansion projects are the primary domain of NPV
and IRR analysis, where the firm must choose among competing
opportunities.

The CFA curriculum emphasizes that before quantitative appraisal,
projects should be modeled according to certain principles: cash flows
measured on an after-tax basis, avoiding double counting, and
including the project's impact on the rest of the firm (positive
impacts like cost savings, negative impacts like cannibalization of
existing product sales). Return on invested capital (ROIC) serves as
a company-wide complement to project-level NPV and IRR: while NPV and
IRR evaluate individual projects, ROIC measures the firm's actual
return across all investments and can be compared to the cost of
capital to assess whether the firm is creating or destroying value
overall. The curriculum also explicitly notes that capital allocation
is "prone to behavioral biases and cognitive errors," acknowledging
that the analytical framework is necessary but not sufficient.

The Corporate Finance Institute's capital planning guide reinforces
that no single metric should be used in isolation. A project with a
high IRR may seem attractive, but if its NPV is negative (possible
when cash flows are unconventional or when the project is small
relative to its IRR), it will not generate long-term value. The
profitability index becomes essential when capital is constrained:
it ranks projects by value created per dollar invested, ensuring that
the limited capital budget is allocated to the projects that produce
the most value per unit of capital.

### Internal Capital Markets: Winner-Picking and Socialism

Stein's 1997 Journal of Finance paper, "Internal Capital Markets and
the Competition for Corporate Resources," established the theoretical
foundation for understanding how headquarters creates (or fails to
create) value through internal resource allocation. Stein's model
shows that headquarters, unlike an external bank, has control rights
that enable "winner-picking" -- the active shifting of funds from one
project to another. By ranking projects by their returns and
reallocating capital accordingly, headquarters can create value even
when it cannot relax overall firm-wide credit constraints. An
important implication is that internal capital markets may function
more efficiently when headquarters oversees a small and focused set
of projects, because broader oversight dilutes the CEO's ability to
rank and reallocate effectively.

The "socialism" finding emerged in subsequent empirical work.
Scharfstein (1998) examined diversified conglomerates and found that
divisional investment was nearly insensitive to industry Q (a proxy
for investment opportunities), while standalone firm investment in
the same industries was significantly more sensitive. This means that
conglomerate headquarters was not allocating more capital to
divisions with better prospects -- it was spreading capital relatively
evenly across divisions regardless of their opportunities.
Crucially, Scharfstein found that the sensitivity of divisional
investment to Q increased as top management's equity stake rose,
implying that socialism is driven by misaligned incentives between
outside investors and management. When the CEO has low-powered
incentives (low equity ownership), the tendency to subsidize weak
divisions is more pronounced.

The MIT working paper by Stein and Scharfstein, "The Dark Side of
Internal Capital Markets," provided the theoretical mechanism:
divisional rent-seeking. Division managers invest in influence
activities -- lobbying, building coalitions, withholding cooperation
-- to increase their bargaining power with the CEO. Because the CEO is
an agent of outside investors (not the owner herself), she finds it
less personally costly to distort capital allocation in favor of
rent-seeking divisions than to pay their managers higher cash wages.
The outside investors would prefer cash compensation (which is
transparent and does not distort investment), but they cannot enforce
this preference because the hiring and retention of division managers
is delegated to the CEO. The result is a "socialist" allocation where
weaker divisions are subsidized by stronger ones.

### CFO Survey Evidence on Capital Allocation in Practice

The 2025 Management Science study by Hoang, Gatzer, and Ruckes
analyzed a unique CFO survey dataset to examine how capital allocation
actually works inside firms. Several findings stand out. First,
financial executives openly acknowledge within-firm agency problems:
56% confirm empire-building tendencies at the divisional level, and
56% confirm wasteful influencing activities (lobbying, propaganda)
by divisional managers seeking larger capital allocations. These
behaviors are complementary -- influencing activities are more severe
when empire-building tendencies are high (67.8% versus 40.4%).

Second, firms implement interconnected systems to counteract these
problems: layers of approval, divisional budgets, reporting
requirements, and compensation schemes tied to firm-wide performance.
Inflated hurdle rates serve as a correction for the systematic
overstatement of project returns by divisional managers. Third, top
management relies heavily on nonfinancial information -- particularly
assessments of divisional managers' abilities -- when making funding
decisions, a factor largely ignored in the theoretical literature but
recognized as important in practice.

Fourth, the degree of decentralization is surprisingly high:
approximately 40% of overall capital expenditures do not require
explicit headquarters approval. Firms trade off the benefits of local
information (lower information acquisition and processing costs) against
the costs of agency (loss of control, empire-building, monitoring
cost). Fifth, even firms with active internal capital markets tilt
allocation toward relatively even distributions, using capital
allocation as a credible communication device. Sixth, CFOs believe
that integrating multiple businesses into an internal capital market
produces tangible financial benefits -- lower costs of capital and
higher debt capacities -- supporting coinsurance arguments.

### The Glaser, LopezdeSilanes, and Sautner Study on Managerial Power

The Journal of Finance study by Glaser, LopezdeSilanes, and Sautner,
"Opening the Black Box: Internal Capital Markets and Managerial
Power," provided direct evidence of how power distorts capital
allocation. Using panel data on planned versus actual allocations in
a multinational conglomerate, they found that following cash
windfalls, more powerful division managers obtained larger allocations
and increased investment substantially more than less connected
peers. Critically, these powerful managers' units exhibited lower
ex post performance and productivity -- the additional capital was
misallocated, not directed toward the best opportunities. This
identifies cash windfalls as a specific source of misallocation and
managerial power as the channel through which misallocation occurs.

Xuan's 2009 Harvard Business School study, "Empire-Building or
Bridge-Building," added a nuance: new CEOs use the capital budget as
a tool to build coalitions. After CEO turnover, divisions not
previously affiliated with the new CEO receive significantly more
capital than divisions through which the CEO had advanced. This
"reverse favoritism" is more pronounced when the new CEO has less
authority or when unaffiliated divisions have more bargaining power.
The interpretation is that specialist CEOs use capital allocation to
elicit cooperation from powerful divisional managers they do not
control through personal relationships -- a political use of the
capital budget rather than an economic one.

### Behavioral Evidence: Overconfidence and Escalation of Commitment

Gervais, Heaton, and Odean's behavioral finance model of capital
budgeting demonstrates that overconfident managers make systematic
investment errors. Overconfident managers overestimate the precision
of their information and the accuracy of their projections, leading
them to overinvest when they believe projects are good (accepting
negative-NPV projects) and to undervalue projects they are uncertain
about (rejecting positive-NPV projects because they do not recognize
their own uncertainty). The selection effect is important: firms may
endogenously select and promote overconfident managers because
overconfident individuals are more likely to have generated extremely
good outcomes in the past (through luck as much as skill), making
them appear more competent.

The escalation of commitment literature, reviewed in the Journal of
Economic Psychology (2019), confirms that the sunk cost effect is
"severe, robust, and costly." Decision-makers continue with failing
courses of action despite negative feedback, leading to delayed or
absent termination of failing projects. The literature identifies
loss aversion as the primary driver: abandoning a project feels like
realizing a loss, and the pain of realizing the loss exceeds the
expected benefit of redirecting the capital. Organizational signaling
amplifies the effect: killing a high-profile project is perceived as
admitting failure, creating a reputational cost that outweighs the
financial benefit of stopping the loss. Debiasing strategies --
pre-mortem analysis, reference class forecasting, independent review
committees, explicit labeling of sunk costs -- can reduce but do not
eliminate the effect.

### Real Options in Practice

The comparative study by RSIS International (2025) examined real
options valuation versus traditional NPV in capital budgeting. The
study found that while NPV provides a deterministic view of project
viability, it fails to account for managerial flexibility under
uncertainty. Real options valuation, derived from financial option
theory, addresses this by valuing the strategic choices embedded in
investment projects -- the option to defer, expand, contract, or
abandon. In their pharmaceutical case study, a project with a
marginally positive NPV showed substantially higher strategic value
when the option to delay pending further trial results was priced,
reflecting the added value of flexibility.

The MDPI study on urban development projects (2025) provided a
concrete example: a project with negative NPV under static DCF
analysis became highly valuable when the deferral option was
incorporated. The option to wait for market conditions to improve
before committing to construction transformed a rejected project into
an accepted one. This illustrates the practical significance of real
options: in environments with high uncertainty and irreversibility,
static NPV can lead to systematic underinvestment in valuable
projects because it ignores the value of waiting and adapting.

However, the ScienceDirect study on managerial flexibility and
corporate investment cautioned that real options effects are strongest
when managers have genuine flexibility to respond to new information.
Firms with rigid organizational structures, long approval cycles, or
strong commitment escalation tendencies may not be able to exercise
the options their projects contain, rendering the option value
theoretical rather than real. The value of real options depends not
only on the project's characteristics but on the organization's
ability to act on new information -- a constraint that ties back to
organizational design and decision-making processes.

## Implications

### For CEOs and Senior Management

The most important implication for senior management is that capital
allocation is not a finance function delegated to the CFO -- it is
the CEO's primary job. Buffett's repeated emphasis on this point
reflects a structural reality: the CEO is the only person in the
organization who can make tradeoffs across all five uses of capital
(reinvestment, acquisitions, debt paydown, dividends, buybacks) and
across all divisions. Delegating these decisions to division managers
without oversight leads to the agency problems documented above.
Delegating to the CFO without strategic direction reduces allocation
to a spreadsheet exercise that misses the qualitative dimensions --
competitive positioning, management capability, strategic fit -- that
determine whether projects succeed.

The practical framework for CEOs is to establish a disciplined
allocation process with three components. First, set a clear hurdle
rate based on WACC plus appropriate risk premiums, and enforce it
consistently. Inflated hurdle rates can counteract division-level
optimism bias, but they must be applied uniformly -- allowing some
projects to bypass the hurdle rate through political advocacy
undermines the entire system. Second, require all project proposals
to include a clear statement of opportunity cost: what else could be
done with this capital, and why is this project better? Third,
conduct post-mortem analyses on completed projects to calibrate
future projections. The systematic overstatement of project returns
documented in the literature can only be corrected if the
organization tracks actual outcomes against projections and uses the
discrepancies to adjust future submissions.

For multi-divisional firms, the CEO must actively manage the internal
capital market. The evidence on "socialism" in internal capital
markets means that passive allocation -- letting each division keep
its own cash flow -- is not neutral; it systematically subsidizes weak
divisions at the expense of strong ones. Active winner-picking
requires headquarters to rank divisions by their risk-adjusted return
on capital and reallocate accordingly, even when this means stripping
resources from powerful division managers. The organizational cost of
this reallocation -- resistance, lobbying, reduced cooperation -- must
be weighed against the value of more efficient allocation. Xuan's
finding that new CEOs use the capital budget for "bridge-building"
suggests that the political costs of reallocation are real, but the
financial costs of failing to reallocate are larger.

### For Boards and Corporate Governance

Boards have a critical role in capital allocation oversight. The
board's primary lever is the approval threshold: setting the capital
expenditure level that requires board approval versus management
discretion. Too low a threshold burdens the board with operational
decisions; too high a threshold allows management to make large
investments without oversight. The right threshold depends on
company size, complexity, and the board's financial expertise, but
the principle is that any investment large enough to materially
affect the firm's value trajectory should receive board scrutiny.

Boards should also evaluate the capital allocation track record of
the CEO as a primary component of performance assessment. This means
looking beyond revenue growth and earnings to examine whether
reinvestment has generated returns above the cost of capital, whether
acquisitions have created or destroyed value (including post-deal
write-downs), and whether buybacks were executed below intrinsic
value or at inflated prices. The basis report framework for grading
capital allocation -- assessing reinvestment discipline, buyback
timing, M&A track record, and dividend sustainability -- provides a
structured approach for boards to evaluate this dimension.

Executive compensation design is the board's most powerful tool for
aligning capital allocation incentives. If compensation is tied to
revenue growth or firm size, managers have incentives to overinvest
and empire-build. If compensation is tied to ROIC or economic value
added (measures that subtract the cost of capital from operating
returns), managers have incentives to invest only in projects that
create value and to return excess cash to shareholders. The
connection between capital allocation and executive compensation is
direct: the compensation system determines whether the CEO's personal
interests align with value-creating allocation or value-destroying
empire-building.

### For Value Investors

For investors evaluating a company, capital allocation is the bridge
between business quality and investment returns. A company can
generate excellent returns on invested capital and still destroy
shareholder value if management deploys cash poorly. The investor's
task is to assess not just the business but the management team's
allocation skill and incentives. The key questions are: Does
reinvestment generate returns above the cost of capital? Are
acquisitions disciplined (clear price limits, demonstrated synergy
realization) or promiscuous (serial deals, repeated write-downs)?
Are buybacks executed below intrinsic value or at price peaks? Is the
dividend sustainable, covered by free cash flow rather than
borrowing?

The five-year to ten-year track record is the right evaluation
window. Capital allocation decisions compound over time, and
single-year outcomes can be noisy. The investor should examine the
trend in ROIC versus WACC (is the spread widening or narrowing?), the
trend in net debt relative to EBITDA (is the balance sheet
strengthening or weakening?), and the cumulative value of buybacks
relative to the share count (is ownership being concentrated or
diluted?). A company whose share count is rising despite large
buyback announcements is using buybacks to offset stock-based
compensation dilution rather than to return capital -- a red flag
that the buybacks are not creating value for outside shareholders.

The value-investing perspective on capital allocation, as articulated
by Buffett and Munger and documented by Thorndike, is that superior
allocation is a competitive advantage in itself. The "Outsider" CEOs
studied by Thorndike were not better operators -- they were better
allocators. They bought back stock when it was cheap, made
contrarian acquisitions when competitors were retreating, and
returned cash when reinvestment opportunities were inadequate. This
skill is rare because the career path to CEO rarely develops it, and
because the organizational pressures (empire-building incentives,
escalation of commitment, political coalition-building) push toward
overinvestment. Identifying a CEO with genuine allocation discipline
-- and the independence to exercise it against organizational pressure
-- is one of the highest-value judgments an investor can make.

### For Organizational Design

The capital allocation process is inseparable from organizational
structure. The degree of centralization in capital decisions shapes
the information flow, incentive alignment, and political dynamics
that determine allocation quality. The finding that approximately 40%
of capital expenditures do not require headquarters approval reflects
a deliberate tradeoff: decentralization captures the benefits of
local information (division managers know their markets, customers,
and operations better than headquarters), but it creates agency costs
(empire-building, influence activities, optimistic projections).

The organizational design response is to build systems that mitigate
the agency costs of decentralization without losing the information
benefits. These include: multi-level approval processes that create
independent review of project proposals; divisional budgets that cap
the capital any single division can deploy without escalation;
performance reporting that tracks actual returns against projections,
creating a track record that disciplines future submissions; and
compensation systems that tie divisional manager pay to firm-wide
performance rather than divisional size. The Hoang, Gatzer, and
Ruckes CFO survey confirms that firms use all of these mechanisms in
interconnected systems rather than relying on any single tool.

The design implication is that there is no single optimal degree of
centralization. The right balance depends on the firm's diversity of
businesses (more diverse businesses benefit more from local
information), the strength of agency problems (firms with strong
governance and aligned incentives can decentralize more), and the
volatility of the environment (volatile environments benefit from the
flexibility of local decision-making but require stronger monitoring
to prevent bias-driven overinvestment). The capital allocation system
should be designed as an integrated whole: hurdle rates, approval
thresholds, compensation, reporting, and governance all work together
or they fail together.

## Sources

1. CFA Institute. "Capital Investments and Capital Allocation."
   Refresher Reading, 2026 CFA Program.
   https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/capital-investments-and-capital-allocation [high]

2. Corporate Finance Institute. "Capital Planning Metrics: The Role
   of NPV, IRR, and Profitability Index."
   https://corporatefinanceinstitute.com/resources/valuation/capital-planning-metrics-guide/ [medium]

3. Corporate Finance Institute. "Hurdle Rate - Definition and
   Example."
   https://corporatefinanceinstitute.com/resources/valuation/hurdle-rate-definition/ [medium]

4. Stein, Jeremy C. (1997). "Internal Capital Markets and the
   Competition for Corporate Resources." Journal of Finance, 52(1),
   111-133.
   https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1997.tb03810.x [high]

5. Scharfstein, David S. and Stein, Jeremy C. "The Dark Side of
   Internal Capital Markets: Divisional Rent-Seeking and Inefficient
   Investment." MIT Working Paper.
   https://web.mit.edu/jcstein/www/newdarkjof.pdf [high]

6. Hoang, Daniel; Gatzer, Sebastian; and Ruckes, Martin E. (2025).
   "The Economics of Capital Allocation in Firms: Evidence from
   Internal Capital Markets." Management Science, 71(8), 6392-6425.
   https://pubsonline.informs.org/doi/10.1287/mnsc.2021.02755 [high]

7. Glaser, Markus; LopezdeSilanes, Florencio; and Sautner, Zacharias.
   "Opening the Black Box: Internal Capital Markets and Managerial
   Power." Journal of Finance.
   https://onlinelibrary.wiley.com/doi/10.1111/jofi.12046 [high]

8. Xuan, Yuhai (2009). "Empire-Building or Bridge-Building? Evidence
   from New CEOs' Internal Capital Allocation Decisions." Review of
   Financial Studies, 22(12), 4919-4948. Harvard Business School.
   https://www.hbs.edu/faculty/Pages/item.aspx?num=35034 [high]

9. Gervais, Simon; Heaton, J.B.; and Odean, Terry. "Behavioral
   Finance: Capital Budgeting and Other Investment Decisions."
   https://sites.duke.edu/sgervais/files/2020/05/Gervais.2010.BookChapter.pdf [high]

10. Thorndike, William. "The Outsiders: Eight Unconventional CEOs and
    Their Radically Rational Blueprint for Success." Referenced via
    Quartr Insights, "Decoding Capital Allocation."
    https://quartr.com/insights/business-philosophy/decoding-capital-allocation [medium]

11. "A Dozen Things I've Learned from Charlie Munger about Capital
    Allocation." 25iq.
    https://25iq.com/2015/10/03/a-dozen-things-ive-learned-from-charlie-munger-about-capital-allocation/ [medium]

12. Wall Street Prep. "Capital Allocation | Strategic Framework +
    Ratio Calculator."
    https://www.wallstreetprep.com/knowledge/capital-allocation/ [medium]

13. Basis Report. "Capital Allocation: Evaluate Any Company."
    https://www.basisreport.com/resources/capital-allocation [medium]

14. Wikipedia. "Real options valuation."
    https://en.wikipedia.org/wiki/Real_options_valuation [medium]

15. RSIS International (2025). "A Study on Real Options Valuation Vs.
    Traditional NPV in Capital Budgeting Decisions: A Comparative
    Study."
    https://rsisinternational.org/journals/ijrsi/articles/a-study-on-real-options-valuation-vs-traditional-npv-in-capital-budgeting-decisions-a-comparative-study [medium]

16. SchildbergHornschach, Christine et al. (2019). "Debiasing
    escalation of commitment: the effectiveness of decision aids to
    enhance de-escalation." Journal of Economic Psychology.
    https://doi.org/10.1007/s00187-019-00290-z [high]

## See Also

- `library/finance/cost-of-capital-and-wacc.md` -- the cost of capital
  that serves as the hurdle rate for capital budgeting decisions.
- `library/value-investing/capital-allocation.md` -- the investor's
  perspective on evaluating management's capital allocation skill,
  complementing this management-side treatment.
- `library/business-management-strategy/corporate-governance-board-effectiveness.md`
  -- board oversight of capital allocation as a core governance
  responsibility.
- `library/business-management-strategy/executive-compensation-incentive-design.md`
  -- how compensation structures align or misalign management
  incentives with value-creating capital allocation.
- `library/business-management-strategy/unit-economics-business-model-design.md`
  -- the unit-level economics that determine whether reinvestment
  creates or destroys value.