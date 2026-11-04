"""CP-15 · Aplicar cupón inválido  [Playwright]"""

import pytest

from utils.test_data import TECLADO, PRECIOS, CUPON_INVALIDO

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp15_aplicar_cupon_invalido(tienda):
    tienda.open_cart_with(TECLADO)              # precondición: carrito con un producto
    tienda.cart.apply_coupon(CUPON_INVALIDO)
    assert "Cupón no válido" in tienda.cart.get_coupon_message()
    assert not tienda.cart.has_discount(), "No debe aplicarse descuento"
    assert tienda.cart.get_total() == dinero(PRECIOS[TECLADO])
