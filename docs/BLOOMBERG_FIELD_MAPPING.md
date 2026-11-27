# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
- Instructor reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` (not present in the team repository; the mapping below was derived by comparing the sample fixture with the expected canonical result)
- Live connectivity: **not demonstrated**

The fixture declares itself as `"sample_kind": "instructor_approved_fallback_fixture"` and `"is_live_bloomberg_output": false`. Its values are illustrative teaching values reused from `data/sample/prices.csv`, not certified Bloomberg historical observations.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Both pairs were checked in the sample fixture (`canonical_ticker` / `provider_identifier` keys of each series).

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | teaching wrapper key; string `YYYY-MM-DD`, kept as is |
| ticker | application mapping from series `canonical_ticker` | `AAPL` or `SP500`; never the Bloomberg identifier |
| open | `open_value` | teaching wrapper key; numeric |
| high | `high_value` | teaching wrapper key; numeric |
| low | `low_value` | teaching wrapper key; numeric |
| close | `close_value` | teaching wrapper key; numeric |
| volume | `volume_value` | teaching wrapper key; integer, `0` for SPX Index |

**Important:** `observation_date`, `open_value`, `high_value`, `low_value`, `close_value` and `volume_value` are **teaching wrapper keys**, not Bloomberg LIVE field mnemonics. No LIVE Bloomberg field name is documented here because none was observed.

## Inspected inputs

| Series | Observations | First date | Last date | Missing values |
|---|---|---|---|---|
| AAPL US Equity -> AAPL | 21 | 2026-09-01 | 2026-09-30 | none |
| SPX Index -> SP500 | 21 | 2026-09-01 | 2026-09-30 | none (volume is 0) |

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: `AAPL US Equity` -> canonical `AAPL`
- Benchmark identifier: `SPX Index` -> canonical `SP500`
- Date representation: string `YYYY-MM-DD` in `observation_date`
- Input structure: JSON object with a `series` list; each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list
- Missing fields: none in the sample
- Special normalization notes:
  - set `ticker` from `canonical_ticker`, not from `provider_identifier`;
  - convert prices to `float` and volume to `int`;
  - SPX Index volume is `0`: an index has no traded volume, so this is expected, not an error;
  - the output must match `data/sample/bloomberg_reference_expected.json` row for row;
  - `analytics.py` must not change.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`

## Security

No credential, session token or terminal information is included in this document.