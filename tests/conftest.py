from django import setup
from django.apps import apps
from django.conf import settings

if not apps.ready and not settings.configured:
    setup()
