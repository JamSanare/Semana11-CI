"""CP-17 · Aplicar cupón repetido: el descuento no debe acumularse."""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import TECLADO, PRECIOS, CUPON_VALIDO, DESCUENTO_VALIDO

PRECIO = PRECIOS[TECLADO]
TOTAL_CON_DESCUENTO = PRECIO * (1 - DESCUENTO_VALIDO)


class TestCP17(TiendaDemoTestCase):
    # Precondición común: carrito con un producto, vista del carrito abierta.
    def setUp(self):
        super().setUp()
        self.open_cart_with(TECLADO)

    # CP-17 · Aplicar cupón repetido: el descuento no debe acumularse.
    # (La app vuelve a mostrar "cupón aplicado" sin un aviso específico.)
    def test_cp17_aplicar_cupon_repetido(self):
        self.cart.apply_coupon(CUPON_VALIDO)
        total_primera_vez = self.cart.get_total()
        self.cart.apply_coupon(CUPON_VALIDO)
        self.assertAlmostEqual(total_primera_vez, TOTAL_CON_DESCUENTO, places=2)
        self.assertAlmostEqual(self.cart.get_total(), total_primera_vez, places=2,
                               msg="El segundo intento no debe aplicar otro descuento")
        self.assertAlmostEqual(self.cart.get_discount(), PRECIO * DESCUENTO_VALIDO, places=2)


if __name__ == '__main__':
    unittest.main()
