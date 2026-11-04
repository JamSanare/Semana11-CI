"""CP-24 · Validar correo obligatorio  [Playwright]"""

import pytest

from utils.test_data import DISCO, cliente_con

pytestmark = pytest.mark.funcional


def test_cp24_validar_correo_obligatorio(tienda):
    tienda.open_checkout_with(DISCO)
    tienda.checkout.fill_form(cliente_con(email=""))
    tienda.checkout.confirm_payment()
    assert tienda.checkout.get_fields_with_error() == ["email"]
    assert not tienda.confirmation.is_displayed()
