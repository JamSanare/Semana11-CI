# language: es
Característica: CP-16 Aplicar cupón vacío
  Como cliente de TiendaDemo
  Quiero completar este flujo
  Para validar el caso de prueba del registro

  Antecedentes:
    Dado estoy en el catálogo de TiendaDemo

  @funcional @CP-16
  Escenario: CP-16 Aplicar cupón vacío
    Dado tengo "Teclado Mecánico" en el carrito
    Y abro el carrito
    Cuando intento aplicar un cupón vacío
    Entonces el mensaje del cupón contiene "Ingresa un código"
    Y no se muestra ningún descuento
