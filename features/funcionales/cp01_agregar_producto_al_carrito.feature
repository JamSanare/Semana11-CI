# language: es
Característica: CP-01 Agregar producto al carrito
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-01
  Escenario: CP-01 Agregar producto al carrito
    Cuando agrego "Laptop Pro 15" al carrito
    Y abro el carrito
    Entonces veo "Laptop Pro 15" en el carrito
    Y el contador del carrito muestra 1
