import pytumblr
import json

with open('tumblr_credentials.json', 'r') as f:
            credentials = json.loads(f.read())
client = pytumblr.TumblrRestClient(credentials['consumer_key'], credentials['consumer_secret'], credentials['oauth_token'], credentials['oauth_token_secret'])
client.info()
