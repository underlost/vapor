from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('',
   url(r'^$', TemplateView.as_view(template_name="core/frontpage.html"), name="home"),
   url(r'^id/(?P<steam_id>[\w-]+)/?$', views.VaporProfile, name="Profile"),
   url(r'^id/(?P<steam_id>[\w-]+)/tf2/?$', views.VaporTF2Backback, name="tf2backpack"),
)
