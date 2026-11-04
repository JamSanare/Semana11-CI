"""
CartPage: encapsula la interacción con la vista del carrito de compras.

Permite leer los elementos del carrito, modificar cantidades, aplicar cupones,
eliminar productos y avanzar al checkout.
"""

from selenium.webdriver.common.by import By
from utils.test_data import parse_price
from .base_page import BasePage


class CartPage(BasePage):
    # Selectores de elementos de la vista del carrito.
    VIEW = (By.ID, "vista-carrito")
    EMPTY_MESSAGE = (By.ID, "carrito-vacio")
    ITEM_ROWS = (By.CSS_SELECTOR, ".item-carrito")
    ITEM_NAMES = (By.CSS_SELECTOR, ".item-nombre")
    ITEM_SUBTOTALS = (By.CSS_SELECTOR, ".item-subtotal")
    QUANTITY_INPUTS = (By.CSS_SELECTOR, ".item-carrito input")
    COUPON_INPUT = (By.ID, "input-cupon")
    COUPON_BUTTON = (By.ID, "btn-aplicar-cupon")
    COUPON_MESSAGE = (By.ID, "msg-cupon")
    CHECKOUT_BUTTON = (By.ID, "btn-ir-checkout")
    EMPTY_CART_BUTTON = (By.ID, "btn-vaciar-carrito")
    SUBTOTAL = (By.ID, "valor-subtotal")
    TOTAL = (By.ID, "valor-total")
    DISCOUNT_ROW = (By.ID, "fila-descuento")
    DISCOUNT_VALUE = (By.ID, "valor-descuento")

    # Devuelve la fila del carrito que contiene el producto indicado.
    def get_item_row(self, name):
        for row in self.driver.find_elements(*self.ITEM_ROWS):
            if name in row.text:
                return row
        return None

    # Devuelve los nombres de todos los productos que hay en el carrito.
    def get_item_names(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    # Devuelve la cantidad actual de un producto en el carrito.
    def get_quantity(self, name):
        row = self.get_item_row(name)
        if not row:
            return 0
        return int(row.find_element(By.CSS_SELECTOR, ".cantidad-num").text)

    # Devuelve el subtotal de la fila de un producto (precio × cantidad).
    def get_item_subtotal(self, name):
        row = self.get_item_row(name)
        return parse_price(row.find_element(By.CSS_SELECTOR, ".item-subtotal").text)

    # Suma de los subtotales de todas las filas, tal como los ve el usuario.
    def sum_item_subtotals(self):
        return sum(parse_price(el.text) for el in self.driver.find_elements(*self.ITEM_SUBTOTALS))

    # Aumenta la cantidad de un producto existente en el carrito.
    def increase_quantity(self, name):
        row = self.get_item_row(name)
        if row:
            self.click_element(row.find_element(By.CSS_SELECTOR, ".btn-cantidad[data-accion='mas']"))

    # Disminuye la cantidad de un producto existente en el carrito.
    def decrease_quantity(self, name):
        row = self.get_item_row(name)
        if row:
            self.click_element(row.find_element(By.CSS_SELECTOR, ".btn-cantidad[data-accion='menos']"))

    # Indica si la interfaz ofrece algún campo editable para escribir cantidades.
    def has_quantity_input(self):
        return self.exists(self.QUANTITY_INPUTS)

    # Elimina un producto del carrito.
    def remove_item(self, name):
        row = self.get_item_row(name)
        if row:
            self.click_element(row.find_element(By.CSS_SELECTOR, ".btn-eliminar"))

    # Aplica un código de cupón en el carrito.
    def apply_coupon(self, code):
        self.fill(self.COUPON_INPUT, code)
        self.click(self.COUPON_BUTTON)

    # Devuelve el mensaje que aparece al aplicar el cupón.
    def get_coupon_message(self):
        return self.find(self.COUPON_MESSAGE).text

    # Subtotal, total y descuento tal como los muestra el resumen del pedido.
    def get_subtotal(self):
        return parse_price(self.find(self.SUBTOTAL).text)

    def get_total(self):
        return parse_price(self.find(self.TOTAL).text)

    def has_discount(self):
        return self.exists(self.DISCOUNT_ROW)

    def get_discount(self):
        return parse_price(self.find(self.DISCOUNT_VALUE).text) if self.has_discount() else 0.0

    def get_discount_row_text(self):
        return self.text_of(self.DISCOUNT_ROW)

    # Avanza desde el carrito hacia el checkout.
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    # Indica si la opción de proceder al pago está disponible.
    def has_checkout_button(self):
        return self.exists(self.CHECKOUT_BUTTON)

    # Vacía el carrito por completo.
    def empty_cart(self):
        self.click(self.EMPTY_CART_BUTTON)

    # Verifica si se muestra el mensaje de carrito vacío.
    def has_empty_message(self):
        return len(self.driver.find_elements(*self.EMPTY_MESSAGE)) > 0

    # Indica si la vista del carrito está visible para el usuario.
    def is_displayed(self):
        return self.is_visible(self.VIEW)
