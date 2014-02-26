#-*- coding:utf-8 -*-
import time

from django.core.urlresolvers import reverse as r
from django.test import LiveServerTestCase

from model_mommy import mommy
from splinter.browser import Browser


class ProtourFeatureTest(LiveServerTestCase):
    fixtures = ['site_data.json']

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('phantomjs')
        super(ProtourFeatureTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(ProtourFeatureTest, cls).tearDownClass()

    def setUp(self):
        self.tour = mommy.make_recipe('core.city_tour_bh')
        self.index_page = r('core:homepage')
        self.detail_page = r('core:detalhes', args=[self.tour.slug])
        self.cart_page = r('core:comprar', args=[self.tour.pk])

    def test_pacote_link(self):
        """
        Should be able to go to the 'pacote' page by anchor clicking.
        """
        self.browser.visit(self.live_server_url + self.index_page)
        time.sleep(3)
        self.browser.find_link_by_text(self.tour.titulo).click()
        self.assertEqual(
            self.live_server_url + self.detail_page,
            self.browser.url)

    def test_pacote_h1(self):
        """
        Details page's h1 should be the pacote's title.

        This is a SEO mandatory item.
        """
        self.browser.visit(self.live_server_url + self.detail_page)
        self.assertEqual(
            self.tour.titulo,
            self.browser.find_by_css('h1')[0].text)

    # def test_destino_in_page(self):
    #     """
    #     Destino's link should be in the Homepage.
    #     """
    #     self.browser.visit(self.live_server_url + self.index_page)
    #     assert self.browser.find_link_by_text(self.tour.destino)

    # def test_comprar_page(self):
    #     """
    #     Buy page should show the pacotes's value
    #     """
    #     self.browser.visit(self.live_server_url + self.cart_page)
    #     preco_esperado = "R$ %.2f" % (self.tour.preco_por, )
    #     preco_esperado = preco_esperado.replace('.', ',')
    #     self.assertEqual(
    #         preco_esperado,
    #         self.browser.find_by_css('h4')[0].text)

    # def test_qtde_comprar_page(self):
    #     """
    #     Should see qtty = 1 when click to buy a pacote's
    #     """
    #     self.browser.visit(self.live_server_url + self.cart_page)
    #     self.assertEqual("1", self.browser.find_by_name('qtty')[0].value)
