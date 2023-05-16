import io

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Destination, Player
from .form import PlayerForm
from .serializers import DestinationSerializer, PlayerSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.http import HttpResponse, JsonResponse

# to Call Create Player we need to Bypass "CSRF" token... eijonno eita Import korlam
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):

    dests = Destination.objects.all()
    players = Player.objects.all()

    return render(request, 'travello/index.html', {'dests' : dests, 'players': players})

def create_player_view(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlayerForm()

    return render(request, 'travello/create_player.html', {'form': form})


#  ************************** APIs ************************************


#  ***************** Destination APIs ******************

# Returns Single Object
def single_destination_detail_api(request, pk):

    dest = Destination.objects.get(id = pk)
    dest_serialized = DestinationSerializer(dest)
    json_data = JSONRenderer().render(dest_serialized.data)

    return HttpResponse(json_data, content_type="application/json")


# QuerySet for All Destinations
def all_destination_detail_api(request):

    dests = Destination.objects.all()

    dest_serialized = DestinationSerializer(dests, many = True)  #QuerySet er jonno "many=True" eita likha Compolsory
    json_data = JSONRenderer().render(dest_serialized.data)

    return HttpResponse(json_data, content_type="application/json")

    # Dict chara onno kono Data pass korte  "safe=False" use korbo... eoikane "List" jacche tai "safe=False" likte huise JsonResponse ee
    # return  JsonResponse(dest_serialized.data, safe=False)  #eivabe 1 line ei "JsonResponse" amra direct Return korte pari




#  ***************** Player APIs ******************

def single_player_detail_api(request, pk):

    player = Player.objects.get(id = pk)
    player_serialized = PlayerSerializer(player)
    json_data = JSONRenderer().render(player_serialized.data)

    return HttpResponse(json_data, content_type="application/json")


def all_player_detail_api(request):

    players = Player.objects.all()

    player_serialized = PlayerSerializer(players, many = True)
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