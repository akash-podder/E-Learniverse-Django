import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import FormView

from EmailApp.forms import ReviewForm
from .models import FootballClub, Player
from .form import FootballClubModelForm, PlayerModelForm
from .serializers import FootballClubSerializer, PlayerSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.http import HttpResponse, JsonResponse

# to Call Create Player we need to Bypass "CSRF" token... eijonno eita Import korlam
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.

class IndexView(View):

    view_name = 'index'

    clubs = FootballClub.objects.all()
    players = Player.objects.all()

    # this Context data is for BOTH POST & GET... that's why it is declared as CLASS Variable
    # And to access it in functions one has to use `self.context`
    context = {
        'clubs': clubs,
        'players': players
    }

    def get(self, request):
        backend_port = request.META.get("HTTP_X_BACKEND_PORT", "unknown")
        client_port = request.get_port()  # usually 80/443 behind nginx
        worker_process_id = os.getpid()

        email_review_form = ReviewForm()
        self.context['email_form'] = email_review_form
        self.context['backend_port'] = backend_port
        self.context['client_port'] = client_port
        self.context['worker_process_id'] = worker_process_id

        return render(request, 'travello/index.html', self.context)

    def post(self, request):
        email_review_form = ReviewForm(request.POST)

        if email_review_form.is_valid():
            # Form er send_email function call dibo
            email_review_form.send_email()
            msg = "Thanks For the Review"
            self.context['email_sent_msg'] = msg
        else:
            self.context['email_sent_msg'] = "Couldn't Send Email Due To Some Errors"
        return render(request, 'travello/index.html', self.context)


class CreatePlayerView(View):
    view_name = "create-player"
    def get(self, request):
        form = PlayerModelForm()
        return render(request, 'travello/create_player.html', {'form': form})

    def post(self, request):
        form = PlayerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'travello/create_player.html', {'form': form})

class CreateFootballClubView(View):
    view_name = "create-footballclub"
    def get(self, request):
        form = FootballClubModelForm()
        return render(request, 'travello/create_footballclub.html', {'form': form})

    def post(self, request):
        form = FootballClubModelForm(request.POST,
                                        request.FILES)  # request.FILES ---> eita MUST important. naile IMAGE Upload Hobe Nah
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'travello/create_footballclub.html', {'form': form})