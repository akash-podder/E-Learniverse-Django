from __future__ import absolute_import

from celery import shared_task
from celery.task import task
from celery.utils.log import get_task_logger
from django.core.cache import cache
from datetime import datetime, timedelta

# Logger Settings
logger = get_task_logger(__name__)

@shared_task(name='learn_celery_tutorial.add_numbers')
def add_numbers_shared_task(x, y):
    logger.info("Numbers Added Asynchronously")
    return x+y

@shared_task(name='learn_celery_tutorial.number_counter_using_celery_beat')
def number_counter_using_celery_beat_task(number):
    logger.info("Celery BEAT: counter ---> Adding Number = {} each time".format(number))
    # get the cache
    data = cache.get('custom_cache_key')
    if data:
        data = data + number
    else:
        data = number
    # Update the cache
    cache.set('custom_cache_key', data, timeout=360)
    return data

@shared_task
def one_time_task():
    # Task logic goes here
    logger.info("One-time task executed at ---> {}".format(datetime.now()))
    return "One-time task executed at ---> {}".format(datetime.now())

@shared_task(name='learn_celery_tutorial.user_push_scheduled_celery_task')
def user_push_scheduled_celery_task():
    logger.info("User Pushed Celery Task is executed at ---> {}".format(datetime.now()))
    return "User Pushed Celery Task is executed at ---> {}".format(datetime.now())