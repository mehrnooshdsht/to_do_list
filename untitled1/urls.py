from django.conf.urls import url
from untitled1 import views


urlpatterns = [
    url(r'^index3/(?P<this_task_id>\d+)/(?P<done>\d+)/(?P<my_id>\d+)/$', views.open2, name="open2"),
    url(r'^$', views.open1, name="open1"),
    url(r'^index$', views.open3, name="open3"),
]
