from django.shortcuts import render
from django.views import View
from .forms import CustomSignUpForm

# Create your views here.
class CustomSignUpView(View):
    view_name = "sign_up"
    def get(self, request):
        form = CustomSignUpForm()
        context = {
            'form' : form
        }
        return render(request, 'register_app/sign_up.html', context)

    def post(self, request):
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'success_msg': "User Successfully Registered"
        }
        return render(request, 'register_app/sign_up.html', context)
