#!/usr/bin/env python3
import argparse
from core.parser import parse_logs
from core.analyzer import detect_anomalies
from core.llm import summarize_anomalies


def main():
    parser = argparse.ArgumentParser(description="NetWatch - Network Log Analyzer CLI")
    parser.add_argument("--file", required=True, help="Path to log file")
    args = parser.parse_args()

    print("Reading logs...")
    logs = parse_logs(args.file)

    print(f"Parsed {len(logs)} entries")
    anomalies = detect_anomalies(logs)

    if not anomalies:
        print("No significant anomalies found.")
        return

    print("\nDetected anomalies:\n")
    for a in anomalies:
        print(f"- {a['type']}: {a.get('summary', a.get('message'))} (count={a.get('count',1)})")

    print("\nGenerating AI summary/recommendations...\n")
    summary = summarize_anomalies(anomalies)
    print(summary)


if __name__ == "__main__":
    main()
