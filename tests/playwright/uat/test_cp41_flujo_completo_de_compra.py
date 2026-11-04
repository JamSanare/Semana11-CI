"""CP-41 · Flujo completo de compra  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, CUPON_VALIDO, CLIENTE_VALIDO, MENSAJE_COMPRA_EXITOSA

pytestmark = pytest.mark.uat


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp41_flujo_completo_de_compra(tienda):
    # Cuando agrego "Laptop Pro 15" al carrito
    tienda.catalog.add_product(LAPTOP)
    # Y abro el carrito
    tienda.catalog.open_cart()
    # Y aplico el cupón "DESCUENTO10"
    tienda.cart.apply_coupon(CUPON_VALIDO)
    # Y procedo al pago
    tienda.cart.proceed_to_checkout()
    # Y completo el formulario con datos válidos
    tienda.checkout.fill_form(CLIENTE_VALIDO)
    # Y confirmo el pago
    tienda.checkout.confirm_payment()
    # Entonces el flujo de compra finaliza con éxito
    assert tienda.confirmation.is_displayed(), "El flujo no llegó a la confirmación"
    assert tienda.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    assert "Confirmado" in tienda.confirmation.get_status()
    # Y el total pagado es 2249.10
    assert tienda.confirmation.get_paid_total() == dinero(2249.10)
    # Y el contador del carrito muestra 0
    assert tienda.catalog.get_cart_count() == 0
