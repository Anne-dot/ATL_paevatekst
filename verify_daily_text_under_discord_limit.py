#!/usr/bin/env python3
"""One-off analysis: verify monthly document extraction for all days.

Checks each day produces a non-empty result under Discord's 2000-char limit.
Not committed - safe to delete after run.
"""
import calendar
import re
from config import MONTHLY_DOC_IDS, MONTH_NAMES
from drive_client import create_google_drive_service, download_document_as_text

DISCORD_LIMIT = 2000
MONTHS_TO_CHECK = range(1, 13)  # All 12 months
YEAR = 2026


def extract_for_day(content, day, month):
    """Mirror date_utils.find_todays_meditation_text but with injected day/month."""
    lines = content.split('\n')
    month_name = MONTH_NAMES[month]
    start_pattern = rf"^0?{day}\.\s*{month_name}\b"
    all_months = "|".join(MONTH_NAMES.values())
    stop_pattern = rf"^\d{{1,2}}\.\s*(?:{all_months})\b"

    start_line = None
    heading = None
    for i, line in enumerate(lines):
        if re.match(start_pattern, line.strip(), re.IGNORECASE):
            start_line = i
            heading = line.strip()
            break

    if start_line is None:
        return {"day": day, "found": False, "heading": None, "chars": 0, "lines": 0}

    collected = []
    for i in range(start_line + 1, len(lines)):
        line = lines[i].strip()
        if re.match(stop_pattern, line, re.IGNORECASE):
            break
        collected.append(line)

    while collected and not collected[0]:
        collected.pop(0)
    while collected and not collected[-1]:
        collected.pop()

    text = '\n'.join(collected)
    return {
        "day": day,
        "found": True,
        "heading": heading,
        "chars": len(text),
        "lines": len(collected),
    }


def classify(r):
    if not r["found"]:
        return "MISSING"
    if r["chars"] == 0:
        return "EMPTY"
    if r["chars"] > DISCORD_LIMIT:
        return "TOO_LONG"
    return "OK"


def main():
    service = create_google_drive_service()
    print()

    all_problems = []
    grand_total = 0

    for month in MONTHS_TO_CHECK:
        days_in_month = calendar.monthrange(YEAR, month)[1]
        month_name = MONTH_NAMES[month]
        doc_id = MONTHLY_DOC_IDS[month]

        print(f"\n{'='*80}")
        print(f"📅 {month_name.upper()} ({days_in_month} days)")
        print(f"{'='*80}")

        content = download_document_as_text(service, doc_id)

        results = [extract_for_day(content, day, month) for day in range(1, days_in_month + 1)]

        print(f"\n{'Day':>4} | {'Chars':>6} | {'Status':<8} | Heading")
        print("-" * 80)
        for r in results:
            status = classify(r)
            heading = r["heading"] or "—"
            print(f"{r['day']:>4} | {r['chars']:>6} | {status:<8} | {heading[:60]}")

        ok_count = sum(1 for r in results if classify(r) == "OK")
        problems = [(month, r) for r in results if classify(r) != "OK"]
        all_problems.extend(problems)
        grand_total += len(results)

        print(f"\n  → {ok_count}/{len(results)} days OK in {month_name}")

    print(f"\n{'='*80}")
    print(f"GRAND TOTAL: {grand_total - len(all_problems)}/{grand_total} days OK")
    if all_problems:
        print(f"\n⚠️  Problems found:")
        for month, r in all_problems:
            print(f"   {MONTH_NAMES[month]} day {r['day']}: {classify(r)} ({r['chars']} chars, heading: {r['heading']})")
    else:
        print(f"✅ All days across all checked months extract cleanly under {DISCORD_LIMIT} chars.")


if __name__ == "__main__":
    main()
