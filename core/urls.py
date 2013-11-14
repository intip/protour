#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView

from pacote.models import Pacote

from core.views import HomePageView, DestinoView, TypeAheadView


urlpatterns = patterns(
    'core.views',
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^comprar/(?P<pk>\d+)/$',
        DetailView.as_view(model=Pacote, template_name="comprar.html"),
        name='comprar'),
    url(r'^pacote/(?P<slug>[\w_-]+)/$', DetailView.as_view(
        model=Pacote), name='detalhes'),
    url(r'^destino/(?P<slug>[\w_-]+)/$',
        DestinoView.as_view(),
        name='destino'),
    url(r'^pacotes\.json$',
        TypeAheadView.as_view(),
        name='typejson'),
)
