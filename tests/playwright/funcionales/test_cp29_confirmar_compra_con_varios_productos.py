"""CP-29 · Confirmar compra con varios productos  [Playwright]"""

import pytest

from utils.test_data import LAPTOP, MOUSE, TECLADO, PRECIOS, MENSAJE_COMPRA_EXITOSA

pytestmark = pytest.mark.funcional


def dinero(monto):
    """Compara importes en soles con tolerancia de medio céntimo."""
    return pytest.approx(monto, abs=0.005)


def test_cp29_confirmar_compra_con_varios_productos(tienda):
    tienda.buy(LAPTOP, MOUSE, TECLADO)
    assert tienda.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
    esperado = PRECIOS[LAPTOP] + PRECIOS[MOUSE] + PRECIOS[TECLADO]
    assert tienda.confirmation.get_paid_total() == dinero(esperado)
