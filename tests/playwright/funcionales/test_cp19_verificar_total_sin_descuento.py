"""CP-19 · Verificar total sin descuento  [Playwright]"""

import pytest

from utils.test_data import TECLADO, PRECIOS

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp19_verificar_total_sin_descuento(tienda):
    tienda.open_cart_with(TECLADO)              # precondición: carrito con un producto
    assert not tienda.cart.has_discount()
    assert tienda.cart.get_total() == dinero(PRECIOS[TECLADO])
