#define WarcraftLogs client
class WarcraftLogs(object):

    BASE_URL = 'https://classic.warcraftlogs.com/api/v2/client'
    ENCOUNTERS_PER_PAGE = 5000

    def __init__(self, api_key):
        self.api_key = api_key

    def logtestmessage(self):
        message = "This is an initiated WarcraftLogs object \n base_url is ",self.BASE_URL
        return message