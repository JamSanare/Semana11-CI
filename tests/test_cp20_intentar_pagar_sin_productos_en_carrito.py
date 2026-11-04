"""CP-20 · Intentar pagar sin productos en carrito"""

import unittest

from tests.base_test import TiendaDemoTestCase


class TestCP20(TiendaDemoTestCase):
    # CP-20 · Intentar pagar sin productos en carrito
    def test_cp20_intentar_pagar_sin_productos_en_carrito(self):
        self.catalog.open_cart()
        self.assertTrue(self.cart.has_empty_message())
        self.assertFalse(self.cart.has_checkout_button(), "No debe ofrecerse 'Proceder al pago'")
        self.assertFalse(self.checkout.is_displayed(), "No debe abrirse el checkout")


if __name__ == '__main__':
    unittest.main()
