"""Pasos UAT propios de CP-39 (aceptación de usuario)."""

from behave import then


# CP-39 · "se bloquea la compra y se muestra la validación"
@then('la compra se bloquea y veo el aviso de carrito vacío')
def step_compra_bloqueada(context):
    assert context.cart.has_empty_message(), "No se muestra el aviso de carrito vacío"
    assert not context.cart.has_checkout_button(), "Se permite continuar al pago con el carrito vacío"
    assert not context.checkout.is_displayed(), "Se abrió el checkout con el carrito vacío"
