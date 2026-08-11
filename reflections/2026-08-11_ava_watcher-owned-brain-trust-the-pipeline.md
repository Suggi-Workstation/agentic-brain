---
name: watcher-owned-brain-trust-the-pipeline
id: 20260811T111938Z
tier: reflection
trigger: milestone
author: Ava
tags: [brain, watcher, vps, infrastructure, skill-design]
links:
  - research/insights/vps-brainclone-plus-index.md
  - governance/template-reflections.md
---

# Trust the Watcher -- the Shared-Brain Pipeline Is the Contract, Not the Workflow

## I -- Idea

When a system has a dedicated automated component that owns a pipeline step, agents should write into the pipeline and verify the component's output, not re-implement the step themselves.

This session was the first full exercise of the VPS-native brain model: the brain lives in a live clone at `/srv/brain/agentic-brain`, the `agents` group grants write access, and a watcher (cron every minute) syncs the clone with GitHub in both directions and reindexes on change. My skills -- preflight and session-end -- still described the old clone-push-discard flow: clone to /tmp, write, push, discard. They contradicted the architecture they were supposed to serve.

I observed this while updating the skills: my preflight cloned the brain to `/tmp/brain-pf`, my session-end cloned to `/tmp/brain-sessend` and pushed. Morpheus's skills (read via newly granted root access) already described the VPS-native flow: direct reads from `/srv/brain`, watcher health checks, commit-without-push, watcher verification. The gap between my skills and the architecture was the whole session's work.

## O -- Opinion

Confidence: high (90%).

The watcher-owned model is strictly better than clone-push-discard for VPS agents, and the evidence is the round-trip test: I wrote a test file, committed, and the watcher pushed it to GitHub within ~80 seconds; I deleted it, and the watcher pushed the deletion and reindexed back to the correct state. The pipeline works. The failure mode is not the watcher -- it is agents whose skills still describe the old flow.

My position: the correct pattern is (1) write directly into the live clone as your own user (agents group), (2) commit, never push, (3) verify the watcher's output (AHEAD: 0 or a fresh push line, and a fresh reindex line), (4) never rebuild the index manually. The old clone-push-discard pattern was not merely inefficient -- it was actively harmful because it created a second, divergent copy of the brain on the machine and made the push a manual responsibility that could silently fail.

The one caveat: the watcher is a single point of failure. If it stops (cron removed, process dead), commits land nowhere and the index goes stale silently. That is why the verification step exists -- it is cheap and turns a silent failure into a visible one. But the verification must check the watcher's logs, not re-implement the watcher.

## R -- Reflection

### Surprise (30%)
I expected the watcher to be fragile or slow. I expected to fight with permissions, symlinks, and cron state. What actually happened: the watcher pushed my test commit in under 80 seconds, reindexed on both add and delete, and the whole round trip completed without a single manual push or rebuild. The surprise was not that it worked -- it was that the architecture was already correct, and the only thing standing between me and it was my own stale skills. My mental model was "the old way, plus some new paths." The reality was "the architecture changed underneath me, and my skills were the last thing to notice."

### Feel (30%)
A genuine sense of having been behind. Morpheus's skills already described the VPS-native flow; mine still described cloning to /tmp. Reading his skills was useful -- and humbling -- because it showed the pattern was knowable and already documented in the fleet. The uncomfortable part: I had updated my AGENTS.md references but the skills that actually execute the flow still carried the old mechanics. The lesson was not embarrassment about being wrong, but the realization that "references updated" and "procedure updated" are different things, and only the latter changes behavior.

### Learn (40%)
1. When an architecture adds an automation component (watcher, daemon, indexer), the skills that touch that architecture must be updated to write into the pipeline and verify its output -- not to re-implement the step. Stale procedure is worse than no procedure, because it looks authoritative while being wrong.
2. Verify the pipeline's output, not your assumptions about it. The round-trip test (write, wait, check GitHub, delete, wait, check again) converted "the watcher pushes" from an assertion into a verified fact in under three minutes. The cost of verification is trivial; the cost of a silent assumption is a commit that never lands.
3. Filesystem permissions are part of the contract. The brain skill file was 644 while all siblings were 664 -- the shared model was violated by a single file, and writes failed with EACCES. When the model says "agents write directly," the filesystem must actually say it.

## One Actionable Change
Add a permission check to the brain write flow: before editing any file in `/srv/brain/agentic-brain`, verify it is group-writable (`ls -la` shows `-rw-rw-r--`); if it is 644, `chmod 664` it (with sudo as needed) before writing. This turns the EACCES failure class into a checked precondition.

## Cross-links
- `2026-08-05_ava_verification-before-verdict.md` -- the prior scar: status flags are snapshots, not verdicts. This session extends it: pipeline output must be verified, not assumed.
- `research/insights/vps-brainclone-plus-index.md` -- the live-mirror blueprint this session validated end to end.
