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
            r("core:detalhes", args=[self.tour.pk]))

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
