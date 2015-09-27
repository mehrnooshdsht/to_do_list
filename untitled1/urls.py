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
    # url(r'^index/[0-2]/$', views.add_list, name="add_list"),
    # modify la8ter in one url one def
    url(r'^index3/(?P<my_id>\d+)/$', views.open2, name="open2"),
    # url(r'^index3$', views.open2, name="open2"),
    # url(r'open2$', views.open2, name="open2"),7
    url(r'index2$', views.open1, name="open1"),
    # url(r'index3$', views.add_task, name="add_task"),
    url(r'^index$', views.open3, name="open3"),
    # url(r'^add/(?P<id>\d+)/$', views.add, name="add"),
    # url(r'^delete/(?P<id>\d+)/$', views.delete, name="delete"),
    # url(r'^done_remove_task$', views.done_remove_task, name="done_remove_task"),
    # url(r'^show_task/(?P<id>\d+)/$', views.show_task, name="show_task"),
]
