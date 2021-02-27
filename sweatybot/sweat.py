# define actual systems here

#define Bot Class 
class SweatyBot(discord.Client):
    async def on_ready(self):
        print ('Online as {0}'.format(self.user))


#define WarcraftLogs client
class WarcraftLogs(object):

    BASE_URL = 'https://www.warcraftlogs.com:443/v2/'
    ENCOUNTERS_PER_PAGE = 5000

    def __init__(self, api_key):
        self.api_key = api_key