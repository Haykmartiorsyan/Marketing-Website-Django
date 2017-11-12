from django.shortcuts import render
from django.views import generic
from .models import *
from Services.models import ServiceItems

# Create your views here.
class Cases(generic.TemplateView):
    template_name = "Cases/index.html"

    def get_context_data(self, **kwargs):
        context = {}

        case_categoryes = CaseCategory.objects.all()
        cases = CaseItems.objects.all().order_by('-created')

        context['case_categoryes'] = case_categoryes
        context['cases'] = cases

        return context


class single_case(generic.DetailView):

    template_name = "Cases/single-case.html"
    cases = CaseItems.objects.all().order_by('-created')
    model = CaseItems
    context_object_name = 'case'
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        center_services = ServiceItems.objects.order_by('-id')[:3]
        related_cases = CaseItems.objects.all().order_by('-created')[:3]
        context = super(single_case, self).get_context_data(**kwargs)

        context['related_cases'] = related_cases
        context['center_services'] = center_services

        return context