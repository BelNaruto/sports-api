"""Print a prediction report for a day of games (win %, projected score, picks).

Sports API on RapidAPI: https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information

Usage:
    pip install requests
    RAPIDAPI_KEY=your_key python predictions_report.py nfl
    RAPIDAPI_KEY=your_key python predictions_report.py soccer --league epl
    RAPIDAPI_KEY=your_key python predictions_report.py nba --date 20260115

Predictions are statistical estimates for information and entertainment,
not betting advice.
"""
import argparse
import os
import sys

import requests

HOST = "sports-information.p.rapidapi.com"


def api(path, **params):
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        sys.exit("Set RAPIDAPI_KEY. Get a key at https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information")
    r = requests.get(
        f"https://{HOST}{path}",
        params={k: v for k, v in params.items() if v},
        headers={"X-RapidAPI-Key": key, "X-RapidAPI-Host": HOST},
        timeout=60,
    )
    body = r.json()
    if not body.get("success"):
        sys.exit(f'{body["error"]["code"]}: {body["message"]}')
    return body["data"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sport", nargs="?", default="nfl")
    ap.add_argument("--date", help="YYYYMMDD (default: today / this week)")
    ap.add_argument("--league", help="soccer / rugby competition, e.g. epl, la liga, ucl")
    a = ap.parse_args()

    data = api(f"/{a.sport}/predictions", date=a.date, league=a.league)
    preds = data.get("predictions", [])
    print(f"{a.sport.upper()} predictions: {len(preds)} games\n")
    for p in preds:
        g, pr = p["game"], p["prediction"]
        probs = pr.get("probabilities", {})
        line = f'{g.get("shortName", "?"):<14} home {probs.get("home", 0):>5.0%}  away {probs.get("away", 0):>5.0%}'
        if "draw" in probs:
            line += f'  draw {probs["draw"]:>5.0%}'
        score = pr.get("projectedScore") or pr.get("mostLikelyScore")
        if score:
            line += f"  projected {score}"
        line += f'  confidence: {pr.get("confidence", "-")}'
        print(line)
    if data.get("accuracy"):
        print(f'\nModel accuracy on finished games: {data["accuracy"]}')


if __name__ == "__main__":
    main()
