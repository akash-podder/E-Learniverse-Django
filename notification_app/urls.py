from django.urls import path
from .views import *

urlpatterns = [
    path('send_push_notification', SendAndroidPushNotificationsView.as_view(), name = SendAndroidPushNotificationsView.view_name),
]