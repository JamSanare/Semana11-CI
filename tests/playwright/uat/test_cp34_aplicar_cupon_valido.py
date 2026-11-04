"""CP-34 · Aplicar cupón válido  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, CUPON_VALIDO

pytestmark = pytest.mark.uat


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp34_aplicar_cupon_valido(tienda):
    # Dado tengo "Laptop Pro 15" en el carrito, Y abro el carrito
    tienda.open_cart_with(LAPTOP)
    # Cuando aplico el cupón "DESCUENTO10"
    tienda.cart.apply_coupon(CUPON_VALIDO)
    # Entonces veo el descuento del 10% reflejado en el resumen del pedido
    porcentaje = 10
    assert tienda.cart.has_discount(), "El resumen no muestra la fila de descuento"
    assert f"{porcentaje}%" in tienda.cart.get_discount_row_text(), \
        f"La fila de descuento no indica {porcentaje}%: '{tienda.cart.get_discount_row_text()}'"
    esperado = tienda.cart.get_subtotal() * porcentaje / 100
    assert tienda.cart.get_discount() == dinero(esperado), "El importe del descuento es incorrecto"
    assert tienda.cart.get_total() == dinero(tienda.cart.get_subtotal() - esperado), \
        "El total no refleja el descuento"
