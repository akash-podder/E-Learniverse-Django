import io

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import FormView

from EmailApp.forms import ReviewForm
from .models import FootballClub, Player
from .form import FootballClubModelForm, PlayerModelForm
from .serializers import DestinationSerializer, PlayerSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

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


class AllPlayersApiView(APIView):
    authentication_classes = []  # No authentication required
    permission_classes = [AllowAny]  # Allow access to all users, authenticated or not

    api_name = "api/players"

    def get(self, request):
        players = Player.objects.all()

        player_serialized = PlayerSerializer(players, many=True)

        json_data = JSONRenderer().render(player_serialized.data)
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(player_serialized.data, safe=False) #Above Two Lines can be written just by Using JsonResponse

    def post(self, request):
        player_serialized = PlayerSerializer(data=request.data)
        if player_serialized.is_valid():
            player_serialized.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(player_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

# it will now ByPass CSRF Token
@csrf_exempt
def player_create(request):
    if request.method == 'POST':
        print("request is POST")
        #==========Flow=============
        # Json Data ---> Python Native Data(Dictionary) ---> Python Complex Data(Database Model Object)

        json_data = request.body
        stream = io.BytesIO(json_data)
        player_pythonData = JSONParser().parse(stream) # JSONParser work is to convert `Json Data` to `Python Native Data Type(Dictionary)`
        player_serializer = PlayerSerializer(data=player_pythonData) # it Converts `Python Native Data Type(Dictionary)`to COMPLEX Data(Database MODEL Object)

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



class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # 'gettoken/' ---> input: Username(Django Portal er Username), Password & returns `Token` & `Refresh token`
    # 'refreshtoken/' ---> input: `Refresh token` & returns `Token`

    # 1. Username & Password diye first ee 'gettoken/' call dite hui... eita 2 ta jinish return kore a) Token, b) Refresh Token
    # 2. Normal Token er validity 5 mins & Refresh Token er Validity 1 Day
    # 3. "Normal Token" er validity sesh huile... Refresh Token diye amra 'refreshtoken/' URL ee Call diye abr "NEW Normal Token" fetch kore niye ashi