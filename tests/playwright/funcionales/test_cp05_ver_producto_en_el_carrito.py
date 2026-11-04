"""CP-05 · Ver producto en el carrito  [Playwright]"""

import pytest

from utils.test_data import TECLADO, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp05_ver_producto_en_el_carrito(tienda):
    tienda.open_cart_with(TECLADO)
    assert tienda.cart.is_displayed(), "Debe mostrarse la vista del carrito"
    assert TECLADO in tienda.cart.get_item_names()
    assert tienda.cart.get_quantity(TECLADO) == 1
    assert tienda.cart.get_item_subtotal(TECLADO) == dinero(PRECIOS[TECLADO])
