from __future__ import absolute_import
import json
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime

from firebase_admin import messaging

from .fcm_client import FCMClient
from .models import *

# Logger Settings
logger = get_task_logger(__name__)

# ****** Send One Time Notification *******
@shared_task
def send_one_time_bulk_notification(serialized_page_object_list):
    fcm_client = FCMClient()

    messages = []
    for serialized_message in json.loads(serialized_page_object_list):
        # Extract the values from the serialized message dictionary & Create a new Message object with the extracted values
        #  (`**`) ---> extracts Value from a List of Objects Dictionary's value and Converts Them Back to Original Object Form
        message = messaging.Message(**serialized_message)

        # `**message.notification` ke UNPACK kore hobe `Notification` Object ee Convert kore & `message.notification` variable ee assign korte hobe
        message.notification = messaging.Notification(**message.notification)
        messages.append(message)

    batch_response = fcm_client.send_all_message(messages)

    logger.info("One-time Notification executed at ---> {}".format(datetime.now()))
    return "One-time Notification executed at ---> {}".format(datetime.now())