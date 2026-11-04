"""Pasos de Behave del checkout y la confirmación de compra.

Son pasos compartidos: los usan tanto los escenarios @funcional como los @uat.
"""

from behave import given, when, then, step

from utils.test_data import (CLIENTE_VALIDO, MENSAJE_COMPRA_EXITOSA, cliente_con)

# Cómo dejar "vacío" cada campo del formulario. El formulario de la app solo
# tiene "Nombre completo": para "apellido" se envía únicamente el nombre de pila.
CAMPO_VACIO = {
    "nombre": {"name": ""},
    "apellido": {"name": "María"},
    "correo": {"email": ""},
    "teléfono": {"phone": ""},
    "dirección": {"address": ""},
}

# Campo de la app donde debe aparecer el error de cada uno de los anteriores.
CAMPO_CON_ERROR = {
    "nombre": "nombre",
    "apellido": "nombre",
    "correo": "email",
    "teléfono": "telefono",
    "dirección": "direccion",
}


def iguales(a, b):
    return abs(a - b) < 0.005


# ── Preparación (Dado) ─────────────────────────────────────────────────────

@given('estoy en el checkout con "{producto}" en el carrito')
def step_en_checkout(context, producto):
    context.catalog.add_product(producto)
    context.catalog.open_cart()
    context.cart.proceed_to_checkout()


@given('he confirmado una compra de "{producto}"')
def step_compra_confirmada(context, producto):
    context.catalog.add_product(producto)
    context.catalog.open_cart()
    context.cart.proceed_to_checkout()
    context.checkout.fill_form(CLIENTE_VALIDO)
    context.checkout.confirm_payment()
    assert context.confirmation.is_displayed(), "La compra de preparación no se confirmó"


# ── Acciones (Cuando) ──────────────────────────────────────────────────────

@step('procedo al pago')
def step_procedo_al_pago(context):
    context.cart.proceed_to_checkout()


@when('confirmo el pago sin completar los datos')
def step_confirmo_sin_datos(context):
    context.checkout.confirm_payment()


@when('completo el formulario con datos válidos')
def step_formulario_valido(context):
    context.checkout.fill_form(CLIENTE_VALIDO)


@when('completo el formulario dejando vacío el campo "{campo}"')
def step_formulario_campo_vacio(context, campo):
    context.checkout.fill_form(cliente_con(**CAMPO_VACIO[campo]))


@when('completo el formulario con el correo "{correo}"')
def step_formulario_correo(context, correo):
    context.checkout.fill_form(cliente_con(email=correo))


@step('confirmo el pago')
def step_confirmo_pago(context):
    context.checkout.confirm_payment()


@when('vuelvo al catálogo desde la confirmación')
def step_volver_catalogo(context):
    context.confirmation.continue_shopping()


# ── Verificaciones (Entonces) ──────────────────────────────────────────────

@then('veo errores en todos los campos obligatorios')
def step_errores_todos(context):
    esperados = {"nombre", "email", "direccion", "ciudad", "telefono"}
    reales = set(context.checkout.get_fields_with_error())
    assert reales == esperados, f"Errores esperados {sorted(esperados)}, visibles {sorted(reales)}"


@then('veo el error del campo "{campo}"')
def step_error_campo(context, campo):
    esperado = CAMPO_CON_ERROR[campo]
    reales = context.checkout.get_fields_with_error()
    assert reales == [esperado], (
        f"Se esperaba un error solo en '{esperado}' (caso '{campo}'), "
        f"pero hay errores en {reales}"
        + (" y la compra se confirmó" if context.confirmation.is_displayed() else ""))


@then('no se muestra la confirmación de compra')
def step_sin_confirmacion(context):
    assert not context.confirmation.is_displayed(), "Se mostró la confirmación de compra"


@then('veo la pantalla de confirmación')
def step_veo_confirmacion(context):
    assert context.confirmation.is_displayed(), "No se muestra la pantalla de confirmación"
    assert context.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA, \
        f"Título inesperado: '{context.confirmation.get_title()}'"


@then('el total pagado es {monto:f}')
def step_total_pagado(context, monto):
    real = context.confirmation.get_paid_total()
    assert iguales(real, monto), f"Total pagado esperado {monto:.2f}, real {real:.2f}"


@then('el pedido tiene número de orden y estado "{estado}"')
def step_orden_y_estado(context, estado):
    assert context.confirmation.get_order_number().startswith("ORD-"), "Falta el número de orden"
    assert estado in context.confirmation.get_status(), \
        f"Estado esperado '{estado}', real '{context.confirmation.get_status()}'"


@then('veo el catálogo de productos')
def step_veo_catalogo(context):
    assert context.catalog.is_displayed(), "El catálogo no está visible"
    assert context.catalog.get_product_names(), "El catálogo no muestra productos"


@then('puedo seguir comprando agregando "{producto}"')
def step_seguir_comprando(context, producto):
    context.catalog.add_product(producto)
    assert context.catalog.get_cart_count() == 1, "No se pudo agregar un producto tras la compra"
