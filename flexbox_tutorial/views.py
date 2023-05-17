from django.shortcuts import render
from django.views import View


def learn_flexbox_horizontal(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-horizontal.html')

def learn_flexbox_vertical(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-vertical.html')

class ShowFlexboxCodeView(View):
    view_name = 'show_flexbox_code'
    def get(self, request, link_id):
        return render(request, 'flexbox_tutorial/learn-flexbox-vertical.html')