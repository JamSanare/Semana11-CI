"""CP-10 · Eliminar un producto del carrito"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP


class TestCP10(TiendaDemoTestCase):
    # CP-10 · Eliminar un producto del carrito
    def test_cp10_eliminar_un_producto_del_carrito(self):
        self.open_cart_with(LAPTOP)
        self.cart.remove_item(LAPTOP)
        self.assertIsNone(self.cart.get_item_row(LAPTOP))


if __name__ == '__main__':
    unittest.main()
