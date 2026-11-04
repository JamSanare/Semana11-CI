"""CP-30 · Ver pantalla de confirmación  [Playwright]"""

import pytest

from utils.test_data import DISCO, PRECIOS, CLIENTE_VALIDO

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp30_ver_pantalla_de_confirmacion(tienda):
    tienda.buy(DISCO)
    assert tienda.confirmation.is_displayed()
    assert tienda.confirmation.get_order_number().startswith("ORD-")
    assert "Confirmado" in tienda.confirmation.get_status()
    assert tienda.confirmation.get_email() == CLIENTE_VALIDO["email"]
    assert tienda.confirmation.get_paid_total() == dinero(PRECIOS[DISCO])
