"""CP-02 · Agregar varios productos diferentes  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, MOUSE

pytestmark = pytest.mark.funcional


def test_cp02_agregar_varios_productos_diferentes(tienda):
    tienda.open_cart_with(LAPTOP, MOUSE)
    assert sorted(tienda.cart.get_item_names()) == sorted([LAPTOP, MOUSE])
    assert tienda.catalog.get_cart_count() == 2
