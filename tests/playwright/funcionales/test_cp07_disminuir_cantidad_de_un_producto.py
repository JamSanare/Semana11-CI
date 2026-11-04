"""CP-07 · Disminuir cantidad de un producto (precondición: cantidad > 1)  [Playwright]"""

import pytest

from utils.test_data import MOUSE, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp07_disminuir_cantidad_de_un_producto(tienda):
    tienda.open_cart_with(MOUSE, MOUSE)
    assert tienda.cart.get_quantity(MOUSE) == 2
    tienda.cart.decrease_quantity(MOUSE)
    assert tienda.cart.get_quantity(MOUSE) == 1
    assert tienda.cart.get_total() == dinero(PRECIOS[MOUSE])
    assert tienda.catalog.get_cart_count() == 1
