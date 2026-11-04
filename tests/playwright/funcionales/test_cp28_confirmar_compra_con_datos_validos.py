"""CP-28 · Confirmar compra con datos válidos  [Playwright]"""

import pytest

from utils.test_data import DISCO, MENSAJE_COMPRA_EXITOSA

pytestmark = pytest.mark.funcional


def test_cp28_confirmar_compra_con_datos_validos(tienda):
    tienda.buy(DISCO)
    assert tienda.confirmation.get_title() == MENSAJE_COMPRA_EXITOSA
