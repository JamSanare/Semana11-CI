"""CP-31 · Volver al catálogo desde confirmación  [Playwright]"""

import pytest

from utils.test_data import MOUSE, DISCO

pytestmark = pytest.mark.funcional


def test_cp31_volver_al_catalogo_desde_confirmacion(tienda):
    tienda.buy(DISCO)
    tienda.confirmation.continue_shopping()
    assert tienda.catalog.is_displayed()
    assert tienda.catalog.get_cart_count() == 0, "El carrito se vacía tras la compra"
    tienda.catalog.add_product(MOUSE)             # el usuario puede seguir comprando
    assert tienda.catalog.get_cart_count() == 1
