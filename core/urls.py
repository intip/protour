#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from pacote.models import Pacote

from core.views import HomePageView, DestinoView


urlpatterns = patterns(
    'core.views',
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^comprar/(?P<pk>\d+)/$',
        TemplateView.as_view(template_name="comprar.html")),
    url(r'^pacote/(?P<slug>[\w_-]+)/$', DetailView.as_view(
        model=Pacote), name='detalhes'),
    url(r'^destino/(?P<slug>[\w_-]+)/$',
        DestinoView.as_view(),
        name='destino'),
)
