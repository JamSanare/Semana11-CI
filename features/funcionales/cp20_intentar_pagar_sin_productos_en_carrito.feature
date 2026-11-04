# language: es
Característica: CP-20 Intentar pagar sin productos en carrito
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-20
  Escenario: CP-20 Intentar pagar sin productos en carrito
    Cuando abro el carrito
    Entonces veo el aviso de carrito vacío
    Y no existe la opción de proceder al pago
