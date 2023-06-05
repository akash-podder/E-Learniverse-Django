from __future__ import absolute_import

from celery import shared_task
from celery.task import task
from celery.utils.log import get_task_logger
from django.core.cache import cache
from datetime import datetime, timedelta
from .models import *

# Logger Settings
logger = get_task_logger(__name__)

@shared_task(name='learn_celery_tutorial.add_numbers')
def add_numbers_shared_task(x, y):
    logger.info("Numbers Added Asynchronously")
    return x+y


# ****** Celery BEAT Task Type-1 *******
@shared_task(name='learn_celery_tutorial.type_1_of_celery_beat_task_for_number_counter')
def type_1_of_celery_beat_task_for_number_counter(number):
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


# ****** Celery BEAT Task Type-2 *******
@shared_task
def type_2_of_celery_beat_task_for_one_time_task():
    # Task logic goes here
    logger.info("One-time task executed at ---> {}".format(datetime.now()))
    return "One-time task executed at ---> {}".format(datetime.now())


# ****** Celery BEAT Task Type-3 *******
@shared_task(name='learn_celery_tutorial.type_3_of_celery_beat_task_for_user_pushing_scheduled_celery_task_in_queue')
def type_3_of_celery_beat_task_for_user_pushing_scheduled_celery_task_in_queue():
    logger.info("User Pushed Celery Task is executed at ---> {}".format(datetime.now()))
    result = "User Pushed Celery Task is executed at ---> {}".format(datetime.now())

    # Saving the TASK_RESULT in My DB, so that i can Retrieve it from VIEW
    UserPushedTaskResult.objects.create(task_name="task_name", result=result)

    return result