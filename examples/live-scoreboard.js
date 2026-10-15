// Live scoreboard in your terminal, refreshed every 30 seconds.
// Sports API on RapidAPI: https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information
//
// Usage:  RAPIDAPI_KEY=your_key node live-scoreboard.js [sport]
//         sport = nba | nfl | mlb | nhl | wnba | cfb | mbb | soccer ... (default: nba)
// Requires Node.js 18+ (built-in fetch).

const SPORT = process.argv[2] || 'nba';
const HOST = 'sports-information.p.rapidapi.com';
const KEY = process.env.RAPIDAPI_KEY;
if (!KEY) {
  console.error('Set RAPIDAPI_KEY first. Get a key at https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information');
  process.exit(1);
}

async function api(path) {
  const res = await fetch(`https://${HOST}${path}`, {
    headers: { 'X-RapidAPI-Key': KEY, 'X-RapidAPI-Host': HOST },
  });
  const body = await res.json();
  if (!body.success) throw new Error(`${body.error?.code}: ${body.message}`);
  return body.data;
}

const games = (data) => (Array.isArray(data) ? data : data?.events ?? []);
const team = (side) => side?.team?.abbreviation || side?.team?.shortDisplayName || side?.team?.displayName || '?';

async function render() {
  const data = await api(`/${SPORT}/scoreboard`);
  console.clear();
  console.log(`${SPORT.toUpperCase()} scoreboard · ${new Date().toLocaleTimeString()}\n`);
  for (const g of games(data)) {
    const live = g.status?.state === 'in' ? '●' : ' ';
    console.log(
      `${live} ${team(g.away).padEnd(5)} ${String(g.away?.score ?? '-').padStart(3)}  @  ` +
      `${team(g.home).padEnd(5)} ${String(g.home?.score ?? '-').padStart(3)}   ${g.status?.detail ?? ''}`
    );
  }
}

render().catch(console.error);
setInterval(() => render().catch(console.error), 30_000); // live data refreshes about every 15 s
