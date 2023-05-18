from django.shortcuts import render
from django.views import View
from .utils import FlexboxTutorialsUtils


def learn_flexbox_horizontal(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-horizontal.html')

def learn_flexbox_vertical(request):
    return render(request, 'flexbox_tutorial/learn-flexbox-vertical.html')

class ShowFlexboxCodeView(View):
    view_name = 'show_flexbox_code'
    def get(self, request, code_id):
        flexbox_tutorial_utils = FlexboxTutorialsUtils()
        code_str = flexbox_tutorial_utils.getCodeFromFlexboxTutorialName(code_id)

        context = {'code_str': code_str}
        return render(request, 'flexbox_tutorial/show-flexbox-code.html', context)