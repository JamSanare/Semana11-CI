"""CP-13 · Actualizar subtotal al eliminar producto"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP, MOUSE, PRECIOS


class TestCP13(TiendaDemoTestCase):
    # CP-13 · Actualizar subtotal al eliminar producto
    def test_cp13_actualizar_subtotal_al_eliminar_producto(self):
        self.open_cart_with(LAPTOP, MOUSE)
        self.assertAlmostEqual(self.cart.get_subtotal(), PRECIOS[LAPTOP] + PRECIOS[MOUSE], places=2)
        self.cart.remove_item(MOUSE)
        self.assertAlmostEqual(self.cart.get_subtotal(), PRECIOS[LAPTOP], places=2)
        self.assertAlmostEqual(self.cart.get_total(), PRECIOS[LAPTOP], places=2)


if __name__ == '__main__':
    unittest.main()
