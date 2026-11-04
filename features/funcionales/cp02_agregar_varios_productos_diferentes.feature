# language: es
Característica: CP-02 Agregar varios productos diferentes
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-02
  Escenario: CP-02 Agregar varios productos diferentes
    Cuando agrego "Laptop Pro 15" al carrito
    Y agrego "Mouse Inalámbrico" al carrito
    Y abro el carrito
    Entonces veo "Laptop Pro 15" en el carrito
    Y veo "Mouse Inalámbrico" en el carrito
    Y el contador del carrito muestra 2
