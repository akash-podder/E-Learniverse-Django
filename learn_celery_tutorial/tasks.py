from __future__ import absolute_import

from celery import shared_task
from celery.task import task
from celery.utils.log import get_task_logger

# Logger Settings
logger = get_task_logger(__name__)

@shared_task(name='learn_celery_tutorial.add_numbers')
def add_numbers(x, y):
    logger.info("Numbers Added Asynchronously")
    return x+y