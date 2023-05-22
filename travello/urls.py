from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name = views.IndexView.view_name),
    path('create/player', views.CreatePlayerView.as_view(), name = views.CreatePlayerView.view_name),
    path('create/footballclub', views.CreateFootballClubView.as_view(), name = views.CreateFootballClubView.view_name),


#  ***************** API Routes ******************

    # Destination API
    path('api/footballclub', views.all_footballclubs_detail_api, name ="api/footballclubs"),
    path('api/footballclub/<int:pk>', views.single_footballclub_detail_api, name ="api/single_footballclub"),

    # Player API
    path('api/players', views.all_player_detail_api, name="api/players"),
    path('api/player/<int:pk>', views.single_player_detail_api, name="api/single_player"),
    path('api/player/create', views.player_create, name="api/player_create"),
]

