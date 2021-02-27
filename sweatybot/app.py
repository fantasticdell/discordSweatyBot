import os
#pip install -U discord.py
import discord
import logging
import asyncio
#pip install -U python-dotenv
from dotenv import load_dotenv
from discord.ext import commands
from sweatybot import config
from sweatybot import SweatyBot  
from sweatbot import WarcraftLogs


#define the discord frontend here, and run the discord.py client
#store config / data structures in config.py
#store application functions in sweat.py

#define logger
logger = logging.getLogger('discord')
#change this to warning later, or define a log file 
#https://discordpy.readthedocs.io/en/latest/logging.html
logger.basicConfig(level=logging.INFO)

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
    print("API Tokencode discovered: ", discordtoken)
#end Set Discord API token

# Set Warcraft Logs API token
key = "SWEATY_BOT_WARCRAFTLOGS_TOKEN"
warcraftlogstoken = os.getenv(key)
if warcraftlogstoken is None:
    raise RuntimeError("SWEATY_BOT_DISCORD_TOKEN environment variable not set")
else:
    print("API Tokencode discovered: ", warcraftlogstoken)


#construct bot
bot = SweatyBot()
wlclient = WarcraftLogs(warcraftlogstoken)
bot.run(discordtoken)