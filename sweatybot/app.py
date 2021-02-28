import os
import discord
#pip install -U discord.py
import logging
import asyncio
import sweatybot.sweat as sweat
import sweatybot.wl as wl
#pip install -U python-dotenv
from dotenv import load_dotenv


#define the discord frontend here, and run the discord.py client
#store config / data structures in config.py
#store application functions in sweat.py

#define logger
logger = logging.getLogger('discord')
#change this to warning later, or define a log file 
#https://discordpy.readthedocs.io/en/latest/logging.html
#logger.basicConfig(level=logging.INFO)

print("Sweaty Bot loading")

#Inherit expected config from .env
keys = ['SWEATY_BOT_DISCORD_TOKEN',
'SWEATY_BOT_WARCRAFTLOGS_CLIENTID',
'SWEATY_BOT_WARCRAFTLOGS_CLIENTSECRET',
'SWEATY_BOT_DISCORD_PREFIX']

keyValues = dict()
load_dotenv()

for key in keys:
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(key," environment variable not set") 
    else:  
        keyValues[key] = value

#construct bot
wlclient = wl.WarcraftLogs(keyValues['SWEATY_BOT_WARCRAFTLOGS_CLIENTID'],
keyValues['SWEATY_BOT_WARCRAFTLOGS_CLIENTSECRET'])
bot = sweat.SweatyBot(wlclient,keyValues['SWEATY_BOT_DISCORD_PREFIX'])

@bot.command()
async def test(ctx):
    await ctx.send(bot.wl.logtestmessage())

bot.run(keyValues['SWEATY_BOT_DISCORD_TOKEN'])
