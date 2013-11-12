#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from pacote.models import Pacote, Variacao


from core.views import HomePageView


urlpatterns = patterns(
    'core.views',
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^comprar/(?P<pk>\d+)/$',
        TemplateView.as_view(template_name="comprar.html")),
    url(r'^pacote/(?P<pk>\d+)/$', DetailView.as_view(
        model=Pacote), name='detalhes'),
)
