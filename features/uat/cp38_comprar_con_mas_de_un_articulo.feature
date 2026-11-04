# language: es
Característica: CP-38 Comprar con más de un artículo
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-38
  Escenario: CP-38 Comprar con más de un artículo
    Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico"
    Y abro el carrito
    Y procedo al pago
    Cuando completo el formulario con datos válidos
    Y confirmo el pago
    Entonces el flujo de compra finaliza con éxito
    Y el total pagado es 2588.90
