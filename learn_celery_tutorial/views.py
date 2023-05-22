from django.shortcuts import render
from .tasks import add_numbers
from django.http import JsonResponse
from .forms import AddNumberForm
from django.views import View

# Create your views here.

class LearnTheoryView(View):
    view_name = "learn_theory"
    def get(self, request):
        return render(request, 'learn_celery_tutorial/learn_theory.html')

class ConfigurationStepsView(View):
    view_name = "learn_theory"
    def get(self, request):
        return render(request, 'learn_celery_tutorial/configuration_steps.html')


class AddNumberCeleryTaskView(View):
    view_name = "add_number"
    def get(self, request):
        form = AddNumberForm()
        return render(request, 'learn_celery_tutorial/input_numbers.html', {'form': form})

    def post(self, request):
        form = AddNumberForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['number1']
            num2 = form.cleaned_data['number2']
            result = add_numbers.delay(num1, num2)  # Trigger the task asynchronously
            # result = add_numbers.apply_async(args=(num1, num2), queue='custom_queue')  # Trigger the task asynchronously

            return render(request, 'learn_celery_tutorial/result.html', {'result': result.id})
        else:
            # Form is not valid, render the form with errors
            errors = form.errors.as_data()
            result = errors
            return render(request, 'learn_celery_tutorial/result.html', {'result': result})

class CheckTaskStatusView(View):
    view_name = "check_task_status"
    def get(self, request):
        task_id = request.GET.get('task_id')
        result = add_numbers.AsyncResult(task_id)
        response_data = {'status': result.status}

        if result.status == 'SUCCESS':
            response_data['result'] = result.get()

        return JsonResponse(response_data)