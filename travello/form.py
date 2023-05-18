from django import forms
from .models import Destination, Player

class DestinationModelForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'img', 'desc', 'price', 'is_club_in_city']

class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'desc', 'country', 'price']