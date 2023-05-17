from django.shortcuts import render

def learn_flexbox_horizontal(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-horizontal.html')

def learn_flexbox_vertical(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-vertical.html')

def show_flexbox_code(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-vertical.html')