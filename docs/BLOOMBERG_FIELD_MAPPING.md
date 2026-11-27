# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source:
data/sample/bloomberg_reference_sample.json

Reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md

Live connectivity:
not demonstrated

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Teaching wrapper key (not a Bloomberg LIVE field mnemonic) |
| ticker | application mapping | Canonical ticker (`AAPL` or `SP500`), distinct from provider identifier |
| open | `open_value` | Teaching wrapper key (not a Bloomberg LIVE field mnemonic) |
| high | `high_value` | Teaching wrapper key (not a Bloomberg LIVE field mnemonic) |
| low | `low_value` | Teaching wrapper key (not a Bloomberg LIVE field mnemonic) |
| close | `close_value` | Teaching wrapper key (not a Bloomberg LIVE field mnemonic) |
| volume | `volume_value` | Teaching wrapper key (not a Bloomberg LIVE field mnemonic; `0` on `SP500` in sample) |

Note: teaching wrapper key != Bloomberg LIVE field mnemonic. Unverified Bloomberg LIVE field names are not invented or assumed here.

## TD10 handoff

- Access mode: APPROVED_SAMPLE (Live connectivity: not demonstrated)
- Instrument identifier: `AAPL US Equity` (canonical: `AAPL`)
- Benchmark identifier: `SPX Index` (canonical: `SP500`)
- Date representation: ISO date string (`YYYY-MM-DD`, e.g., `2026-09-01`)
- Input structure: JSON object with top-level metadata and a `series` array containing per-role objects (`role`, `canonical_ticker`, `provider_identifier`, `observations` list of daily records)
- Missing fields: None in the fallback sample fixture (`observation_date`, `open_value`, `high_value`, `low_value`, `close_value`, `volume_value` are all present; `volume_value` is `0` for `SP500`)
- Special normalization notes: Map `series[*].observations[*]` into flat canonical rows (`date`, `ticker`, `open`, `high`, `low`, `close`, `volume`) while preserving canonical tickers (`AAPL`, `SP500`) rather than `provider_identifier` (`AAPL US Equity`, `SPX Index`). Keep `src/analytics.py` provider-neutral.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`