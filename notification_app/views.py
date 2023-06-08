from django.shortcuts import render
from django.views import View
from firebase_admin import messaging

from .fcm_client import FCMClient
from .models import RegisteredAndroidUser

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