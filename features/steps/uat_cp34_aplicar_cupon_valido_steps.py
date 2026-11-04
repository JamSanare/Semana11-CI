"""Pasos UAT propios de CP-34 (aceptación de usuario)."""

from behave import then


def iguales(a, b):
    return abs(a - b) < 0.005


# CP-34 · el descuento "se refleja visiblemente"
@then('veo el descuento del {porcentaje:d}% reflejado en el resumen del pedido')
def step_descuento_visible(context, porcentaje):
    assert context.cart.has_discount(), "El resumen no muestra la fila de descuento"
    assert f"{porcentaje}%" in context.cart.get_discount_row_text(), \
        f"La fila de descuento no indica {porcentaje}%: '{context.cart.get_discount_row_text()}'"
    esperado = context.cart.get_subtotal() * porcentaje / 100
    assert iguales(context.cart.get_discount(), esperado), "El importe del descuento es incorrecto"
    assert iguales(context.cart.get_total(), context.cart.get_subtotal() - esperado), \
        "El total no refleja el descuento"
