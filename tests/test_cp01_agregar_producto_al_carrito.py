"""CP-01 · Agregar producto al carrito"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP


class TestCP01(TiendaDemoTestCase):
    # CP-01 · Agregar producto al carrito
    def test_cp01_agregar_producto_al_carrito(self):
        self.catalog.add_product(LAPTOP)
        self.assertEqual(self.catalog.get_cart_count(), 1, "El contador debe aumentar a 1")
        self.catalog.open_cart()
        self.assertIn(LAPTOP, self.cart.get_item_names())


if __name__ == '__main__':
    unittest.main()
