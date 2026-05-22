#!/usr/bin/env python3
"""Simple local threat intelligence lookup module."""

import csv
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
IOC_PATH = BASE_DIR / "iocs.csv"


def load_iocs():
    with IOC_PATH.open(newline="") as file:
        return {row["indicator"]: row for row in csv.DictReader(file)}


def lookup(indicator, iocs):
    if indicator in iocs:
        row = iocs[indicator]
        return {
            "indicator": indicator,
            "verdict": "known",
            "type": row["type"],
            "category": row["category"],
            "confidence": row["confidence"],
            "source": row["source"],
        }

    return {
        "indicator": indicator,
        "verdict": "unknown",
        "type": "unknown",
        "category": "not listed",
        "confidence": "none",
        "source": "local IOC list",
    }


def main():
    indicators = sys.argv[1:] or [
        "malware.testcategory.com",
        "203.0.113.60",
        "example.com",
    ]

    iocs = load_iocs()
    for indicator in indicators:
        result = lookup(indicator, iocs)
        print(
            f"{result['indicator']}: {result['verdict']} "
            f"({result['type']}, {result['category']}, confidence={result['confidence']}, source={result['source']})"
        )


if __name__ == "__main__":
    main()

