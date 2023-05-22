from django.urls import path
from . import views

urlpatterns = [
    path('theory', views.LearnTheoryView.as_view(), name = views.LearnTheoryView.view_name),
    path('configuration-steps', views.ConfigurationStepsView.as_view(), name = views.ConfigurationStepsView.view_name),
    path('add-number', views.AddNumberCeleryTaskView.as_view(), name = views.AddNumberCeleryTaskView.view_name),
    path('check_task_status/', views.CheckTaskStatusView.as_view(), name = views.CheckTaskStatusView.view_name),
]