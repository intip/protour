# -*- coding:utf-8 -*-

from django.views.generic import ListView

from pacote.models import Pacote


class HomePageView(ListView):
    """
    Main page for the site.
    """
    template_name = "index.html"
    queryset = Pacote.objects.filter(destaque=True).filter(publicado=True)
