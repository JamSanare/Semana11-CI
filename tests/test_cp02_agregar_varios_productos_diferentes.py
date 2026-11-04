"""CP-02 · Agregar varios productos diferentes"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP, MOUSE


class TestCP02(TiendaDemoTestCase):
    # CP-02 · Agregar varios productos diferentes
    def test_cp02_agregar_varios_productos_diferentes(self):
        self.open_cart_with(LAPTOP, MOUSE)
        self.assertCountEqual(self.cart.get_item_names(), [LAPTOP, MOUSE])
        self.assertEqual(self.catalog.get_cart_count(), 2)


if __name__ == '__main__':
    unittest.main()
