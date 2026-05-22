#!/usr/bin/env python3
"""Small honeytoken monitor for a controlled deception-technology demo."""

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TOKENS_PATH = BASE_DIR / "honeytokens.json"
EVENTS_PATH = BASE_DIR / "events.jsonl"


def load_json(path):
    return json.loads(path.read_text())


def load_events(path):
    return [
        json.loads(line)
        for line in path.read_text().splitlines()
        if line.strip()
    ]


def find_honeytoken_alerts(tokens, events):
    alerts = []
    for event in events:
        message = event.get("message", "")
        for token in tokens:
            if token["value"] in message:
                alerts.append({
                    "severity": "high",
                    "timestamp": event["timestamp"],
                    "event_type": event["event_type"],
                    "user": event["user"],
                    "src_ip": event["src_ip"],
                    "honeytoken": token["label"],
                    "recommended_response": token["recommended_response"],
                })
    return alerts


def main():
    tokens = load_json(TOKENS_PATH)
    events = load_events(EVENTS_PATH)
    alerts = find_honeytoken_alerts(tokens, events)

    if not alerts:
        print("No honeytoken use detected.")
        return

    for alert in alerts:
        print(
            f"[{alert['severity'].upper()}] {alert['timestamp']} "
            f"{alert['event_type']} from {alert['src_ip']} "
            f"user={alert['user']} honeytoken={alert['honeytoken']}"
        )
        print(f"Recommended response: {alert['recommended_response']}")


if __name__ == "__main__":
    main()

