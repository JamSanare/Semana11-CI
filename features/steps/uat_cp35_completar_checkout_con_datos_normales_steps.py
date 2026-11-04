"""Pasos UAT propios de CP-35, CP-38, CP-41 (aceptación de usuario)."""

from behave import then
from utils.test_data import MENSAJE_COMPRA_EXITOSA


# CP-35 · CP-38 · CP-41 · "el flujo finaliza con éxito"
@then('el flujo de compra finaliza con éxito')
def step_flujo_exitoso(context):
    assert context.confirmation.is_displayed(), "El flujo no llegó a la confirmación"
    assert context.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    assert "Confirmado" in context.confirmation.get_status()
