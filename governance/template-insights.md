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

An insight is a self-contained manual or blueprint of one subject as it
stands now: a system, a repo, a program we wrote, a pipeline, a process,
a framework, or a piece of durable knowledge. Any agent must be able to
read it with no other context and understand what the subject is, what
it is made of, how it works end to end, and where its limits are.

The subject decides the body. A repo, a program, and a pipeline need
different sections, so the body structure is up to the author and the
person who asked for the insight. The frontmatter, the opening summary,
and the checklist below are fixed. An insight is a living document:
when its subject changes, the insight is updated in place.

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

- [ ] Frontmatter: all 8 fields present (name, id, tier, status, source, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "insight"  (PASS / HALT)
- [ ] status: `active`; `superseded by <id>` with mutual link only when another insight replaces it  (PASS / HALT)
- [ ] source: ids of the artifacts the insight draws on, or `[]` when it describes its subject directly  (PASS / HALT)
- [ ] Source chain swept: interim statuses of proposals, reports, or evaluations it closes moved in the same commit  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from repo root; `repo:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Opening summary: the first paragraph says what the subject is, what it is for, and where it lives  (PASS / HALT)
- [ ] Self-contained: a fresh agent with no chat history can follow the subject end to end; every term, part, path, and step it needs is defined or linked  (PASS / HALT)
- [ ] Current state only: no history, version tables, dated change narrative, or "previously ... now" text  (PASS / HALT)
- [ ] Verified: every path, command, name, and behavior checked against the live subject or its files before committing  (PASS / HALT)
- [ ] Lean: as long as the subject needs and no longer; content owned by another file is linked, not restated  (PASS / HALT)
- [ ] Public-safe: no secrets, credentials, or private access details  (PASS / HALT)
- [ ] Cross-links: the files or repos it describes + related insights + governance it is bound by  (PASS / HALT)
- [ ] Filename: lowercase, kebab-case slug  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: insight                # always insight
status: active               # active | superseded by <id>
source: [<id>, <id>]              # artifacts the insight draws on;
                                  # [] when it describes its subject directly
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<tag>, <tag>]             # lowercase, hyphens for spaces
links: [<path/to/file.md>]   # paths relative to repo root. Cross-repo references use the `repo:` prefix; omit for same-repo links.
---
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `logbook-archiver`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing, including when the insight is updated. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `tier` is always `insight`.
- Chain closure: when the insight draws on research artifacts, query
  its `source:` chain with `query-brain-vps`. Any proposal, report, or
  evaluation still sitting at an interim status whose outcome is now
  evident (approved, implemented, final) is moved in the SAME commit as
  the insight. Never invent decisions: close a proposal only on
  evidence that Suggi decided or the work landed.
- `status` is `active` at birth and stays `active` while the insight is
  updated in place. When a different insight replaces this one, set
  `superseded by <id>`, link the replacement from here and this file
  from the replacement, and never delete the file. See
  `research/README.md`.
- `source` lists the ids of the reflections, reports, evaluations, or
  other artifacts the insight draws on. Use `[]` when it describes a
  system, program, or process directly from its live state.
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

Example: `logbook-archiver.md`

## Body

The body is free-form within the checklist. It opens with the title and
the opening summary, then uses whatever sections make the subject
understandable, and ends with Cross-Links.

Common building blocks -- use what fits, rename freely, add your own:

| Block | Answers |
|:--|:--|
| Parts | What is it made of? Where does each part live, and what does it do? |
| How it works | What happens, step by step, from input to result? |
| Rules | What must always hold? What is forbidden? |
| Usage | How do agents, people, or other systems use it: commands, files, inputs, outputs? |
| Operations | How is it run, checked, maintained, and recovered? |
| Limits | What it does not do; known edge cases and failure modes |
| Rationale | Why it is built this way, where the reason matters for using it correctly |
| Evidence | For a lesson or framework: the artifacts (by id) and observations that support it |

Example shapes, by subject:

- **A repo or onboarding system:** summary, Parts, Rules, the flow end to
  end, Checks, Communication, Maintenance, Cross-Links.
- **A program or tool:** summary, Parts, How it works, Usage,
  Configuration, Limits, Cross-Links.
- **A pipeline or process:** summary, Stages, Hand-offs, Gates, Failure
  handling, Cross-Links.
- **A framework or durable lesson:** summary (the core idea in one
  sentence), Explanation, When it applies, Evidence, Limits, Cross-Links.

Writing rules:

- Present tense; describe what is, not what changed.
- Tables for parts and gates, numbered steps for flows, prose for
  reasoning.
- Define a term at first use. Name paths, commands, and files exactly.
- Refer to procedures and documents by name, never by another
  document's mutable step or section number.
- No mutable counts (R11) unless the number is the point; then derive it
  live before writing.

## Version History

None. Git history is the version record. Do not add version-history tables to these files.

## Cross-Links

Link to:
- The files, repos, or systems the insight describes.
- Related insights that complement or extend this one.
- Governance the subject is bound by.
- Source artifacts, when it draws on any.

## Minimal Structure

```markdown
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>
tier: insight
status: active
source: []
author: <Name>
tags: [<tag>, <tag>]
links:
  - <path/to/related-file.md>
---

# <Subject> -- <What It Is>

<Opening summary: what the subject is, what it is for, where it lives,
and who uses it.>

## <A section that fits the subject, e.g. Parts>

## <Another section, e.g. How It Works>

## Cross-Links

- `<path/to/related-file.md>` -- <why it matters>
```

---

*Last updated: 2026-10-21 by Morpheus, approved by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
