import os
#pip install -U discord.py
import discord
import logging
import asyncio
#pip install -U python-dotenv
from dotenv import load_dotenv
from discord.ext import commands
from sweatybot import config
from sweatybot import sweat

#define the discord frontend here, and run the discord.py client
#store config / data structures in config.py
#store application functions in sweat.py

print("Sweaty Bot loading")
# Set Discord API token
# this is stored in .env as SWEATY_BOT_DISCORD_TOKEN and should be set before any build
key = "SWEATY_BOT_DISCORD_TOKEN"
#load .env into process
load_dotenv()
#pull our key pair
token = os.getenv(key)

if token is None:
    raise RuntimeError("SWEATY_BOT_DISCORD_TOKEN environment variable not set")
else:
    print("API Tokencode discovered: ", token)
#end Set Discord API token

#define Bot Class 
class SweatyBot(discord.Client):
    async def on_ready(self):
        print ('Online as {0}'.format(self.user))

#construct bot
bot = SweatyBot()
bot = commands.Bot(command_prefix="!sweaty")
bot.run(token)