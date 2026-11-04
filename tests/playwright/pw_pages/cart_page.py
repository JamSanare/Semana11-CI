"""CartPage (Playwright): filas del carrito, cantidades, cupones y resumen."""

import re

from utils.test_data import parse_price
from .base_page import BasePage


class CartPage(BasePage):
    VIEW = "#vista-carrito"
    EMPTY_MESSAGE = "#carrito-vacio"
    ITEM_ROWS = ".item-carrito"
    ITEM_NAMES = ".item-nombre"
    ITEM_SUBTOTALS = ".item-subtotal"
    QUANTITY_INPUTS = ".item-carrito input"
    COUPON_INPUT = "#input-cupon"
    COUPON_BUTTON = "#btn-aplicar-cupon"
    COUPON_MESSAGE = "#msg-cupon"
    CHECKOUT_BUTTON = "#btn-ir-checkout"
    EMPTY_CART_BUTTON = "#btn-vaciar-carrito"
    SUBTOTAL = "#valor-subtotal"
    TOTAL = "#valor-total"
    DISCOUNT_ROW = "#fila-descuento"
    DISCOUNT_VALUE = "#valor-descuento"

    # Fila del carrito del producto indicado (Locator; puede no existir).
    def item_row(self, name):
        nombre = self.page.locator(self.ITEM_NAMES, has_text=re.compile(f"^{re.escape(name)}$"))
        return self.page.locator(self.ITEM_ROWS).filter(has=nombre)

    def has_item(self, name):
        return self.item_row(name).count() > 0

    def get_item_names(self):
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def get_quantity(self, name):
        row = self.item_row(name)
        if row.count() == 0:
            return 0
        return int(row.locator(".cantidad-num").inner_text())

    def get_item_subtotal(self, name):
        return parse_price(self.item_row(name).locator(".item-subtotal").inner_text())

    def sum_item_subtotals(self):
        return sum(parse_price(t) for t in self.page.locator(self.ITEM_SUBTOTALS).all_inner_texts())

    def increase_quantity(self, name):
        row = self.item_row(name)
        if row.count():
            row.locator(".btn-cantidad[data-accion='mas']").click()

    def decrease_quantity(self, name):
        row = self.item_row(name)
        if row.count():
            row.locator(".btn-cantidad[data-accion='menos']").click()

    def has_quantity_input(self):
        return self.exists(self.QUANTITY_INPUTS)

    def remove_item(self, name):
        row = self.item_row(name)
        if row.count():
            row.locator(".btn-eliminar").click()

    def apply_coupon(self, code):
        self.page.locator(self.COUPON_INPUT).fill(code)
        self.page.locator(self.COUPON_BUTTON).click()

    def get_coupon_message(self):
        return self.page.locator(self.COUPON_MESSAGE).inner_text()

    def get_subtotal(self):
        return parse_price(self.page.locator(self.SUBTOTAL).inner_text())

    def get_total(self):
        return parse_price(self.page.locator(self.TOTAL).inner_text())

    def has_discount(self):
        return self.exists(self.DISCOUNT_ROW)

    def get_discount(self):
        if not self.has_discount():
            return 0.0
        return parse_price(self.page.locator(self.DISCOUNT_VALUE).inner_text())

    def get_discount_row_text(self):
        return self.text_of(self.DISCOUNT_ROW)

    def proceed_to_checkout(self):
        self.page.locator(self.CHECKOUT_BUTTON).click()

    def has_checkout_button(self):
        return self.exists(self.CHECKOUT_BUTTON)

    def empty_cart(self):
        self.page.locator(self.EMPTY_CART_BUTTON).click()

    def has_empty_message(self):
        return self.exists(self.EMPTY_MESSAGE)

    def is_displayed(self):
        return self.is_visible(self.VIEW)
