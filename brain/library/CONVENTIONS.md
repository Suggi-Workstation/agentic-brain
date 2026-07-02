# Library Conventions - how knowledge is stored and found

Every agent MUST follow these rules. They are what makes the library
searchable today (by agents) and vector-search-ready tomorrow.

## 1. Layout

    brain/library/_index.md            <- master catalog: all domains
    brain/library/<domain>/_index.md   <- domain catalog: groups + topics
    brain/library/<domain>/group_<slug>.md   <- group summary file
    brain/library/<domain>/<topic-slug>.md   <- one topic, one file

## 2. One topic = one file = one chunk

A topic file covers ONE idea deeply. If it grows past ~400 lines,
split it. This keeps each file a clean retrieval unit for both
agents and (later) embedding chunks.

## 3. Front matter - required on every topic file

    ---
    name: exact-file-slug
    domain: laws-regulations
    group: securities-corporate-law
    description: One sentence. THE most important line for search.
    tags: [antitrust, moats, regulation]
    links: [patent-law-ip-moats, entity-list-investment-signal]
    status: stub | draft | complete
    created: 2026-07-02
    updated: 2026-07-02
    ---

Rules:
- `description` must be a specific, dense sentence (not "notes about X").
- `links` are slugs of related topics, cross-domain welcome.
- `tags` are lowercase, singular, reused across the library (check
  existing tags before inventing new ones).

## 4. How to SEARCH the library (agents)

Layered, cheapest first:
1. Read `brain/library/_index.md` - pick candidate domains by description.
2. Read the domain `_index.md` - scan the topic table descriptions.
3. Grep front matter across the library for tags or keywords:
   `grep -r "tags:.*moat" brain/library --include=*.md -l`
4. Only then open full topic files. Follow `links:` to neighbors.

## 5. Density rule

Max 6 topics per group. At 7+, split the group and record the split
in the domain `_index.md` changelog.

## 6. Vector-search readiness

Because every topic is one file with a `description`, `tags`, and
`links`, an embeddings index can later be built directly from front
matter + body, with zero restructuring. Until then, agents ARE the
semantic layer: they navigate descriptions the way a vector index
navigates embeddings.

## 7. ASCII only

Plain 7-bit ASCII in every file. No emojis, no smart quotes, no
em-dashes. Use [x] and [ ] for status marks. CI enforces this.
