"""CP-08 · Cambiar cantidad a cero → regla de la app: el producto se elimina"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import MOUSE


class TestCP08(TiendaDemoTestCase):
    # CP-08 · Cambiar cantidad a cero → regla de la app: el producto se elimina
    def test_cp08_cambiar_cantidad_a_cero(self):
        self.open_cart_with(MOUSE)
        self.cart.decrease_quantity(MOUSE)          # 1 → 0
        self.assertIsNone(self.cart.get_item_row(MOUSE), "Con cantidad 0 el producto se elimina")
        self.assertTrue(self.cart.has_empty_message())
        self.assertEqual(self.catalog.get_cart_count(), 0)


if __name__ == '__main__':
    unittest.main()
