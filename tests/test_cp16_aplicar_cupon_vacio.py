"""CP-16 · Aplicar cupón vacío"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, PRECIOS

PRECIO = PRECIOS[TECLADO]


class TestCP16(TiendaDemoTestCase):
    # Precondición común: carrito con un producto, vista del carrito abierta.
    def setUp(self):
        super().setUp()
        self.open_cart_with(TECLADO)

    # CP-16 · Aplicar cupón vacío
    def test_cp16_aplicar_cupon_vacio(self):
        self.cart.apply_coupon("")
        self.assertIn("Ingresa un código", self.cart.get_coupon_message())
        self.assertFalse(self.cart.has_discount())
        self.assertAlmostEqual(self.cart.get_total(), PRECIO, places=2)


if __name__ == '__main__':
    unittest.main()
