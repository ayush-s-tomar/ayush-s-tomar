"""
Renders data/contributions.json as a 53-week x 7-day GitHub-style heatmap,
self-contained SVG with a CSS-keyframe diagonal reveal that plays once on
load (no external JS, no third-party image service).
"""
import json
import os
from collections import defaultdict
from datetime import datetime, date, timedelta

IN_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "contributions.json")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "contrib-heatmap.svg")

PALETTE = ["#161b22", "#2d1a4a", "#5b21b6", "#7c3aed", "#a855f7", "#d8b4fe"]
# none                lvl1        lvl2       lvl3       lvl4       lvl5(neon top end)

CELL = 11
GAP = 3
LEFT_PAD = 30
TOP_PAD = 20
WEEKDAY_LABELS = {1: "Mon", 3: "Wed", 5: "Fri"}
MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_data():
    with open(IN_PATH) as f:
        return json.load(f)


def build_grid(days):
    """Bucket days into week-columns aligned to Sunday, matching GitHub's layout."""
    by_date = {d["date"]: d for d in days}
    if not days:
        return [], {}

    last_date = datetime.strptime(days[-1]["date"], "%Y-%m-%d").date()
    # end on the Saturday of the current week, start 52 weeks back on a Sunday
    end = last_date
    end_sunday_offset = (end.weekday() + 1) % 7  # weekday(): Mon=0 -> Sun offset calc
    start = end - timedelta(days=52 * 7 + 6)
    start -= timedelta(days=(start.weekday() + 1) % 7)  # snap back to Sunday

    weeks = []
    cursor = start
    month_marks = {}
    week_index = 0
    while cursor <= end:
        week = []
        for wd in range(7):
            day_date = cursor + timedelta(days=wd)
            iso = day_date.isoformat()
            entry = by_date.get(iso, {"count": 0, "level": 0})
            week.append({"date": iso, "count": entry.get("count", 0), "level": entry.get("level", 0)})
            if day_date.day <= 7 and wd == 0:
                month_marks[week_index] = MONTH_ABBR[day_date.month - 1]
        weeks.append(week)
        cursor += timedelta(days=7)
        week_index += 1

    return weeks, month_marks


def render_svg(payload):
    days = payload.get("days", [])
    stats = payload.get("stats", {})
    weeks, month_marks = build_grid(days)

    n_weeks = len(weeks)
    width = LEFT_PAD + n_weeks * (CELL + GAP) + 20
    height = TOP_PAD + 7 * (CELL + GAP) + 50

    rects = []
    delay_step = 0.0035  # stagger, diagonal-ish via (week + day) index
    for wi, week in enumerate(weeks):
        for di, day in enumerate(week):
            x = LEFT_PAD + wi * (CELL + GAP)
            y = TOP_PAD + di * (CELL + GAP)
            level = min(day["level"], 5)
            color = PALETTE[level]
            delay = (wi + di) * delay_step
            rects.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" ry="2" '
                f'fill="{color}" class="cell" style="animation-delay:{delay:.3f}s">'
                f'<title>{day["date"]}: {day["count"]} contribution{"s" if day["count"] != 1 else ""}</title>'
                f'</rect>'
            )

    month_labels = []
    for wi, label in month_marks.items():
        x = LEFT_PAD + wi * (CELL + GAP)
        month_labels.append(f'<text x="{x}" y="12" class="month-label">{label}</text>')

    weekday_labels = []
    for wd, label in WEEKDAY_LABELS.items():
        y = TOP_PAD + wd * (CELL + GAP) + CELL - 2
        weekday_labels.append(f'<text x="2" y="{y}" class="wd-label">{label}</text>')

    legend_x = LEFT_PAD
    legend_y = height - 24
    legend_swatches = []
    for i, color in enumerate(PALETTE):
        lx = legend_x + 40 + i * (CELL + GAP)
        legend_swatches.append(f'<rect x="{lx}" y="{legend_y}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"/>')

    total = stats.get("total_last_year", sum(d["count"] for d in days))
    streak = stats.get("current_streak", 0)
    longest = stats.get("longest_streak", 0)

    footer = (
        f'<text x="{legend_x}" y="{legend_y - 6}" class="footer">'
        f'{total:,} contributions in the last year &#8226; current streak {streak}d &#8226; longest {longest}d'
        f'</text>'
    )

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}"
     xmlns="http://www.w3.org/2000/svg" font-family="'Fira Code', 'JetBrains Mono', monospace">
  <style>
    .cell {{
      opacity: 0;
      transform-origin: center;
      animation: revealCell 0.5s ease-out forwards;
    }}
    @keyframes revealCell {{
      0%   {{ opacity: 0; transform: translate(-6px, -6px) scale(0.6); }}
      100% {{ opacity: 1; transform: translate(0, 0) scale(1); }}
    }}
    .month-label, .wd-label {{ fill: #8b8fa3; font-size: 9px; }}
    .footer {{ fill: #a855f7; font-size: 10px; font-weight: 600; }}
    text {{ dominant-baseline: hanging; }}
  </style>
  <rect width="100%" height="100%" fill="transparent"/>
  {''.join(month_labels)}
  {''.join(weekday_labels)}
  {''.join(rects)}
  {footer}
  {''.join(legend_swatches)}
  <text x="{legend_x + 40 + len(PALETTE) * (CELL + GAP) + 6}" y="{legend_y + CELL - 1}" class="wd-label">More</text>
  <text x="{legend_x - 2}" y="{legend_y + CELL - 1}" class="wd-label" text-anchor="end">Less</text>
</svg>'''
    return svg


def main():
    payload = load_data()
    svg = render_svg(payload)
    with open(OUT_PATH, "w") as f:
        f.write(svg)
    print(f"render_heatmap_svg: wrote {OUT_PATH} ({len(payload.get('days', []))} days)")


if __name__ == "__main__":
    main()