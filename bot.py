import os
import asyncio
from datetime import datetime, date
from zoneinfo import ZoneInfo

import discord

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_ID"])

BASE_DATE = date(2026, 11, 3)
BASE_DAY = 281

async def main():
    today = datetime.now(ZoneInfo("Asia/Seoul")).date()
    day_count = BASE_DAY + (today - BASE_DATE).days

    client = discord.Client(intents=discord.Intents.none())

    async with client:
        await client.login(TOKEN)
        channel = await client.fetch_channel(CHANNEL_ID)
        await channel.send(f"노어게인 기원 {day_count}일차")

asyncio.run(main())
