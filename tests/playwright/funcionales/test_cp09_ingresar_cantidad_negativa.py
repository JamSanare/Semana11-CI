"""CP-09 · Ingresar cantidad negativa  [Playwright]"""

import pytest

from utils.test_data import MOUSE

pytestmark = pytest.mark.funcional


def test_cp09_ingresar_cantidad_negativa(tienda):
    # La interfaz no tiene campo para escribir cantidades (solo botones − y +),
    # así que un valor negativo no se puede ingresar; el intento más cercano es
    # seguir pulsando "−" por debajo de cero.
    tienda.open_cart_with(MOUSE)
    assert not tienda.cart.has_quantity_input(), "No debe existir un campo editable que admita -1"
    tienda.cart.decrease_quantity(MOUSE)          # 1 → 0 (elimina)
    tienda.cart.decrease_quantity(MOUSE)          # intento bajo cero: no hay fila
    assert tienda.catalog.get_cart_count() == 0, "El contador nunca es negativo"
    assert tienda.cart.get_quantity(MOUSE) == 0
