#!/usr/bin/env python3
"""Controlled local IDS-style test using sample network events."""

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
EVENTS_PATH = BASE_DIR / "network_events.csv"


def parse_time(value):
    return datetime.fromisoformat(value)


def load_events():
    with EVENTS_PATH.open(newline="") as file:
        return list(csv.DictReader(file))


def detect_port_scan(events):
    alerts = []
    grouped = defaultdict(list)
    for event in events:
        grouped[(event["src_ip"], event["dst_ip"])].append(event)

    for (src_ip, dst_ip), group in grouped.items():
        ports = {event["dst_port"] for event in group}
        times = [parse_time(event["timestamp"]) for event in group]
        if len(ports) >= 5 and (max(times) - min(times)).total_seconds() <= 60:
            alerts.append({
                "type": "port_scan",
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "detail": f"{len(ports)} ports contacted within 60 seconds",
            })
    return alerts


def detect_sql_injection(events):
    alerts = []
    patterns = ["' or '1'='1", " union select ", "--", "/*"]
    for event in events:
        text = event["event"].lower()
        if any(pattern in text for pattern in patterns):
            alerts.append({
                "type": "possible_sql_injection",
                "src_ip": event["src_ip"],
                "dst_ip": event["dst_ip"],
                "detail": event["event"],
            })
    return alerts


def detect_ssh_bruteforce(events):
    alerts = []
    failures = defaultdict(int)
    for event in events:
        if event["event"] == "ssh_failed":
            failures[(event["src_ip"], event["dst_ip"])] += 1

    for (src_ip, dst_ip), count in failures.items():
        if count >= 3:
            alerts.append({
                "type": "ssh_bruteforce",
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "detail": f"{count} failed SSH attempts",
            })
    return alerts


def main():
    events = load_events()
    alerts = []
    alerts.extend(detect_port_scan(events))
    alerts.extend(detect_sql_injection(events))
    alerts.extend(detect_ssh_bruteforce(events))

    for alert in alerts:
        print(f"{alert['type']}: {alert['src_ip']} -> {alert['dst_ip']} ({alert['detail']})")


if __name__ == "__main__":
    main()

