"""CP-18 · Verificar total con descuento  [Playwright]"""

import pytest

from utils.test_data import TECLADO, PRECIOS, CUPON_VALIDO, DESCUENTO_VALIDO

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp18_verificar_total_con_descuento(tienda):
    precio = PRECIOS[TECLADO]
    tienda.open_cart_with(TECLADO)              # precondición: carrito con un producto
    tienda.cart.apply_coupon(CUPON_VALIDO)
    assert tienda.cart.get_subtotal() == dinero(precio)
    assert tienda.cart.get_discount() == dinero(precio * DESCUENTO_VALIDO)
    assert tienda.cart.get_total() == dinero(precio * (1 - DESCUENTO_VALIDO))
