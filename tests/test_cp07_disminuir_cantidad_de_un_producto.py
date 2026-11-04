"""CP-07 · Disminuir cantidad de un producto (precondición: cantidad > 1)"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import MOUSE, PRECIOS


class TestCP07(TiendaDemoTestCase):
    # CP-07 · Disminuir cantidad de un producto (precondición: cantidad > 1)
    def test_cp07_disminuir_cantidad_de_un_producto(self):
        self.open_cart_with(MOUSE, MOUSE)
        self.assertEqual(self.cart.get_quantity(MOUSE), 2)
        self.cart.decrease_quantity(MOUSE)
        self.assertEqual(self.cart.get_quantity(MOUSE), 1)
        self.assertAlmostEqual(self.cart.get_total(), PRECIOS[MOUSE], places=2)
        self.assertEqual(self.catalog.get_cart_count(), 1)


if __name__ == '__main__':
    unittest.main()
