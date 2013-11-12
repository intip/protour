# -*- coding:utf-8 -*-

from django.test import TestCase

from model_mommy import mommy

from pacote.models import Pacote


class ModelNameTests(TestCase):
    """
    """

    def test_promocao_creation(self):
        """
        Should be able to create a 'Pacote' with preco_de and preco_por.
        """
        mommy.make(Pacote,
                   texto="c",
                   preco_de=120.10,
                   preco_por=120.10)
