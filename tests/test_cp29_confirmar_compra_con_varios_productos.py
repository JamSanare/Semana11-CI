"""CP-29 · Confirmar compra con varios productos"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import LAPTOP, MOUSE, TECLADO, PRECIOS, MENSAJE_COMPRA_EXITOSA


class TestCP29(TiendaDemoTestCase):
    # CP-29 · Confirmar compra con varios productos
    def test_cp29_confirmar_compra_con_varios_productos(self):
        self.buy(LAPTOP, MOUSE, TECLADO)
        self.assertEqual(self.confirmation.get_title(), MENSAJE_COMPRA_EXITOSA)
        esperado = PRECIOS[LAPTOP] + PRECIOS[MOUSE] + PRECIOS[TECLADO]
        self.assertAlmostEqual(self.confirmation.get_paid_total(), esperado, places=2)


if __name__ == '__main__':
    unittest.main()
