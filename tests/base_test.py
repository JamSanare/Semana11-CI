"""Clase base para las pruebas funcionales Selenium (unittest) de TiendaDemo.

Centraliza la creación del navegador y de los Page Objects, y ofrece pasos
de preparación reutilizables, de modo que cada archivo de test se concentre
en el caso que automatiza.
"""

import unittest

from pages import CatalogPage, CartPage, CheckoutPage, ConfirmationPage
from utils.config import BASE_URL
from utils.driver_factory import DriverFactory
from utils.test_data import CLIENTE_VALIDO


class TiendaDemoTestCase(unittest.TestCase):
    # Un navegador por clase de test (más rápido); el estado se reinicia en setUp.
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_chrome()
        cls.catalog = CatalogPage(cls.driver)
        cls.cart = CartPage(cls.driver)
        cls.checkout = CheckoutPage(cls.driver)
        cls.confirmation = ConfirmationPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Recargar la página reinicia el carrito, que vive solo en memoria.
    def setUp(self):
        self.catalog.open(BASE_URL)

    # --- Pasos de preparación reutilizables ---------------------------------
    def add_products(self, *names):
        for name in names:
            self.catalog.add_product(name)

    def open_cart_with(self, *names):
        self.add_products(*names)
        self.catalog.open_cart()

    def open_checkout_with(self, *names):
        self.open_cart_with(*names)
        self.cart.proceed_to_checkout()

    def buy(self, *names, data=None):
        """Compra completa: agrega productos, rellena el checkout y confirma."""
        self.open_checkout_with(*names)
        self.checkout.fill_form(data or CLIENTE_VALIDO)
        self.checkout.confirm_payment()
