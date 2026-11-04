# language: es
Característica: CP-13 Actualizar subtotal al eliminar producto
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-13
  Escenario: CP-13 Actualizar subtotal al eliminar producto
    Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico"
    Y abro el carrito
    Cuando elimino "Mouse Inalámbrico" del carrito
    Entonces el subtotal del carrito es 2499.00
