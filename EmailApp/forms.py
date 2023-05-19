from django import forms
from .tasks import send_review_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'class':'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'})
                           )

    email_address = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'})
                            )
    email_subject = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs = {'class': 'form-control', 'placeholder': 'Email Subject', 'rows': '5'})
                           )
    review_message = forms.CharField(label='Review', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '5'})
    )

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email_address'],
            self.cleaned_data['email_subject'],
            self.cleaned_data['review_message']
        )