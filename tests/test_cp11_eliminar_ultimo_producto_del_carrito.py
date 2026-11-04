"""CP-11 · Eliminar último producto del carrito"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP


class TestCP11(TiendaDemoTestCase):
    # CP-11 · Eliminar último producto del carrito
    def test_cp11_eliminar_ultimo_producto_del_carrito(self):
        self.open_cart_with(LAPTOP)
        self.cart.remove_item(LAPTOP)
        self.assertTrue(self.cart.has_empty_message(), "El carrito debe quedar vacío")
        self.assertEqual(self.catalog.get_cart_count(), 0)


if __name__ == '__main__':
    unittest.main()
