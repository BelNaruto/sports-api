"""Export a team's season schedule to an .ics file (Google Calendar, Apple Calendar, Outlook).

Sports API on RapidAPI: https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information

Usage:
    pip install requests
    RAPIDAPI_KEY=your_key python team_schedule_to_ics.py nba 13          # Los Angeles Lakers
    RAPIDAPI_KEY=your_key python team_schedule_to_ics.py soccer 359 --league eng.1   # Arsenal

Find team ids with GET /{sport}/teams or GET /search?query=lakers
"""
import argparse
import os
import sys
from datetime import datetime, timedelta

import requests

HOST = "sports-information.p.rapidapi.com"


def api(path, **params):
    r = requests.get(
        f"https://{HOST}{path}",
        params={k: v for k, v in params.items() if v},
        headers={"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"], "X-RapidAPI-Host": HOST},
        timeout=60,
    )
    body = r.json()
    if not body.get("success"):
        sys.exit(f'{body["error"]["code"]}: {body["message"]}')
    return body["data"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sport")
    ap.add_argument("team_id")
    ap.add_argument("--season")
    ap.add_argument("--league", help="required for soccer / rugby, e.g. eng.1")
    a = ap.parse_args()

    data = api(f"/{a.sport}/teams/{a.team_id}/schedule", season=a.season, league=a.league)
    events = data if isinstance(data, list) else data.get("events", [])

    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//sports-api-example//EN"]
    for ev in events:
        start = datetime.fromisoformat(ev["date"].replace("Z", "+00:00"))
        end = start + timedelta(hours=3)
        fmt = "%Y%m%dT%H%M%SZ"
        lines += [
            "BEGIN:VEVENT",
            f'UID:{ev["id"]}@sports-api',
            f"DTSTART:{start.strftime(fmt)}",
            f"DTEND:{end.strftime(fmt)}",
            f'SUMMARY:{ev.get("name") or ev.get("shortName", "Game")}',
            f'LOCATION:{(ev.get("venue") or {}).get("name", "")}',
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")

    out = f"{a.sport}-{a.team_id}.ics"
    with open(out, "w") as f:
        f.write("\r\n".join(lines))
    print(f"Wrote {len(events)} games to {out}")


if __name__ == "__main__":
    main()
