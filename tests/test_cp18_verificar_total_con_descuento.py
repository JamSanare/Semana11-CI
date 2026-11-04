"""CP-18 · Verificar total con descuento"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, PRECIOS, CUPON_VALIDO, DESCUENTO_VALIDO

PRECIO = PRECIOS[TECLADO]
TOTAL_CON_DESCUENTO = PRECIO * (1 - DESCUENTO_VALIDO)


class TestCP18(TiendaDemoTestCase):
    # Precondición común: carrito con un producto, vista del carrito abierta.
    def setUp(self):
        super().setUp()
        self.open_cart_with(TECLADO)

    # CP-18 · Verificar total con descuento
    def test_cp18_verificar_total_con_descuento(self):
        self.cart.apply_coupon(CUPON_VALIDO)
        self.assertAlmostEqual(self.cart.get_subtotal(), PRECIO, places=2)
        self.assertAlmostEqual(self.cart.get_discount(), PRECIO * DESCUENTO_VALIDO, places=2)
        self.assertAlmostEqual(self.cart.get_total(), TOTAL_CON_DESCUENTO, places=2)


if __name__ == '__main__':
    unittest.main()
