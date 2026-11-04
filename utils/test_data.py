"""Datos de prueba de TiendaDemo (catálogo, cupones y cliente de ejemplo).

Los valores salen de app/carrito.js: si cambian allí, se cambian aquí.
"""

import re

# --- Productos del catálogo (nombre -> precio unitario en soles) -------------
LAPTOP = "Laptop Pro 15"
MOUSE = "Mouse Inalámbrico"
TECLADO = "Teclado Mecánico"
DISCO = "Disco SSD 1TB"

PRECIOS = {
    LAPTOP: 2499.00,
    MOUSE: 89.90,
    TECLADO: 249.00,
    DISCO: 329.00,
}

# --- Cupones -----------------------------------------------------------------
CUPON_VALIDO = "DESCUENTO10"      # 10 % de descuento
CUPON_INVALIDO = "INVALIDO"
DESCUENTO_VALIDO = 0.10

# --- Cliente con datos válidos para el checkout -------------------------------
CLIENTE_VALIDO = {
    "name": "María López",
    "email": "maria@correo.com",
    "address": "Jr. 9 de Octubre 456",
    "city": "Lima",
    "phone": "987654321",
}

MENSAJE_COMPRA_EXITOSA = "¡Compra realizada con éxito!"
MENSAJE_CARRITO_VACIO = "Tu carrito está vacío"


def parse_price(text):
    """Convierte 'S/ 2,499.00' (o '−S/ 249.90') en el número 2499.0 (249.9)."""
    digits = re.sub(r"[^\d.]", "", text)
    return float(digits)


def cliente_con(**cambios):
    """Devuelve una copia del cliente válido con algunos campos modificados."""
    datos = dict(CLIENTE_VALIDO)
    datos.update(cambios)
    return datos
