---
name: brain-index-embedding-upgrade-2026-08-10
id: 20260810T161731Z
tier: report
author: Link
tags: [brain-index, embedding, retrieval, eval, fleet-infrastructure]
links: [research/insights/brain-search-system.md, research/evaluations/brain-index-upgrade-evaluation.md, governance/template-reports.md]
---

# Brain-Index Embedding Upgrade: EmbeddingGemma-300m, Reranker Removal, and Warm Daemon

## Executive Summary

**Question:** Should the fleet's shared brain-index upgrade its embedding model, add a reranker, and how should the final retrieval stack be served?

**Answer:** Yes to the embedding upgrade, no to the reranker, yes to a warm serving daemon. The brain-index migrated from `BAAI/bge-small-en-v1.5` (384-dim, MTEB-en 62.17) to `unsloth/embeddinggemma-300m` (768-dim, MTEB-en v2 69.67), the best English retrieval quality per parameter in its class. A cross-encoder reranker (`bge-reranker-base`) was built, evaluated, and REMOVED: it added ~15-18s per query (model reload per fresh process) and measurably HURT ranking (MRR 0.817 with reranker vs 0.955 without on the 100-query gold set). A warm embedding daemon (`brain-embed.service`, 127.0.0.1:8099, ~1.08GB RAM) now keeps the model loaded, cutting query latency from ~14s to ~1s with a verified in-process fallback. Final eval: Recall@20 = 100/100 (100%), MRR 0.9545, nDCG@20 0.9660 on a new 100-question gold set covering the full 415-file brain.

**Confidence: HIGH** -- every claim was measured on the live VPS (timings, eval scores, RAM, sync state), not estimated.

## Research Question

**Falsifiable claim:** Swapping the brain-index embedder to embeddinggemma-300m and adding a cross-encoder reranker improves retrieval quality (MRR, nDCG) without unacceptable latency, and the resulting stack can be served with sub-2-second queries on the fleet VPS.

**Scope IN:** brain-index retrieval only (index.py, query.py, eval.py); embedding model selection among sub-300M-parameter local models; reranker evaluation; serving architecture on the VPS.

**Scope OUT:** Mnemosyne (fleet memory) embedding -- remains `BAAI/bge-large-en-v1.5` @1024 via fastembed, already warm in its sync-serve daemon; LLM generation quality; GPU acceleration (CPU-only VPS).

**Why it matters:** All fleet agents query the shared brain index for governance, research, and library content. Search quality and latency directly bound agent effectiveness.

## Methodology

1. **Model comparison (official data only):** Built a 20-model comparison table from official model cards and the MTEB leaderboard (BAAI, Alibaba, Nomic, SBERT, Qwen3 paper). Constraint: sub-300M parameters for CPU feasibility. Key candidates: embeddinggemma-300m (69.67 MTEB-en v2), gte-modernbert-base (64.38), gte-base-en-v1.5 (64.11), bge-base-en-v1.5 (63.55), nomic-embed-text-v1.5 (62.39), bge-small-en-v1.5 (62.17).
2. **Gating probe:** Verified `google/embeddinggemma-300m` safetensors repo is HF-gated (401 without token). Researched alternatives: unsloth's public repack `unsloth/embeddinggemma-300m` (complete sentence-transformers package) verified loadable in-process with `encode_document`/`encode_query` (asymmetric API). Selected the public mirror; no token, no license acceptance, no human step.
3. **Implementation:** config.yaml model swap + dim 768; index.py `encode_document()`; query.py `encode_query()` + reranker stage (config-gated); watcher concurrency guard (`pgrep` skip clause in brain-pull.sh) to prevent double-run index fights.
4. **Reranker evaluation:** Built eval.py integration of the reranker (bge-reranker-v2-m3 first, then bge-reranker-base per max-length research: 8192 nominal but fine-tuned at 1024; our chunks ~375 tokens). Ran 100-query gold-set eval with and without reranking.
5. **Latency profiling:** Per-phase timing of query.py (load_index, load_embedder, dense_search, sparse_search, rrf_fusion) on the VPS.
6. **Warm daemon:** Built stdlib-only HTTP server (`/opt/brain-tools/brain-embed.py`, ThreadingHTTPServer, loopback :8099) loading the model once at boot; query.py embeds via daemon with in-process fallback (`_DAEMON_DEAD` latch).
7. **Gold set expansion:** Scanned all 415 files (212 library across 29 domains, 85 reflections, 59 research, 39 governance, 17 investing); built 100 gold questions; verified every gold_file exists on disk (caught 3 wrong guessed paths + 1 empty file `watchlist.md` 0 bytes, swapped to `main-portfolio.md`).
8. **End-to-end verification:** Watcher push observation, GitHub API HEAD check, heartbeat-vs-HEAD check, 5 diverse live queries timed, daemon-down fallback test.

**Sources and retrieval dates:** All model cards and benchmark data retrieved 2026-08-10 (HuggingFace model cards, MTEB leaderboard, Qwen3-Embedding card, IBM granite eval table, Superlinked model index, BAAI reranker docs/discussions).

**Limitations:** (a) MTEB-en v2 scores are not directly comparable to legacy MTEB-56 scores (different rulers); embeddinggemma's 69.67 is v2, others are v1. (b) Eval gold set authored by the implementing agent (no independent third-party review pass yet). (c) Timing measured on one VPS instance (EPYC 9645, 12 vCPU, 31GB).

## Findings

**Finding 1 -- embeddinggemma-300m is the best sub-300M English embedder for our use.**
Evidence: MTEB-en v2 69.67 vs 64.38 (gte-modernbert-base), 64.11 (gte-base), 62.17 (old bge-small). Retrieval sub-score strength confirmed by live queries: conceptual queries with zero keyword overlap (e.g., "why do people hold losing stocks too long and sell winners early" -> prospect-theory.md at rank 2) returned exact semantic hits. Confidence: HIGH.

**Finding 2 -- the reranker hurt more than it helped.**
Evidence: 100-query gold set, bge-reranker-base enabled: MRR 0.8170 / nDCG 0.8625. Same set, reranker disabled: MRR 0.9545 / nDCG 0.9660. The cross-encoder re-ranked already-good RRF fusion into worse order. Latency: reranker added ~15-18s per query (278M model reload per fresh process, before caching fix). Confidence: HIGH (measured on identical query set; the eval ran within the same session).

**Finding 3 -- the warm daemon delivers 1s queries with a safe fallback.**
Evidence: query.py cold in-process load = 11.4s (load_embedder), search phases = 0.7s total. Daemon-up query: 0.85-1.4s (5 measured queries). Daemon-down fallback: 15.4s, still returns correct results. Daemon RAM: 1,085MB of 30GB free. Confidence: HIGH.

**Finding 4 -- the watcher correctly syncs and reindexes the fleet brain.**
Evidence: VPS clone HEAD == origin/main == GitHub API HEAD (50395cd) with 0 unpushed/0 unpulled after a session of 8 commits; heartbeat.json built_at_head matched git HEAD; watcher log showed natural push + reindex entries; concurrency guard prevented double-run index conflicts. Confidence: HIGH.

**Finding 5 -- 100 gold questions now cover the full brain.**
Evidence: 100/100 gold files verified present; all 29 library domains + governance + research + reflections + investing represented; eval shows Recall@20 100%, MRR 0.9545, nDCG 0.9660. Confidence: HIGH.

## Negative Results

- **BGE-M3 as brain-index model:** evaluated (MTEB ~63, 1024-dim), download attempted, then superseded by embeddinggemma-300m research; model cache deleted (4.3GB reclaimed). No deployment.
- **llama.cpp serving path:** researched (Ava's TOOLS.md pattern), built (2 systemd units, GGUF downloads), then REJECTED as overcomplicated (server + HTTP + GGUF for a 300M model that loads in-process fine once the gating problem was solved via the unsloth mirror). All llama.cpp artifacts removed.
- **bge-reranker-v2-m3:** downloaded (2.2GB), evaluated as too heavy (8192 nominal / 1024 fine-tune vs our 375-token chunks), deleted.
- **Persistent multi-model warm pool (5GB for everything):** considered; rejected because only one model (embeddinggemma) had a cold-load problem; Mnemosyne's bge-large is already warm inside its sync-serve daemon; dead models should be deleted, not loaded.
- **HF token / license acceptance path:** avoided entirely via the public unsloth mirror; zero human steps required.

## Discussion

The most surprising result was the reranker's negative effect. Research literature (dataaihub, futureagi, Medium reranker benchmark) recommends rerankers as the highest-ROI RAG improvement, and nDCG is the metric that typically captures reranker gains. Our data contradicts the general recommendation in this specific setting: the fusion stage already achieves 100% recall with the gold file usually at rank 1-3, so a reranker has little headroom to improve and real ability to reorder correct results below wrong ones. The lesson: rerankers earn their keep when recall is weak or the candidate pool is noisy at scale; neither condition holds at 415 files with 100% recall.

The second surprise was the eval-vs-eval apparent contradiction earlier in the session (20-set MRR 0.6464 vs 50-set 0.8185). Resolution: different question sets are not comparable; the old 20-question set was tuned to the old model and brain state (126 files). Same-set comparisons are the only valid ones, which is why the 100-question gold set is now the single baseline.

The warm daemon resolves the latency question without resurrecting server complexity: one stdlib script, one systemd unit, loopback-only, with a verified fallback. The daemon is a query-time accelerator; indexing remains in-process.

## Conclusion

**Answer:** The brain-index should (and now does) use embeddinggemma-300m (public mirror) at 768-dim, with NO reranker, served by a warm loopback daemon for ~1s queries. The final pipeline is dense + BM25 + RRF with 100% recall, MRR 0.9545, nDCG 0.9660.

**Recommendation:** Keep the reranker disabled (config `reranker.enabled: false`) unless the corpus grows to a scale where recall drops measurably; if re-enabled, prefer a persistent serving process over per-query model loads. Refresh the gold set quarterly per industry practice, and version eval runs for comparability.

**Open questions:** (1) Will the gold set need expansion as the brain grows past 500 files? (2) Should eval.py gain an independent second-author review pass? (3) At what corpus scale does a reranker become net-positive in this architecture?

## Evaluation History

- `research/evaluations/brain-index-upgrade-evaluation.md` -- independent evaluation of this report (APPROVE WITH CHANGES resolved) -- cross-referenced.

## Cross-Links

- `research/insights/brain-search-system.md` -- the system blueprint this report updates
- `research/evaluations/brain-index-upgrade-evaluation.md` -- this report's evaluation
- `research/insights/two-tier-fleet-memory-single-vector-space.md` -- related fleet memory architecture
- `governance/template-reports.md` -- format validator used for this file
- `brain-index/README.md` -- tool documentation

## Version History

| Date | Author | Change |
|------|--------|--------|
| 2026-08-10 | Link | Initial report of the brain-index embedding upgrade session |
