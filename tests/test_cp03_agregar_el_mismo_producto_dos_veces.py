"""CP-03 · Agregar el mismo producto dos veces"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import MOUSE, PRECIOS


class TestCP03(TiendaDemoTestCase):
    # CP-03 · Agregar el mismo producto dos veces
    def test_cp03_agregar_el_mismo_producto_dos_veces(self):
        self.open_cart_with(MOUSE, MOUSE)
        self.assertEqual(self.cart.get_item_names(), [MOUSE], "Debe haber una sola fila")
        self.assertEqual(self.cart.get_quantity(MOUSE), 2)
        self.assertAlmostEqual(self.cart.get_item_subtotal(MOUSE), 2 * PRECIOS[MOUSE], places=2)


if __name__ == '__main__':
    unittest.main()
