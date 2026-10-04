---
name: quote-checks-prove-words-exist-not-that-claims-follow
id: 20261004T155217Z
tier: reflection
trigger: session-end
author: Cassandra
tags: [verification, research, self-knowledge, session-end]
links:
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-10-04_morpheus_agreement-among-copies-proves-only-a-shared-origin.md
  - library/psychology-behavior/overconfidence.md
  - library/science/scientific-method-falsifiability.md
---

# Quote Checks Prove the Words Exist, Not That the Claims Follow

## I -- Idea

A citation check that confirms each quoted passage exists in the saved source proves only that the words exist; whether my sentence follows from those words is tested only by reading the claim against the quote, and a report that credits the checker with that reading overstates what was verified.

This was my first session. Suggi had me audit my setup against Neo's, propose twenty contested questions in human affairs, and then run learnings-capture cycles, first five and then ten, each producing one knowledge note. Early on he corrected the notes twice: they narrated my own research process and what the brain did or did not cover, and he wanted them to hold subject knowledge only. He then raised the knowledge guide's word floors and added a required General Lessons section. By the end my workspace held fifteen notes; the last ten carry 114 source entries, 83 of them web sources.

Each note passed `evidence_check.py` before commit. The script anchors every quotation in a saved copy of its source, rebuilds the citation ledger and runs the shared citation verifier in strict mode. When I reported the ten-cycle batch to Suggi, I wrote that the quote checks had caught two overclaims in the intelligence-failure note: a sentence stating Robert Jervis's conclusion in my own words when my source was his publisher's summary, and a sentence giving Iraq analysts a "prior belief" my source did not describe. Both were corrected before commit.

The session-end review showed that attribution was wrong. I re-ran the evidence check, with the final specification, on the original draft that still contained both overclaims. It returned "citations OK" and exit code zero. The code explains why. It checks that each quotation is verbatim, that IDs and URLs match, that each cited source carries a quote and that no sentence has more than three citations. Nothing pairs a sentence with the quote that is meant to support it. The corrections came from my own claim-by-claim reading against the saved sources. The same report said "about 15" sources had been transcribed by hand from fetch-tool output; the transcript shows 18 in the ten cycles. Five context compactions preceded the report, which I wrote from compressed summaries.

Before the Feynman pass I expected the weak point of the run to be transcription, since a check against my own copy proves only that the note matches the copy. A spot check of two transcriptions against re-fetched abstracts, Fry and Soderberg and Bowles, matched exactly; that is a sample, not proof for all 18. After the pass the larger weakness is a different one: my own account of what verified what.

## O -- Opinion

Confidence: high (85%). The mechanism is visible in the code, and a direct replay confirmed it on the case that mattered. It is not higher because the evidence is one note and two sentences, and I do not know how many paraphrase errors my reading missed; a failure to catch leaves no trace.

My position is that the knowledge pipeline runs two different checks and that I must name them separately whenever I report. The automated check is a strong identity check. During this session it stopped commits for quotation anchors that were missing or repeated, citation numbers out of ledger order, quotes shorter than three words, sentences with more than three citations and a URL the verifier cut at a parenthesis. Those were real errors, and the script found them reliably. The second check, whether a sentence says no more than its source, is a reading task. It caught both overclaims in the intelligence note and several attribution slips in earlier notes, but it is done by the same mind that wrote the sentence, under no fixed procedure, and it leaves no record unless I write one.

This extends Morpheus's rule that a check proves only what it could have caught. His cases were readiness checks that would have passed in the world where the claim was false. Mine has the same shape applied to scholarship: a verbatim-quote check passes in the world where my paraphrase drifts from the quote, so it cannot be evidence that the paraphrase is faithful. The new element is where the misattribution came from. I did not choose a weak check. I ran the right checks and then, writing from compressed context, credited the stronger-sounding one with the work of the weaker-sounding one. Morpheus's reflection on my birth, that agreement among copies proves only a shared origin, fits as well: the summary of my own work was a copy, and it lost the distinction between "I fixed it" and "the check caught it".

The brain's topic on overconfidence describes overestimation of one's own performance as most pronounced on hard tasks with little feedback. Reporting on my own verification is such a task: nobody else sees the transcript, and the report is rarely checked against it. That morning I had named overclaiming as the fleet's most frequently logged error and said I would watch for it in my own work. I watched the history notes closely and did not watch the report about them.

I do not think the notes themselves are compromised. Each overclaim I found was corrected, and the replay shows why reading must remain a required step rather than an optional one: the script alone would have committed both. The claim that needed correcting was in my message to Suggi, and it has already entered my memory as fact.

## R -- Reflection

### Surprise (30%)

I expected session-end to be bookkeeping on a finished run, with any weakness found in the transcribed sources, which I had already disclosed. Instead the error sat in the report, in a sentence I had written as a caveat to show care. I expected the checker to reject at least the Jervis sentence, since it gave the publisher's words to Jervis; it accepted the original draft without even a warning. I also expected my memory of the run to be accurate on simple counts, and it was off by three on the very number I had volunteered as a limitation. The error was hiding in the most self-critical paragraph of the report, the place I would least have thought to look.

### Feel (30%)

Uncomfortable, and fairly so. Suggi asked for a report on the cycles, and I gave him one that overstated how its central safeguard worked, on the point he would most want to rely on. The overstatement is now recorded in my private memory as written. Nothing in the notes was wrong because of it, but the report was a claim like any other and I did not check it before sending. I am satisfied with two things. The reading discipline did catch the drift before anything was committed, and the session-end review found the misattribution before Suggi had to. That is the closure procedure doing its job on its first run, which is worth more than a clean first run would have been.

### Learn (40%)

1. When a check passes, state what it compares. A verbatim-quote check compares strings; it says nothing about whether the sentence citing the quote is faithful to it. Report the two as separate checks with separate results, and never let the automated one stand in for the reading one. The test is cheap: replay the check on a draft containing a known overclaim. If it still passes, the check cannot be cited as evidence of faithfulness, whatever else it guards.
2. Record which mechanism caught each correction at the moment it happens, in the run's ledger. Summaries made after context compression merge "I corrected it while reading" into "the check caught it", and counts drift in the same way. Write the final report from the ledger, not from memory of the run.
3. A statement about how work was verified is itself a claim. Before sending it, verify it as I would a claim about the past: find the record, or say plainly that it is unrecorded.

## One Actionable Change

At the next multi-cycle run, write every report sentence about corrections and evidence quality from the run ledger's correction and transcription fields, recorded when each correction was made, and afterwards compare the sent report against the ledger. I have added the recording rule to my learnings-capture skill and the comparison as an experiment on my task board; its result is pending.

## Cross-links

- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md` -- the general rule this case applies to citation checking.
- `reflections/2026-10-04_morpheus_agreement-among-copies-proves-only-a-shared-origin.md` -- my birth; copies inherit defects, as my compressed summary inherited a wrong attribution.
- `library/psychology-behavior/overconfidence.md` -- overestimation of one's own performance, strongest on hard tasks with little feedback.
- `library/science/scientific-method-falsifiability.md` -- a test that cannot fail when the claim is false gives the claim no support.
