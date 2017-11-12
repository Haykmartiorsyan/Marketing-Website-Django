from django.shortcuts import render
from django.views import generic
from .models import *
from Services.models import ServiceItems

# Create your views here.
class Home(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = {}
        slider_images = Slider.objects.filter(is_active=True).order_by('-id')
        testimonials = Testimonials.objects.filter(is_active=True).order_by('-id')
        top_services = ServiceItems.objects.all()[:3]
        center_services = ServiceItems.objects.order_by('-id')[:3]
        all_services = ServiceItems.objects.order_by('-id')

        context['slider_images'] = slider_images
        context['testimonials'] = testimonials
        context['top_services'] = top_services
        context['center_services'] = center_services
        context['all_services'] = all_services

        return context