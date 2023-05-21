from django.urls import path
from . import views

urlpatterns = [
    path('theory', views.learn_theory, name = "learn_theory"),
    path('configuration-steps', views.configuration_steps, name = "configuration_steps"),
    path('add-number', views.add_number_using_celery_async, name = "add_number"),
    path('check_task_status/', views.check_task_status, name = "check_task_status"),
]