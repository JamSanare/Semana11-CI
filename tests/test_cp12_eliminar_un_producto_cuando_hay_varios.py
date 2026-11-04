"""CP-12 · Eliminar un producto cuando hay varios"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP, MOUSE, TECLADO


class TestCP12(TiendaDemoTestCase):
    # CP-12 · Eliminar un producto cuando hay varios
    def test_cp12_eliminar_un_producto_cuando_hay_varios(self):
        self.open_cart_with(LAPTOP, MOUSE, TECLADO)
        self.cart.remove_item(MOUSE)
        self.assertIsNone(self.cart.get_item_row(MOUSE))
        self.assertCountEqual(self.cart.get_item_names(), [LAPTOP, TECLADO])


if __name__ == '__main__':
    unittest.main()
