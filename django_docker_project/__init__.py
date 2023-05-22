# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

# *********************************************************************************************
# Without This Line CELERY won't Pickup Proper Configuration while Loading from DJANGO_SETTINGS
# *********************************************************************************************

from .celery import app as celery_app

__all__ = ('celery_app',)