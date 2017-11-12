from django.shortcuts import render
from django.views import generic


# Create your views here.
class Contact(generic.TemplateView):
    template_name = "Contact/index.html"

    def get_context_data(self, **kwargs):
        context = {}

        return context