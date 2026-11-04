"""CP-27 · Validar dirección obligatoria  [Playwright]"""

import pytest

from utils.test_data import DISCO, cliente_con

pytestmark = pytest.mark.funcional


def test_cp27_validar_direccion_obligatoria(tienda):
    tienda.open_checkout_with(DISCO)
    tienda.checkout.fill_form(cliente_con(address=""))
    tienda.checkout.confirm_payment()
    assert tienda.checkout.get_fields_with_error() == ["direccion"]
    assert "dirección es obligatoria" in tienda.checkout.get_field_error("direccion")
    assert not tienda.confirmation.is_displayed()
