"""CP-31 · Volver al catálogo desde confirmación"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import MOUSE, DISCO


class TestCP31(TiendaDemoTestCase):
    # CP-31 · Volver al catálogo desde confirmación
    def test_cp31_volver_al_catalogo_desde_confirmacion(self):
        self.buy(DISCO)
        self.confirmation.continue_shopping()
        self.assertTrue(self.catalog.is_displayed())
        self.assertEqual(self.catalog.get_cart_count(), 0, "El carrito se vacía tras la compra")
        self.catalog.add_product(MOUSE)             # el usuario puede seguir comprando
        self.assertEqual(self.catalog.get_cart_count(), 1)


if __name__ == '__main__':
    unittest.main()
