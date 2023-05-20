from django.urls import path
from . import views

urlpatterns = [
    path('theory', views.learn_theory, name = "learn_theory"),
    path('configuration-steps', views.configuration_steps, name = "configuration_steps"),
]