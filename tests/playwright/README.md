# Pruebas Playwright — TiendaDemo

Los mismos **41 casos** del registro (CP-01 a CP-41), migrados de Selenium/Behave a
**Playwright para Python** con **pytest** y Page Object Model.

## Estructura

```
tests/playwright/
├── pytest.ini            configuración (rutas, marcas, captura en fallos)
├── conftest.py           fixture "tienda": abre la app y entrega los Page Objects
├── pw_pages/             Page Objects Playwright (catálogo, carrito, checkout, confirmación)
├── funcionales/          CP-01 … CP-31  →  test_cpNN_<nombre>.py   (marca @funcional)
└── uat/                  CP-32 … CP-41  →  test_cpNN_<nombre>.py   (marca @uat)
```

Los datos de prueba (productos, precios, cupones, cliente válido) se reutilizan de
`utils/test_data.py`, igual que en Selenium. Cada test recibe un navegador limpio,
así que el carrito siempre empieza vacío.

## Instalación (una sola vez)

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Ejecución

Desde la **raíz del proyecto**:

| Qué ejecutar | Comando |
|---|---|
| Los 41 casos | `pytest tests/playwright` |
| Solo funcionales (CP-01 a CP-31) | `pytest tests/playwright -m funcional` |
| Solo aceptación UAT (CP-32 a CP-41) | `pytest tests/playwright -m uat` |
| Todo menos el defecto conocido (CP-23) | `pytest tests/playwright -m "not defecto"` |
| Un caso por número | `pytest tests/playwright -k cp18` |
| Varios casos | `pytest tests/playwright -k "cp01 or cp14 or cp41"` |
| Un caso por archivo | `pytest tests/playwright/funcionales/test_cp18_verificar_total_con_descuento.py` |
| Viendo el navegador | `pytest tests/playwright -k cp41 --headed --slowmo 500` |
| En Firefox / WebKit | `pytest tests/playwright --browser firefox` (antes: `python -m playwright install firefox`) |

Las capturas de pantalla de los tests fallidos quedan en `evidencias-playwright/`.

## Resultado de la última ejecución

41 pruebas → **40 OK, 1 falla (CP-23, DEF-01)**, igual que con Selenium/Behave.
CP-23 falla a propósito: la app no tiene campo *Apellido* y confirma la compra con
solo "María". Lleva la marca `defecto` para poder excluirlo con `-m "not defecto"`.
