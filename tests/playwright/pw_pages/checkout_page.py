"""CheckoutPage (Playwright): formulario de envío, método de pago y validaciones."""

from utils.test_data import CLIENTE_VALIDO, parse_price
from .base_page import BasePage


class CheckoutPage(BasePage):
    VIEW = "#vista-checkout"
    NAME_INPUT = "#campo-nombre"
    EMAIL_INPUT = "#campo-email"
    ADDRESS_INPUT = "#campo-direccion"
    CITY_INPUT = "#campo-ciudad"
    PHONE_INPUT = "#campo-telefono"
    PAY_BUTTON = "#btn-confirmar-pago"
    TOTAL = "#total-checkout"
    ERROR_MESSAGES = ".error-campo.visible"

    # Mensaje de error asociado a cada campo del formulario.
    FIELD_ERRORS = {
        "nombre": "#error-nombre",
        "email": "#error-email",
        "direccion": "#error-direccion",
        "ciudad": "#error-ciudad",
        "telefono": "#error-telefono",
    }

    # fill() de Playwright limpia el campo antes de escribir; con "" lo deja vacío.
    def fill_shipping_info(self, name, email, address, city, phone):
        self.page.locator(self.NAME_INPUT).fill(name)
        self.page.locator(self.EMAIL_INPUT).fill(email)
        self.page.locator(self.ADDRESS_INPUT).fill(address)
        self.page.locator(self.CITY_INPUT).fill(city)
        self.page.locator(self.PHONE_INPUT).fill(phone)

    def fill_form(self, data=None):
        self.fill_shipping_info(**(data or CLIENTE_VALIDO))

    def select_payment_method(self, method_value):
        self.page.locator(f".opcion-pago input[type='radio'][value='{method_value}']").check()

    def confirm_payment(self):
        self.page.locator(self.PAY_BUTTON).click()

    def get_error_messages(self):
        return self.page.locator(self.ERROR_MESSAGES).all_inner_texts()

    def get_fields_with_error(self):
        return [field for field, sel in self.FIELD_ERRORS.items() if self.is_visible(sel)]

    def get_field_error(self, field):
        return self.text_of(self.FIELD_ERRORS[field])

    def get_total(self):
        return parse_price(self.page.locator(self.TOTAL).inner_text())

    def is_displayed(self):
        return self.is_visible(self.VIEW)
