"""CP-04 · Verificar contador del carrito  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, TECLADO

pytestmark = pytest.mark.funcional


def test_cp04_verificar_contador_del_carrito(tienda):
    assert tienda.catalog.get_cart_count() == 0, "El carrito inicia en 0"
    tienda.catalog.add_product(TECLADO)
    assert tienda.catalog.get_cart_count() == 1
    tienda.catalog.add_product(LAPTOP)
    assert tienda.catalog.get_cart_count() == 2
