#pip install -U session
from requests import Session
#standard module
from urllib import parse

#define WarcraftLogs client
class WarcraftLogs(object):

    BASE_URL = 'https://classic.warcraftlogs.com/api/v2/client'
    ENCOUNTERS_PER_PAGE = 5000

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = Session()

#_get will return content from warcraftlogs, when provided with the url path parameters
    def _get(self, path, **kwargs):
        params = {"api_key": self.api_key}
        params.update(kwargs)

        url = parse.urljoin(self.BASE_URL,path)

        return self.session.get(url,params=params)


    def logtestmessage(self):
        message = "This is an initiated WarcraftLogs object \n base_url is ",self.BASE_URL
        return message