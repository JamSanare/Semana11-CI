"""CP-33 · Ver el carrito con el producto agregado  [Playwright]"""

import pytest

from utils.test_data import TECLADO

pytestmark = pytest.mark.uat


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp33_ver_el_carrito_con_el_producto_agregado(tienda):
    # Dado tengo "Teclado Mecánico" en el carrito
    tienda.catalog.add_product(TECLADO)
    # Cuando abro el carrito
    tienda.catalog.open_cart()
    # Entonces veo "Teclado Mecánico" en el carrito
    assert TECLADO in tienda.cart.get_item_names()
    # Y la cantidad de "Teclado Mecánico" es 1
    assert tienda.cart.get_quantity(TECLADO) == 1
    # Y el total del carrito es 249.00
    assert tienda.cart.get_total() == dinero(249.00)
