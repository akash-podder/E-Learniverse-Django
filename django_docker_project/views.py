from django.shortcuts import render

def learn_flexbox_horizontal(request):
    return render(request, 'mainApp/learn-flexbox-horizontal.html')
def learn_flexbox_vertical(request):
    return render(request, 'mainApp/learn-flexbox-vertical.html')