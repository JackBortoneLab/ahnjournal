#!/usr/bin/env python3
import django
django.setup()
from janeway.core.wsgi import application as wsgi_application
from django.urls import set_script_prefix

from djangohotsauce.controllers.wsgi import WSGIController

class JanewayController(WSGIController):
    def __call__(self, environ, start_response):
        return wsgi_application(environ, start_response)


application = JanewayController()
