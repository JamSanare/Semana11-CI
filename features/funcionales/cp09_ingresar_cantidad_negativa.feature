# language: es
Característica: CP-09 Ingresar cantidad negativa
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-09
  Escenario: CP-09 Ingresar cantidad negativa
    Dado tengo "Mouse Inalámbrico" en el carrito
    Y abro el carrito
    Cuando intento bajar la cantidad de "Mouse Inalámbrico" por debajo de cero
    Entonces no existe un campo para escribir la cantidad manualmente
    Y el contador del carrito muestra 0
