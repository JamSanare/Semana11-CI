"""CP-14 · Aplicar cupón válido"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, CUPON_VALIDO


class TestCP14(TiendaDemoTestCase):
    # Precondición común: carrito con un producto, vista del carrito abierta.
    def setUp(self):
        super().setUp()
        self.open_cart_with(TECLADO)

    # CP-14 · Aplicar cupón válido
    def test_cp14_aplicar_cupon_valido(self):
        self.cart.apply_coupon(CUPON_VALIDO)
        message = self.cart.get_coupon_message()
        self.assertIn(CUPON_VALIDO, message)
        self.assertIn("aplicado", message)


if __name__ == '__main__':
    unittest.main()
