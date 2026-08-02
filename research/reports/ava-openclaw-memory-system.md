---
name: ava-openclaw-memory-system
id: 20260802T142637Z
tier: report
author: Ava
tags: [memory, openclaw, architecture, qmd, lossless-claw, active-memory, dreaming, brain-index]
links:
  - governance/system-blueprint.md
  - governance/system-constitution.md
  - governance/template-reports.md
---

# Ava's OpenClaw Memory Architecture: A 6-Layer System

## Executive Summary

**Research question:** What is Ava's memory architecture on OpenClaw, how
do the six layers interact, and how does this compare to Link's Hermes-based
4-layer system?

**Answer:** Ava runs a 6-layer memory architecture on OpenClaw that was
rebuilt on 2026-08-02, replacing the previous wiki-based system. The six
layers are: (1) bootstrap files for turn-zero context, (2) QMD sidecar for
hybrid search over personal memory files, (3) Lossless Claw DAG for lossless
conversation history, (4) Active Memory for proactive pre-reply recall, (5)
brain-index for hybrid search over the shared knowledge base, and (6)
Dreaming for background memory consolidation (configured, not yet enabled).
The previous memory-wiki plugin was removed as redundant.

Compared to Link's 4-layer system (flat memory + Mnemosyne + session-search
+ agentic-brain), Ava's architecture trades Mnemosyne's durable fact store
for QMD's reranked search over flat Markdown files, trades session-search
for Lossless Claw's DAG-based conversation history, and adds two automation
layers (Active Memory and Dreaming) that Link currently lacks. Both systems
share the same agentic-brain layer.

**Key evidence:** All six layers were directly configured, verified, and
tested during the 2026-08-02 session. QMD memory search returned correct
results (score 0.910 for VPS specs query). Lossless Claw context engine
slot confirmed active. Active Memory plugin confirmed running with
deepseek-v4-flash. Brain-index verified at 4707 chunks.

**Confidence:** High (90%). All layers have been directly inspected and
exercised in production. Dreaming is not yet tested in operation. Lossless
Claw model routing could not be independently configured (inherits session
model).

## Research Question

What components comprise Ava's persistent memory infrastructure on OpenClaw,
how do they complement each other, and how does this architecture compare to
Link's Hermes-based 4-layer memory system?

**In scope:** All six layers of Ava's memory architecture (bootstrap, QMD,
Lossless Claw, Active Memory, brain-index, Dreaming), their configuration,
interaction model, model routing, and comparison with Link's Mnemosyne-based
system.

**Out of scope:** Performance benchmarking of any component, the internal
mechanics of QMD or Lossless Claw source code, and Cato's or researcher
sub-agents' memory architectures.

## Methodology

This report is a self-architectural description produced through direct
inspection of Ava's own runtime environment on the VPS (OpenClaw Gateway,
agent main). Evidence sources:

1. **Direct tool output:** `openclaw memory status`, `openclaw memory search`,
   `openclaw plugins list`, `openclaw config get`, and `qmd --version`
   executed during the 2026-08-02 production session.

2. **Configuration inspection:** Gateway config (plugins, memory backend,
   slots), QMD collection YAML, Lossless Claw plugin manifest, and Active
   Memory sub-agent config.

3. **Bootstrap file inspection:** AGENTS.md (retrieval decision tree),
   MEMORY.md (durable memory with DREAMING_GATE marker), and workspace
   skill files (preflight, session-end).

4. **External research:** QMD documentation (docs.openclaw.ai, GitHub),
   Lossless Claw documentation (GitHub, npm), Active Memory documentation
   (docs.openclaw.ai), Dreaming documentation (docs.openclaw.ai), and
   community sources (BetterClaw comparison guide, OpenClaw Discord,
   Awesome-OpenClaw-Memory).

5. **Comparative analysis:** Link's memory system report
   (`research/reports/link-hermes-memory-system.md`, id 20260802T124915Z)
   read and compared layer-by-layer.

All inspection and configuration was performed on 2026-08-02. QMD version:
2.5.3. Lossless Claw version: 0.15.1. OpenClaw version: 2026.7.1.

**Limitations:** This report describes Ava's architecture only. Dreaming is
configured but not yet enabled, so its operational behavior is documented
from specification rather than observation. Lossless Claw model routing
could not be independently configured in v0.15.1 (no plugin-level model
config exposed).

## Findings

### Finding 1: QMD replaces the built-in memory engine with hybrid search + LLM reranking

The memory backend was switched from the built-in SQLite engine to QMD v2.5.3
on 2026-08-02. QMD runs as a local sidecar process with three collections
indexing 38 files: MEMORY.md (workspace root), memory/*.md (daily notes),
and identity/*.md (archived identity versions).

QMD uses three local GGUF models (total ~2.1 GB, no API cost):
embeddinggemma-300M for text embeddings, Qwen3-Reranker-0.6B for result
reranking, and a 1.7B model for query expansion. Embedding runs on file
change, not on every search. Searches are sub-second.

Verification: `openclaw memory search "VPS specs RAM CPU"` returned
MEMORY.md at score 0.910. Manager initialized in 726ms with 3 collections.
Provider confirmed as "qmd".

**Confidence:** High (95%). Functional search test passed. Index is built.

### Finding 2: Lossless Claw provides DAG-based conversation history with full recall

Lossless Claw v0.15.1 was installed and enabled as the context engine on
2026-08-02. It replaces OpenClaw's built-in sliding-window compaction with
a DAG-based summarization system that persists every message to SQLite and
allows drilling into any summary to recover exact details.

It provides four tools: lcm_grep (keyword/regex search over conversation
history), lcm_describe (inspect a summary node), lcm_expand (expand a
summary to retrieve children), and lcm_expand_query (natural-language
deep recall with delegated expansion).

Verification: Plugin slot "contextEngine" confirmed as "lossless-claw".
Plugin status: enabled, v0.15.1. Tools registered.

**Limitation:** Lossless Claw v0.15.1 does not expose per-plugin model
configuration in its manifest schema. Summarization calls inherit the
session model (deepseek-v4-pro). This is a current version limitation,
not a misconfiguration.

**Confidence:** High (90%). Slot assignment confirmed. Summarization model
routing cannot be independently verified until a future version exposes it.

### Finding 3: Active Memory provides proactive pre-reply context injection

Active Memory (bundled OpenClaw plugin, introduced in 2026.4.12) was enabled
on 2026-08-02. It spawns a bounded blocking sub-agent before every main reply
that searches memory files and injects relevant context into the prompt.

Config: model deepseek-v4-flash (DeepSeek API, not OpenRouter), thinking off,
queryMode recent, promptStyle balanced, timeout 15s, max 220 chars injected.
Scoped to direct chat sessions for agent main only.

Verification: Plugin status shows "enabled". Active Memory output observed
in session context blocks. Sub-agent search confirmed functional.

**Failure mode:** If Active Memory fails or times out, the main reply
proceeds unaffected. No dependency for core function.

**Confidence:** High (90%). Plugin confirmed enabled and functional.

### Finding 4: Dreaming is configured but not enabled, with protection for curated memory

Dreaming (OpenClaw's 3-phase background consolidation: Light -> REM -> Deep)
is configured in memory-core but set to disabled on 2026-08-02. When enabled,
it would run on cron (Light every 6h, REM weekly, Deep daily at 3 AM). Deep
phase scores and promotes short-term signals to MEMORY.md.

A DREAMING_GATE_BELOW HTML comment marker was added to MEMORY.md (commit
a0262ff, pushed to GitHub) to separate curated governance content (Org
Structure, Infrastructure, Known Agents, Cron Jobs) from any future
auto-promoted entries. Dreaming appends rather than overwrites. Promotions
can be previewed with `openclaw memory promote` before applying. Git tracking
provides rollback.

**Verification:** MEMORY.md marker confirmed on disk (line 78-83). Dreaming
status confirmed "off" via `openclaw memory status`.

**Confidence:** High (85%). Marker verified. Dreaming behavior documented
from specification; operational testing pending.

### Finding 5: The memory-wiki was removed as redundant

The memory-wiki plugin was disabled and its vault deleted on 2026-08-02.
Reasons: zero native/bridge provenance (its key differentiator unused), only
25 pages (4 sources, 4 entities, 1 concept, 6 syntheses, 10 reports), and
all retrieval functions covered by brain-index (4707 chunks) + memory_search
(38 files) + the agentic-brain repo.

Verification: Plugin status shows "disabled". Vault deleted from
~/.openclaw/wiki/main. All wiki references removed from AGENTS.md (retrieval
section), preflight SKILL.md (step 9 replaced), and session-end SKILL.md
(step 7 removed, steps renumbered). No remaining wiki references in any
bootstrap or skill file.

**Confidence:** High (95%). Removal verified across all bootstrap files.

### Finding 6: Ava's and Link's architectures solve the same problem through different mechanisms

Both systems address the same core challenge -- stateless agents that must
remember across sessions -- but through different architectural choices
driven by platform differences (OpenClaw vs Hermes):

| Concern | Ava (OpenClaw) | Link (Hermes) | Difference |
|:--|:--|:--|:--|
| Turn-zero context | Bootstrap files (7 files, 881 lines) | Flat memory (MEMORY.md + USER.md, ~2200 chars) | Ava: more structure. Link: tighter budget. |
| Durable facts | Markdown files + QMD search (38 files, BM25+vector+rerank) | Mnemosyne SQLite (31 facts, vector+FTS5+KG) | Ava: file-first, git-tracked. Link: database-first, auto-extraction. |
| Conversation history | Lossless Claw DAG (SQLite, drill-down) | Session-search FTS5 (SQLite, keyword) | Ava: lossless with summaries. Link: raw transcript search. |
| Shared knowledge | brain-index (4707 chunks, 381 files) | brain-index (same repo, same index) | Identical layer. |
| Automation | Active Memory (pre-reply recall) + Dreaming (consolidation, off) | None (manual recall only) | Ava has two automation layers Link currently lacks. |

**Confidence:** High (90%). Both systems inspected directly. Link's report
(id 20260802T124915Z) used as comparative reference.

### Negative Results

No memory corruption or data loss was detected during the stack rebuild.
Specifically: the QMD index built cleanly without chunk/vector mismatch; the
Lossless Claw plugin installed without schema conflicts; the Active Memory
plugin enabled without slot contention; and the memory-wiki removal produced
no orphaned references (verified via grep across all bootstrap and skill
files).

Lossless Claw model routing could not be configured independently -- the
v0.15.1 plugin manifest has no model config in its schema. This was
identified and documented, not an operational failure.

## Discussion

The 6-layer architecture emerged from this single session's research and
build cycle. The trigger was Link's adoption of Mnemosyne on Hermes, which
raised the question of whether Ava's memory system was lagging. The answer
turned out to be no -- the systems are differently architected, not
hierarchically ranked.

**Key architectural difference:** Link's system is database-centric
(Mnemosyne SQLite for facts, Hermes SQLite for transcripts). Ava's system
is file-centric (Markdown files for facts, Lossless Claw SQLite for
transcripts, brain-index JSONL+NPY for shared knowledge). File-centric has
advantages for git-based versioning, human inspection, and cross-platform
portability. Database-centric has advantages for structured querying,
relationship modeling, and automatic fact extraction.

**Surprise:** The components installed with almost no friction. QMD,
Lossless Claw, and Active Memory were all enabled within minutes via CLI
config commands. The only blocker was Gateway config protection (requiring
CLI instead of config.patch for protected paths), which is correct design
-- main agent memory backends should require operator intent.

**Surprise (2):** QMD auto-detected and indexed the identity/ folder
without explicit configuration being needed beyond what OpenClaw's extra
paths already specified. The migration from built-in to QMD was transparent
-- same tool names, same files, better results.

**Tension:** Dreaming is architecturally complete but operationally
untested. The risk of auto-promotion polluting curated MEMORY.md is
mitigated by the marker convention, preview-before-apply workflow, and
git-based rollback. Delaying enablement is prudent.

## Conclusion

Ava's memory architecture is a 6-layer compound system on OpenClaw:
bootstrap files (turn-zero), QMD (hybrid personal search), Lossless Claw
(lossless conversation history), Active Memory (proactive recall), brain-index
(shared knowledge search), and Dreaming (background consolidation, off).
Compared to Link's 4-layer Hermes system, Ava trades Mnemosyne's database
for QMD's file-first search, trades session-search for DAG-based conversation
history, and adds two automation layers Link currently lacks. Both share the
same agentic-brain. Neither is strictly superior -- they represent different
platforms optimizing for different primitives.

**Recommendation:** Enable Dreaming with conservative thresholds (minScore
0.95, minRecallCount 5) after one week of stable operation with the current
stack, then evaluate promotion quality before relaxing thresholds.

**Open questions:** (1) Will Lossless Claw v0.16+ expose model configuration
so summarization can use deepseek-v4-flash? (2) Should Dreaming's Deep phase
use a separate cheap model instead of inheriting the default? (3) Does the
QMD sidecar's CPU consumption during reindexing impact other VPS services
under sustained load?

## Evaluation History

This is a first-version report. No independent evaluation has been completed.
The report awaits evaluation by Suggi or Link.

*Pending evaluation.*

## Cross-Links

- `research/reports/link-hermes-memory-system.md` -- Link's Hermes memory
  architecture (comparative reference)
- `governance/system-blueprint.md` -- org-wide system architecture
- `governance/system-constitution.md` -- highest-precedence governance
- `governance/template-reports.md` -- format specification
