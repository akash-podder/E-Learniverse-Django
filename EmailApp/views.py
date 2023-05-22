from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponse
from django.views.generic.edit import FormView

# Create your views here.

class ReviewEmailView(FormView):
    # template_name = 'EmailApp/review.html'
    view_name = "reviews"
    form_class = ReviewForm

    def form_valid(self, form):
        # Form er send_email function call dibo
        form.send_email()
        msg = "Thanks For the Review"
        return HttpResponse(msg)