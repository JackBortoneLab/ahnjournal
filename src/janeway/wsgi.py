#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-
#import django
#django.setup()

#from djangohotsauce.controllers.oauth import (
#    OAuthController, 
#    oauthclient,
#    twitter
#    )
#from djangohotsauce.controllers.wsgi import WSGIController
from janeway.core.wsgi import application

#settings = wsgi_app.settings
#application = OAuthController(wsgi_app, client=oauthclient(twitter, 
#      settings.TWITTER_API_KEY,
#      settings.TWITTER_API_SECRET_KEY,
#      settings.TWITTER_ACCESS_TOKEN,
       #settings.OAUTH2_SCOPE,
#      settings.TWITTER_REDIRECT_URL
#      ))
