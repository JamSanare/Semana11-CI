"""CP-23 · Validar apellido obligatorio  [Playwright]"""

import pytest

from utils.test_data import DISCO, cliente_con

pytestmark = [pytest.mark.funcional, pytest.mark.defecto]


def test_cp23_validar_apellido_obligatorio(tienda):
    # DEFECTO DEF-01 (conocido): el formulario solo tiene "Nombre completo" y
    # no existe el campo "Apellido", por lo que no se puede exigir. El caso
    # espera un error de apellido obligatorio; la app confirma la compra con
    # solo el nombre de pila. Este test FALLA a propósito hasta que se corrija
    # la app: su resultado es el defecto, no un problema de la prueba.
    tienda.open_checkout_with(DISCO)
    tienda.checkout.fill_form(cliente_con(name="María"))
    tienda.checkout.confirm_payment()
    assert not tienda.confirmation.is_displayed(), \
        "La compra se confirmó con un nombre sin apellido: la app no valida el apellido"
    assert "nombre" in tienda.checkout.get_fields_with_error()
