from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'calc.html', {'name':'Akash'})

def add(request):

    # val1 = int(request.GET.get('num1','0'))
    # val2 = int(request.GET.get('num2','0'))

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
   
    res = val1 + val2

    return render(request, 'result.html', {'result' : res})