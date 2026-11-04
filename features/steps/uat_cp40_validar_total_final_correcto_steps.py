"""Pasos UAT propios de CP-40 (aceptación de usuario)."""

from behave import then
from utils.test_data import DESCUENTO_VALIDO


def iguales(a, b):
    return abs(a - b) < 0.005


# CP-40 · "el total coincide con productos y descuentos"
@then('el total coincide con la suma de los productos menos el descuento')
def step_total_coincide(context):
    suma_productos = context.cart.sum_item_subtotals()
    descuento = context.cart.get_discount()
    assert iguales(context.cart.get_subtotal(), suma_productos), \
        "El subtotal no coincide con la suma de las filas del carrito"
    assert iguales(descuento, suma_productos * DESCUENTO_VALIDO), "El descuento mostrado es incorrecto"
    assert iguales(context.cart.get_total(), suma_productos - descuento), \
        f"Total {context.cart.get_total():.2f} ≠ {suma_productos:.2f} − {descuento:.2f}"
