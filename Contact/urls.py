from django.conf.urls import url
from . import views


app_name='Contact'
urlpatterns = [
    url(r'^$', views.Contact.as_view(), name='index'),
]