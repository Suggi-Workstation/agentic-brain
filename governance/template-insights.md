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
production procedure (clone, Feynman loop, write, commit, push, discard)
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
- [ ] source: links to every originating IOR, report, or evaluation by id  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from brain root; `brain:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] One-sentence insight: fits in one quotable line; if it takes a paragraph, it is not yet an insight  (PASS / HALT)
- [ ] Evidence: at least one source cited by id, chain of evidence complete  (PASS / HALT)
- [ ] Implications: concrete ("changes X" or "informs decision Y"), not platitudes  (PASS / HALT)
- [ ] Counter-evidence: states what would prove the insight wrong; an insight that cannot be falsified is dogma  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Cross-links: source artifacts + related insights + affected governance files  (PASS / HALT)
- [ ] Version-history table: present (date + author + change rows) if file has version updates; omitted for single-version files; located at top of file, immediately after title, before content  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: insight                # always insight
source: [<id>, <id>]              # IOR(s), report(s), or evaluation(s)
                                  # that produced this insight
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<path/to/file.md>]   # paths relative to agentic-brain root. Use `brain:` prefix for cross-repo references; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `verification-is-the-bottleneck`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `insight`.
- `source` lists the ids of the IORs, reports, or evaluations that
  produced this insight. At least one source required.
- `author` is who wrote the insight (e.g. Link, Ava, Zelda, Suggi, Luffy).
- `tags` use lowercase, hyphens for spaces. Prefer existing tags from
  the brain's tag registry.
- `links` are paths relative to the agentic-brain root. Use `brain:`
  prefix (e.g. `governance/system-constitution.md`) for
  cross-repo references. No prefix = same-repo link. Do not use
  absolute paths or file:// URIs.

## Naming Convention

Files are named: `<short-slug>.md`

- `short-slug` -- kebab-case, max 60 chars, unique.

Example: `verification-is-the-bottleneck.md`

## Body Structure

### The Insight
*What did we learn? State it in one sentence.*

- The core realization as a single, memorable sentence.
- This is the headline. It should be quotable.

### Evidence
*How do we know this is true?*

- What was observed that led to this insight.
- Cite the specific IORs, evaluations, or reports that produced it.
- If the insight was tested across multiple sessions or domains, note
  the pattern.

### Implications
*What changes because we know this?*

- How does this alter our architecture, our processes, or our behavior?
- What decisions does this insight inform?
- What should new agents know about this on day one?

### Counter-evidence
*What would prove this wrong?*

- State the conditions under which this insight would be invalidated.
- If those conditions have already been tested and the insight held,
  note that.
- This section makes the insight falsifiable and prevents it from
  becoming dogma.

## Version History
*Has this insight evolved?*

The version-history table should ONLY be created if the file has been
updated and additions/removals were made; omit for single-version files.

The version-history table lives at the top of the file, immediately
after the title, before any content section. See "## Example" section.

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | YYYY-MM-DD | <Agent> | Initial insight. |
| 2 | YYYY-MM-DD | <Agent> | Initial insight. |

HALT - Add the version-history table ONLY if the file has been updated.

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

## Version History (only when file has version updates)

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-06-14 | Suggi | Initial insight from WO-1 through WO-8 findings. |
| 2 | 2026-06-17 | Ava | Added extra explanations. |

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
