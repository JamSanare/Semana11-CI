"""CP-01 · Agregar producto al carrito  [Playwright]"""

import pytest

from utils.test_data import LAPTOP

pytestmark = pytest.mark.funcional


def test_cp01_agregar_producto_al_carrito(tienda):
    tienda.catalog.add_product(LAPTOP)
    assert tienda.catalog.get_cart_count() == 1, "El contador debe aumentar a 1"
    tienda.catalog.open_cart()
    assert LAPTOP in tienda.cart.get_item_names()
