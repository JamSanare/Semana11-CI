"""Hooks de Behave: preparan el navegador y los Page Objects de cada escenario.

- before_scenario: abre un navegador nuevo (estado limpio) y crea los Page Objects.
- after_step:      si un paso falla, guarda una captura en evidencias/behave/.
- after_scenario:  cierra el navegador y libera recursos.
"""

import os
import re
import sys

# Behave solo añade features/ al path: se añade la raíz del proyecto para poder
# importar pages/ y utils/ igual que lo hacen los tests de unittest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages import CatalogPage, CartPage, CheckoutPage, ConfirmationPage  # noqa: E402
from utils.config import EVIDENCE_DIR  # noqa: E402
from utils.driver_factory import DriverFactory  # noqa: E402


def before_scenario(context, scenario):
    context.driver = DriverFactory.create_chrome()
    context.catalog = CatalogPage(context.driver)
    context.cart = CartPage(context.driver)
    context.checkout = CheckoutPage(context.driver)
    context.confirmation = ConfirmationPage(context.driver)


def after_step(context, step):
    if step.status == "failed" and getattr(context, 'driver', None):
        folder = EVIDENCE_DIR / "behave"
        folder.mkdir(parents=True, exist_ok=True)
        name = re.sub(r'[^A-Za-z0-9_-]+', '_', context.scenario.name)[:80]
        context.driver.save_screenshot(str(folder / f"{name}.png"))


def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        context.driver = None
