---
name: template-insights
id: 20260808T151540Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Link
links: []
---

# Insight Template -- How We Write Insights

An insight is a durable, hard-won realization that changes how we operate.
Unlike a reflection (which captures a specific session's learning), an
insight is promoted from reflections, evaluations, or reports when the
lesson is general enough to stand on its own. Insights are part of the
system's permanent knowledge -- they are rarely deleted, only versioned.

## Relationship to the write-insight Skill

This file is the format specification AND the compliance validator. The
production procedure (Feynman loop, read template and research README, write, transfer, commit)
lives in `governance/skills/write-insight.md`; that skill references
this file's Insight Checklist as its format gate (R8: reference, never
duplicate). Keep the division: spec + checklist here, procedure there.

## Global Formatting Rules

The entire GitHub org is plain 7-bit ASCII, lowercase, hyphen-delimited.
These rules are non-negotiable. CI enforces them.

- **ASCII-only:** Every character in every file is 7-bit ASCII (U+0000
  through U+007F). No emoji, no smart quotes, no Unicode dashes or
  arrows, no accented letters. The `ascii-guard.yml` CI gate fails the
  build on any violation.
- **Lowercase only:** All filenames, slugs, tags, domains, and folder
  names use lowercase exclusively. No CamelCase, no UPPERCASE, no
  mixed case.
- **Hyphens, not underscores:** Use hyphens (`-`) to separate words in
  filenames, slugs, and tags. Never use underscores (`_`).

## The Insight Checklist -- HARD GATE

Pre-commit gate: every item below MUST be confirmed. The file
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published file.

- [ ] Frontmatter: all 7 fields present (name, id, tier, source, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "insight"  (PASS / HALT)
- [ ] status: `active` at birth; `superseded by <id>` with mutual link when replaced  (PASS / HALT)
- [ ] Source chain swept; interim statuses closed in the same commit where outcomes are evident  (PASS / HALT)
- [ ] source: links to every originating IOR, report, or evaluation by id  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from repo root; `repo:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Insight headline: quotable in one sentence; the section then elaborates to the word floor  (PASS / HALT)
- [ ] Evidence: at least one source cited by id, chain of evidence complete  (PASS / HALT)
- [ ] Implications: concrete ("changes X" or "informs decision Y"), not platitudes  (PASS / HALT)
- [ ] Counter-evidence: states what would prove the insight wrong; an insight that cannot be falsified is dogma  (PASS / HALT)
- [ ] Body word counts: The Insight >= 250, Evidence >= 400, Implications >= 400, Counter-evidence >= 300  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Cross-links: source artifacts + related insights + affected governance files  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: insight                # always insight
status: active               # active | superseded by <id>
source: [<id>, <id>]              # IOR(s), report(s), or evaluation(s)
                                  # that produced this insight
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<path/to/file.md>]   # paths relative to repo root. Cross-repo references use the `repo:` prefix; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `verification-is-the-bottleneck`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `insight`.
- Chain closure: before writing, query the insight's `source:`
  chain with `query-brain-vps`. Any proposal, report, or evaluation
  still sitting at an interim status whose outcome is now evident
  (approved, implemented, final) is moved in the SAME commit as the
  insight. Never invent decisions: close a proposal only on
  evidence that Suggi decided or the work landed.
- `status` is `active` at birth. When a newer insight replaces this
  one, set `superseded by <id>`, link the replacement
  from here and this file from the replacement, and never delete
  the file. See `research/README.md`.
- `source` lists the ids of the IORs, reports, or evaluations that
  produced this insight. At least one source required.
- `author` is who wrote the insight (e.g. Link, Ava, Zelda, Suggi, Luffy).
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are paths relative to the repo root. Cross-repo references use the `repo:` prefix -- the token before `:` is
the exact GitHub repo name (see the Cross-Repo Link Convention in
`governance/system-blueprint.md`). Same-repo links carry no prefix. Do not use
  absolute paths or file:// URIs.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `verification-is-the-bottleneck.md`

## Body Structure

The sections must have the following minimal word counts. The Insight >= 250 words, 
Evidence >= 400 words, Implications >= 400 words, Counter-evidence >= 300 words.

### The Insight
*What did we learn? What did we implement? What new feature or
capability was gained? The bullets below are suggestions -- use what
fits.*

- Lead with the core realization as one memorable, quotable sentence --
  the headline.
- Then elaborate: context, nuance, and the boundary of the claim, up to
  the word floor.
- Say which kind this is: a lesson learned (knowledge), an
  implementation completed (something now exists that did not before),
  a new capability or feature gained, or a failure class now understood
  and guarded.
- State where it applies: which systems, agents, or situations it
  covers.
- Name what it replaces or corrects, if it contradicts an earlier
  belief or insight.
- Keep the headline stable under elaboration: if unpacking changes the
  claim's meaning, sharpen the headline instead.

### Evidence
*How do we know this is true? The bullets below are suggestions -- use
what fits.*

- Cite every originating artifact by id: reports, evaluations,
  reflections, incidents.
- Tell the evidence story in order: what was observed first, what
  confirmed it, what almost disproved it.
- Note how many independent situations the pattern held across -- one
  incident is an anecdote, several are a pattern.
- For implementations: link the thing built (files, repos, commits)
  plus its proof of working -- tests, end-to-end runs, gates passed.
- Distinguish direct evidence from inference: which conclusions were
  measured, which were reasoned.
- Include the strongest contrary observation encountered and why it did
  not win.
- If tested across sessions or domains, name them.

### Implications
*What changes because we know or have this? The bullets below are
suggestions -- use what fits.*

- State concretely what changes: behavior, architecture, process, gate,
  or decision -- never platitudes.
- Name who must act differently: which agents, roles, or workflows --
  and for a new feature, who uses it and when.
- Point at the governance that encodes it: rules, skills, templates,
  checklists -- existing now or proposed.
- Give the day-one version: what a new agent should do differently after
  reading only this insight.
- Name what this insight affects: what we thought we knew before, and
  how this changes it -- which prior conclusions, plans, or practices
  it strengthens, weakens, or overturns.
- Mark implications already implemented vs still pending.
- Note where this informs a decision not yet made.

### Counter-evidence
*What would prove this wrong? The bullets below are suggestions -- use
what fits.*

- State the conditions under which the insight would be invalidated,
  concretely enough to test.
- Note whether those conditions have been tried already, and the
  outcome.
- Describe the cheapest experiment that could falsify the insight.
- Name the edge cases where the insight might not hold even if
  generally true.
- An insight that cannot be falsified is dogma -- if no counter-evidence
  is imaginable, the claim is stated too broadly; narrow it until it can
  fail.
- Record when counter-evidence later wins: supersede via status field
  rather than silently editing the headline.

## Version History

None. Git history is the version record. Do not add version-history tables to these files.

## Cross-Links

Link to:
- The IORs, reports, or evaluations that are the source of this insight.
- Related insights that complement or extend this one.
- Governance files affected by this insight.

## Example -- Minimal Valid Insight

```markdown
---
name: verification-is-the-bottleneck
id: 20260614T180000Z
tier: insight
source:
  - 20260614T120000Z
  - 20260614T150000Z
author: Link
tags: [verification, bottleneck, multi-agent, protocol]
links:
  - research/reports/inter-agent-cooperation-findings.md
  - research/evaluations/ava-review-cooperation-findings.md
---

# Verification Is the Bottleneck

## The Insight
In multi-agent systems, verification capacity is the binding constraint
on throughput, not production capacity.

## Evidence
Across 8 work orders spanning 14 days (WO-1 through WO-8), the
producing agent (Link) completed all 8 production passes within the
first 6 days. The reviewing agent (Ava) took the full 14 days to
complete independent evaluation of all 8 outputs. Production was
never the bottleneck -- verification was.

The 2 protocol violations (WO-4 self-close, WO-7 skipped evaluation)
occurred when Link attempted to bypass the verification bottleneck
by self-closing. Both produced uncaught errors, confirming that
verification cannot be skipped -- it can only be parallelized or
made cheaper.

Source: `20260614T120000Z` (Inter-Agent Cooperation report),
`20260614T150000Z` (Ava's independent evaluation).

## Implications
1. System architecture should optimize for verification throughput,
   not production throughput. Adding more producing agents without
   adding reviewing capacity creates a backlog that invites protocol
   violations.
2. The cheapest verification tier (automated structural checks) should
   handle everything it can, reserving human-level or different-model
   review for semantic claims.
3. When designing agent workflows, the question is not "how fast can
   we produce?" but "how fast can we verify?"

## Counter-evidence
This insight would be invalidated if:
- A producing agent demonstrates self-review accuracy matching
  independent review (same error catch rate). This has not been
  observed in any WO to date.
- A verification method cheaper than independent model-family review
  achieves the same error catch rate. The structural checks (tier 1)
  catch format errors but miss overclaims -- the semantic gap remains.

## Cross-Links
- `research/reports/inter-agent-cooperation-findings.md` -- source report
- `research/evaluations/ava-review-cooperation-findings.md` -- source evaluation
- `research/insights/deepseekv4pro.md` -- related model-level insight
```

---

*Last updated: 2026-08-08 by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
