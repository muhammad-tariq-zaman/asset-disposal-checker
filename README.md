# asset-disposal-checker

Verify asset disposals against sensitivity rules: high-sensitivity kit needs destruction/degaussing plus a certificate, weaker wipes are flagged as gaps.

## How to run

```sh
python3 main.py disposals.csv
```

## Example output

```
LAP-014: COMPLIANT (meets standard)
LAP-015: GAP (wipe-1pass is not enough for high sensitivity)
1 disposal(s) with gaps.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
