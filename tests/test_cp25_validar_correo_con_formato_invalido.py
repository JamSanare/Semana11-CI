"""CP-25 · Validar correo con formato inválido (sin @)"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, cliente_con


class TestCP25(TiendaDemoTestCase):
    # Rellena el checkout con datos válidos salvo los indicados, y confirma.
    def _confirmar_con(self, **cambios):
        self.open_checkout_with(DISCO)
        self.checkout.fill_form(cliente_con(**cambios))
        self.checkout.confirm_payment()

    # CP-25 · Validar correo con formato inválido (sin @)
    def test_cp25_validar_correo_con_formato_invalido(self):
        self._confirmar_con(email="maria.correo.com")
        self.assertEqual(self.checkout.get_fields_with_error(), ["email"])
        self.assertIn("correo válido", self.checkout.get_field_error("email"))
        self.assertFalse(self.confirmation.is_displayed())


if __name__ == '__main__':
    unittest.main()
