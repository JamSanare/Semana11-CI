"""CP-28 · Confirmar compra con datos válidos"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, MENSAJE_COMPRA_EXITOSA


class TestCP28(TiendaDemoTestCase):
    # CP-28 · Confirmar compra con datos válidos
    def test_cp28_confirmar_compra_con_datos_validos(self):
        self.buy(DISCO)
        self.assertEqual(self.confirmation.get_title(), MENSAJE_COMPRA_EXITOSA)


if __name__ == '__main__':
    unittest.main()
