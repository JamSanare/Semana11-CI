"""CP-39 · Intentar compra con carrito vacío  [Playwright]"""

import pytest

pytestmark = pytest.mark.uat


def test_cp39_intentar_compra_con_carrito_vacio(tienda):
    # Cuando abro el carrito
    tienda.catalog.open_cart()
    # Entonces la compra se bloquea y veo el aviso de carrito vacío
    assert tienda.cart.has_empty_message(), "No se muestra el aviso de carrito vacío"
    assert not tienda.cart.has_checkout_button(), "Se permite continuar al pago con el carrito vacío"
    assert not tienda.checkout.is_displayed(), "Se abrió el checkout con el carrito vacío"
