from django.shortcuts import render
from .tasks import add_numbers
from django.http import JsonResponse
from .forms import AddNumberForm

# Create your views here.
def learn_theory(request):
    return render(request, 'learn_celery_tutorial/learn_theory.html')
def configuration_steps(request):
    return render(request, 'learn_celery_tutorial/configuration_steps.html')

def add_number_using_celery_async(request):
    form = AddNumberForm()

    if request.method == 'POST':
        form = AddNumberForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['number1']
            num2 = form.cleaned_data['number2']
            result = add_numbers.delay(num1, num2)  # Trigger the task asynchronously
            return render(request, 'learn_celery_tutorial/result.html', {'result': result.id})
        else:
            # Form is not valid, render the form with errors
            errors = form.errors.as_data()
            result = errors
            return render(request, 'learn_celery_tutorial/result.html', {'result': result})

    # if request.GET we Load The Form
    else:
        return render(request, 'learn_celery_tutorial/input_numbers.html', {'form': form})

def check_task_status(request):
    task_id = request.GET.get('task_id')
    result = add_numbers.AsyncResult(task_id)
    response_data = {'status': result.status}

    if result.status == 'SUCCESS':
        response_data['result'] = result.get()

    return JsonResponse(response_data)