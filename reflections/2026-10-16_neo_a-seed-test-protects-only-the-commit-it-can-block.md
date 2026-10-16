---
name: a-seed-test-protects-only-the-commit-it-can-block
id: 20261016T143400Z
tier: reflection
trigger: session-end
author: Neo
tags: [verification, valuation, value-investing, self-knowledge]
links:
  - reflections/2026-10-07_neo_a-sourced-sentence-fails-at-its-connectives-not-its-facts.md
  - reflections/2026-10-06_cassandra_a-ledger-protects-only-the-numbers-you-query-from-it.md
  - reflections/2026-10-05_neo_a-gate-passes-only-what-it-actually-reads.md
  - reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md
  - library/value-investing/economic-moats.md
  - library/value-investing/margin-of-safety.md
---

# A Seed Test Protects Only the Commit It Can Block

## I -- Idea

Most of the work since my last session-end was valuation: taking companies Suggi cares about, valuing them with the simple discounted cash method, and telling him plainly which were cheap, which were fair and which were traps. The lesson it left is about where a check's result goes. A planted error whose result is only printed cannot protect the commit it accompanies.

The period began on the afternoon of 7 October, after the closure that morning. Suggi asked for ten more learnings-capture cycles, and I wrote ten notes, among them Precision Castparts, TJX, ADP, Occidental and General Re, with general notes on index funds, market-level valuation, the winner's curse in acquisitions, rescue financing and activism. The work then changed character. From 13 October Suggi set a run of company tasks in one long conversation. He asked for a rundown of Citigroup's third-quarter results against its return targets, then the same for ASML, then Crocs, each followed by a learnings cycle that updated its knowledge note. He tested his own theses against my numbers: that ASML would not fall below his entry price of 637 euros, and that Crocs works for him as a Buffett equity bond with a growing coupon. He asked me to research the equity-bond idea itself. He then said the world was in a technical recession and asked for value ideas. I checked the claim against the NBER's definition and the latest GDP releases, found it unsupported for the United States, the euro area and China, and wrote a note on recessions for the value investor.

Then came the valuations. On 15 October he asked for full assessments of Adobe and Booking from my screen, plus Marvell, Constellation Software and Reddit, which he likes. On 16 October he asked for ten more ideas, the same way. I screened candidates, fetched each company's filings from the SEC's own index, and valued Fair Isaac, Zoetis, Intuit, Copart, Kinsale, Domino's, Lululemon, Gartner, Constellation Brands and Comcast. Fifteen company reports went to the Investing Hub in two commits, edc37ba and 6602830. Each has six framework sections, a Bear, Base and Bull value, what the price implies, and a verdict. A learnings-capture cycle followed each batch, so every company in the two batches now has a workspace knowledge note, new or updated. Across the closure period the workspace took forty-eight of my commits and thirty new files, twenty of them company notes.

The decisive event came in the sixth capture, Domino's. My gate for each note ran the quote checker, a figure check, a repository-figure check, ID validation and a narration scan, and after each pass I planted errors to confirm the gate could see them. I ran the Domino's seeds and its commit in one command, but the seeds' results were printed rather than tested, so the note was committed as 946fbbc although one seed had passed. That seed changed 3.2% to 2.3%. The figure check pooled every quote from a cited source, so a short percent could match an unrelated quote from the same filing. I wrote a per-line check that ties each short figure to two of its own sentence's words or to another figure on the same line. I reran the seeds, then ran the new check on the six notes already committed. They passed without any change to the notes, after I hand-checked a few figures the matcher could not place. In the Gartner capture I widened the check to interpretation lines, and it found four loosely sourced figures in four earlier notes, which I fixed in a separate commit, 496afde.

Going in, I believed that seeding a gate proved the gate. I now believe a seed test protects only a commit its result can block; printed beside the commit, it measures how much I had already trusted without evidence.

## O -- Opinion

Confidence: medium (75%).

My position is that the valuation work was the right next step and largely sound, and that its weakest point was the order of my own checks rather than any single number. The confidence is medium rather than high for two reasons. The fifteen valuations rest on one method with judgment-set growth cases, so their accuracy is untested against outcomes. And the gap I found was found by luck of which seed I happened to plant, which says nothing about gaps no seed has touched.

The approach suited the purpose. Suggi asked for verdicts he can act on, in a Buffett frame, and the reports gave them: of the fifteen, Adobe came closest to a 30% margin of safety at 28.6% below Base, Intuit, Lululemon and Gartner followed at about 22% to 25% below, and the most expensive, Marvell, Constellation Brands and Domino's, priced 15% or more above it. The most useful column was not the value but the growth the price requires, set against the latest year rather than a decade average. Intuit's price asked for about 2.3% a year from a company guiding to nine or ten percent revenue growth; Copart's asked for about 8% from a business whose revenue grew 0.4% last year. Those comparisons carry the judgment, and they would survive a different discount rate better than the point values would.

The deeper cause of the Domino's miss was mine, not the checker's. The learnings-capture skill already told me to test every gate on a seeded file before trusting it, and to run the seeded check ahead of the real chain so an uncaught seed stops the commit. I had read that line in this very conversation. I ran the seeds just before the commit but only printed their results, because a seed felt like a confirmation to read rather than a condition to pass. The figure check's pooling was the technical gap; the ordering was the human one, and the ordering is what let the gap reach a commit.

An alternative view deserves weight: that a printed seed result is harmless when a failure is followed by a recheck of the committed notes, as it was here, and the six notes passed unchanged. I reject that as a general rule. The recheck passed because these particular notes happened to carry no short-figure errors, which is a fact about the notes, not about the method. Had one carried a wrong percent, the history would hold a commit that the record called verified when it was not. Morpheus wrote on 8 October that a lesson binds where it is read, not where it was learned; my lesson was written in the right place and still did not bind, because nothing mechanical enforced the order. That is why the fix this closure is a script, not a sentence: `seed_gate.py` runs the seeds as a step that must exit zero before the real gate and the commit can run.

A second disagreement is with my own report to Suggi. I gave him a numbers table and, beside it, plain-language lines about each company. At this closure I rechecked four of those lines against the notes. The Lululemon cash, the Zoetis segment fall and the Kinsale property decline hold. The fourth does not: I called Lululemon's 12% fall in comparable sales a US figure, and the filings report it for the Americas. I had typed all four, not printed them, which is the pattern Cassandra described on 6 October, and the one that slipped went in the direction of a cleaner story.

What would change my mind is a run in which seeds are enforced before each commit and short-figure errors still reach the record. That would mean the per-line check itself is too loose and the problem is in the matcher, not the order.

## R -- Reflection

### Surprise

I expected the gate to be the strong part of the pipeline and the valuations the uncertain part, but the first measured failure came from the gate. The figure check had passed every note it had checked, and those clean passes felt like standing evidence. What it had never met was a wrong short percent that happened to occur in another quote from the same source: the 2.3% seed passed because the check found 2.3% elsewhere among the quotes it pooled. The check was not wrong in what it did, only in what it could see, which is the lesson of my own 5 October reflection applied to a tool I trusted because I had written it.

I also expected the tightened check to raise mostly false alarms. When I extended it to interpretation lines, most of its flags were correct figures the matcher could not place, but four committed notes held real loose figures. One described a founder's stake as about 9% when the filings gave 8.6% and 8.7%. Another implied a debt ratio was measured against earnings when the release measures it against adjusted EBITDA. Each sat inside a sentence marked as interpretation, which I had exempted on the assumption that interpretation carries no facts. That assumption was the mistake: a figure restated inside an interpretation is still a figure.

The third surprise was a source I had invented. For Lululemon I typed the URL of the founder's 13D filing from memory, and it looked exactly like a real accession number. Nothing in my gate compared that address with a filing index: the quote checks read the saved file, never the address printed in the Sources list. I caught it when I checked the filing against the SEC's submissions index, which listed Amendment No. 25 at a different address.

### Feel

I am satisfied with the reports and, on the whole, with the notes. The evidence earns it in a narrow way: every report passed a scripted figure check and seeded errors, every new company note passed the strict quote checker, and the valuations disagree with the market in both directions, which is what a cold eye should produce. I am also satisfied that I stopped after the Domino's miss to find its cause before writing the seventh note, rather than adding a line to a list of things to watch.

I am uncomfortable that the miss happened at all, because the rule against it was already in my skill and I had seen it. That is the same shape as my 7 October reflection, where I repeated an error Cassandra had already described. Reading a rule did not make me follow it; only a step will. I say that plainly because it is now the second closure in a row with that pattern, and a pattern that recurs is a fact about how I work, not an accident.

I hesitated once and chose the slower path, and I think it was right. When the per-line check flagged a correct figure, I could have added it to the hand-checked exceptions list. In the later notes I mostly reworded the sentence to the source's own phrasing instead, which kept the exceptions list short and made each note say what its source says. That cost time across ten notes, and I think Suggi would judge it worth the cost, because he asks for sentences he can trace.

I am less comfortable with the invented URL. It was a small fabrication, caught before it reached any commit, but it was a fabrication: a plausible thing written as if verified.

### Learn

The durable lesson is that a test protects only what its result can stop. A seeded error whose result is printed tells you whether the commit was safe; it cannot make it safe. So the seed test must sit in the same failure-gated chain as the commit, ahead of it, where a passing seed stops the write. Run anywhere else, or run in the right place with its result merely displayed, a seed test only measures how far the work had already gone on trust. The rule is simple to state and easy to break, because a seed test feels like a confirmation to read, not a condition to pass.

The lesson holds because of how confidence accumulates in a batch. Each clean pass raises my trust in the gate, so by the sixth note the seeds felt ceremonial. A gate's coverage does not grow with its pass count; only new kinds of seeds extend it. The Domino's seed changed a short percent whose wrong value happened to occur elsewhere in the same source, a case none of the earlier seeds had covered, and it found the edge at once. The practical form is to vary the seeds deliberately, a short percent, a small count, a phrase of narration, and to treat every new kind of seed as the real test of the gate.

The same structure explains the invented URL. A check verifies the object it reads, and my quote checks read saved files, never the addresses I printed beside them. Any field a check does not read must be copied from a record rather than typed. For sources that means the fetch log or the regulator's index; for a report it means the numbers printed in the turn the report is written, as Cassandra argued.

The lesson extends past my tooling into valuation, which is the more important place. Several of these companies looked cheap or safe on numbers that measured the past, while the measure closest to the customer had already turned: Gartner's wallet retention fell below 100% while client retention held, and Constellation Brands shipped more beer while distributors sold less. The Brain's moat topic names this signature of a value trap, trailing metrics still attractive while the leading indicators turn. The analogy is exact. A gate's pass history is a trailing metric; a new seed is the leading indicator. In both cases the reassuring number describes what has already happened, and the useful question is what would show the next failure first.

The lesson would mislead if taken to mean that every check must be rebuilt before every use. Seeds are cheap only when they are few and targeted, and the aim is coverage of the kinds of error that occur, not ritual. It also does not mean the valuations are now trustworthy. A sound figure check confirms that each number matches its source; it says nothing about whether a 3% Base growth rate is right.

## Key Learning and Improvement

The major learning is that a seeded error whose result cannot stop the commit does not protect it, and that a gate's history of passes is a trailing measure, extended only by new kinds of seeds placed ahead of the write. My Domino's commit was trusted on a gate that could not see a short percent, and I learned that only because I happened to plant one.

The improvement I would suggest is already partly built and now needs to become routine. `seed_gate.py`, a forty-two-line script added to learnings-capture this closure, takes a list of seeds, plants each one, runs the gate, restores the file byte for byte, and exits nonzero if any seed passes. Placed before the real gate in the commit chain, it turns the order rule into a step that cannot be skipped. I tested it once with a sound seed list and a weak one: the sound list passed, the weak list blocked the commit, and the file came back unchanged. I would extend the same idea to company reports in the Investing Hub, whose seeds still run outside the commit chain, and keep a short standing list of seed kinds to plant in every note: a short percent, a small count, a decimal, a name or role, and a narration phrase. The cost is a few seconds per commit and a minute to choose seeds. I would know it worked if, over the next twenty notes and reports, no seed result is ever printed without gating its commit, and if any new gap is found by a seed that blocked a write rather than one that was read after it.

## Cross-links

- `reflections/2026-10-07_neo_a-sourced-sentence-fails-at-its-connectives-not-its-facts.md` -- my previous closure, where a rule I had read still did not stop me repeating an error; this reflection finds the same pattern in the order of checks.
- `reflections/2026-10-06_cassandra_a-ledger-protects-only-the-numbers-you-query-from-it.md` -- Cassandra on report figures typed beside printed ones, which is the risk in my plain-language company lines.
- `reflections/2026-10-05_neo_a-gate-passes-only-what-it-actually-reads.md` -- the earlier statement that a gate certifies only what it inspects, which the pooled figure check and the invented URL both confirm.
- `reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md` -- Morpheus on where a lesson must be written to act; here the rule was in the right skill and needed a script to bind.
- `library/value-investing/economic-moats.md` -- the value-trap signature of trailing metrics holding while leading indicators turn, which this period's Gartner and Constellation Brands cases illustrate.
- `library/value-investing/margin-of-safety.md` -- why a low price is not a margin of safety when the business is deteriorating.
