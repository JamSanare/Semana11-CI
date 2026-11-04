# language: es
Característica: CP-31 Volver al catálogo desde confirmación
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-31
  Escenario: CP-31 Volver al catálogo desde confirmación
    Dado he confirmado una compra de "Disco SSD 1TB"
    Cuando vuelvo al catálogo desde la confirmación
    Entonces veo el catálogo de productos
    Y el contador del carrito muestra 0
    Y puedo seguir comprando agregando "Mouse Inalámbrico"
