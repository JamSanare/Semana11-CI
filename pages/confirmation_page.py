"""
ConfirmationPage: pantalla que se muestra después de confirmar una compra.
"""

from selenium.webdriver.common.by import By
from utils.test_data import parse_price
from .base_page import BasePage


class ConfirmationPage(BasePage):
    VIEW = (By.ID, "vista-confirmacion")
    TITLE = (By.ID, "msg-confirmacion")
    ORDER_NUMBER = (By.ID, "numero-orden")
    DETAILS = (By.ID, "detalle-orden")
    CONTINUE_BUTTON = (By.ID, "btn-seguir-comprando")

    # Fila del detalle de la orden (Fecha, Email, Método de pago, Total, Estado).
    def _detail(self, label):
        row = self.driver.find_element(
            By.XPATH, f"//*[@id='detalle-orden']/div[contains(., '{label}')]/span")
        return row.text

    # Indica si la pantalla de confirmación está visible con su contenido.
    def is_displayed(self):
        return self.is_visible(self.VIEW) and self.is_visible(self.TITLE)

    def get_title(self):
        return self.text_of(self.TITLE)

    def get_order_number(self):
        return self.text_of(self.ORDER_NUMBER)

    def get_paid_total(self):
        return parse_price(self._detail("Total pagado"))

    def get_status(self):
        return self._detail("Estado")

    def get_email(self):
        return self._detail("Email")

    # Vuelve al catálogo para seguir comprando.
    def continue_shopping(self):
        self.click(self.CONTINUE_BUTTON)
