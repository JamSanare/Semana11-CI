# Proyecto TiendaDemo

Pruebas funcionales y de aceptación (UAT) de la tienda demo, con Selenium + Page Object Model,
y también con **Playwright** (ver `tests/playwright/README.md`).
Cubre los **41 casos** del *Registro de casos de prueba*: 31 funcionales (CP-01 a CP-31) y 10 de aceptación (CP-32 a CP-41).

## Estructura

| Carpeta | Contenido |
|---|---|
| `app/` | Aplicación bajo prueba (`tienda_demo.html`, `carrito.js`, `estilos.css`) |
| `pages/` | Page Objects: `BasePage`, `CatalogPage`, `CartPage`, `CheckoutPage`, `ConfirmationPage` |
| `tests/` | **Casos funcionales** CP-01 a CP-31 (Selenium + unittest): **un archivo por caso**, `test_cpNN_<nombre>.py`. `base_test.py` es la clase base común |
| `tests/playwright/` | **Los 41 casos en Playwright + pytest**: `funcionales/` (CP-01 a CP-31) y `uat/` (CP-32 a CP-41), un archivo por caso; Page Objects en `pw_pages/` |
| `features/funcionales/` y `features/uat/` | **Gherkin: un `.feature` por caso** (41 en total, en español), `cpNN_<nombre>.feature`. Etiquetas `@funcional` / `@uat` y `@CP-xx` |
| `features/steps/` | Step definitions de Behave. **Aceptación (UAT)**: un archivo por caso `uat_cpNN_..._steps.py`; acciones compartidas en `carrito_steps.py` y `checkout_steps.py` |
| `features/environment.py` | Hooks de Behave (abre/cierra navegador; captura de pantalla si un paso falla) |
| `utils/` | `driver_factory.py` (Chrome), `config.py` (URL base), `test_data.py` (productos, cupones, cliente válido) |

## Instalación

```bash
pip install -r requirements.txt
```

Requiere Google Chrome instalado (Selenium 4 descarga el chromedriver automáticamente).

## Ejecución

Todos los comandos se ejecutan desde la raíz del proyecto.

```bash
# Casos funcionales (31) con unittest
python -m unittest discover -s tests
python -m unittest tests.test_cp18_verificar_total_con_descuento   # un solo caso

# Gherkin con Behave (los 41 escenarios)
behave features
behave features --tags=@uat            # solo aceptación (CP-32 a CP-41)
behave features --tags=@funcional      # solo funcionales (CP-01 a CP-31)
behave features --tags=@CP-41          # un caso concreto
behave features/uat/cp41_flujo_completo_de_compra.feature   # o por archivo
```

```bash
# Playwright (los 41 casos) — requiere una vez: python -m playwright install chromium
pytest tests/playwright
pytest tests/playwright -m funcional   # CP-01 a CP-31
pytest tests/playwright -m uat         # CP-32 a CP-41
pytest tests/playwright -k cp18        # un caso concreto
```

Las capturas de pasos fallidos de Behave quedan en `evidencias/behave/`.

Variables de entorno opcionales (CI, contenedores, Chrome en otra ruta):
`CHROME_BINARY`, `CHROMEDRIVER_PATH`, `CHROME_NO_SANDBOX=1`.

## Resultado de la última ejecución

- `unittest`: 31 pruebas → **30 OK, 1 falla (CP-23, DEF-01)**.
- `behave`: 41 escenarios → **40 OK, 1 falla (CP-23, DEF-01)**.

### Defectos encontrados

- **DEF-01 · CP-23 (apellido obligatorio) — defecto de la app.** El formulario solo tiene un campo *Nombre completo*;
  no existe campo *Apellido* y la app acepta un nombre de una sola palabra ("María") y confirma la compra.
  El caso queda **fallando a propósito** (escenario etiquetado `@defecto`) hasta que se corrija la app.

### Observaciones al automatizar

- **CP-09 (cantidad negativa):** la interfaz no tiene campo para escribir cantidades (solo botones − y +), por lo que no se puede
  ingresar -1. La prueba verifica que no existe ese campo y que seguir pulsando − nunca deja el contador bajo 0.
- **CP-08 (cantidad cero):** regla aplicada por la app: al llegar a 0 el producto se elimina.
- **CP-17 (cupón repetido):** la app no muestra un aviso, pero tampoco acumula el descuento; la prueba verifica que no se acumula.
- **CP-24 y CP-26:** el mensaje de la app dice "Ingresa un correo válido" / "Ingresa un teléfono válido", no "obligatorio";
  se valida que aparezca el error del campo correcto.

## Trazabilidad

Un archivo por caso de prueba. En UAT, los casos sin steps propios (CP-33, CP-38, CP-41) reutilizan los pasos compartidos.

| ID | Tipo | Caso de prueba | Test Selenium (unittest) | Gherkin | Steps propios |
|---|---|---|---|---|---|
| CP-01 | Funcional | Agregar producto al carrito | `tests/test_cp01_agregar_producto_al_carrito.py` | `features/funcionales/cp01_agregar_producto_al_carrito.feature` | compartidos |
| CP-02 | Funcional | Agregar varios productos diferentes | `tests/test_cp02_agregar_varios_productos_diferentes.py` | `features/funcionales/cp02_agregar_varios_productos_diferentes.feature` | compartidos |
| CP-03 | Funcional | Agregar el mismo producto dos veces | `tests/test_cp03_agregar_el_mismo_producto_dos_veces.py` | `features/funcionales/cp03_agregar_el_mismo_producto_dos_veces.feature` | compartidos |
| CP-04 | Funcional | Verificar contador del carrito | `tests/test_cp04_verificar_contador_del_carrito.py` | `features/funcionales/cp04_verificar_contador_del_carrito.feature` | compartidos |
| CP-05 | Funcional | Ver producto en el carrito | `tests/test_cp05_ver_producto_en_el_carrito.py` | `features/funcionales/cp05_ver_producto_en_el_carrito.feature` | compartidos |
| CP-06 | Funcional | Aumentar cantidad de un producto | `tests/test_cp06_aumentar_cantidad_de_un_producto.py` | `features/funcionales/cp06_aumentar_cantidad_de_un_producto.feature` | compartidos |
| CP-07 | Funcional | Disminuir cantidad de un producto | `tests/test_cp07_disminuir_cantidad_de_un_producto.py` | `features/funcionales/cp07_disminuir_cantidad_de_un_producto.feature` | compartidos |
| CP-08 | Funcional | Cambiar cantidad a cero | `tests/test_cp08_cambiar_cantidad_a_cero.py` | `features/funcionales/cp08_cambiar_cantidad_a_cero.feature` | compartidos |
| CP-09 | Funcional | Ingresar cantidad negativa | `tests/test_cp09_ingresar_cantidad_negativa.py` | `features/funcionales/cp09_ingresar_cantidad_negativa.feature` | compartidos |
| CP-10 | Funcional | Eliminar un producto del carrito | `tests/test_cp10_eliminar_un_producto_del_carrito.py` | `features/funcionales/cp10_eliminar_un_producto_del_carrito.feature` | compartidos |
| CP-11 | Funcional | Eliminar último producto del carrito | `tests/test_cp11_eliminar_ultimo_producto_del_carrito.py` | `features/funcionales/cp11_eliminar_ultimo_producto_del_carrito.feature` | compartidos |
| CP-12 | Funcional | Eliminar un producto cuando hay varios | `tests/test_cp12_eliminar_un_producto_cuando_hay_varios.py` | `features/funcionales/cp12_eliminar_un_producto_cuando_hay_varios.feature` | compartidos |
| CP-13 | Funcional | Actualizar subtotal al eliminar producto | `tests/test_cp13_actualizar_subtotal_al_eliminar_producto.py` | `features/funcionales/cp13_actualizar_subtotal_al_eliminar_producto.feature` | compartidos |
| CP-14 | Funcional | Aplicar cupón válido | `tests/test_cp14_aplicar_cupon_valido.py` | `features/funcionales/cp14_aplicar_cupon_valido.feature` | compartidos |
| CP-15 | Funcional | Aplicar cupón inválido | `tests/test_cp15_aplicar_cupon_invalido.py` | `features/funcionales/cp15_aplicar_cupon_invalido.feature` | compartidos |
| CP-16 | Funcional | Aplicar cupón vacío | `tests/test_cp16_aplicar_cupon_vacio.py` | `features/funcionales/cp16_aplicar_cupon_vacio.feature` | compartidos |
| CP-17 | Funcional | Aplicar cupón repetido | `tests/test_cp17_aplicar_cupon_repetido.py` | `features/funcionales/cp17_aplicar_cupon_repetido.feature` | compartidos |
| CP-18 | Funcional | Verificar total con descuento | `tests/test_cp18_verificar_total_con_descuento.py` | `features/funcionales/cp18_verificar_total_con_descuento.feature` | compartidos |
| CP-19 | Funcional | Verificar total sin descuento | `tests/test_cp19_verificar_total_sin_descuento.py` | `features/funcionales/cp19_verificar_total_sin_descuento.feature` | compartidos |
| CP-20 | Funcional | Intentar pagar sin productos en carrito | `tests/test_cp20_intentar_pagar_sin_productos_en_carrito.py` | `features/funcionales/cp20_intentar_pagar_sin_productos_en_carrito.feature` | compartidos |
| CP-21 | Funcional | Confirmar checkout con datos vacíos | `tests/test_cp21_confirmar_checkout_con_datos_vacios.py` | `features/funcionales/cp21_confirmar_checkout_con_datos_vacios.feature` | compartidos |
| CP-22 | Funcional | Validar nombre obligatorio | `tests/test_cp22_validar_nombre_obligatorio.py` | `features/funcionales/cp22_validar_nombre_obligatorio.feature` | compartidos |
| CP-23 | Funcional | Validar apellido obligatorio | `tests/test_cp23_validar_apellido_obligatorio.py` | `features/funcionales/cp23_validar_apellido_obligatorio.feature` | compartidos |
| CP-24 | Funcional | Validar correo obligatorio | `tests/test_cp24_validar_correo_obligatorio.py` | `features/funcionales/cp24_validar_correo_obligatorio.feature` | compartidos |
| CP-25 | Funcional | Validar correo con formato inválido | `tests/test_cp25_validar_correo_con_formato_invalido.py` | `features/funcionales/cp25_validar_correo_con_formato_invalido.feature` | compartidos |
| CP-26 | Funcional | Validar teléfono obligatorio | `tests/test_cp26_validar_telefono_obligatorio.py` | `features/funcionales/cp26_validar_telefono_obligatorio.feature` | compartidos |
| CP-27 | Funcional | Validar dirección obligatoria | `tests/test_cp27_validar_direccion_obligatoria.py` | `features/funcionales/cp27_validar_direccion_obligatoria.feature` | compartidos |
| CP-28 | Funcional | Confirmar compra con datos válidos | `tests/test_cp28_confirmar_compra_con_datos_validos.py` | `features/funcionales/cp28_confirmar_compra_con_datos_validos.feature` | compartidos |
| CP-29 | Funcional | Confirmar compra con varios productos | `tests/test_cp29_confirmar_compra_con_varios_productos.py` | `features/funcionales/cp29_confirmar_compra_con_varios_productos.feature` | compartidos |
| CP-30 | Funcional | Ver pantalla de confirmación | `tests/test_cp30_ver_pantalla_de_confirmacion.py` | `features/funcionales/cp30_ver_pantalla_de_confirmacion.feature` | compartidos |
| CP-31 | Funcional | Volver al catálogo desde confirmación | `tests/test_cp31_volver_al_catalogo_desde_confirmacion.py` | `features/funcionales/cp31_volver_al_catalogo_desde_confirmacion.feature` | compartidos |
| CP-32 | UAT | Agregar producto desde la perspectiva del usuario | — | `features/uat/cp32_agregar_producto_desde_la_perspectiva_del_usuario.feature` | `features/steps/uat_cp32_agregar_producto_desde_la_perspectiva_del_usuario_steps.py` |
| CP-33 | UAT | Ver el carrito con el producto agregado | — | `features/uat/cp33_ver_el_carrito_con_el_producto_agregado.feature` | — |
| CP-34 | UAT | Aplicar cupón válido | — | `features/uat/cp34_aplicar_cupon_valido.feature` | `features/steps/uat_cp34_aplicar_cupon_valido_steps.py` |
| CP-35 | UAT | Completar checkout con datos normales | — | `features/uat/cp35_completar_checkout_con_datos_normales.feature` | `features/steps/uat_cp35_completar_checkout_con_datos_normales_steps.py` |
| CP-36 | UAT | Intentar compra con datos incompletos | — | `features/uat/cp36_intentar_compra_con_datos_incompletos.feature` | `features/steps/uat_cp36_intentar_compra_con_datos_incompletos_steps.py` |
| CP-37 | UAT | Confirmar pedido final | — | `features/uat/cp37_confirmar_pedido_final.feature` | `features/steps/uat_cp37_confirmar_pedido_final_steps.py` |
| CP-38 | UAT | Comprar con más de un artículo | — | `features/uat/cp38_comprar_con_mas_de_un_articulo.feature` | — |
| CP-39 | UAT | Intentar compra con carrito vacío | — | `features/uat/cp39_intentar_compra_con_carrito_vacio.feature` | `features/steps/uat_cp39_intentar_compra_con_carrito_vacio_steps.py` |
| CP-40 | UAT | Validar total final correcto | — | `features/uat/cp40_validar_total_final_correcto.feature` | `features/steps/uat_cp40_validar_total_final_correcto_steps.py` |
| CP-41 | UAT | Flujo completo de compra | — | `features/uat/cp41_flujo_completo_de_compra.feature` | — |
