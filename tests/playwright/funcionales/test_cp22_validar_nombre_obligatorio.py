"""CP-22 · Validar nombre obligatorio  [Playwright]"""

import pytest

from utils.test_data import DISCO, cliente_con

pytestmark = pytest.mark.funcional


def test_cp22_validar_nombre_obligatorio(tienda):
    tienda.open_checkout_with(DISCO)
    tienda.checkout.fill_form(cliente_con(name=""))
    tienda.checkout.confirm_payment()
    assert tienda.checkout.get_fields_with_error() == ["nombre"]
    assert "nombre es obligatorio" in tienda.checkout.get_field_error("nombre")
    assert not tienda.confirmation.is_displayed()
