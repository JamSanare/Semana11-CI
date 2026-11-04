# language: es
Característica: CP-03 Agregar el mismo producto dos veces
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-03
  Escenario: CP-03 Agregar el mismo producto dos veces
    Cuando agrego "Mouse Inalámbrico" al carrito
    Y agrego "Mouse Inalámbrico" al carrito
    Y abro el carrito
    Entonces la cantidad de "Mouse Inalámbrico" es 2
    Y el total del carrito es 179.80
