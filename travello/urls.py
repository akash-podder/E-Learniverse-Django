from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name = views.IndexView.view_name),
    path('create/player', views.CreatePlayerView.as_view(), name = views.CreatePlayerView.view_name),
    path('create/footballclub', views.CreateFootballClubView.as_view(), name = views.CreateFootballClubView.view_name),
]

