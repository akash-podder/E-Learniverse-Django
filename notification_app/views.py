from datetime import datetime, timedelta
import json
from django.shortcuts import render
from django.views import View
from firebase_admin import messaging
from firebase_admin._messaging_encoder import MessageEncoder

from .fcm_client import FCMClient
from .models import RegisteredAndroidUser
from .tasks import *

# Create your views here.
class RegisteredUsersInfoView(View):
    view_name = "registered_users_info"
    def get(self, request):
        user_list = RegisteredAndroidUser.objects.all()
        context = {
            'user_list' : user_list,
        }
        return render(request, 'notification_app/send_notification.html', context)

class SendAndroidPushNotificationToMobileNumberView(View):
    view_name = "send_android_push_notification_to_mobile_number"
    def get(self, request, mobile_no):

        fcm_client = FCMClient()

        user = RegisteredAndroidUser.objects.get(mobile=mobile_no)
        token = user.fcm_token

        notification_title = 'E Learniverse: ' + user.name
        notification_body = 'This is Test From Django ' + user.mobile
        notification_data = {'key': 'value'}

        try:
            fcm_client.send_push_notification(token, notification_title, notification_body)
            fcm_client.send_message({'key': 'value'}, token)

            context = {
                'msg': 'Notification Sent to ' + user.name
            }

        except messaging.UnregisteredError:
            context = {
                'msg': user.name + '\'s ---> Token is No Longer Valid or Device has Uninstalled the App'
            }

        return render(request, 'notification_app/send_notification.html', context)


class SendBulkAndroidPushNotifications(View):
    view_name = "send_bulk_android_push_notifications"
    def post(self, request):

        fcm_client = FCMClient()

        users = RegisteredAndroidUser.objects.all()
        messages = []
        for user in users:
            token = user.fcm_token
            notification_title = 'E Learniverse: ' + user.name
            notification_body = 'This is BULK Test From Django ' + user.mobile

            message = fcm_client.create_push_notification_message(token, notification_title, notification_body)
            messages.append(message)
            context = {
                'msg': 'Notification Sent to ' + user.name
            }
        fcm_client.send_all_message(messages)

        execution_time = datetime.now() + timedelta(seconds=1)  # Example: 1 seconds from now
        serialized_messages_object_list = json.dumps(list(messages), cls=MessageEncoder)

        # Celery Task Serialized Object chara Parameter ee Onno kisu Receive kora nah
        # Reason hocche: caz, task gula shb Message Broker er Queue te joma hui... so Object gula Serializable hote hobe
        # result = send_one_time_bulk_notification.apply_async(args=[serialized_messages_object_list], eta=execution_time)  # "eta" argument in a task refers to the Estimated Time of Arrival.
        result = send_one_time_bulk_notification(serialized_messages_object_list)  # "eta" argument in a task refers to the Estimated Time of Arrival.

        send_one_time_notification_task_context = "Bulk Notification Sent"
        context = {
            'one_time_task_context': send_one_time_notification_task_context,
            'result': result
        }

        return render(request, 'notification_app/send_notification.html', context)