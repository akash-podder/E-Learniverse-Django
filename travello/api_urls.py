from . api_views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

player_router = DefaultRouter()

# Registering `PlayerModelViewSet` with Router
# ekn `player` er All Players, Single Player, Delete Player etc. shb kisu er jonno ei ekta `playerapi` tei Hit korle Pabo
player_router.register('playerapi', PlayerModelViewSet, basename='playerapi')

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

    # adding `player_router` Urls to Main Urls
    path('', include(player_router.urls)),

    # JWT(Json Web Token) Url Paths
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]