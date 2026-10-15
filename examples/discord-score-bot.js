// Discord bot that posts final scores to a channel when games end.
// Sports API on RapidAPI: https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/sports-information
//
// Usage:
//   npm install discord.js
//   RAPIDAPI_KEY=... DISCORD_TOKEN=... CHANNEL_ID=... SPORTS=nba,nfl,nhl node discord-score-bot.js

const { Client, GatewayIntentBits } = require('discord.js');

const HOST = 'sports-information.p.rapidapi.com';
const SPORTS = (process.env.SPORTS || 'nba,nfl').split(',');
const posted = new Set();

async function scoreboard(sport) {
  const res = await fetch(`https://${HOST}/${sport}/scoreboard`, {
    headers: { 'X-RapidAPI-Key': process.env.RAPIDAPI_KEY, 'X-RapidAPI-Host': HOST },
  });
  const body = await res.json();
  if (!body.success) throw new Error(body.error?.code);
  return Array.isArray(body.data) ? body.data : body.data?.events ?? [];
}

const name = (s) => s?.team?.displayName || s?.team?.abbreviation || '?';

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

client.once('ready', async () => {
  const channel = await client.channels.fetch(process.env.CHANNEL_ID);
  const tick = async () => {
    for (const sport of SPORTS) {
      try {
        for (const g of await scoreboard(sport)) {
          if (g.status?.state !== 'post' || posted.has(g.id)) continue;
          posted.add(g.id);
          await channel.send(
            `🏁 **${sport.toUpperCase()} final:** ${name(g.away)} ${g.away?.score} – ${g.home?.score} ${name(g.home)}`
          );
        }
      } catch (e) {
        console.error(sport, e.message);
      }
    }
  };
  await tick();
  setInterval(tick, 60_000); // poll once a minute; scoreboards are cached ~15 s
});

client.login(process.env.DISCORD_TOKEN);
