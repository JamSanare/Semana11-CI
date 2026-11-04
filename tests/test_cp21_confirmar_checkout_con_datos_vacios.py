"""CP-21 · Confirmar checkout con datos vacíos"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO


class TestCP21(TiendaDemoTestCase):
    # CP-21 · Confirmar checkout con datos vacíos
    def test_cp21_confirmar_checkout_con_datos_vacios(self):
        self.open_checkout_with(DISCO)
        self.checkout.confirm_payment()
        self.assertCountEqual(self.checkout.get_fields_with_error(),
                              ["nombre", "email", "direccion", "ciudad", "telefono"])
        self.assertFalse(self.confirmation.is_displayed())


if __name__ == '__main__':
    unittest.main()
