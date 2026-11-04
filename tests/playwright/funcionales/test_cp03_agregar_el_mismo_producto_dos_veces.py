"""CP-03 · Agregar el mismo producto dos veces  [Playwright]"""

import pytest

from utils.test_data import MOUSE, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp03_agregar_el_mismo_producto_dos_veces(tienda):
    tienda.open_cart_with(MOUSE, MOUSE)
    assert tienda.cart.get_item_names() == [MOUSE], "Debe haber una sola fila"
    assert tienda.cart.get_quantity(MOUSE) == 2
    assert tienda.cart.get_item_subtotal(MOUSE) == dinero(2 * PRECIOS[MOUSE])
