# Sports API: full endpoint reference (932 endpoints)

> Every endpoint of the **Sports Information API** on RapidAPI, grouped by sport. **[Get a free API key on RapidAPI →](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information)**  
> Back to the [README](README.md) · Support on Telegram: [@pintoflow](https://t.me/pintoflow)

Base URL: `https://sports-information.p.rapidapi.com` · `:id` = path parameter · **bold** parameters are required.

41 sports, 932 endpoints. **Bold** parameters are required.

- **US & Canada pro leagues:** [NBA](#nba) · [WNBA](#wnba) · [NBA G League](#nba-g-league) · [NFL](#nfl) · [CFL](#cfl) · [UFL](#ufl) · [MLB](#mlb) · [NHL](#nhl)
- **College:** [College Football](#college-football) · [Men's College Basketball](#mens-college-basketball) · [Women's College Basketball](#womens-college-basketball) · [College Baseball](#college-baseball) · [College Softball](#college-softball) · [Men's College Hockey](#mens-college-hockey) · [Women's College Hockey](#womens-college-hockey) · [Men's College Volleyball](#mens-college-volleyball) · [Women's College Volleyball](#womens-college-volleyball) · [Women's College Field Hockey](#womens-college-field-hockey) · [NCAA (all sports)](#ncaa-all-sports)
- **Soccer, rugby & other team sports:** [Soccer](#soccer) · [Rugby union](#rugby-union) · [NRL](#nrl) · [AFL](#afl) · [National Lacrosse League](#national-lacrosse-league) · [Premier Lacrosse League](#premier-lacrosse-league) · [FIBA Basketball World Cup](#fiba-basketball-world-cup) · [World Baseball Classic](#world-baseball-classic) · [Cricket](#cricket)
- **Tennis:** [Tennis](#tennis)
- **Motor racing:** [Formula 1](#formula-1) · [NASCAR Cup Series](#nascar-cup-series) · [IndyCar](#indycar)
- **Golf:** [PGA Tour](#pga-tour) · [LPGA Tour](#lpga-tour) · [LIV Golf](#liv-golf) · [DP World Tour](#dp-world-tour) · [PGA Tour Champions](#pga-tour-champions) · [Korn Ferry Tour](#korn-ferry-tour)
- **MMA:** [UFC](#ufc) · [Professional Fighters League](#professional-fighters-league) · [Bellator](#bellator)

### General

| Endpoint | Description | Parameters |
|---|---|---|
| `/` | API index. | – |
| `/health` | Liveness probe. | – |
| `/sports` | Every supported league and its base path. | – |
| `/endpoints` | Every endpoint with a short description. | sport |
| `/search` | Search players, teams, leagues and articles. | **query**, limit, page, type |
| `/today` | Every game today (or on `date`) across several leagues in one call. | leagues, date |
| `/live` | Every game in progress right now across several leagues. | leagues |

## US & Canada pro leagues

### NBA

Base path `/nba` · 36 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nba/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/nba/live` | Games currently in progress. | – |
| `/nba/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/nba/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/nba/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/nba/box-score/:id` | Team and player box score. | – |
| `/nba/play-by-play/:id` | Every play. | – |
| `/nba/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/nba/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/nba/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nba/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/nba/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/nba/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nba/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/nba/teams` | All teams with ids, names, colors and logos.<br>Also at: `/nba/team-list` | – |
| `/nba/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/nba/team-info/:id` | – |
| `/nba/teams/:id/roster` | Team roster.<br>Also at: `/nba/team-players/:id`, `/nba/team-roster?teamId=` | season |
| `/nba/teams/:id/schedule` | Team schedule and results.<br>Also at: `/nba/schedule-team?teamId=` | season, seasontype |
| `/nba/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/nba/team-statistics?teamId=`, `/nba/team-statistic?teamId=` | season, seasontype |
| `/nba/teams/:id/injuries` | Injury report for one team. | – |
| `/nba/teams/:id/depth-chart` | Depth chart by formation and position. | – |
| `/nba/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/nba/team-form?teamId=` | last, season |
| `/nba/teams/:id/news` | News about one team. | limit |
| `/nba/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nba/news` | Latest news. | limit |
| `/nba/injuries` | Injury report for every team. | raw |
| `/nba/transactions` | Signings, trades, waivers and other roster moves. | limit, page |
| `/nba/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/nba/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |
| `/nba/power-index` | ESPN power index team ratings (BPI / FPI). | season |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nba/players/:id` | Player profile with season stats summary. | – |
| `/nba/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/nba/players/:id/stats` | Career and season statistics.<br>Also at: `/nba/player-statistic2?playerId=` | season, seasontype |
| `/nba/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/nba/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/nba/player-splits?playerId=` | season, seasontype |
| `/nba/player-statistics` | Player statistics document (v1 format).<br>Also at: `/nba/player-statistic` | **playerId** |

### WNBA

Base path `/wnba` · 34 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wnba/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/wnba/live` | Games currently in progress. | – |
| `/wnba/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/wnba/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/wnba/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/wnba/box-score/:id` | Team and player box score. | – |
| `/wnba/play-by-play/:id` | Every play. | – |
| `/wnba/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/wnba/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/wnba/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wnba/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/wnba/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/wnba/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wnba/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/wnba/teams` | All teams with ids, names, colors and logos.<br>Also at: `/wnba/team-list` | – |
| `/wnba/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/wnba/team-info/:id` | – |
| `/wnba/teams/:id/roster` | Team roster.<br>Also at: `/wnba/team-players/:id`, `/wnba/team-roster?teamId=` | season |
| `/wnba/teams/:id/schedule` | Team schedule and results.<br>Also at: `/wnba/schedule-team?teamId=` | season, seasontype |
| `/wnba/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/wnba/team-statistics?teamId=`, `/wnba/team-statistic?teamId=` | season, seasontype |
| `/wnba/teams/:id/injuries` | Injury report for one team. | – |
| `/wnba/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/wnba/team-form?teamId=` | last, season |
| `/wnba/teams/:id/news` | News about one team. | limit |
| `/wnba/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wnba/news` | Latest news. | limit |
| `/wnba/injuries` | Injury report for every team. | raw |
| `/wnba/transactions` | Signings, trades, waivers and other roster moves. | limit, page |
| `/wnba/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/wnba/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wnba/players/:id` | Player profile with season stats summary. | – |
| `/wnba/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/wnba/players/:id/stats` | Career and season statistics.<br>Also at: `/wnba/player-statistic2?playerId=` | season, seasontype |
| `/wnba/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/wnba/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/wnba/player-splits?playerId=` | season, seasontype |
| `/wnba/player-statistics` | Player statistics document (v1 format).<br>Also at: `/wnba/player-statistic` | **playerId** |

### NBA G League

Base path `/g-league` · 30 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/g-league/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/g-league/live` | Games currently in progress. | – |
| `/g-league/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/g-league/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/g-league/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/g-league/box-score/:id` | Team and player box score. | – |
| `/g-league/play-by-play/:id` | Every play. | – |
| `/g-league/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/g-league/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/g-league/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/g-league/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/g-league/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/g-league/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/g-league/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/g-league/teams` | All teams with ids, names, colors and logos. | – |
| `/g-league/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/g-league/teams/:id/roster` | Team roster. | season |
| `/g-league/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/g-league/teams/:id/injuries` | Injury report for one team. | – |
| `/g-league/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/g-league/teams/:id/news` | News about one team. | limit |
| `/g-league/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/g-league/news` | Latest news. | limit |
| `/g-league/injuries` | Injury report for every team. | raw |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/g-league/players/:id` | Player profile with season stats summary. | – |
| `/g-league/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/g-league/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/g-league/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/g-league/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/g-league/player-statistics` | Player statistics document (v1 format). | **playerId** |

### NFL

Base path `/nfl` · 36 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nfl/scoreboard` | Scores and games for a day, a date range or a week (default: today). | date, from, to, week, year, seasontype, limit, raw |
| `/nfl/live` | Games currently in progress. | – |
| `/nfl/schedule` | Games grouped by day for a date, a date range (max 14 days) or a week.<br>Also at: `/nfl/weekly-schedule` | date, from, to, week, year, seasontype, limit |
| `/nfl/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/nfl/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/nfl/box-score/:id` | Team and player box score. | – |
| `/nfl/play-by-play/:id` | Every play, grouped in drives, plus scoring plays. | – |
| `/nfl/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/nfl/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/nfl/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nfl/predictions` | Predictions for every game of a day or week, with accuracy on games already finished. | date, from, to, week, year, seasontype, limit |
| `/nfl/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/nfl/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nfl/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/nfl/teams` | All teams with ids, names, colors and logos.<br>Also at: `/nfl/team-list` | – |
| `/nfl/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/nfl/team-info/:id` | – |
| `/nfl/teams/:id/roster` | Team roster.<br>Also at: `/nfl/team-players/:id`, `/nfl/team-roster?teamId=` | season |
| `/nfl/teams/:id/schedule` | Team schedule and results.<br>Also at: `/nfl/schedule-team?teamId=` | season, seasontype |
| `/nfl/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/nfl/team-statistics?teamId=`, `/nfl/team-statistic?teamId=` | season, seasontype |
| `/nfl/teams/:id/injuries` | Injury report for one team. | – |
| `/nfl/teams/:id/depth-chart` | Depth chart by formation and position. | – |
| `/nfl/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/nfl/team-form?teamId=` | last, season |
| `/nfl/teams/:id/news` | News about one team. | limit |
| `/nfl/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nfl/news` | Latest news. | limit |
| `/nfl/injuries` | Injury report for every team. | raw |
| `/nfl/transactions` | Signings, trades, waivers and other roster moves. | limit, page |
| `/nfl/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/nfl/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |
| `/nfl/power-index` | ESPN power index team ratings (BPI / FPI). | season |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nfl/players/:id` | Player profile with season stats summary. | – |
| `/nfl/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/nfl/players/:id/stats` | Career and season statistics.<br>Also at: `/nfl/player-statistic2?playerId=` | season, seasontype |
| `/nfl/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/nfl/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/nfl/player-splits?playerId=` | season, seasontype |
| `/nfl/player-statistics` | Player statistics document (v1 format).<br>Also at: `/nfl/player-statistic` | **playerId** |

### CFL

Base path `/cfl` · 30 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfl/scoreboard` | Scores and games for a day, a date range or a week (default: today). | date, from, to, week, year, seasontype, limit, raw |
| `/cfl/live` | Games currently in progress. | – |
| `/cfl/schedule` | Games grouped by day for a date, a date range (max 14 days) or a week. | date, from, to, week, year, seasontype, limit |
| `/cfl/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/cfl/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/cfl/box-score/:id` | Team and player box score. | – |
| `/cfl/play-by-play/:id` | Every play, grouped in drives, plus scoring plays. | – |
| `/cfl/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/cfl/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/cfl/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfl/predictions` | Predictions for every game of a day or week, with accuracy on games already finished. | date, from, to, week, year, seasontype, limit |
| `/cfl/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/cfl/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfl/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/cfl/teams` | All teams with ids, names, colors and logos. | – |
| `/cfl/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/cfl/teams/:id/roster` | Team roster. | season |
| `/cfl/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/cfl/teams/:id/injuries` | Injury report for one team. | – |
| `/cfl/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/cfl/teams/:id/news` | News about one team. | limit |
| `/cfl/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfl/news` | Latest news. | limit |
| `/cfl/injuries` | Injury report for every team. | raw |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfl/players/:id` | Player profile with season stats summary. | – |
| `/cfl/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/cfl/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/cfl/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/cfl/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/cfl/player-statistics` | Player statistics document (v1 format). | **playerId** |

### UFL

Base path `/ufl` · 30 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufl/scoreboard` | Scores and games for a day, a date range or a week (default: today). | date, from, to, week, year, seasontype, limit, raw |
| `/ufl/live` | Games currently in progress. | – |
| `/ufl/schedule` | Games grouped by day for a date, a date range (max 14 days) or a week. | date, from, to, week, year, seasontype, limit |
| `/ufl/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/ufl/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/ufl/box-score/:id` | Team and player box score. | – |
| `/ufl/play-by-play/:id` | Every play, grouped in drives, plus scoring plays. | – |
| `/ufl/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/ufl/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/ufl/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufl/predictions` | Predictions for every game of a day or week, with accuracy on games already finished. | date, from, to, week, year, seasontype, limit |
| `/ufl/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/ufl/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufl/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/ufl/teams` | All teams with ids, names, colors and logos. | – |
| `/ufl/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/ufl/teams/:id/roster` | Team roster. | season |
| `/ufl/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/ufl/teams/:id/injuries` | Injury report for one team. | – |
| `/ufl/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/ufl/teams/:id/news` | News about one team. | limit |
| `/ufl/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufl/news` | Latest news. | limit |
| `/ufl/injuries` | Injury report for every team. | raw |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufl/players/:id` | Player profile with season stats summary. | – |
| `/ufl/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/ufl/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/ufl/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/ufl/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/ufl/player-statistics` | Player statistics document (v1 format). | **playerId** |

### MLB

Base path `/mlb` · 35 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mlb/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/mlb/live` | Games currently in progress. | – |
| `/mlb/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/mlb/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/mlb/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/mlb/box-score/:id` | Team and player box score. | – |
| `/mlb/play-by-play/:id` | Every play. | – |
| `/mlb/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/mlb/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/mlb/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mlb/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/mlb/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/mlb/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mlb/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/mlb/teams` | All teams with ids, names, colors and logos.<br>Also at: `/mlb/team-list` | – |
| `/mlb/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/mlb/team-info/:id` | – |
| `/mlb/teams/:id/roster` | Team roster.<br>Also at: `/mlb/team-players/:id`, `/mlb/team-roster?teamId=` | season |
| `/mlb/teams/:id/schedule` | Team schedule and results.<br>Also at: `/mlb/schedule-team?teamId=` | season, seasontype |
| `/mlb/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/mlb/team-statistics?teamId=`, `/mlb/team-statistic?teamId=` | season, seasontype |
| `/mlb/teams/:id/injuries` | Injury report for one team. | – |
| `/mlb/teams/:id/depth-chart` | Depth chart by formation and position. | – |
| `/mlb/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/mlb/team-form?teamId=` | last, season |
| `/mlb/teams/:id/news` | News about one team. | limit |
| `/mlb/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mlb/news` | Latest news. | limit |
| `/mlb/injuries` | Injury report for every team. | raw |
| `/mlb/transactions` | Signings, trades, waivers and other roster moves. | limit, page |
| `/mlb/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/mlb/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mlb/players/:id` | Player profile with season stats summary. | – |
| `/mlb/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/mlb/players/:id/stats` | Career and season statistics.<br>Also at: `/mlb/player-statistic2?playerId=` | season, seasontype |
| `/mlb/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/mlb/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/mlb/player-splits?playerId=` | season, seasontype |
| `/mlb/player-statistics` | Player statistics document (v1 format).<br>Also at: `/mlb/player-statistic` | **playerId** |

### NHL

Base path `/nhl` · 34 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nhl/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/nhl/live` | Games currently in progress. | – |
| `/nhl/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/nhl/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/nhl/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/nhl/box-score/:id` | Team and player box score. | – |
| `/nhl/play-by-play/:id` | Every play. | – |
| `/nhl/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/nhl/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/nhl/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nhl/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/nhl/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/nhl/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nhl/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/nhl/teams` | All teams with ids, names, colors and logos.<br>Also at: `/nhl/team-list` | – |
| `/nhl/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/nhl/team-info/:id` | – |
| `/nhl/teams/:id/roster` | Team roster.<br>Also at: `/nhl/team-players/:id`, `/nhl/team-roster?teamId=` | season |
| `/nhl/teams/:id/schedule` | Team schedule and results.<br>Also at: `/nhl/schedule-team?teamId=` | season, seasontype |
| `/nhl/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/nhl/team-statistics?teamId=`, `/nhl/team-statistic?teamId=` | season, seasontype |
| `/nhl/teams/:id/injuries` | Injury report for one team. | – |
| `/nhl/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/nhl/team-form?teamId=` | last, season |
| `/nhl/teams/:id/news` | News about one team. | limit |
| `/nhl/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nhl/news` | Latest news. | limit |
| `/nhl/injuries` | Injury report for every team. | raw |
| `/nhl/transactions` | Signings, trades, waivers and other roster moves. | limit, page |
| `/nhl/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/nhl/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nhl/players/:id` | Player profile with season stats summary. | – |
| `/nhl/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/nhl/players/:id/stats` | Career and season statistics.<br>Also at: `/nhl/player-statistic2?playerId=` | season, seasontype |
| `/nhl/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/nhl/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/nhl/player-splits?playerId=` | season, seasontype |
| `/nhl/player-statistics` | Player statistics document (v1 format).<br>Also at: `/nhl/player-statistic` | **playerId** |

## College

### College Football

Base path `/cfb` · 39 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/scoreboard` | Scores and games for a day, a date range or a week (default: today). | date, from, to, week, year, seasontype, groups, limit, raw |
| `/cfb/live` | Games currently in progress. | groups |
| `/cfb/schedule` | Games grouped by day for a date, a date range (max 14 days) or a week.<br>Also at: `/cfb/weekly-schedule` | date, from, to, week, year, seasontype, groups, limit |
| `/cfb/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/cfb/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/cfb/box-score/:id` | Team and player box score. | – |
| `/cfb/play-by-play/:id` | Every play, grouped in drives, plus scoring plays. | – |
| `/cfb/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/cfb/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/cfb/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/predictions` | Predictions for every game of a day or week, with accuracy on games already finished. | date, from, to, week, year, seasontype, groups, limit |
| `/cfb/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/cfb/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/cfb/teams` | All teams with ids, names, colors and logos.<br>Also at: `/cfb/team-list` | groups |
| `/cfb/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/cfb/team-info/:id` | – |
| `/cfb/teams/:id/roster` | Team roster.<br>Also at: `/cfb/team-players/:id`, `/cfb/team-roster?teamId=` | season |
| `/cfb/teams/:id/schedule` | Team schedule and results.<br>Also at: `/cfb/schedule-team?teamId=` | season, seasontype |
| `/cfb/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/cfb/team-statistics?teamId=`, `/cfb/team-statistic?teamId=` | season, seasontype |
| `/cfb/teams/:id/injuries` | Injury report for one team. | – |
| `/cfb/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/cfb/team-form?teamId=` | last, season |
| `/cfb/teams/:id/news` | News about one team. | limit |
| `/cfb/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/news` | Latest news. | limit |
| `/cfb/injuries` | Injury report for every team. | raw |
| `/cfb/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/cfb/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |
| `/cfb/power-index` | ESPN power index team ratings (BPI / FPI). | season |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/players/:id` | Player profile with season stats summary. | – |
| `/cfb/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/cfb/players/:id/stats` | Career and season statistics.<br>Also at: `/cfb/player-statistic2?playerId=` | season, seasontype |
| `/cfb/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/cfb/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/cfb/player-splits?playerId=` | season, seasontype |
| `/cfb/player-statistics` | Player statistics document (v1 format).<br>Also at: `/cfb/player-statistic` | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/cfb/conferences` | Divisions and conferences with group ids and teams.<br>Also at: `/cfb/groups` | – |

**Recruiting**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cfb/player-rankings` | 247Sports composite recruit rankings (50 per page). | **year**, page, position, state, institution |
| `/cfb/school-rankings` | 247Sports team recruiting class rankings. | **year**, page |
| `/cfb/school-commits` | A school's commitments for a recruiting class. | **school**, **year** |

### Men's College Basketball

Base path `/mbb` · 39 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/mbb/live` | Games currently in progress. | groups |
| `/mbb/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/mbb/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/mbb/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/mbb/box-score/:id` | Team and player box score. | – |
| `/mbb/play-by-play/:id` | Every play. | – |
| `/mbb/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/mbb/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/mbb/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/mbb/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/mbb/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/mbb/teams` | All teams with ids, names, colors and logos.<br>Also at: `/mbb/team-list` | groups |
| `/mbb/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/mbb/team-info/:id` | – |
| `/mbb/teams/:id/roster` | Team roster.<br>Also at: `/mbb/team-players/:id`, `/mbb/team-roster?teamId=` | season |
| `/mbb/teams/:id/schedule` | Team schedule and results.<br>Also at: `/mbb/schedule-team?teamId=` | season, seasontype |
| `/mbb/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/mbb/team-statistics?teamId=`, `/mbb/team-statistic?teamId=` | season, seasontype |
| `/mbb/teams/:id/injuries` | Injury report for one team. | – |
| `/mbb/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/mbb/team-form?teamId=` | last, season |
| `/mbb/teams/:id/news` | News about one team. | limit |
| `/mbb/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/news` | Latest news. | limit |
| `/mbb/injuries` | Injury report for every team. | raw |
| `/mbb/leaders` | Statistical leaders by category. | season, seasontype, limit |
| `/mbb/futures` | Futures markets (championship, MVP...) with implied probabilities. | season, limit |
| `/mbb/power-index` | ESPN power index team ratings (BPI / FPI). | season |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/players/:id` | Player profile with season stats summary. | – |
| `/mbb/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/mbb/players/:id/stats` | Career and season statistics.<br>Also at: `/mbb/player-statistic2?playerId=` | season, seasontype |
| `/mbb/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/mbb/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/mbb/player-splits?playerId=` | season, seasontype |
| `/mbb/player-statistics` | Player statistics document (v1 format).<br>Also at: `/mbb/player-statistic` | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/mbb/conferences` | Divisions and conferences with group ids and teams.<br>Also at: `/mbb/groups` | – |

**Recruiting**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mbb/player-rankings` | 247Sports composite recruit rankings (50 per page). | **year**, page, position, state, institution |
| `/mbb/school-rankings` | 247Sports team recruiting class rankings. | **year**, page |
| `/mbb/school-commits` | A school's commitments for a recruiting class. | **school**, **year** |

### Women's College Basketball

Base path `/wbb` · 34 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wbb/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/wbb/live` | Games currently in progress. | groups |
| `/wbb/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/wbb/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/wbb/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/wbb/box-score/:id` | Team and player box score. | – |
| `/wbb/play-by-play/:id` | Every play. | – |
| `/wbb/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/wbb/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/wbb/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wbb/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/wbb/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/wbb/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wbb/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/wbb/teams` | All teams with ids, names, colors and logos.<br>Also at: `/wbb/team-list` | groups |
| `/wbb/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/wbb/team-info/:id` | – |
| `/wbb/teams/:id/roster` | Team roster.<br>Also at: `/wbb/team-players/:id`, `/wbb/team-roster?teamId=` | season |
| `/wbb/teams/:id/schedule` | Team schedule and results.<br>Also at: `/wbb/schedule-team?teamId=` | season, seasontype |
| `/wbb/teams/:id/statistics` | Team season statistics with league ranks.<br>Also at: `/wbb/team-statistics?teamId=`, `/wbb/team-statistic?teamId=` | season, seasontype |
| `/wbb/teams/:id/injuries` | Injury report for one team. | – |
| `/wbb/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/wbb/team-form?teamId=` | last, season |
| `/wbb/teams/:id/news` | News about one team. | limit |
| `/wbb/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wbb/news` | Latest news. | limit |
| `/wbb/injuries` | Injury report for every team. | raw |
| `/wbb/leaders` | Statistical leaders by category. | season, seasontype, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wbb/players/:id` | Player profile with season stats summary. | – |
| `/wbb/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/wbb/players/:id/stats` | Career and season statistics.<br>Also at: `/wbb/player-statistic2?playerId=` | season, seasontype |
| `/wbb/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/wbb/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/wbb/player-splits?playerId=` | season, seasontype |
| `/wbb/player-statistics` | Player statistics document (v1 format).<br>Also at: `/wbb/player-statistic` | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/wbb/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/wbb/conferences` | Divisions and conferences with group ids and teams.<br>Also at: `/wbb/groups` | – |

### College Baseball

Base path `/college-baseball` · 29 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-baseball/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/college-baseball/live` | Games currently in progress. | groups |
| `/college-baseball/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/college-baseball/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/college-baseball/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/college-baseball/box-score/:id` | Team and player box score. | – |
| `/college-baseball/play-by-play/:id` | Every play. | – |
| `/college-baseball/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/college-baseball/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/college-baseball/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-baseball/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/college-baseball/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/college-baseball/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-baseball/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/college-baseball/teams` | All teams with ids, names, colors and logos. | groups |
| `/college-baseball/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/college-baseball/teams/:id/roster` | Team roster. | season |
| `/college-baseball/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/college-baseball/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/college-baseball/teams/:id/news` | News about one team. | limit |
| `/college-baseball/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-baseball/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-baseball/players/:id` | Player profile with season stats summary. | – |
| `/college-baseball/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/college-baseball/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/college-baseball/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/college-baseball/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/college-baseball/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-baseball/conferences` | Divisions and conferences with group ids and teams. | – |

### College Softball

Base path `/college-softball` · 29 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-softball/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/college-softball/live` | Games currently in progress. | groups |
| `/college-softball/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/college-softball/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/college-softball/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/college-softball/box-score/:id` | Team and player box score. | – |
| `/college-softball/play-by-play/:id` | Every play. | – |
| `/college-softball/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/college-softball/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/college-softball/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-softball/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/college-softball/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/college-softball/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-softball/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/college-softball/teams` | All teams with ids, names, colors and logos. | groups |
| `/college-softball/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/college-softball/teams/:id/roster` | Team roster. | season |
| `/college-softball/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/college-softball/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/college-softball/teams/:id/news` | News about one team. | limit |
| `/college-softball/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-softball/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-softball/players/:id` | Player profile with season stats summary. | – |
| `/college-softball/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/college-softball/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/college-softball/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/college-softball/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/college-softball/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-softball/conferences` | Divisions and conferences with group ids and teams. | – |

### Men's College Hockey

Base path `/mens-college-hockey` · 32 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-hockey/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/mens-college-hockey/live` | Games currently in progress. | groups |
| `/mens-college-hockey/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/mens-college-hockey/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/mens-college-hockey/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/mens-college-hockey/box-score/:id` | Team and player box score. | – |
| `/mens-college-hockey/play-by-play/:id` | Every play. | – |
| `/mens-college-hockey/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/mens-college-hockey/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/mens-college-hockey/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-hockey/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/mens-college-hockey/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/mens-college-hockey/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-hockey/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/mens-college-hockey/teams` | All teams with ids, names, colors and logos. | groups |
| `/mens-college-hockey/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/mens-college-hockey/teams/:id/roster` | Team roster. | season |
| `/mens-college-hockey/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/mens-college-hockey/teams/:id/injuries` | Injury report for one team. | – |
| `/mens-college-hockey/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/mens-college-hockey/teams/:id/news` | News about one team. | limit |
| `/mens-college-hockey/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-hockey/news` | Latest news. | limit |
| `/mens-college-hockey/injuries` | Injury report for every team. | raw |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-hockey/players/:id` | Player profile with season stats summary. | – |
| `/mens-college-hockey/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/mens-college-hockey/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/mens-college-hockey/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/mens-college-hockey/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/mens-college-hockey/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-hockey/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/mens-college-hockey/conferences` | Divisions and conferences with group ids and teams. | – |

### Women's College Hockey

Base path `/womens-college-hockey` · 32 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-hockey/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/womens-college-hockey/live` | Games currently in progress. | groups |
| `/womens-college-hockey/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/womens-college-hockey/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/womens-college-hockey/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/womens-college-hockey/box-score/:id` | Team and player box score. | – |
| `/womens-college-hockey/play-by-play/:id` | Every play. | – |
| `/womens-college-hockey/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/womens-college-hockey/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/womens-college-hockey/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-hockey/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/womens-college-hockey/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/womens-college-hockey/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-hockey/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/womens-college-hockey/teams` | All teams with ids, names, colors and logos. | groups |
| `/womens-college-hockey/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/womens-college-hockey/teams/:id/roster` | Team roster. | season |
| `/womens-college-hockey/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/womens-college-hockey/teams/:id/injuries` | Injury report for one team. | – |
| `/womens-college-hockey/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/womens-college-hockey/teams/:id/news` | News about one team. | limit |
| `/womens-college-hockey/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-hockey/news` | Latest news. | limit |
| `/womens-college-hockey/injuries` | Injury report for every team. | raw |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-hockey/players/:id` | Player profile with season stats summary. | – |
| `/womens-college-hockey/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/womens-college-hockey/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/womens-college-hockey/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/womens-college-hockey/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/womens-college-hockey/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-hockey/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/womens-college-hockey/conferences` | Divisions and conferences with group ids and teams. | – |

### Men's College Volleyball

Base path `/mens-college-volleyball` · 30 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-volleyball/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/mens-college-volleyball/live` | Games currently in progress. | groups |
| `/mens-college-volleyball/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/mens-college-volleyball/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/mens-college-volleyball/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/mens-college-volleyball/box-score/:id` | Team and player box score. | – |
| `/mens-college-volleyball/play-by-play/:id` | Every play. | – |
| `/mens-college-volleyball/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/mens-college-volleyball/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/mens-college-volleyball/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-volleyball/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/mens-college-volleyball/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/mens-college-volleyball/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-volleyball/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/mens-college-volleyball/teams` | All teams with ids, names, colors and logos. | groups |
| `/mens-college-volleyball/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/mens-college-volleyball/teams/:id/roster` | Team roster. | season |
| `/mens-college-volleyball/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/mens-college-volleyball/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/mens-college-volleyball/teams/:id/news` | News about one team. | limit |
| `/mens-college-volleyball/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-volleyball/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-volleyball/players/:id` | Player profile with season stats summary. | – |
| `/mens-college-volleyball/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/mens-college-volleyball/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/mens-college-volleyball/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/mens-college-volleyball/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/mens-college-volleyball/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/mens-college-volleyball/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/mens-college-volleyball/conferences` | Divisions and conferences with group ids and teams. | – |

### Women's College Volleyball

Base path `/womens-college-volleyball` · 30 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-volleyball/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/womens-college-volleyball/live` | Games currently in progress. | groups |
| `/womens-college-volleyball/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/womens-college-volleyball/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/womens-college-volleyball/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/womens-college-volleyball/box-score/:id` | Team and player box score. | – |
| `/womens-college-volleyball/play-by-play/:id` | Every play. | – |
| `/womens-college-volleyball/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/womens-college-volleyball/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/womens-college-volleyball/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-volleyball/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/womens-college-volleyball/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/womens-college-volleyball/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-volleyball/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/womens-college-volleyball/teams` | All teams with ids, names, colors and logos. | groups |
| `/womens-college-volleyball/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/womens-college-volleyball/teams/:id/roster` | Team roster. | season |
| `/womens-college-volleyball/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/womens-college-volleyball/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/womens-college-volleyball/teams/:id/news` | News about one team. | limit |
| `/womens-college-volleyball/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-volleyball/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-volleyball/players/:id` | Player profile with season stats summary. | – |
| `/womens-college-volleyball/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/womens-college-volleyball/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/womens-college-volleyball/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/womens-college-volleyball/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/womens-college-volleyball/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/womens-college-volleyball/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/womens-college-volleyball/conferences` | Divisions and conferences with group ids and teams. | – |

### Women's College Field Hockey

Base path `/college-field-hockey` · 29 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-field-hockey/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, groups, limit, raw |
| `/college-field-hockey/live` | Games currently in progress. | groups |
| `/college-field-hockey/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, groups, limit |
| `/college-field-hockey/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/college-field-hockey/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/college-field-hockey/box-score/:id` | Team and player box score. | – |
| `/college-field-hockey/play-by-play/:id` | Every play. | – |
| `/college-field-hockey/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/college-field-hockey/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/college-field-hockey/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-field-hockey/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, groups, limit |
| `/college-field-hockey/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/college-field-hockey/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-field-hockey/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/college-field-hockey/teams` | All teams with ids, names, colors and logos. | groups |
| `/college-field-hockey/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/college-field-hockey/teams/:id/roster` | Team roster. | season |
| `/college-field-hockey/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/college-field-hockey/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/college-field-hockey/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-field-hockey/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-field-hockey/players/:id` | Player profile with season stats summary. | – |
| `/college-field-hockey/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/college-field-hockey/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/college-field-hockey/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/college-field-hockey/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/college-field-hockey/player-statistics` | Player statistics document (v1 format). | **playerId** |

**College**

| Endpoint | Description | Parameters |
|---|---|---|
| `/college-field-hockey/rankings` | Polls (AP, Coaches, CFP...) with points and first-place votes. | year, week, seasontype |
| `/college-field-hockey/conferences` | Divisions and conferences with group ids and teams. | – |

### NCAA (all sports)

Base path `/ncaa` · 16 endpoints

**Reference**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ncaa/sports` | NCAA sports, their divisions and which have live scoreboards. | – |
| `/ncaa/divisions` | Divisions available for a sport. | **sport** |
| `/ncaa/news` | NCAA.com news for a sport. | **sport**, division |
| `/ncaa/schools` | Every NCAA school with its slug. | – |

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ncaa/scoreboard` | Scores for a day (football: a week). | **sport**, division, date, week, season |
| `/ncaa/weeks` | Weeks of a season with game counts and the current week. | **sport**, division, season |
| `/ncaa/game/:id` | Game details: teams, score, line score, status, venue, championship round, what is available.<br>Also at: `/ncaa/info/:game` | raw |
| `/ncaa/game/:id/box-score` | Box score: team totals and every player, home and away.<br>Also at: `/ncaa/box-score/:gameId` | raw |
| `/ncaa/game/:id/play-by-play` | Play-by-play by period, with clock, team, score and (football) drive situation.<br>Also at: `/ncaa/play-by-play/:gameId` | raw |
| `/ncaa/game/:id/team-stats` | Team stats comparison.<br>Also at: `/ncaa/team-stats/:gameId` | raw |
| `/ncaa/game/:id/scoring-summary` | Scoring summary.<br>Also at: `/ncaa/scoring-summary/:game` | raw |
| `/ncaa/schedule` | Season schedule: every game day (football: week) with its game count. | **sport**, division, season |

**Rankings, standings & stats**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ncaa/rankings` | Polls / rankings (default AP where available). | **sport**, division, poll |
| `/ncaa/standings` | Conference standings. | **sport**, division |
| `/ncaa/history` | Championship history (champions, runners-up, scores). | **sport**, division |
| `/ncaa/stats` | Without category: the list of stat categories. With category: the leaderboard. | **sport**, division, type, category, page |

## Soccer, rugby & other team sports

### Soccer

Base path `/soccer` · 35 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/soccer/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, league, raw |
| `/soccer/live` | Games currently in progress. | league |
| `/soccer/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit, league |
| `/soccer/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype, league |
| `/soccer/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | league |
| `/soccer/box-score/:id` | Team and player box score. | league |
| `/soccer/play-by-play/:id` | Key events and commentary. | league |
| `/soccer/win-probability/:id` | Pre-game and play-by-play win probability. | league |
| `/soccer/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | league |
| `/soccer/picks/:id` | Pick center (v1 format). | league |
| `/soccer/match-summary/:id` | Match summary (v1 name of /soccer/summary/:id). | league |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/soccer/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit, league |
| `/soccer/predictions/:id` | One match: home / draw / away, expected goals, most likely score, over 2.5, both teams to score. | league |
| `/soccer/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral, league |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/soccer/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw, league |
| `/soccer/teams` | All teams with ids, names, colors and logos.<br>Also at: `/soccer/team-list` | league |
| `/soccer/teams/:id` | Team details: record, standing summary, venue, next game.<br>Also at: `/soccer/team-info/:id` | league |
| `/soccer/teams/:id/roster` | Team roster.<br>Also at: `/soccer/team-players/:id`, `/soccer/team-roster?teamId=` | season, league |
| `/soccer/teams/:id/schedule` | Team schedule and results.<br>Also at: `/soccer/schedule-team?teamId=` | season, seasontype, league |
| `/soccer/teams/:id/injuries` | Injury report for one team. | league |
| `/soccer/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game.<br>Also at: `/soccer/team-form?teamId=` | last, season, league |
| `/soccer/teams/:id/news` | News about one team. | limit, league |
| `/soccer/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons, league |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/soccer/news` | Latest news. | limit, league |
| `/soccer/injuries` | Injury report for every team. | raw, league |
| `/soccer/leaders` | Top scorers, assists and other leaders. | season, seasontype, limit, league |
| `/soccer/transfers` | Transfers in and out (league=all for every league). | league, year, limit, page |
| `/soccer/league-stats` | Top scorers, assists and other league leaders. | league, season |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/soccer/players/:id` | Player profile with season stats summary. | league |
| `/soccer/players/:id/overview` | Player overview: stats, recent games, news. | league |
| `/soccer/players/:id/stats` | Career and season statistics.<br>Also at: `/soccer/player-statistic2?playerId=` | season, seasontype, league |
| `/soccer/players/:id/gamelog` | Game-by-game log. | season, seasontype, league |
| `/soccer/players/:id/splits` | Statistical splits (home/away, by month, by opponent...).<br>Also at: `/soccer/player-splits?playerId=` | season, seasontype, league |
| `/soccer/player-statistics` | Player statistics document (v1 format).<br>Also at: `/soccer/player-statistic` | **playerId**, league |

**Competitions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/soccer/leagues` | Supported soccer competitions and their ids.<br>Also at: `/soccer/leagueIds` | – |

### Rugby union

Base path `/rugby` · 29 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/rugby/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, league, raw |
| `/rugby/live` | Games currently in progress. | league |
| `/rugby/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit, league |
| `/rugby/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype, league |
| `/rugby/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | league |
| `/rugby/box-score/:id` | Team and player box score. | league |
| `/rugby/play-by-play/:id` | Key events and commentary. | league |
| `/rugby/win-probability/:id` | Pre-game and play-by-play win probability. | league |
| `/rugby/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | league |
| `/rugby/picks/:id` | Pick center (v1 format). | league |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/rugby/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit, league |
| `/rugby/predictions/:id` | One match: home / draw / away, expected goals, most likely score, over 2.5, both teams to score. | league |
| `/rugby/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral, league |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/rugby/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw, league |
| `/rugby/teams` | All teams with ids, names, colors and logos. | league |
| `/rugby/teams/:id` | Team details: record, standing summary, venue, next game. | league |
| `/rugby/teams/:id/roster` | Team roster. | season, league |
| `/rugby/teams/:id/schedule` | Team schedule and results. | season, seasontype, league |
| `/rugby/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season, league |
| `/rugby/teams/:id/news` | News about one team. | limit, league |
| `/rugby/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons, league |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/rugby/news` | Latest news. | limit, league |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/rugby/players/:id` | Player profile with season stats summary. | league |
| `/rugby/players/:id/overview` | Player overview: stats, recent games, news. | league |
| `/rugby/players/:id/stats` | Career and season statistics. | season, seasontype, league |
| `/rugby/players/:id/gamelog` | Game-by-game log. | season, seasontype, league |
| `/rugby/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype, league |
| `/rugby/player-statistics` | Player statistics document (v1 format). | **playerId**, league |

**Competitions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/rugby/leagues` | Supported rugby union competitions and their ids. | – |

### NRL

Base path `/nrl` · 29 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nrl/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/nrl/live` | Games currently in progress. | – |
| `/nrl/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/nrl/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/nrl/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/nrl/box-score/:id` | Team and player box score. | – |
| `/nrl/play-by-play/:id` | Every play. | – |
| `/nrl/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/nrl/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/nrl/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nrl/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/nrl/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/nrl/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nrl/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/nrl/teams` | All teams with ids, names, colors and logos. | – |
| `/nrl/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/nrl/teams/:id/roster` | Team roster. | season |
| `/nrl/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/nrl/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/nrl/teams/:id/news` | News about one team. | limit |
| `/nrl/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nrl/news` | Latest news. | limit |
| `/nrl/leaders` | Statistical leaders by category. | season, seasontype, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nrl/players/:id` | Player profile with season stats summary. | – |
| `/nrl/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/nrl/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/nrl/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/nrl/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/nrl/player-statistics` | Player statistics document (v1 format). | **playerId** |

### AFL

Base path `/afl` · 31 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/afl/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/afl/live` | Games currently in progress. | – |
| `/afl/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/afl/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/afl/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/afl/box-score/:id` | Team and player box score. | – |
| `/afl/play-by-play/:id` | Every play. | – |
| `/afl/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/afl/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/afl/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/afl/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/afl/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/afl/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/afl/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/afl/teams` | All teams with ids, names, colors and logos. | – |
| `/afl/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/afl/teams/:id/roster` | Team roster. | season |
| `/afl/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/afl/teams/:id/injuries` | Injury report for one team. | – |
| `/afl/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/afl/teams/:id/news` | News about one team. | limit |
| `/afl/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/afl/news` | Latest news. | limit |
| `/afl/injuries` | Injury report for every team. | raw |
| `/afl/leaders` | Statistical leaders by category. | season, seasontype, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/afl/players/:id` | Player profile with season stats summary. | – |
| `/afl/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/afl/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/afl/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/afl/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/afl/player-statistics` | Player statistics document (v1 format). | **playerId** |

### National Lacrosse League

Base path `/nll` · 28 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nll/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/nll/live` | Games currently in progress. | – |
| `/nll/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/nll/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/nll/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/nll/box-score/:id` | Team and player box score. | – |
| `/nll/play-by-play/:id` | Every play. | – |
| `/nll/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/nll/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/nll/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nll/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/nll/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/nll/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nll/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/nll/teams` | All teams with ids, names, colors and logos. | – |
| `/nll/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/nll/teams/:id/roster` | Team roster. | season |
| `/nll/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/nll/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/nll/teams/:id/news` | News about one team. | limit |
| `/nll/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nll/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nll/players/:id` | Player profile with season stats summary. | – |
| `/nll/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/nll/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/nll/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/nll/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/nll/player-statistics` | Player statistics document (v1 format). | **playerId** |

### Premier Lacrosse League

Base path `/pll` · 28 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pll/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/pll/live` | Games currently in progress. | – |
| `/pll/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/pll/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/pll/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/pll/box-score/:id` | Team and player box score. | – |
| `/pll/play-by-play/:id` | Every play. | – |
| `/pll/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/pll/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/pll/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pll/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/pll/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/pll/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pll/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/pll/teams` | All teams with ids, names, colors and logos. | – |
| `/pll/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/pll/teams/:id/roster` | Team roster. | season |
| `/pll/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/pll/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/pll/teams/:id/news` | News about one team. | limit |
| `/pll/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pll/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pll/players/:id` | Player profile with season stats summary. | – |
| `/pll/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/pll/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/pll/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/pll/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/pll/player-statistics` | Player statistics document (v1 format). | **playerId** |

### FIBA Basketball World Cup

Base path `/fiba` · 28 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/fiba/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/fiba/live` | Games currently in progress. | – |
| `/fiba/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/fiba/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/fiba/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/fiba/box-score/:id` | Team and player box score. | – |
| `/fiba/play-by-play/:id` | Every play. | – |
| `/fiba/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/fiba/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/fiba/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/fiba/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/fiba/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/fiba/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/fiba/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/fiba/teams` | All teams with ids, names, colors and logos. | – |
| `/fiba/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/fiba/teams/:id/roster` | Team roster. | season |
| `/fiba/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/fiba/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/fiba/teams/:id/news` | News about one team. | limit |
| `/fiba/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/fiba/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/fiba/players/:id` | Player profile with season stats summary. | – |
| `/fiba/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/fiba/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/fiba/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/fiba/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/fiba/player-statistics` | Player statistics document (v1 format). | **playerId** |

### World Baseball Classic

Base path `/world-baseball-classic` · 28 endpoints

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/world-baseball-classic/scoreboard` | Scores and games for a day or a date range (default: today). | date, from, to, seasontype, limit, raw |
| `/world-baseball-classic/live` | Games currently in progress. | – |
| `/world-baseball-classic/schedule` | Games grouped by day for a date or a date range (max 14 days). | date, from, to, seasontype, limit |
| `/world-baseball-classic/calendar` | Season calendar: phases, weeks or match days with start and end dates. | season, seasontype |
| `/world-baseball-classic/summary/:id` | Full game package: box score, leaders, odds, win probability, standings, news. | – |
| `/world-baseball-classic/box-score/:id` | Team and player box score. | – |
| `/world-baseball-classic/play-by-play/:id` | Every play. | – |
| `/world-baseball-classic/win-probability/:id` | Pre-game and play-by-play win probability. | – |
| `/world-baseball-classic/odds/:id` | Sportsbook lines with implied probabilities, against-the-spread records, ESPN predictor. | – |
| `/world-baseball-classic/picks/:id` | Pick center (v1 format). | – |

**Predictions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/world-baseball-classic/predictions` | Predictions for every game of a day, with accuracy on games already finished. | date, from, to, seasontype, limit |
| `/world-baseball-classic/predictions/:id` | One game: win probability, projected score, spread and total picks; live win probability while in progress. | – |
| `/world-baseball-classic/matchup` | Model prediction for any hypothetical matchup. | **home**, **away**, neutral |

**Standings & teams**

| Endpoint | Description | Parameters |
|---|---|---|
| `/world-baseball-classic/standings` | Standings with every stat (wins, losses, streak, points for/against...). | season, group, seasontype, raw |
| `/world-baseball-classic/teams` | All teams with ids, names, colors and logos. | – |
| `/world-baseball-classic/teams/:id` | Team details: record, standing summary, venue, next game. | – |
| `/world-baseball-classic/teams/:id/roster` | Team roster. | season |
| `/world-baseball-classic/teams/:id/schedule` | Team schedule and results. | season, seasontype |
| `/world-baseball-classic/teams/:id/form` | Recent form: last N results, streak, average scored and conceded, next game. | last, season |
| `/world-baseball-classic/teams/:id/news` | News about one team. | limit |
| `/world-baseball-classic/head-to-head` | Head-to-head results between two teams over recent seasons. | **team1**, **team2**, seasons |

**News & league**

| Endpoint | Description | Parameters |
|---|---|---|
| `/world-baseball-classic/news` | Latest news. | limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/world-baseball-classic/players/:id` | Player profile with season stats summary. | – |
| `/world-baseball-classic/players/:id/overview` | Player overview: stats, recent games, news. | – |
| `/world-baseball-classic/players/:id/stats` | Career and season statistics. | season, seasontype |
| `/world-baseball-classic/players/:id/gamelog` | Game-by-game log. | season, seasontype |
| `/world-baseball-classic/players/:id/splits` | Statistical splits (home/away, by month, by opponent...). | season, seasontype |
| `/world-baseball-classic/player-statistics` | Player statistics document (v1 format). | **playerId** |

### Cricket

Base path `/cricket` · 6 endpoints

**Competitions**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cricket/leagues` | Known cricket series ids (any numeric ESPN series id also works). | – |

**Games**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cricket/scoreboard` | Matches of a series for a day (default: current). Scores are text, e.g. "161/5 (18/20 ov)", in scoreDisplay. | league, date, raw |
| `/cricket/live` | Matches in progress. | league |
| `/cricket/summary/:id` | Full match package: innings, scorecard, commentary, match info. | league |

**Standings**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cricket/standings` | Points table. | league, season |

**News**

| Endpoint | Description | Parameters |
|---|---|---|
| `/cricket/news` | News. | league, limit |

## Tennis

### Tennis

Base path `/tennis` · 7 endpoints

**Matches**

| Endpoint | Description | Parameters |
|---|---|---|
| `/tennis/scoreboard` | Tournaments and matches for a day (default today). | league, date, grouping, state |
| `/tennis/live` | Matches in progress. | league, grouping |

**Rankings & schedule**

| Endpoint | Description | Parameters |
|---|---|---|
| `/tennis/rankings` | Current ATP / WTA singles rankings. | type |
| `/tennis/schedule` | Tournament calendar for a season. | year, type |

**News**

| Endpoint | Description | Parameters |
|---|---|---|
| `/tennis/news` | Tennis news. | league, limit |

**Players**

| Endpoint | Description | Parameters |
|---|---|---|
| `/tennis/players/:id` | Player profile.<br>Also at: `/tennis/player-profile?playerId=` | league |
| `/tennis/players/:id/results` | A player's tournaments for a season.<br>Also at: `/tennis/player-results?playerId=` | year, league |

## Motor racing

### Formula 1

Base path `/f1` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/f1/scoreboard` | Current race weekend sessions and results (or the one on `date`). | date |
| `/f1/events/:id` | One race weekend with every session. | – |
| `/f1/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/f1/standings` | Driver (and constructor) championship standings. | season |
| `/f1/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/f1/athletes/:id` | Driver profile. | – |

### NASCAR Cup Series

Base path `/nascar` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nascar/scoreboard` | Current race weekend sessions and results (or the one on `date`). | date |
| `/nascar/events/:id` | One race weekend with every session. | – |
| `/nascar/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nascar/standings` | Driver (and constructor) championship standings. | season |
| `/nascar/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/nascar/athletes/:id` | Driver profile. | – |

### IndyCar

Base path `/indycar` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/indycar/scoreboard` | Current race weekend sessions and results (or the one on `date`). | date |
| `/indycar/events/:id` | One race weekend with every session. | – |
| `/indycar/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/indycar/standings` | Driver (and constructor) championship standings. | season |
| `/indycar/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/indycar/athletes/:id` | Driver profile. | – |

## Golf

### PGA Tour

Base path `/pga` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pga/scoreboard` | Current tournament leaderboard (or the one on `date`). | date |
| `/pga/events/:id` | One tournament with its full leaderboard. | – |
| `/pga/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pga/standings` | Season standings. | season |
| `/pga/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pga/athletes/:id` | Player profile. | – |

### LPGA Tour

Base path `/lpga` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/lpga/scoreboard` | Current tournament leaderboard (or the one on `date`). | date |
| `/lpga/events/:id` | One tournament with its full leaderboard. | – |
| `/lpga/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/lpga/standings` | Season standings. | season |
| `/lpga/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/lpga/athletes/:id` | Player profile. | – |

### LIV Golf

Base path `/liv` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/liv/scoreboard` | Current tournament leaderboard (or the one on `date`). | date |
| `/liv/events/:id` | One tournament with its full leaderboard. | – |
| `/liv/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/liv/standings` | Season standings. | season |
| `/liv/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/liv/athletes/:id` | Player profile. | – |

### DP World Tour

Base path `/dp-world-tour` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/dp-world-tour/scoreboard` | Current tournament leaderboard (or the one on `date`). | date |
| `/dp-world-tour/events/:id` | One tournament with its full leaderboard. | – |
| `/dp-world-tour/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/dp-world-tour/standings` | Season standings. | season |
| `/dp-world-tour/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/dp-world-tour/athletes/:id` | Player profile. | – |

### PGA Tour Champions

Base path `/champions-tour` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/champions-tour/scoreboard` | Current tournament leaderboard (or the one on `date`). | date |
| `/champions-tour/events/:id` | One tournament with its full leaderboard. | – |
| `/champions-tour/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/champions-tour/standings` | Season standings. | season |
| `/champions-tour/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/champions-tour/athletes/:id` | Player profile. | – |

### Korn Ferry Tour

Base path `/korn-ferry` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/korn-ferry/scoreboard` | Current tournament leaderboard (or the one on `date`). | date |
| `/korn-ferry/events/:id` | One tournament with its full leaderboard. | – |
| `/korn-ferry/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/korn-ferry/standings` | Season standings. | season |
| `/korn-ferry/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/korn-ferry/athletes/:id` | Player profile. | – |

## MMA

### UFC

Base path `/ufc` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufc/scoreboard` | Fight card results (or the one on `date`). | date |
| `/ufc/events/:id` | One card with every bout. | – |
| `/ufc/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufc/standings` | Season standings. | season |
| `/ufc/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/ufc/athletes/:id` | Fighter profile. | – |

### Professional Fighters League

Base path `/pfl` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pfl/scoreboard` | Fight card results (or the one on `date`). | date |
| `/pfl/events/:id` | One card with every bout. | – |
| `/pfl/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pfl/standings` | Season standings. | season |
| `/pfl/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/pfl/athletes/:id` | Fighter profile. | – |

### Bellator

Base path `/bellator` · 6 endpoints

**Events**

| Endpoint | Description | Parameters |
|---|---|---|
| `/bellator/scoreboard` | Fight card results (or the one on `date`). | date |
| `/bellator/events/:id` | One card with every bout. | – |
| `/bellator/schedule` | Season calendar with event ids. | year |

**Standings & news**

| Endpoint | Description | Parameters |
|---|---|---|
| `/bellator/standings` | Season standings. | season |
| `/bellator/news` | Latest news. | limit |

**Athletes**

| Endpoint | Description | Parameters |
|---|---|---|
| `/bellator/athletes/:id` | Fighter profile. | – |
