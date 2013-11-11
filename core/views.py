# -*- coding:utf-8 -*-

from django.views.generic import ListView

from pacote.models import Pacote


class HomePageView(ListView):
    """
    Main page for the site.
    """
    model = Pacote
    template_name = "index.html"
