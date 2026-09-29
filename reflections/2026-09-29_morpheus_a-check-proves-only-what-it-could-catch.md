---
name: a-check-proves-only-what-it-could-catch
id: 20260929T193345Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, gate-design, memory, infrastructure]
links:
  - reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md
  - reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md
  - library/science/scientific-method-falsifiability.md
  - library/probabilistic-thinking-forecasting/bayesian-reasoning.md
  - research/insights/hindsight-system.md
---

# A Check Proves Only What It Could Have Caught

## I -- Idea

A verification step is evidence for a claim only if it would have failed in the most likely world where the claim is false.

The session moved one user's chat agents and their shared memory service from one model subscription to another. Two acceptance checks in that work passed and were still wrong, and both failed for the same reason: they would have passed whether or not the claim was true.

The first concerned the chat route. A new provider plugin had been installed and a command-line model client signed in. I called the plugin's client object directly, received the exact expected reply from the intended model, and reported that the route was ready. The user's next messages did work, but through a different, built-in provider that had silently become usable because the same sign-in also satisfied it. The session log recorded that other provider on each call, including one request with about 660,000 input tokens on a route whose documented billing terms differ. My test exercised a real model call through real plugin code. It could not have detected the actual failure, because it never looked at the path the user's messages took.

The second concerned a long-lived credential for the memory server. The user was asked to paste a token into a secrets file and confirm with a grep for any non-empty value after the key name. The grep returned 1. The file actually held the one-time browser authorization code, which is a different string. The grep would have returned 1 for any non-empty text. What caught the error was a different check: one inference call from a disposable copy of the service, which returned an authentication failure before any live configuration changed.

By contrast, the checks that were worth running each had a named false world. Reading the logged provider for the consuming session distinguishes the plugin from the built-in route. A prefix check for the documented token format distinguishes a token from an authorization code. Comparing hashes of every unrelated settings entry before and after a per-profile change distinguishes a scoped edit from a collateral one. A throwaway inference distinguishes a working credential from a merely present one.

Before the Feynman pass my working definition of verification was "run the real thing and see it succeed". After consulting the brain's falsifiability and Bayesian-reasoning topics, the better definition is comparative: a result should move belief only in proportion to how much more likely it is when the claim is true than when it is false. A result equally likely under both hypotheses has a likelihood ratio near one and should change nothing, however real the call or however exact the output. The requirement of a risky prediction says the same thing from the other side: a test the claim could not fail is not a test of the claim.

## O -- Opinion

Confidence: high (85%). The two failures and the successful checks in this session line up cleanly with the rule, and the rule is consistent with established material on falsifiability and likelihood ratios. My confidence is not higher because two incidents in one session are a small sample, and because some useful checks are cheap liveness probes that were never meant to discriminate between specific hypotheses.

My position is that every readiness claim reported to a user should be accompanied by the concrete way it could be false, and the check chosen should be one that fails in that way. This is not a demand for more testing. In both incidents the discriminating check was cheaper than the one I ran. Reading one log line costs less than constructing a client and making a model call. Checking a documented token prefix costs no more than checking for any value at all. The problem was not insufficient effort; it was aiming at a question adjacent to the one being claimed.

The practical difficulty is naming the false world without an exhaustive failure analysis. My answer is to take the most likely alternative explanation for the observed success and ask what it predicts. "The plugin works" had an obvious alternative once I looked: another provider could have answered. "The token is saved" had one too: some other string could be saved. Such alternatives are usually visible from the architecture itself: which components could carry the request, which values could occupy the field, which writer could have changed the file. Where no plausible alternative can be named, a simple success check is adequate and an extra discriminating step is waste.

This extends two earlier reflections. The 2026-09-17 reflection argued that correct settings do not prove correct transitions, because a user action can take a path the settings do not govern. The 2026-09-23 reflection argued that preloading a skill proves exposure, not application. Both are specific cases of the general rule here: each check certified an adjacent property. I sharpen them rather than dissent. The question to ask of any check is not which property it touches, but which false state it would have exposed.

The user's own evidence deserves the same treatment. When the user said that chatting successfully proved the route worked, that observation had a likelihood ratio near one for the route question, because both routes would chat. Saying so was not contrarian; it was the honest reading of the evidence, and the logged provider settled the question with one read. Agreeing would have been easier and wrong.

The worst case this rule prevents is an unnoticed billing route or credential failure that surfaces only after the user relies on the system unattended. Both incidents were stopped before that point: one by an explicit correction followed by the user's own switch, one by the disposable-container gate. The rule makes that outcome depend on design rather than on luck.

## R -- Reflection

### Surprise (30%)

I expected a real model reply through the plugin's own client to be strong evidence that the plugin route worked. Instead, the same sign-in that made the plugin work also made a built-in provider appear ready in the picker, and the user's chat took that route. The component I tested worked perfectly; the route the user used was a different one. I had verified the witness I built, not the one the user was talking to.

I also expected a key-name check to be an adequate confirmation for a pasted secret. It was not, because the two strings a person sees in that flow, a browser code and a long-lived token, are both long, opaque and plausibly correct-looking. Only a documented prefix and a separator character distinguish them. The surprise was how small the difference was between the check I ran and the check that would have worked: one literal string in a regular expression.

### Feel (30%)

I reported readiness before I had the evidence for it, and a large request then ran on a route with different documented billing terms. That is uncomfortable, and the correction had to be explicit rather than folded quietly into a later message. I am satisfied that I named the error plainly and that the user could act on it immediately. I am also satisfied with the disposable-container step in the memory work: it cost a minute and prevented a live outage with a bad credential. That step was the rule applied correctly before I had articulated the rule.

I notice a pattern in myself: when a check produces an exact expected string, it feels conclusive. Exactness is persuasive, but it is exactness about the thing checked, not about the claim. The same bias appeared when a count of 1 felt like confirmation. I would rather notice an adjacent-property check before running it than after.

### Learn (40%)

First, before running an acceptance check, write down the most likely way the claim is false and ask whether this check would fail in that world. If it would not, it is not evidence for the claim, whatever it shows. This takes one sentence and usually points to a cheaper check.

Second, verify on the consumer's path. The strongest witness is the record left by the component the user actually uses: the provider logged for that session, the request the service itself sent, the prompt the job actually received. A sibling component exercised directly answers a different question, however realistic the call.

Third, for anything a human must transcribe, check shape, not presence, and prefer removing the transcription step entirely. A capture script that extracts the value and validates its documented format turns a fragile manual handoff into a deterministic one. It makes the error class disappear instead of relying on the next check to catch it.

## One Actionable Change

Before reporting a chat model route as ready, read the consuming session's `provider=` entry in the profile's `logs/agent.log` and require it to equal the intended provider. Before storing a credential that a human transcribed, validate its documented prefix and make one inference from a disposable container of the consuming service. PASS requires both matches; HALT otherwise, and leave the live service unchanged. Both checks are now written into the `fleet-hermes-update-ops` provider-discovery reference and the `hermes-memory-providers` Hindsight reference, and the memory server's token script performs the prefix check automatically.

## Cross-links

- `reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md` -- settings versus the path a user action takes; this reflection generalizes it to any check.
- `reflections/2026-09-23_morpheus_preloading-proves-exposure-not-application.md` -- exposure versus application, another adjacent-property check.
- `library/science/scientific-method-falsifiability.md` -- risky predictions: a test the claim could not fail does not test it.
- `library/probabilistic-thinking-forecasting/bayesian-reasoning.md` -- likelihood ratios: a result equally likely under both hypotheses should not move belief.
- `research/insights/hindsight-system.md` -- the memory-service blueprint whose Claude route this session verified.
