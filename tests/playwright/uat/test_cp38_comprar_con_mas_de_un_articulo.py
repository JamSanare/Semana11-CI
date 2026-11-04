"""CP-38 · Comprar con más de un artículo  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, MOUSE, CLIENTE_VALIDO, MENSAJE_COMPRA_EXITOSA

pytestmark = pytest.mark.uat


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp38_comprar_con_mas_de_un_articulo(tienda):
    # Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico"
    # Y abro el carrito, Y procedo al pago
    tienda.open_checkout_with(LAPTOP, MOUSE)
    # Cuando completo el formulario con datos válidos, Y confirmo el pago
    tienda.checkout.fill_form(CLIENTE_VALIDO)
    tienda.checkout.confirm_payment()
    # Entonces el flujo de compra finaliza con éxito
    assert tienda.confirmation.is_displayed(), "El flujo no llegó a la confirmación"
    assert tienda.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    assert "Confirmado" in tienda.confirmation.get_status()
    # Y el total pagado es 2588.90
    assert tienda.confirmation.get_paid_total() == dinero(2588.90)
