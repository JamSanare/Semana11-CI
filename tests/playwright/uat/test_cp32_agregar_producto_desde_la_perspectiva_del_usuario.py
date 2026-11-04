"""CP-32 · Agregar producto desde la perspectiva del usuario  [Playwright]"""

import pytest

from utils.test_data import LAPTOP

pytestmark = pytest.mark.uat


def test_cp32_agregar_producto_desde_la_perspectiva_del_usuario(tienda):
    # Cuando navego por el catálogo
    assert tienda.catalog.is_displayed(), "El catálogo no está visible"
    assert tienda.catalog.get_product_names(), "El catálogo no muestra productos"
    # Y agrego "Laptop Pro 15" al carrito
    tienda.catalog.add_product(LAPTOP)
    # Entonces veo una notificación de que el producto se agregó
    assert tienda.catalog.toast_is_visible(), "No apareció ninguna notificación"
    assert "agregado al carrito" in tienda.catalog.get_toast_text(), \
        f"Notificación inesperada: '{tienda.catalog.get_toast_text()}'"
    # Y el contador del carrito muestra 1
    assert tienda.catalog.get_cart_count() == 1
