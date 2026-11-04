# language: es
Característica: CP-18 Verificar total con descuento
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-18
  Escenario: CP-18 Verificar total con descuento
    Dado tengo "Teclado Mecánico" en el carrito
    Y abro el carrito
    Cuando aplico el cupón "DESCUENTO10"
    Entonces el descuento mostrado es 24.90
    Y el total del carrito es 224.10
