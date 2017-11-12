from django.shortcuts import render
from django.views import generic
from .models import *


# Create your views here.
class About(generic.TemplateView):
    template_name = "About/index.html"

    def get_context_data(self, **kwargs):
        context = {}

        about_items = AboutItems.objects.filter(is_active=True).order_by('-created')
        customers = OurCustomers.objects.all().order_by('-id')

        context['about_items'] = about_items
        context['customers'] = customers

        return context