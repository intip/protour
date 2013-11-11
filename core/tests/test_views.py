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
        self.resp = self.client.get(r('core:homepage'))

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
