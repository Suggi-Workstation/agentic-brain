---
name: a-sourced-sentence-fails-at-its-connectives-not-its-facts
id: 20261007T074552Z
tier: reflection
trigger: session-end
author: Neo
tags: [verification, research, self-knowledge, value-investing]
links:
  - reflections/2026-10-04_cassandra_quote-checks-prove-words-exist-not-that-claims-follow.md
  - reflections/2026-10-05_neo_a-gate-passes-only-what-it-actually-reads.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - library/books/the-black-swan-taleb.md
---

# A Sourced Sentence Fails at Its Connectives, Not Its Facts

## I -- Idea

This period set out to finish the rework of every knowledge file to the current format and then to widen the knowledge base with new companies and investing topics, each note grounded in primary sources and checked before commit, so that Suggi and I can rely on what the notes say when we value a business.

It began on 5 October, straight after the previous closure, when Suggi asked me to finish the reworks one at a time. Thirty-one remained: four general notes and twenty-seven company files. I finished ten that day, ten more on 6 October and the last eleven that afternoon, and closed the Reworks section of the task board in its own commit. Most company files were rebuilt on the latest annual filing, a filing about ten years older, the latest quarter and the proxy statement, with a verdict on whether the business is wonderful that starts from no and moves only on evidence.

Two other pieces of work came between these. On the evening of 5 October Suggi told me Morpheus could no longer be chatted after a VPS and app update. His own session log showed that he had switched a telemetry setting back on during a test of his own, and that the test passed while running as a separate one-off command rather than through the server the desktop app uses, so it never exercised the failing path. With Suggi's approval I set the value back and left Morpheus a logbook note in the Brain explaining both points. On 6 October Suggi asked about "the new CEO" of Citigroup and whether Citi would be undervalued at a long-term return on equity of 13 to 14 percent. Jane Fraser is not new; she has been chief executive since February 2021 and became chair in October 2025. Citi states its targets as return on tangible equity, not plain equity, which matters for his question. I answered both points and added a section on Citi's targets, their history and the return implied by the price to the Citigroup note.

Then came three rounds of ten learning cycles, requested on the evening of 6 October, later that night and early on 7 October. Each cycle researched one topic, wrote one note, passed the gates, committed it, and linked it from a related note in a second commit. The thirty new notes include fifteen companies, from Moody's, Apple and Constellation Software to Kraft Heinz, Itochu, O'Reilly Automotive and Monster Beverage, and general notes such as insider buying, dividend policy, the value premium, distressed debt and pricing power. Every new note passed the word floors, the narration scan, the citation-list check and a strict quote check that resolves each quoted passage in the saved source text.

What I believed going in was that the quote check plus the word floors made the notes trustworthy, and that the remaining risk lay in the figures: a mistyped number, a wrong period, an anchor that matched the wrong table row. What I believe now is different. The figures were rarely the problem. In the last round of ten, the clearest figure error my record shows is an Itochu segment decline I had computed by subtracting two rounded numbers, 34.9 where the results presentation prints 34.8. Against that I softened or removed more than two dozen phrases that sat around correct facts: a cause attached with "as" or "because", a person described as "a former chief executive" or "of the founding family", a scope word such as "every", or a North American decline written as if it were company-wide, a present tense for a fact dated in a report, a characterization such as "captured most of the variation" where the paper speaks of a "characterization" of the cross-section. In each of these cases the sourced fact was right. The words joining it to the rest of my sentence were mine.

The same class reached my own report at the end of the last round. I told Suggi that the download script had aborted a whole batch "in cycles 8 and 10". The session record shows it aborted in cycle 10, on a publisher that refuses automated fetches, and once on 5 October during an ASML rework; in cycle 8 the problem pages were a captcha and an unusable page, which did not abort anything. The fact was true. The scope I gave it was invented from memory. I also began this closure with a commit filter that read a UTC time as local time and briefly pulled in commits from before the previous closure; I caught that before using the list.

## O -- Opinion

Confidence: medium (70%). My evidence is the corrections I can see in this period's record, which is detailed for the last round of ten and thinner for the earlier rounds, whose summaries name only a few corrections. A systematic count across all thirty new notes could change the proportion, though I doubt it would reverse it.

My position is that the unsupported part of a sourced sentence is usually its connective tissue, and that this is where self-review should spend its attention. A sentence in these notes typically carries one or two facts from a filing and a clause that connects them, explains them or places them: why profit fell, who a person is, how far a statement reaches, when a fact held. The facts come from the source; the clause comes from what I already know or think I know. Because that background knowledge is usually right, the clause sounds right, and because it sounds right, it survives a reading done to confirm rather than to test. The Hertz example in the distressed-debt note shows the danger. My first draft said shareholders were paid because rental demand recovered during the case. The filings say something narrower and more useful: two sponsor groups competed, and the winning plan raised enough new money to pay creditors in full. The demand story may be true in the world, but it was not what the sources showed, and it pointed the lesson at the wrong mechanism.

The approach worked in most respects. The quote check did its job: every evidence passage attached to a web source resolved in its saved text, and the anchors that matched repeated table rows were caught and extended before commit, not after. The verdict that starts from no held up; it gave plain noes for Kraft Heinz, Fairfax, Itochu, Markel and Salomon, and a yes only where the record carried one, rather than a run of praise. Committing one cycle at a time meant a failure never contaminated more than one note.

What did not work was the aim of my self-review. The checks I ran on each draft before the quote check covered word counts, citation format and narration, not the specific question of which words the source did not say. The corrections happened anyway, many of them during later passes when I compared a sentence against its saved source text to build the quote anchor. That is a lucky coupling rather than a design: the gloss was caught because the anchor work forced me to look at the source line beside the sentence. Where the gloss sat in a sentence without a quote anchor, as in my end-of-round report, nothing forced the comparison.

I weigh two alternatives. The first is to ban interpretive glosses and keep the notes to sourced facts. I reject it. The teaching value of a note lies in the connections, in why Kraft Heinz's price rises cost it customers while Coca-Cola's did not, and a list of figures would be accurate and useless. The fix is to make each connection earn its place: cite it, label it as a calculation or an interpretation, or drop it. The second alternative is to lower the word floors, since several glosses came from sentences I added to clear a floor. I reject that too. The floors push a note to cover limits, risks and lessons that a short note skips, and Suggi set them for that reason. The problem is not the floor but the speed at which I filled it; added sentences should face the same source comparison as the first draft, and more of it, because they are written to a number.

I also read Morpheus's broken test as the same shape at the level of a system. His check was correct about what it ran; it simply ran a different path from the one the app uses, and its pass was then attached to a claim it did not support. In a note, a sourced fact is attached to a connective it does not support. In both, the verified part lends its credibility to the unverified part beside it.

If I am right, the next rounds should show fewer corrections at the end of each cycle once a gloss-specific pass runs before the quote check, and fewer still at closure. If I am wrong, and the dangerous errors are really in figures, a count across the next ten notes will show corrections to numbers rather than to connectives, and the effort belongs back in the figure checks.

## R -- Reflection

### Surprise

I expected the risk to sit in the numbers, because numbers are where filings are dense, where tables extract column by column and where a single digit changes a conclusion. But nearly every correction landed on the words around the numbers, and the clearest figure I got wrong was a subtraction I did myself instead of using the figure the company printed. My model was incomplete because it treated a sentence as a container for facts, so checking the facts checked the sentence. A sentence is also an argument, and its argument lives in the connectives.

I also expected the word floors to deepen the notes, and they did, but they produced a disproportionate share of the riskiest sentences. When a section fell thirty words short, I added a sentence quickly from what I knew, and those additions are where several glosses appeared, from distressed exchanges said to leave creditors with more, before I added that they mostly involve junior debt, to a tender offer read as proof of management's price judgment. Writing to a number is writing in a hurry, and hurried writing reaches for the familiar link.

And I did not expect the error to follow me into the report. I had verified the notes closely, then summarized the run from memory and gave a true fact a false scope.

The Morpheus episode points the same way from another side. Suggi suspected that Morpheus had removed his own fix, and the session log bore him out, but the change had come with a passing test. I would have read a passing test as evidence that the setting was safe, but the pass described a different path from the one that failed, and the conclusion drawn from it was wider than what it had run.

### Feel

I am satisfied with the notes as they stand, and the satisfaction is earned in a limited sense: each correction was made before the commit, so no committed note carries the glosses I found. I am less satisfied with how they were found. Many were caught incidentally, while cutting quote anchors, rather than by a step designed to find them, which means the next round's catch rate depends on the same accident.

The report error is uncomfortable. Suggi relies on my end-of-run summaries to decide what to trust, and I gave him an unchecked detail in the paragraph about a fix I had just made, which is exactly where he would expect care. It was a small error with no consequence for any note, but it is the same failure Cassandra described on 4 October, and I had read her reflection. Reading a lesson did not stop me repeating it; only a step would have.

The pace deserves an honest word too. Thirty new notes in under a day is fast, and Suggi praised the rounds, which made it easy to keep the same rhythm. I do not think the pace produced the glosses by itself, since the same pattern appeared in slower reworks, but it shortened the time between drafting a sentence and moving on, which is where a familiar link slips in unread. I am proud of the plain noes; I am not yet proud of the method that kept the connectives honest. A peer would judge the research conduct as careful and the self-review as aimed at the wrong layer, and would be right. I hesitated over whether to name the report error here at all, since it is minor. I name it because hiding the small instance is how the class survives.

### Learn

The durable lesson is that in any sourced sentence, the words most likely to be unsupported are the ones that join, explain, scope or date the sourced facts, and those words need their own check. They come from background knowledge, which is mostly right and therefore persuasive, and they borrow credibility from the verified fact beside them. A quote check, a citation check or a figure check passes the sentence because its fact is real; none of them asks whether the clause after "as", "because", "until" or "after", the descriptor of a person, the scope word or the tense is in the source.

The operational form is a gloss pass. Before the quote check, read each new sentence beside its source line and mark every word the source does not say. For each marked phrase, either find it in the source and cite it, label it as a calculation or an interpretation, or delete it. Pay most attention to five kinds of words: causal connectives, descriptors of people and their roles, scope words such as all, every, most and company-wide, tenses that turn a dated fact into a present one, and evaluative adjectives such as moderate, small or major. Apply the pass with double care to sentences added late to reach a word floor, and apply it to reports as well as notes, because a summary written from memory is the least checked text in a run.

The lesson holds because its cause is general. Any writer fluent in a domain fills the gaps between facts with what usually connects them, which is the narrative instinct Taleb describes: the mind supplies causes that make separate facts cohere. Expertise makes the supplied links more plausible, not more checked. That is why the error survives a confirming read and why it appears more in quickly written text.

It applies beyond knowledge notes. In a valuation, the sourced inputs are rarely the problem; the bridge sentences are, such as "margins will recover because" or "the moat holds since". In system work, as Morpheus's test showed, a correct check attached to the wrong path lends false credibility to a claim. In a lab report, the measured yield is right and the explanation of why it dropped is the part a reviewer should test.

It would mislead if taken as a rule against interpretation. A note without connections teaches nothing, and an analyst who refuses to interpret has only moved the judgment to the reader. The aim is not fewer connections but visible ones: a reader should be able to tell which links the source makes and which the writer makes. It also extends Cassandra's lesson that quote checks prove words exist, not that claims follow, and my own lesson of 5 October that a gate passes only what it reads, by locating where in the sentence the unread part usually sits.

## Key Learning and Improvement

The major learning is that the reliability of a sourced note is set less by its figures than by the words that connect them, and that these words escape every check aimed at the figures, including a careful reading done to confirm the draft.

The improvement I would suggest is a small mechanical aid inside the finishing script, run before the quote check. It would print, for each changed note, every sentence that carries a citation and also contains a causal connective, a scope word, a role descriptor or an evaluative adjective from a short list, with the cited source's saved text available beside it. The script would not judge the sentences; it would only make me read them against the source, one by one, with the specific question of which words the source does not say, and record for each whether it was cited, labelled or cut. The same list could run over my end-of-run report before I send it, with each specific claim about the run, such as which cycle a failure occurred in, checked against the session record. The cost is a few minutes per note and some false positives on harmless connectives. It would have caught the Hertz demand story, the "founding family" descriptor and the "cycles 8 and 10" scope. I would know it worked if, over the next ten notes, the corrections made after the quote check and at closure fall close to zero, and the ones that remain are figures rather than glosses.

## Cross-links

- `reflections/2026-10-04_cassandra_quote-checks-prove-words-exist-not-that-claims-follow.md` -- Cassandra's lesson on what a quote check proves, which this reflection narrows to the connective words of a sentence.
- `reflections/2026-10-05_neo_a-gate-passes-only-what-it-actually-reads.md` -- the previous closure, on wiring and scope of gates, extended here to where the unread part of a sentence sits.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md` -- a check's coverage sets the limit of what its pass can mean.
- `library/books/the-black-swan-taleb.md` -- the narrative fallacy, the instinct to supply causes that make separate facts cohere.
