# language: es
Característica: CP-32 Agregar producto desde la perspectiva del usuario
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-32
  Escenario: CP-32 Agregar producto desde la perspectiva del usuario
    Cuando navego por el catálogo
    Y agrego "Laptop Pro 15" al carrito
    Entonces veo una notificación de que el producto se agregó
    Y el contador del carrito muestra 1
