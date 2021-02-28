# define actual systems here
#TODO reconsider naming convention for modules and class names, is this confusing?
import discord
from discord.ext import commands
#define Bot Class 
class SweatyBot(commands.Bot):
    
    def __init__(self, warcraftlogs_client, prefix):
        super().__init__(command_prefix = prefix)
        self.wl = warcraftlogs_client

    async def on_ready(self):
        print ('Online as {0}'.format(self.user))
