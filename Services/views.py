from django.shortcuts import render
from django.views import generic
from .models import *
from Cases.models import CaseItems


# Create your views here.
class Services(generic.TemplateView):
    template_name = "Services/index.html"

    def get_context_data(self, **kwargs):
        context = {}

        top_services = ServiceItems.objects.all()[:3]
        center_services = ServiceItems.objects.order_by('-id')[:3]
        all_services = ServiceItems.objects.order_by('-id')

        context['top_services'] = top_services
        context['center_services'] = center_services
        context['all_services'] = all_services

        return context


class single_service(generic.DetailView):

    template_name = "Services/single-service.html"
    all_services = ServiceItems.objects.order_by('-id')
    model = ServiceItems
    context_object_name = 'service'
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        related_cases = CaseItems.objects.all().order_by('-created')[:3]

        context = super(single_service, self).get_context_data(**kwargs)
        context['related_cases'] = related_cases

        return context
