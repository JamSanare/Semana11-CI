"""CP-19 · Verificar total sin descuento"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, PRECIOS

PRECIO = PRECIOS[TECLADO]


class TestCP19(TiendaDemoTestCase):
    # Precondición común: carrito con un producto, vista del carrito abierta.
    def setUp(self):
        super().setUp()
        self.open_cart_with(TECLADO)

    # CP-19 · Verificar total sin descuento
    def test_cp19_verificar_total_sin_descuento(self):
        self.assertFalse(self.cart.has_discount())
        self.assertAlmostEqual(self.cart.get_total(), PRECIO, places=2)


if __name__ == '__main__':
    unittest.main()
