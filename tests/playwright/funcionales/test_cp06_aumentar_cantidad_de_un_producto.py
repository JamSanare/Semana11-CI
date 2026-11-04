"""CP-06 · Aumentar cantidad de un producto  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp06_aumentar_cantidad_de_un_producto(tienda):
    tienda.open_cart_with(LAPTOP)
    tienda.cart.increase_quantity(LAPTOP)
    assert tienda.cart.get_quantity(LAPTOP) == 2
    assert tienda.cart.get_item_subtotal(LAPTOP) == dinero(2 * PRECIOS[LAPTOP])
    assert tienda.cart.get_total() == dinero(2 * PRECIOS[LAPTOP])
    assert tienda.catalog.get_cart_count() == 2
