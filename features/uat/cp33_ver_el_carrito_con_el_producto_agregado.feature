# language: es
Característica: CP-33 Ver el carrito con el producto agregado
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-33
  Escenario: CP-33 Ver el carrito con el producto agregado
    Dado tengo "Teclado Mecánico" en el carrito
    Cuando abro el carrito
    Entonces veo "Teclado Mecánico" en el carrito
    Y la cantidad de "Teclado Mecánico" es 1
    Y el total del carrito es 249.00
