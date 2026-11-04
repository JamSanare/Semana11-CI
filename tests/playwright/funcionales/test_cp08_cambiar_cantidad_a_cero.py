"""CP-08 · Cambiar cantidad a cero → regla de la app: el producto se elimina  [Playwright]"""

import pytest

from utils.test_data import MOUSE

pytestmark = pytest.mark.funcional


def test_cp08_cambiar_cantidad_a_cero(tienda):
    tienda.open_cart_with(MOUSE)
    tienda.cart.decrease_quantity(MOUSE)          # 1 → 0
    assert not tienda.cart.has_item(MOUSE), "Con cantidad 0 el producto se elimina"
    assert tienda.cart.has_empty_message()
    assert tienda.catalog.get_cart_count() == 0
