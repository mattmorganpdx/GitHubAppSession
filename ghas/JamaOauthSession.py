from requests import Session
from urllib3.connection import ConnectionError

class JamaOauthSession(Session):
    def __init__(self, url, client_id, client_secret):
        super(JamaOauthSession, self).__init__()
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        
        token_url = '{}/rest/oauth/token'.format(self.url)
        try:
            response = self.post(url=token_url, auth=(self.client_id, self.client_secret), data= { 'grant_type': 'client_credentials'})
            if response.status_code != 200:
                raise JamaOauthError('Request to {} returned code {}'.format(token_url, response.status_code))
            access_obj = response.json()
            self.update_bearer(access_obj.get('access_token'))
        except ConnectionError:
            raise JamaOauthError('Could not connect to {}'.format(token_url))

    def update_bearer(self, bearer_token):
        self.headers.update({'Authorization': 'Bearer {}'.format(bearer_token)})


class JamaOauthError(Exception):
    def __init__(self, message):
        super(JamaOauthError, self).__init__(message)


