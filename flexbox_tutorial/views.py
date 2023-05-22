from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .utils import FlexboxTutorialsUtils

# extends Normal Class-based `View`
class HorizontalTutorialView(View):
    view_name = 'learn_flexbox_horizontal'
    def get(self, request):
        return render(request, 'flexbox_tutorial/learn-flexbox-horizontal.html')

# extends class-based `TemplateView`
class VerticalTutorialTemplateView(TemplateView):
    view_name = 'learn_flexbox_vertical'
    template_name = "flexbox_tutorial/learn-flexbox-vertical.html"


# By default, the TemplateView class in Django is intended for handling GET requests and rendering templates.
# It does not provide built-in support for handling POST requests.
class ShowFlexboxCodeView(TemplateView):
    view_name = 'show_flexbox_code'
    template_name = "flexbox_tutorial/show-flexbox-code.html"

    def get_context_data(self, **kwargs):
        # we call the PARENT CLASS method(super().get_context_data(**kwargs)) to get the default context data.
        context = super().get_context_data(**kwargs)

        flexbox_tutorial_utils = FlexboxTutorialsUtils()
        code_id = self.kwargs.get('code_id')
        code_str = flexbox_tutorial_utils.getCodeFromFlexboxTutorialName(code_id)

        context['code_str'] = code_str

        return context