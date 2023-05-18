from django import forms
from .models import FootballClub, Player

class FootballClubModelForm(forms.ModelForm):
    class Meta:
        model = FootballClub
        fields = ['name', 'img', 'desc', 'price', 'is_club_in_city']

class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'desc', 'country', 'price']