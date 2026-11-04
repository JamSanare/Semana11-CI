"""CP-16 · Aplicar cupón vacío  [Playwright]"""

import pytest

from utils.test_data import TECLADO, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp16_aplicar_cupon_vacio(tienda):
    tienda.open_cart_with(TECLADO)              # precondición: carrito con un producto
    tienda.cart.apply_coupon("")
    assert "Ingresa un código" in tienda.cart.get_coupon_message()
    assert not tienda.cart.has_discount()
    assert tienda.cart.get_total() == dinero(PRECIOS[TECLADO])
