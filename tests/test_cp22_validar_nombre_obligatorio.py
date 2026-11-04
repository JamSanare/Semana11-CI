"""CP-22 · Validar nombre obligatorio"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, cliente_con


class TestCP22(TiendaDemoTestCase):
    # Rellena el checkout con datos válidos salvo los indicados, y confirma.
    def _confirmar_con(self, **cambios):
        self.open_checkout_with(DISCO)
        self.checkout.fill_form(cliente_con(**cambios))
        self.checkout.confirm_payment()

    # CP-22 · Validar nombre obligatorio
    def test_cp22_validar_nombre_obligatorio(self):
        self._confirmar_con(name="")
        self.assertEqual(self.checkout.get_fields_with_error(), ["nombre"])
        self.assertIn("nombre es obligatorio", self.checkout.get_field_error("nombre"))
        self.assertFalse(self.confirmation.is_displayed())


if __name__ == '__main__':
    unittest.main()
