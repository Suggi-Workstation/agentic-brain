---
name: template-inv-dcf
id: 20260819T172742Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Neo
links:
  - investing/frameworks/dcf-intrinsic-value.md
  - library/value-investing/margin-of-safety.md
  - library/value-investing/intrinsic-value-estimation-methods.md
---

# Investment Template -- DCF Intrinsic Value Scoreboard

The output format for a discounted cash flow valuation. Produces a
defensible intrinsic value RANGE with bull/base/bear scenarios, EPV
cross-check, sensitivity matrix, and margin of safety verdict. The
methodology lives in `investing/frameworks/dcf-intrinsic-value.md`;
this template defines what the completed analysis looks like.

## What This Template Is

A scoreboard, not a textbook. Every field is a number or a verdict.
Methodology explanation belongs in the framework file, not here. The
analyst fills in the tables; the template enforces the structure.

## Global Formatting Rules

Same as all brain files: 7-bit ASCII, lowercase, hyphen-delimited.
CI enforces.

## Compliance Checklist -- HARD GATE

Pre-commit gate. Every item MUST be confirmed. Do not include this
checklist in the published file.

- [ ] Ticker and company name stated  (PASS / HALT)
- [ ] Valuation date and price source cited  (PASS / HALT)
- [ ] WACC derivation: Rf, beta, ERP, moat adjustment all stated  (PASS / HALT)
- [ ] Revenue growth path: 5-year table with thesis rationale per year  (PASS / HALT)
- [ ] Margin path: stated, moat-consistent, not above historical peak  (PASS / HALT)
- [ ] Terminal growth rate: below GDP, moat-justified  (PASS / HALT)
- [ ] Exit multiple cross-check: implied EV/EBIT within sector range  (PASS / HALT)
- [ ] Bull/base/bear scenario table: all 6 parameters per scenario  (PASS / HALT)
- [ ] Scenario weights stated; not used to justify a buy  (PASS / HALT)
- [ ] EPV calculated and interpreted (growth-free floor)  (PASS / HALT)
- [ ] DCF base > 2x EPV flagged if present  (PASS / HALT)
- [ ] Sensitivity matrix: 5x5 WACC x terminal growth, populated  (PASS / HALT)
- [ ] Intrinsic value range table: bear/base/bull/weighted/EPV  (PASS / HALT)
- [ ] MOS calculated against base AND bear cases  (PASS / HALT)
- [ ] MOS classification matches moat-score calibration  (PASS / HALT)
- [ ] Key assumptions table: value, rationale, what-would-change-it  (PASS / HALT)
- [ ] Verdict: BUY CANDIDATE / WATCHLIST / DISCARD with confidence  (PASS / HALT)
- [ ] Every number sourced (filing year, data provider, or "estimated")  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters  (PASS / HALT)

## Frontmatter Schema

```yaml
---
name: <ticker>-dcf
id: <YYYYMMDDTHHMMSSZ>
tier: investment-dcf
author: Neo
tags: [dcf, valuation, intrinsic-value, <ticker>]
links:
  - investing/frameworks/dcf-intrinsic-value.md
  - investing/companies/<ticker>.md
---
```

## Scoreboard

### Header

```
Company:    <name>
Ticker:     <ticker>
Sector:     <sector>
Price:      $<X> (as of <date>, source: <provider>)
Shares:     <N> diluted (source: <filing>)
```

### WACC Derivation

```
Risk-free rate (Rf):    <X>%  (source: <10Y bond, date>)
Beta:                  <X>   (source: <provider, 5yr monthly>)
ERP:                   <X>%  (equity risk premium)
Moat adjustment:       <+/->pp  (rationale: <moat score reference>)
WACC:                  <X>%
```

### Revenue Growth Path

| Year | Growth Rate | Rationale |
|:--|:--|:--|
| Y1 | X% | <thesis pillar> |
| Y2 | X% | <thesis pillar> |
| Y3 | X% | <converging> |
| Y4 | X% | <converging> |
| Y5 | X% | <approaching terminal> |

### Margin Path

| Year | Operating Margin | Rationale |
|:--|:--|:--|
| Y1 | X% | <moat-consistent> |
| Y5 | X% | <terminal level> |

### Terminal Value

```
Method: Gordon Growth
Terminal growth (g):  <X>%  (rationale: <moat + GDP>)
FCF_Year5:            $<X>
Terminal Value:       $<X>
TV as % of total IV:  <X>%  (must be 50-90%)
Implied exit EV/EBIT: <X>x  (sector comp range: <A>-<B>x)
```

### Scenario Table

| Parameter | Bear | Base | Bull |
|:--|:--|:--|:--|
| Revenue growth (Y1-3 avg) | X% | X% | X% |
| Revenue growth (Y4-5 avg) | X% | X% | X% |
| Operating margin (terminal) | X% | X% | X% |
| CapEx as % of revenue | X% | X% | X% |
| WACC | X% | X% | X% |
| Terminal growth rate | X% | X% | X% |

Weights: <P-bear>% / <P-base>% / <P-bull>%

### EPV Cross-Check

```
Adjusted Earnings:    $<X>  (normalized EBIT * (1-tax) + 0.5*dep - maint CapEx)
EPV (enterprise):     $<X>  (Adjusted Earnings / WACC)
EPV per share:        $<X>
EPV vs price:         <X>x  (interpretation: <growth free / priced in / aggressive>)
DCF base / EPV:       <X>x  (flag if > 2.0)
```

### Sensitivity Matrix (IV per share)

| WACC \ g | g-1.0% | g-0.5% | Base g | g+0.5% | g+1.0% |
|:--|:--|:--|:--|:--|:--|
| WACC-2.0% | $X | $X | $X | $X | $X |
| WACC-1.0% | $X | $X | $X | $X | $X |
| Base WACC | $X | $X | $X | $X | $X |
| WACC+1.0% | $X | $X | $X | $X | $X |
| WACC+2.0% | $X | $X | $X | $X | $X |

### Intrinsic Value Range

| Scenario | IV per Share | vs Current Price | MOS |
|:--|:--|:--|:--|
| Bear | $X | +/-X% | X% |
| Base | $X | +/-X% | X% |
| Bull | $X | +/-X% | X% |
| Weighted | $X | +/-X% | X% |
| EPV (no-growth) | $X | +/-X% | -- |

### Margin of Safety Classification

```
Moat score: <X.X>  (source: <moat template or framework>)
Required MOS: <X>%  (wide >= 20%, narrow >= 30%, weak >= 40%)
Actual MOS (base): <X>%
Actual MOS (bear): <X>%
```

### Key Assumptions

| Assumption | Base Value | Rationale | What Would Change It |
|:--|:--|:--|:--|
| Revenue CAGR (Y1-5) | X% | <thesis> | <risk> |
| Terminal margin | X% | <5yr avg + moat> | <risk> |
| WACC | X% | <CAPM + moat adj> | <risk> |
| Terminal growth | X% | <GDP-based> | <risk> |

### Verdict

```
INTRINSIC VALUE RANGE: $<low> to $<high> per share
BASE CASE: $<X>
CURRENT PRICE: $<W>
MARGIN OF SAFETY (base): <X>%
MARGIN OF SAFETY (bear): <X>%

VERDICT: <BUY CANDIDATE / WATCHLIST / DISCARD>
CONVICTION: <HIGH / MODERATE / LOW>

Key risk: <single most impactful assumption>
```

---

*Last updated: 2026-08-19 by Neo. Scoreboard format; methodology in the framework file.*