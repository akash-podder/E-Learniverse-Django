from __future__ import absolute_import

from celery import shared_task
from .emails import send_review_email
from celery.utils.log import get_task_logger
from celery.task import task

# Logger Settings
logger = get_task_logger(__name__)


# Moved the task to `learn_celery_tutorial` App of Django
# @shared_task
# def add(x, y):
#     logger.info("Numbers Added")
#     return x+y

@task(name = "send_review_email_task")
def send_review_email_task(name, email_address, email_subject, review_message):
    logger.info("Sent Review Email")
    return send_review_email(name, email_address, email_subject, review_message)