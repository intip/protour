# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from destino.models import Destino
from pacote.models import Pacote


class HomePageView(ListView):
    """
    Main page for the site.
    """
    template_name = "index.html"
    qs = Pacote.objects.filter(destaque=True).filter(publicado=True)
    qs = qs.order_by("data_publicacao")
    queryset = qs


class DestinoView(ListView):
    """
    View for the destino's list.
    """
    template_name = "index.html"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        self.destino = get_object_or_404(Destino, slug=slug)
        qs = Pacote.objects.filter(publicado=True).filter(destino=self.destino)
        qs = qs.order_by("data_publicacao")
        return qs

    def get_context_data(self, **kwargs):
        context = super(DestinoView, self).get_context_data(**kwargs)
        context["destino"] = self.destino
        return context
