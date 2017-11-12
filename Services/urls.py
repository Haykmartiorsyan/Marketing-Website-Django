from django.conf.urls import url
from . import views


app_name='Services'
urlpatterns = [
    url(r'^$', views.Services.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.single_service.as_view(), name="single-service"),

]