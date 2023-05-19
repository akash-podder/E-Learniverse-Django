from __future__ import absolute_import

from celery import shared_task
from .emails import send_review_email
from celery.utils.log import get_task_logger
from celery.task import task
from django.conf import settings

@shared_task
def add(x, y):
    return x+y

logger = get_task_logger(__name__)

@task(name = "send_review_email_task")
def send_review_email_task(name, email_address, email_subject, review_message):
    logger.info("Sent Review Email")
    return send_review_email(name, email_address, email_subject, review_message)