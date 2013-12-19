# -*- coding:utf-8 -*-

import json

from django.core.urlresolvers import reverse as r
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View, TemplateView
from django.views.generic.detail import DetailView

import watson

from configuracao.models import FormaPagamento
from destino.models import Destino, Estado, Regiao, Pais
from pacote.models import Pacote, Variacao


class HomePageView(ListView):
    """
    Main page for the site.
    """
    template_name = "index.html"
    qs = Pacote.objects.filter(destaque=True).filter(publicado=True)
    qs = qs.order_by("data_publicacao")
    queryset = qs
    paginate_by = "10"


class DestinoView(ListView):
    """
    View for the destino's list.
    """
    template_name = "index.html"
    paginate_by = "10"
    model = Destino
    field = "destino"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.destino = get_object_or_404(self.model, slug=slug)
        query = {self.field: self.destino}
        qs = Pacote.objects.filter(publicado=True).filter(**query)
        qs = qs.order_by("data_publicacao")
        return qs

    def get_context_data(self, **kwargs):
        context = super(DestinoView, self).get_context_data(**kwargs)
        context["destino"] = self.destino
        return context


class EstadoView(DestinoView):
    model = Estado
    field = "destino__estado"


class RegiaoView(DestinoView):
    model = Regiao
    field = "destino__estado__regiao"


class PaisView(DestinoView):
    model = Pais
    field = "destino__pais"


class ComprarView(DetailView):
    model = Variacao
    template_name = "comprar.html"

    def get_context_data(self, **kwargs):
        context = super(ComprarView, self).get_context_data(**kwargs)
        context["pagamento"] = FormaPagamento.objects.get_singleton()
        return context


class TypeAheadView(View):
    """
    """
    response_class = HttpResponse

    def get(self, request, **response_kwargs):
        self.queryset = Pacote.objects.filter(publicado=True)
        pacotes = []
        for pacote in self.queryset:
            url = r("core:detalhes", args=[pacote.slug])
            tokens = pacote.titulo.split()
            tokens += pacote.destino.titulo.split()
            tokens = list(set(tokens))
            datum = {
                "value": pacote.titulo,
                "url": url,
                "tokens": tokens
            }
            pacotes.append(datum)
        response = json.dumps(pacotes)
        return self.response_class(response, **response_kwargs)


class SearchView(TemplateView):
    """
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        kwargs = self.request.GET
        query = kwargs.get("q", "")
        pacotes = watson.search(query)
        context["object_list"] = [i.object for i in pacotes]
        context["query"] = query
        return context
