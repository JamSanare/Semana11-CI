"""CP-21 · Confirmar checkout con datos vacíos  [Playwright]"""

import pytest

from utils.test_data import DISCO

pytestmark = pytest.mark.funcional


def test_cp21_confirmar_checkout_con_datos_vacios(tienda):
    tienda.open_checkout_with(DISCO)
    tienda.checkout.confirm_payment()
    assert sorted(tienda.checkout.get_fields_with_error()) == sorted(
        ["nombre", "email", "direccion", "ciudad", "telefono"])
    assert not tienda.confirmation.is_displayed()
