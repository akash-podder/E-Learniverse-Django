from django.urls import path
from .views import *

urlpatterns = [
    path('send_push_notification', PushAndroidNotificationsView.as_view(), name = PushAndroidNotificationsView.view_name),
]