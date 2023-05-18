from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

