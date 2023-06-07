from django.shortcuts import render
from django.views import View


# Create your views here.
class PushAndroidNotificationsView(View):
    view_name = "send_android_push_notification"
    def get(self, request):
        context = {
        }
        return render(request, 'notification_app/send_notification.html', context)

    def post(self, request):
        context = {
            
        }
        return render(request, 'notification_app/send_notification.html', context)