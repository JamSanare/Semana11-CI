"""CP-40 · Validar total final correcto  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, MOUSE, CUPON_VALIDO, DESCUENTO_VALIDO

pytestmark = pytest.mark.uat


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp40_validar_total_final_correcto(tienda):
    # Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico"
    # Y abro el carrito
    tienda.open_cart_with(LAPTOP, MOUSE)
    # Cuando aplico el cupón "DESCUENTO10"
    tienda.cart.apply_coupon(CUPON_VALIDO)
    # Entonces el total coincide con la suma de los productos menos el descuento
    suma_productos = tienda.cart.sum_item_subtotals()
    descuento = tienda.cart.get_discount()
    assert tienda.cart.get_subtotal() == dinero(suma_productos), \
        "El subtotal no coincide con la suma de las filas del carrito"
    assert descuento == dinero(suma_productos * DESCUENTO_VALIDO), "El descuento mostrado es incorrecto"
    assert tienda.cart.get_total() == dinero(suma_productos - descuento)
    # Y el total del carrito es 2330.01
    assert tienda.cart.get_total() == dinero(2330.01)
