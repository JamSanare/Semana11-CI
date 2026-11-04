"""CatalogPage (Playwright): vista del catálogo y contador del carrito."""

from .base_page import BasePage


class CatalogPage(BasePage):
    VIEW = "#vista-catalogo"
    PRODUCT_CARDS = ".tarjeta-producto"
    PRODUCT_NAMES = ".producto-nombre"
    CART_COUNT = "#contador-carrito"
    SEARCH_INPUT = "#buscador"
    SEARCH_BUTTON = "#btn-buscar"
    CATEGORY_FILTER = "#filtro-categoria"
    CART_BUTTON = "#btn-abrir-carrito"

    # Pulsa "Agregar al carrito" en la tarjeta cuyo nombre coincide exactamente.
    def add_product(self, name):
        card = self.page.locator(self.PRODUCT_CARDS).filter(
            has=self.page.get_by_text(name, exact=True))
        card.locator(".btn-agregar").click()

    def open_cart(self):
        self.page.locator(self.CART_BUTTON).click()

    def search(self, query):
        self.page.locator(self.SEARCH_INPUT).fill(query)
        self.page.locator(self.SEARCH_BUTTON).click()

    def filter_category(self, category):
        self.page.locator(self.CATEGORY_FILTER).select_option(category)

    def get_cart_count(self):
        return int(self.page.locator(self.CART_COUNT).inner_text())

    def is_displayed(self):
        return self.is_visible(self.VIEW)

    def get_product_names(self):
        self.page.locator(self.PRODUCT_CARDS).first.wait_for()
        return self.page.locator(self.PRODUCT_NAMES).all_inner_texts()
