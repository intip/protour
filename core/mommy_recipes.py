#-*- coding:utf-8 -*-

from destino.models import Destino
from pacote.models import Pacote

from model_mommy.recipe import Recipe, foreign_key


belzonte = Recipe(
    Destino,
    titulo="Belo Horizonte"
)


city_tour_bh = Recipe(
    Pacote,
    texto="Aproveite!",
    publicado=True,
    destaque=True,
    destino=foreign_key(belzonte),
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
