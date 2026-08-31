---
name: mutual-funds-etfs-retail-capital-pooling
id: 20260831T181609Z
tier: library-topic
domain: investment-vehicles-fund-structures
author: Library Runner
tags: [mutual-funds, etfs, passive-investing, index-funds, expense-ratios, creation-redemption, nav-pricing, tax-efficiency, fund-structures]
links: [library/investment-vehicles-fund-structures/insurance-float-as-investment-capital.md, library/investment-vehicles-fund-structures/pe-vc-fund-structures-lp-gp-carried-interest-j-curve.md, library/finance/anchor-finance.md]
---

# Mutual Funds and ETFs -- How the Architecture of Pooled Vehicles Shapes Retail Capital Allocation and Market Structure

Mutual funds and exchange-traded funds (ETFs) are the dominant legal and economic structures through which retail and institutional investors pool capital for collective investment in diversified portfolios. The structural differences between open-end mutual funds, closed-end funds, and ETFs -- in pricing mechanics, liquidity provision, tax treatment, fee architecture, and governance -- are not incidental: they determine who bears transaction costs, how capital flows respond to market conditions, and how the rise of passive investing reshapes corporate governance and price discovery across the entire financial system.

## Background

The pooled investment vehicle is an old idea. The first recognized investment
trust, the Foreign and Colonial Government Trust, was established in London in
1868, offering small investors a diversified portfolio of government bonds that
would have been impractical to assemble individually. The concept crossed the
Atlantic in the 1890s with the Boston Personal Property Trust, but the modern
mutual fund industry traces its origin to the Massachusetts Investors Trust,
founded in 1924. This was the first open-end fund: it continuously issued new
shares and stood ready to redeem existing ones at net asset value, a structural
innovation that distinguished it from the fixed-capital investment trusts that
preceded it.

The open-end structure was revolutionary because it solved a fundamental
problem of collective investment: liquidity without liquidation. In a
closed-end trust, investors who wanted to exit had to find a buyer on a
secondary market, often at a discount to the underlying portfolio value. The
open-end fund promised redemption at the portfolio's actual worth, eliminating
the discount risk that plagued closed-end vehicles. This promise, however,
created a new structural tension: the fund had to maintain cash reserves or
sell securities to meet redemption requests, potentially imposing transaction
costs and tax consequences on remaining shareholders.

The regulatory architecture for these vehicles was established by the
Investment Company Act of 1940, passed in the aftermath of the 1929 crash and
the investment trust collapses of the Great Depression. The Act defined four
categories of investment companies: face-amount certificate companies, unit
investment trusts (UITs), open-end management companies (mutual funds), and
closed-end management companies. The Act imposed fiduciary duties, disclosure
requirements, governance standards, and restrictions on affiliated
transactions. It created the framework under which all subsequent fund
innovation occurred, including the development of the ETF.

The first ETF, the SPDR S&P 500 ETF (SPY), launched on the American Stock
Exchange on January 22, 1993. State Street Global Advisors created it as a
hybrid: legally an open-end fund under the 1940 Act, but with a secondary
market trading mechanism borrowed from closed-end funds. The critical
innovation was the creation-redemption process, which allowed large
institutional participants to exchange baskets of underlying securities for
ETF shares and vice versa, keeping the ETF's market price anchored to its net
asset value through arbitrage. This mechanism distinguished the ETF from both
traditional open-end funds (which transact only at end-of-day NAV) and
closed-end funds (which can trade at persistent premiums or discounts).

The ETF grew slowly at first. By 2000, there were approximately 80 ETFs
globally with $75 billion in assets. The acceleration came in the 2000s as
investors increasingly sought low-cost, tax-efficient, intraday-tradable
alternatives to mutual funds. The financial crisis of 2008-2009 further
boosted ETF adoption: the transparency of ETF holdings and the arbitrage
mechanism that kept prices near NAV contrasted with the opacity and
illiquidity of some structured products that failed during the crisis. By the
end of 2025, U.S. ETF assets reached approximately $13.5 trillion, according
to ETFGI industry data, and by May 2026, that figure surpassed $15.69
trillion across 5,283 products from 488 providers.

The parallel story was the rise of passive investing. The first index mutual
fund, Vanguard 500 Index Fund, was launched by John Bogle in 1976. Bogle's
thesis was simple: actively managed funds, after fees, underperform market
benchmarks because the aggregate of all active investors must return the
market average minus costs. Therefore, a fund that simply held the market
portfolio at minimal cost would outperform the majority of active managers
after fees. The empirical evidence eventually vindicated this thesis. SPIVA
(S&P Indices Versus Active) scorecards consistently show that over 10-year
periods, approximately 78% of actively managed large-cap funds
underperform their passive benchmarks. The combination of ETF structure and
index-tracking strategy created the dominant investment vehicle of the 21st
century: low-cost, tax-efficient, intraday-tradable, diversified exposure to
virtually any asset class or market segment.

The industry that emerged is highly concentrated. By the end of 2024,
Vanguard held approximately 28% of U.S. fund industry assets under
management, with BlackRock at 11%, Fidelity at 10%, and Capital Group at 8%.
Together, the top four firms managed roughly 57% of industry assets. Among
ETF providers specifically, iShares (BlackRock) and Vanguard were effectively
tied for leadership by mid-2026, holding 28.9% and 28.6% market share
respectively, while State Street SPDR held 13.2%. The "Big Three" index fund
managers -- BlackRock, Vanguard, and State Street -- together control over a
quarter of shareholder votes on S&P 500 companies, raising governance
questions that are reshaping the debate over corporate control and market
efficiency.

## Core Concepts

### Open-End Mutual Funds -- The Continuous-Issuance Model

An open-end mutual fund is an investment company that continuously issues
and redeems shares directly with investors at the fund's net asset value
(NAV). The fund has no fixed number of shares outstanding; it creates new
shares when investors buy and destroys shares when investors redeem. NAV is
calculated as (Total Assets - Total Liabilities) / Total Shares Outstanding,
and for open-end funds this calculation occurs once per day after the market
closes at 4:00 PM Eastern Time. This is called forward pricing: an order
placed during the trading day receives the NAV calculated at the end of that
business day, meaning the investor does not know the exact execution price at
the time the order is placed.

The continuous-issuance model has a critical structural consequence: the
fund must maintain liquidity to meet redemptions. When investors withdraw
capital, the fund manager must either hold sufficient cash or sell
underlying securities to raise the redemption proceeds. If the fund sells
appreciated securities, it realizes capital gains that are then distributed
to all remaining shareholders as taxable distributions -- even shareholders
who did not redeem. This is the structural weakness of the mutual fund
model: the actions of one group of investors (those redeeming) can impose
costs on everyone else in the fund. The Investment Company Act of 1940
requires regulated investment companies to distribute at least 90% of their
net investment income and realized capital gains annually to maintain
pass-through tax status under IRC Subchapter M, which means these
realizations cannot be deferred inside the fund.

Open-end funds cannot trade at a premium or discount to NAV because
investors always transact directly with the fund at NAV (plus or minus any
sales charge). This eliminates the discount risk of closed-end funds but
introduces the liquidity-management burden described above. The fund's
portfolio manager must balance the investment objective against the need to
hold cash reserves or maintain the ability to sell securities quickly
without excessive market impact, particularly during periods of market
stress when redemptions tend to cluster.

### Closed-End Funds -- Fixed Capital, Market Pricing

Closed-end funds issue a fixed number of shares through an initial public
offering (IPO), after which the fund does not create or redeem shares
directly with investors. The shares trade on a secondary market (a stock
exchange) throughout the day at prices determined by supply and demand.
Because the market price is set by investor sentiment rather than the
fund's direct redemption mechanism, closed-end funds can trade at a
premium (above NAV) or a discount (below NAV) to their underlying portfolio
value.

The premium/discount dynamic is the defining structural feature of
closed-end funds. Premiums can arise when investor demand for a particular
strategy or asset class exceeds the supply of closed-end fund shares.
Discounts are more common and more persistent, particularly for funds
investing in less liquid or less popular asset classes. The discount
reflects a combination of factors: management fees (which reduce the value
of holding the fund versus its underlying assets), liquidity concerns,
tax overhang (unrealized capital gains that would be distributed if the
fund were liquidated), and investor sentiment. Some closed-end funds employ
leverage (borrowing against the portfolio to enhance returns), which
amplifies both gains and the premium/discount volatility.

Closed-end funds solve the liquidity-management problem that plagues
open-end funds: because the fund never needs to redeem shares, it can hold
illiquid or less-liquid assets without facing forced selling. This makes
closed-end structures suitable for specialized strategies in emerging
markets, municipal bonds, or alternative assets where daily liquidity at
NAV would be impractical. The trade-off is that the investor bears the
premium/discount risk: an investor who buys at a premium and sells at a
discount loses money even if the underlying portfolio appreciates.

### ETFs -- The Hybrid Structure

ETFs are legally classified as open-end investment companies under the
Investment Company Act of 1940, placing them in the same regulatory
category as traditional mutual funds. This classification matters because
it determines how they are regulated and how they create and destroy
shares. The critical distinction from traditional open-end funds is that
ETFs trade on stock exchanges throughout the day at market prices, while
only authorized participants (APs) -- large financial institutions
contracted with the ETF issuer -- can create or redeem shares directly
with the fund, and only in large blocks called creation units (typically
50,000 shares or more).

The creation-redemption mechanism is the structural innovation that
distinguishes ETFs from both open-end mutual funds and closed-end funds.
When an ETF's market price drifts above its NAV (a premium), an authorized
participant assembles a basket of the underlying securities that
comprises the ETF's tracked index and delivers it to the ETF issuer in
exchange for a creation unit of new ETF shares. The AP then sells these
newly created shares into the secondary market, increasing supply and
pushing the price back toward NAV. When the ETF trades at a discount, the
process reverses: the AP buys ETF shares in the secondary market,
aggregates them into a creation unit, and delivers them to the issuer for
redemption, receiving a basket of the underlying securities in return.
This reduces the supply of ETF shares, pushing the price back up toward
NAV.

The arbitrage incentive is what keeps ETF prices close to NAV. APs are
profit-driven institutions -- typically major broker-dealers such as
Goldman Sachs, JPMorgan, or Barclays -- that profit from the discrepancy
between the ETF's market price and the aggregate value of its underlying
holdings. This arbitrage typically completes within minutes, which is why
most broad-market ETFs trade within a few basis points of NAV during
normal market conditions. Without APs, an ETF would function like a
closed-end fund, susceptible to premiums and discounts driven by investor
sentiment rather than fundamental value.

The in-kind nature of the creation-redemption process is the key to ETF
tax efficiency. When an AP redeems ETF shares, the fund delivers the
underlying securities directly rather than selling them for cash. Under
IRC Section 852(b)(6), a regulated investment company does not recognize
gain or loss when it distributes portfolio securities in-kind to satisfy
a redemption. This means the fund can remove appreciated securities from
its portfolio without triggering a taxable event for remaining
shareholders. In contrast, a traditional mutual fund that sells
appreciated securities to meet cash redemptions realizes capital gains
that must be distributed to all remaining shareholders. Approximately 52%
of equity mutual funds distributed capital gains in 2025, compared to
approximately 6% of equity ETFs, according to industry data.

### Expense Ratios and Fee Architecture

The expense ratio is the annual cost of owning a fund, expressed as a
percentage of assets under management. It includes the management fee
(paid to the investment adviser), administrative costs, and 12b-1 fees
(marketing and distribution charges named after the SEC rule that
permits them, capped at 1% total under the Investment Company Act).
The expense ratio is deducted from fund assets daily, reducing the
investor's return continuously. It is not a bill the investor pays
separately; it is embedded in the fund's net asset value.

The fee gap between active and passive management is substantial and
compounds dramatically over time. Asset-weighted expense ratios for
actively managed equity mutual funds averaged approximately 0.40% in
2024, while index funds typically charged 0.03% to 0.14%. The simple
average (not asset-weighted) for actively managed funds was approximately
1.10%. For ETFs, index-based versions averaged 0.48% and active versions
averaged 0.74% in 2025. A 0.75% annual fee difference on a $100,000
portfolio compounding at 8% over 30 years costs approximately $200,000
in lost growth -- a sum larger than the initial investment itself.

Sales loads are separate from expense ratios. Front-end loads (Class A
shares) typically range from 3% to 5.75%, deducted from the initial
investment before it goes to work. A $10,000 investment with a 5%
front-end load puts only $9,500 to work. Back-end loads (Class B or C
shares), also called contingent deferred sales charges (CDSC), start
around 5% and decline annually, typically reaching zero after 5 to 7
years. FINRA caps total loads at 8.5%. By 2025, approximately 92% of new
mutual fund sales went into no-load share classes, reflecting the
industry's shift away from commission-based distribution toward
fee-based advisory models.

The full cost of fund ownership extends beyond the stated expense ratio.
Trading costs (turnover drag), market impact, cash drag (the cost of
holding uninvested cash), and tax drag (capital gains distributions in
taxable accounts) are often invisible in the headline fee but materially
affect returns. For a typical active fund, the all-in cost including
turnover drag and cash drag can be 1.0% to 1.5%, significantly above the
stated expense ratio. Passive index funds have minimal turnover and low
cash drag, making their all-in cost very close to the stated expense
ratio.

### Tracking Error and Premium/Discount Dynamics

Tracking error measures how closely an index fund or ETF replicates the
performance of its underlying benchmark. It is the standard deviation of
the difference between the fund's returns and the benchmark's returns
over a specified period. For broad-market, large-cap index ETFs, tracking
error is typically a few basis points per year. For funds tracking less
liquid indices, international markets, or niche strategies, tracking error
can be materially larger.

Several factors drive tracking error. Expense ratios create a structural
drag: a fund charging 0.10% will underperform its benchmark by
approximately 0.10% per year before other factors. Trading costs from
portfolio rebalancing, index reconstitution, and cash management add
incremental drag. Cash drag arises when the fund holds cash that does
not participate in the index's returns. For ETFs, the creation-redemption
process itself can introduce tracking error: when an AP delivers a
creation basket, the fund must integrate those securities into its
portfolio, and timing differences between the creation and the NAV
calculation can create small discrepancies.

Premium and discount dynamics are primarily relevant to closed-end funds
and, to a lesser extent, ETFs in stressed market conditions. For most
broad-market ETFs, the arbitrage mechanism keeps premiums and discounts
within a few basis points of NAV during normal trading. However, during
market stress -- the flash crash of May 2010, the market disruption of
March 2020 -- ETF premiums and discounts can widen significantly,
particularly for ETFs holding less liquid underlying assets. Bond ETFs,
international ETFs, and ETFs holding emerging-market securities are more
prone to premium/discount volatility because their underlying securities
trade less frequently and the arbitrage mechanism is slower to correct
mispricing. Cash creation and redemption (as opposed to in-kind) is more
common in these segments, which can increase both tracking error and tax
burden.

### Active vs. Passive Management

The active-versus-passive debate is not merely a question of investment
philosophy; it is a question of vehicle economics. Active management
attempts to outperform a benchmark through security selection and market
timing. Passive management attempts to replicate a benchmark at minimal
cost. The structural economic argument for passive investing, first
articulated by Bogle and later formalized by academic research, is that
the aggregate of all active investors must earn the market return minus
their costs, while passive investors earn the market return minus minimal
costs. Therefore, the average active investor must underperform the
average passive investor by the fee differential.

The empirical evidence is strongly consistent with this prediction.
SPIVA scorecards show that over 10-year periods, approximately 78% of
actively managed large-cap U.S. equity funds underperform the S&P 500.
The underperformance rate is even higher over longer periods and for
certain asset classes. Critically, top-quartile performers in one
5-year period have no better than random chance of repeating in the next
5-year period, undermining the argument that skill rather than luck
explains past outperformance.

The rise of passive investing has structural implications beyond
individual investor returns. As index funds and ETFs grew to hold over
50% of U.S. equity fund assets by the mid-2020s, the composition of
shareholders in public corporations changed fundamentally. The "Big
Three" index fund managers -- BlackRock, Vanguard, and State Street --
became the largest shareholders in most large U.S. corporations. This
concentration raises questions about corporate governance, common
ownership, and the incentives of passive fund managers to monitor
portfolio companies, questions that academic research is actively
debating and that have direct policy implications.

### The Regulatory Framework

The Investment Company Act of 1940 is the foundational statute governing
all U.S. registered investment companies, including mutual funds, ETFs,
and closed-end funds. The Act requires registration with the SEC,
imposes fiduciary duties on fund boards, mandates disclosure through
prospectuses and periodic reports, restricts affiliated transactions, and
sets capital structure requirements. The Act's key provisions include
Section 8 (registration), Section 22(d) (daily NAV pricing for open-end
funds), Section 22(e) (seven-day redemption mandate), and Section 30
(periodic SEC reporting).

The ETF-specific regulatory framework was formalized by SEC Rule 6c-11,
adopted in September 2019 and effective December 2019. Before Rule
6c-11, ETFs required individual exemptive orders from the SEC to operate,
a costly and time-consuming process. Rule 6c-11 created a standardized
framework permitting ETFs to operate without individual exemptive orders,
explicitly authorizing in-kind creation and redemption baskets. The rule
also permits "custom baskets" -- redemption baskets composed of a
non-representative selection of the fund's holdings -- as long as the
fund adopts written policies governing basket construction. This
flexibility is particularly valuable for actively managed ETFs, whose
portfolios change more frequently than index-tracking ETFs.

The tax framework is governed by IRC Subchapter M (Sections 851-855),
which provides pass-through tax treatment for funds qualifying as
regulated investment companies (RICs). To maintain RIC status, a fund
must distribute at least 90% of its net investment income annually.
Section 852(b)(6) provides that a RIC does not recognize gain or loss
when it distributes portfolio securities in-kind to satisfy a redemption
-- the statutory basis for ETF tax efficiency. This provision does not
apply to cash redemptions, where the fund sells securities and
distributes the cash proceeds, potentially realizing capital gains.

### Fund Lifecycle and Succession

Mutual funds and ETFs have a lifecycle that begins with product
development and regulatory approval, proceeds through asset gathering and
portfolio management, and may end with liquidation or merger. Fund
liquidation occurs when a fund's assets fall below a viable operating
threshold, or when the adviser decides the product is no longer
strategically viable. Liquidation involves selling the portfolio,
distributing proceeds to shareholders (triggering taxable events in
taxable accounts), and closing the fund. Fund mergers combine two funds
into one, typically to consolidate overlapping strategies or eliminate
unviable products while preserving the tax deferral of the absorbed
fund's shareholders.

Succession in fund management is a structural concern that is often
underappreciated. The investment adviser -- the entity that manages the
fund's portfolio -- may change due to acquisition, strategic
restructuring, or the departure of key personnel. For actively managed
funds, the departure of a star portfolio manager can trigger significant
redemptions and performance disruption. For passive funds, adviser
changes are less disruptive because the investment process is
mechanical, but fee renegotiations and operational transitions still
require oversight by the fund's board of directors. The 1940 Act
requires that fund boards, including a majority of independent directors,
approve any change in investment adviser, providing a governance
checkpoint on succession transitions.

## Evidence

### The SPIVA Scorecards -- Active Underperformance Is Persistent and Structural

The S&P Indices Versus Active (SPIVA) scorecards, published annually by
S&P Dow Jones Indices, compare the performance of actively managed funds
against their benchmarks across multiple asset classes and time horizons.
The methodology is designed to be survivorship-bias-free: it includes
funds that were liquidated or merged during the measurement period,
avoiding the common error of counting only surviving funds. The results
are remarkably consistent across years and asset classes.

For U.S. large-cap equity funds, the SPIVA data shows that approximately
78% of actively managed funds underperform the S&P 500 over 10-year
periods. The underperformance rate is higher over longer horizons:
over 15-year periods, the figure typically exceeds 85%. The
underperformance is not concentrated in a few poorly managed funds; it
is a broad, systematic pattern. Even among funds that outperform in one
period, the probability of repeating that outperformance in the next
period is no better than chance. This evidence is consistent with the
Grossman-Stiglitz theoretical framework: active management generates
returns only to the extent that it produces information that is not
already reflected in prices, and the aggregate of active managers
cannot outperform the market they collectively comprise, net of costs.

The implication for vehicle structure is direct: the expense ratio
differential between active and passive funds is not compensated by
superior returns for the average investor. A 0.75% annual fee
differential, compounded over a 30-year investment horizon on a
$100,000 portfolio, consumes approximately $200,000 in lost growth --
a figure that exceeds the initial investment. The structural
conclusion is that for the median investor in the median fund, passive
vehicles dominate active vehicles on an after-fee, after-tax basis.

### The NBER Study -- Index Funds and Corporate Governance

Bebchuk and Hirst (2019), in a National Bureau of Economic Research
working paper titled "Index Funds and the Future of Corporate
Governance," analyzed the governance implications of the rise of index
funds. Their central finding was that the index fund sector is heavily
concentrated and dominated by the "Big Three" -- BlackRock, Vanguard,
and State Street. The concentration is structural: economies of scale in
operating index funds, branding advantages, and liquidity benefits for
large ETFs create barriers to entry that the authors predict will
persist. The dominant incumbents have significant structural advantages
that derive from the economics of scale; new entrants have no significant
opportunities to attract business from incumbents by introducing products
the incumbents cannot imitate.

The governance concern arises from incentive misalignment. Index fund
managers capture a tiny fraction of the governance gains they produce --
their fees are a few basis points of assets under management, while the
value of improved governance at a portfolio company accrues to all
shareholders, including competitors' funds tracking the same index. This
creates a free-rider problem: each index fund manager bears the full cost
of monitoring but shares the benefit with all funds tracking the same
index. The authors' empirical study found that index fund managers
underinvest in stewardship and defer to corporate managers, consistent
with the incentive structure. The top three index fund families had on
average only 21 investment stewardship personnel to cover 17,849 firms in
their combined portfolios.

The policy implications are significant. The rise of index funds has
increased common ownership -- the same large asset managers hold
positions in all companies within a given sector. Some scholars argue
this produces anticompetitive effects; others contest the empirical
basis. The NBER authors argue that the alarmism over common ownership may
be counterproductive, potentially pushing index fund managers to act even
more deferentially to corporate management. They also argue that the
rise of index funds cannot substitute for hedge fund activism in the
corporate governance system, because hedge fund managers -- with
"2-and-20" compensation structures -- capture a meaningful proportion of
governance gains, giving them incentives to engage that index fund
managers lack.

### The ECGI Study -- Do Index Funds Monitor?

Heath, Macchiavelli, Michaely, and Ringgenberg (2022), in a working
paper published by the European Corporate Governance Institute, provided
the most direct empirical evidence on the monitoring behavior of index
funds. Their central finding: relative to active funds, index funds are
less effective monitors. Index funds are less likely to vote against firm
management on contentious governance issues, there is no evidence they
engage effectively publicly or privately, and they promote less board
independence and worse pay-performance sensitivity at their portfolio
companies.

The study used fund-firm-agenda-item-level voting data and included
firm-by-year fixed effects that controlled for time-varying heterogeneity
at the firm level, providing cleanly identified evidence. The results
were uniform across governance dimensions: index funds were 11 percentage
points more likely to side with firm management on contentious board
items, with the largest difference on compensation votes (11.3 percentage
points). Low-fee index funds were even more likely to vote with
management, indicating that the low-cost structure of index funds
directly affects their capacity to monitor.

The aggregate conclusion of the study was that the rise of index
investing shifts power from investors to corporate managers. This finding
is consistent with the theoretical predictions of Bebchuk, Cohen, and
Hirst (2017) and Edmans, Levit, and Reilly (2018), who model the
incentive structure of passive fund managers. The evidence directly
contradicts the view that the large positions held by index funds
necessarily motivate effective monitoring, as classic agency theory
(Grossman and Hart, 1980) would predict.

### The Appel, Gormley, and Keim Study -- Passive Investors as Active Owners

Appel, Gormley, and Keim (2016), in a study published by NYU Stern,
provided evidence on the opposite side of the governance debate. Using
variation in passive institutional ownership resulting from stocks being
assigned to either the Russell 1000 or Russell 2000 index as an
instrumental variable, they found that an increase in ownership by
passive institutions is associated with more independent directors, the
removal of poison pills, fewer restrictions on shareholders' ability to
call special meetings, and fewer dual-class share structures. Passive
investors appeared to exert influence through their large voting blocs:
passive ownership was associated with less support for management
proposals and more support for shareholder-initiated governance proposals.

This study illustrates the unresolved tension in the literature. Some
studies find that passive ownership reduces managerial power (Appel,
Gormley, and Keim, 2016, 2019); others find the opposite (Schmidt and
Fahlenbrach, 2017; Heath et al., 2022). The conflicting findings may
reflect differences in methodology, sample period, or the specific
governance outcomes examined. Corum, Malenko, and Malenko (2022)
provided a theoretical framework suggesting that the effect of passive
fund growth is non-monotonic: initial growth improves governance (as
passive funds replace unengaged retail investors), but further growth
harms it (as passive funds replace engaged active funds and fees decline,
reducing the benefits of engagement). This non-monotonic prediction may
help reconcile the conflicting empirical findings.

### The Coles, Heath, and Ringgenberg Study -- Index Investing and Price Efficiency

Coles, Heath, and Ringgenberg (2017) examined whether the rise of index
investing affects the informational efficiency of stock prices, using
predictions derived from a Grossman-Stiglitz framework. Their central
finding: an exogenous increase in index investing leads to lower
information production (as measured by Google searches, EDGAR views, and
analyst reports), yet price informativeness remains unchanged. This is
consistent with an equilibrium in which investors choose to gather
private information whenever it is profitable. As index investing
increases, there are fewer privately-informed active investors (so
overall information production drops), but the remaining mix of investors
adjusts until the returns to active investing are unchanged.

The practical implication is that the rise of passive investing does not
appear to undermine price efficiency, at least within the range of
passive ownership observed through 2016. Over the sample period from
2007 to 2016, index fund ownership quintupled from 2% to 11% of market
capitalization on average, yet the average variance ratio (a measure of
price efficiency) fell slightly from 1.16 to 1.10, reflecting a slight
improvement in price efficiency. The authors caution that their results
rely on assumptions and that the model's predictions hold for any feasible
level of passive investing, but they note that the trend has not changed
direction even as passive ownership has continued to grow beyond their
sample period.

### Industry Concentration Data -- The Big Three and Market Structure

The concentration of the asset management industry is documented by
Morningstar's fund family data and by ETFGI's industry reports. As of
the end of 2024, Vanguard led all fund families with an estimated 28%
of U.S. fund industry assets under management, with $8.7 trillion in
AUM. BlackRock held 11%, Fidelity 10%, and Capital Group 8%. The top
four firms managed roughly 57% of industry assets, and the top five
managed 63%. Among ETF providers, iShares (BlackRock) and Vanguard were
effectively tied for leadership by mid-2026, holding 28.9% and 28.6%
market share respectively, while State Street SPDR held 13.2%. Together,
the Big Three ETF providers held over 70% of ETF assets.

The Thinking Ahead Institute's 2025 survey of the world's 500 largest
asset managers found total AUM of $139.9 trillion at the end of 2024, up
9.4% from 2023. Passive strategies accounted for 39.0% of total
investments, a 6.1% increase in share from the prior year, while active
assets represented 61.0%. The top 20 managers' share of total AUM grew
from 45.5% in 2023 to 47.0% in 2024. The trend toward concentration and
passive investing is unambiguous and accelerating.

## Implications

### For Individual Investors -- Vehicle Selection as the Primary Cost Lever

For the individual investor, the choice of investment vehicle is the
single most consequential cost decision in a long-term portfolio. The
expense ratio differential between active and passive funds -- typically
0.50% to 1.00% per year -- is not a one-time cost but a perpetual drag
that compounds against the portfolio. Over a 30-year horizon, a 0.75%
annual fee differential on a $100,000 initial investment compounding at
8% consumes approximately $200,000 in foregone growth. This is a
structural cost: it is paid every year, regardless of market conditions,
and it is deducted before the investor sees any return.

The practical implication is that for the core of a diversified portfolio
-- broad equity market exposure, international equity, investment-grade
bonds -- passive vehicles (index mutual funds or ETFs) are structurally
superior for the median investor. The SPIVA evidence shows that the
probability of selecting an active fund that outperforms its benchmark
over 10-15 years is approximately 15-20%, and the probability of
selecting one that outperforms in two consecutive periods is no better
than chance. For specialized strategies, niche asset classes, or markets
where information is less efficiently priced, active management may
add value, but the investor should demand clear evidence of persistent
skill, not merely a track record that could be explained by luck.

The ETF-versus-mutual-fund choice for passive exposure involves trade-offs
that depend on the investor's circumstances. ETFs offer intraday
trading, tax efficiency in taxable accounts (through the in-kind
redemption mechanism), and generally lower expense ratios. Mutual funds
offer automatic investment plans, fractional share purchases, and no
bid-ask spread cost. The 2023 expiration of Vanguard's patent on the
dual-share-class structure (which allowed ETF and mutual fund shares
to share a single portfolio, extending ETF tax efficiency to the mutual
fund share class) has prompted the SEC to approve additional firms to
offer ETF share classes of existing mutual funds, potentially narrowing
the tax-efficiency gap between the structures.

### For Corporate Governance -- The Concentration Problem

The rise of passive investing has created a governance concentration that
is unprecedented in the history of public equity markets. The Big Three
index fund managers -- BlackRock, Vanguard, and State Street -- are now
the largest shareholders in most large U.S. corporations, collectively
controlling over a quarter of S&P 500 shareholder votes. This
concentration has two structural consequences that the academic literature
is actively debating.

First, the incentive structure of passive fund managers may lead to
underinvestment in stewardship. Index fund managers capture only a tiny
fraction of the governance gains they produce (their fees are a few basis
points of AUM), while the costs of monitoring are borne entirely by the
fund. This creates a free-rider problem: each index fund manager rationally
underinvests in monitoring, because the benefit of monitoring is shared
with all funds tracking the same index. The ECGI study by Heath et al.
(2022) found empirical evidence consistent with this prediction: index
funds are significantly more likely to vote with management on
contentious governance issues, and low-fee index funds are even more
likely to do so.

Second, the common ownership created by index funds -- the same managers
holding positions in all companies within a sector -- raises potential
anticompetitive concerns. Some scholars argue that common ownership
reduces competitive incentives because the same shareholders benefit from
all firms in an industry, reducing the benefit of competition between
them. Others contest the empirical basis for this concern. The NBER
study by Bebchuk and Hirst (2019) argues that alarmism over common
ownership may be counterproductive, pushing index fund managers toward
greater deference to management and distracting antitrust regulators from
the decisions of corporate managers that drive market concentration.

The policy implications are substantial. The INDEX Act, proposed by a
group of U.S. senators, would require passive funds to vote proxies in
accordance with the instructions of fund investors rather than at the
discretion of the fund manager. This would address the incentive
misalignment by shifting voting power back to beneficial owners, but it
would also impose operational complexity on fund investors who would need
to vote on thousands of ballot items across thousands of portfolio
companies.

### For Market Structure -- Price Discovery and the Active-Passive Equilibrium

The question of whether the rise of passive investing undermines price
discovery is one of the most consequential structural questions for
financial markets. The concern is intuitive: if a growing share of
investors simply buys the market portfolio without analyzing individual
securities, who is left to incorporate information into prices? The
Grossman-Stiglitz framework predicts that the market reaches an
equilibrium where the marginal active investor is indifferent between
gathering information and not gathering it. As passive investing grows,
fewer investors gather information, but the returns to information
gathering increase (because there is less competition), drawing in
marginal investors until the equilibrium is restored.

The empirical evidence from Coles, Heath, and Ringgenberg (2017) is
consistent with this prediction: information production declines as
passive ownership rises, but price informativeness remains unchanged.
However, this evidence covers a period when passive ownership rose from
2% to 11% of market capitalization. The question of whether the
equilibrium holds at much higher levels of passive ownership -- 30%,
40%, 50% of market capitalization -- remains open. If the equilibrium
breaks down at extreme levels, the consequences could include reduced
price efficiency, greater mispricing of individual securities, and
reduced allocative efficiency of capital markets.

The practical implication for market participants is that the active-
passive boundary is not static. As passive ownership grows, the
opportunities for active management may increase (because there is less
competition for information), but the cost of active management must
decline to remain competitive with passive alternatives. The industry
data confirms this: passive products accounted for 42% of industry AUM
by the end of September 2024, and the trend is unambiguous. Asset
managers with heavy exposure to active equity funds have posted negative
organic AUM growth, while passive-only managers like BlackRock have
outpaced the industry. The structural conclusion is that the vehicle
economics of passive investing -- low cost, tax efficiency, scale
economies -- create a self-reinforcing cycle that continues to take
share from active management.

### For Vehicle Architecture -- The Structural Lessons

The evolution from closed-end funds to open-end mutual funds to ETFs
reveals a structural pattern: each innovation solved a limitation of its
predecessor while introducing a new trade-off. Closed-end funds solved
the liquidity-management problem (no redemptions, so the portfolio can
hold illiquid assets) but introduced premium/discount risk. Open-end
mutual funds solved the premium/discount problem (always transact at NAV)
but introduced the liquidity-management burden (must sell securities to
meet redemptions, imposing costs on remaining shareholders). ETFs solved
both problems through the creation-redemption mechanism: the arbitrage
process keeps prices near NAV (solving premium/discount risk), while the
in-kind transfer avoids forced selling (solving the liquidity-management
burden and providing tax efficiency).

The lesson for vehicle architecture is that structural design determines
incentives and costs. The in-kind creation-redemption mechanism is not a
minor operational detail; it is the structural feature that makes ETFs
tax-efficient, keeps prices near NAV, and eliminates the cross-subsidy
problem where redeeming investors impose costs on remaining shareholders.
Similarly, the expense ratio is not merely a cost; it is the structural
lever that determines whether a fund can attract assets at scale, whether
the manager has resources to invest in stewardship, and whether the
vehicle's economics compound for or against the investor over time.

The comparative analysis across fund structures connects directly to the
other vehicle types in this domain. Insurance float (as analyzed in the
brain's topic on the subject) provides a form of permanent, low-cost
capital that is structurally different from redeemable fund capital.
Private equity and venture capital partnerships (as analyzed in the
brain's topic on LP-GP structures) use closed-end fund structures with
contractual lockups that eliminate redemption risk entirely, at the cost
of investor liquidity. Berkshire Hathaway's permanent-capital holding
company structure represents yet another architecture: no redemption
rights, no fee drag, capital allocated across businesses and securities
by a single decision-maker. Each structure solves the same fundamental
problem -- pooling capital for collective investment -- with different
trade-offs among liquidity, cost, governance, and control.

## Sources

1. Bebchuk, L. & Hirst, S. (2019). "Index Funds and the Future of
   Corporate Governance: Theory, Evidence, and Policy." NBER Working
   Paper No. 26543. National Bureau of Economic Research.
   https://www.nber.org/system/files/working_papers/w26543/w26543.pdf [high]

2. Heath, D., Macchiavelli, M., Michaely, R., & Ringgenberg, K. (2022).
   "Do Index Funds Monitor?" ECGI Working Paper.
   https://www.ecgi.global/sites/default/files/working_papers/documents/heathmacchiocchimichaelyringgenbergfinal.pdf [high]

3. Appel, I., Gormley, T., & Keim, D. (2016). "Passive Investors, Not
   Passive Owners." NYU Stern Working Paper.
   https://www.stern.nyu.edu/sites/default/files/assets/documents/1%20Gormley%20Passive%20Investors%20Not%20Passive%20Owners.pdf [high]

4. Coles, J., Heath, D., & Ringgenberg, K. (2017). "On Index Investing."
   SSRN Working Paper.
   https://r.jordan.im/download/investing/coles2017.pdf [high]

5. Malenko, A., Malenko, N., & Corum, D. (2022). "Corporate Governance
   Implications of the Growth in Indexing." ECGI Working Paper.
   https://www.ecgi.global/sites/default/files/working_papers/documents/corporategovernanceimplicationsofthegrowthinindexing_1.pdf [high]

6. Investment Company Institute (2022). "2022 Investment Company Fact
   Book." Data on domestic index mutual funds and ETF assets.
   https://www.ici.org [high]

7. Morningstar (2025). "Low-Cost Provider Vanguard Gathers the Most Fee
   Revenue." Fund family AUM and management-fee share data.
   https://www.morningstar.com/funds/low-cost-provider-vanguard-gathers-most-fee-revenue [high]

8. ETFGI (2026). "ETFs Industry in the US Reaches US$15.7 Trillion
   Milestone." Industry assets and flows data.
   https://etfgi.com/news/press-releases/2026/06/etfgi-reports-etfs-industry-us-reaches-us157-trillion-milestone-driven [high]

9. SEC (2019). "Rule 6c-11: Exchange-Traded Funds." SEC Release
   IC-33646. Investment Company Act of 1940, 17 CFR 270.6c-11.
   https://www.sec.gov [high]

10. Thinking Ahead Institute (2025). "The World's 500 Largest Asset
    Managers." Pensions & Investment Research.
    https://www.thinkingaheadinstitute.org/content/uploads/2025/11/PI-500-2025_key-findings.pdf [high]

11. LegalClarity (2025). "Are ETFs More Tax Efficient Than Mutual Funds?"
    Analysis of IRC Section 852(b)(6) and ETF in-kind redemption tax
    treatment.
    https://legalclarity.org/are-etfs-more-tax-efficient-than-mutual-funds [medium]

12. etfvsindexfund.com (2025). "ETF vs Index Fund: SEC EDGAR Data, Rule
    6c-11 Mechanics." Statutory analysis of 1940 Act and IRC Subchapter M.
    https://etfvsindexfund.com [medium]

## See Also

- `library/investment-vehicles-fund-structures/insurance-float-as-investment-capital.md` -- a structurally different source of low-cost, permanent investment capital; insurance float provides capital that cannot be redeemed, in contrast to the redeemable capital of mutual funds.
- `library/investment-vehicles-fund-structures/pe-vc-fund-structures-lp-gp-carried-interest-j-curve.md` -- the closed-end partnership alternative to open-end mutual funds and ETFs, with contractual lockups that eliminate redemption risk at the cost of investor liquidity.
- `library/finance/anchor-finance.md` -- the broader finance domain covering financial institutions, securities, and market mechanics within which pooled investment vehicles operate.