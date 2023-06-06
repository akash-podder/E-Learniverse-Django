from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CustomSignUpForm(UserCreationForm):
    # Overriding `password2` form from Parent Class(UserCreationForm)
    password2 = forms.CharField(
        label=("Confirm Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    # Override behavior of Parent Class(UserCreationForm)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'} # we can Customize the LABEL of the mentioned `fields` like this
