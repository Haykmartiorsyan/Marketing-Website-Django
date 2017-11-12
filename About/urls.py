from django.conf.urls import url
from . import views


app_name='About'
urlpatterns = [
    url(r'^$', views.About.as_view(), name='index'),
]