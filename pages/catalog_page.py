"""
CatalogPage: encapsula las acciones disponibles en la vista del catálogo.

Incluye operaciones como agregar productos al carrito, realizar búsquedas,
filtrar por categoría y leer el contador del carrito.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage


class CatalogPage(BasePage):
    # Selectores de elementos de la vista de catálogo.
    VIEW = (By.ID, "vista-catalogo")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".tarjeta-producto")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".producto-nombre")
    CART_COUNT = (By.ID, "contador-carrito")
    SEARCH_INPUT = (By.ID, "buscador")
    SEARCH_BUTTON = (By.ID, "btn-buscar")
    CATEGORY_FILTER = (By.ID, "filtro-categoria")
    CART_BUTTON = (By.ID, "btn-abrir-carrito")

    # Agrega un producto al carrito usando el nombre del producto.
    def add_product(self, name):
        # El catálogo se dibuja con JavaScript al cargar: se espera a que haya tarjetas.
        cards = self.wait.until(lambda d: d.find_elements(*self.PRODUCT_CARDS))
        for card in cards:
            if name in card.text:
                btn = card.find_element(By.CSS_SELECTOR, ".btn-agregar")
                self.click_element(btn)
                return True
        raise ValueError(f"Producto '{name}' no encontrado en el catálogo")

    # Abre la vista del carrito desde el catálogo.
    def open_cart(self):
        self.click(self.CART_BUTTON)

    # Realiza una búsqueda con el texto provisto.
    def search(self, query):
        self.fill(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)

    # Cambia el filtro de categoría del catálogo.
    def filter_category(self, category):
        select = self.find(self.CATEGORY_FILTER)
        select.send_keys(category)

    # Retorna el número actual de artículos en el contador del carrito.
    def get_cart_count(self):
        return int(self.find(self.CART_COUNT).text)

    # Indica si la vista del catálogo está visible para el usuario.
    def is_displayed(self):
        return self.is_visible(self.VIEW)

    # Nombres de los productos que muestra el catálogo.
    def get_product_names(self):
        self.wait.until(lambda d: d.find_elements(*self.PRODUCT_CARDS))
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]
