# language: es
Característica: CP-29 Confirmar compra con varios productos
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-29
  Escenario: CP-29 Confirmar compra con varios productos
    Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico" y "Teclado Mecánico"
    Y abro el carrito
    Y procedo al pago
    Cuando completo el formulario con datos válidos
    Y confirmo el pago
    Entonces veo la pantalla de confirmación
    Y el total pagado es 2837.90
