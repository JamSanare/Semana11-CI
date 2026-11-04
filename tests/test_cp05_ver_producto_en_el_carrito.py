"""CP-05 · Ver producto en el carrito"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, PRECIOS


class TestCP05(TiendaDemoTestCase):
    # CP-05 · Ver producto en el carrito
    def test_cp05_ver_producto_en_el_carrito(self):
        self.open_cart_with(TECLADO)
        self.assertTrue(self.cart.is_displayed(), "Debe mostrarse la vista del carrito")
        self.assertIn(TECLADO, self.cart.get_item_names())
        self.assertEqual(self.cart.get_quantity(TECLADO), 1)
        self.assertAlmostEqual(self.cart.get_item_subtotal(TECLADO), PRECIOS[TECLADO], places=2)


if __name__ == '__main__':
    unittest.main()
