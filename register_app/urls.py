from django.urls import path
from .views import *

urlpatterns = [
    path('signup', CustomSignUpView.as_view(), name = CustomSignUpView.view_name),
]