# language: es
Característica: CP-05 Ver producto en el carrito
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-05
  Escenario: CP-05 Ver producto en el carrito
    Dado tengo "Teclado Mecánico" en el carrito
    Cuando abro el carrito
    Entonces veo "Teclado Mecánico" en el carrito
    Y la cantidad de "Teclado Mecánico" es 1
