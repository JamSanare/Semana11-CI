"""Pasos UAT propios de CP-36 (aceptación de usuario)."""

from behave import then


# CP-36 · "el sistema guía al usuario con errores claros"
@then('el sistema me guía con mensajes de error claros')
def step_errores_claros(context):
    assert context.checkout.is_displayed(), "El usuario fue sacado del checkout"
    mensajes = context.checkout.get_error_messages()
    assert len(mensajes) == 5, f"Se esperaba un mensaje por cada campo (5); hay {len(mensajes)}"
    for mensaje in mensajes:
        assert len(mensaje) >= 8, f"Mensaje de error demasiado vago: '{mensaje}'"
        assert "obligatori" in mensaje or "válido" in mensaje, \
            f"El mensaje no dice qué corregir: '{mensaje}'"
