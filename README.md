# Sports API: live scores, stats, odds & predictions for 90+ leagues (NBA, NFL, MLB, NHL, Soccer, NCAA, F1, UFC...)

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Sports%20Information%20API-0055DA?logo=rapid&logoColor=white)](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information)
[![Try it free](https://img.shields.io/badge/Try%20it-Free%20plan-2ea44f)](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information/pricing)
[![Endpoints](https://img.shields.io/badge/endpoints-932-blue)](ENDPOINTS.md)
[![Sports](https://img.shields.io/badge/sports-41-orange)](#supported-sports-and-leagues)
[![Telegram support](https://img.shields.io/badge/Support-Telegram%20%40pintoflow-26A5E4?logo=telegram&logoColor=white)](https://t.me/pintoflow)

**One REST API for sports data.** Live scores, schedules, standings, box scores, play-by-play, betting odds, injuries, rosters, player stats, news, recruiting **and game predictions** for 90+ leagues and competitions, all in one clean JSON format.

> **👉 [Get your API key on RapidAPI](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information)** · [Open the playground](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information/playground) · [Full endpoint reference (932 endpoints)](ENDPOINTS.md) · [Code examples](examples/)
>
> 💬 **Need help or a faster response?** Contact us on Telegram: [@pintoflow](https://t.me/pintoflow)

Covers **NBA, WNBA, G League, NFL, CFL, UFL, MLB, NHL**, college football, college basketball, baseball, softball, hockey, volleyball and field hockey, **every NCAA sport**, **45+ soccer competitions** (Premier League, La Liga, Serie A, Bundesliga, Ligue 1, MLS, Champions League, World Cup...), rugby union (Six Nations, Premiership, URC, Top 14, Super Rugby), NRL, AFL, lacrosse (NLL, PLL), cricket (IPL, World Cup), FIBA, World Baseball Classic, **ATP/WTA tennis**, **Formula 1, NASCAR, IndyCar**, **PGA, LPGA, LIV, DP World Tour**, **UFC, PFL** and more.

---

## Why this API

- **One API, every major sport.** Code written for `/nba/scoreboard` works for `/nfl/scoreboard`, `/nhl/scoreboard` or `/soccer/scoreboard?league=epl`: same endpoint names, same response shape.
- **Live data.** Live scoreboards refresh about every 15 seconds; one call to `/live` returns every game in progress across leagues.
- **Game predictions built in.** Win probabilities, projected scores, spread and total picks that blend sportsbook odds, ESPN's predictor, team ratings and a log5 model. Soccer gets a Poisson goals model with draw probability, expected goals and the most likely score.
- **Deep game data.** Box scores, play-by-play, win probability, odds from each sportsbook, injuries, depth charts, futures, power index, recruiting rankings.
- **Clean, predictable JSON.** Every response uses the same `{ success, message, error, data, meta }` envelope, with typed error codes and a `requestId`.
- **Free plan available** on [RapidAPI](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information/pricing), so you can start building in minutes.

---

## What you can build

| Project | Endpoints you need |
|---|---|
| **Live score app / widget** (web, mobile, smart TV) | `/live`, `/today`, `/{sport}/scoreboard`, `/{sport}/summary/:id` |
| **Discord / Telegram / Slack sports bot** (scores, final results, injury alerts) | `/{sport}/live`, `/{sport}/scoreboard`, `/{sport}/injuries`, `/{sport}/news` |
| **Fantasy sports assistant** (start/sit, injuries, player trends) | `/{sport}/players/:id/gamelog`, `/{sport}/players/:id/splits`, `/{sport}/injuries`, `/{sport}/teams/:id/depth-chart` |
| **Game prediction dashboard** (win %, projected scores, model accuracy) | `/{sport}/predictions`, `/{sport}/predictions/:id`, `/{sport}/matchup` |
| **Odds comparison & market tracker** (lines, implied probabilities, futures) | `/{sport}/odds/:id`, `/{sport}/futures`, `/{sport}/power-index` |
| **League standings & stats site** (tables, leaders, team pages) | `/{sport}/standings`, `/{sport}/leaders`, `/{sport}/teams/:id/statistics` |
| **Team calendar sync** (export a team's schedule to Google Calendar / iCal) | `/{sport}/teams/:id/schedule`, `/{sport}/calendar` |
| **College sports & recruiting tracker** (AP / Coaches / CFP polls, 247 recruiting) | `/cfb/rankings`, `/mbb/rankings`, `/cfb/player-rankings`, `/cfb/school-commits`, `/ncaa/*` |
| **Sports news aggregator** | `/{sport}/news`, `/{sport}/teams/:id/news`, `/search` |
| **Data science & ML** (historical results, play-by-play, team form, head-to-head) | `/{sport}/schedule?from=&to=`, `/{sport}/play-by-play/:id`, `/{sport}/teams/:id/form`, `/{sport}/head-to-head` |
| **F1 / golf / UFC event trackers** (race sessions, leaderboards, fight cards) | `/f1/scoreboard`, `/f1/standings`, `/pga/scoreboard`, `/ufc/scoreboard`, `/{sport}/events/:id` |
| **Tennis live tracker** (ATP / WTA rankings, Grand Slam draws) | `/tennis/scoreboard`, `/tennis/live`, `/tennis/rankings` |

Ready-to-run code for several of these is in the [`examples/`](examples/) folder.

---

## Code examples

### Live NBA scores (Node.js)

```js
const res = await fetch('https://sports-information.p.rapidapi.com/nba/live', {
  headers: {
    'X-RapidAPI-Key': process.env.RAPIDAPI_KEY,
    'X-RapidAPI-Host': 'sports-information.p.rapidapi.com',
  },
});
const { success, data, error } = await res.json();
if (!success) throw new Error(error.code);
for (const g of data.events ?? data) {
  console.log(`${g.away.team.abbreviation} ${g.away.score} @ ${g.home.team.abbreviation} ${g.home.score}  ${g.status.detail}`);
}
```

### This week's NFL predictions (Python)

```python
import os, requests

r = requests.get(
    "https://sports-information.p.rapidapi.com/nfl/predictions",
    headers={"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
             "X-RapidAPI-Host": "sports-information.p.rapidapi.com"},
    timeout=30,
)
for p in r.json()["data"]["predictions"]:
    probs = p["prediction"]["probabilities"]
    print(f'{p["game"]["shortName"]:12} home {probs["home"]:.0%}  away {probs["away"]:.0%}  ({p["prediction"]["confidence"]})')
```

### Premier League table (curl)

```bash
curl -s 'https://sports-information.p.rapidapi.com/soccer/standings?league=epl' \
  -H 'X-RapidAPI-Key: YOUR_KEY' \
  -H 'X-RapidAPI-Host: sports-information.p.rapidapi.com'
```

More examples: [live scoreboard in the terminal](examples/live-scoreboard.js) · [predictions report](examples/predictions_report.py) · [Discord score bot](examples/discord-score-bot.js) · [team schedule to iCal](examples/team_schedule_to_ics.py) · [embeddable HTML widget](examples/scores-widget.html)

---

## Supported sports and leagues

| Group | Base paths |
|---|---|
| US & Canada pro | `/nba` · `/wnba` · `/g-league` · `/nfl` · `/cfl` · `/ufl` · `/mlb` · `/nhl` |
| College | `/cfb` · `/mbb` · `/wbb` · `/college-baseball` · `/college-softball` · `/mens-college-hockey` · `/womens-college-hockey` · `/mens-college-volleyball` · `/womens-college-volleyball` · `/college-field-hockey` · `/ncaa` (every NCAA sport) |
| Soccer, rugby & more | `/soccer` (45+ competitions) · `/rugby` · `/nrl` · `/afl` · `/nll` · `/pll` · `/fiba` · `/world-baseball-classic` · `/cricket` |
| Tennis | `/tennis` (ATP, WTA) |
| Motor racing | `/f1` · `/nascar` · `/indycar` |
| Golf | `/pga` · `/lpga` · `/liv` · `/dp-world-tour` · `/champions-tour` · `/korn-ferry` |
| MMA | `/ufc` · `/pfl` · `/bellator` |

Each team sport has scoreboards, live games, schedules, calendars, game summaries, box scores, play-by-play, win probability, odds, predictions, standings, teams, rosters, team schedules and stats, injuries, news, leaders and player profiles, stats, game logs and splits. **See every endpoint and parameter in [ENDPOINTS.md](ENDPOINTS.md).**

---

## Contents

1. [Quick start](#quick-start)
2. [Response format](#response-format)
3. [Errors](#errors)
4. [Finding ids](#finding-ids)
5. [Dates, weeks and seasons](#dates-weeks-and-seasons)
6. [Sports and endpoints](#sports-and-endpoints)
7. [Sport-specific notes](#sport-specific-notes)
8. [Predictions](#predictions)
9. [Data freshness](#data-freshness)
10. [Dos and don'ts](#dos-and-donts)
11. [FAQ](#faq)
12. [Support](#support)

---

## Quick start

Every request needs your RapidAPI key and host headers:

```bash
curl --request GET \
  --url 'https://sports-information.p.rapidapi.com/nba/scoreboard?date=20260115' \
  --header 'X-RapidAPI-Key: YOUR_KEY' \
  --header 'X-RapidAPI-Host: sports-information.p.rapidapi.com'
```

Get your key by subscribing (a free plan is available) on the **[Sports Information API page on RapidAPI](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information)**. The key is shown in the RapidAPI playground under *Code Snippets*.

**JavaScript**

```js
const res = await fetch('https://sports-information.p.rapidapi.com/nfl/predictions', {
  headers: { 'X-RapidAPI-Key': process.env.RAPIDAPI_KEY, 'X-RapidAPI-Host': 'sports-information.p.rapidapi.com' },
});
const { success, data, error, message } = await res.json();
if (!success) throw new Error(`${error.code}: ${message}`);
for (const p of data.predictions) console.log(p.game.shortName, p.prediction.probabilities);
```

**Python**

```python
import requests

r = requests.get(
    "https://sports-information.p.rapidapi.com/soccer/standings",
    params={"league": "esp.1"},
    headers={"X-RapidAPI-Key": "YOUR_KEY", "X-RapidAPI-Host": "sports-information.p.rapidapi.com"},
    timeout=30,
)
body = r.json()
if body["success"]:
    for row in body["data"]["groups"][0]["entries"]:
        print(row["team"]["displayName"], row["stats"]["points"])
else:
    print(body["error"]["code"], body["message"])
```

Good first calls:

| What you want | Call |
|---|---|
| What's available | `GET /sports` and `GET /endpoints?sport=nba` |
| Today's games in all major US leagues | `GET /today` |
| Everything live right now | `GET /live` |
| Find a player or team id | `GET /search?query=lebron` |

---

## Response format

Every response, success or error, has the same shape:

```json
{
  "success": true,
  "message": "OK",
  "error": null,
  "data": { "...": "..." },
  "meta": {
    "requestId": "5f3c0d1e-...",
    "timestamp": "2026-10-14T12:00:00.000Z",
    "responseTimeMs": 182,
    "count": 25
  }
}
```

| Field | Meaning |
|---|---|
| `success` | `true` when `data` holds the result, `false` on any error |
| `message` | Human-readable summary (on errors: what went wrong) |
| `error` | `null` on success, otherwise `{ code, status, details? }` |
| `data` | The payload (`null` on errors) |
| `meta.requestId` | Include it when you report a problem on Telegram ([@pintoflow](https://t.me/pintoflow)) |
| `meta.count` | Present when `data` is an array |

Games share one shape in every league: `id`, `date`, `name`, `status { state: pre | in | post, detail, clock, period }`, `venue`, `broadcasts`, `home` / `away` (`team`, `score`, `winner`, `records`, `linescores`, `leaders`), `odds` and `link`.

Some list endpoints accept `raw=true` and return the provider's original document instead (larger, less consistent; use only if you need a field we don't expose).

---

## Errors

| HTTP | `error.code` | When | What to do |
|---|---|---|---|
| 400 | `VALIDATION_ERROR` | A parameter is missing or malformed | Read `error.details` (`parameter`, `received`, `allowed`, `example`, `didYouMean`) and fix the call. Do not retry unchanged. |
| 400 | `NOT_SUPPORTED` | The feature is not available for that request (rare: each sport group only lists endpoints it supports) | Use another endpoint; do not retry |
| 401 | `UNAUTHORIZED` | Request did not come through RapidAPI | Call through your RapidAPI host with your key |
| 404 | `NOT_FOUND` | Unknown endpoint (e.g. an endpoint that sport's group does not have), or the game / team / player id does not exist, or no data for that date / season | Check the id with a list endpoint; empty dates are normal |
| 405 | `METHOD_NOT_ALLOWED` | Anything other than `GET` | Use `GET` |
| 410 | `DEPRECATED` | A v1 endpoint whose source no longer exists | `error.details.replacement` names the new endpoint |
| 502 | `UPSTREAM_ERROR` | The data provider returned an error | Retry after a few seconds |
| 503 | `SERVICE_UNAVAILABLE` | Provider temporarily unavailable or rate limiting | Retry with backoff (e.g. 2 s, 5 s, 15 s) |
| 504 | `UPSTREAM_TIMEOUT` | Provider too slow | Retry once; for big fan-out calls narrow the request |
| 500 | `INTERNAL_ERROR` | Unexpected | Retry once; report it on Telegram [@pintoflow](https://t.me/pintoflow) with `meta.requestId` |

Example:

```json
{
  "success": false,
  "message": "Unknown soccer league 'premier leage'.",
  "error": {
    "code": "VALIDATION_ERROR",
    "status": 400,
    "details": { "parameter": "league", "received": "premier leage", "didYouMean": "eng.1", "hint": "GET /soccer/leagues lists every supported league id." }
  },
  "data": null,
  "meta": { "requestId": "...", "timestamp": "..." }
}
```

Only retry `5xx` responses. A `4xx` returns the same answer every time.

---

## Finding ids

Ids are numeric strings. Get them from list endpoints instead of guessing:

| Need | Where to find it |
|---|---|
| Game id | `/nba/scoreboard`, `/nba/schedule`, `/nba/teams/:id/schedule` (same in every sport) → `events[].id` |
| Team id | `/nba/teams` → `[].id` (also inside every game: `home.team.id`) |
| Player id | `/nba/teams/:id/roster` → `athletes[].id`, `/nba/leaders`, or `/search?query=` |
| Soccer league id | `/soccer/leagues` (e.g. `eng.1`, `esp.1`, `uefa.champions`) |
| College conference / group id | `/cfb/conferences`, `/mbb/conferences`, `/wbb/conferences` |
| NCAA game id | `/ncaa/scoreboard` → `games[].id` |
| NCAA stat category id | `/ncaa/stats?sport=...&division=...` |
| Tennis player id | `/tennis/rankings` → `ranks[].athlete.id` |

Ids are per league: NBA team `13` (Lakers) is not NFL team `13`.

---

## Dates, weeks and seasons

| Parameter | Format | Notes |
|---|---|---|
| `date` | `YYYYMMDD` or `YYYY-MM-DD` | Default: today (US Eastern sports day). `year` + `month` + `day` also works. |
| `from`, `to` | same as `date` | Date range, max 14 days, on scoreboard / schedule |
| `week` | integer | Football (NFL, CFB, UFL). Use with `year` and `seasontype`. |
| `seasontype` | `1` preseason, `2` regular season, `3` postseason, `4` off-season | |
| `season` (or `year`) | `YYYY` | ESPN labels a season by the year it **ends** (NBA/NHL 2025-26 = `2026`); NFL/MLB/soccer use the year it starts. |
| `groups` | ESPN group id | College only. CFB: `80` FBS (default), `81` FCS. Basketball: `50` Division I (default). `all` for everything. |
| `limit` / `page` | integer | Lists are capped (news 50, leaders 50, transactions 100, scoreboard 1000) |

When a new season has started on the calendar but has no table yet, `standings` and `power-index` return the most recent completed season automatically.

---

## Sports and endpoints

Every sport has its own group of endpoints under its own base path: `/nba/...`, `/wnba/...`, `/nfl/...`, `/soccer/...` and so on. Pick the group for the sport you need and call its endpoints directly; there is no league name to pass in the path.

- The team sports share the same endpoint names, so code written for `/nba/scoreboard` works for `/wnba/scoreboard` or `/nhl/scoreboard` by changing the base path.
- Each group only lists endpoints that sport actually publishes. For example, injuries and depth charts exist for the NFL but not for the NLL.
- Every endpoint name from v1 of this API still works. Old names are listed as **Also at** next to their new equivalent, so v1 users only need to switch their base URL and read the payload from `data`.
- `/soccer`, `/rugby` and `/cricket` cover many competitions, so they take a `league` query parameter (`/soccer/standings?league=la liga`), exactly like v1 did. See [Sport-specific notes](#sport-specific-notes).
- `GET /endpoints?sport=nba` returns the same list as JSON, and `GET /openapi.json` returns an OpenAPI 3 document with one tag per sport.

**The full list of 932 endpoints, with every parameter, is in [ENDPOINTS.md](ENDPOINTS.md).** Jump to a sport: [NBA](ENDPOINTS.md#nba) · [NFL](ENDPOINTS.md#nfl) · [MLB](ENDPOINTS.md#mlb) · [NHL](ENDPOINTS.md#nhl) · [WNBA](ENDPOINTS.md#wnba) · [College Football](ENDPOINTS.md#college-football) · [Men's College Basketball](ENDPOINTS.md#mens-college-basketball) · [NCAA](ENDPOINTS.md#ncaa-all-sports) · [Soccer](ENDPOINTS.md#soccer) · [Rugby](ENDPOINTS.md#rugby-union) · [Cricket](ENDPOINTS.md#cricket) · [Tennis](ENDPOINTS.md#tennis) · [Formula 1](ENDPOINTS.md#formula-1) · [PGA Tour](ENDPOINTS.md#pga-tour) · [UFC](ENDPOINTS.md#ufc)

---

## Sport-specific notes

### Soccer competitions

Choose the competition with `league=` (id, name or nickname). Default: English Premier League.

```
/soccer/standings?league=esp.1
/soccer/standings?league=la liga
/soccer/scoreboard?league=uefa.champions&date=20261021
/soccer/predictions?league=bundesliga
/soccer/teams/359/form?league=eng.1&last=10
```

`GET /soccer/leagues` lists all 48 supported ids. Nicknames accepted: `epl`, `premier league`, `championship`, `la liga`, `bundesliga`, `serie a`, `ligue 1`, `eredivisie`, `mls`, `nwsl`, `liga mx`, `ucl` / `champions league`, `uel`, `uecl`, `world cup`, `euro`, `libertadores`, `fa cup`, `carabao cup`, `saudi pro league`. Any other ESPN league slug (e.g. `jpn.1`) is passed through as well.

Always send the same `league` you used to find a game or team id: a match id from `esp.1` must be requested with `league=esp.1`.

### Rugby union competitions

Choose the competition with `league=`. Default: Six Nations. Rugby league (NRL) has its own group at `/nrl`.

| `league` | Competition | Nicknames |
|---|---|---|
| `180659` | Six Nations | `six nations`, `6n` |
| `244293` | The Rugby Championship | `rugby championship`, `trc` |
| `164205` | Rugby World Cup | `world cup`, `rwc` |
| `289234` | International Test Matches | `tests` |
| `267979` | Gallagher Premiership | `premiership`, `prem` |
| `270557` | United Rugby Championship | `urc` |
| `270559` | French Top 14 | `top 14` |
| `271937` | European Rugby Champions Cup | `champions cup` |
| `242041` | Super Rugby Pacific | `super rugby` |
| `282` | Olympic Men's Sevens | `sevens`, `7s` |

Any other numeric ESPN rugby competition id is accepted too.

### Cricket

`league` is a series id or name: `ipl` (`8048`, default), `world cup` (`8039`), or any numeric ESPN series id. Cricket scores are not single numbers, so `score` is `null` and the text is in `scoreDisplay` (e.g. `"161/5 (18/20 ov, target 156)"`). Predictions are not offered for cricket.

### Tennis

`league` (or `type` on rankings / schedule) is `atp` or `wta`. Scoreboards on Grand Slam days hold hundreds of matches: use `grouping` (`mens-singles`, `womens-singles`, ...) and `state` (`pre`, `in`, `post`) to get only what you need.

### NCAA

`sport` is required and `division` defaults to the first one of the sport. Values: `football` (`fbs`, `fcs`, `d2`, `d3`), `basketball-men`, `basketball-women`, `baseball`, `softball`, `soccer-men`, `soccer-women`, `volleyball-women`, `volleyball-men`, `icehockey-men`, `icehockey-women`, `lacrosse-men`, `lacrosse-women`, `fieldhockey`, `waterpolo-men`, `beach-volleyball`, plus rankings / stats / history only: `tennis-men`, `tennis-women`, `golf-men`, `golf-women`, `wrestling-men`, `gymnastics-women`, `swimming-men`, `swimming-women`. `GET /ncaa/sports` lists them.

Game endpoints (`/ncaa/game/:id`, `/box-score`, `/play-by-play`, `/team-stats`, `/scoring-summary`) return the same clean style as the rest of the API (home / away, numbers as numbers). Add `raw=true` for NCAA's original document. Game ids come from `/ncaa/scoreboard` → `games[].id`.

Retired v1 endpoints `/ncaa/seasons/:sport`, `/ncaa/sport-division-data`, `/ncaa/player-data` and `/ncaa/team-data` answer `410` and name their replacement.

### College groups

`groups` on college scoreboards picks the division: football `80` FBS (default), `81` FCS; basketball `50` Division I (default), `51` Division II, `52` Division III; `all` for everything. Conference ids come from `/cfb/conferences`, `/mbb/conferences`, ...

### CFL standings

The data source does not currently publish CFL standings, so `/cfl/standings` answers `404`.

---

## Predictions

Every team sport has the same three prediction endpoints, e.g. `/nba/predictions`, `/nba/predictions/:id` and `/nba/matchup` (also `/nfl/...`, `/soccer/...`, `/rugby/...`). They return:

```json
{
  "game": { "id": "401872995", "shortName": "SEA @ DEN", "status": { "state": "pre" }, "home": { "team": {}, "record": "3-2" }, "away": {} },
  "prediction": {
    "winner": { "side": "away", "team": { "abbreviation": "SEA" } },
    "probabilities": { "home": 0.452, "away": 0.548 },
    "confidence": "low",
    "confidenceScore": 0.096,
    "projectedMargin": -3.6,
    "projectedScore": { "home": 20.6, "away": 24.1 },
    "projectedTotal": 44.7,
    "picks": {
      "spread": { "line": { "home": 2.5, "away": -2.5 }, "pick": "away", "edge": 1.1 },
      "total": { "line": 40.5, "pick": "over", "edge": 4.2 }
    },
    "basedOn": ["market", "espn", "ratings", "log5"]
  },
  "components": {
    "market":  { "home": 0.4365, "away": 0.5635, "provider": "DraftKings", "weight": 0.45 },
    "espn":    { "home": 0.4705, "away": 0.5257, "weight": 0.3 },
    "ratings": { "home": 0.3956, "away": 0.6044, "weight": 0.15 },
    "log5":    { "home": 0.5531, "away": 0.4469, "weight": 0.1 }
  },
  "inputs": { "home": { "gamesPlayed": 5, "winPercent": 0.6, "pointsFor": 22.4, "pointsAgainst": 19.8 }, "away": {} },
  "result": { "final": true, "score": { "home": 20, "away": 27 }, "outcome": "away", "predictionCorrect": true },
  "disclaimer": "..."
}
```

How it works:

| Signal | What it is |
|---|---|
| `market` | Sportsbook moneyline turned into a probability, bookmaker margin removed |
| `espn` | ESPN's matchup predictor (BPI / FPI), when published |
| `ratings` | Expected margin from each team's points for / against, home advantage, early-season regression, then a normal distribution |
| `log5` | Win-percentage head-to-head estimate with home advantage |

The final probability is a weighted blend of the signals available for that game (weights are re-normalised and shown). `basedOn` lists which signals were used.

**Soccer** uses a Poisson goals model (attack and defence strength vs the league average, home factor) blended 50/50 with the 3-way market when odds exist. It returns `home` / `draw` / `away`, `expectedGoals`, `mostLikelyScore`, `overUnder25` and `bothTeamsToScore`.

- `confidence` is `low`, `medium` or `high`, from how far the favourite's probability is from a coin flip.
- `result` only appears once the game is final. `predictions` lists add `accuracy` for the finished games in the list.
- For a game in progress, `/predictions/:id` adds `liveWinProbability`.
- **Past dates:** predictions for finished games use that season's final standings, so they know more than a real pre-game model did. Treat past accuracy as optimistic.
- **Early season / preseason:** few games played means `low` confidence and sometimes `basedOn: "home-advantage-only"`.

> Predictions are statistical estimates for information and entertainment. They are not betting or financial advice and nothing is guaranteed.

---

## Data freshness

Responses are cached briefly so popular calls stay fast:

| Data | Cached for |
|---|---|
| Live scoreboards and live games | about 15 seconds |
| Today's / upcoming scoreboards | about 1 minute |
| News, injuries, transactions, standings | about 5 minutes |
| Rosters, team stats, rankings, leaders, futures | 30 minutes to a few hours |
| Finished games, team lists, schools, stat categories | hours to a day |

Polling a live game more often than every 15 seconds returns the same data.

---

## Dos and don'ts

**Do**

- Check `success` on every response and branch on `error.code`, not on the message text (messages can change, codes don't).
- Get ids from list endpoints (`teams`, `scoreboard`, `roster`, `search`) and store them; they don't change.
- Cache reference data on your side (teams, rosters, schools, league ids). They change rarely and each call counts against your quota.
- Poll live games every 15–30 seconds, and stop when `status.state` is `post`.
- Use the narrowest endpoint you need: `box-score/:id` instead of `summary/:id`, `live` instead of `scoreboard` when you only want games in progress, `grouping=` for tennis.
- Retry only `502`, `503` and `504`, with backoff, and at most 2–3 times.
- Send `league=` on every soccer call, matching the league the id came from.
- Use `YYYYMMDD` dates and the season conventions above.
- Include `meta.requestId` when you contact support on Telegram ([@pintoflow](https://t.me/pintoflow)).

**Don't**

- Don't retry `400`, `404` or `410`. They will return the same answer.
- Don't loop over every date of a season to build a schedule. Use a team schedule (`/nba/teams/:id/schedule`), the calendar (`/nba/calendar`), `/ncaa/schedule` or `from`/`to` ranges (max 14 days).
- Don't poll faster than the cache refreshes; you pay for identical responses.
- Don't fire dozens of parallel requests in a burst; spread them out. Heavy endpoints (`predictions` for a full college slate, `futures`, `head-to-head`, `today`) do many lookups internally.
- Don't assume an empty list is an error: off-days, off-season and bye weeks legitimately return no games.
- Don't depend on undocumented fields from `raw=true` or `summary`; they come straight from the provider and may change.
- Don't use predictions as betting advice, and don't present them to your users as guaranteed.
- Don't put your RapidAPI key in client-side code (browser or mobile app). Call the API from your server.

---

## FAQ

**Why does a game id return 404?**
It belongs to another league (or another soccer `league=`), or it doesn't exist. Ids are not shared between leagues.

**Why is the scoreboard empty?**
No games that day in that league. For college sports also check `groups` (CFB defaults to FBS, basketball to Division I).

**Which season number do I send?**
The year the season ends for NBA, NHL, WNBA, college basketball (2025-26 → `2026`); the year it starts for NFL, college football, MLB and most soccer leagues.

**How do I get only one team's games?**
The team schedule endpoint of that sport, e.g. `/nba/teams/13/schedule?season=2026` or `/nfl/teams/12/schedule?season=2025`.

**How do I get standings by conference or division?**
`group=conference` or `group=division` on the sport's standings, e.g. `/nfl/standings?group=division`.

**Do the v1 endpoint names still work?**
Yes: `team-list`, `team-info/:id`, `team-players/:id`, `team-roster`, `schedule-team`, `team-statistic(s)`, `player-statistic(s)`, `player-splits`, `weekly-schedule`, `soccer/leagueIds`, `soccer/match-summary/:id`, `ncaa/info/:id` and the other v1 paths all work. Responses now use the `{ success, message, error, data, meta }` envelope: read your old payload from `data`.

---

## Support

💬 For questions, bug reports or feature requests, contact us on Telegram: **[@pintoflow](https://t.me/pintoflow)**. Include the endpoint, the parameters you sent and the `meta.requestId`.

## Get started

1. Open the **[Sports Information API on RapidAPI](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information)** and subscribe (free plan available).
2. Copy your `X-RapidAPI-Key`.
3. Call `GET https://sports-information.p.rapidapi.com/today` and start building, or run one of the [examples](examples/).

---

<sub>Keywords: sports API, live scores API, NBA API, NFL API, MLB API, NHL API, WNBA API, soccer API, football API, Premier League API, Champions League API, college football API, NCAA API, March Madness API, F1 API, Formula 1 API, NASCAR API, golf API, PGA Tour API, UFC API, MMA API, tennis API, cricket API, IPL API, rugby API, AFL API, NRL API, sports odds API, sports betting odds API, game predictions API, fantasy sports API, box score API, play-by-play API, injuries API, sports schedule API, standings API, ESPN data API, sports data JSON REST API.</sub>
