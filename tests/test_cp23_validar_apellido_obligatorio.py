"""CP-23 · Validar apellido obligatorio"""

import unittest

from tests.base_test import TiendaDemoTestCase
from utils.test_data import DISCO, cliente_con


class TestCP23(TiendaDemoTestCase):
    # Rellena el checkout con datos válidos salvo los indicados, y confirma.
    def _confirmar_con(self, **cambios):
        self.open_checkout_with(DISCO)
        self.checkout.fill_form(cliente_con(**cambios))
        self.checkout.confirm_payment()

    # CP-23 · Validar apellido obligatorio
    # DEFECTO DEF-01 (conocido): el formulario solo tiene "Nombre completo" y
    # no existe el campo "Apellido", por lo que no se puede exigir. El caso
    # espera un error de apellido obligatorio; la app confirma la compra con
    # solo el nombre de pila. Este test FALLA a propósito hasta que se corrija
    # la app: su resultado es el defecto, no un problema de la prueba.
    def test_cp23_validar_apellido_obligatorio(self):
        self._confirmar_con(name="María")
        self.assertFalse(self.confirmation.is_displayed(),
                         "La compra se confirmó con un nombre sin apellido: la app no valida el apellido")
        self.assertIn("nombre", self.checkout.get_fields_with_error())


if __name__ == '__main__':
    unittest.main()
