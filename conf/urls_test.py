"""
URL Patterns to use for testing, designed to help find any hard coded url references in views (and sometimes templates)
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'testing-url/', include('conf.urls')),
]
