# language: es
Característica: CP-06 Aumentar cantidad de un producto
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-06
  Escenario: CP-06 Aumentar cantidad de un producto
    Dado tengo "Laptop Pro 15" en el carrito
    Y abro el carrito
    Cuando aumento la cantidad de "Laptop Pro 15"
    Entonces la cantidad de "Laptop Pro 15" es 2
    Y el total del carrito es 4998.00
