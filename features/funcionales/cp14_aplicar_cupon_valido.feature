# language: es
Característica: CP-14 Aplicar cupón válido
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-14
  Escenario: CP-14 Aplicar cupón válido
    Dado tengo "Teclado Mecánico" en el carrito
    Y abro el carrito
    Cuando aplico el cupón "DESCUENTO10"
    Entonces el mensaje del cupón contiene "DESCUENTO10"
    Y el mensaje del cupón contiene "aplicado"
