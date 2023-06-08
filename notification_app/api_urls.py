from .api_views import *
from django.urls import path

urlpatterns = [
    #  ***************** API Routes ******************

    #  ***************** "api/" Prefix is already defined in MainApp of Django Project ******************
    # Destination API
    path('register-android-user', RegisterAndroidUserApiView.as_view(), name = RegisterAndroidUserApiView.api_name),
]