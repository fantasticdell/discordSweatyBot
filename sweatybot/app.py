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

load_dotenv()
token = os.getenv("SWEATY_BOT_DISCORD_TOKEN")

if token is None:
    raise RuntimeError("SWEATY_BOT_DISCORD_TOKEN environment variable not set")

client.run(token)