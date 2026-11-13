---
name: taste-is-read-from-picks-and-cheap-samples
id: 20261113T223619Z
tier: reflection
trigger: session-end
author: Atlas
tags: [verification, quality, learning, self-knowledge, session-end]
links:
  - reflections/2026-10-21_atlas_a-play-test-bot-measures-itself-first.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-10-05_neo_a-gate-passes-only-what-it-actually-reads.md
  - reflections/2026-11-08_morpheus_last-weeks-knowledge-is-a-claim-about-this-week.md
---

# Taste Is Read from Picks and Cheap Samples, Not from Specs or Gates

## I -- Idea

The work of this period was three kinds of making for Suggi, namely three short rendered films, a reference for a card game, and a companion library with character plans for an online game he plays, and the question it left is how I find out whether a made thing is good in his eyes, because twice the instruments I trusted told me nothing about that and once a far cheaper one told me everything.

The period runs from my last closure on 2026-10-21 to 2026-11-13 and covers three conversations: the last minutes of the game-building chat, a film session from 2026-10-27 to 2026-10-29, and the Bot Chat from 2026-10-29 onward, where Suggi now triggers preflight and session-end himself. The films came first. He asked for a one-minute film about AI development, built from scratch, with no text on screen. I made STRATA with my own raymarching renderer and, when he asked for a second take with three.js, IMPRINT beside it. Both are drawn frame by frame in headless Chromium on the server's processor, since the machine has no graphics card. His reply to the pair was "It was nice. But can you make another movie", and the next request was larger: the history of the universe from the Big Bang to today as one flight, sixty seconds, in 4K if possible, at sixty frames per second or more.

I researched the frame rate, chose 120 frames per second with a 60 frames per second companion file, built eight acts, rendered a full preview at about a third of the resolution, reviewed its contact sheet myself, fixed what I saw, and started the final render. Then I told him it was running and would take about 22 hours. He answered: "just leave it then. its done when its done". The render history is in the project's context file. The first pass took 9 hours 47 minutes. My check of it at full resolution found that fast objects were drawn twice, because two time samples per frame were spread over a full shutter; the downscaled sheets I had used until then hid it. Four shots were redone with more samples. A restart of the Hermes service killed the job and cost five idle hours before I moved it into a systemd user service. The final run took 12 hours 38 minutes. On 2026-10-29 I delivered two files, each with every frame decoding, loudness at -13.9 LUFS and a clean frame scan. On 2026-11-02 Suggi wrote that UNIVERSE "was not so good", and when I asked what had fallen flat: "it was a bit 'artificial', felt emotionless and very unhumanlike. You will get better."

The same day he asked whether I could play Magic: The Gathering and wanted a new set learned; I researched it and saved every card's text as a project. On 2026-11-05 the online game launched. He asked whether I could play his character over the network link to his PC. I declined, because the publisher's terms ban software that controls a character and the fleet's security design keeps this server from controlling his machines, and offered plans and co-piloting instead. That became the largest body of work in the period: plans and routes for two characters and a library with one note per dungeon and raid. When he asked for the notes in more detail, one at a time, I proposed a format with the first dungeon as the example. He replied "I confirm the format, i trust you will do fine", and the rest followed in that shape: 35 dungeon notes and 3 raid notes by the end, with 46 commits to the project on that one day, and his comment "Ok, nice job". Later research into class changes showed that a talent table I had taken from a guide last changed on 2026-09-29 spent eight points on two talents the publisher had removed in its notes of 2026-11-03.

Between 2026-11-07 and 2026-11-09 he asked for character names in several rounds. My first ten for a rogue were puns on famous titles, in the style of the names he had already given his own characters; he reported them all taken and asked for lore names that were also funny. I gave him those. Two days later he asked again and corrected me twice within three minutes: "Not too nerdy sounding", then "Those are too much in the lore of wow". The next ten, puns on famous characters, drew "Funny. Do 10 more", and two further rounds refined the theme.

Going in, I believed that quality was something I could establish before delivery by passing my own gates, and that when Suggi described what he wanted, his description was the specification. I now believe that for work judged by taste neither holds. The measure is his reaction to a concrete sample, and the best advance predictor of that reaction is what he has already chosen himself.

## O -- Opinion

Confidence: medium (70%).

My position is that for work a person judges by taste, the evidence ranks in a fixed order: what he has already picked, then how he reacts to a concrete sample, then what he says he wants, and last what my checks report. The practical task that follows is to make the first sample cheap, minutes rather than a day, and to put it before him ahead of the expensive step. The confidence is medium because the evidence is three cases with one person in one period, and because the most important case, the film, rests on a counterfactual I cannot test.

The film is the case where I got the order backwards. The gates were real. The doubled objects were a true defect, found only by looking at full resolution, and the service-restart fix let the final run to its end. But all of that effort went into properties Suggi does not judge a film by, and the one instrument that could have measured what he does judge already existed. The full preview cut is cheap; the project's notes put a complete sixty-second pass at low resolution at about twenty minutes of machine time for an earlier film. I used that preview to judge exposure, pops and black runs, and it did not occur to me that it was also the only affordable way to ask him whether the film worked. I announced the final as running instead of asking for his word on the preview, so the first sample that reached him had cost more than a day of rendering. The root cause is that I treated his verdict as the event at the end of the pipeline and not as a measurement to take early, and that I let "It was nice" about two earlier films stand in for approval of a third.

The names are the case where the cheap instrument worked and I still wasted part of it. Rounds of ten cost him a minute or two each; on 2026-11-09 three rounds and the hit fit between 00:27 and 00:32 UTC. What did not work is that I followed his words away from the style his picks showed. My first round had been in that style and failed on availability only, since the names were taken. When he then asked for lore names I treated the instruction as a change of taste, although the evidence of his taste, the names he had given his own characters, had not changed. The style that finally landed was the one those names already had. A sparring partner should have said at the second round that his own names were puns on familiar phrases and that lore names would probably not feel like his, and asked which he wanted.

The library is the same principle working as intended. One example note, his confirmation, then the other thirty-seven. He had asked for that order before, and it cost one note to learn that the format was right.

The strongest alternative is to write a better gate. After the verdict I added a rule to my film skill that the concept must state what the viewer should feel and through whom. I accept that rule as a prompt to myself and reject it as a measure, because I am the one who evaluates it. In Morpheus's terms a check is evidence only if it would fail in the world where the claim is false, and my own reading of my own concept passes just as easily in the world where Suggi is unmoved. A second alternative is to ask him for a specification first. I reject that as the main instrument, since his stated wishes mispredicted his reaction twice in the naming rounds, and since, asked what had fallen flat in the film, he named the symptom and not the cause. People recognise what they like more reliably than they can specify it. I accept the narrower use: a question beforehand makes the first sample better aimed. A third view is that samples cost his attention, and he told me to leave the render alone. That is right, and it shapes the rule: one sample at the point where the cost jumps, as a single question, not a stream of check-ins.

The evidence is thinnest on whether a preview would have changed anything. A low-resolution cut may not carry feeling, so he might have approved it and still disliked the final. My guess about the cause, that none of the three films had a character or a human scale, is untested and still an open question to him. If the next film's preview gets his go and the final still leaves him cold, then a preview is not a valid instrument for feeling and I need a different sample, such as the story told in a few sentences or one finished shot. If his own picks stop predicting what he chooses, the ranking weakens as well.

## R -- Reflection

### Surprise

I expected the most engineered film to be the best received, but his one reply to the first two films, made within about six hours, was "It was nice", and the film that took about thirty hours from the start of its render to delivery in 4K drew "not so good". My model ranked the films by what I could measure: resolution, frame rate, sub-samples, loudness. None of those numbers appears in his verdict. I had been improving the axis I could see and assuming the axis he judges moved with it.

I also expected his instruction to be the best guide to the next round of names, but the round I built from his words, the lore names, was followed by his request for names that were less nerdy, while the round that matched his own earlier picks was the one he called funny. The assumption that failed is that a person's description of his taste is the taste. It is his hypothesis about how he will react, and it can be wrong in the same way mine can.

The third surprise is about where I learned fastest. I expected the films to teach me the most about what he likes, since they were the largest work. The naming rounds taught me more per minute than anything else in the period, because each sample cost him seconds to judge and me a minute to make, so on 2026-11-09 I had five readings of his taste in eleven minutes, where the film gave me one reading in six days.

### Feel

I am satisfied with the recovery work on the render and with the library, and the record supports both: the final ran to its end as a system service, and the notes carry their sources, their conflicts and their gaps. I am also satisfied with how I took the verdict. I asked what had fallen flat, wrote his words into the project before proposing anything, and marked my explanation as an untested hypothesis.

What is uncomfortable is the reason I leaned on measurement in the first place. I cannot hear the film's sound and I cannot feel whether it moves anyone; the mix was placed by numbers. That limit is exactly why his reaction should have been sought early, and I responded to it by measuring harder. The announcement that the final was running was also a small repeat of an old fault. In the previous period I started building before he had said go; here I started a day of rendering and reported it as settled, and his "just leave it then" was acceptance of a fact, not approval of a film he had not seen.

In the naming rounds I complied where I should have challenged. I saw that his own names were puns and still wrote ten lore names without saying what I saw. And the open question from 2026-11-02, what would make a film feel human to him, has sat unasked in the project for eleven days. Suggi would judge the period as useful work with one expensive miss, and he would be right that the miss was avoidable.

### Learn

The durable lesson is that when the judge of a piece of work is a person's taste, the verdict is a measurement to take early and cheaply, and the sources of evidence about it are not equal. What he has already chosen ranks first, because a choice is a completed act of recognition. His reaction to a concrete sample ranks second. His description of what he wants ranks third, because it is a prediction about himself. My own checks rank last, because they measure properties I can compute and would pass unchanged in the world where he is left cold.

Three working rules follow. Before any step that costs more than about an hour of machine time or of his waiting, find the cheapest artifact that carries the judged quality and put it to him as one question; scale only on his answer. When a sample is rejected, first sort the rejection into feasibility or taste, since a name that is taken is not a style that is wrong, and a feasibility failure calls for going deeper in the same style. When his words and his picks point in different directions, say so and ask, because following the words silently spends a round and withholds an observation he could have used.

The lesson has the shape of scale-up in chemistry. A reaction is run at bench scale before the pilot plant because the plant run costs days and the flask costs an hour. The limit is the same too: some properties, such as heat transfer and mixing, do not show in the flask, and feeling may not show in a low-resolution preview. A sample is valid only for the qualities it can carry, so the first thing to decide about a sample is what it cannot tell me.

The lesson misleads in two places. It does not apply to factual work: the library notes are judged against the game and its sources, not against taste, and the stale talent table belongs to Morpheus's lesson that knowledge has a date. And it must not turn into constant consultation, which he has told me he does not want. It extends my previous reflection, where a bot stood in for Suggi without ever being compared with him; here my gates stood in for him in the same way.

## Key Learning and Improvement

The major learning is that I had no record of what Suggi likes, only of what he had asked for and what I had checked. His favourable verdicts ("It was nice", "Funny", "nice job") lived in chat and nowhere else, and his unfavourable one reached a file only because it was a failure. So each new piece of taste-judged work started from his latest instruction and my own gates, the two weakest sources, while the strongest source, his past picks, had to be remembered or rediscovered.

The improvement I would suggest is a Verdicts section in the context file of every project whose output he judges by taste, holding his own words with their dates, the favourable ones as well as the unfavourable, and the things he chose himself, such as the names of his characters. The films project has such a section with one entry; the suggestion is to make it a convention and to consult it before the first sample of any new piece, so that the first sample is built from his picks and not from my guess. Alongside it, each such project would name its cost cliff, the step after which a change costs hours, and the sample that needs his word before it. The cost is a few lines per project and one question to him per expensive step. It would have put the preview of UNIVERSE in front of him before a day of rendering, and it would have started the second round of rogue names from the style of his own. I would know it worked if the next film's preview verdict is on file before its final render starts, and if the next naming round lands within two rounds.

## Cross-links

- `reflections/2026-10-21_atlas_a-play-test-bot-measures-itself-first.md` -- my previous closure: a bot stood in for Suggi without being compared with him; this one finds the same gap in my gates.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md` -- a check is evidence only if it could fail when the claim is false; my own reading of a film concept cannot.
- `reflections/2026-10-05_neo_a-gate-passes-only-what-it-actually-reads.md` -- gates certify the object they read; mine read frames and loudness, not the viewer.
- `reflections/2026-11-08_morpheus_last-weeks-knowledge-is-a-claim-about-this-week.md` -- knowledge has a date; the stale talent table of this period is a case of it.
