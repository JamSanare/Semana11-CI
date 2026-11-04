"""CP-26 · Validar teléfono obligatorio  [Playwright]"""

import pytest

from utils.test_data import DISCO, cliente_con

pytestmark = pytest.mark.funcional


def test_cp26_validar_telefono_obligatorio(tienda):
    tienda.open_checkout_with(DISCO)
    tienda.checkout.fill_form(cliente_con(phone=""))
    tienda.checkout.confirm_payment()
    assert tienda.checkout.get_fields_with_error() == ["telefono"]
    assert not tienda.confirmation.is_displayed()
