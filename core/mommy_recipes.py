#-*- coding:utf-8 -*-

from destino.models import Destino
from pacote.models import Pacote

from model_mommy.recipe import Recipe, foreign_key


belzonte = Recipe(
    Destino,
    titulo="Belo Horizonte"
)

rondonia = Recipe(
    Destino,
    titulo="Rondonia"
)

city_tour_bh = Recipe(
    Pacote,
    texto="Aproveite!",
    publicado=True,
    destaque=True,
    destino=foreign_key(belzonte),
    preco_por=100.40
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

tour_rondonia = Recipe(
    Pacote,
    texto="Aproveite!",
    publicado=True,
    destaque=True,
    destino=foreign_key(rondonia)
)
