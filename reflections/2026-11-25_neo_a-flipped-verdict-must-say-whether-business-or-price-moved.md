---
name: a-flipped-verdict-must-say-whether-business-or-price-moved
id: 20261125T122214Z
tier: reflection
trigger: session-end
author: Neo
tags: [valuation, value-investing, cron, mr-market]
links:
  - reflections/2026-11-25_neo_a-source-file-i-write-is-a-claim-not-a-source.md
  - reflections/2026-10-07_neo_a-sourced-sentence-fails-at-its-connectives-not-its-facts.md
  - reflections/2026-10-16_neo_a-seed-test-protects-only-the-commit-it-can-block.md
  - library/value-investing/mr-market.md
  - library/value-investing/margin-of-safety.md
  - investing-hub:companies/BABA.md
---

# A Flipped Verdict Must Say Whether the Business or the Price Moved

## I -- Idea

This run set out to review Alibaba's results for the quarter ended September 30, 2026, revalue the company and carry the new value into every file that depends on it, so that Suggi, who holds the Hong Kong shares, finds a checked view of the quarter rather than the valuation I published on 10 November. It was a scheduled one-time job, the replacement for the Alibaba results job that failed on 19 November on a provider rate limit before doing any work, and it ran with nobody present: preflight, a check that the results were really out, the review and revaluation, the dependent files, a learnings capture, this closure and a short report to Bot Chat.

The before picture matters for everything that follows. On 10 November I had valued Alibaba on normalized owner earnings, an earnings proxy because free cash flow is negative, at Bear, Base and Bull values of 46, 86 and 144 Hong Kong dollars a share against a price of 104.60. The file judged the shares overvalued relative to Base with low confidence, and it said the price needed e-commerce adjusted EBITA of about 169,000 million renminbi a year, roughly the level before the price war, while the Base case needed about 132,000. The job prompt asked me to say which of those two the quarter supported.

The work went in the order the company-research skill and the job prompt lay down. The results were on EDGAR as a 6-K filed on 19 November, so the run continued. I copied the old ledger script and its saved sources out of the Trash folder of the 10 November run and ran the gate against the live Hub file; it passed with 79 ledger entries and no mismatch, so the old Base was reproduced before any input changed. I then read the release, the call transcript, the 6-K on the planned T-Head listing, JD.com's third-quarter release as the nearest peer, a law-firm summary of the US export-control rule of 16 November and the Hong Kong price history, and I rebuilt the valuation in a new ledger that recomputes every derived figure from filing inputs.

The quarter itself was mixed in an instructive way. Alibaba E-commerce Group adjusted EBITA was 38,851 million against 11,336 a year earlier, because quick-commerce losses narrowed, and it was close to the 39,749 of the June quarter, so the June figure was not a one-off. Cloud revenue grew 53% and its adjusted EBITA margin reached 14.5%. AI Labs lost 10,503, less than in June. Against that, capital expenditure of 50,477 again exceeded operating cash flow of 15,690, and on the call management said next year's cloud growth target might be 30% to 45%, after saying the new export rules will affect next year's products and services, and it expects positive cash flow overall only in the second half of 2028.

The new values are 53, 99 and 153 Hong Kong dollars against a price of 82.20 on 24 November, so the verdict moved from overvalued relative to Base to undervalued relative to Base, still with low confidence and still without any claimed margin of safety. The quarter's 38,851 sits above the 33,000 a quarter the old Base needed and below the 42,250 a quarter the old price needed, and the new price needs only about 111,000 a year, below what the last four quarters produced. I published the Hub file, added a September-quarter section and the new valuation to the company note, pinned an older citation in the off-book note to the commit it depends on, rewrote the private portfolio line and reset the daily brief's value markers.

What I believed going in was that the verdict would turn on the quarter: if e-commerce profit held near June's level the Base would rise and the gap to the price would narrow. What I believe now is that the verdict turned more on the price than on the quarter, and that a report which says only "overvalued then, undervalued now" invites the reader to think the business changed sharply in fifteen days when mostly the market did.

## O -- Opinion

Confidence: low (55%) in the valuation and the verdict; high (85%) in the process lesson about reporting a changed verdict.

My position on Alibaba is that the new verdict is correct as arithmetic and weak as a judgment, and that it should be reported to Suggi with its decomposition attached. The Base value rose about 15%, from 85.90 to 98.93 Hong Kong dollars, and the exchange rate explains almost none of that. The price fell about 21%. Measured on the ratio of price to Base value, which went from about 1.22 to about 0.83, roughly 63% of the change came from the price and 37% from the value. A holder reading "the verdict flipped" deserves those two numbers before any conclusion, because they say where the news was.

The value side of the change deserves a harder look than its size suggests, and this is where my confidence stays low. Owner earnings rose from 92,625 to 108,764 mainly because two inputs are annualized from a single quarter: the Base e-commerce figure is midway between the trailing four quarters and four times the latest quarter, and the cloud figure is four times the latest quarter. Rolling the trailing window forward dropped the 11,336 of September 2025, the depth of the quick-commerce subsidies, and that one roll lifted the trailing sum by about 27,500. The equity adjustment rose as well, partly because AI Labs losses narrowed and partly because the investments outside the liquid portfolio rose by about 77,700 in the quarter, mainly from mark-to-market gains, which are themselves market prices, not business results. So even the value side of the change carries some market movement inside it.

The price side has a cause I can name but cannot value. Between 9 and 24 November the shares fell on a series of days that line up with the reports and then the publication of the US rule on remote access to advanced chips. The rule exempts commercial recommender systems, so it leaves the marketplaces alone and falls on cloud and model training. In my valuation the cloud counts only at four times its current quarterly profit, and growth beyond that sits in the off-book table as a hint, so the rule mostly affects a part of the value I had not counted. That is why I accept the new verdict as arithmetic. It is also why I do not trust it much: if the market is right that the rule cuts cloud profit itself, not just its growth, the counted part shrinks too, and one quarter of cloud margin at 14.5% is thin evidence against that.

The alternative view is that this decomposition is decoration, and that the only thing a value investor needs is the gap between price and value now. I reject that for a holder who reads the verdicts over time. A verdict that alternates between overvalued and undervalued within a fortnight, reported without its cause, trains the reader either to ignore the label or to trade on it, and neither is what the work is for. Graham's partner offers a different price each day; the job of the analyst is to say how much of the change in the gap came from the partner and how much from the business.

A second alternative is that the revaluation should not have moved the Base at all on one quarter, and that holding the old e-commerce input until the December quarter would be more disciplined. I see the appeal, because the December quarter will show whether the profit holds as consumers turn cautious, which management itself said they are doing. I reject it because the June and September quarters now agree with each other, and refusing to update on two consistent quarters is anchoring, not discipline. The answer is to update and to show how much of the update rests on annualizing.

On the process I am more satisfied. The reproduction from the Trash ledger made every later change attributable. The seeds blocked what they were built to block, seventeen in the Hub file and nineteen in the note, after two word-swap seeds in the note first passed and I added exact-phrase binds as the skill prescribes.

## R -- Reflection

### Surprise

I expected the price to be close to where I left it and the verdict to hinge on whether e-commerce profit held, but the price had fallen by almost a fifth before the results were even published, and the results then raised the value. My model of a results review was that the new information arrives in the filing. In this case most of the new information, as the market saw it, arrived in a US government rule a few days before the filing, and the filing mainly confirmed a profit level that the June quarter had already shown. I had framed the job around one question, which of two profit requirements the quarter supports, and the honest answer turned out to be that the quarter supports the old Base requirement comfortably and that the price requirement fell beneath both of them while I was not looking.

I also expected a third-party transcript and the issuer's release to agree on a headline ratio. They did not: the transcript printed the cloud margin as 14.9% in two places and 14.5% in others, while the release states 14.5% and its own segment figures give 14.5%. The skill warns that transcripts mislabel speakers and that their summaries can invent questions; it does not say that they misprint figures the release states plainly, and I had treated figures as the safe part of a transcript. Taking every figure from the release and only quoted words from the transcript turned out to be necessary rather than merely tidy.

### Feel

I am satisfied with the parts of the run that make the result checkable. The old Base was reproduced before anything changed, every derived figure in the new file is recomputed in a ledger, and the dependent files changed in the same run, so the portfolio line, the note, the Hub file and the brief markers agree. I am less satisfied with how quickly a confident-sounding label changed. I wrote "overvalued relative to Base" on 10 November with low confidence, and I am writing "undervalued relative to Base" on 25 November with low confidence, and if Suggi reads only the labels he would be right to ask what the labels are worth.

One small thing was uncomfortable because it repeats an old class. In the note I first wrote that management expected 30% to 45% cloud growth "because" the export rules would affect next year's products. The transcript says the rules will affect next year, says the supply chain is uncertain and says domestic compute is ahead of plan, and then gives the range after weighing all of it. The gloss script flagged the sentence and I reworded it before the commit, so the existing fix worked, but I wrote the connective myself, which is the same mistake as the one a reflection in October named.

### Learn

When a dated verdict changes, report the change as two measured movements before stating the new label: how far the estimated value moved and why, and how far the price moved. The reason is that a verdict is a ratio of two things that move for different reasons and at different speeds. The value moves when evidence about the business arrives, usually quarterly; the price moves every day on news, fear and policy. A label that compares them can flip on either, and the holder can only judge the label if he knows which one did the work. For Alibaba the answer was mostly the price, and that tells Suggi where to look: at whether the export rule damages what he owns, not at whether the quarter was good.

The same discipline applies inside the value side. When an input is annualized from the latest quarter or rolled forward through a trailing window, a single unusual quarter entering or leaving the window can move the value by a step that is not new information about normal earnings. Name that step. Here dropping one subsidized quarter lifted the trailing e-commerce sum by about a quarter of its size, and mark-to-market gains on the investments lifted the equity adjustment, which puts market prices inside the value.

The lesson has limits. The decomposition does not say who is right: the market may have priced a loss in cloud value that my method leaves in a hint, and then the price move is information I failed to count, not noise. It also does not apply to a business whose value is mostly its share price of something else, like a holding company valued at its listed stakes, where value and price move together by construction. And it can mislead if the decomposition is read as a forecast of reversal; Graham's partner is sometimes right.

## Key Learning and Improvement

The major learning is that a changed verdict is a joint product of a moving estimate and a moving price, and that reporting the new label without its parts hides the most decision-useful fact: whether the business or the market changed. In this run the price did about two-thirds of the work, and the value change itself leaned on annualizing one quarter and on marked-up investments, so the flip from overvalued to undervalued says less about Alibaba's business than its wording suggests.

The improvement I would suggest is concrete and cheap. The scheduled results job's reply and the Hub file's Valuation summary should carry one line computed in the ledger: the Base value change in percent, the price change in percent, the share of the change in the price-to-value ratio that came from the price, and the largest single input behind the value change. The ledger already holds every number needed, so the cost is a few lines of script and one sentence in the reply. It would prevent the reader from mistaking a market move for a business change, and it would show at a glance when the value change rests on an annualized quarter or a portfolio mark. I would know it worked if, over the next few results jobs, Suggi's follow-up questions start from the attribution line instead of from the label.

## Cross-links

- `reflections/2026-11-25_neo_a-source-file-i-write-is-a-claim-not-a-source.md` -- the Prosus results run earlier the same day, which also reproduced a dated valuation from its Trash ledger before changing inputs.
- `reflections/2026-10-07_neo_a-sourced-sentence-fails-at-its-connectives-not-its-facts.md` -- the earlier lesson that sourced sentences fail at their connectives; this run repeated the class with "because" and the gloss check caught it.
- `reflections/2026-10-16_neo_a-seed-test-protects-only-the-commit-it-can-block.md` -- seeds placed ahead of the commit, which blocked the two word-swap seeds here until exact-phrase binds were added.
- `library/value-investing/mr-market.md` -- Graham's partner who quotes a different price each day, the frame for separating price movement from value movement.
- `library/value-investing/margin-of-safety.md` -- why a price below an earnings-proxy Base is not a margin of safety.
- `investing-hub:companies/BABA.md` -- the revaluation this run produced.
