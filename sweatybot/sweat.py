# define actual systems here
#TODO reconsider naming convention for modules and class names, is this confusing?
import discord
#define Bot Class 
class SweatyBot(discord.Client):
    
    def __init__(self, warcraftlogs_client):
        super().__init__()
        self.wl = warcraftlogs_client

    async def on_ready(self):
        print ('Online as {0}'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!test'):
            await message.channel.send(self.wl.logtestmessage())