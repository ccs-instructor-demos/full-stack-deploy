"""Production settings and globals."""
from .base import *

# Double check debug is off
DEBUG = True

# HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [
    'full-stack-deploy.herokuapp.com',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# HEROKU CONFIGURATION for DATABASE_URL, ALLOWED_HOSTS, WhiteNoise (for static assets), Logging, and Heroku CI
# See: https://github.com/heroku/django-heroku
import django_heroku
django_heroku.settings(locals())
