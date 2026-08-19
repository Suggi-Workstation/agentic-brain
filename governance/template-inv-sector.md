---
name: template-inv-sector
id: 20260819T171739Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Neo
links:
  - investing/frameworks/sector-specific-metrics.md
  - investing/frameworks/dcf-intrinsic-value.md
---

# Investment Template -- Sector Scoreboard

The output format for sector-specific metric selection and
adjustments. Identifies the sector, selects the correct growth /
quality / cheapness metrics, states what NOT to use, and lists
sector-specific DCF adjustments. The methodology lives in
`investing/frameworks/sector-specific-metrics.md`; this template
defines what the completed analysis looks like.

## What This Template Is

A routing template. It tells the analyst which metrics apply and
which are misleading for this company's sector. A one-size-fits-all
screening approach systematically misranks banks, SaaS companies,
REITs, insurers, and cyclicals. This template prevents that.

## Global Formatting Rules

Same as all brain files: 7-bit ASCII, lowercase, hyphen-delimited.

## Compliance Checklist -- HARD GATE

Pre-commit gate. Every item MUST be confirmed.

- [ ] Ticker and company name stated  (PASS / HALT)
- [ ] Sector classified from the standard list  (PASS / HALT)
- [ ] Growth metric selected with formula and 5yr value  (PASS / HALT)
- [ ] Quality metric selected with formula and 5yr value  (PASS / HALT)
- [ ] Cheapness metric selected with formula and current value  (PASS / HALT)
- [ ] Sector-specific quality checks listed  (PASS / HALT)
- [ ] "What NOT to use" section populated  (PASS / HALT)
- [ ] DCF adjustments: sector-specific modifications stated  (PASS / HALT)
- [ ] Composite rank calculated (if screening)  (PASS / HALT)
- [ ] All values sourced  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <ticker>-sector
id: <YYYYMMDDTHHMMSSZ>
tier: investment-sector
author: Neo
tags: [sector-metrics, screening, <ticker>]
links:
  - investing/frameworks/sector-specific-metrics.md
  - investing/companies/<ticker>.md
---
```

## Scoreboard

### Header

```
Company:    <name>
Ticker:     <ticker>
Sector:     <one of: industrial, consumer, technology-saas,
             financial-bank, financial-insurance, reit,
             energy-materials, healthcare-pharma, utility>
```

### Metric Selection

| Metric Type | Selected Metric | Formula | 5yr Value | Signal |
|:--|:--|:--|:--|:--|
| Growth | <metric> | <formula> | <X%> | <strong/moderate/weak> |
| Quality | <metric> | <formula> | <X%> | <strong/moderate/weak> |
| Cheapness | <metric> | <formula> | <Xx> | <cheap/reasonable/expensive> |

### Sector-Specific Quality Checks

| Check | Value | Threshold | Pass? |
|:--|:--|:--|:--|
| <check 1> | <X> | <threshold> | Y/N |
| <check 2> | <X> | <threshold> | Y/N |
| <check 3> | <X> | <threshold> | Y/N |

### What NOT to Use

| Metric | Why It Fails Here |
|:--|:--|
| <metric 1> | <rationale> |
| <metric 2> | <rationale> |

### DCF Adjustments

| Parameter | Standard Approach | Sector Adjustment | Rationale |
|:--|:--|:--|:--|
| FCF definition | EBIT*(1-tax)+dep-capex-wc | <adjustment> | <why> |
| WACC | CAPM + moat adj | <adjustment> | <why> |
| Terminal value | Gordon Growth | <adjustment> | <why> |
| Other | -- | <adjustment> | <why> |

### Composite Rank (if screening)

```
Growth percentile:    <X>
Quality percentile:   <X>
Cheapness percentile:  <X>
Composite rank:       <X>  (0.25*g + 0.25*q + 0.50*c, lower = better)
```

### Verdict

```
SECTOR: <classification>
APPLICABLE METRICS: <growth>, <quality>, <cheapness>
METRIC SIGNALS: growth=<signal>, quality=<signal>, cheapness=<signal>
SECTOR FIT: <clean / requires adjustments / non-standard>

Key sector risk: <single most sector-specific risk>
```

---

*Last updated: 2026-08-19 by Neo. Scoreboard format; methodology in the framework file.*