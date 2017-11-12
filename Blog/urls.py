from django.conf.urls import url
from . import views


app_name='Blog'
urlpatterns = [
    url(r'^$', views.Blog, name='index'),
    url(r'^(?P<pk>\d+)/$', views.single_post.as_view(), name="single-post"),

]