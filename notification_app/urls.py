from django.urls import path
from .views import *

urlpatterns = [
    path('registered_users_info', RegisteredUsersInfoView.as_view(), name = RegisteredUsersInfoView.view_name),
    path('send_push_notification/<str:mobile_no>', SendAndroidPushNotificationToMobileNumberView.as_view(), name = SendAndroidPushNotificationToMobileNumberView.view_name),
    path('send_bulk_push_notification', SendBulkAndroidPushNotifications.as_view(), name = SendBulkAndroidPushNotifications.view_name),
]