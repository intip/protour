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
    queryset = Pacote.objects.filter(destaque=True).filter(publicado=True)


class DestinoView(ListView):
    """
    View for the destino's list.
    """
    template_name = "index.html"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        destino = get_object_or_404(Destino, slug=slug)
        return Pacote.objects.filter(publicado=True).filter(destino=destino)
