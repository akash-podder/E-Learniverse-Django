from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('create/player', views.create_player_view, name = "create-player"),
    path('create/footballclub', views.create_footballclub_view, name ="create-footballclub"),


#  ***************** API Routes ******************

    # Destination API
    path('api/footballclub', views.all_footballclubs_detail_api, name ="api/footballclubs"),
    path('api/footballclub/<int:pk>', views.single_footballclub_detail_api, name ="api/single_footballclub"),

    # Player API
    path('api/players', views.all_player_detail_api, name="api/players"),
    path('api/player/<int:pk>', views.single_player_detail_api, name="api/single_player"),
    path('api/player/create', views.player_create, name="api/player_create"),
]
