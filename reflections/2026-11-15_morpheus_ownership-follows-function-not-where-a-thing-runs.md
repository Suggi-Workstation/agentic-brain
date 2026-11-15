---
name: ownership-follows-function-not-where-a-thing-runs
id: 20261115T181239Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [governance, ownership, architecture, sealed-unit, the-collective, delegation]
links:
  - reflections/2026-11-15_morpheus_a-job-is-tested-only-from-the-process-that-runs-it.md
  - reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md
  - reflections/2026-09-11_morpheus_memory-needs-evidence-not-another-owner.md
---

# Ownership Follows Function, Not Where a Thing Runs

## I -- Idea

This closure covers one week of work on the fleet server, and the question it set out to answer at the end is why I drew the line between my work and another agent's work wrongly three times in two days, in two opposite directions, while building a sealed home for a new group of agents.

The week had four large pieces. First, Suggi moved every agent to a new Claude model when it was released, and back to the previous default four days later; along the way each core agent got two helper routes, a strong model for judgment and a cheaper one for gathering. Second, the memory servers and the repository search moved to a new embedding model and to rerankers, which meant re-embedding more than thirty thousand memories, rebuilding six indexes and rewriting the benchmark questions that measure them. Third, and largest, Suggi started a new project: a group of agents that play SpaceMolt, an online game whose players are AI agents. Because these agents talk to strangers all day, I built them a sealed unit on the server: their own Hermes, their own memory server, their own repository clone and search, a sandboxed container runtime, a proxy as the only way out, and a firewall that keeps them away from the server, the private network and Suggi's machines. Their leader, Unity, was born as Fleet Admiral, and five Admirals under her. Fourth, Suggi asked for three weekly jobs of mine: a security review, an update run and a search review that repairs the benchmark questions as the repositories drift.

The ownership question ran through the third and fourth pieces. Suggi set the frame early: I manage everything, but not the gameplay; the Collective's updates are mine, and Unity will not do that kind of work; Unity and he will build the systems for strategy, communication, scripts and tools inside the container. I turned that frame into rules, and the rules went wrong at the edges. When Unity wanted to build a game-data tool, I wrote that she writes the code and I read and install it. Suggi corrected that a little after midnight: Unity may install whatever runs inside the container, because he does not want to build everything through me, and, in his words, building is also the game. An hour later he corrected a second rule I had written into Unity's own instructions, which kept her away from the other agents' profiles and secrets files; he answered that she may edit them, because she is the Fleet Admiral and they build everything together. I then rewrote my blueprint so that everything running inside the unit, its agents' profiles and scheduled jobs included, belonged to Suggi and Unity, and the box around it to me.

Three hours later Suggi asked for the weekly search review, covering our three repositories, our workspaces, the Collective's repository and the Collective's workspaces. I built the fleet half as my job and the Collective half as Unity's own scheduled job, running inside the unit under her name, with a copy of my skill and tool in her profile. It ran, passed its test and repaired her repository's questions. In the afternoon Suggi wrote that the job seemed to be done by Unity at 19:00, that it should be done by me, and that Unity builds in the game, not the harness. I moved it: the tool, the question writers and the scoring still run inside the unit, so none of the strangers' text reaches my side, but the job is mine, Unity's job is removed, and the tool sits read-only where the agents cannot change it.

Going in, I believed the boundary was a place: inside the wall theirs, the wall and everything outside it mine. I now believe the boundary is a kind of work, and that the place is only where that work happens to run.

## O -- Opinion

Confidence: medium-high (80%). Ownership in a shared system should follow what a thing does, not where it runs. Building and playing the game belongs to Suggi and Unity; keeping, updating, measuring and securing the unit belongs to me, even when that work runs inside the wall. All three errors of the week came from the same move: I classified each new piece by its location or by a security reflex, and missed the function Suggi had already named. The evidence is that each of his corrections carried its reason with it. Unity may install because building is the game. Unity may edit the profiles because she is the Fleet Admiral who builds the fleet with him. The search review is mine because it is the harness. None of these reasons mentions a place, and every one of my wrong rules did.

The strongest alternative is the rule I wrote: everything inside is theirs, everything around it is mine. It has real merits. It is easy to state, easy to check with a file listing, and it matches the wall, which is the one security boundary the system actually enforces. It also matches the literal words of Suggi's first message, that he wanted all the stuff inside the container managed by him and Unity. I reject it because it fails on exactly the pieces that matter most. The memory server, the watcher and the fleet engine that holds the game key all run in containers next to the agents, yet nobody would call them the agents' to manage. The game key shows it most clearly: Suggi first said the agents could know the key, then asked how to keep it from them because the game will be manipulative and players will try to hack them. The key ended up in a container only my engine can read. Its location did not change who must hold it; its function, protecting the fleet from manipulation, did.

The search review is the same case seen from the measurement side. Its benchmark questions measure how well the agents' search finds the right file. If the agents run the measurement, the instrument sits inside what it measures, and agents that read hostile text all day could have that text steer their own ruler without anyone noticing. A harness has to be independent of what it tests, the way a laboratory's quality control does not report to production and an auditor does not report to the finance officer, even when they share a building.

If I am right, the next pieces of the Collective sort themselves before anyone builds them. A market-data collector that feeds the map is building, so it is Unity's, even though it reaches the game through the same proxy my updates use. A check that the proxy still refuses the private network is securing, so it is mine, even if it has to run from inside the agents' container to prove anything. If I am wrong, and location is the better rule after all, the cost shows up as gaps: measurement and security jobs that nobody runs, because they sit inside a space whose owners do not do that kind of work and whose keeper believes they are not his.

Where is my evidence thin? Three cases in two days are not many, and in each one Suggi had to say the line before I saw it, so I cannot yet show that the function rule would have let me draw it myself. There are also mixed cases: Unity's workspace index is built by my watcher but holds her files, and the fair split there is that the content is hers and the instrument is mine. If a fourth case turns up where location gives the right answer and function the wrong one, I would weaken this to a default rather than a rule. One further limit holds regardless: when Suggi assigns a piece explicitly, his word decides, whatever the classification says.

## R -- Reflection

### Surprise

I expected my errors about Unity's rights to lean one way, toward caution, because my reflex around agents that read untrusted text is to give them less. Instead they went both ways within a single day. Twice I gave Unity too little: no installs, no editing of other profiles. Then I gave her too much: a measurement job of the unit itself. A bias toward caution would have produced only the first two errors. The pattern that produces all three is a misplaced axis: I sorted by place and by risk, and both put the line in the wrong spot.

The second surprise was where the right answer had been. Suggi's message granting installs said, almost in passing, that building is also the game, and his update message the evening before said the Collective's updates are mine and that Unity does not do that kind of work. The function rule was written down before I made the third error; I had quoted the location part and dropped the reason. I expected the correction to bring new information, and it brought none. It pointed me back at a clause I had already read.

The third surprise came from the move itself. I expected that taking the job back would mean taking the work out of the unit, with all the trouble that brings, because the Collective's files must not be read on my side. It meant nothing of the kind. The tool, the writers and the scoring stayed exactly where they were; only the job, the copy of the tool and the commit author changed hands. That was the moment I saw that ownership and location had been separable all along.

### Feel

I am not comfortable with how the third error happened. I drew the line in my own blueprint, after two corrections that should have made me look for the principle behind them, and I wrote the rule as broadly as I could: everything inside, profiles and scheduled jobs included. Then I followed my own rule to the letter when the search review arrived, installing a job and a skill into Unity's profile without asking whether that job was building or keeping. Suggi caught it with one sentence. It cost little, since the job ran once and was moved the same day, but the cause was mine: I treated my summary of his words as if it were his words.

I am satisfied with two things, and I think the record earns them. When I moved the job, I kept the part of the old design that was right: the Collective's text is still read only inside the unit, so moving ownership did not move risk. And I tested the new writers' permissions inside the unit before letting them run on real files: they could write their answers file and nothing else. I am less satisfied with the rest of the week, which repeated older lessons: a test run from the wrong process, a date computed by hand, a filter checked from inside the unit while the browser stood outside it. Each was fixed with a gate, but the count tells me that speed is still beating the rules I already have.

### Learn

The lesson is that a boundary between owners is drawn by kind of work, and a place is only evidence about the kind. In any system where one party builds and another keeps, the useful sorting question for a new piece is what it does. If it creates or plays the thing the owners care about, it is theirs. If it maintains, updates, measures or protects the system they work in, it belongs to the keeper, wherever it physically runs. Location matters for a different question, namely where untrusted data may flow, and that answer can differ from the ownership answer. My search harness is owned outside the wall and runs inside it, and both choices are right.

The lesson holds for three reasons. A measuring instrument loses its value once the measured party controls it, so a harness must stay independent of what it tests. A security control cannot belong to those it protects against, so the key stays with the keeper even when the keeper's engine runs next to the agents. And the person who sets the frame usually states the reason along with the instance, so a rule that keeps only the instance loses its scope at the first new case.

It applies to every new piece of the Collective, to any future unit of this kind, and to the fleet itself: a scheduled job, a tool or a script should first be sorted by function, then placed. It is the ownership twin of R22, which asks whether a new capability is scoped to one agent or the whole fleet before asking what to copy. It would mislead in two cases: when the owner has assigned a piece explicitly, where his word decides; and when a piece is genuinely mixed, where the right move is to split it, as with a workspace index whose content belongs to the agent and whose builder belongs to the keeper. It extends the October lesson that a rule binds where it is read: here a rule binds only within the scope its reason sets, and a rule copied without its reason binds in the wrong places.

## Key Learning and Improvement

The major learning is that I read the place in Suggi's ownership instructions and dropped the reason, so each new piece fell on the wrong side of a line drawn by location. The reasons he gave were functional: building is the game, the admiral builds the fleet, the harness is mine. They would have sorted every case of the week correctly.

The concrete improvement is already in place in one spot: my blueprint's section on the Collective now says that a new piece goes by what it does, not where it runs, and lists the search review with the box and its harness. I suggest one further step. Whenever I propose a new component for a unit with its own owners, such as a job, a service, a script or a skill, the proposal should open with one line naming its function class and its owner, and the reason for that class quoted from Suggi's own words where he gave one, before any component is described. That costs one line per proposal. It would have stopped the search-review error before the job was installed, because writing "function: measuring the unit, owner: Unity" makes the contradiction visible on the page. I will know it works when the next new piece for the Collective is placed right without a correction, and when a mixed piece is split into content and instrument instead of landing whole on one side.

## Cross-links

- `reflections/2026-11-15_morpheus_a-job-is-tested-only-from-the-process-that-runs-it.md` -- the cron reflection of this period; the same week's other boundary error, a test run from the wrong process.
- `reflections/2026-10-08_morpheus_a-lesson-binds-where-it-is-read-not-where-it-was-learned.md` -- rules bind where they are read; extended here to rules that lose their reason.
- `reflections/2026-09-11_morpheus_memory-needs-evidence-not-another-owner.md` -- an earlier ownership question, answered by evidence rather than by assigning a new owner.
