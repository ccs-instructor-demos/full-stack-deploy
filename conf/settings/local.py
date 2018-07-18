"""
Local development settings and globals.
"""
from .base import *


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        # The last part of ENGINE is 'postgresql', 'mysql', 'sqlite3', 'oracle', or 'ado_mssql'.
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'full_stack_demo',
        'USER': 'full_stack_demo',
        'PASSWORD': 'outweigh-jab-regatta-mordant-hothouse-bock-hayfork',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# STATIC CONFIGURATION
# For storage locally. Dont want to have to run collect static while in dev.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
