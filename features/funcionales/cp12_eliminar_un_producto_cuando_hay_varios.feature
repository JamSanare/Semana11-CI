# language: es
Característica: CP-12 Eliminar un producto cuando hay varios
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-12
  Escenario: CP-12 Eliminar un producto cuando hay varios
    Dado tengo en el carrito los productos "Laptop Pro 15", "Mouse Inalámbrico" y "Teclado Mecánico"
    Y abro el carrito
    Cuando elimino "Mouse Inalámbrico" del carrito
    Entonces no veo "Mouse Inalámbrico" en el carrito
    Y veo "Laptop Pro 15" en el carrito
    Y veo "Teclado Mecánico" en el carrito
