"""
CheckoutPage: maneja la vista de pago y la validación del formulario.

Este objeto ofrece métodos para completar los datos de envío, seleccionar el
método de pago y confirmar la orden.
"""

from selenium.webdriver.common.by import By
from utils.test_data import CLIENTE_VALIDO, parse_price
from .base_page import BasePage


class CheckoutPage(BasePage):
    # Selectores de elementos de la vista de checkout.
    VIEW = (By.ID, "vista-checkout")
    NAME_INPUT = (By.ID, "campo-nombre")
    EMAIL_INPUT = (By.ID, "campo-email")
    ADDRESS_INPUT = (By.ID, "campo-direccion")
    CITY_INPUT = (By.ID, "campo-ciudad")
    PHONE_INPUT = (By.ID, "campo-telefono")
    PAYMENT_OPTIONS = (By.CSS_SELECTOR, ".opcion-pago input[type='radio']")
    PAY_BUTTON = (By.ID, "btn-confirmar-pago")
    TOTAL = (By.ID, "total-checkout")
    ERROR_MESSAGES = (By.CSS_SELECTOR, ".error-campo.visible")

    # Mensaje de error asociado a cada campo del formulario.
    FIELD_ERRORS = {
        "nombre": (By.ID, "error-nombre"),
        "email": (By.ID, "error-email"),
        "direccion": (By.ID, "error-direccion"),
        "ciudad": (By.ID, "error-ciudad"),
        "telefono": (By.ID, "error-telefono"),
    }

    # Completa los datos de envío requeridos en el formulario.
    def fill_shipping_info(self, name, email, address, city, phone):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.ADDRESS_INPUT, address)
        self.fill(self.CITY_INPUT, city)
        self.fill(self.PHONE_INPUT, phone)

    # Completa el formulario con un diccionario de datos (por defecto, válidos).
    def fill_form(self, data=None):
        self.fill_shipping_info(**(data or CLIENTE_VALIDO))

    # Selecciona un método de pago por su valor.
    def select_payment_method(self, method_value):
        radios = self.driver.find_elements(*self.PAYMENT_OPTIONS)
        for radio in radios:
            if radio.get_attribute("value") == method_value:
                self.click_element(radio)
                return
        raise ValueError(f"Método de pago '{method_value}' no encontrado")

    # Confirma el pago en el checkout.
    def confirm_payment(self):
        self.click(self.PAY_BUTTON)

    # Devuelve los mensajes de error visibles tras validación.
    def get_error_messages(self):
        return [el.text for el in self.driver.find_elements(*self.ERROR_MESSAGES)]

    # Nombres de los campos que muestran un error en este momento.
    def get_fields_with_error(self):
        return [field for field, locator in self.FIELD_ERRORS.items() if self.is_visible(locator)]

    # Texto del error de un campo concreto.
    def get_field_error(self, field):
        return self.text_of(self.FIELD_ERRORS[field])

    # Total que muestra el resumen del checkout.
    def get_total(self):
        return parse_price(self.find(self.TOTAL).text)

    # Indica si la vista de checkout está visible para el usuario.
    def is_displayed(self):
        return self.is_visible(self.VIEW)
