# language: es
Característica: CP-35 Completar checkout con datos normales
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-35
  Escenario: CP-35 Completar checkout con datos normales
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando completo el formulario con datos válidos
    Y confirmo el pago
    Entonces el flujo de compra finaliza con éxito
