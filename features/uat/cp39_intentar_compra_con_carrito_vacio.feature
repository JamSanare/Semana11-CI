# language: es
Característica: CP-39 Intentar compra con carrito vacío
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @uat @CP-39
  Escenario: CP-39 Intentar compra con carrito vacío
    Cuando abro el carrito
    Entonces la compra se bloquea y veo el aviso de carrito vacío
