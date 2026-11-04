"""Fixtures comunes de las pruebas Playwright de TiendaDemo.

pytest-playwright ya provee los fixtures `browser`, `context` y `page`
(un contexto y una pestaña nuevos por cada test, por lo que el carrito
siempre empieza vacío). Aquí se añade el fixture `tienda`, que abre la app
y entrega los Page Objects junto con pasos de preparación reutilizables.
"""

import pytest

from pw_pages import CatalogPage, CartPage, CheckoutPage, ConfirmationPage
from utils.config import BASE_URL
from utils.test_data import CLIENTE_VALIDO


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    # Mismo tamaño de ventana que usaba el DriverFactory de Selenium.
    return {**browser_context_args, "viewport": {"width": 1366, "height": 900}}


class Tienda:
    """Agrupa los Page Objects y los pasos de preparación más usados."""

    def __init__(self, page):
        self.page = page
        self.catalog = CatalogPage(page)
        self.cart = CartPage(page)
        self.checkout = CheckoutPage(page)
        self.confirmation = ConfirmationPage(page)

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


@pytest.fixture
def tienda(page):
    """Abre TiendaDemo en el catálogo (carrito vacío) y devuelve los Page Objects."""
    page.goto(BASE_URL)
    return Tienda(page)
