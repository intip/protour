#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from core.views import HomePageView


urlpatterns = patterns(
    'core.views',
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^pacote/$', TemplateView.as_view(
        template_name="pacote_details.html")),
    url(r'^comprar/$', TemplateView.as_view(template_name="comprar.html")),
)
