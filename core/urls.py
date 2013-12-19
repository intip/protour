#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView

from pacote.models import Pacote

from core.views import HomePageView, DestinoView, TypeAheadView, ComprarView,\
    SearchView, EstadoView, RegiaoView, PaisView


urlpatterns = patterns(
    'core.views',
    url(r'^$', HomePageView.as_view(), name='homepage'),

    url(r'^comprar/(?P<pk>\d+)/$',
        ComprarView.as_view(),
        name='comprar'),

    url(r'^pacote/(?P<slug>[\w_-]+)/$', DetailView.as_view(
        model=Pacote), name='detalhes'),

    url(r'^destino/(?P<slug>[\w_-]+)/$',
        DestinoView.as_view(),
        name='destino'),

    url(r'^estado/(?P<slug>[\w_-]+)/$',
        EstadoView.as_view(),
        name='estado'),

    url(r'^regiao/(?P<slug>[\w_-]+)/$',
        RegiaoView.as_view(),
        name='regiao'),

    url(r'^pais/(?P<slug>[\w_-]+)/$',
        PaisView.as_view(),
        name='pais'),

    url(r'^pacotes\.json$',
        TypeAheadView.as_view(),
        name='typejson'),

    url(r'^busca/$', SearchView.as_view(), name="search"),
)
