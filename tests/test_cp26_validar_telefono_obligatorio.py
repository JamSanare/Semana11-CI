"""CP-26 · Validar teléfono obligatorio"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, cliente_con


class TestCP26(TiendaDemoTestCase):
    # Rellena el checkout con datos válidos salvo los indicados, y confirma.
    def _confirmar_con(self, **cambios):
        self.open_checkout_with(DISCO)
        self.checkout.fill_form(cliente_con(**cambios))
        self.checkout.confirm_payment()

    # CP-26 · Validar teléfono obligatorio
    def test_cp26_validar_telefono_obligatorio(self):
        self._confirmar_con(phone="")
        self.assertEqual(self.checkout.get_fields_with_error(), ["telefono"])
        self.assertFalse(self.confirmation.is_displayed())


if __name__ == '__main__':
    unittest.main()
