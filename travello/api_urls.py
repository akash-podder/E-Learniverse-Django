from . api_views import *
from django.urls import path

urlpatterns = [
    #  ***************** API Routes ******************

    #  ***************** "api/" Prefix is already defined in MainApp of Django Project ******************
    # Destination API
    path('footballclubs', AllFootballClubsDetailApi.as_view(), name = AllFootballClubsDetailApi.api_name),
    path('footballclub/<int:pk>', SingleFootballClubDetailApi.as_view(), name = SingleFootballClubDetailApi.api_name),

    # Player API
    path('players', AllPlayersApiView.as_view(), name= AllPlayersApiView.api_name),
    path('player/<int:pk>', SinglePlayerDetailApi.as_view(), name= SinglePlayerDetailApi.api_name),
    path('player/create', player_create, name="api/player_create"),
]