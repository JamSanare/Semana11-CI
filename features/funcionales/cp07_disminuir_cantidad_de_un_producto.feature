# language: es
Característica: CP-07 Disminuir cantidad de un producto
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-07
  Escenario: CP-07 Disminuir cantidad de un producto
    Dado tengo 2 unidades de "Mouse Inalámbrico" en el carrito
    Y abro el carrito
    Cuando disminuyo la cantidad de "Mouse Inalámbrico"
    Entonces la cantidad de "Mouse Inalámbrico" es 1
    Y el total del carrito es 89.90
