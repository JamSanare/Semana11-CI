"""CP-12 · Eliminar un producto cuando hay varios  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, MOUSE, TECLADO

pytestmark = pytest.mark.funcional


def test_cp12_eliminar_un_producto_cuando_hay_varios(tienda):
    tienda.open_cart_with(LAPTOP, MOUSE, TECLADO)
    tienda.cart.remove_item(MOUSE)
    assert not tienda.cart.has_item(MOUSE)
    assert sorted(tienda.cart.get_item_names()) == sorted([LAPTOP, TECLADO])
