from __future__ import absolute_import
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_docker_project.settings')

# this is the NAME which we have to Pass to instantiate `CELERY_WORKER`
# eikane jei NAME use korbo `CELERY_WORKER` invoke korar time sheita Argument hisave Pass korbo
# Example : app = Celery('my_custom_project')
# `CELERY_WORKER`: celery -A my_custom_project worker

app = Celery('django_docker_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

# ek kothay SETTINGS.py ee `CELERY_` prefix er shb Config Catch korte parbe CELERY APP
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
