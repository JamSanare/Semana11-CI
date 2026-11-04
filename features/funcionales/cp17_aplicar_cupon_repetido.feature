# language: es
Característica: CP-17 Aplicar cupón repetido
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-17
  Escenario: CP-17 Aplicar cupón repetido
    Dado tengo "Teclado Mecánico" en el carrito
    Y abro el carrito
    Y tengo aplicado el cupón "DESCUENTO10"
    Cuando aplico el cupón "DESCUENTO10"
    Entonces el descuento no se acumula y el total del carrito es 224.10
