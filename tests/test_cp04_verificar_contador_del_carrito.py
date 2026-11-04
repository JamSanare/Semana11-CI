"""CP-04 · Verificar contador del carrito"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP, TECLADO


class TestCP04(TiendaDemoTestCase):
    # CP-04 · Verificar contador del carrito
    def test_cp04_verificar_contador_del_carrito(self):
        self.assertEqual(self.catalog.get_cart_count(), 0, "El carrito inicia en 0")
        self.catalog.add_product(TECLADO)
        self.assertEqual(self.catalog.get_cart_count(), 1)
        self.catalog.add_product(LAPTOP)
        self.assertEqual(self.catalog.get_cart_count(), 2)


if __name__ == '__main__':
    unittest.main()
