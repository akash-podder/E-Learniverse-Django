import io

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.views.generic.edit import FormView

from EmailApp.forms import ReviewForm
from .models import FootballClub, Player
from .form import FootballClubModelForm, PlayerModelForm
from .serializers import DestinationSerializer, PlayerSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.http import HttpResponse, JsonResponse

# to Call Create Player we need to Bypass "CSRF" token... eijonno eita Import korlam
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

#  ***************** Football-Club APIs ******************

# Returns Single Object
class SingleFootballClubDetailApi(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow access to all users, authenticated or not

    api_name = "api/single_footballclub"

    def get(self, request, pk):
        club = FootballClub.objects.get(id=pk)
        club_serialized = DestinationSerializer(club)
        json_data = JSONRenderer().render(club_serialized.data)

        return HttpResponse(json_data, content_type="application/json")


# QuerySet for All FootballClubs
class AllFootballClubsDetailApi(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow access to all users, authenticated or not

    api_name = "api/footballclubs"

    def get(self, request):
        clubs = FootballClub.objects.all()

        club_serialized = DestinationSerializer(clubs, many=True)  # QuerySet er jonno "many=True" eita likha Compolsory
        json_data = JSONRenderer().render(club_serialized.data)

        return HttpResponse(json_data, content_type="application/json")

        # Dict chara onno kono Data pass korte  "safe=False" use korbo... eikane "List" jacche tai "safe=False" likte huise JsonResponse ee
        # return  JsonResponse(dest_serialized.data, safe=False)  #eivabe 1 line ei "JsonResponse" amra direct Return korte pari

#  ***************** Player APIs ******************


class SinglePlayerDetailApi(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow access to all users, authenticated or not

    api_name = "api/single_player"

    def get(self, request, pk):
        player = Player.objects.get(id=pk)
        player_serialized = PlayerSerializer(player)
        json_data = JSONRenderer().render(player_serialized.data)

        return HttpResponse(json_data, content_type="application/json")


class AllPlayersDetailApi(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow access to all users, authenticated or not

    api_name = "api/players"

    def get(self, request):
        players = Player.objects.all()

        player_serialized = PlayerSerializer(players, many=True)
        json_data = JSONRenderer().render(player_serialized.data)

        return HttpResponse(json_data, content_type="application/json")


# it will now ByPass CSRF Token
@csrf_exempt
def player_create(request):
    if request.method == 'POST':
        print("request is POST")
        json_data = request.body
        stream = io.BytesIO(json_data)
        player_pythonData = JSONParser().parse(stream)
        player_serializer = PlayerSerializer(data=player_pythonData)

        if player_serializer.is_valid():
            player_serializer.save()
            response_msg = { 'msg' : 'Data Created'}

            json_data = JSONRenderer().render(response_msg)

            return HttpResponse(json_data, content_type="application/json")

        else:
            json_data = JSONRenderer().render(player_serializer.errors)
            return HttpResponse(json_data, content_type="application/json")

    else:
        print("request is NOT POST")