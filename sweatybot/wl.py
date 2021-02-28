#pip install -U session
import requests
#pip install -U requests_oauthlib
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
#standard module
from urllib import parse

#define WarcraftLogs client
class WarcraftLogs(object):
    #these should probably be in .env
    BASE_URL = 'https://www.warcraftlogs.com/oauth/authorize'
    TOKEN_URL = 'https://www.warcraftlogs.com/oauth/token'
    REDIRECT_URL = 'https://www.warcraftlogs.com/api/docs'
    ENCOUNTERS_PER_PAGE = 5000

    def __init__(self, clientid, clientsecret):
        self.client = BackendApplicationClient(client_id=clientid)
        self.oauth = OAuth2Session(client=self.client)
        self.token = self.oauth.fetch_token(token_url=self.TOKEN_URL,
        client_id=clientid,client_secret=clientsecret)


#_get will return content from warcraftlogs, when provided with the url path parameters
    def _get(self, path, **kwargs):
        params = {"api_key": self.api_key}
        params.update(kwargs)

        url = parse.urljoin(self.BASE_URL,path)

        return self.session.get(url,params=params)


    def logtestmessage(self):
        message = "TokenID is ", self.token
        return message


#notes https://www.warcraftlogs.com/api/docs
#authorization ui https://www.warcraftlogs.com/oauth/authorize
#access token uri https://www.warcraftlogs.com/oauth/token