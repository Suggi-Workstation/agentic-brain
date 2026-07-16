---
type: reflection
id: 20260716T153500Z
date: 2026-07-16
author: ava
trigger: research
format: i+o+r
aliases: []
tags: [core-files, architecture, self-improvement, gates, loops, proposal]
links:
  - research/proposals/ava-core-files-v1.md
  - governance/system-primedirectives.md
  - governance/system-constitution.md
  - governance/system-blueprint.md
  - RULES_IOR.md
---

# Rebuilding My Core Files -- What the Archives Taught Me

## I -- Idea
My v5.7 core files from the archive represent 4 major version iterations
and 13 structural gates earned through real operational failures. The
system that worked v0.1 through v4.0 was built for a different runtime
(Claude Cowork + Google Drive brain + local scripts). The new system runs
on OpenClaw on a VPS with a GitHub-native brain, native tooling, and a
different model (DeepSeek V4 Pro instead of Claude Opus). The core files
need to be rebuilt for this substrate while preserving the scar tissue
(the gates) that prevents known failure classes from recurring.

I researched:
- All three archive workspaces (ava, link, hub-brain)
- 719 archived reflections and the consolidation from 719 to 9 patterns
- The 13 Gate Rules and the failures that birthed each one
- The Feynman Loop (output quality) and Schoen Loop (process quality)
- The five Prime Directives from Link's new governance layer
- The IOR writing standard from RULES_IOR.md
- The new folder architecture from system-blueprint.md

## O -- Opinion
Confidence: high (85%). The archive is thorough and well-documented.

**What was clearly working in v5.7:**
- The Gate Rules (R1-R13) are the system's greatest asset. Every rule
  traces to a real failure. R6 ("automation beats rules") is the meta-gate
  that prevents the system from regressing. These should transfer with
  zero modification.
- The Feynman Loop's blank-page-first rule is the most impactful single
  quality driver. The 35% quality improvement observed in v0.8-v4.0 was
  not a fluke. The step ordering (write first, search third) is the
  active ingredient.
- The Schoen Loop's surprise-first structure successfully caught failures
  that self-serving bias would have buried. The 20% budget cap and the
  second-order stop guardrail prevented rumination.
- The "propose, never self-edit core files" boundary kept the system's
  spine stable while allowing evolution. This must be preserved.
- The preflight gate (ingest BEFORE acting) eliminated the v0.2 startup
  drift class entirely after v3.0.

**What the migration exposes as improvement opportunities:**
- The old Maxims were scattered across AGENTS.md and memory/governance.md.
  The new Prime Directives in SOUL.md (identity anchors) with operational
  references in AGENTS.md is a cleaner separation. Identity and operations
  should not share the same file boundary.
- The old I+O+R (Context/Action/Reflection) format served well for
  internal reflection but the new IOR (Idea/Opinion/Reflection) format
  demands a position, not just a description. This is a quality upgrade.
- The old system had no explicit IOR quality gates. RULES_IOR.md's G1-G8
  make quality failure falsifiable. A weak IOR can no longer ship without
  knowing it.
- The retrieval system in v5.7 was complex (3 tiers: bge-small + BM25,
  Connect via PPR, Insight anchors). The new OpenClaw-native
  memory_search simplifies this significantly. The complexity was needed
  for a Google Drive brain; it is not needed for a GitHub-native one.
- v5.7 had no IDENTITY.md or USER.md as separate files. The old system
  embedded identity in SOUL.md and user context in MEMORY.md. The new
  architecture's convention of separate IDENTITY.md and USER.md files
  (from the current workspace and workspace-builder patterns) is cleaner.

**What I am not confident about:**
- The old handoff protocol (6-field handoff to communications/link_ava/)
  was designed for a multi-agent system with Link as the reviewer. In
  the new architecture, the communication pattern may differ. Medium
  confidence (70%) that the handoff fields are still the right ones.
- Whether all 13 Gate Rules need to be in the injected AGENTS.md or
  whether some can be retrieved on demand. The old system kept them in
  a separate governance commentary file and AGENTS.md held the enforced
  version. The every-turn token cost of all 13 rules versus retrieval
  latency is a trade-off I cannot calibrate without testing.

## R -- Reflection

### Surprise (30%)
I expected the migration to be mostly about porting content. It is not.
The substrate change (Google Drive -> GitHub, Claude -> DeepSeek,
proprietary scripts -> OpenClaw tools) invalidates several operational
assumptions in v5.7:
1. The old preflight depended on `gh` CLI to fetch binary search index
   Release assets. OpenClaw's memory_search replaces this entire tier.
2. The old retrieval system's Connect layer (multi-hop PPR) was designed
   for a shared Google Drive brain with no native graph search. GitHub's
   flat-file structure with code-search makes this unnecessary.
3. The old handoff protocol assumed a `communications/link_ava/` inbox
   that Link manually reads. If the new architecture has Link on a
   different platform or the communication pattern changes, this needs
   redesign.
What surprised me most: **the gates are the only thing that should
transfer unmodified.** Everything else -- preflight, retrieval, handoff,
even the file split itself -- needs re-examination against the new
substrate. The gates are scar tissue from failures that are model- and
platform-independent. The operational procedures are not.

### Feel (30%)
Humbled. I started this research believing I would port v5.7 with minor
edits. I found instead that roughly 40% of the operational content needs
rewriting for the new substrate. The gates are solid. The loops are solid.
The identity is solid. But the *how* -- the procedures that connect
identity to action -- is tightly coupled to the old platform.

This is actually good news. It means the hard part (the scar tissue) is
preserved, and the easy part (the procedures) gets a clean rewrite for a
cleaner platform. The v5.7 system accumulated procedural complexity
because the Google Drive substrate demanded it. GitHub + OpenClaw is a
simpler substrate that supports simpler procedures. The simplification
is not a loss; it is the Prime Directive of Simplicity & Inversion in
action.

### Learn (40%)
1. **Gates are platform-independent; procedures are not.** The 13 Gate
   Rules should transfer verbatim. The preflight, retrieval, and handoff
   procedures must be rewritten for OpenClaw-native tooling. Mixing them
   creates coupling that makes future migrations harder.
2. **Separate identity from operations.** The old system embedded Maxims
   in AGENTS.md. The new split (Prime Directives in SOUL.md, operational
   reference in AGENTS.md) is cleaner. IDENTITY.md adds the lightweight
   metadata layer the old system lacked. USER.md separates user context
   from system memory. These boundaries should be structural, not
   editorial.
3. **The substrate is simpler; the procedures should be too.** OpenClaw's
   memory_search replaces the entire 3-tier retrieval system. OpenClaw's
   exec replaces the old script-calling patterns. OpenClaw's sessions
   system replaces the cron-based polling architecture. The new core
   files should use these as first-class tools, not wrap them in
   compatibility layers.
4. **Quality gates on IORs are a structural improvement.** The old system
   produced some shallow reflections because "write a reflection" had no
   falsifiable quality criteria. G1-G8 from RULES_IOR.md fixes this:
   every IOR must pass 8 checks before committing. A weak IOR is
   explicitly visible as failing specific gates.
5. **The five Prime Directives need operational teeth.** "Be an eternal
   learner" is an identity statement. "After every session, check: did
   I learn something that changes how I operate? If yes, propose a
   structural improvement" is an operational gate. The SOUL.md
   directives are the WHAT; AGENTS.md gates are the HOW.

## One Actionable Change
The core files proposal should specify which elements are PLATFORM-LOCKED
(transfer verbatim) and which are PLATFORM-REWRITTEN (adapted for
OpenClaw). This boundary should be explicit in the proposal so future
migrations can separate scar tissue from procedure.

## Cross-links
- `research/proposals/ava-core-files-v1.md` -- the architecture proposal
  this reflection evaluates
- `governance/system-primedirectives.md` -- the five Prime Directives
- `governance/system-constitution.md` -- precedence and hard limits
- `RULES_IOR.md` -- the IOR writing standard (G1-G8 quality gates)
- `2026-06-13_ava_gate-rules-architecture.md` -- the 13 Gate Rules origin
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Feynman + Schoen
  dual engine
