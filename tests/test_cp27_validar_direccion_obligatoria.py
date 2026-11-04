"""CP-27 · Validar dirección obligatoria"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, cliente_con


class TestCP27(TiendaDemoTestCase):
    # Rellena el checkout con datos válidos salvo los indicados, y confirma.
    def _confirmar_con(self, **cambios):
        self.open_checkout_with(DISCO)
        self.checkout.fill_form(cliente_con(**cambios))
        self.checkout.confirm_payment()

    # CP-27 · Validar dirección obligatoria
    def test_cp27_validar_direccion_obligatoria(self):
        self._confirmar_con(address="")
        self.assertEqual(self.checkout.get_fields_with_error(), ["direccion"])
        self.assertIn("dirección es obligatoria", self.checkout.get_field_error("direccion"))
        self.assertFalse(self.confirmation.is_displayed())


if __name__ == '__main__':
    unittest.main()
