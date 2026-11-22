---
name: a-slipping-question-needs-the-judgment-a-miss-gets
id: 20261122T214715Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [gold-queries, evaluation, information-retrieval, brain-index, the-collective, cron]
links:
  - reflections/2026-11-15_morpheus_a-score-change-needs-the-same-ruler-and-a-kept-baseline.md
  - reflections/2026-11-15_morpheus_a-sealed-writer-must-report-its-process-in-numbers.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - research/insights/gold-query-maintenance-procedure.md
---

# A Slipping Question Needs the Judgment a Miss Gets

## I -- Idea

This run of the weekly search review set out to repair the gold question sets wherever their files had drifted and then to score every search index on this server, and the part of it worth reflecting on is what the scoring could tell me, and what it could not, about whether retrieval had become worse.

The job is mine and runs every Sunday at 17:00 UTC as a scheduled run with nobody present. A gold set pairs each question with the file that answers it; it is the ruler for the hybrid search that the agents use before they write or decide. The run has hard boundaries: it writes only the gold question files and its own records, it never rebuilds an index or edits a search tool, and it never changes a question because the question scores badly. Questions are written by independent writers who read the whole file and see neither search results nor the existing questions. The Collective, the sealed unit where the game agents live, gets the same treatment inside its wall, and its files are never read on the host side.

The preflight passed and found only my own cron entries of last week in the logbook. The plan found drift in two of the six host sets. The brain repository had one question to rewrite, because the watcher insight it points to had changed, and four new reflections to cover, all of them mine from last Sunday's cron runs. My own workspace had two questions to rewrite and nine new daily memory and identity files to cover. Two writers produced sixteen questions, the check passed them with no failures and no warnings, the apply step validated both sets, and the commits landed: the brain commit on GitHub within a minute, the workspace commit locally.

Scoring took 224.4 minutes in total, against 103.1 minutes last week for a question count that grew only from 685 to 698. The ranks did not move with the clock. Four host sets scored exactly what they scored last week, my workspace gained, and the brain repository fell from an MRR of 0.9353 to 0.9344. The tool printed three unchanged questions whose result moved. One of them, g271, asks why a security scan gate halts on clean days when short-lived socket files vanish before the classifier checks them. Its gold file is my reflection on that classifier. One query showed why it fell to rank 2: my newer reflection on the security review, written the same evening about a different fault, recounts the scan halts as its context and now ranks first.

The misses step then listed ten questions whose gold file was not in the first five, the same ten as last week at the same ranks. The rule added to the skill after last week's run says a judged miss keeps its verdict when its question, its gold files and every file ranked above them are unchanged. I reran the eight repository queries and read the git history of every ranked and gold file since last week's judgment. One file ranked above a gold file had changed, the watcher insight above the brain search README, so that miss was judged again and kept its verdict; the other nine carried. No relevance set grew.

Inside the Collective the drift was large: twenty-seven rewrites and twenty new files in its repository with seventy-one more waiting under the cap, thirty new files in the Fleet Admiral's workspace, and first gold sets for the five Admirals' workspaces. Eight sealed writers wrote 159 questions; every summary line showed no shell command other than the check and no refusal. Seven commits each hold one gold file, and the scores and five misses were listed, not judged.

Going in, I believed that the misses step is where the review notices a corpus that has grown, and that a question still inside the first five is healthy. I now believe the earliest sign of growth is a question that slips inside the first five, and that the step built to judge growth never looks there.

## O -- Opinion

Confidence: medium (75%). The direction I hold with more confidence than the size of the effect, because one week gave me one clear case.

My position is that the weekly review should judge an unchanged question that moved down the same way it judges a miss: read the file that now ranks above the gold file, add it to the relevance set when it answers the question as well, and report a retrieval slip when it does not. The review currently judges only questions whose gold file left the first five. That filter is narrower than the rule it serves. The gold-query maintenance insight in the brain already says that under material corpus growth the top-ranked results are reassessed and newly relevant files are added, and it names the exact signature I saw: recall stays complete, MRR drops slightly, because new relevant files rank above the gold files. So this is not a new idea that needs a new rule; it is an existing rule that the weekly step applies only at its far end.

The case for it rests on attribution. The brain repository's MRR fell by less than a thousandth this week. That number is useless unless I can say what caused it, and the honest answer today is that I cannot. If my newer reflection answers the g271 question as well as the older one, the fall is growth and the ruler is wrong; if it does not, the fall is a small, real retrieval loss. Both are possible from what I saw, and the run had no step that would decide between them. Over many weeks such unexplained slips add up to a drifting score that nobody can attribute, which is the condition the kept baseline and the moved-questions line were built last week to end. The moved line now names the question; this proposal finishes the job by giving the named question a verdict.

The cost is small. This week the host had three moved lines against ten misses, and two of the three moved by one place inside my own workspace, where one moved up. The carry rule makes a repeated judgment nearly free, because a slip whose surrounding files have not changed keeps its verdict.

The strongest alternative view is that a slip from rank 1 to rank 2 does not matter, because every agent's query skill tells it to read the top three to five files, so an agent searching for g271's answer would read both reflections and lose nothing. I accept the premise and reject the conclusion. The harm to an agent is indeed nil this week. But the benchmark exists to tell growth from degradation, not to measure harm, and a ruler that cannot attribute its own movement stops being a ruler. A second alternative is that judging inside the top five invites inflation, adding near-duplicates until every score is perfect. The standard guards against that: a file joins the relevance set only when it answers the question as well as the gold file, and a reflection that recaps an incident in its first paragraph does not answer a question about the mechanism as well as the reflection devoted to it. On my one grep, that is the likely verdict for g271, but I did not read both files whole, so I hold it as a guess.

On the doubled scoring time I take a narrower position: it is an observation, not a finding. The load average was between 14 and 22 at my checks and the swap was nearly full, but no record of last week's load exists, so I cannot attribute the slowdown, and I would not add machinery for it. The ranks, which are what the benchmark judges, were unaffected.

What would change my mind is several weeks of data. If moved-down lines almost never turn out to be equivalent answers, judging them adds cost and no information, and the current filter is right.

## R -- Reflection

### Surprise

I expected the scoring to take about as long as last week's 103 minutes, since the question sets had grown by only thirteen questions, and it took 224.4 minutes with ranks that were identical on every unchanged host question except three. I had treated the benchmark's run time as a property of the benchmark. It is a property of the server it runs on. The ranks come from the index and the questions; the clock comes from everything else the machine is doing at the same time, and this evening the machine was carrying the Collective's sandboxes, a security review that started at 21:00, and a swap file close to full.

I also expected the Collective's drift to look like the host's, a handful of files. Its agents had written so much in one week that the plan held seventy-one new files back under the cap after covering twenty.

The third surprise was the sharpest. I expected my own writing to add answers to the corpus, never to compete with them. My newer reflection displaced my older one on the older one's question, because I tell the story of an earlier incident as the context of a later one. The benchmark measures the index on a corpus that I keep writing into, so my writing habits are part of what it measures.

### Feel

I am satisfied with the parts of the run that the record supports. Every step ran in the skill's order, every number I report came from the tool, a query or git, and the carry rule did what it was proposed to do: nine verdicts carried on evidence, and the tenth went back to judgment for the right reason, a changed file ranked above the gold file, rather than from habit.

I am less satisfied with one check I wrote myself. To confirm that each of the seven Collective commits held its gold file alone, I wrote a small loop that read the commit list from a here-document and ran a command inside the unit for each line. The command forwarded its standard input into the unit, which consumed the rest of the list, and the loop printed one line for seven commits. I caught it because I counted the lines, and the rerun printed all seven. It is the same lesson I wrote down in September, that a check proves only what it could catch, and I applied it after the fact instead of before, by writing a check whose reach I had not tested.

I also notice a discomfort I should name without overstating it. I watched the swap of a server I own run close to full for four hours and only recorded it, because this run may not touch the box. That was correct, and the report will carry the reading to Suggi.

### Learn

The durable lesson is that in a retrieval benchmark over a growing corpus, the first sign of growth is not a miss but a slip inside the top results. A newer file that answers the same question as well as the gold file takes rank 1, the gold file drops to rank 2, recall stays complete, and the score falls even though retrieval is as good as it was. If the review judges only misses, healthy growth and real degradation blend into one unattributed number. So when an unchanged question moves down, the file that moved above it deserves the same judgment a miss gets: it joins the relevance set if it answers as well, and the slip is reported as retrieval if it does not.

The lesson holds because MRR rewards rank 1 alone. A relevance set written before the corpus grew is a claim about the corpus of that day, and every new file that answers an old question makes the claim a little more wrong without changing any question or any gold file. The moved lines are where that wrongness first becomes visible.

It applies wherever a ground truth is fixed before its corpus grows: search benchmarks, test fixtures whose expected output names one source, and the baselines my security review compares against. It misleads in two places. When the pipeline itself changed between two runs, a moved line measures the pipeline, not the corpus, and judging the files above it would credit growth for a model change; the tool's not-like-for-like note is the guard. And when the corpus holds near-duplicates, such as archived skills that restate current ones, judging them as equivalent would reward clutter, so an archive should answer as well only when it truly does.

A second, smaller lesson rides along: rank and time measure different things. Rank comparisons stay valid under load; time comparisons need the host's load beside them before they mean anything. The lesson extends last week's reflection on keeping the same ruler. There the ruler was the pipeline and the per-question record. Here the ruler is the relevance set itself, and it drifts with the corpus even when nobody touches it.

## Key Learning and Improvement

The major learning is that the weekly review's misses step is narrower than the maintenance rule it serves: the brain's gold-query insight already prescribes reassessing the top-ranked results as the corpus grows, while the weekly step judges only questions that left the first five. The run therefore names the earliest growth signal, an unchanged question slipping inside the five, and leaves it without a verdict, so a small change in MRR cannot be attributed.

The improvement I would make, offered to Suggi as a suggestion because this run may write only gold files and its own records, is in the tool's misses command. Besides the questions outside the first five, it would list the eval's moved-down lines for unchanged questions, and the run would judge the file now ranked above each with the same standard and the same carry rule a miss gets. This week that would have meant two extra judgments on the host, g271 and w075. It would cost a few minutes a week and would prevent a slowly drifting score that nobody can explain. I would know it worked when every MRR change on an unchanged host set comes with named questions and a verdict for each. A second, smaller suggestion: a verify command in the Collective script that prints each gold commit's files, author and committer and the repository commit's place on origin/main, so the skill's own verification is part of the tool and no run has to write an untested loop for it.

## Cross-links

- `reflections/2026-11-15_morpheus_a-score-change-needs-the-same-ruler-and-a-kept-baseline.md` -- last week's test run of this job, which introduced the kept baseline and the moved-questions line that named g271 here.
- `reflections/2026-11-15_morpheus_a-sealed-writer-must-report-its-process-in-numbers.md` -- last week's scheduled run, whose proposed carry rule for judged misses settled nine of ten misses this week.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md` -- the earlier lesson my commit-check loop repeated: a check's reach must be known before its silence is trusted.
- `research/insights/gold-query-maintenance-procedure.md` -- the maintenance rule that already prescribes reassessing top-ranked results as the corpus grows.
