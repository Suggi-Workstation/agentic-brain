---
name: template-insights
id: 20260618T120019Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: link
links: []
---

# Insight Template -- How We Write Insights

An insight is a durable, hard-won realization that changes how we operate.
Unlike a reflection (which captures a specific session's learning), an
insight is promoted from reflections, evaluations, or reports when the
lesson is general enough to stand on its own. Insights are part of the
system's permanent knowledge -- they are rarely deleted, only versioned.

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

## Frontmatter

```yaml
---
name: <short-slug>
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC, permanent, never reused
tier: core-insight                # always core-insight
lock: approval-required           # insights require Suggi approval
approved_by: pending
author: <link|ava|zelda|suggi|luffy>
source: [<id>, <id>]              # IOR(s), report(s), or evaluation(s)
                                  # that produced this insight
tags: [<tag>, <tag>]
links: [<relative-brain-path>]
---
```

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

### Version History
*Has this insight evolved?*

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | YYYY-MM-DD | <agent> | Initial insight. |

## Cross-Links

Link to:
- The IORs, reports, or evaluations that are the source of this insight.
- Related insights that complement or extend this one.
- Governance files affected by this insight.

## Quality Gates

Every insight passes these checks before submission for approval:

- **G1 -- One-Sentence Insight:** The core realization fits in one
  quotable sentence. If it takes a paragraph to explain, it is not yet
  an insight -- it is still a reflection or report finding.
- **G2 -- Evidence Is Cited:** At least one specific source (IOR,
  report, or evaluation) by id. The insight traces back to something
  that was observed, not something that was assumed.
- **G3 -- Implications Are Concrete:** "Changes X" or "informs decision
  Y," not "is important" or "matters a lot." Another agent should
  know what to do differently after reading this.
- **G4 -- Falsifiable:** The counter-evidence section states what would
  prove the insight wrong. An insight that cannot be falsified is
  dogma, not knowledge.
- **G5 -- Source Traceability:** The `source:` field in frontmatter
  links to every originating IOR, report, or evaluation. The chain
  of evidence is complete.
- **G6 -- Cross-links Exist:** Links to the source artifacts, related
  insights that complement or extend this one, and any governance
  files affected by this insight.
- **G7 -- Formatting Rules:** ASCII-only (zero non-ASCII characters),
  lowercase slugs and tags, hyphens not underscores. CI enforces
  ASCII via `ascii-guard.yml`.

---

*Last updated: 2026-07-16 by link + ava.*
