# language: es
Característica: CP-19 Verificar total sin descuento
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-19
  Escenario: CP-19 Verificar total sin descuento
    Dado tengo "Teclado Mecánico" en el carrito
    Cuando abro el carrito
    Entonces no se muestra ningún descuento
    Y el total del carrito es 249.00
