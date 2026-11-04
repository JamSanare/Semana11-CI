"""CP-09 · Ingresar cantidad negativa"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import MOUSE


class TestCP09(TiendaDemoTestCase):
    # CP-09 · Ingresar cantidad negativa
    # La interfaz no tiene campo para escribir cantidades (solo botones − y +),
    # así que un valor negativo no se puede ingresar; el intento más cercano es
    # seguir pulsando "−" por debajo de cero.
    def test_cp09_ingresar_cantidad_negativa(self):
        self.open_cart_with(MOUSE)
        self.assertFalse(self.cart.has_quantity_input(),
                         "No debe existir un campo editable que admita -1")
        self.cart.decrease_quantity(MOUSE)          # 1 → 0 (elimina)
        self.cart.decrease_quantity(MOUSE)          # intento bajo cero: no hay fila
        self.assertEqual(self.catalog.get_cart_count(), 0, "El contador nunca es negativo")
        self.assertEqual(self.cart.get_quantity(MOUSE), 0)


if __name__ == '__main__':
    unittest.main()
