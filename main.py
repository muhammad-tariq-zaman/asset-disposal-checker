"""Check IT asset disposals meet the wipe standard for their sensitivity.

Usage: python3 main.py disposals.csv
CSV columns: asset,sensitivity,wipe_method,certificate (yes/no)
High sensitivity needs physical destruction or degaussing + a
certificate; medium needs a 3-pass wipe + certificate; low needs any
wipe + certificate. Anything else is a GAP.
"""
import argparse, csv, sys

REQUIRED = {"high": {"destroy", "degauss"},
            "medium": {"wipe-3pass"},
            "low": {"wipe-1pass", "wipe-3pass", "destroy", "degauss"}}


def check(row):
    sensitivity = row["sensitivity"].strip().lower()
    method = row["wipe_method"].strip().lower()
    if sensitivity not in REQUIRED:
        return "GAP", "unknown sensitivity"
    if method not in REQUIRED[sensitivity]:
        return "GAP", f"{method} is not enough for {sensitivity} sensitivity"
    if row["certificate"].strip().lower() != "yes":
        return "GAP", "no destruction certificate"
    return "COMPLIANT", "meets standard"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    gaps = 0
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            verdict, reason = check(row)
            if verdict == "GAP":
                gaps += 1
            print(f"{row['asset']}: {verdict} ({reason})")
    print(f"{gaps} disposal(s) with gaps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
