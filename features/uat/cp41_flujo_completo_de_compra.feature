# language: es
Característica: CP-41 Flujo completo de compra
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-41
  Escenario: CP-41 Flujo completo de compra
    Cuando agrego "Laptop Pro 15" al carrito
    Y abro el carrito
    Y aplico el cupón "DESCUENTO10"
    Y procedo al pago
    Y completo el formulario con datos válidos
    Y confirmo el pago
    Entonces el flujo de compra finaliza con éxito
    Y el total pagado es 2249.10
    Y el contador del carrito muestra 0
