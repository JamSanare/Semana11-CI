# language: es
Característica: CP-10 Eliminar un producto del carrito
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-10
  Escenario: CP-10 Eliminar un producto del carrito
    Dado tengo "Laptop Pro 15" en el carrito
    Y abro el carrito
    Cuando elimino "Laptop Pro 15" del carrito
    Entonces no veo "Laptop Pro 15" en el carrito
