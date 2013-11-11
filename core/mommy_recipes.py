#-*- coding:utf-8 -*-

from pacote.models import Pacote

from model_mommy.recipe import Recipe

city_tour_bh = Recipe(
    Pacote,
    texto="Aproveite!",
    publicado=True,
    destaque=True,
)

city_tour_bh_despublicado = Recipe(
    Pacote,
    texto="Aproveite!",
    publicado=False,
    destaque=True,
)

city_tour_bh_sem_destaque = Recipe(
    Pacote,
    texto="Aproveite!",
    publicado=True,
    destaque=False,
)
