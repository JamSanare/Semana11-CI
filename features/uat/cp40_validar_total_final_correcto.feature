# language: es
Característica: CP-40 Validar total final correcto
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-40
  Escenario: CP-40 Validar total final correcto
    Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico"
    Y abro el carrito
    Cuando aplico el cupón "DESCUENTO10"
    Entonces el total coincide con la suma de los productos menos el descuento
    Y el total del carrito es 2330.01
