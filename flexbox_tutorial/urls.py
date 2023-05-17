from django.urls import path
from . import views

urlpatterns = [
    path('horizontal', views.learn_flexbox_horizontal, name = "learn_flexbox_horizontal"),
    path('vertical', views.learn_flexbox_vertical, name = "learn_flexbox_vertical"),
    path('code/<str:code_id>', views.ShowFlexboxCodeView.as_view(), name='show_flexbox_code'),
]