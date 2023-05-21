from django.shortcuts import render
from .tasks import add_numbers
from django.http import JsonResponse

# Create your views here.
def learn_theory(request):
    return render(request, 'learn_celery_tutorial/learn_theory.html')
def configuration_steps(request):
    return render(request, 'learn_celery_tutorial/configuration_steps.html')
def add_number_using_celery_async(request):
    a = 3
    b = 4
    result = add_numbers.delay(a, b)  # Trigger the task asynchronously
    return render(request, 'learn_celery_tutorial/result.html',{'result': result.id})

def check_task_status(request):
    task_id = request.GET.get('task_id')
    result = add_numbers.AsyncResult(task_id)
    response_data = {'status': result.status}

    if result.status == 'SUCCESS':
        response_data['result'] = result.get()

    return JsonResponse(response_data)