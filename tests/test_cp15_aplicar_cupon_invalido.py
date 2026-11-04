"""CP-15 · Aplicar cupón inválido"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, PRECIOS, CUPON_INVALIDO

PRECIO = PRECIOS[TECLADO]


class TestCP15(TiendaDemoTestCase):
    # Precondición común: carrito con un producto, vista del carrito abierta.
    def setUp(self):
        super().setUp()
        self.open_cart_with(TECLADO)

    # CP-15 · Aplicar cupón inválido
    def test_cp15_aplicar_cupon_invalido(self):
        self.cart.apply_coupon(CUPON_INVALIDO)
        self.assertIn("Cupón no válido", self.cart.get_coupon_message())
        self.assertFalse(self.cart.has_discount(), "No debe aplicarse descuento")
        self.assertAlmostEqual(self.cart.get_total(), PRECIO, places=2)


if __name__ == '__main__':
    unittest.main()
