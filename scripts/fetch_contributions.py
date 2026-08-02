"""
Scrapes the public contribution-calendar HTML fragment GitHub serves for any
profile, no auth/token required. Writes data/contributions.json with raw
day-level data plus derived stats used by render_heatmap_svg.py.

Source: https://github.com/users/<username>/contributions
"""
import json
import os
import sys
from datetime import datetime, date

import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GH_USERNAME", "ayush-s-tomar")
URL = f"https://github.com/users/{USERNAME}/contributions"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")


def fetch_html(url: str) -> str:
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (profile-readme-bot)"}, timeout=20)
    resp.raise_for_status()
    return resp.text


def parse_days(html: str):
    soup = BeautifulSoup(html, "html.parser")
    cells = soup.select("td.ContributionCalendar-day")
    if not cells:
        # GitHub has changed markup before; fall back to the tool-tip based <table> layout
        cells = soup.select("[data-date]")

    days = []
    for cell in cells:
        d = cell.get("data-date")
        if not d:
            continue
        level_raw = cell.get("data-level")
        count_attr = cell.get("data-count")
        if count_attr is not None:
            count = int(count_attr)
        else:
            tooltip_id = cell.get("id")
            count = 0
            if tooltip_id:
                tip = soup.find("tool-tip", attrs={"for": tooltip_id})
                if tip and tip.text:
                    first_token = tip.text.strip().split(" ")[0]
                    count = 0 if first_token.lower() == "no" else int(first_token)
        level = int(level_raw) if level_raw is not None else min(count, 4)
        days.append({"date": d, "count": count, "level": level})

    days.sort(key=lambda x: x["date"])
    return days


def derive_stats(days):
    if not days:
        return {}

    total = sum(d["count"] for d in days)

    # current streak: walk backwards from most recent day
    current_streak = 0
    for d in reversed(days):
        if d["count"] > 0:
            current_streak += 1
        else:
            break

    # longest streak
    longest_streak = 0
    running = 0
    for d in days:
        if d["count"] > 0:
            running += 1
            longest_streak = max(longest_streak, running)
        else:
            running = 0

    best_day = max(days, key=lambda x: x["count"])

    monthly = {}
    for d in days:
        month_key = d["date"][:7]  # YYYY-MM
        monthly[month_key] = monthly.get(month_key, 0) + d["count"]

    return {
        "total_last_year": total,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": {"date": best_day["date"], "count": best_day["count"]},
        "monthly_totals": monthly,
        "generated_at": datetime.utcnow().isoformat() + "Z",
    }


def main():
    try:
        html = fetch_html(URL)
        days = parse_days(html)
        if not days:
            raise ValueError("No contribution cells parsed — GitHub markup may have changed")
    except Exception as exc:
        print(f"fetch_contributions: FAILED ({exc})", file=sys.stderr)
        # Keep the existing data file untouched rather than overwrite with empty data
        sys.exit(1)

    stats = derive_stats(days)
    payload = {"username": USERNAME, "days": days, "stats": stats}

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"fetch_contributions: wrote {len(days)} days, {stats.get('total_last_year', 0)} total contributions")


if __name__ == "__main__":
    main()