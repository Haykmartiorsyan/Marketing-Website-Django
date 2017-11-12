from django.conf.urls import url
from . import views


app_name='Cases'
urlpatterns = [
    url(r'^$', views.Cases.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.single_case.as_view(), name="single-case"),
]