"""CP-35 · Completar checkout con datos normales  [Playwright]"""

import pytest

from utils.test_data import DISCO, CLIENTE_VALIDO, MENSAJE_COMPRA_EXITOSA

pytestmark = pytest.mark.uat


def test_cp35_completar_checkout_con_datos_normales(tienda):
    # Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    tienda.open_checkout_with(DISCO)
    # Cuando completo el formulario con datos válidos, Y confirmo el pago
    tienda.checkout.fill_form(CLIENTE_VALIDO)
    tienda.checkout.confirm_payment()
    # Entonces el flujo de compra finaliza con éxito
    assert tienda.confirmation.is_displayed(), "El flujo no llegó a la confirmación"
    assert tienda.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    assert "Confirmado" in tienda.confirmation.get_status()
