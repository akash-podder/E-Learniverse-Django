from django.urls import path
from . import views

urlpatterns = [
    path('horizontal', views.HorizontalTutorialView.as_view(), name = views.HorizontalTutorialView.view_name),
    path('vertical', views.VerticalTutorialTemplateView.as_view(), name = views.VerticalTutorialTemplateView.view_name),
    path('code/<str:code_id>', views.ShowFlexboxCodeView.as_view(), name=views.ShowFlexboxCodeView.view_name),
]