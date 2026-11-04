# language: es
Característica: CP-34 Aplicar cupón válido
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-34
  Escenario: CP-34 Aplicar cupón válido
    Dado tengo "Laptop Pro 15" en el carrito
    Y abro el carrito
    Cuando aplico el cupón "DESCUENTO10"
    Entonces veo el descuento del 10% reflejado en el resumen del pedido
