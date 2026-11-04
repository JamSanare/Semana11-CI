"""CP-17 · Aplicar cupón repetido: el descuento no debe acumularse  [Playwright]"""

import pytest

from utils.test_data import TECLADO, PRECIOS, CUPON_VALIDO, DESCUENTO_VALIDO

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp17_aplicar_cupon_repetido(tienda):
    # La app vuelve a mostrar "cupón aplicado" sin un aviso específico;
    # se verifica que el descuento no se acumula.
    precio = PRECIOS[TECLADO]
    tienda.open_cart_with(TECLADO)              # precondición: carrito con un producto
    tienda.cart.apply_coupon(CUPON_VALIDO)
    total_primera_vez = tienda.cart.get_total()
    tienda.cart.apply_coupon(CUPON_VALIDO)
    assert total_primera_vez == dinero(precio * (1 - DESCUENTO_VALIDO))
    assert tienda.cart.get_total() == dinero(total_primera_vez), \
        "El segundo intento no debe aplicar otro descuento"
    assert tienda.cart.get_discount() == dinero(precio * DESCUENTO_VALIDO)
