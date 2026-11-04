"""CP-36 · Intentar compra con datos incompletos  [Playwright]"""

import pytest

from utils.test_data import DISCO

pytestmark = pytest.mark.uat


def test_cp36_intentar_compra_con_datos_incompletos(tienda):
    # Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    tienda.open_checkout_with(DISCO)
    # Cuando confirmo el pago sin completar los datos
    tienda.checkout.confirm_payment()
    # Entonces el sistema me guía con mensajes de error claros
    assert tienda.checkout.is_displayed(), "El usuario fue sacado del checkout"
    mensajes = tienda.checkout.get_error_messages()
    assert len(mensajes) == 5, f"Se esperaba un mensaje por cada campo (5); hay {len(mensajes)}"
    for mensaje in mensajes:
        assert len(mensaje) >= 8, f"Mensaje de error demasiado vago: '{mensaje}'"
        assert "obligatori" in mensaje or "válido" in mensaje, \
            f"El mensaje no dice qué corregir: '{mensaje}'"
    # Y no se muestra la confirmación de compra
    assert not tienda.confirmation.is_displayed(), "Se mostró la confirmación de compra"
