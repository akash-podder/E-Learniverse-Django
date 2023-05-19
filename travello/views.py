import io

from django.shortcuts import render, redirect
from django.http import HttpResponse
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

# Create your views here.

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ReviewForm

    def form_valid(self, form):
        # Form er send_email function call dibo
        form.send_email()
        msg = "Thanks For the Review"
        return HttpResponse(msg)

def index(request):

    clubs = FootballClub.objects.all()
    players = Player.objects.all()

    context = {
        'clubs': clubs,
        'players': players
    }

    if request.method == 'POST':
        email_review_form = ReviewForm(request.POST)
        if email_review_form.is_valid():
            email_review_form.send_email()
            msg = "Thanks For the Review"
            return HttpResponse(msg)
    else:
        email_review_form = ReviewForm()

    context['email_form'] = email_review_form

    return render(request, 'travello/index.html', context)

def create_player_view(request):
    if request.method == 'POST':
        form = PlayerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlayerModelForm()

    return render(request, 'travello/create_player.html', {'form': form})

def create_footballclub_view(request):
    if request.method == 'POST':
        form = FootballClubModelForm(request.POST, request.FILES)  # request.FILES ---> eita MUST important. naile IMAGE Upload Hobe Nah
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FootballClubModelForm()

    return render(request, 'travello/create_footballclub.html', {'form': form})


#  ************************** APIs ************************************


#  ***************** Destination APIs ******************

# Returns Single Object
def single_footballclub_detail_api(request, pk):

    club = FootballClub.objects.get(id = pk)
    club_serialized = DestinationSerializer(club)
    json_data = JSONRenderer().render(club_serialized.data)

    return HttpResponse(json_data, content_type="application/json")


# QuerySet for All Destinations
def all_footballclubs_detail_api(request):

    clubs = FootballClub.objects.all()

    club_serialized = DestinationSerializer(clubs, many = True)  #QuerySet er jonno "many=True" eita likha Compolsory
    json_data = JSONRenderer().render(club_serialized.data)

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