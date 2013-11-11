#-*- coding:utf-8 -*-

from pacote.models import Pacote

from model_mommy.recipe import Recipe

city_tour_bh = Recipe(
    Pacote,
    titulo=u"City Tour BH",
    texto="Aproveite!",
    publicado=True,
)
