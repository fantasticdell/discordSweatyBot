import os
import discord
import logging
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from sweatybot import config
from sweatybot import sweat

#define the discord frontend here, and run the discord.py client
#store config / data structures in config.py
#store application functions in sweat.py

# Set Discord API token
# this is stored in .env as SWEATY_BOT_DISCORD_TOKEN and should be set before any build
token = os.getenv("SWEATY_BOT_DISCORD_TOKEN")

if token is None:
    raise RuntimeError("SWEATY_BOT_DISCORD_TOKEN environment variable not set")
#end Set Discord API token

@bot.event 
async def on_ready():
        print ('Online as {0.user}'.format(bot))


bot = commands.Bot(command_prefix="!sweaty")

@bot.command()
async def test(ctx):
    await ctx.send("Test")

bot.run(token)