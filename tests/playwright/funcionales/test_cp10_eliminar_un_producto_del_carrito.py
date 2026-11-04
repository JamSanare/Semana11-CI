"""CP-10 · Eliminar un producto del carrito  [Playwright]"""

import pytest

from utils.test_data import LAPTOP

pytestmark = pytest.mark.funcional


def test_cp10_eliminar_un_producto_del_carrito(tienda):
    tienda.open_cart_with(LAPTOP)
    tienda.cart.remove_item(LAPTOP)
    assert not tienda.cart.has_item(LAPTOP)
