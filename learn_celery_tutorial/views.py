from celery.result import AsyncResult
from django.shortcuts import render
from .tasks import *
from .models import *
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from .forms import AddNumberForm
from django.views import View
from django.core.cache import cache
from django_celery_beat.models import CrontabSchedule, PeriodicTask, IntervalSchedule

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
            result = add_numbers_shared_task.delay(num1, num2)  # Trigger the task asynchronously
            # result = add_numbers.apply_async(args=(num1, num2), queue='custom_queue')  # Trigger the task asynchronously

            return render(request, 'learn_celery_tutorial/result.html', {'result': result.id})
        else:
            # Form is not valid, render the form with errors
            errors = form.errors.as_data()
            result = errors
            return render(request, 'learn_celery_tutorial/result.html', {'result': result})

class NumberCounterPeriodicCeleryBeatScheduledTaskView(View):
    view_name = "clock_scheduled"
    def get(self, request):
        # task_result = number_counter_using_celery_beat_task.delay(7)
        # Wait for the task to complete
        # task_result.wait()
        # result = task_result.result

        # Retrieve the cache data
        result = cache.get('custom_cache_key')

        return render(request, 'learn_celery_tutorial/number_counter_celery_beat.html', {'result': result})

class OneTimeTaskView(View):
    view_name = "one_time_task"
    def get(self, request):
        # Calculate the desired execution time
        execution_time = datetime.now() + timedelta(seconds=6)  # Example: 6 seconds from now

        # Schedule the task to run at the desired time
        result = one_time_task.apply_async(eta=execution_time)
        one_time_task_context = "one-time-task"

        context = {
            'one_time_task_context': one_time_task_context,
            'result' : result
        }

        return render(request, 'learn_celery_tutorial/number_counter_celery_beat.html', context)

class UserPushScheduledCeleryTask(View):
    view_name = "user_push_scheduled_celery_task"
    def get(self, request):
        return render(request, 'learn_celery_tutorial/user_push_scheduled_celery_view.html')

    def post(self, request):
        try:
            periodic_task = PeriodicTask.objects.get(name="User_Periodic_Task") # Task with the specified name found

        except PeriodicTask.DoesNotExist:

            # `PeriodicTask` Model table sobsomoy `IntervalSchedule` Object Argument hisave ney... eijonno ei Object ta Create kora lagtese
            interval_schedule, _ = IntervalSchedule.objects.get_or_create(
                every=int(6),
                period=IntervalSchedule.SECONDS
            )
            # Create a new PeriodicTask object
            periodic_task = PeriodicTask.objects.create(
                name='User_Periodic_Task',
                task='learn_celery_tutorial.user_push_scheduled_celery_task',
                interval=interval_schedule,  # Set the task interval
                enabled=True  # Enable the task
            )
            periodic_task.save()

        # Get the result of the `periodic_task`
        result = AsyncResult(periodic_task.id)

        context = {
            'result': result
        }

        return render(request, 'learn_celery_tutorial/user_push_scheduled_celery_view.html', context)



# JavaScript AJAX will Call this Api
class GetPeriodicTaskResult(View):
    view_name = "get_periodic_task_result"
    def get(self, request):
        try:
            task_result = UserPushedTaskResult.objects.latest('created_at')
            context = task_result.result
            return JsonResponse({'result': context})
        except UserPushedTaskResult.DoesNotExist:
            context = 'Task result not found'
            return JsonResponse({'result': context})


# JavaScript AJAX will Call this Api
class CheckTaskStatusView(View):
    view_name = "check_task_status"
    def get(self, request):
        task_id = request.GET.get('task_id')
        result = add_numbers_shared_task.AsyncResult(task_id)
        response_data = {'status': result.status}

        if result.status == 'SUCCESS':
            response_data['result'] = result.get()

        return JsonResponse(response_data)

class GetCounterNumberFromCacheView(View):
    view_name = "counter_number_from_cache"

    def get(self, request):
        result = cache.get('custom_cache_key')
        response_data = {'result': result}
        return JsonResponse(response_data)