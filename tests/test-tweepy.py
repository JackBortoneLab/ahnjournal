#!/usr/bin/env python
from core.janeway_global_settings import (
        TWITTER_API_KEY, TWITTER_API_SECRET_KEY,
    )        
import tweepy

token = '977885623230124032-EEcDtdxRuVpoeEdiKRcsH56y8pHNIgp'
token_secret = 'QUzM0Rc85WLTayUFZa9eq7jEzILbFYXBuZnuwhiakQ9fd'

#OAUth 2 auth
auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
#auth.set_access_token(token, token_secret)

api = tweepy.API(auth)
for tweet in api.user_timeline('ahnjournal'):
    print(tweet)
