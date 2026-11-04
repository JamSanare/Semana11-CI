"""CP-30 · Ver pantalla de confirmación"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, PRECIOS, CLIENTE_VALIDO


class TestCP30(TiendaDemoTestCase):
    # CP-30 · Ver pantalla de confirmación
    def test_cp30_ver_pantalla_de_confirmacion(self):
        self.buy(DISCO)
        self.assertTrue(self.confirmation.is_displayed())
        self.assertTrue(self.confirmation.get_order_number().startswith("ORD-"))
        self.assertIn("Confirmado", self.confirmation.get_status())
        self.assertEqual(self.confirmation.get_email(), CLIENTE_VALIDO["email"])
        self.assertAlmostEqual(self.confirmation.get_paid_total(), PRECIOS[DISCO], places=2)


if __name__ == '__main__':
    unittest.main()
