from django.urls import path
from .views import *

urlpatterns = [
    path('signup', SignUpCustomView.as_view(), name = SignUpCustomView.view_name),
    path('login', LogInCustomView.as_view(), name = LogInCustomView.view_name),
    path('profile', UserProfileCustomView.as_view(), name = UserProfileCustomView.view_name),
    path('logout', UserLogOutCustomView.as_view(), name = UserLogOutCustomView.view_name),
    path('changepass', UserChangePasswordCustomView.as_view(), name = UserChangePasswordCustomView.view_name),
    path('changepass_without_oldpass', UserForgetPassword.as_view(), name = UserForgetPassword.view_name),
]