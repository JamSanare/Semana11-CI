# language: es
Característica: CP-04 Verificar contador del carrito
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-04
  Escenario: CP-04 Verificar contador del carrito
    Entonces el contador del carrito muestra 0
    Cuando agrego "Teclado Mecánico" al carrito
    Entonces el contador del carrito muestra 1
