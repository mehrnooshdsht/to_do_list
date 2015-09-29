# """untitled1 URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.8/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Add an import:  from blog import urls as blog_urls
#     2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
# """

from django.conf.urls import url
from untitled1 import views

urlpatterns = [
    url(r'^index3/(?P<this_task_id>\d+)/(?P<done>\d+)/(?P<my_id>\d+)/$', views.open2, name="open2"),
    url(r'index2$', views.open1, name="open1"),
    url(r'^index$', views.open3, name="open3"),
]
