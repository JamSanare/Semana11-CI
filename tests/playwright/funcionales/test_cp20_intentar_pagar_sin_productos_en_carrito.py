"""CP-20 · Intentar pagar sin productos en carrito  [Playwright]"""

import pytest

pytestmark = pytest.mark.funcional


def test_cp20_intentar_pagar_sin_productos_en_carrito(tienda):
    tienda.catalog.open_cart()
    assert tienda.cart.has_empty_message()
    assert not tienda.cart.has_checkout_button(), "No debe ofrecerse 'Proceder al pago'"
    assert not tienda.checkout.is_displayed(), "No debe abrirse el checkout"
