"""CP-25 · Validar correo con formato inválido (sin @)  [Playwright]"""

import pytest

from utils.test_data import DISCO, cliente_con

pytestmark = pytest.mark.funcional


def test_cp25_validar_correo_con_formato_invalido(tienda):
    tienda.open_checkout_with(DISCO)
    tienda.checkout.fill_form(cliente_con(email="maria.correo.com"))
    tienda.checkout.confirm_payment()
    assert tienda.checkout.get_fields_with_error() == ["email"]
    assert "correo válido" in tienda.checkout.get_field_error("email")
    assert not tienda.confirmation.is_displayed()
