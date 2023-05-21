from django import forms

class AddNumberForm(forms.Form):
    number1 = forms.IntegerField(label='Number 1')
    number2 = forms.IntegerField(label='Number 2')