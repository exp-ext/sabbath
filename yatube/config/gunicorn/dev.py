"""Gunicorn *development* config file"""
# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "yatube.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 4 + 1
# The socket to bind
bind = '0.0.0.0:8000'
# Restart workers when code changes (development only!)
reload = True
