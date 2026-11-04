"""CP-37 · Confirmar pedido final  [Playwright]"""

import pytest

from utils.test_data import DISCO, CLIENTE_VALIDO, MENSAJE_COMPRA_EXITOSA

pytestmark = pytest.mark.uat


def test_cp37_confirmar_pedido_final(tienda):
    # Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    tienda.open_checkout_with(DISCO)
    # Cuando completo el formulario con datos válidos, Y confirmo el pago
    tienda.checkout.fill_form(CLIENTE_VALIDO)
    tienda.checkout.confirm_payment()
    # Entonces puedo confirmar que mi pedido se realizó con su número de orden
    assert tienda.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    orden = tienda.confirmation.get_order_number()
    assert orden.startswith("ORD-") and len(orden) > 4, f"Número de orden inválido: '{orden}'"
    assert "Confirmado" in tienda.confirmation.get_status()
