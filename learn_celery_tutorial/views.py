from django.shortcuts import render

# Create your views here.
def learn_theory(request):
    return render(request, 'learn_celery_tutorial/learn_theory.html')
def configuration_steps(request):
    return render(request, 'learn_celery_tutorial/configuration_steps.html')