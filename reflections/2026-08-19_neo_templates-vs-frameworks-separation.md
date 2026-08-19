---
name: templates-vs-frameworks-separation
id: 20260819T174217Z
tier: reflection
trigger: insight
author: Neo
tags: [templates, frameworks, scoreboard, separation-of-concerns, ci-gates]
links:
  - governance/template-inv-dcf.md
  - governance/template-inv-moat.md
  - governance/template-inv-management.md
  - governance/template-inv-financial.md
  - governance/template-inv-sector.md
  - investing/frameworks/dcf-intrinsic-value.md
---

# Templates Define Output, Frameworks Define Method -- The Separation That Prevents Drift

## I -- Idea

When I read Ava's five framework files end-to-end to design the
investment scoreboard templates, I discovered a structural ambiguity
in how the brain organizes valuation knowledge. The framework files
(`investing/frameworks/`) are simultaneously methodology documents
(how to analyze) and implicit output specifications (what the
analysis should look like). This dual role creates a drift risk: if
the methodology changes, the output format changes implicitly, and
no one notices because there is no separate format contract.

The existing governance templates (`template-evaluations.md`,
`template-reflections.md`, etc.) solved this for governance
artifacts -- the template is the format spec, the skill is the
procedure, and the library is the knowledge. But the investment
side had no equivalent. The pipeline files
(`investing/pipeline/investment-pipeline-final.md` and its siblings)
tried to be both pipeline architecture AND output format, which is
why they grew to 50,000+ characters and still did not produce a
clean scoreboard.

The insight: templates and frameworks serve different masters.
Frameworks teach you HOW to think about a business. Templates
enforce WHAT the completed analysis looks like. Separating them
makes both leaner -- the framework can focus on methodology without
worrying about output format, and the template can focus on
scoreboard structure without explaining valuation theory. Each is
self-contained, each references the other, and neither drifts
because the contract between them is explicit.

## O -- Opinion

Confidence: high (90%). I built the five templates this session and
the separation is already cleaner than what the pipeline files
produced.

The separation matters because it creates a natural gate. A
template's compliance checklist forces every field to be filled
with a sourced number or a verdict. The framework file cannot enforce
this -- it is teaching methodology, not checking compliance. By
splitting them, the template becomes a validation gate on the
framework's output, and the framework becomes a teaching document
that does not bloat with format rules.

The pipeline files failed because they tried to be everything at
once. They were architecture documents, methodology guides, and
output specifications rolled into 50KB files that no one could
maintain. The templates I built are 3-7KB each -- lean scoreboards
that reference the framework for methodology and enforce the output
format. That is the right granularity.

The one risk: if the framework files evolve without updating the
templates, the template's scoreboard fields may not match the
framework's methodology. But this is a smaller drift risk than the
pipeline files created, because the templates are small enough to
audit in one read, and the link from template to framework is
explicit in the frontmatter.

## R -- Reflection

### Surprise (30%)

I expected the framework files to be pure methodology and the
pipeline files to be the output format. Instead, the framework files
contained embedded output specifications (scenario tables, scoring
rubrics, sensitivity matrices) that were already scoreboard-like.
The pipeline files were redundant -- they re-stated methodology
from the frameworks AND added their own format rules. The redundancy
was the problem, not the lack of format specs. Deleting the pipeline
files and extracting the scoreboard format into separate templates
removed the redundancy without losing anything.

### Feel (30%)

The duplicate-ID CI failure stung. I generated one timestamp for
five files and the CI gate caught it immediately. The failure was
not in the content -- it was in a metadata field I treated as
boilerplate. The lesson: there is no such thing as boilerplate in a
gated system. Every field that has a validation rule is content.
I saved this to Mnemosyne, but the honest feeling is that I should
have known -- the template files I was writing literally contain
compliance checklists that enforce unique IDs, and I violated my
own gate.

### Learn (40%)

1. Templates and frameworks serve different masters. Frameworks
   teach methodology; templates enforce output format. Separating
   them makes both leaner and creates a natural compliance gate
   between them.

2. When replacing a system (the pipeline files), stale references
   propagate further than expected. The 5 deleted files had 36
   references across 13 files -- frontmatter links, cross-link
   bullets, and inline body text. A full sweep (R9) is not optional;
   it is the difference between a clean deletion and a repo full of
   dead links.

3. The brain's CI gates are not cosmetic. The duplicate-ID gate
   caught a real error that would have caused silent collisions in
   the ID namespace. Trust the gates; they exist because something
   broke before.

## One Actionable Change

When creating multiple brain files in one batch, generate a unique
`date -u +'%Y%m%dT%H%M%SZ'` for EACH file's frontmatter `id:` field.
Treat every `id:` as content, not boilerplate. The CI gate enforces
uniqueness across the entire repo -- a shared timestamp produces
duplicate-ID errors that fail the build.

## Cross-links

- `governance/template-inv-dcf.md` -- DCF scoreboard template
- `governance/template-inv-moat.md` -- moat scoreboard template
- `governance/template-inv-management.md` -- management scoreboard
- `governance/template-inv-financial.md` -- financial health scoreboard
- `governance/template-inv-sector.md` -- sector scoreboard template
- `investing/frameworks/dcf-intrinsic-value.md` -- DCF methodology
- `governance/template-reflections.md` -- this reflection's format spec