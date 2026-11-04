"""Pasos de Behave del catálogo y del carrito (agregar, cantidades, eliminar, cupones).

Son pasos compartidos: los usan tanto los escenarios @funcional como los @uat.
"""

import re

from behave import given, when, then, step

from utils.config import BASE_URL
from utils.test_data import DESCUENTO_VALIDO


def iguales(a, b):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return abs(a - b) < 0.005


# ── Preparación (Dado) ─────────────────────────────────────────────────────

@given('estoy en el catálogo de TiendaDemo')
def step_catalogo(context):
    context.catalog.open(BASE_URL)


@given('tengo "{producto}" en el carrito')
def step_tengo_producto(context, producto):
    context.catalog.add_product(producto)


@given('tengo {cantidad:d} unidades de "{producto}" en el carrito')
def step_tengo_unidades(context, cantidad, producto):
    for _ in range(cantidad):
        context.catalog.add_product(producto)


@given('tengo en el carrito los productos {lista}')
def step_tengo_productos(context, lista):
    for producto in re.findall(r'"([^"]+)"', lista):
        context.catalog.add_product(producto)


@given('tengo aplicado el cupón "{cupon}"')
def step_cupon_ya_aplicado(context, cupon):
    context.cart.apply_coupon(cupon)


# ── Acciones (Cuando) ──────────────────────────────────────────────────────

@when('navego por el catálogo')
def step_navego_catalogo(context):
    assert context.catalog.is_displayed(), "El catálogo no está visible"
    assert context.catalog.get_product_names(), "El catálogo no muestra productos"


@when('agrego "{producto}" al carrito')
def step_agrego(context, producto):
    context.catalog.add_product(producto)


@step('abro el carrito')
def step_abro_carrito(context):
    context.catalog.open_cart()


@when('aumento la cantidad de "{producto}"')
def step_aumento(context, producto):
    context.cart.increase_quantity(producto)


@when('disminuyo la cantidad de "{producto}"')
def step_disminuyo(context, producto):
    context.cart.decrease_quantity(producto)


@when('reduzco la cantidad de "{producto}" hasta cero')
def step_reduzco_a_cero(context, producto):
    while context.cart.get_item_row(producto):
        context.cart.decrease_quantity(producto)


@when('intento bajar la cantidad de "{producto}" por debajo de cero')
def step_bajo_de_cero(context, producto):
    # La interfaz solo ofrece los botones − y +; se sigue pulsando "−" más allá de 0.
    cantidad = context.cart.get_quantity(producto)
    for _ in range(cantidad + 2):
        context.cart.decrease_quantity(producto)


@when('elimino "{producto}" del carrito')
def step_elimino(context, producto):
    context.cart.remove_item(producto)


@when('aplico el cupón "{cupon}"')
def step_aplico_cupon(context, cupon):
    context.cart.apply_coupon(cupon)


@when('intento aplicar un cupón vacío')
def step_cupon_vacio(context):
    context.cart.apply_coupon("")


# ── Verificaciones (Entonces) ──────────────────────────────────────────────

@then('veo "{producto}" en el carrito')
def step_veo_producto(context, producto):
    assert producto in context.cart.get_item_names(), \
        f"'{producto}' no está en el carrito; hay: {context.cart.get_item_names()}"


@then('no veo "{producto}" en el carrito')
def step_no_veo_producto(context, producto):
    assert producto not in context.cart.get_item_names(), f"'{producto}' sigue en el carrito"


@then('el contador del carrito muestra {n:d}')
def step_contador(context, n):
    real = context.catalog.get_cart_count()
    assert real == n, f"Contador esperado {n}, real {real}"


@then('la cantidad de "{producto}" es {n:d}')
def step_cantidad(context, producto, n):
    real = context.cart.get_quantity(producto)
    assert real == n, f"Cantidad esperada {n} de '{producto}', real {real}"


@then('el subtotal del carrito es {monto:f}')
def step_subtotal(context, monto):
    real = context.cart.get_subtotal()
    assert iguales(real, monto), f"Subtotal esperado {monto:.2f}, real {real:.2f}"


@then('el total del carrito es {monto:f}')
def step_total(context, monto):
    real = context.cart.get_total()
    assert iguales(real, monto), f"Total esperado {monto:.2f}, real {real:.2f}"


@then('el carrito queda vacío')
def step_carrito_vacio(context):
    assert context.cart.has_empty_message(), "No se muestra el mensaje de carrito vacío"
    assert context.catalog.get_cart_count() == 0, "El contador no volvió a 0"


@then('no existe un campo para escribir la cantidad manualmente')
def step_sin_campo_cantidad(context):
    assert not context.cart.has_quantity_input(), "Existe un campo editable de cantidad"


@then('el mensaje del cupón contiene "{texto}"')
def step_mensaje_cupon(context, texto):
    mensaje = context.cart.get_coupon_message()
    assert texto in mensaje, f"Se esperaba '{texto}' en el mensaje del cupón; real: '{mensaje}'"


@then('no se muestra ningún descuento')
def step_sin_descuento(context):
    assert not context.cart.has_discount(), "Se muestra una fila de descuento"


@then('el descuento mostrado es {monto:f}')
def step_descuento(context, monto):
    real = context.cart.get_discount()
    assert iguales(real, monto), f"Descuento esperado {monto:.2f}, real {real:.2f}"


@then('el descuento no se acumula y el total del carrito es {monto:f}')
def step_descuento_no_acumula(context, monto):
    subtotal = context.cart.get_subtotal()
    assert iguales(context.cart.get_discount(), subtotal * DESCUENTO_VALIDO), \
        "El descuento debe seguir siendo un único 10 %"
    assert iguales(context.cart.get_total(), monto), \
        f"Total esperado {monto:.2f}, real {context.cart.get_total():.2f}"


@then('veo el aviso de carrito vacío')
def step_aviso_vacio(context):
    assert context.cart.has_empty_message(), "No se muestra 'Tu carrito está vacío'"


@then('no existe la opción de proceder al pago')
def step_sin_pago(context):
    assert not context.cart.has_checkout_button(), "Se ofrece 'Proceder al pago' con carrito vacío"
    assert not context.checkout.is_displayed(), "Se abrió el checkout con carrito vacío"
