from . import api_views
from django.urls import path

urlpatterns = [
    #  ***************** API Routes ******************

    #  ***************** "api/" Prefix is already defined in MainApp of Django Project ******************
    # Destination API
    path('footballclub', api_views.all_footballclubs_detail_api, name ="api/footballclubs"),
    path('footballclub/<int:pk>', api_views.single_footballclub_detail_api, name ="api/single_footballclub"),

    # Player API
    path('players', api_views.all_player_detail_api, name="api/players"),
    path('player/<int:pk>', api_views.single_player_detail_api, name="api/single_player"),
    path('player/create', api_views.player_create, name="api/player_create"),
]