import os
import discord
#pip install -U discord.py
import logging
import asyncio
import sweatybot.sweat as sweat
#pip install -U python-dotenv
from dotenv import load_dotenv
from discord.ext import commands


#define the discord frontend here, and run the discord.py client
#store config / data structures in config.py
#store application functions in sweat.py

#define logger
#logger = logging.getLogger('discord')
#change this to warning later, or define a log file 
#https://discordpy.readthedocs.io/en/latest/logging.html
#logger.basicConfig(level=logging.INFO)

print("Sweaty Bot loading")




# Set Discord API token
# this is stored in .env as SWEATY_BOT_DISCORD_TOKEN and should be set before any build
key = "SWEATY_BOT_DISCORD_TOKEN"
#load .env into process
load_dotenv()
#pull our key pair
discordtoken = os.getenv(key)

if discordtoken is None:
    raise RuntimeError("SWEATY_BOT_DISCORD_TOKEN environment variable not set")
else:
    print("Discord API Tokencode discovered: ", discordtoken)
#end Set Discord API token

# Set Warcraft Logs API token
key = "SWEATY_BOT_WARCRAFTLOGS_TOKEN"
warcraftlogstoken = os.getenv(key)
if warcraftlogstoken is None:
    raise RuntimeError("SWEATY_BOT_DISCORD_TOKEN environment variable not set")
else:
    print("Warcraft Logs API Tokencode discovered: ", warcraftlogstoken)


#construct bot
bot = sweat.SweatyBot()
wlclient = sweat.WarcraftLogs(warcraftlogstoken)
bot.run(discordtoken)