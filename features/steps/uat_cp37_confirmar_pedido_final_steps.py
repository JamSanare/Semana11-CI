"""Pasos UAT propios de CP-37 (aceptación de usuario)."""

from behave import then
from utils.test_data import MENSAJE_COMPRA_EXITOSA


# CP-37 · "el usuario confirma que el pedido se realizó"
@then('puedo confirmar que mi pedido se realizó con su número de orden')
def step_pedido_realizado(context):
    assert context.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    orden = context.confirmation.get_order_number()
    assert orden.startswith("ORD-") and len(orden) > 4, f"Número de orden inválido: '{orden}'"
    assert "Confirmado" in context.confirmation.get_status()
