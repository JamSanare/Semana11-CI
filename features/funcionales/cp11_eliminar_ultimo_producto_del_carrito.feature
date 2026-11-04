# language: es
Característica: CP-11 Eliminar último producto del carrito
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-11
  Escenario: CP-11 Eliminar último producto del carrito
    Dado tengo "Laptop Pro 15" en el carrito
    Y abro el carrito
    Cuando elimino "Laptop Pro 15" del carrito
    Entonces el carrito queda vacío
