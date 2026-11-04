# language: es
Característica: CP-08 Cambiar cantidad a cero
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-08
  Escenario: CP-08 Cambiar cantidad a cero
    Dado tengo "Mouse Inalámbrico" en el carrito
    Y abro el carrito
    Cuando reduzco la cantidad de "Mouse Inalámbrico" hasta cero
    Entonces no veo "Mouse Inalámbrico" en el carrito
    Y el carrito queda vacío
