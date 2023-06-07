from django.shortcuts import render
from django.views import View
from .fcm_client import FCMClient
from django.conf import settings

# Create your views here.
class SendAndroidPushNotificationsView(View):
    view_name = "send_android_push_notification"
    def get(self, request):
        return render(request, 'notification_app/send_notification.html')

    def post(self, request):
        fcm_client = FCMClient()

        token = settings.DUMMY_ANDROID_TOKEN

        notification_title = 'E Learniverse'
        notification_body = 'This is Test From Django'
        notification_data = {'key': 'value'}

        fcm_client.send_push_notification(token, notification_title, notification_body)
        fcm_client.send_message({'key': 'value'}, token)

        context = {
            'msg': 'Notification Sent'
        }

        return render(request, 'notification_app/send_notification.html', context)