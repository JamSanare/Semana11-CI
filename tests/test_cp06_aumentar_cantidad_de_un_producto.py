"""CP-06 · Aumentar cantidad de un producto"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP, PRECIOS


class TestCP06(TiendaDemoTestCase):
    # CP-06 · Aumentar cantidad de un producto
    def test_cp06_aumentar_cantidad_de_un_producto(self):
        self.open_cart_with(LAPTOP)
        self.cart.increase_quantity(LAPTOP)
        self.assertEqual(self.cart.get_quantity(LAPTOP), 2)
        self.assertAlmostEqual(self.cart.get_item_subtotal(LAPTOP), 2 * PRECIOS[LAPTOP], places=2)
        self.assertAlmostEqual(self.cart.get_total(), 2 * PRECIOS[LAPTOP], places=2)
        self.assertEqual(self.catalog.get_cart_count(), 2)


if __name__ == '__main__':
    unittest.main()
