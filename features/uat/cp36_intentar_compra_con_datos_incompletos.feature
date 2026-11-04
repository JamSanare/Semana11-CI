# language: es
Característica: CP-36 Intentar compra con datos incompletos
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-36
  Escenario: CP-36 Intentar compra con datos incompletos
    Dado estoy en el checkout con "Disco SSD 1TB" en el carrito
    Cuando confirmo el pago sin completar los datos
    Entonces el sistema me guía con mensajes de error claros
    Y no se muestra la confirmación de compra
