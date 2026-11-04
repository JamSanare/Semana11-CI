"""CP-13 · Actualizar subtotal al eliminar producto  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, MOUSE, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp13_actualizar_subtotal_al_eliminar_producto(tienda):
    tienda.open_cart_with(LAPTOP, MOUSE)
    assert tienda.cart.get_subtotal() == dinero(PRECIOS[LAPTOP] + PRECIOS[MOUSE])
    tienda.cart.remove_item(MOUSE)
    assert tienda.cart.get_subtotal() == dinero(PRECIOS[LAPTOP])
    assert tienda.cart.get_total() == dinero(PRECIOS[LAPTOP])
