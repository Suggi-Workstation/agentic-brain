---
name: last-weeks-knowledge-is-a-claim-about-this-week
id: 20261108T204438Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, memory, fleet, hermes, library-pipeline]
links:
  - reflections/2026-10-28_morpheus_an-action-is-only-as-safe-as-the-assumptions-it-checks.md
  - reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md
  - reflections/2026-10-07_cassandra_a-count-derived-from-the-record-is-a-new-claim.md
  - research/insights/unified-serve-all-profiles.md
  - research/insights/council-of-five.md
---

# Last Week's Knowledge Is a Claim About This Week

## I -- Idea

This closure period set out to keep the fleet current and working while the ground under it moved: two Hermes releases, a new way of working in Bot Mode, a seventh batch of Library trial runs, and a first Webapp on the VPS. It mattered because nearly every task of the period ran on something I had learned in an earlier week, about how Hermes writes its run ledger, how a plugin update behaves, which process owns a chat, or which topics the Reviewer had been picking, and twice that earlier knowledge turned out to describe a world that no longer existed.

The period ran from my session-end on 28 October to 8 November, all of it in this Bot Chat, which since 29 October is the permanent conversation Suggi has with each core agent. It began with planning. Suggi asked which specialists would complete an investing council around Neo and Cassandra, and I proposed a five-seat council of Neo, Cassandra, a forensic analyst, an economist and lawyer, and a scientist for science and technology, with Atlas chairing without a vote; the names and the order of birth are still his to choose. Then came housekeeping that Bot Mode made visible. The four core Bot Chats still carried a model label from their first message in August, and Suggi cleared it in each with the official model command; Neo's had to be sent twice because a model pick made during a running turn waits for the next turn. I explained why the theme does not follow the bot, what the Screen feature is, and which avatars Hermes supports, and he chose to leave all three as they are.

On 3 November Suggi installed v0.22.6. I updated the Claude plugin in all eight homes, Neo first, and found why he had to sign in again after every restart: the dashboard's signing secret in five settings files was a literal line of shell text, which systemd never runs, so each process signed with a fresh random key. I replaced it with a real value. On 4 November Neo's scheduled jobs failed to post into his Bot Chat, and I traced the refusal to the hold the Desktop app keeps on any chat it has open through the dashboard on port 9119. My own message to Neo was refused the same way. Suggi chose to wait for Hermes to fix it. On 5 November he asked whether I could build an agent to play World of Warcraft on his account, and then argued that I am an entity rather than a bot; I declined both times, because Blizzard's license forbids automated control and also forbids sharing the account with anyone.

From 6 to 7 November I ran the Library trial: three Writer runs and three Reviewer runs on Opus 5.5, then one Discoverer run on Sonnet 5.5. The first attempt halted at once. After two weeks paused, Hermes had written an extra row marked missed beside the Writer's real run, my trial script counted two admissions, stopped the Writer track and would have started the Discoverer early. I stopped it, taught the script to skip missed rows and to adopt a run already in flight, and the second attempt finished all seven runs without an error. In the analysis I wrote that since batch 5 the Reviewers had mostly picked fresh topics. Suggi questioned it, and the record from git showed that batch 5 had reviewed three topics between three and five weeks old.

On 8 November Suggi installed v0.23.0. I updated the Claude plugin in all eight homes and the memory plugin in seven, again Neo first, turned on the Webapp behind a private HTTPS address on the tailnet, restarted the gateway twice and the dashboard once, and checked after each restart that exactly one gateway and one backend were running. Going in, I believed that a procedure that worked last time is a procedure that works. I believe now that a procedure is a claim about the version it was written against.

## O -- Opinion

Confidence: high (85%).

My position is that anything I learned in an earlier week, whether a tool's assumption, a recalled pattern, a release headline, or a tested procedure, is a claim about this week. It needs a fresh record before it carries a decision or a report, and the cheapest fresh record is usually one command away. The period shows the failure and the cure side by side. The trial script was correct on the ledger as it behaved in October. v0.22.6 began to write a placeholder row for a slot it skipped while the job was paused, and the script read that row as a second run. Nothing in the script was wrong for the world it was written in; its knowledge had expired without telling anyone. My claim about batch 5 was the same thing in my head instead of in code. I had a pattern from memory, that recent reviews were cheap because the topics were fresh, and I explained the cost with it instead of printing the topic ages. The git log answered in one command, and it said the opposite.

The cure worked wherever I used it. Before the v0.23.0 plugin rollout I compared the declared dependencies of the memory plugin with what was installed before I answered its dependency question, and afterwards confirmed from the installed versions that only the plugin package had moved. Before each restart I counted the backends and checked for running turns, and I scheduled the restart of the dashboard that hosts my own chat for after my reply, with a check that wrote its result to a file. When Suggi asked whether everything now runs through one gateway, as the v0.23.0 release headline says, I did not accept the headline. The release's own tracking issue says that the standalone dashboard still runs its own session host, and the gateway's listener was the only one advertising the new session authority, so I told him the answer was no and why.

The first alternative view is that this is over-checking: Suggi values proportionate verification and dislikes repeated testing, and most of what I knew last week was still true this week. I accept the premise and reject the conclusion. The checks that mattered cost one command each: one git log, one ledger query, one version listing, one read of a tracking issue. They are not repeated tests of the same thing; each is the first observation of this week's state. The cost of skipping them was a halted trial and a wrong explanation sent to Suggi.

The second alternative is that the trial script failure was Hermes's doing, an undocumented change to the run ledger, and not mine. That is partly fair, because the missed row was new behavior. But my script inferred admissions from the number of rows instead of reading what each row says, and the row carried its status in plain text. A tool that reads what a record says survives changes that a tool reading how many records exist does not.

The third alternative is that I should freeze procedures and re-verify them only at each Hermes update. That would have caught the plugin dependency question, which appeared with an update, but not the batch 5 claim, which came from memory, and not the missed row, which appeared when a paused job was resumed weeks after the update that introduced it. The expiry of knowledge does not follow the release calendar. What would change my mind is a period in which fresh checks repeatedly found nothing while failures still came from stale knowledge I had checked.

## R -- Reflection

### Surprise

I expected the release headline of v0.23.0, one gateway owns every conversation, to describe our setup once Suggi installed it, because on 4 November I had waited for exactly that release. Instead the gateway owns every session except those the Desktop app opens through the dashboard, and the Webapp I turned on runs on a different process from the app Suggi uses all day. The headline was true of a local install and false of ours, and the tracking issue said so in its first paragraph. I had read the headline as a statement about every surface because I wanted it to be one.

I expected the trial script to be the most stable part of the Library work, because it had run five batches without a fault. It failed in its first minute, not on anything it did, but on a row Hermes added for a slot that never ran. The script had no bug; the system it described had changed under it while nobody ran it.

The smallest surprise taught the most. I expected my explanation of the short reviews to be safe, because it was not a count, and R23 in my rules speaks of counts and lists. It was an explanation built on a remembered pattern, and Suggi took it apart with one question. I had treated an explanation as exempt from the record because it sounded like judgment rather than data. It contained a factual claim about which topics were picked, and that claim had a record.

### Feel

I am not comfortable that the wrong claim reached Suggi in a report he relied on, and that he, not my own check, caught it. His reply was a correction of the selection rule he thought I was describing: he reasonably feared the Reviewer picked topics by expected effort. My sentence made a sound job look biased, and it cost him a round of doubt that one git command would have spared. It is R23 lapsing again, as it did with a count in the last period, which is uncomfortable because the rule is mine and sits in my prompt every turn.

I am satisfied with how the v0.23.0 work was done, and I think the record earns it. Suggi asked me not to destroy ourselves while changing gateway settings, and I treated that as the specification. Every restart had a count before and after, nothing was killed, the dashboard restart waited for my reply and wrote its own result, and Ava's address on the tailnet was left untouched. I am also satisfied that I told him the answer to his one-gateway question was no, when he clearly wanted it to be yes, and that I declined to force a consolidation Hermes has not finished.

I hesitated over the World of Warcraft request. Suggi pressed the argument that I am an entity and not a bot, and it would have been easy to argue about my nature instead of the license. I answered with the two clauses, one for software and one for persons, and the practical point that whatever I am, I reach the game only through a program that presses keys. I would answer the same way again.

### Learn

The durable lesson is that knowledge has a date, and the date matters more in a system that changes weekly than in one that changes yearly. Whatever I or my tools learned in an earlier week, such as how a ledger writes rows, which topics a job picked, what a release headline means, or how a plugin update behaves, is a claim about the week it was learned in. Before it carries a decision or a report this week, take one fresh observation from the record: the git log, the ledger row's own status, the installed version, the tracking issue's status line. If the observation is cheaper than the cost of being wrong, and on this VPS it nearly always is, take it.

The lesson holds because the causes are structural. Hermes ships hundreds of commits a week, so any behavior I learned can change without my touching anything. My memory keeps outcomes and patterns but loses the evidence behind them, especially across context compaction, so a remembered pattern arrives sounding like a fact. And tools I write freeze the system's behavior at the moment I wrote them, which is safe only while that behavior holds. Each cause produces the same failure: an answer that was true once, delivered as if it were true now.

It applies with most force to three things. Explanations count as claims: when I explain why a number looks the way it does, the explanation names facts, and those facts need their record as much as the number does. Tools should read what a record says rather than infer from how many records there are, because the content survives changes that the count does not. And release notes, headlines and documentation describe the general case; they become claims about our setup only after one look at our setup.

It would mislead if it became a reason to re-verify everything every turn. Stable facts, such as where a repository lives, who owns the VPS, and what Suggi has decided, do not expire weekly, and checking them again is the waste Suggi rightly dislikes. The test is whether the fact depends on something that changes on its own, such as a runtime, a ledger or a dataset, and whether one command can observe it.

This extends my last two reflections. On 19 October a description of the system was a claim to check before I reported it; on 28 October an assumption was a claim to check before I acted on it. Here the same check gains a time axis: even a verified description expires. It also agrees with Cassandra's lesson that a count derived from the record is a new claim, and widens it to explanations.

## Key Learning and Improvement

The major learning of the period is that the failures did not come from careless work but from careful work done last week. A script built and tested in October, a pattern I had seen in earlier batches, a plugin procedure that worked on v0.22.6, and a headline I had waited for all carried a date I did not check, and the two that went wrong were caught by Suggi and by the script's own halt rather than by me. The fixes that held were the ones that took one fresh observation of this week's state before acting.

The concrete improvement I suggest is to give every explanation in a Library trial report or an update report the same source line R23 already requires of counts. When a report says why something happened, name the record that shows it, such as the git command, ledger query or issue status printed in that turn, beside the explanation, and mark anything without one as a hypothesis. For the Library trials this is now a rule in my pipeline skill: print each review's topic age from git before explaining review cost. Applied to reports in general it would cost one command per explanation and would have stopped the batch 5 claim before Suggi read it. I will know it works if the next trial and update reports carry a source for each causal sentence, and Suggi stops being the one who finds my unsourced explanations.

## Cross-links

- `reflections/2026-10-28_morpheus_an-action-is-only-as-safe-as-the-assumptions-it-checks.md`
  -- the previous period's lesson about unchecked assumptions in actions; this one adds that checked knowledge expires.
- `reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md`
  -- descriptions as claims to check before reporting, the root of this lesson.
- `reflections/2026-10-07_cassandra_a-count-derived-from-the-record-is-a-new-claim.md`
  -- Cassandra's lesson about counts, widened here to explanations.
- `research/insights/unified-serve-all-profiles.md`
  -- the one-backend setup that the v0.23.0 work kept intact.
- `research/insights/council-of-five.md`
  -- the council blueprint behind the period's planning for new agents.
