"""CP-11 · Eliminar último producto del carrito  [Playwright]"""

import pytest

from utils.test_data import LAPTOP

pytestmark = pytest.mark.funcional


def test_cp11_eliminar_ultimo_producto_del_carrito(tienda):
    tienda.open_cart_with(LAPTOP)
    tienda.cart.remove_item(LAPTOP)
    assert tienda.cart.has_empty_message(), "El carrito debe quedar vacío"
    assert tienda.catalog.get_cart_count() == 0
