# language: es
Característica: CP-15 Aplicar cupón inválido
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-15
  Escenario: CP-15 Aplicar cupón inválido
    Dado tengo "Teclado Mecánico" en el carrito
    Y abro el carrito
    Cuando aplico el cupón "INVALIDO"
    Entonces el mensaje del cupón contiene "Cupón no válido"
    Y no se muestra ningún descuento
    Y el total del carrito es 249.00
