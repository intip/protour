# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse as r
from django.test import TestCase

from model_mommy import mommy


class HomePageTest(TestCase):
    """
    Tests the homepage views
    """
    def setUp(self):
        self.tour = mommy.make_recipe('core.city_tour_bh')
        self.tour_unpub = mommy.make_recipe('core.city_tour_bh_despublicado')
        self.tour_unfeat = mommy.make_recipe('core.city_tour_bh_sem_destaque')
        self.resp = self.client.get(r('core:homepage'))
        self.detail_page = self.client.get(
            r("core:detalhes", args=[self.tour.slug]))

    def test_http_status(self):
        """
        Homepage http status should be 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_homepage_template(self):
        """
        Homepage shoud use the 'index.html' template.
        """
        self.assertTemplateUsed(self.resp, "index.html")

    def test_pacote(self):
        """
        Homepage should contain a 'pacote'.
        """
        self.assertIn(self.tour.titulo, self.resp.content.decode("utf8"))

    def test_pacote_despublicado(self):
        """
        Homepage should not contain unpublished 'pacotes'.
        """
        self.assertNotIn(self.tour_unpub.titulo,
                         self.resp.content.decode("utf8"))

    def test_pacote_sem_destaque(self):
        """
        Homepage should not contain unfeatured 'pacotes'.
        """
        self.assertNotIn(self.tour_unfeat.titulo,
                         self.resp.content.decode("utf8"))


class PacoteDetailTest(TestCase):
    """
    Tests for the details page.
    """
    def setUp(self):
        self.tour = mommy.make_recipe('core.city_tour_bh')
        self.detail_page = self.client.get(
            r("core:detalhes", args=[self.tour.slug]))

    def test_pacote_detail(self):
        """
        Pacote's detail page http status should be 200.
        """
        self.assertEqual(200, self.detail_page.status_code)

    def test_pacote_detail_in_page(self):
        """
        Pacote's title should be in the details page.
        """
        self.assertIn(
            self.tour.titulo,
            self.detail_page.content.decode("utf8"))


class DestinoViewTest(TestCase):
    """
    Test for the destino's page.
    """
    def setUp(self):
        self.tour = mommy.make_recipe('core.city_tour_bh')
        self.tour_rondonia = mommy.make_recipe('core.tour_rondonia')
        self.destino = self.tour.destino
        self.resp = self.client.get(
            r("core:destino", args=[self.destino.slug]))

    def test_destino_status(self):
        """
        Destino's page http status should be 200.
        """
        self.assertEqual(self.resp.status_code, 200)

    def test_pacote_in_page(self):
        """
        Pacote of the Destino should be in page.
        """
        self.assertIn(self.tour.titulo, self.resp.content.decode("utf8"))

    def test_other_destino_pacote_not_in_page(self):
        """
        Pacote of other Destino should not be in page.
        """
        self.assertNotIn(
            self.tour_rondonia.titulo,
            self.resp.content.decode("utf8"))


class GlobalViewsTest(TestCase):
    """
    Global pages tests.
    """
    def setUp(self):
        self.tour = mommy.make_recipe('core.city_tour_bh')
        self.resp = self.client.get(r('core:homepage'))

    def test_destinos_in_context(self):
        """
        Pacote's destino should be in the context
        """
        self.assertIn(self.tour.destino, self.resp.context["destinos"])
