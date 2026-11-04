"""CP-14 · Aplicar cupón válido  [Playwright]"""

import pytest

from utils.test_data import TECLADO, CUPON_VALIDO

pytestmark = pytest.mark.funcional


def test_cp14_aplicar_cupon_valido(tienda):
    tienda.open_cart_with(TECLADO)              # precondición: carrito con un producto
    tienda.cart.apply_coupon(CUPON_VALIDO)
    mensaje = tienda.cart.get_coupon_message()
    assert CUPON_VALIDO in mensaje
    assert "aplicado" in mensaje
