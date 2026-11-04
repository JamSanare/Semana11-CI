"""Pasos UAT propios de CP-32 (aceptación de usuario)."""

from behave import then


# CP-32 · el usuario agrega un producto "sin dificultad"
@then('veo una notificación de que el producto se agregó')
def step_notificacion_agregado(context):
    assert context.catalog.toast_is_visible(), "No apareció ninguna notificación"
    assert "agregado al carrito" in context.catalog.get_toast_text(), \
        f"Notificación inesperada: '{context.catalog.get_toast_text()}'"
