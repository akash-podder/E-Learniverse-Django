from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('create/player', views.create_player_view, name = "create-player"),


#  ***************** API Routes ******************

    # Destination API
    path('api/destinations', views.all_destination_detail_api, name = "api/destinations"),
    path('api/destination/<int:pk>', views.single_destination_detail_api, name = "api/single_destination"),

    # Player API
    path('api/players', views.all_player_detail_api, name="api/players"),
    path('api/player/<int:pk>', views.single_player_detail_api, name="api/single_player"),
    path('api/player/create', views.player_create, name="api/player_create"),
]
