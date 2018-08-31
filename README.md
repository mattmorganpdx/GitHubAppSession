# GitHub App Session
While trying to make a github app in the python flask framework I had a real problem finding a python example of how to interact as a GitHub App. The goal of this package is to take the information from the high level github tutorial and take it the last mile to actually have your app working with the api.

## Usage
```
import os
from ghas import GitHubAppSession

# Things you needs to supply:
# 1. Your App's ID from the GitHub console
# 2. The contents of the private key .pem file. You generate this on the GitHub console
# 3. The installation id. This is an identifier you will get out of the payload sent to 
# your webhook e.g. request.json.get('installation', {}).get('id')

APP_ID = os.getenv('APP_ID')
PK     = os.getenv('PK')

def handle_webhook():
    installation_id = request.json.get('installation', {}).get('id')
    with GitHubAppSession(APP_ID, PK, installation_id) as s:
        # all the cool stuff you'd do with a requests.Session

```

## Installation
pip install git+https://github.com/mattmorganpdx/GitHubAppSession

## Sources
These blog posts help me get this working:

https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps

https://developer.github.com/apps/building-your-first-github-app


# Jama Oauth Session
A session wrapper to perform api requests with the Jama Connect requirements management software.

## Usage
```
from ghas import JamaOauthSession

# Things you need to supply:
# 1. The base url of your Jama Connect instance
# 2. Oauth Client ID
# 3. Oauth Client Secret

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

JAMA_URL = 'https://jama.mycompany.com'

jama_session = JamaOauthSession(JAMA_URL, CLIENT_ID, CLIENT_SECRET)

response = jama_session.get('{}/rest/v1/users/current'.format(JAMA_URL))
user_info = response.json()

print(user_info)

```

## Sources
See the Jama rest documentation for more info:

http://dev.jamasoftware.com/rest