"""ConfirmationPage (Playwright): pantalla posterior a confirmar la compra."""

from utils.test_data import parse_price
from .base_page import BasePage


class ConfirmationPage(BasePage):
    VIEW = "#vista-confirmacion"
    TITLE = "#msg-confirmacion"
    ORDER_NUMBER = "#numero-orden"
    DETAILS = "#detalle-orden"
    CONTINUE_BUTTON = "#btn-seguir-comprando"

    # Valor de una fila del detalle (Fecha, Email, Método de pago, Total pagado, Estado).
    def _detail(self, label):
        fila = self.page.locator(f"{self.DETAILS} > div", has_text=label)
        return fila.locator("span").inner_text()

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

    def continue_shopping(self):
        self.page.locator(self.CONTINUE_BUTTON).click()
